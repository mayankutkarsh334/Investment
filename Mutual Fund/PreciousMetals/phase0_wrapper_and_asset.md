# Phase 0 — Wrapper & Asset Verdict

**Status:** ✅ **PHASE 0 COMPLETE** — 0.1 wrapper *(provisional, gated on one SID lookup)* · 0.2 **flow-rebalance** · 0.3 **gold only** · 0.4 **SGB out**
**Budget:** ₹10,000/month, 10-year hold, annual rebalancing, 30% slab

> **⚠ Not investment advice.** Modelling only. Every cost input below is aggregator-sourced and **none has been verified against a SID** — which the headline finding turns out to depend on entirely.

---

## 0.1 — ETF or FoF? *(complete, provisional)*

### The comparison reduces to two numbers

Both routes hold the same metal at the same price. Stripping out what cancels, the only real differences are:

| | FoF route | ETF route |
|---|---|---|
| Annual drag | FoF layer ER **+** underlying ETF ER | ETF ER alone |
| Entry cost | **None** — buys at NAV | Brokerage + half-spread + premium-to-iNAV, on **each of 120 buys** |
| Account cost | None | Demat annual maintenance |
| LTCG gate | 24 months | 12 months |

**When comparing a FoF to its own underlying ETF, the ETF layer cancels.** The question collapses to: **is the FoF's extra layer cheaper than the ETF's trading friction?** One is an annual charge on a growing corpus; the other is a one-time charge on each contribution.

### ⭐ Finding 1 — The 24-month gate is nearly irrelevant. My framing fact 3 was wrong.

`study_plan.md` framing fact 3 asserted the 12-vs-24-month gate is *"worth multiples"* of the ER spread. **The model says it is worth ₹525 to ₹1,959 over ten years.**

| Annual trim | Tax, 24-mo gate | Tax, 12-mo gate | **Penalty** |
|---|--:|--:|--:|
| 10% of sleeve | ₹24,194 | ₹23,669 | **+₹525** |
| 15% of sleeve | ₹27,027 | ₹26,296 | **+₹731** |
| 25% of sleeve | ₹26,787 | ₹24,828 | **+₹1,959** |

**Why FIFO defuses it:** selling oldest-first, the units disposed at rebalance #3 and beyond are always 36+ months old — long-term under *either* gate. The gate can only bite at rebalances #1 and #2, when the sleeve is worth ₹1.2L–₹2.5L and the embedded gain is a few thousand rupees. **A structural-looking disadvantage that is really a two-year transitional one, on a tiny base.**

This removes the entire reason Phase 0.1 was billed as "the single highest-value analysis in the study." It isn't. **The wrapper decision is a pure cost decision.**

### Finding 2 — The crossover, in one number

FoF layer ER at which the two routes tie (₹10K/mo, 10y, 8% gold, 15% annual trim):

| ETF entry cost | Demat ₹0/yr | **₹400/yr** | ₹800/yr |
|---|---|---|---|
| 0.10% | 0.031% | 0.110% | 0.189% |
| **0.25%** | 0.098% | **0.178%** | 0.258% |
| 0.50% | 0.212% | 0.292% | 0.372% |

> **Rule of thumb: the FoF wins if its own layer costs less than ~0.10–0.25%/yr.** Below that band the ETF's per-purchase friction and demat charge outweigh the second layer; above it, they don't.

Against the Direct-plan FoF layers found so far — Nippon 0.05%, Quantum 0.06%, UTI 0.09%, Groww 0.14%, Axis/ICICI 0.18%, HDFC 0.20%, ABSL 0.21%, SBI/Tata 0.24%, LIC 0.35% — **the cheapest four sit below the crossover in the central case and the rest sit above it.**

### ⚠ Finding 3 — The verdict hinges on one unresolved number

The crossover assumes the FoF's *underlying* ETF is no dearer than the ETF you'd otherwise buy. That assumption is contested:

| Source | Nippon's underlying gold ETF ER |
|---|---|
| Search result (GOLDBEES) | **0.25%** |
| 1finance comparison table | **0.82%** |

Run both:

| Stack | vs a 0.25% ETF (entry 0.25%, demat ₹400) | Verdict |
|---|--:|---|
| Nippon FoF 0.05% + underlying **0.25%** = 0.30% | **+₹6,446** | **FoF** |
| Nippon FoF 0.05% + underlying **0.82%** = 0.87% | **−₹21,892** | **ETF** |
| UTI FoF 0.09% + underlying 0.50% = 0.59% | −₹8,102 | ETF |
| ICICI FoF 0.18% + ICICI ETF 0.50% = 0.68% | −₹12,562 | ETF |

