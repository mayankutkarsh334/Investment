# MF-Signal Stock Backtest — Study Plan

> **Question:** If I buy stocks that mutual funds are buying, then manage each trade with a fixed stop-loss ladder, do I beat (a) the index and (b) the same rules applied to *random* stocks — after costs and tax?
>
> **Status:** Phases 0–6 done Nov-13-2026. **Final result:** B (biggest bets) beats random stocks consistently — replicated on independent fund houses (ICICI, Axis, UTI: 99.9th pct) — but under the user's rules its post-tax XIRR ties/trails a plain small-cap SIP (14.50% vs 14.56%); C (the original idea) is rejected. See [phase5_results.md](phase5_results.md) and [phase6_results.md](phase6_results.md).

---

## 1. Why this study exists

The idea: a fund holds 50+ stocks, so even a great pick is only 1–3% of its money. Copy the picks directly in a concentrated portfolio and keep more of the upside.

Two things have to be true for that to work, and they are tested **separately**:

1. **The entry signal has an edge.** Stocks that funds are buying go up more often than chance. *(If this fails, no exit rule can rescue it. For a stock with no trend, a stop-loss or trailing stop only changes the pattern of wins and losses, not the average, and trading costs make the average negative.)*
2. **The exit rules capture that edge.** Given the edge exists, which stop and exit rules turn it into the most profit after tax.

---

## 2. Data window and sources

| Data | Source | Range | Verified |
|---|---|---|---|
| Daily OHLC prices (incl. delisted stocks) | NSE price files (bhavcopy): old format to Jul-2024, new UDiFF format after; both include ISIN | 1995 → today | ✅ 2012, 2014, 2024, 2026 samples checked |
| Monthly MF holdings — **pilot: HDFC, SBI, Nippon, Aditya Birla SL, DSP, PPFAS** | Each fund house's own archive (direct download links) | ISINs from Sep-2012 … Nov-2013 (SBI last) | ✅ Phase 0: samples downloaded and parsed |
| Monthly MF holdings — ICICI, Axis, UTI (Phase 6) | Fund house sites; links only appear after the page's code runs, so they need a browser session | Jan-2013 / 2012 / 2014 | ✅ archive depth checked; downloader not built |
| Not usable | Kotak (last ~4 months only), Mirae (latest month only), Franklin (~2021+), HDFC 2007–Aug-2012 (no ISINs) | — | ❌ dropped |
| Corporate actions (splits, bonuses, dividends) | NSE `api/corporates-corporateActions` (needs a browser session); `PREVCLOSE` in the price file is **not** adjusted | 2013 → today | ✅ |
| Benchmark | Nifty 500 price index + dividend yield from NSE daily index files ("S&P CNX 500" in 2012); TRI from niftyindices.com | 2012 → today | ✅ price index · ❌ TRI to verify |

Full details: [data_audit.md](data_audit.md).

