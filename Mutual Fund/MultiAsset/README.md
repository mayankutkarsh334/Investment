# Multi Asset Allocation Funds — Category Study

**Fifth category study** (after FlexiCap, SmallCap, International, MidCap) · 35-fund universe screened · **7 funds studied in full** · decision tree complete · **≈15,000 lines across 58 files**

> **⚠ Not investment advice.** Mechanics and evidence only.
>
> **Weights (LOCKED, multi-asset re-weight):** Risk 25 · Returns 20 · Allocation-Engine 20 · Cost+Tax 20 · Manager 10 · AMC 5. **Scores are NOT comparable to the four equity categories** — they measure a risk-reduction product against blended benchmarks and a DIY basket, not a single equity index.

---

## ⭐ The verdict

**The portfolio needs the non-equity exposure. It does not need a multi-asset fund to get it.**

Tested at the level that matters — what each fund does to a portfolio that already holds four equity sleeves — **a plain do-it-yourself basket of a gold ETF plus a short-duration debt fund improved whole-portfolio risk-adjusted return more than any of the seven studied funds in two of three windows**, and was beaten only by Quant in the third.

| Sleeve added at 20% of portfolio | 3.19y | 5.91y *(incl. 2022)* | 6.89y *(incl. COVID)* |
|---|---|---|---|
| **DIY — gold ETF + short-duration debt** | **+0.20** | **+0.11** | +0.08 |
| Best fund (Quant) | +0.10 | +0.10 | **+0.11** |
| Best *investable* fund (WOC / ICICI) | +0.10 / +0.03 | — / +0.08 | — / +0.05 |
| UTI · ABSL | 0.00 / −0.01 | **−0.02** | **−0.04** |

*(change in whole-portfolio Sharpe vs a core of 30% PP FlexiCap / 25% Edelweiss MidCap / 25% DSP SmallCap / 20% international)*

**Why:** the funds hold **26–68% equity**, correlating **0.77–0.93** to the FlexiCap core. A DIY sleeve is 100% non-equity. **You are paying a fund to hand back the asset class you were trying to dilute.**

→ **Full reasoning, sizing and caveats: [decision_tree.md](decision_tree.md)**

---

## The seven funds

| Rank | Fund | Score | M1 Ret | M2 Risk | M3 Alloc | M4 Cost | M5 Mgr | M6 AMC | Character | Audit |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **[ICICI Pru](funds/icici/README.md)** | **3.82** | 4.3 | 3.4 | **3.9** | 3.8 | **3.8** | 3.7 | Best alpha, best 2022, equity-taxed, only auditable engine — **−30.6% COVID drawdown** | ✅ primary-source |
| 2 | [SBI](funds/sbi/README.md) | 3.66 | 3.6 | **4.5** | 3.0 | 3.5 | 3.2 | **3.9** | Elite cycle-proven dampener; static book; ⚠ **loses to DIY over 5.91y** | ⚠ **not audited** |
| 3 | [Nippon](funds/nippon/README.md) | **3.51** | 3.8 | 3.3 | 3.1 | **4.1** | 3.0 | 3.7 | Cheapest ER, broadest book — ⚠ alpha cut +3.85%→+1.4% on audit | ✅ audited |
| 4 | [WOC](funds/woc/README.md) | 3.39 | 3.4 | **4.1** | 2.9 | 3.3 | 3.0 | 2.8 | Best-measured risk profile; frozen engine; unprovable fee | ✅ primary-source |
| 5 | [Quant](funds/quant/README.md) | 3.20 | **4.3** | 2.6 | 3.3 | 3.5 | 2.4 | **1.8** | Returns leader; equity-level risk; **settled front-running case** | ✅ audited |
| 6 | [ABSL](funds/absl/README.md) | 3.18 | 3.2 | 3.1 | 3.0 | 3.3 | 3.2 | 3.6 | Well-built, wholly untested; out-dampened by no-gold cousins | ⚠ **not audited** |
| 7 | [UTI](funds/uti/README.md) | 3.03 | 2.7 | 3.2 | 2.8 | 3.4 | 2.8 | 3.4 | Closet equity (0.93 correlation); negative allocation alpha | ⚠ **not audited** |

**Every fund has 6 modules + a README.** Depth ranges from 1,647 lines (Quant) to 2,674 (WOC); 24–36 charts each.

---

## ⭐ What this study established

**1. No allocation alpha anywhere — the category's defining skill claim is unsupported.**
Seven of seven funds, with three distinct failure modes: **frozen dial** (WOC, −2.56%/yr, risk-reducing), **swinging dial** (ICICI, −0.12%/yr, risk-*additive*), **refuted model** (UTI). And it **replicates outside the category** — three Balanced Advantage funds at three AMCs, the purest expression of tactical allocation in Indian mutual funds:

| Balanced Advantage fund | vs a plain Nifty 500 index |
|---|---|
| ICICI Prudential BAF (6.9y) | **−2.53pp/yr** |
| WhiteOak Capital BAF (3.5y) | **−0.91pp/yr** |
| HDFC BAF (6.9y) | Sharpe **0.72** vs pure equity's **1.01** |

At both WhiteOak and ICICI, the *same team's* stock-selection funds beat their benchmarks by **+2.5 to +7.9pp/yr** while their allocation products failed.

**2. The tax triad is worth ~0.1–0.2pp/yr, not the decisive edge the framework assumed.**
Equity taxation separates the shortlist by **₹15,625 flat** per ₹10 lakh — the LTCG rate is 12.5% in both the equity and middle tiers. It matters only against *slab*, which no studied fund faces. The internal rebalancing shield models at **0.08–0.17pp/yr**. **Together: the fund-vs-DIY question is decided by manager alpha, not structure.**