**One number flips the answer by ₹28,000.** And the 0.82% figure is the better-corroborated one: 1finance's ETF column matches the independent search on ICICI (0.50% = 0.50%), Kotak (0.55% = 0.55%) and SBI (0.73% vs 0.70%), and diverges only on Nippon. That does not settle it — a stale figure on one row is exactly the failure mode MultiAsset documented five times — but it tilts against the cheap-FoF case.

**⭐ RESOLVED Aug 9 2026 — empirically, not from a disclosure. See §0.1b below.**

### Finding 4 — The whole decision is second-order

Across every scenario modelled, the wrapper is worth **₹3,000 to ₹28,000 over ten years on a terminal corpus of ~₹15 lakh** — between **0.2% and 1.9%**. Real, worth getting right, but far smaller than the plan implied. It is also smaller than the plausible spread in *tracking difference* between schemes, which Module 1 measures and which no amount of wrapper optimisation can recover.

**Corollary: this decision must not delay starting the SIP.** Switching wrappers later costs one capital-gains event on a small base.

### Finding 5 — The result is robust to the gold-return assumption

| Gold | FoF (0.30%) | ETF (0.25% + 0.25% entry) | Gap |
|---|--:|--:|--:|
| 5%/yr | ₹13,75,673 | ₹13,69,038 | +₹6,635 |
| 8%/yr | ₹15,07,898 | ₹15,01,452 | +₹6,446 |
| 12%/yr | ₹17,13,327 | ₹17,07,131 | +₹6,196 |
| 20%/yr | ₹22,50,088 | ₹22,44,404 | +₹5,684 |

The gap is stable within ₹1,000 across a 4× range of return assumptions. **The wrapper conclusion does not depend on a view about gold** — which matters given MultiAsset's warning that the measured DIY advantage was flattered by gold's ~29%/yr run.

### Provisional verdict

> **PROCEED WITH BOTH WRAPPERS IN SCOPE, pending the SID check.**
>
> - **If a FoF layer ≤ ~0.10% pairs with an underlying ETF ≤ ~0.30%** → **FoF**, on cost, plus an unmodelled advantage: native auto-SIP. MultiAsset's own caveat — *"the DIY route requires discipline the fund provides automatically"* — applies here. An ETF SIP is broker-simulated or manual, and a few missed buys cost more than the entire ER difference.
> - **Otherwise** → **ETF**, and the FoF universe leaves the study.
>
> Stage 1 therefore screens **both** wrapper universes until the Nippon/GOLDBEES ER is resolved from primary documents.

### What this model does not capture

1. **Tracking difference between schemes** — Module 1's subject, and plausibly larger than everything measured here. A scheme leaking 0.30%/yr in unexplained slippage erases the entire wrapper advantage.
2. **Premium/discount volatility** — modelled as a flat per-buy cost. Real premiums spike in demand surges, and a SIP buys on a fixed date regardless. Needs NSE/BSE bhavcopy vs iNAV.
3. **Exit loads** — not in the model; several gold FoFs carry ~1% inside a short window, which interacts with the annual trim.
4. **Behavioural risk** on the ETF side, noted above and deliberately left unquantified.

### Model

`scratchpad/phase0_1.py` — month-by-month, 120 buys, FIFO lot tracking, drag compounded monthly on the corpus, tax at 12.5% above the gate and 30% slab below, **no ₹1.25L exemption** (§112A is listed-equity only). Trim variants 0% (flow-rebalanced) and 15% (active trimming); the 0% case is Phase 0.2's subject.

---

## 0.1b — The ER dispute, settled by measurement · **COMPLETE**

**The disclosure was never obtainable from aggregators, so it was measured instead.** Every gold FoF holds the same metal, so NAV divergence between two of them over a common window *is* their cost difference — no disclosed ER required. AMFI publishes ETF NAVs too, which allows the sharper test: **each FoF against its own underlying ETF.**

### Test 1 — FoF vs its own underlying ETF (the gap *is* the FoF layer), 3y to 2026-08-07

