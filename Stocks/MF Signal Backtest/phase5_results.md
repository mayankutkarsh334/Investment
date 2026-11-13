# Phase 5: Results

> **Run:** Nov-12-2026, once, with the rules and pass/fail gates fixed beforehand (study_plan.md §3–§7, phase4_engine.md §6).
> **Window:** buys from Jan-2014 to Oct-2026 (155 months). ₹2,000 → ₹5,000 a month (+7.94% each January), ≈ ₹5.09 lakh invested. Idle money sits in a small-cap index fund. Today's tax rules apply throughout.
> *This is a historical test, not investment advice.*

---

## 1. Verdict

**The idea does not produce a robust edge under your rules.**

- **B (biggest bets)** is the only signal whose stock picks beat luck: +4.1% per buy vs +1.1% for random, better than 98.7% of 1,000 random portfolios.
- **But B fails the gate that matters for your money (G4).** Its post-tax XIRR (14.686%) is a dead heat with simply investing the same money in the small-cap fund (14.687%). In rupees, B's stock picks added about **₹18,000 over 13 years**.
- **B's edge depends on one stock.** Remove its 36 TVS Motor buys, or allow only one buy per stock, and B no longer beats 95% of random portfolios.
- **A, C (your original small-position idea) and D don't beat luck** at the 95% level.
- **The −10% stop-loss ladder shapes the outcome more than the stock choice.** Most buys end within weeks, so the portfolio is essentially the small-cap fund plus small, short trades.

Under the plan's rule ("if no signal passes → stop; if borderline → test on more fund houses before believing it"), B is **borderline**. The honest reading is "not proven". Section 6 lists what could change that.

---

## 2. Main results (your rules: −10% stop ladder, funds-selling exit, 24-month cap, up to 3 buys per stock)

| Signal | Buys | Avg return per buy | Median per buy | Win rate | Median days held | Random portfolios: median (5th–95th) | Beats % of random | t-stat |
|---|---|---|---|---|---|---|---|---|
| **B: biggest bets** | 155 | **+4.13%** | +4.05% | 55% | 76 | +1.07% (−0.69 … +3.03) | **98.7%** | **2.18** |
| D: steady buying | 153 | +2.50% | +2.73% | 52% | 49 | +0.61% (−1.14 … +2.95) | 92.4% | 1.36 |
| D2 (2-month streak) | 154 | +2.41% | +2.03% | 51% | 49 | +0.66% | 90.4% | 1.27 |
| A: group buying | 155 | +2.32% | +3.80% | 55% | 50 | +0.92% (−0.84 … +2.95) | 86.9% | 1.18 |
| A3 (3+ houses) | 148 | +1.65% | +3.80% | 55% | 50 | +0.89% | 72.8% | 0.67 |
| C: small new bets (your idea) | 155 | +1.49% | −7.07% | 46% | 32 | +0.87% (−0.90 … +2.92) | 70.6% | 0.49 |

### Gates

| Signal | G1 beats ≥95% random | G2 both halves | G3 without top-10 buys | G4 XIRR beats all 3 SIPs | **Pass** |
|---|---|---|---|---|---|
| **B** | ✅ 98.7% | ✅ 2014–19: +5.2% vs +0.5% · 2020–26: +3.2% vs +1.5% | ✅ +1.29% vs +1.07% | ❌ 14.686% vs small-cap SIP 14.687% | **No** |
| D | ❌ | ✅ | ❌ | ❌ | No |
| D2 | ❌ | ✅ | ❌ | ❌ | No |
| A | ❌ | ❌ (2014–19: −0.2%) | ❌ | ❌ | No |
| A3 | ❌ | ❌ | ❌ | ❌ | No |
| C | ❌ | ✅ | ❌ | ❌ | No |

### What your money became (post-tax, same ₹5.09 lakh)

| | Post-tax XIRR | Final value |
|---|---|---|
| Strategy B | 14.69% | ₹12.08 lakh |
| Strategies A / C / D | 14.49% / 14.60% / 14.58% | — |
| Random portfolios (median) | ~14.45% | — |
| **SIP: small-cap index fund** | **14.69%** | ₹12.2 lakh |
| SIP: 6 flagship funds | 14.42% | ₹11.9 lakh |
| SIP: Nifty 500 index fund | 12.25% | ₹10.4 lakh |

---

## 3. What drives B

- **Concentration:**
  - TVS Motor makes up 36 of 155 buys, at +8.0% per buy.
  - Without it, B averages **+2.96%**, just below the random 95th percentile (+3.03%).
  - Other frequent picks: Reliance (12 buys, +11.1%), Axis Bank (12, −2.4%), Muthoot (10, +8.3%), HDFC Bank (10, +2.1%).
- **One buy per stock:** forced to diversify, B falls to +2.95% and the 94.6th percentile, failing G1.
- **Large caps:** B's picks have a median ₹131 crore of daily turnover (A ₹210 crore, C ₹103 crore). B is essentially "large stocks one diversified fund is very overweight in".
- **Uneven by year:** strong in 2016, 2017 and 2023 (+11 to +13%); negative in 2015, 2019, 2024 and 2026.
- **Why the rupee effect is tiny:**
  - each buy is ₹2,000–5,000 and 85% end at a stop within months;
  - meanwhile the money would have earned ~15% a year in the small-cap fund anyway;
  - so B's stock picks netted only ₹18,266 on ₹4.39 lakh of buys.

---

## 4. Exit-rule variants (only meaningful for B, which passed the stock-picking gates)

Each variant was compared with 1,000 random portfolios run under the *same* exit rule.