**There is no central free dataset.** Each fund house publishes its own files in its own layout, and older files often have **no ISIN** (company names only). The open-source [mf-portfolio](https://github.com/captn3m0/mf-portfolio) project tried to build one, but it's unfinished and has no published data.
| Corporate actions (splits, bonus) | NSE corporate-action archive, or derived from the price file's PREVCLOSE vs the prior day's CLOSE | — | ❌ to verify |
| Benchmark | Nifty 500 TRI (niftyindices.com) | 1995 → today | ❌ to verify |

**Why not 30 years:** stock-level monthly MF holdings aren't publicly archived before about 2012. **Test window: Dec-2013 → Oct-2026 (about 13 years, ~155 monthly picks)**, the period when all 6 pilot fund houses have ISIN-tagged files. It covers the 2015–16 slowdown, the 2018 midcap crash, the 2020 Covid crash and the 2024–25 correction, but it's mostly a bull market, so results are compared against random stocks over the **same** dates, not just against zero.

---

## 3. Trading rules (user-confirmed)

### 3.1 Entry
- **Signal date** = month-end of the disclosed portfolio.
- **Earliest action** = the portfolio becomes public about 10 days after month-end.
- **Buy** at the **open of the first trading day after the 10th** of the following month. No look-ahead.

### 3.2 Entry signals (each tested separately)

| ID | Signal | Logic |
|---|---|---|
| **A** | **Group buying** | Stock newly added or increased by ≥ N **fund houses** in the same month (N = 2, 3; each fund house counts once however many of its schemes buy) |
| **B** | **Biggest bets** | Stock among a fund's top-5 weights, or ≥ 2× its benchmark weight (an above-benchmark "active" bet) |
| **C** | **Small positions** *(the original idea)* | Stock held at < 2% weight |
| **D** | **Steady buying** | Total fund shares held up for ≥ 2 or 3 months in a row |

### 3.3 Exit — the first of these to trigger

**1. Stop-loss ladder (user-confirmed).** It is based on the highest price reached since entry.

| Highest gain reached | Stop-loss moves to |
|---|---|
| Entry | **−10%** |
| +15% | **+5%** |
| +20% | **+10%** |
| +25% | **+15%** |
| +30% | **+20%** |
| +40% | **+30%** |
| +50%, +60% … | 10 points below each new 10-point step |

**2. Funds start selling.** This is checked at each monthly disclosure and acted on at the next possible open. Default definition: **≥ 2 fund houses holding the stock cut or exit it in the same month, OR total fund shares held fall ≥ 20% month-on-month**. Variants: ≥ 3 fund houses (once more fund houses are added); ≥ 10% fall.

**3. Time cap.** Sell at **24 months** whatever happens (user's maximum hold).

### 3.4 How fills are simulated (conservative)
- The stop is checked against the **day's low**. Fill at the stop price, or at the **open if the price gapped below** the stop.
- The peak is updated from the **day's high**, but only **after** that day's stop check. On a day that hits both a new high and the stop, assume the stop hit first.
- A stock that is delisted or suspended exits at its last traded price. If a later recovery is unknown, record it as a loss.

### 3.5 Costs and tax
- Charges are modelled **in rupees, not as a flat %**, because some are fixed per trade and weigh heavily on a small position:
  - STT 0.1% each side; stamp duty 0.015% on buy; exchange + SEBI charges ≈ 0.004%; ₹0 brokerage (discount-broker delivery)
  - **Depository charge ≈ ₹16 per stock sold** (with GST). On a ₹5,000 buy that alone is ≈ 0.3%; on the early ₹2,000 buys it is ≈ 0.8%.
  - Expected round trip ≈ **0.5–0.6% on ₹5,000, ≈ 1% on ₹2,000**. A ₹20/trade brokerage variant is also run.
- **Current tax rules applied to every year**, so the results reflect today's rules:
  - Held ≤ 12 months: **20% short-term tax**.
  - Held > 12 months: **12.5% long-term tax** on gains above **₹1.25L per financial year**.
  - Losses set off against gains (short-term losses against either kind; long-term losses only against long-term gains).
  - At ₹2,000–5,000/month, yearly long-term gains will rarely exceed ₹1.25L, so in practice **short-term tax is the main tax cost**. Every stop-out within a year is taxed at 20% if it's a gain.

### 3.6 Portfolio construction — one stock every month, amount stepped up yearly (user-confirmed)

**Monthly amount (inflation step-up):** ₹2,000 a month in 2014, rising **~7.94% every January** to ₹5,000 in 2026 (`2,000 × 2.5^((year − 2014)/12)`, rounded to the rupee).

| Year | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ₹ / month | 2,000 | 2,159 | 2,330 | 2,515 | 2,714 | 2,930 | 3,162 | 3,413 | 3,684 | 3,976 | 4,292 | 4,632 | 5,000 |

Total invested over the 154 buys (Jan-2014 → Oct-2026) ≈ **₹5.04 lakh**.

- **Every month: invest that year's amount in ONE stock**, the top-ranked signal of that month's disclosure. There is no lump sum.
- **Skip disputed picks (user-confirmed):** a stock that other fund houses are *selling* the same month (the `sell_default` flag: 2+ houses cut or exit, or total fund holdings down 20%+) is skipped and the next-ranked stock is taken. Rare: about 4 (A), 11 (B), 4 (C), 0 (D) of ~155 monthly picks.
- **Signals run separately (user-confirmed):** A, B, C and D are four independent strategies in the first run; combinations are tested only afterwards, if more than one shows promise.
- **Ranking when several stocks qualify:** by signal strength (A: number of funds buying → total fund shares added; B: active weight; C: lowest weight; D: number of months of buying in a row). Ties are broken by liquidity (higher 20-day traded value).
- **Already holding the #1 stock? Add another monthly amount to it** (user-confirmed), up to a **cap of 3 purchases per stock** (whatever each purchase's rupee amount; user-confirmed). Once a stock has 3 open purchases, the month's ₹5,000 goes to the next-ranked stock.
  - **Each monthly purchase is its own trade**, with its own buy price and its own stop-loss ladder (§3.3). Example: a month-1 purchase at ₹100 may already have its stop at +10% while a month-2 purchase at ₹120 is still at −10%.
  - **The "funds start selling" exit and the 24-month time limit apply per stock.** When they trigger, all open purchases of that stock are sold together. (The 24-month limit counts from each purchase's own buy date.)
  - **Tax uses FIFO.** Indian demat sales are first-in-first-out, so even when a newer purchase's stop triggers, the oldest shares are treated as sold for working out short- vs long-term tax.
  - **Buying again after a stop-out** is allowed from the next month if the stock ranks #1 again.
  - *Variants: skip stocks already held (one purchase per stock) · cap at 25% of portfolio value · no cap.*
  - *Statistics:* repeated purchases of one stock are not independent bets, so t-stats are calculated per **stock** (purchases grouped together), not per purchase, to avoid overstating confidence.
- **Must afford at least 1 share:** only stocks priced ≤ **that year's monthly amount** at entry qualify (≤ ₹2,000 in 2014 … ≤ ₹5,000 in 2026). Buy whole shares; the leftover rupees go to a cash pool.
- **Liquidity floor:** 20-day average traded value ≥ ₹1 crore/day, so the price data is realistic and exits are possible.
- **Idle money (user decision, Phase 4):** sale money, dividends, leftover rupees and no-pick months' amounts go into a **small-cap fund** (proxy: Nifty Smallcap 250 TRI less 0.3%/yr) on the day they become free; yearly tax is paid by redeeming its oldest units; sold at the end. *(Variants: cash at 0%; liquid fund; all into the next buy.)*
- **Holdings grow naturally:** at most 24 open purchases (24-month cap), spread over 8–24 stocks depending on repeat buys; fewer as stops trigger.
- Idle money earns the small-cap fund's return (see above).
- **Months with no qualifying signal:** that month's amount stays in cash for that month (logged; shows how often the strategy has nothing to buy).

---

## 4. Comparisons and controls

All comparisons use the **same stepped-up monthly amounts (₹2,000 → ₹5,000) on the same dates**, so the returns are directly comparable.

| Comparison | Purpose |
|---|---|
| **Random stock each month, same rules** | **The key test.** Each month pick one random stock that passes the same price, liquidity and market-cap filters, apply identical exits, then repeat the whole 14-year run 1,000×. This gives a spread of possible XIRRs; *where does the signal land in it?* |
| Same monthly amounts into the Nifty 500 index (TRI) | Did the effort beat a passive index SIP? |
| Same monthly amounts into the 6 flagship funds (HDFC Flexi Cap, SBI Flexicap, Nippon Multi Cap, ABSL Flexi Cap, DSP Flexi Cap, Parag Parikh Flexi Cap; direct) | Did copying beat simply investing monthly in the funds? |
| Same monthly amounts into the small-cap fund | Since idle money sits there, the strategy must beat it too — else the result is just 'small caps did well' |
| Same signal, no stop (24-month hold only) | Does the stop ladder help or hurt? |

---

## 5. Exit-rule variants (Q2 — only meaningful if Q1 passes)

- Step size above +30%: **10-point steps (default)** vs **5-point steps throughout** (+35% → +25%, …)
- Initial stop: −10% (default) vs **2× or 3× ATR** (average true range; scales with each stock's own volatility)
- Time cap: 24 months (default) vs 3 / 6 / 12 months
- "Funds start selling" exit: on vs off

---

## 6. Metrics reported

**Per trade:** success rate · average win vs average loss · post-tax profit per trade (expectancy) · holding period · share of exits by reason (stop / funds selling / time cap)

**Portfolio (monthly investing):** **post-tax XIRR** on the stepped-up monthly contributions (the headline number) · total invested vs final value · maximum drawdown of the portfolio value · rolling 3-year XIRR · average cash held, and months with no signal

**Statistical:** the signal's XIRR as a **percentile of the 1,000 random-stock runs**, plus the t-stat of per-trade excess return vs random stocks. About 155 picks over 13 years (one a month) is a small sample, so the percentile view matters more than any single number. Results are split **2014–2019 vs 2020–2026**, and the top 10 trades are removed, to check the result isn't driven by luck or a few big winners.

---

## 7. Pass/fail gate (set **before** seeing results; metric confirmed by user in Phase 4)

The signal "works" only if **all** of these hold:
1. **G1:** its **average post-cost return per buy** beats **≥ 95% of 1,000 random portfolios** (random eligible stock from the same liquidity quintile, same months, same rules); t-stat vs random reported (clustered by stock).
2. **G2:** above the random median in **both** halves (buys in 2014–19 and 2020–26).
3. **G3:** still above the random median **after removing its 10 best buys**.
4. **G4:** post-tax XIRR (idle money in the small-cap fund) beats SIPs into the **Nifty 500**, the **6 flagship funds** and the **small-cap fund**.

Why per buy, not XIRR: with the −10% stop a random buy lasts ~29 days, so the portfolio is mostly the small-cap fund and XIRR barely separates good and bad picking (random portfolios: 14.2–14.7%). Random portfolios average −1.4% … +2.4% per buy (5th–95th pct), so G1 needs roughly ≥ +2.4% per buy.

If no signal passes → stop; the idea doesn't survive. If borderline or promising → expand to more fund houses (Phase 6) before believing it.

---

## 8. Phases

| Phase | Work | Output |
|---|---|---|
| **0. Data audit** | Check the **top ~12 fund houses** (by equity assets): archive start date, file format, whether files include ISIN, how many layout changes over the years, scheme mergers (2018 SEBI reclassification). Pilot set: **HDFC, SBI, Nippon, ABSL, DSP, PPFAS**, so "various funds" means *different fund houses* from day one ✅ **Done** | `data_audit.md` |
| **1. Holdings panel** | Parse all files into one table: month × scheme × ISIN × shares × weight ✅ **Done** (2,400 files → 645,937 holdings; 152–155 of 155 months per fund house) | `holdings_scheme.parquet`, `holdings_amc.parquet`, [phase1_holdings.md](phase1_holdings.md) |
| **2. Prices** | Download NSE price files 2013–2026 (both formats), adjust for splits and bonuses, map ISIN ↔ ticker ✅ **Done** (5.96 M price rows; 98.7% of split/bonus factors match price gaps; Nifty 500/50/Midcap/Smallcap TRI) | `prices_adj.parquet`, `index_tri.parquet`, [phase2_prices.md](phase2_prices.md) |
| **3. Signals** | Build signals A–D and the "funds start selling" flags ✅ **Done** (votes per fund house with launch/rename and flow corrections; B = excess weight in diversified funds; C = new < 2% starter positions; action date 11th–14th of next month) | `signals.parquet`, [phase3_signals.md](phase3_signals.md) |
| **4. Backtest engine** | Trade simulator (stop ladder, fills, costs, tax, small-cap parking) + random control + SIP benchmarks ✅ **Done** (19/19 tests; placebo fails as it should; Nifty 500 SIP 12.25%, 6 funds 14.42%, small-cap 14.69% post-tax) | `engine.py`, `runner.py`, `evaluate.py`, [phase4_engine.md](phase4_engine.md) |
| **5. Results (pilot)** | Run signals × exit variants; apply the §7 gate ✅ **Done** — B passes G1–G3, fails G4 (14.686% vs 14.687%); A/C/D fail G1; stop-loss dominates outcomes | [phase5_results.md](phase5_results.md) |
| **6. Expansion** | Added ICICI, Axis, UTI; replication (NEW) + all 9 houses (ALL); pre-registered H1 (B, user rules) and H2 (C, no stops) ✅ **Done** — H1 passes G1/G2/G3/G5 on both but fails G4 (XIRR ≈ small-cap SIP) → inconclusive; H2 rejected (60th/23rd pct) | [phase6_results.md](phase6_results.md) |

---

## 9. Known limitations

- **Pilot = 6 fund houses, not the whole industry.** "Various MFs buying/selling" is measured across the pilot fund houses, with each fund house counted **once** (several schemes of one fund house share a research team, so they don't count as independent votes). Industry-wide group buying needs Phase 6.
- **PPFAS is unusual:** about 25 Indian stocks plus foreign shares, and very low turnover. It's useful as an independent vote, but too few stocks to carry the signal alone.
- **Monthly snapshots** miss trades made and reversed within the same month, and month-end portfolios can be window-dressed (tidied up to look better).
- **Bull-market-heavy window**; the random-stock control partly corrects for this.
- **Tax simplified** to current rules for all years. Real past tax was lower: long-term gains were untaxed before Feb-2018, and the old rates were 15% short-term and 10% long-term.
- **Execution:** small-cap fills at the open may slip on low-volume days; checked by testing liquidity filters.

---

*This is a backtest for learning, not investment advice. Past results, even if positive, don't guarantee future returns.*