| AMC | FoF CAGR | ETF CAGR | **Implied FoF layer** | Underlying |
|---|--:|--:|--:|---|
| **Nippon** | 34.50% | 34.50% | **0.01%** | Gold BeES |
| ICICI Pru | 34.75% | 34.84% | 0.09% | ICICI Gold ETF |
| Kotak | 34.69% | 34.74% | 0.04% | Kotak Gold ETF |
| Axis | 34.52% | 34.66% | 0.14% | Axis Gold ETF |
| ABSL | 34.76% | 34.75% | −0.01% | ABSL Gold ETF |
| ⚠ SBI | 34.82% | 34.47% | **−0.35%** | SBI Gold ETF |
| ⚠ Quantum | 34.95% | 34.72% | **−0.23%** | Quantum Gold ETF |

### Test 2 — ETF vs ETF, 3y (which underlying is expensive?)

| Gold ETF | CAGR | Drag vs best |
|---|--:|--:|
| ICICI Gold ETF | 34.84% | 0.00% |
| ABSL Gold ETF | 34.75% | 0.09% |
| Kotak Gold ETF | 34.74% | 0.10% |
| Quantum Gold ETF | 34.72% | 0.11% |
| HDFC Gold ETF | 34.66% | 0.17% |
| Axis Gold ETF | 34.66% | 0.18% |
| ⚠ **Nippon Gold BeES** | **34.50%** | **0.34%** |
| SBI Gold ETF | 34.47% | 0.37% |

### ⭐ The answer: both sources were half right, and the conclusion flips

**Nippon's FoF layer is genuinely ~0.01–0.06%** — the 0.05% disclosure is real. **But Gold BeES, the ETF it holds, is the second-worst tracker of eight**, 0.34pp/yr behind ICICI's. So Nippon's *stack* is cheap on the layer everyone quotes and expensive on the layer nobody quotes.

**The "0.05% + 0.25% = 0.30%, FoF wins by ₹6,446" scenario in §0.1 is falsified.** Not because the FoF layer was overstated, but because the underlying is not cheap. Direction of the 0.82% figure is supported; its exact level is not established.

### ⭐ The larger finding — stated ER does not predict realised drag

| Fund | Stated FoF layer | Rank on realised 3y drag (of 8) |
|---|--:|--:|
| Quantum | 0.06% | **1st** |
| SBI | 0.24% | 2nd |
| ABSL | 0.21% | 3rd |
| ICICI | 0.18% | 4th |
| Kotak | 0.10% | 5th |
| Axis | 0.18% | 6th |
| **Nippon** | **0.05%** *(cheapest)* | ⚠ **7th** |

**The cheapest stated layer produced the second-worst realised outcome.** This vindicates the study design: `study_plan.md` weights Module 1 (realised tracking fidelity) at 35% and Module 2 (stated cost structure) at 20%, and Stage 2 screens on tracking difference rather than ER. **Screening this category on published expense ratios would have picked the wrong fund.**

### ⭐ And it makes the wrapper question near-moot

Realised spreads, 3y: **within FoFs 0.45pp** (Quantum 34.95% → Invesco 34.10%); **within ETFs 0.37pp** (ICICI 34.84% → SBI 34.47%); **between the best FoF and the best ETF, ~0.1pp.**

**The intra-wrapper spread is larger than the inter-wrapper difference.** Choosing the right *scheme* matters more than choosing the right *wrapper* — and both are smaller than §0.1's ±0.26% band suggested the whole decision was worth.

> **Revised 0.1 verdict: PROCEED WITH BOTH WRAPPERS. The blocker is dissolved rather than resolved** — the disclosed ER no longer gates anything, because Phase 1 screens on measured tracking difference, which is what actually decides this. **Nippon is no longer a leading candidate under either wrapper.**

### ⚠ Data-quality caveats — these numbers are indicative, not Module 1

1. **Three "FoF layers" came out negative** (SBI −0.35%, Quantum −0.23%, ABSL −0.01%). A FoF cannot outperform its own underlying ETF. This indicates NAV timing/reporting artefacts, or that the FoF does not hold only that ETF. **Treat all FoF-layer figures as ±0.3pp.**
2. **The 5-year ETF window is corrupted** by unit splits (SBI, Quantum and ABSL ETFs return −50% to −43%). Only the 3-year window is usable. A split-adjustment pass is required before these become study-grade.
3. **This measures *relative* drag, not absolute.** Without the domestic gold price benchmark that Phase 1 must construct (IBJA / MCX / rebuilt LBMA), no absolute all-in cost can be stated — only rankings.
4. Three years is one regime, and a gold-bull one.

**None of this changes the two conclusions that matter:** Nippon's stack is not cheap, and stated ER does not predict realised drag.

### Model

`scratchpad/gold_drag.py` plus the ETF-pair runs. MFAPI FoF codes 115132/118663/119781/119788/120473/120531/120546/120685; ETF codes 140088/111954/113076/106193/107693/113434/115127/113049.

