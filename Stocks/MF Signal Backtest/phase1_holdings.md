# Phase 1: Fund Holdings Table

> **Done:** Nov-12-2026. All six pilot fund houses' monthly portfolios from 2013 to Oct-2026 are downloaded, parsed and cleaned into one table.
> **Result:** 645,937 scheme-level holdings. Rolled up, that's 231,592 rows of "fund house × company × month". **Window coverage: 152–155 of 155 months per fund house.**

---

## 1. What was built

| Step | Script | Output |
|---|---|---|
| Collect file links | `harvest_links.py` (Nippon, DSP, PPFAS pages)<br>`hdfc_links.py` (HDFC API)<br>browser extraction (SBI API, ABSL page) | `data/raw/links_<amc>.csv` |
| Download | `download.py` (parallel per fund house, resumable) | **2,400 files, 1.4 GB, 0 failures**, in `data/raw/files/` |
| Parse | `parse_holdings.py` | 81,680 sheets, 1.55 M equity rows<br>`data/interim/holdings_raw.parquet` |
| Classify schemes | `classify_schemes.py` | `data/interim/schemes.csv`: **226 of 2,275 schemes are active equity** |
| Clean and roll up | `build_holdings.py` | `data/processed/holdings_scheme.parquet` (12.5 MB)<br>`data/processed/holdings_amc.parquet` (4.4 MB)<br>`checks.csv`, `relabelled_months.csv` |

`data/` is git-ignored. Everything can be rebuilt from the scripts in this order.

### Output columns

- **`holdings_scheme`**:
  - `amc, ym, scheme_key, scheme_raw`: fund house, month, scheme
  - `isin, issuer, name, industry`: the stock
  - `qty`: number of shares held
  - `mv_lakhs`: market value in ₹ lakh
  - `pct`: % of the scheme's NAV, as a percent (8.56 = 8.56%)
- **`holdings_amc`**: per fund house, company and month:
  - `qty`, `mv_lakhs`: total shares and value across all its active equity schemes
  - `n_schemes`: how many of its schemes hold the stock
  - `max_pct`: the largest weight in any one scheme
  - `issuer` = first 7 characters of the ISIN (e.g. `INE090A` = ICICI Bank). It stays the same through splits and face-value changes.

---

## 2. Coverage

| Fund house | Months in file | Window months (Dec-13 → Oct-26, 155) | Active-equity schemes | Median schemes / month | Median stocks / month |
|---|---|---|---|---|---|
| HDFC | 158 | **155** | 47 | 13 | 244 |
| Aditya Birla SL | 159 | **155** | 56 | 22 | 308 |
| DSP | 165 | **155** | 27 | 11 | 225 |
| PPFAS | 161 | **155** | 6 | 2 | 25 |
| Nippon | 162 | **153** | 35 | 16 | 300 |
| SBI | 153 | **152** | 52 | 19 | 255 |

**5 months the fund houses never published online:**
- **Nippon:** Jun-2021 and Jan-2022 (only the debt file is posted for Jan-2022).
- **SBI:** Dec-2015, Apr-2016 and Jul-2018.

Signals will compare against the last available month and flag the gap.

**Breadth:**
- 1,280 different companies were held at some point in the window.
- In a typical month, about 600 companies are held by at least one pilot fund house, and **about 365 by two or more**. That's plenty of material for the "group buying" signal.

**Size check (₹ thousand crore in active equity):**

| | Dec-2013 | Oct-2026 |
|---|---|---|
| HDFC | 30 | 418 |
| SBI | 13 | 372 |
| Nippon | 23 | 304 |
| Aditya Birla | 10 | 141 |
| DSP | 9 | 110 |
| PPFAS | 0.2 | 118 |

The growth matches the industry's known path.

**Spot checks against known portfolios:**
- SBI Bluechip, Dec-2019: HDFC Bank 9.7%, ICICI Bank 7.3%, ITC, L&T.
- HDFC Flexi Cap, Oct-2026: ICICI Bank 9.3%, HDFC Bank, Axis Bank, SBI.
- PPFAS Flexi Cap: HDFC Bank, Power Grid, ITC, ICICI Bank.

---

## 3. Which schemes count as "active equity"