**3. Gold does the diversification work; debt does almost none.**
A 20% pure short-duration-debt sleeve changed whole-portfolio Sharpe by **+0.01, +0.01, −0.01** across three windows.

**4. The DIY counterfactual hardens over longer windows.**
Over 3.19 years all seven funds beat it. Over **5.91 years including 2022, SBI lost by ₹18,914 and UTI by ₹1,061** — only three of five cycle-tested funds cleared the bar.

**5. ⚠ The screen made one error, and it was the biggest fund in the category.**
**ICICI Pru was eliminated at Stage 2** on a 3-year window — adopted *because most survivors lacked 5Y history*, then applied to the one fund that had it — using a **Tickertape Sharpe of 0.29** contradicted by the AMC's own factsheet (**1.10**) and by MFAPI (**1.32** over 5Y, **1.51** over 5.91y). Re-studied in full, **it is the highest-scoring fund here.** Every other elimination was re-tested and holds.

**6. ⚠ Aggregator data failed repeatedly, and every conclusion that mattered had to be re-verified.**
**Five stale expense ratios** (Nippon 0.43→0.27, SBI 0.74→0.51, Quant 1.16→0.51, WOC 0.67 vs 0.39, ICICI 0.79 vs 0.54), **two wrong Sharpe ratios** (WOC 1.20 vs 1.84, ICICI 0.29 vs 1.10), **three wrong benchmarks**, one wrong exit load. **The SID and the AMC monthly factsheet were the only reliable sources.**

---

## The two structural findings from screening

1. **The category is a post-2023 tax-driven launch wave.** Only **8 of 35** funds are cycle-tested (≥60 months); 27 launched after the April-2023 removal of debt-fund indexation made ≥65%-gross-equity multi-asset the tax-efficient way to hold gold and debt. **The category as it exists was largely manufactured by a tax change** — which forced replacing the age filter with a **≥36-month track-record floor** plus a `no-2022-data` flag.
2. **The ₹84,000 Cr flagship screened out** — and see finding 5 above. That elimination was wrong, and correcting it changed the study's answer at the top.

---

## Method — the apparatus

- **MFAPI NAV self-computation** as the backbone: CAGR ladders, calendar years, rolling 1/3/5/10Y distributions, drawdown-and-recovery ledgers, SIP XIRR (Newton-Raphson), daily-return distributions. Up to **3,344 NAVs / 163 monthly observations** per fund.
- **Blended benchmarks built per fund from its own SID**, using index-fund NAV legs — because no single benchmark exists for a multi-asset fund.
- **Allocation-vs-selection decomposition** (constrained returns-based style analysis + Brinson-style replica) — the method that produced finding 1.
- **Rolling-26-week asset-path reconstruction**, reconciled to factsheet weights, which made ICICI's seven market turns individually gradeable.
- **Post-tax DIY modelling** with full cost-basis tracking through each annual rebalance.
- **Whole-portfolio testing** — each fund added at 20% to a four-sleeve equity core, across three windows.
- **Methods introduced by this study:** the **NAV smoothing / stale-pricing test** (lag-1..3 autocorrelation + Geltner unsmoothing — Nippon is the only fund that fails it); **notional-vs-effective exposure** (which found WOC's 16pp hidden arbitrage book); and **regulatory capacity ceilings** (ETCD 30% of NAV) as a constraint distinct from AUM.

---

## Files

| File | Contents |
|---|---|
| **[decision_tree.md](decision_tree.md)** | ⭐ **The verdict** — sleeve question, fund-vs-DIY, sub-type, sizing, review triggers |
| [study_plan.md](study_plan.md) | Framework, the four framing facts, module specs, locked weights |
| [dimensions_covered.md](dimensions_covered.md) | The completeness gate — every dimension inherited from four prior studies + 18 new |
| [module_prompt_template.md](module_prompt_template.md) | Reusable per-module commissioning prompt |
| [screening/](screening/) | methodology · stage1 (35→11) · stage2 (11→6) · all_funds_data |
| `funds/<name>/` | 6 modules + README per fund, ×7 |

---

## ⚠ Outstanding

| # | Item | Why it matters |
|---|---|---|
| 1 | **Audit SBI, UTI and ABSL** against primary documents | The two audits run so far moved one fund's score by 0.20 and a rank, and left the other unchanged. **SBI sits at rank 2 and is unaudited.** |
| 2 | **Correct `screening/methodology.md` and `stage2_performance.md`** | Both still record ICICI's elimination as merit-based. It was not. |
| 3 | **Resolve WOC's expense ratio** (0.39–0.67% across five sources) | It decides whether that fund beats a DIY basket over ten years. |
| 4 | **Verify the possible Nippon executive SEBI settlement** | Surfaced during the Quant audit; Nippon's Module 6 (3.7) does not record it. |
| 5 | **Retrofit the Nifty-500 equity leg** to SBI, UTI, ABSL | Their published alphas use a Nifty-50 leg and are overstated ~1.5–2.5pp/yr. *(Done for Nippon and Quant.)* |

**None of these changes the decision-tree verdict** — DIY wins by a margin no plausible correction closes. They affect the *ranking among funds*, which matters only if the fund route is taken anyway.

---

*Category study complete: screening (Jul 2026) → seven six-module deep studies → decision tree (Aug 2026). Feeds [Portfolio/allocation_options.md](../Portfolio/allocation_options.md) for the ₹65K/month cross-sleeve deployment. **Headline: the non-equity sleeve earns a slot; the fund does not.***