---

## 0.2 — Rebalancing mechanics under corrected tax · **COMPLETE**

**Question:** hold the gold sleeve at target by **trimming** it annually, or by **directing the monthly ₹75,000 SIP** to whatever is underweight and never selling?

**Method:** FIFO lot book per asset, gold LTCG 12.5% with **no ₹1.25L shelter** and 30% slab inside 24 months, equity LTCG 12.5% above a ₹1.25L annual exemption. Four strategies compared on terminal wealth **after a full liquidation**, so deferred tax is never mistaken for wealth. Run over the actual 74-month NAV path and over a forward 10-year grid. Target gold weight **10%** (₹7,500 of ₹75,000).

| Strategy | Mechanic |
|---|---|
| **FIXED** | ₹7,500/mo to gold forever, never rebalance |
| **FLOW** | Direct the ₹75,000 preferentially to whatever is underweight. Never sell |
| **BAND** | FLOW, plus trim only if gold breaches target +5pp at an annual check |
| **TRIM** | Annual reset to exact target, selling the overweight side |

### Result 1 — Historical path (2020-07 → 2026-08, 74 months, gold ran hot)

| Strategy | Net wealth | Tax during | End wt | Max wt | Max drift |
|---|--:|--:|--:|--:|--:|
| FIXED | ₹99,01,835 | ₹0 | 11.9% | 14.4% | 4.4pp |
| **FLOW** | **₹99,87,295** | **₹0** | 13.1% | 16.6% | 6.6pp |
| BAND | ₹99,87,295 | ₹0 | 13.1% | 16.6% | 6.6pp |
| TRIM | ₹99,41,562 | **₹32,415** | 10.3% | 15.8% | 5.8pp |

FLOW beat TRIM by **₹45,733** while paying **zero** tax along the way — but most of that gap is simply that FLOW ended holding more gold during a gold bull run, not a tax effect.

### Result 2 — Forward 10-year grid (net wealth, ₹ lakh)

| Equity | Gold | FIXED | FLOW | BAND | TRIM | FLOW−TRIM | FLOW drift |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 12% | 5% | 152.5 | 151.5 | 151.5 | 151.9 | −0.39 | 0.0pp |
| 12% | 8% | 154.2 | 153.9 | 153.9 | 154.0 | −0.19 | 0.0pp |
| 12% | 12% | 156.9 | 156.9 | 156.9 | 156.9 | +0.00 | 0.0pp |
| 12% | 18% | 162.3 | 161.5 | 161.5 | 161.5 | +0.04 | 0.0pp |
| 12% | 25% | 171.4 | 167.0 | 167.0 | 166.9 | +0.06 | 1.0pp |

### ⭐ Finding 1 — The choice of mechanic is worth ±0.26%. It is not a wealth decision.

Across the entire forward grid the four strategies land within **₹0.39 lakh on ~₹150 lakh**. The spread that *does* appear tracks nothing but how much gold each strategy happened to hold — FIXED wins when gold lags because it drifts *underweight*, and loses when gold runs. **That is a bet on gold wearing a rebalancing costume, not a rebalancing effect.**

> **Rebalancing mechanics should therefore be chosen on risk control and operational simplicity. There is no meaningful tax alpha here to harvest.**

### ⭐ Finding 2 — Flows are far more powerful than expected

Peak gold weight reached under FLOW, target 10%:

| Gold return | 5y | 10y | 15y | 20y |
|--:|--:|--:|--:|--:|
| 5% | 10.0% | 10.0% | 10.0% | 10.0% |
| 8% | 10.0% | 10.0% | 10.0% | 10.0% |
| 12% | 10.0% | 10.0% | 10.0% | 10.0% |
| 18% | 10.0% | 10.0% | 10.6% | 12.2% |
| 25% | 10.0% | 11.0% | **15.0%** | **21.7%** |

**Flows hold the target with zero measurable drift up to an 18%/yr gold regime sustained for a decade.** The reason is structural: the sleeve is only 10% of the book, so correcting its weight requires redirecting an amount that stays small relative to ₹9L/yr of contributions. Only a 25%/yr gold regime persisting 15+ years — the 2022–26 regime running four times as long — defeats it.

**Never selling therefore costs nothing in risk control**, which is the objection that would normally sink a no-sell policy.

### Finding 3 — This closes two earlier threads

