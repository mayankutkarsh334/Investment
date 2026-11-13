# Phase 0 — Data Audit

> **Done:** Nov-12-2026. Checked 12 fund houses' archives (through AMFI's official links), downloaded 15 sample portfolio files plus NSE price, index and corporate-action samples. Inspected with `scripts/inspect_samples.py`.
> **Verdict:** Workable. **6 fund houses** can be pulled with plain direct links from late 2012 / 2013, with ISINs, share quantities and % of NAV. That's enough for a real multi-fund-house pilot. **Recommended test window: Dec-2013 → Oct-2026 (~13 years, ~155 monthly picks).**

---

## 1. Fund-house archives

Links come from AMFI's portfolio-disclosure page, which points to each fund house's official archive.

| Fund house | Archive starts | ISINs from | Format | How to download | Pilot? |
|---|---|---|---|---|---|
| **HDFC** | **Jan-2007** (partial 2005–06) | **Sep-2012** (2007–Aug-2012 = company names only) | `.xls` one workbook/month to ~2025, then **one `.xlsx` per scheme** | Direct links on `files.hdfcfund.com`; list from the page's year picker | ✅ |
| **SBI** | **Nov-2013** | Nov-2013 | `.xlsx` one workbook/month (equity+debt; FMPs separate) | Direct links `sbimf.com/docs/default-source/scheme-portfolios/…` | ✅ |
| **Nippon India** (ex-Reliance) | **Sep-2012** | Sep-2012 | `.xls` one workbook/month | Direct links `…/FactsheetsDocuments/Reliance-Monthly-Portfolios-DD-MM-YYYY.xls` | ✅ |
| **Aditya Birla SL** | **Oct-2012** (2009–12 zips = close-ended/FMP only) | Oct-2012 | `.zip` → one `.xls`, one sheet per scheme | Direct links `…/monthly-portfolio/monthly-portfolio-<mon>-<yyyy>.zip` | ✅ |
| **DSP** | **Jan-2013** (Sep–Dec-2012 entries point to the Jan-2013 file) | Jan-2013 | `.zip` → `.xls` (open-ended + a close-ended file) | Direct links on `dspim.com` | ✅ |
| **PPFAS** | **Jun-2013** (fund launched May-2013) | Jun-2013 | `.xls`, 1 sheet | Direct links `amc.ppfas.com/downloads/portfolio-disclosure/…` | ✅ (one vote; ~25 Indian stocks) |
| **ICICI Prudential** | **Jan-2013** (FY12-13 has Jan–Mar 2013 only) | not yet sampled | — | Site's download API; links are created by the page's code, so this **needs a browser session** | Phase 6 |
| **Axis** | **2012** (Nov-2012 confirmed) | not yet sampled | — | Site's year/month picker; **needs a browser session** | Phase 6 |
| **UTI** | **2014** (month not checked) | not yet sampled | — | Form-based picker; **needs a browser session** | Phase 6 |
| **Franklin Templeton** | ~Sep-2021 listed (one stray Dec-2019) | — | — | Older months may sit behind a date filter, not checked | ❌ too short |
| **Kotak** | **Only the last ~4 months** shown on the site | — | — | Older months aren't published online | ❌ |
| **Mirae Asset** | **Latest month only** | — | — | Older months aren't published online | ❌ |

**No central dataset exists.** AMFI's "Portfolio Disclosure" page only links to each fund house's own page.

### What the files contain (samples inspected)

| Sample | Sheets | Rows with ISIN | Header row (holdings table) |
|---|---|---|---|
| HDFC Jan-2007 | 45 | **0** | Name of Instrument · Industry · Quantity · Market value · % to NAV |
| HDFC Dec-2011 | 40 | **0** | (names only) |
| HDFC Sep-2012 | 40 | 1,813 | ISIN · Name · Industry · Quantity · Value · % to NAV |
| HDFC Oct-2026 (Flexi Cap only) | 1 | 85 | ISIN · Coupon · Name · Industry · Quantity · Value · % to NAV · Yield |
| SBI Nov-2013 | 43 | 1,130 | Name · ISIN · Quantity · Market value · Rating · Industry · % to NAV |
| SBI Oct-2026 | 120 | 5,388 | Name · ISIN · Industry · Quantity · Value · % to AUM · YTM · ESG scores |
| Nippon Sep-2012 | 113 | 2,103 | ISIN · Name · Industry · Quantity · Value · % to NAV |
| ABSL Oct-2012 | 127 | 2,487 | Name · ISIN · Industry · Quantity · Value · % of net assets |
| DSP Jan-2013 | 25 (+42 close-ended) | 907 | Sr · Name · ISIN · Industry · Quantity · Value · % to net assets |
| PPFAS Jun-2013 | 1 | 15 | Sr · Name · ISIN · Industry · Quantity · Value · % to NAV |

---

## 2. Parsing issues found (each must be handled in Phase 1)

