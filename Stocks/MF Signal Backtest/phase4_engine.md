# Phase 4: Backtest Engine

> **Done:** Nov-12-2026. The simulator runs your exact rules day by day, month by month, with real charges and tax, against 1,000 random portfolios and three SIP benchmarks.
> **Still not done:** no signal strategy (A–D) has been run. The engine was checked only on made-up prices, random portfolios, a placebo signal and the benchmarks. Phase 5 runs the signals once, and the pass/fail rule below is fixed now.

---

## 1. How one month works (`runner.run_portfolio`)

On each action date (first trading day on or after the 11th):
1. **Sell** every buy whose exit has happened (stop-loss, funds selling, or 24 months), at the open.
2. **Pay last financial year's tax** (only once a year has ended).
3. **Add this year's monthly amount**: ₹2,000 in 2014, rising ~7.94% each January to ₹5,000 in 2026.
4. **Buy** the month's pick, in whole shares at the open:
   - the pick is #1, or the next stock if you already hold 3 buys of #1 or one share isn't affordable at the actual open;
   - buy charges are paid on top.
5. **Idle money goes into the small-cap fund** (user decision): leftover rupees, the whole amount in a no-pick month, and sale money plus dividends on the day each buy closes.

**At the end (11-Nov-2026):** buys still open are valued at the last close, the fund is sold, final tax is paid, and XIRR is computed on what you put in vs what you end with.

## 2. One buy (`engine.simulate_lot`)

| Rule | How it's applied |
|---|---|
| Stop-loss ladder | Starts at −10%. Peak +15% → stop +5%, +20% → +10%, +25% → +15%, +30% → +20%, +40% → +30%, then 10-point steps (5-point variant available) |
| Order within a day | The day's **low** is checked against the stop set by *earlier* days' highs; the day's high only raises the stop afterwards (conservative) |
| Gap below the stop | Filled at the **open** (worse than the stop) |
| Funds selling | A newer portfolio month flags the stock → sell at that action date's open |
| 24-month cap | Sell at the open of the first trading day on or after entry + 24 months |
| Delisted / suspended > 180 days | Closed at the last traded close |
| Prices | Split/bonus/demerger-adjusted; dividends credited |

## 3. Money, charges and tax (`engine.Book`)

- **Charges (in rupees):**
  - STT 0.1% each side, stamp duty 0.015% on buy, NSE + SEBI fees with 18% GST;
  - **₹15.93 depository charge per sale**, ₹0 brokerage;
  - that's ₹5.93 on a ₹5,000 buy and ₹21.11 on a ₹5,000 sale.
- **Capital-gains tax (today's rules, every year):**
  - short-term (≤ 12 months) 20%, long-term 12.5% above ₹1.25 lakh a year, plus 4% cess;
  - losses set off (short-term against both kinds, long-term only against long-term) and carried forward;
  - each buy is taxed on its own holding period.
- **Dividends** are taxed at 31.2% (30% slab + cess, a conservative assumption).
- **Idle money in the small-cap fund:**
  - proxy = Nifty Smallcap 250 total-return index less a 0.3% yearly fee, plus 0.005% stamp duty on each purchase;
  - yearly tax is paid by selling the oldest fund units, and those sales are taxed too;
  - the fund is sold at the end and taxed.

## 4. Benchmarks (same ₹2,000 → ₹5,000 monthly amounts, same dates, post-tax)

| SIP into… | Post-tax XIRR | ₹5.09 lakh invested became |
|---|---|---|
| Nifty 500 index fund (0.2% fee) | **12.25%** | ₹10.4 lakh |
| 6 flagship funds, equal split (direct plans: HDFC Flexi Cap, SBI Flexicap, Nippon Multi Cap, ABSL Flexi Cap, DSP Flexi Cap, Parag Parikh Flexi Cap) | **14.42%** | ₹11.9 lakh |
| Small-cap index fund (0.3% fee), i.e. where your idle money goes | **14.69%** | ₹12.2 lakh |
| (info) Nifty 50 / Midcap 150 | 10.94% / 16.32% | |

Individual funds: Parag Parikh 15.9%, HDFC 15.8%, Nippon 15.1%, ABSL 14.2%, DSP 13.4%, SBI 11.7%.

## 5. What the engine showed about your rules (random stocks, not signals)

- A random buy lasts a **median ~29 days**, and **97% of exits are stop-losses** (including trailing stops that lock in profit).
- With −10% on stocks that move 2–4% a day, most buys are closed within weeks.
- The average random buy makes **+0.5% after charges**, essentially luck.
- So your portfolio is mostly the small-cap fund plus a stream of short trades:
  - random portfolios end at a **median 14.44% XIRR**, with a 5th–95th percentile range of only 14.2–14.7%;
  - that's just below the small-cap SIP (14.69%) because of trading charges and short-term tax.
- **Implication:** XIRR barely separates good and bad stock picking, which is why pass/fail uses **average return per buy**.

## 6. Pass/fail rule (fixed now, before any signal is run)

A signal **passes only if all four hold**:

| Gate | Test |
|---|---|
| **G1** | Its **average post-cost return per buy beats ≥ 95% of 1,000 random portfolios**. Each random portfolio buys a random eligible stock from the same liquidity quintile in the same months, under the same rules. Also reported: t-stat of (signal buy − random average that month), clustered by stock |
| **G2** | Above the random median in **both halves** (buys in 2014–19 and in 2020–26) |
| **G3** | Still above the random median **after removing its 10 best buys** |
| **G4** | **Post-tax XIRR beats all three SIPs**: Nifty 500, the 6 flagship funds, and the small-cap fund itself |

**The bar:** random portfolios average between −1.4% and +2.4% per buy (5th–95th percentile). So G1 needs roughly **+2.4% or more per buy**.

## 7. Verification

| Check | Result |
|---|---|
| 19 hand-built price paths (each stop level, gap fill, same-day high and low, 5-point variant, funds selling, 24-month cap, delisting, charges, tax set-off and carry-forward, XIRR) | **19/19 pass** (`scripts/test_engine.py`) |
| Real trades hand-checked against raw prices (Radico's Apr-2014 lower circuit filled at the gap-down open; Lloyd Electric's Feb-2016 −10% stop filled exactly) | ✔ |
| Pick order: #1 each month, #2 when 3 buys of #1 are held, first affordable when #1 costs more than the budget | **155/155 months** correct |
| **Placebo signal** (random picks pretending to be a signal) | 65th percentile, t = 0.4, **fails** G1/G3/G4, as it should |
| Random portfolios vs small-cap SIP | 14.44% vs 14.69%; the gap matches the expected charges and tax |
| Speed | 1,000 random portfolios ≈ 2 minutes per signal |

## 8. Simplifications to know about

1. **Dividends** are credited when the buy is closed, not on the ex-date (small timing effect on XIRR).
2. **Tax is per buy**, using its own dates. Strict FIFO only differs when several buys of one stock are open together.
3. **The small-cap fund is an index proxy.** A specific active small-cap fund's real NAV can replace it.
4. **Demergers are value-neutral and rights are ignored** (as in Phase 2).
5. **Surcharge is ignored**, and the 30% slab is assumed for dividends.

## Files

`scripts/engine.py` (per-buy simulator, accounting, tax, XIRR) · `scripts/runner.py` (monthly loop, small-cap parking, pickers, random universe, SIP benchmarks) · `scripts/evaluate.py` (1,000-run comparison and the four gates) · `scripts/test_engine.py` (19 tests) · `data/processed/fund_nav.parquet` (6 flagship funds' daily NAV)