1. **The 24-month FoF gate becomes entirely moot.** Phase 0.1 found it worth ₹525–₹1,959 *assuming annual trimming*. Under FLOW there are no metal sales at all, so it is worth **₹0**. The wrapper decision is now purely a cost decision — which strengthens 0.1's conclusion and makes the outstanding Nippon SID lookup the only thing still gating it.
2. **The ₹1.25L correction has little practical consequence.** It was right — §112A does not shelter metals — but the correct policy is not to realise metal gains at all, so the shelter's absence rarely bites.

### ⚠ Finding 4 — The annual check misses intra-year peaks

BAND returned results **identical to FLOW** on the historical path: gold peaked at 16.6% but never exceeded the 15% trigger *on an annual checkpoint*. A once-a-year look will miss real breaches. If a band is used as a backstop, check it **quarterly** and act annually.

### Verdict on 0.2

> **FLOW-rebalance the gold sleeve. Never sell gold to rebalance.**
>
> - Direct the monthly SIP to whatever is underweight. Zero tax, zero exit load, no gate exposure.
> - **Backstop:** if gold exceeds ~15% of the book (target +5pp), trim back to target. On the evidence this should almost never fire.
> - **Check quarterly, act at most annually** — Finding 4.
> - **Operational note:** the model re-optimises flows monthly, which is heavy in practice. **An annual reset of the SIP split captures nearly all of it**, given the drift headroom in Finding 2.
>
> **Secondary benefit:** MultiAsset's standing trigger — *"two consecutive missed years and the fund route becomes the better choice"* — is much easier to satisfy under FLOW. There is no sell decision, no capital-gains computation, and no exit-load window to track. **The DIY route's main practical weakness was rebalancing discipline; flow-rebalancing largely removes it.**

### ⚠ Limitations

1. **Assumes the SIP keeps running.** Flows are the entire rebalancing mechanism, so if contributions stop, only trimming remains. **Contributions are modelled flat at ₹75,000/month with no step-up** — confirmed by the user (Aug 9 2026) as the actual policy: increases will be **ad hoc, on salary rises, not a committed annual escalator**. This is the conservative case; any increase makes flows *more* powerful at holding the band, so the verdict holds a fortiori.
2. Forward grid uses constant returns; the historical path is a single realisation, and a gold-favourable one.
3. Equity is modelled as one asset. Rebalancing *within* the equity sleeves is a separate question this does not address.

### Model

`scratchpad/phase0_2.py` — FIFO lot books, monthly SIP, annual checkpoints, terminal full liquidation.

## 0.3 — Does silver earn a place? · **COMPLETE**

**Method:** MultiAsset Q1's whole-portfolio test, re-run against the **actual six-fund book** rather than the study's modelled 30/25/25/20 core. Core = Edelweiss US Tech 6.7 / PP 26.7 / BOI Flexi 13.3 / Invesco Mid 13.3 / DSP Small 24 / BOI Small 16. Each candidate added at **13.3% (₹10K of ₹75K)**, core diluted proportionally, annual rebalancing, daily MFAPI NAVs, rf 6.5%.

**Window constraint:** silver FoFs did not exist before **Feb 2022** (ICICI Pru Silver ETF FoF, the oldest and largest, inception 2022-02-02). MultiAsset tested three windows; **silver permits one, of 4.13 years.** Gold is run over the same window as the like-for-like control, and over the full 5.61-year core history for context.

### Result — Window S (2022-02-03 → 2026-08-07, 4.13y)

| Sleeve added at 13.3% | CAGR | Vol | Sharpe | **ΔSharpe** | MaxDD | **ΔDD** |
|---|--:|--:|--:|--:|--:|--:|
| **CORE (no sleeve)** | 18.93% | 14.44% | 0.86 | — | −18.54% | — |
| **Gold 100%** | 21.16% | **12.96%** | **1.13** | **+0.27** | **−14.73%** | **+3.82** |
| Gold 75 / Silver 25 | 21.57% | 13.35% | 1.13 | +0.27 | −15.10% | +3.44 |
| Gold 50 / Silver 50 | 21.98% | 13.86% | 1.12 | +0.26 | −15.58% | +2.97 |
| Gold 25 / Silver 75 | 22.37% | 14.44% | 1.10 | +0.24 | −17.71% | +0.83 |
| **Silver 100%** | **22.75%** | ⚠ **15.08%** | 1.08 | +0.22 | ⚠ **−19.74%** | ⚠ **−1.20** |
| Gold 60 / Debt 40 *(MultiAsset DIY)* | 19.74% | 12.70% | 1.04 | +0.18 | −15.17% | +3.37 |