1. **Column order differs** by fund house and by year. → Find the header row by keywords (ISIN, Quantity, % to NAV), not by fixed position.
2. **% of NAV is sometimes a fraction and sometimes a percent.** Nippon and PPFAS use fractions (0.0542), HDFC and ABSL use percents (8.56). → Normalise per scheme so the weights sum to ≈100.
3. **Sheet names are scheme codes** (`RGF`, `MEF`, `ADVG`, `HDFCEQ`). → Each workbook has an `Index`/`Schemes` sheet mapping code → scheme name; use it.
4. **One workbook mixes every scheme type**: equity, debt, liquid, FMPs, ETFs, index funds, arbitrage, fund-of-funds. → **Keep only actively managed equity schemes** (large, mid, small, flexi/multi, focused, value/contra, ELSS, sector/thematic). **Exclude index funds and ETFs** (no manager decision), arbitrage funds (hedged, not a bet on the stock) and fund-of-funds.
5. **A company's ISIN changes after a split or face-value change.** Example: ICICI Bank `INE090A01013` → `INE090A01021` after its Dec-2014 split. → Identify the company by the **issuer part of the ISIN** (`INE090A`) for equity shares (security code `01`), not by the full ISIN, so a split doesn't look like "funds sold the stock".
6. **HDFC switched to one file per scheme** (about 100+ files a month) in recent years. That means more downloads, but each file is simple.
7. **HDFC 2007–Aug-2012 have no ISINs.** Using them would mean matching company names, including old names (e.g. "Infosys Technologies Ltd"). → **Not worth it**: HDFC would be the only fund house in that period, so there could be no cross-fund-house signal. Excluded.
8. **Scheme mergers and renames (2018 SEBI recategorisation)**: **not audited yet**. → Phase 1 builds a scheme-identity table (code + name over time) and flags discontinuities.

---

## 3. Prices, corporate actions and benchmark

| Item | Finding | Verified |
|---|---|---|
| **Daily prices: old format** (`cm<DD><MON><YYYY>bhav.csv.zip`) | 1995 → Jul-2024. Has OHLC, volume, value traded, **ISIN** (in 2012 files). About 1,450 EQ-series stocks in 2014. | ✅ 2012, 2014, Jul-2024 downloaded |
| **Daily prices: new format** (`BhavCopy_NSE_CM_0_0_0_<YYYYMMDD>_F_0000.csv.zip`) | Jul-2024 → today. Different column names (`TckrSymb`, `ClsPric`, `ISIN` …). About 2,700 EQ stocks in Oct-2026. | ✅ Nov-2024, Oct-2026 downloaded |
| **Split / bonus adjustment** | NSE's `PREVCLOSE` is **not** adjusted on the ex-date. ICICI Bank on 04-Dec-2014: PREVCLOSE 1794.1, close 362.2. So adjustments can't be read from the price file. | ✅ |
| **Corporate actions list** | NSE's `api/corporates-corporateActions` returns splits, bonuses and dividends with ex-dates (e.g. ICICIBANK split 04-Dec-2014, INFY bonus 1:1 02-Dec-2014). **Needs a browser session** (cookie-gated). | ✅ |
| **Benchmark: Nifty 500** | Daily `ind_close_all_<DDMMYYYY>.csv` has the Nifty 500 price index plus dividend yield (named **"S&P CNX 500"** in 2012). | ✅ |
| **Nifty 500 TRI** (total-return index, dividends reinvested) | Not yet pulled. niftyindices.com publishes TRI history. Fallback: price index + daily dividend yield. | ❌ verify in Phase 2 |
| **Fund NAVs** (for the "SIP into the fund" comparison) | AMFI NAV history (public) / `captn3m0/historical-mf-data` | not checked; low risk |

---

## 4. Decision: pilot set and window

**Pilot fund houses (6), all with direct download links and ISINs:**
**HDFC · SBI · Nippon · Aditya Birla SL · DSP · PPFAS**
— 4 of the 5 largest equity fund houses plus 2 independent-minded smaller ones.

**Test window: Dec-2013 → Oct-2026.**
- All 6 fund houses are available from Nov-2013 (SBI is the last to start).
- A signal is first computed from the Dec-2013 holdings (it needs the previous month to see what changed), so the first trade is in mid-Jan-2014.
- About 13 years and **~155 monthly picks**.
- *Trade-off:* starting at Oct-2012 would add ~13 months but only with 3–5 fund houses. Not worth the inconsistency.

**Signal thresholds with 6 fund houses** (each house = one vote):
- **Group buying (A):** ≥ 2 houses (variant ≥ 3).
- **"Funds start selling" exit:** ≥ 2 houses cut or exit.

**Phase 6 additions:** ICICI (Jan-2013), Axis (2012) and UTI (2014). Each needs a browser-session downloader, which is more work but no blocker.

**Dropped:** Kotak and Mirae (no history online). Franklin (only ~2021+ visible). HDFC 2007–2012 (no ISINs, single fund house).

---

## 5. Rough data volume

| Source | Files | Note |
|---|---|---|
| HDFC | ~155 monthly workbooks + per-scheme files for recent years (~100/month) | Biggest effort |
| SBI, Nippon, ABSL, DSP, PPFAS | ~155 each ≈ 775 | One workbook (or zip) per month |
| NSE daily prices | ~3,200 trading days | ~60–200 KB each |
| NSE corporate actions | ~13 yearly API pulls | Browser session |
| Index closes | ~3,200 daily files, or one niftyindices pull | |

Raw data goes to `data/raw/` (git-ignored). Scripts go to `scripts/`. Downloaded files are opened with `.venv/bin/python -I` only.