| Variant | Avg per buy | Beats % random | t | XIRR | G1 | G2 | G3 | G4 | All |
|---|---|---|---|---|---|---|---|---|---|
| Default (your rules) | +4.13% | 98.7% | 2.18 | 14.69% | ✅ | ✅ | ✅ | ❌ | ❌ |
| 5-point steps above +30% | +4.21% | 99.1% | 2.25 | 14.66% | ✅ | ✅ | ✅ | ❌ | ❌ |
| Initial stop = 2× ATR | +1.92% | 91.0% | 1.51 | 14.73% | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Initial stop = 3× ATR** | +4.35% | 99.1% | 1.99 | **14.78%** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Time cap 3 months** | +2.88% | 97.2% | 2.49 | **14.76%** | ✅ | ✅ | ✅ | ✅ | ✅ |
| Time cap 6 months | +3.45% | 97.8% | 1.68 | 14.68% | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Time cap 12 months** | +4.11% | 98.7% | 2.15 | **14.69%** | ✅ | ✅ | ✅ | ✅ | ✅ |
| No funds-selling exit | +4.24% | 98.7% | 1.54 | 14.72% | ✅ | ✅ | ❌ | ✅ | ❌ |
| Funds-selling = 3+ houses | +4.34% | 98.9% | 1.63 | 14.74% | ✅ | ✅ | ❌ | ✅ | ❌ |
| Funds-selling = 10% fall | +4.10% | 98.9% | 2.24 | 14.68% | ✅ | ✅ | ✅ | ❌ | ❌ |
| One buy per stock | +2.95% | 94.6% | 1.59 | 14.60% | ❌ | ✅ | ❌ | ❌ | ❌ |
| No stop-loss (24-month hold) | +18.72% | 26.1% | −1.11 | 14.90% | ❌ | ❌ | ❌ | ✅ | ❌ |

**The three variants that pass all four gates are not convincing:**
- **Margins are tiny:** their XIRR beats the small-cap SIP by only **0.01–0.10 percentage points** (about ₹500–₹8,000 over 13 years).
- **They don't survive without TVS Motor.** Removing it makes all three fail G1:

  | Variant | Without TVS Motor | Random 95th percentile |
  |---|---|---|
  | 3× ATR | +3.09% | +3.27% |
  | 3-month cap | +2.31% | +2.51% |
  | 12-month cap | +2.93% | +2.98% |

- **Many tries:** about 20 rule combinations were tried in total, so 2–3 "passes" are roughly what chance alone would produce.

---

## 5. Biggest lesson: the stop-loss decides more than the stock picking

Each signal re-run **without the stop-loss ladder** (hold up to 24 months, exit early only if funds sell):

| Signal | Avg per buy (no stops) | Random no-stop median | Beats % random | XIRR (no stops) | vs small-cap SIP 14.69% |
|---|---|---|---|---|---|
| C: small new bets | **+26.5%** | +19.0% | 90.4% | **15.61%** | **+0.92 pts** |
| D: steady buying | +29.8% | +26.7% | 66.7% | 15.18% | +0.49 |
| B: biggest bets | +18.7% | +22.5% | 26.1% | 14.90% | +0.21 |
| A: group buying | +16.3% | +17.2% | 43.7% | 14.60% | −0.09 |

- **Holding longer beat cutting losses.** In 2014–2026, a mostly rising market, every signal and every random portfolio earned far more per buy without the −10% stop. Typical holding went from ~1–2 months to 7–12 months.
- **Your original idea (C) looks best this way:** 15.61% XIRR, about 0.9 points a year above the small-cap SIP. But it still beats only 90% of random no-stop portfolios, so it **fails G1**, and the window is one long bull market. It's a lead, not proof.
- **The stop rule mainly turned the strategy into "small-cap fund + small trades".** That protected against crashes (Yes Bank, DHFL) but gave up most of the upside of holding.

---

## 6. Caveats

1. **Many tests:** 6 signal versions + 14 variants. At a 95% bar, one or two "passes" by luck are expected. B's main result (98.7%, t 2.18) is right at the threshold that allows for testing 4 signals (≈ 98.75%).
2. **One period, mostly bull market.** 2014–2026 includes 2015–16, the 2018 mid-cap fall, the 2020 crash and 2024–25, but rising markets dominate. That favours holding over stopping.
3. **6 fund houses only.** "Group buying" and "funds selling" are measured across HDFC, SBI, Nippon, ABSL, DSP and PPFAS, not the whole industry.
4. **Small-cap fund as the parking place.** Idle money earns small-cap returns (14.7% SIP), a high bar for short stock trades to beat. With idle money in a liquid fund, every strategy's XIRR would be much lower, but the per-buy comparison with random would be the same.
5. **Simplifications from Phase 4:** dividends credited at exit, per-buy tax lots, a 30% slab on dividends, an index proxy for the small-cap fund.

---

## 7. What could still change the conclusion

| Option | What it tests | Worth it? |
|---|---|---|
| **Phase 6: add ICICI, Axis and UTI** (browser-session downloaders) | Whether B, and C without stops, hold up with more fund houses' data. That's the plan's prescribed next step for a borderline result | Yes, if you want to keep pursuing the idea. It's the only fair way to confirm or kill B |
| **Re-think the exit rule** (e.g. no stop, or a much wider one, with the 24-month cap) as a *new* pre-registered test | Whether C/D's no-stop edge is real | Only with fresh data (Phase 6) or a held-out period, otherwise it's fitting to this result |
| **Stop here** | — | Reasonable. On this evidence, a plain SIP into a small-cap or flexi-cap fund did as well as or better than copying fund buying, with far less effort |

---

## Files

- `data/results/phase5_summary.csv`, `phase5_<signal>.pkl`: main runs (all buys, 1,000 random comparisons).
- `data/results/variants_summary.csv`, `variant_<name>.pkl`: the 14 variants.
- `scripts/run_phase5.py`, `scripts/run_variants.py`: reproduce everything.