**Standalone, same window:**

| Asset | CAGR | Vol | MaxDD | corr(core) | corr(PP) |
|---|--:|--:|--:|--:|--:|
| SBI Gold | 30.31% | **19.09%** | **−24.71%** | **+0.08** | +0.06 |
| ICICI Pru Silver FoF | 35.61% | ⚠ **34.49%** | ⚠ **−45.53%** | +0.16 | +0.13 |

### ⭐ Finding 1 — Silver fails at the job the ₹10K slot exists to do

**Silver 100% raises portfolio volatility above the core's own (15.08% vs 14.44%) and deepens max drawdown (−19.74% vs −18.54%).** It is the only candidate tested that makes the book *riskier*. Its Sharpe gain is entirely a return effect from a 35.61% CAGR run, not a diversification effect.

Structurally: silver runs **1.8× gold's volatility**, a **−45.53%** standalone drawdown, and **twice gold's correlation to the core** (+0.16 vs +0.08) — consistent with roughly half of silver demand being industrial. **It is a return-seeking asset, and this book does not need more return-seeking: 40% of flows already go to small cap.**

### ⭐ Finding 2 — Gold confirmed, and worth *more* here than the study measured

| Core used | ΔSharpe from a gold-bearing sleeve |
|---|---|
| MultiAsset's modelled core (20% international) | +0.20 / +0.11 / +0.08 across three windows |
| **The actual book (6.7% international, 40% small)** | **+0.27** |

The inference offered when this sleeve was first recommended — that the real book is more equity-concentrated than the study's model, so gold should be worth more, not less — **is now measured rather than assumed.**

### ⭐ Finding 3 — The case for gold is a *risk* case, not a Sharpe case

Both metals ran extraordinarily in this window. Haircutting **both** to a common CAGR, preserving volatility and correlation structure:

| Metals haircut to | Gold ΔSharpe | Gold ΔDD | Silver ΔSharpe | Silver ΔDD |
|---|--:|--:|--:|--:|
| *realised (30% / 36%)* | +0.27 | +3.82 | +0.22 | −1.20 |
| 20%/yr | +0.16 | +3.51 | +0.08 | −0.55 |
| 12%/yr | +0.07 | +3.20 | +0.01 | −0.19 |
| 8%/yr | +0.03 | +3.04 | −0.03 | −0.01 |
| 5%/yr | −0.01 | +2.91 | −0.06 | +0.13 |

**Two things to read here.**

**(a) The Sharpe gain is almost entirely regime.** At a gold return of ~8%/yr or below it vanishes. Anyone citing "+0.27 Sharpe" as the reason to hold gold is citing 2022–26.

**(b) ⭐ The volatility and drawdown reduction are regime-*independent*.** Gold cuts portfolio volatility to ~13.0% and max drawdown by ~2.9–3.8pp at **every** return assumption tested. That is the durable benefit, and Sharpe obscures it by mixing it with return.

> **The honest statement of the case: this sleeve buys ~1.5pp less portfolio volatility and ~3pp less drawdown, permanently. Whether it also raises risk-adjusted return depends on a view about gold that nobody has.**

**And the gold-vs-silver ordering is stable at every assumption** — gold > blends > silver, throughout. That ranking is not a product of the window.

### Finding 4 — The debt leg is rehabilitated, but on sizing grounds, not Sharpe

At realised returns, Gold 60/Debt 40 (+0.18) is clearly worse than pure gold (+0.27) — apparently confirming MultiAsset's "debt does nothing." **But under the haircut it converges and then inverts:** at 8%/yr both give +0.03; at 5%/yr the debt version wins (+0.01 vs −0.01). Debt's stabilising role matters more precisely when gold is not compounding.

Separately: **pure gold at ₹10,000 puts gold at 13.3% of flows, above MultiAsset's own recommended 8–12% band.** A debt leg is one way to bring it into band — ₹7,500 gold / ₹2,500 debt gives gold 10%.

### ⚠ Correction to the recommendation made before this study existed

The ₹6,000 gold / ₹4,000 debt split proposed earlier was scaled off MultiAsset's 12/8 basket. **Measured on the actual core it is not the best use of the ₹10K** — it gives up roughly a third of the drawdown benefit and, at anything above an 8%/yr gold assumption, most of the Sharpe gain. Gold-weighted is better; the exact split is a sizing judgement, not a modelling result.

### Verdict on 0.3

