# Deep Study Plan — Precious Metals (Gold & Silver)

## Context

Sixth category study, following the established pipeline: **screen the universe → shortlist → module-wise deep study per scheme → decision tree**. It is commissioned by the MultiAsset decision tree, which concluded that *"the portfolio needs the non-equity exposure and does not need a multi-asset fund to get it"* and specified a DIY gold leg at 8–12% of portfolio — without ever studying which gold vehicle to use.

**Investment goal (confirmed):** the **₹10,000/month** open slot in the ₹75,000 SIP, sourced from SmallCap (DSP 18→12, BOI Small 12→8). 10+ year horizon, annual rebalancing. This is the sleeve `Personal Finance/mutual_fund_sip_decisions_2026-07.md` §4b leaves undecided.

> **⚠ This study breaks the 6-module framework, deliberately.** The four equity studies and MultiAsset all measure *manager skill* — stock selection, allocation timing, team quality. **There is no manager skill in this category.** Every gold scheme holds the same metal at the same price. Forcing six modules here would manufacture false depth. **This plan proposes five modules, re-scoped and re-weighted.** Scores will not be comparable to any prior study.

---

## The five framing facts (read first — each rewrites a module)

**1. There is no alpha, and no benchmark-construction problem — there is only leakage.**
Returns are the domestic gold (or silver) price, identical across every scheme up to tracking difference. The entire performance question collapses to a single measurable number: **how much of the metal's return failed to reach you.** Module 1 is that number and nothing else.

**2. ⚠ Screening on returns would be a category error.** Ranking these schemes on 1Y/3Y CAGR ranks the gold price and each scheme's launch date — pure noise. The MultiAsset study's finding #5 (ICICI eliminated on a bad Sharpe reading) is the precedent for how a wrong screen poisons a whole study. **Stage 2 here screens on tracking difference, never on return.**

**3. ⚠ ~~The wrapper decision dominates via the tax gate.~~ CORRECTED Aug 9 2026 — this was wrong.**
~~The ETF-vs-FoF LTCG gate is worth multiples of the ER spread.~~ **Phase 0.1 measured it: the 12-vs-24-month gate is worth ₹525–₹1,959 over ten years**, because FIFO means every rebalance from the third onward sells units that are long-term under either gate. **The wrapper decision is a pure *cost* decision** — FoF layer ER versus ETF trading friction plus demat charges — **worth ₹3,000–₹28,000 over ten years (0.2%–1.9% of terminal corpus).** Phase 0 still runs first, because it scopes the universe; but it is no longer the study's highest-value analysis. **Phase 0.3 (does silver earn a place?) now is.** See [phase0_wrapper_and_asset.md](phase0_wrapper_and_asset.md).

**4. ⚠ Published expense ratios are the FoF layer only.** The underlying ETF's ER sits beneath and is never in the aggregator number. A scheme quoted at 0.05% is not a 0.05% product. Every cost figure in this study must be the **two-layer all-in stack, sourced from the SID**, or it is unusable. Aggregator data already self-contradicted during preliminary work (Nippon gold 0.05% vs 0.10%; ICICI 0.18% vs 0.20%; LIC 0.30% vs 0.35%).

**5. Silver is unstudied and must not be assumed to behave like gold.** MultiAsset's decorrelation finding was measured on **gold** NAVs. Silver carries roughly half its demand from industrial use, giving it an equity-cycle sensitivity gold lacks, at materially higher volatility. **Nothing in this repo establishes that silver plays the same portfolio role.** Phase 0.3 tests it before any silver scheme is screened.

---

## ⚠ A correction this study must carry back

Preliminary verification found two errors in inherited material. Both are recorded here because Module 3 depends on them:

| Claim | Where | Status |
|---|---|---|
| Gold ETFs get 12.5% LTCG after **12 months** | MultiAsset `decision_tree.md` Q5 caveat 3 | ✅ True **for the ETF**. ⚠ **False for the FoF wrapper** — unlisted units carry a **24-month** gate |
| DIY rebalancing drag is *"largely absorbed by the ₹1.25L LTCG exemption"* | MultiAsset `decision_tree.md` Q2, Q5 caveat 2 | ⚠ **Does not hold for the metal leg.** The ₹1.25L exemption is a §112A benefit for listed equity only. Gold and silver gains get **no exemption at all** |