A scheme counts only if, in at least 60% of the months it appears, it meets all three tests:
1. **Name** has no index / ETF / debt / hybrid / arbitrage / fund-of-funds / foreign / closed-ended ("Series", "1126D", "Close-ended", RGESS) marker.
2. **Indian equity** is at least 75% of NAV. For PPFAS the bar is 60%, because its funds may hold up to 35% foreign shares.
3. **Bonds, T-bills and other Indian debt instruments** are at most 10% of NAV. This rules out hybrids, which don't always say "hybrid" in the name.

The decision is made **once per scheme**, not month by month. Otherwise a fund that drifts around a threshold would flicker in and out, and look like the fund house buying or selling everything it holds.

**Kept:** large, mid and small cap; flexi and multi cap; focused; value and contra; dividend yield; ELSS tax-saver; sector and thematic funds; equity-oriented retirement plans; quant funds.

**Dropped:** index funds and ETFs (no manager decision), arbitrage funds (hedged positions), hybrids and balanced funds, closed-ended "Series" funds (forced selling at maturity would look like a sell signal), fund-of-funds and international funds.

**Renames don't matter.** Many schemes changed names (e.g. PPFAS "Long Term Value" → "Long Term Equity" → "Flexi Cap"; SEBI's 2018 and 2025 recategorisations). Signals are measured at fund-house level, so moving shares between a fund house's own schemes cancels out.

---

## 4. Problems found and fixed

| # | Problem | Fix |
|---|---|---|
| 1 | Link file names use every date style ("December_31_2023", "july-31st-2023", "31122014", "31-Oct-26"); early parsing misread some | Rewrote the date parser and dropped mid-month (fortnightly) files |
| 2 | Nippon's "with-Riskometer" monthly files were filtered out as risk reports | Narrowed the filter to "risk-parameter" files only |
| 3 | HDFC changed format three times: one workbook (to 2020), equity/debt split (2020–Jul-2021), one file per scheme (Aug-2021 on) | API pulled per year and per month. Per-scheme files take the month that was requested. "Other than Debt Schemes" files are no longer dropped |
| 4 | HDFC's "Coupon (%)" column was read as "% of NAV", giving 0% weights | Coupon, yield and ESG columns are ignored when finding columns |
| 5 | Some Aditya Birla sheet titles have no "Fund" word (e.g. "Dividend Yield Plus") | Fall back to the workbook's code→name Index sheet, then to the first title line |
| 6 | PPFAS Mar-2021 (and similar) leave the ISIN column **unlabelled** | Find the column whose values look like ISINs and realign the other columns |
| 7 | **DSP's "jan2016" zip actually holds the Jan-2017 portfolio.** That made Jan-2016 look about 2× too large and Jan-2017 look missing | Each sheet's printed "Portfolio as on …" date now overrides the link's month. This affected only that one file (16 sheets) |
| 8 | ELSS ("Equity Linked **Savings** Scheme") and retirement equity plans were dropped by the word "savings" / "retirement" | Those words removed from the exclusion list; the equity % and bond % tests decide instead |
| 9 | Old Nippon "R\*Shares" ETFs slipped past the ETF filter | Added `R*Shares` / `CNX` patterns |
| 10 | 20 files can't be parsed | All are non-portfolio files picked up by the link filter (DSP fund-performance, HDFC overlap, Nippon risk/web-link files). Each month's real portfolio file is present |

**Integrity checks passed:**
- No scheme is counted twice in a month under two names (checked by searching for identical holdings).
- No downloaded file is corrupt.
- Month-on-month jumps in scheme count, stock count or value are all explained by real events: PPFAS launching new funds, and the 5 unpublished months.

---

## 5. Known limitations carried into Phase 2/3

1. **Share counts change with splits and bonuses.** A 1:5 split multiplies `qty` by 5 without any buying. Before measuring "fund house bought more", `qty` must be adjusted using NSE's corporate-action list (Phase 2). `issuer` already keeps the company identity stable.
2. **Fund-house totals grow with inflows.** When money flows in, funds buy more of everything they already hold. So "added to an existing holding" should be judged by **weight change** or **qty growth above the fund house's overall growth**, not raw qty. A **brand-new position** is the cleanest signal.
3. **Month-end snapshots only.** Trades made and reversed within a month are invisible, and month-end portfolios may be tidied up ("window dressing").
4. **Disclosure timing is assumed** to be the 10th of the following month (SEBI deadline). Actual upload dates aren't recorded in most archives.
5. **Names are not cleaned** (e.g. "HDFC Bank Ltd.£"). This is harmless, because joins use ISIN/issuer. Display names will come from NSE data in Phase 2.