> **GOLD ONLY. Silver does not earn a place in this slot.**
>
> Silver is excluded not because it performed badly — it had the best CAGR of anything tested — but because **it makes the book more volatile and more drawdown-prone, which is the opposite of what the ₹10K is for.**
>
> **Universe scoping:** the 15 silver FoFs, the silver ETFs, and the 3 combined gold+silver FoFs all leave the study. **Phase 1 screens gold vehicles only** — roughly 13 gold FoFs and 12–14 gold ETFs, pending the wrapper resolution in 0.1.
>
> *Marginal note:* a **25% silver tilt inside the sleeve is roughly Sharpe-neutral** (+0.27 preserved, +0.41pp CAGR, −0.37pp drawdown) at realised returns, and degrades under haircut. It is defensible but adds a second scheme to monitor at ₹2,500/month for a marginal gain. **Not recommended; recorded so the option is not silently dropped.**

### ⚠ Limitations

1. **One window, 4.13 years.** MultiAsset used three; silver data does not exist earlier. Silver's verdict rests on a single regime — though it *failed during its own bull market*, which strengthens rather than weakens it.
2. **No severe equity bear in the window.** Core max drawdown was −18.54% (the Sep-2024 → Mar-2025 correction), not a 2018 or 2020 scale event. Gold's cushioning is untested here against a real crash on this core.
3. **Both metal legs are FoFs**, so each scheme's own tracking difference is embedded in these numbers. Module 1's job.
4. Sharpe uses rf 6.5%; **deltas** are insensitive to that choice, levels are not.

### Model

`scratchpad/phase0_3.py` (whole-portfolio test) and `phase0_3b.py` (regime haircut). MFAPI codes — core: 148063, 122639, 148404, 120403, 119212, 145678; gold 119788; silver 149775; debt 119016.

## 0.4 — SGB secondary market in/out · **COMPLETE**

**Question:** with new issuance discontinued, does buying Sovereign Gold Bonds on the NSE/BSE secondary market belong in the gold universe?

SGBs deserved a real hearing rather than a dismissal, because they carry **a 2.5% coupon that no fund vehicle has** — nominally a ~3pp/yr swing against a gold FoF's expense drag. Measured, that headline does not survive.

### ⚠ Finding 1 — Budget 2026 killed the marquee benefit for anyone buying now

**Effective 1 April 2026, the capital-gains exemption on SGB redemption applies only to bonds subscribed by an individual at original issue and held continuously to maturity.** Bonds acquired by transfer or purchase in the secondary market are excluded. *(Provision: s.70(1)(x) of the Income Tax Act 2025, previously s.47(viic) of the 1961 Act.)*

**A secondary-market buyer's redemption at maturity is now taxed at 12.5% LTCG — identical to a gold ETF.** The single feature that historically made SGBs the best gold vehicle in India is unavailable on the only route still open. **⚠ Verify with a CA before acting; this took effect four months before this analysis.**

### ⭐ Finding 2 — The 2.5% coupon is not 2.5%

**The coupon is paid on the bond's nominal (original issue) value, not on market value.** Gold has multiplied since most tranches were issued, so the yield on what a buyer actually pays today has collapsed:

| Tranche | Issue ₹/g | Matures | Residual | Coupon ₹/g | **Yield on market** | **Net of 30% slab** |
|---|--:|--:|--:|--:|--:|--:|
| 2019-20 Ser V | 3,788 | 2027.9 | 1.3y | 95 | 0.60% | 0.42% |
| 2020-21 Ser IV | 4,852 | 2028.6 | 2.0y | 121 | 0.77% | 0.54% |
| 2021-22 Ser VII | 4,761 | 2029.9 | 3.3y | 119 | 0.75% | 0.53% |
| 2022-23 Ser II | 5,091 | 2030.6 | 4.0y | 127 | 0.81% | 0.56% |
| 2023-24 Ser III | 6,199 | 2031.9 | 5.3y | 155 | 0.98% | 0.69% |
| **2023-24 Ser IV** *(last ever)* | 6,263 | 2032.2 | **5.6y** | 157 | 0.99% | **0.69%** |

*Spot ₹15,775/g, indicative from March-2026 press; re-verify at the current level.*

**Net coupon of 0.42%–0.69% roughly cancels a gold FoF's all-in expense drag (0.30%–0.87%). It does not beat it.** And the relationship is perverse: the better gold performs, the more the coupon dilutes.

### Finding 3 — The discount is the only genuine remaining edge

