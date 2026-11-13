# Phase 2: Prices, Corporate Actions and Benchmarks

> **Done:** Nov-12-2026. Daily NSE prices for every listed company from Nov-2013 to Nov-2026, adjusted for splits, bonuses and demergers, with dividends. Also: total-return benchmarks, and fund share counts converted to split-adjusted units.

---

## 1. What was built

| Step | Script | Output (`data/processed/`) |
|---|---|---|
| Daily price files (NSE bhavcopy) | `download_prices.py` | 3,210 trading days. Old format to 5-Jul-2024, new UDiFF format from 8-Jul-2024. 189 weekdays had no file, about 14–15 a year, which matches NSE holidays |
| Corporate actions | NSE `corporates-corporateActions` API (no browser needed) → `corp_actions.py` | `corp_actions.parquet`: 28,577 records → 16,603 dividends, 463 splits, 481 bonuses, 2 consolidations, 155 demerger/arrangement entries, 25 zero-premium rights |
| Raw prices | `build_prices.py` | `prices_raw.parquet`: **5.96 M rows, 3,706 companies**, equity series EQ/BE/BZ/BT/SM/ST |
| Adjusted prices | `build_prices.py` + `manual_corp_actions.csv` | `prices_adj.parquet`: adjusted open/high/low/close, dividend per adjusted share, daily total return, total-return index |
| Benchmarks | niftyindices.com `getTotalReturnIndexString` | `index_tri.parquet`: **Nifty 500, Nifty 50, Midcap 150, Smallcap 250 total-return indices**, Jan-2013 → Nov-2026 |
| Fund share counts | `adjust_holdings.py` | `holdings_amc` / `holdings_scheme` gain `qty_adj` (in today's share units), `symbol`, `listed`, `close_me` |

**Rebuild order:** `download_prices` → `corp_actions` → `build_prices` → `adjust_holdings`.

---

## 2. How prices are adjusted

- **Company key** = `issuer` (first 7 characters of the ISIN). It survives ticker renames and the new ISIN issued at a split.
- **Splits, bonuses, consolidations:**
  - Factor = old ÷ new face value (split) or (a+b)/b (bonus a:b).
  - Adjusted price = raw price ÷ product of all factors with ex-date *after* that day. Today's prices stay unchanged; older prices are scaled down.
- **Demergers / schemes of arrangement:** the factor is measured as previous close ÷ ex-day open. It's applied only when the drop is 3–400%, so ordinary mergers with no price drop are ignored. This treats the spin-off as value-neutral, as if the new company's shares were kept.
- **Dividends:** credited on the ex-date (`adj_div`). The total-return index reinvests them.
- **Rights issued at face value:** these adjust the price only, and only when the ex-day price gap confirms the ratio. They do **not** change fund share counts, because shares come only to those who pay for them.
- **Long suspensions:** no return is counted across a trading gap of more than 180 days (relisting, or a dormant ISIN reused).

### Validation

| Check | Result |
|---|---|
| Split/bonus factor vs actual ex-day price gap (within 15%) | **98.7% of 894 events.** The 3 misses on fund-held stocks are explained: first day of data (Ashiana), a genuine +17% move on the ex-day (VST), and a small stock |
| Infosys spot check | All three 1:1 bonuses (Dec-2014, Jun-2015, Sep-2018) applied. The adjusted series has no artificial jump (largest daily move 16%, real) |
| Big unexplained moves on fund-held stocks (>+50% / <−40% in a day) | 37 at first → **10 left, all real events**: Yes Bank's Mar-2020 collapse and rescue, Jet Airways, DHFL, Amtek Auto, RCOM, South West Pinnacle, and relistings after 75–88-day suspensions |
| Fund-house holdings spanning a split/bonus: share count jumps >40% | **87% raw → 22.5% adjusted.** Ordinary months run at 7.9%. Only 31 of 1,099 remaining jumps equal the split ratio; the rest are real trades, often a re-entry months or years later |

### Bugs found and fixed in NSE's feed

1. **2016–17 abbreviations:** "Fv Splt Frm Rs 10 To Re 1". This hid splits in JSW Steel, Solar Industries, Karur Vysya, KNR, Gulshan Polyols, ICIL and KPR Mill.
2. **Dividend and split in one line:** "Interim Div Rs 6 + Split from Rs 10 to Re 1" was read as a 6× split. Split numbers are now read only after the word "split".
3. **Split wording without "Rs":** "Split From 10/- To Face Value 2/-".
4. **Debenture, NCRPS and preference "bonuses"** are excluded; they don't create equity shares.
5. **Nine reviewed events missing from or mislabelled in the feed** are in `scripts/manual_corp_actions.csv`, each with a note:
   - Strides special dividend (2013), Future Retail (2016), LT Foods split (2017), Sintex demerger (2017), GFL demerger (2019), Suven demerger (2020), Majesco special dividend (2020), NXTDIGITAL (2022), Mirza/RedTape demerger (2023);
   - their factor is measured from the price gap.

---

## 3. Benchmarks (total return, dividends reinvested)

| Index | Jan-2013 | Nov-2026 | ≈ CAGR |
|---|---|---|---|
| Nifty 500 TRI | 6,621 | 38,424 | ~13.5% |
| Nifty 50 TRI | 7,651 | 38,474 | ~12.3% |
| Nifty Midcap 150 TRI | 3,026 | 29,126 | ~17.8% |
| Nifty Smallcap 250 TRI | 3,031 | 23,008 | ~15.9% |

The **Nifty 500 TRI** is the main benchmark. Midcap and Smallcap help tell whether a result is stock-picking or just small/mid-cap exposure.

---

## 4. Fund holdings after Phase 2

- `qty_adj`: every month-end share count expressed in today's share units. **Month-to-month changes now reflect real buying and selling**, not splits.
- 99.0% of fund-house holdings map to an NSE ticker.
- 95.6% traded on NSE within 10 days of the month-end. The other 4.4% are suspended, delisted, BSE-only, or not yet listed (IPO allotments reported before listing). These can't be bought on NSE, so Phase 3 will skip them as candidates.

---

## 5. Known limitations

1. **Demergers are treated as value-neutral.** In reality you'd receive the new company's shares and could hold or sell them. The total-return effect is the same, but the backtest won't model selling the spin-off separately.
2. **Rights issues at a premium are ignored.** They cause a small price drop for holders who don't subscribe. Few events, small effect.
3. **Market-cap buckets aren't built yet.** The random-stock control needs "same size bucket". Phase 3 will use traded value as a size proxy, or AMFI's half-yearly large/mid/small-cap lists (2018+), which need downloading.
4. **NSE only.** BSE-only companies held by funds have no prices here and are excluded as candidates.
5. **Corporate-action ex-dates are assumed correct in NSE's feed.** A misdated event would show up as a price-gap mismatch, and 98.7% match.