**Implication:** MultiAsset's modelled DIY rebalancing drag is understated for the gold leg. It does not overturn the DIY verdict (the margin is far too wide), but Phase 0.2 must re-model it without the exemption. *Both items to be verified with a CA before acting — tax treatment here changed twice between 2024 and 2025.*

---

## Phase 0 — The Prior Questions (NOT deferred)

MidCap and MultiAsset both deferred Phase 0 to decision-tree time and it worked, because in those studies the prior question was *"does this sleeve earn a slot?"* — answerable only after the funds were known. **Here the prior question determines what the universe even is.** If the wrapper answer is ETF, the entire FoF universe is out of scope. Phase 0 runs first.

| # | Question | Method | Decides |
|---|---|---|---|
| **0.1** | **Wrapper: ETF or FoF?** | Model 12 monthly buys + one annual rebalance over 10Y at ₹10K/mo. **ETF cost** = single-layer ER + realised bid-ask spread + premium/discount to iNAV on each buy (NSE/BSE bhavcopy vs iNAV). **FoF cost** = two-layer ER + the 24-month gate forcing slab-rate tax on units under 2 years old at rebalance. | Which wrapper's universe gets screened. **The single highest-value analysis in the study** |
| **0.2** | **Rebalancing mechanics under the corrected tax** | Re-model MultiAsset's annual rebalance with **no ₹1.25L shelter on the metal leg**. Test the alternative: rebalance by *adjusting equity SIP flows* rather than trimming metal, which defers the metal gain indefinitely. | Whether the sleeve is ever sold at all — which in turn may make the FoF's 24-month gate moot |
| **0.3** | **Does silver earn a place?** | The MultiAsset whole-portfolio test, re-run: add silver, and gold+silver blends, at 13.3% to the **actual** core (Intl 6.7 / Flexi 40 / Mid 13.3 / Small 40 — not the study's modelled 30/25/25/20), across the same three windows. Report Sharpe delta, volatility, max drawdown, and correlation to PP FlexiCap. | Gold-only vs gold+silver vs combined-FoF — i.e. the asset mix of the ₹10K |
| **0.4** | **SGB secondary market — in or out?** | Availability, on-exchange liquidity and typical premium/discount for residual-tenor tranches; whether the tax-free-at-maturity benefit survives a secondary purchase. **New issuance is discontinued** (no tranche since Feb-2024 Series IV; confirmed at the Feb-2025 post-Budget briefing). | Whether a fourth wrapper enters the screen or is formally excluded with reasons |

> **Deliverable:** `phase0_wrapper_and_asset.md` with a locked verdict on **(a) wrapper, (b) gold-only vs gold+silver and the ratio, (c) SGB in/out**. Every subsequent phase is scoped by it.

> **⚠ Phase 0 can end the study.** If 0.1 returns "ETF" and 0.3 returns "gold only", the universe collapses to ~12 gold ETFs and the remaining work is a two-week screen, not a six-module study. That is a legitimate and welcome outcome.

---

## Phase 1 — Screening Pipeline

### Universe (~44 schemes, Direct/Growth)

| Segment | Count (preliminary) | Notes |
|---|---|---|
| Gold FoF / gold savings funds | ~13 named + HSBC, Kotak | Nippon, Quantum, UTI, Groww, Axis, ICICI, HDFC, ABSL, SBI, Tata, LIC, HSBC, Kotak |
| Gold ETFs | ~12–14 | Requires NSE/BSE data, not MFAPI |
| Silver FoF | 15 | Axis, Bandhan, UTI, Edelweiss, Groww, ICICI, Angel One, Zerodha, HDFC, Nippon, Tata, Kotak, SBI, ABSL, DSP |
| Silver ETFs | ~10–12 | Category permitted from SEBI's late-2021 framework |
| Combined gold+silver FoF | 3 | Axis, Motilal Oswal, Edelweiss |

Preliminary counts are from aggregators and are **indicative only** — the authoritative universe is the AMFI scheme list. Save the raw pull to `Mutual Fund/TickerTape Data/PreciousMetals_<date>.csv`.

### Stage 1 — Hard Filters

| Filter | Threshold | Rationale | vs prior studies |
|---|---|---|---|
| **Wrapper match** | Must match the Phase-0.1 verdict | Scoping filter, applied first | **New** — no analog |
| **Asset match** | Must match the Phase-0.3 verdict | Ditto | **New** |
| Track record | **≥ 36 months** | Needed for a 3Y tracking-difference series. Silver ETFs mostly launched 2022+, so this is the binding constraint on that segment; sub-36mo schemes carry a `short-history` flag | Same floor as MultiAsset |
| **Underlying ETF AUM** | **≥ ₹300 Cr** | For a FoF, the *underlying* ETF's size governs on-exchange liquidity and therefore the premium the FoF pays. **The FoF's own AUM is nearly irrelevant** and must not be used | **New — inverts the usual AUM filter** |
| **All-in cost stack** | **≤ 1.00%** (both layers, SID-sourced) | A ceiling, not a ranker. Above this the vehicle cannot deliver the metal's return well enough to matter | **New calibration** |
| Direct plan + SIP available at ≤ ₹1,000 | Binary | ₹10K/mo needs a monthly SIP, not lump-sum-only | **New** |

**Not used as filters:** returns of any period (framing fact 2), FoF-level AUM, star ratings, AMC brand.

### Stage 2 — Tracking Fidelity Filter *(the only performance screen)*

| Filter | Threshold | Rationale |
|---|---|---|
| **Tracking difference vs domestic metal price, 3Y annualised** | **Better than universe median** | The category's entire performance question. Signed (not absolute) — persistent shortfall is the defect |
| **Tracking difference, 1Y** | Better than universe median | Catches schemes whose 3Y number is carried by a stale, since-raised ER |
| **Tracking error (σ of daily differences)** | **≤ universe 75th percentile** | Consistency of the tracking, distinct from its level. A scheme that tracks well on average via offsetting errors is worse than its TD suggests |

**Benchmark construction (the study's main data risk):** there is no free, clean domestic gold price series. Candidates, in order of preference — (a) **IBJA AM/PM rates**, the industry reference; (b) **MCX spot**; (c) LBMA price × RBI reference rate + import duty + GST, rebuilt. **Pick one, document it, use it for every scheme.** A different benchmark changes every TD number, so it must be chosen once and never varied. *Expect this to be the slowest part of Phase 1.*

**Expected funnel:** ~44 → Stage 1 (wrapper/asset scoping does most of the cutting) → ~12–15 → Stage 2 → **3 finalists.**

### How the three finalists are chosen

Phase 0 leaves one or two surviving **(asset × wrapper)** cells. The three are drawn as:

- **One cell surviving** (e.g. gold-only + FoF) → the top three on Stage-2 tracking fidelity.
- **Two cells surviving** (e.g. gold + silver) → the top scheme in each cell, plus the next-best on combined rank — **or** substitute a combined gold+silver FoF as the third, so the one-ticket structure gets tested against the two-ticket build.

> ⚠ **At ₹10,000/month you will hold one or at most two of these.** `Portfolio/allocation_options.md` sets the floor at **~₹1,000–2,000/scheme** before a split stops being worth the monitoring. Three are studied to make the choice evidenced; three are not bought.

### Deliverables

`screening/methodology.md`, `screening/stage1_hard_filters.md`, `screening/stage2_tracking.md`, `screening/all_schemes_data.md` — plus a **benchmark-construction note** recording the chosen domestic price series and why.

---

## Phase 2 — The Five Modules

### Proposed weights — ⚠ OPEN, to lock before Phase 2

| Module | Weight | Why |
|---|---:|---|
| **1 — Tracking Fidelity** | **35%** | The realised outcome. Everything else is a driver of this |
| **2 — Cost Stack (forward)** | **20%** | What you will pay going forward, independent of what leaked historically |
| **3 — Wrapper, Tax & Liquidity** | **20%** | Where the largest rupee differences actually live |
| **4 — Structural & Operational Integrity** | **15%** | Custody, purity, audit — the tail risk that never shows in NAV until it does |
| **5 — AMC & Scheme Viability** | **10%** | Mostly carry-forward from five prior studies |

**Scale:** 1 = Poor · 2 = Below Avg · 3 = Average · 4 = Good · 5 = Excellent

> ⚠ **Known methodological hazard — M1 and M2 are correlated by construction.** Realised tracking difference *contains* the cost stack. Scoring both risks double-counting cost at 55% of the total. **The separation is deliberate and must be maintained in the writing:** M1 is strictly **backward-looking and realised** (what actually leaked, from NAV vs benchmark); M2 is strictly **forward-looking and structural** (the current two-layer stack, ER trajectory, and whether the historical TD is repeatable). A scheme with excellent M1 and poor M2 has a stale advantage — that divergence is a *finding*, not an averaging problem. **The decision tree must read the two side by side, not sum them.**

---

### Module 1 — Tracking Fidelity (35%)

The only performance module. **Do not report CAGR as a merit; report it once for context and move on.**

1. **Tracking difference** — annualised, signed, over 1Y / 3Y / 5Y / since-inception, vs the Phase-1 benchmark series.
2. **Tracking error** — standard deviation of daily return differences; and lag-1 autocorrelation to catch stale NAV marking (the **NAV smoothing test** MultiAsset introduced for Nippon).
3. **TD decomposition** — how much of the shortfall is explained by the disclosed two-layer ER, and how much is *unexplained*. Unexplained leakage is cash drag, ETF premium paid by the FoF, or operational slippage. **A scheme whose TD materially exceeds its stated cost stack is the key negative finding this module can produce.**
4. **Stability over time** — TD by calendar year. Deteriorating fidelity is worse than a consistently mediocre level.
5. **Behaviour in stress** — TD during **Q1-2026 (gold −24.71%)** and during **2025's +71.85% run**. Vehicles often track well in calm markets and slip at the extremes; this sleeve exists precisely for the extremes.

**Scorecard:** 3Y TD vs universe median (Critical) · 1Y TD (Critical) · tracking error (High) · unexplained leakage vs stated cost (Critical) · TD stability by year (High) · stress-window fidelity (High) · NAV-smoothing test pass/fail (Modifier).

---

### Module 2 — Cost Stack, Forward (20%)

1. **The two-layer stack, SID-sourced** — FoF ER **+** underlying ETF ER, stated separately and summed. For an ETF wrapper: single ER + the modelled trading cost from Phase 0.1. **An aggregator figure is not acceptable evidence here.**
2. **ER trajectory** — 3-year history of both layers. MultiAsset found **five stale expense ratios** across seven funds; assume the published number is wrong until the SID confirms it.
3. **Waivers and their durability** — some AMCs waive the FoF layer. Is it contractual or discretionary, and has it been withdrawn before?
4. **Exit load** — structure and window. Directly taxes the annual rebalance.
5. **Ten-year rupee cost** at ₹10,000/month against the cheapest surviving alternative — the number that actually decides this module.

**Scorecard:** all-in stack vs universe (Critical) · SID-verified vs aggregator-only (Critical — unverified caps the score at 3) · ER trajectory (High) · waiver durability (Medium) · exit load (Medium) · 10Y rupee cost (High).

---

### Module 3 — Wrapper, Tax & Liquidity (20%)

Where Phase 0's verdict gets applied scheme by scheme.

1. **LTCG gate** — 12 months (listed ETF) vs 24 months (unlisted FoF units), 12.5% without indexation above it, **slab below it**, and **no ₹1.25L exemption in either case**.
2. **Rebalance interaction** — under the Phase-0.2 mechanics, model the actual tax cost of this specific wrapper across a 10-year hold with annual rebalancing.
3. **For ETFs:** realised bid-ask spread, average daily traded value, and **premium/discount to iNAV** across a sample of trading days. A thin ETF's persistent premium is a real, recurring cost that never appears in its ER.
4. **For FoFs:** the underlying ETF's liquidity, since the FoF pays that premium on your behalf — and whether the AMC uses in-kind creation to avoid it.
5. **Redemption mechanics and settlement timing** — T+ cycle, cut-off times, and any gating.

**Scorecard:** LTCG gate fit to the rebalancing plan (Critical) · modelled 10Y wrapper tax cost (Critical) · liquidity/impact cost (High) · premium-discount behaviour (High) · redemption mechanics (Medium).

---

### Module 4 — Structural & Operational Integrity (15%)

The module that replaces "Fund Manager". No skill to assess — **custody and purity instead.**

1. **Physical backing** — is the scheme backed by allocated physical metal, or does it use futures/ETCDs? Futures introduce roll drag and a wholly different risk profile.
2. **Custodian and vaulting** — who holds the metal, where, and under what segregation.
3. **Purity standard** — LBMA Good Delivery (995 gold / 999 silver) conformity, and the SID's stated standard.
4. **Independent physical verification** — frequency of auditor confirmation of the bullion, and whether results are published.
5. **Creation/redemption mechanism** — cash vs in-kind, and the authorised participant bench. A single AP is a concentration risk.
6. **⚠ Silver-specific:** silver's bulk-to-value ratio is roughly 80× gold's, making storage cost and vault capacity a real constraint rather than a formality. Check disclosed storage charges separately.

**Scorecard:** physical vs derivative backing (Critical) · custodian quality & segregation (High) · purity standard (High) · audit frequency & disclosure (High) · AP bench depth (Medium) · storage cost disclosure (Medium, weighted up for silver).

---

### Module 5 — AMC & Scheme Viability (10%)

**Carry-forward first** — the AMC bench across five studies already covers ICICI, HDFC, Nippon, SBI, Kotak, DSP, Edelweiss, Axis, ABSL, UTI, Quant, Motilal, Tata. Reuse those assessments; do not re-derive.

Precious-metals-specific additions:
1. **Passive-franchise commitment** — is the AMC's passive desk a serious operation or a shelf-filler? A neglected FoF drifts on cost and tracking.
2. **⚠ New-entrant AMCs** — Groww, Zerodha, Angel One appear in this universe and in **no prior study**. They have no bench entry, short operating histories, and small AUM. Score them on operating record, not on brand novelty.
3. **Scheme viability** — a sub-₹100 Cr FoF risks merger or wind-up; note the AUM trend, not just the level.
4. **Regulatory record** — standard SEBI check, and specifically any action relating to the AMC's ETF or commodity operations.

---

## Study Order (set post-screening)

1. **The longest, cleanest tracking record first** — builds the benchmark apparatus and the TD reference frame for the other two.
2. **The screening leader second** — test whether its fidelity is genuine or an artefact of a stale ER.
3. **The structural contrast third** — the other wrapper, the other metal, or the combined FoF, so the Phase-0 verdict gets stress-tested rather than assumed.

---

## Phase 3 — Decision Tree

`decision_tree.md` answers, in order:

1. **Asset:** gold only, or gold + silver, and at what ratio — with the Phase-0.3 whole-portfolio evidence, run against the *actual* four-sleeve core.
2. **Wrapper:** ETF or FoF, with the 10-year modelled cost and tax difference in rupees.
3. **Scheme:** which one of the three, and whether a second is worth holding at ₹10,000/month given the ₹1,000–2,000 floor.
4. **Sizing and mechanics:** the split of the ₹10K, SIP date, step-up treatment, and **the rebalancing rule** — flow-adjustment vs trimming, per Phase 0.2.
5. **Review triggers:** ER drift on either layer, tracking difference deterioration, underlying ETF liquidity decline, custodian or audit change, tax-regime change, scheme merger/wind-up, and the standing gold-weight-drift trigger inherited from MultiAsset.
6. **Feed:** `Portfolio/allocation_options.md` and `Personal Finance/mutual_fund_sip_decisions_2026-07.md` §4b, which this study closes.

---

## Data Sources

| Source | What to pull |
|---|---|
| **AMFI scheme list** | The authoritative universe — not aggregators |
| **MFAPI** | FoF NAV history → TD, tracking error, rolling series |
| **NSE/BSE bhavcopy + iNAV** | ETF market price, traded volume, premium/discount — **required for Phase 0.1; MFAPI cannot supply it** |
| **IBJA / MCX** | The domestic metal benchmark series |
| **SID + SAI + monthly factsheet** | ⭐ **Two-layer ER, custodian, purity standard, audit policy, exit load, backing mechanism.** The only acceptable source for cost |
| Prior repo studies | AMC carry-forward (Module 5) |
| CBDT / SID / a CA | Tax treatment confirmation — **changed twice 2024–25; do not rely on this plan's summary** |
| SEBI / NSE / BSE | Regulatory actions |

Aggregators (Tickertape, Groww, Value Research) are permitted for **universe discovery only** and must not source any scored number. This is a hard rule carried from MultiAsset's finding #6.

---

## Execution Checklist

- [ ] **Lock:** module count (5, not 6) and the proposed weights (35/20/20/15/10)
- [x] **Phase 0.1:** ETF-vs-FoF cost + tax model → **provisional; a pure cost decision, gated on one SID lookup.** Tax gate found worth ₹525–₹1,959 (framing fact 3 corrected)
- [x] **Phase 0.2:** rebalancing → **FLOW-REBALANCE, never sell gold.** Mechanic worth ±0.26%; flows hold the target to 18%/yr gold over a decade. Makes the 24-mo gate worth ₹0
- [x] **Phase 0.3:** silver whole-portfolio test vs the actual core → **GOLD ONLY.** Silver raises portfolio vol above the core's own and deepens drawdown. Gold's benefit is a *risk* benefit, regime-independent (~3pp drawdown); its Sharpe gain is not
- [x] **Phase 0.4:** SGB → **OUT.** Budget-2026 removed the secondary-buyer exemption; coupon is 0.42–0.69% net, not 2.5%; no SIP; ≤5.6y residual tenor
- [x] **Phase 0:** [phase0_wrapper_and_asset.md](phase0_wrapper_and_asset.md) → **universe locked to gold FoFs + gold ETFs**
- [x] **⚠ BLOCKER — CLEARED Aug 9 2026 (Phase 0.1b), by measurement rather than disclosure.** Nippon's FoF layer is genuinely ~0.01–0.06%, but **Gold BeES is the 2nd-worst tracker of 8 gold ETFs** (0.34pp/yr behind ICICI's) — so the stack is not cheap and the "FoF wins" scenario is falsified. **⭐ Stated ER does not predict realised drag: the cheapest stated layer (Nippon 0.05%) ranked 7th of 8 on realised 3y tracking.** Screening on published ERs would pick the wrong fund. Both wrapper universes proceed to Phase 1, screened on measured tracking difference
- [x] **Phase 1 prerequisite:** split-adjust ETF NAV series — **10 schemes carried splits**; detector built, all fall outside the 3y window
- [x] **Phase 1:** benchmark — no free IBJA/MCX feed, so **median-proxy anchored by four-ETF ER triangulation → gross gold 35.26%** (anchor spread only 0.17pp). ⚠ estimate; a real series must supersede it
- [x] **Phase 1:** universe pull from AMFI (44 schemes) → [screening/](screening/)
- [x] **Phase 1:** Stage 1 (44→20) → Stage 2 (→8) → **3 finalists: ICICI Gold ETF · ICICI Pru Gold FoF · ABSL Gold ETF**
- [x] **⭐ Nippon closed independently:** Gold BeES TD **0.76%**, FoF 0.77% → **the 0.82% figure is right, 0.25% is wrong.** Both Nippon vehicles fail Stage 2
- [x] **⚠ Two measurement artefacts found:** daily TE penalises FoFs as a class (lag artefact → TE now measured **monthly**); three schemes report **physically impossible** tracking (UTI FoF, SBI Fund, Quantum FoF) and are excluded on integrity, not merit
- [x] **Stage 3 robustness** ([screening/stage3_robustness.md](screening/stage3_robustness.md)) — single-window screen re-run over **19 overlapping 3y windows, 2014-06 → 2026-08**. Ranking moved; shortlist revised to **ICICI Gold ETF · ICICI Pru Gold FoF · Kotak Gold ETF** (ABSL ETF co-equal reserve)
- [x] **⚠ Self-correction:** the "impossible tracking" exclusions were **noise, not corruption** — a ±20-day window shift swings the implied FoF layer 0.26–0.45pp, more than the signal. The methodology §3b consistency check is **withdrawn**. Quantum Gold FoF's 0.31% was noise (true median 0.63%) and displaces nobody
- [x] **⚠ Signal/noise is only 2.5×** (median spread 1.00pp vs typical IQR 0.40pp) — schemes within ~0.4pp are indistinguishable. **Module 1 must not over-read small TD gaps**
- [x] **⚠ Access constraint found:** six AMCs restricted gold-scheme subscriptions from June 2026 (HDFC, ICICI, Nippon, Tata, Axis, ABSL); category AUM +195% YoY to ₹1.85L Cr; import duty 6%→15%. **Does not bind at ₹7,500–10,000/mo** — caps target ₹25 Cr institutional and ₹10L/mo FoF lump sums. **New annual review trigger**
- [x] **Stage 4 — split estimator corrected** ([screening/stage4_corrected.md](screening/stage4_corrected.md)). My own adjustment was buggy: it divided by the raw NAV ratio on split days, baking that day's gold move into the factor (**ICICI off by 8.20%, Axis by 2.70%**). **Axis Gold ETF moved 1.29% → 0.51% — never a bad tracker, just a badly adjusted series.** Axis exclusion **withdrawn**
- [x] **⭐⭐ CATEGORY-DEFINING FINDING: the ranking is noise.** Corrected, the between-scheme spread is **0.42pp** against a within-scheme IQR of **0.43pp** — **signal/noise 1.0×**. No gold vehicle is distinguishable from another on tracking difference. Third such outcome in the repo after MidCap's "no significant alpha" and MultiAsset's "no allocation alpha"
- [x] **⚠ Module 1 must be re-scoped.** It carries 35% weight to measure something that does not vary between schemes. Re-weight toward Modules 2–4, or narrow Module 1 to *dispersion/consistency* rather than level
- [x] **⚠ The ER-anchored benchmark is partly circular** — gross gold ≡ mean(anchor CAGR + anchor ER), which forces each anchor ETF's TD toward its own stated ER. ICICI's leading 0.49% vs a stated 0.50% is near-definitional, **not independent evidence**. A true IBJA/MCX series is now a **hard prerequisite**, not an improvement
- [ ] **⚠ Still open before Phase 2:** real IBJA/MCX benchmark (blocking); **AMFI scheme-wise AUM — endpoint 404s, needs a manual pull**; SBI Gold Fund still impossible (−0.42%) and not split-related — its ETF needed no correction and is internally coherent (TD 0.72% vs stated ER 0.70%), so the FoF series is untrustworthy; **excluded, unexplained**
- [x] **Phase 2 — DELIBERATELY NOT RUN.** 70% of its module weight is either proven non-discriminating (Module 1) or already settled in Phase 0 (Modules 3, 5). Running 15 module documents to separate vehicles that differ by less than measurement error would manufacture false precision. Precedent: MidCap's co-equal index default, MultiAsset's DIY outcome
- [x] **Phase 3:** [decision_tree.md](decision_tree.md) — **gold only · FoF on mechanics · any large cheap physically-backed vehicle · ₹7,500 gold + ₹2,500 debt · flow-rebalance, never sell**
- [ ] **Carry back:** post the two inherited-error corrections into MultiAsset's `decision_tree.md` (24-month FoF gate; ₹1.25L exemption does not apply to metals)
- [ ] **Close:** `Personal Finance/mutual_fund_sip_decisions_2026-07.md` §4b, and update the finalized-plan tables in both Personal Finance docs

---

*Study plan version: 1.0 | Created: August 9, 2026 | Status: PLAN ONLY — Phase 0 not started; module count and weights unlocked | Framework: **5-Module Weighted Scoring (precious-metals adaptation)** — scores NOT comparable to any prior study | Defining constraints: no manager skill and no alpha → tracking fidelity replaces returns; the wrapper decision dominates the scheme decision, so Phase 0 runs first rather than deferred; published ERs are single-layer and unusable; silver is untested in this repo and is gated behind a whole-portfolio test | Budget: ₹10,000/month, the open slot in the ₹75K SIP*