SGB series were quoted at ₹15,200–15,700 against spot ₹15,775 — **discounts of 0.48% to 3.65%**, a consequence of thin secondary liquidity. Held to maturity the bond redeems at gold value, so the discount is captured:

| Purchase price | Discount | Annualised over a 4y residual |
|---|--:|--:|
| ₹15,700 | 0.48% | 0.12%/yr |
| ₹15,500 | 1.74% | 0.44%/yr |
| ₹15,200 | 3.65% | 0.93%/yr |

**Total edge over a 0.30% all-in gold FoF: roughly +0.3% to +1.3%/yr** — *before* entry costs. Against that, liquidity is severe: **100–150 bonds/day in a typical series, and ~₹13.4 Cr/day of combined traded value across every SGB series on both exchanges.** Bid-ask on a thin series can consume most of the discount on the way in.

### Finding 4 — Three structural disqualifiers for *this* sleeve

Even taking the residual edge at face value, SGBs cannot do the job the ₹10K slot requires:

1. **⚠ No SIP is possible.** Purchases are manual exchange orders into an illiquid book at whatever price clears. The sleeve is a monthly contribution.
2. **⚠ Maximum residual tenor is 5.6 years.** The last tranche ever issued matures Feb 2032; everything else sooner. The sleeve is a **10+ year hold**, so every bond matures mid-horizon and forces reinvestment — into a gold fund, which is where the study was heading anyway.
3. **⚠ It breaks Phase 0.2's rebalancing policy.** Flow-rebalancing requires directing small monthly amounts into the sleeve. A lumpy, illiquid, maturity-fragmented instrument cannot absorb ₹7,500/month at a controlled price.

### Verdict on 0.4

> **OUT. SGBs are formally excluded from the study universe.**
>
> Not because they are a poor gold vehicle — held from original issue to maturity they were the best one available in India — but because **the tax exemption that made them so is closed to secondary buyers as of April 2026, the coupon is worth 0.42–0.69% net rather than 2.5%, and the instrument cannot be bought monthly or held for the sleeve's full horizon.**
>
> *Recorded for completeness:* for a **lump sum** with a horizon that matches a specific tranche's maturity, the discount-plus-coupon edge is real and worth roughly +0.3% to +1.3%/yr. That is a different decision from this one, and it is not the ₹10,000/month sleeve.

---

## Phase 0 — Consolidated verdict

| # | Question | Verdict |
|---|---|---|
| **0.1** | ETF or FoF? | ⚠ **Both remain in scope** — a pure cost decision, gated on one SID lookup (Nippon's underlying ETF ER, 0.25% vs 0.82%, which flips it by ₹28,000) |
| **0.2** | How to rebalance? | ✅ **Flow-rebalance, never sell gold.** Backstop trim only above ~15% of book; check quarterly, act annually |
| **0.3** | Gold, silver, or both? | ✅ **Gold only.** Silver raises portfolio volatility above the core's own and deepens drawdown |
| **0.4** | SGB secondary market? | ✅ **Out** |

**Universe for Phase 1:** gold FoFs (~13) and gold ETFs (~12–14). Silver (15 FoFs + ETFs), combined gold+silver FoFs (3), and SGBs are all excluded. **The screen cannot start until the 0.1 SID lookup resolves**, since it decides which of the two wrapper universes is screened.

**One consequence worth carrying forward:** 0.2 showed the sleeve should never be sold, which makes the 24-month FoF tax gate worth ₹0 and removes the last non-cost consideration from 0.1. **The wrapper question is now entirely "which stack is cheaper," and nothing else.**

---

## Corrections to carry back

| Document | Correction |
|---|---|
| `PreciousMetals/study_plan.md` framing fact 3 | ⚠ **Wrong.** The wrapper decision does *not* dominate via the tax gate; the gate is worth ₹525–₹1,959. The wrapper decision is a pure cost decision worth ₹3K–28K. **Applied.** |
| `PreciousMetals/study_plan.md` Phase 0 framing | 0.1 is no longer "the highest-value analysis." **0.3 (silver) now is** — it decides the asset, which is a bigger question than the wrapper. |
| `MultiAsset/decision_tree.md` Q5 caveat 3 | Gold **FoFs** carry a 24-month gate, not 12 (ETFs: 12). *Not yet applied.* |
| `MultiAsset/decision_tree.md` Q2 & Q5 caveat 2 | The ₹1.25L exemption does not apply to metals at all. *Not yet applied.* |

---

*Phase 0.1 completed August 9, 2026 | Verdict PROVISIONAL — gated on one SID lookup | All cost inputs aggregator-sourced and unverified*
