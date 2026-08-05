# Deep Study Plan — Multi Asset Allocation Funds

## Context

Fifth category study, following the established pipeline: **screen the universe → shortlist → 6-module deep study per fund → decision tree**. Same 6-module weighted framework as FlexiCap, SmallCap, International, and MidCap — but with **the largest set of adaptations yet**, because this is the first study of a *hybrid, multi-asset-class* category rather than a single equity band.

**Investment goal (working assumption — confirm before Phase 2):** part of the ₹65,000/month cross-sleeve budget. Unlike the four equity sleeves, multi-asset is a candidate for the **all-weather / volatility-dampener role** — the one sleeve that introduces *non-equity* exposure (debt + gold ± silver/REITs) the current portfolio entirely lacks. Working assumption: **₹15–20K/month**, 7–10+ year horizon.

**The four framing facts (read first — each rewrites a module):**

1. **There is no single benchmark.** A Multi Asset fund is measured against a *blended* index (e.g. 65% Nifty 500 TRI + 25% NIFTY Composite Debt + 10% domestic gold). "Alpha" decomposes into **asset-allocation skill + security selection**, not one number. Module 1 must build a custom blended benchmark per fund and separate the two sources of return.

2. **The counterfactual is not an index fund — it is DIY.** The prior four studies asked "why not the 0.20% index fund?" Here the sharper question is: **"why pay an active multi-asset fund instead of assembling equity index + gold ETF + debt fund yourself and rebalancing annually?"** The fund must beat a *naïve static-allocation DIY basket*, not just its peers. This is the permanent standing test in Modules 1 and 4.

3. **Tax is a first-class structural variable, not a footnote.** Two things the DIY basket cannot replicate: (a) **internal rebalancing is tax-free** inside the fund, while a DIY investor triggers capital gains every time they rebalance; (b) funds that hold **≥65% gross equity** (often topped up with arbitrage/derivatives) get **equity taxation on the entire corpus** — including the gold and debt sleeves. That tax shield can *exceed* the fund's higher expense ratio over 10 years. Tax analysis moves into Module 4 as a core scored dimension.

4. **This is a risk-reduction product — so Risk and the Allocation Engine carry the thesis, not Returns.** The entire value proposition is *lower drawdown and smoother compounding*, not maximum CAGR. Judged on raw return a multi-asset fund will always lose to the equity sleeves; that is not its job. See the **proposed re-weighting** below — an open decision to confirm before Phase 2.

---

## The Category's Defining Split (decide segmentation at screening)

SEBI's "Multi Asset Allocation" label covers two economically different animals:

| Sub-type | Equity stance | Taxation | Role |
|----------|--------------|----------|------|
| **Equity-oriented** | ≥65% *gross* equity (often net 40–55% + arbitrage/derivative top-up to clear 65%) | **Equity** (12.5% LTCG >₹1.25L, 20% STCG) | All-weather equity-plus, tax-efficient; closest to what the portfolio already owns |
| **Conservative / debt-oriented** | 35–55% equity, no 65% top-up | **Debt/hybrid** (slab or 12.5% depending on structure & date) | More genuine diversification (more debt+gold), worse tax |

**✅ LOCKED (Jul 28 2026): study BOTH sub-types, segmented.** Equity-oriented and conservative/debt-oriented funds are screened and scored in separate buckets so the diversification-vs-tax tradeoff is made concrete rather than assumed away.

**Implication:** these should be **segmented, not pooled**, in screening. For a portfolio that is currently ~100% equity, the tension is explicit:
- The *equity-oriented* funds are more tax-efficient but overlap more with the existing sleeves (they *are* mostly equity).
- The *debt-oriented* funds diversify harder (more non-equity) but tax worse and pull expected return down.

Naming which sub-type is in scope is part of the Phase-0 prior question below.

---

## Phase 0 — The Prior Question (sharper here than in any prior study)

MidCap opened with "does a mid-cap sleeve earn a slot?" For Multi Asset the gate is even more decisive, because a multi-asset fund partially duplicates the **equity** the portfolio already holds while adding **debt + gold** it does not. Four analyses, done once, before fund-level work:

| # | Analysis | Method | Kill / reshape criterion |
|---|----------|--------|--------------------------|
| 0.1 | **What is the sleeve actually FOR?** | Is the goal (a) reduce whole-portfolio volatility, (b) add a gold/debt allocation the portfolio lacks, (c) a tax-efficient rebalancing vehicle, or (d) simplicity? Each points to a different sub-type and weight. | If the goal is purely "add gold," a gold ETF + a short-duration debt fund (DIY) may dominate any multi-asset fund on cost and control |
| 0.2 | **The DIY counterfactual, specified** | Construct the reference basket the fund must beat: e.g. **65% Nifty 500 index / 25% debt index fund / 10% gold ETF, rebalanced annually**, on a *post-tax, post-cost* basis over 10Y (MFAPI/index NAVs). | If the average shortlisted fund cannot beat this basket post-tax, the recommendation is "DIY the basket," and the study becomes a search for the *exceptions* |
| 0.3 | **Overlap with existing equity sleeves** | The equity book of a multi-asset fund vs Parag Parikh FlexiCap + the chosen MidCap/SmallCap picks (name-level, like the International study did vs Franklin). | High overlap means the "diversification" is mostly the debt+gold slice — size the sleeve to the *non-equity* contribution, not the headline AUM |
| 0.4 | **Tax-status confirmation per candidate** | Equity vs debt/hybrid taxation, and *how* 65% gross equity is maintained (arbitrage overlay honesty). | A fund taxed as debt needs materially higher gross return to tie an equity-taxed peer; this reshapes the whole comparison |

> **Deliverable:** `phase0_prior_question.md` with a PROCEED / PROCEED-AS-DIY / PROCEED-WITH-REDUCED-SCOPE / STOP verdict, plus the specified DIY basket that every Module 1 and Module 4 will reference.

> **Precedent:** the International study's SEBI-cap analysis and MidCap's sleeve gate both reshaped their studies before any fund was touched. Multi Asset's Phase 0 is the most consequential of the five.

> **✅ STATUS (Jul 28 2026): Phase 0 DEFERRED to decision-tree time (MidCap precedent) — study the funds first, decide portfolio fit at the end. Analyses 0.2 (DIY basket) and 0.4 (tax status) survive *inside every Module 1 and Module 4* as standing tests, because the modules cannot be scored without them.**

---

## Phase 1 — Screening Pipeline

### Data required (Tickertape screener API, ~25–30 funds, Direct Growth)

Same screener-API pull as MidCap (subsector = "Multi Asset Allocation Fund"), plus **category-specific fields that must be gathered from factsheets** because Tickertape does not carry them cleanly:

| Source field | Contents |
|------|----------|
| API | AUM, ER, NAV, fund manager, inception, exit load, AMC |
| API | CAGR 10Y/5Y/3Y, alpha (note: vs Tickertape's chosen benchmark — treat as indicative only), returns 1Y/6M/3M |
| API | Volatility, Sharpe, Sortino, category St Dev |
| **Factsheet / SID** | **Current & trailing equity / debt / gold / silver / cash split** (the defining data — not reliably in the API) |
| **Factsheet / SID** | **Net vs gross equity** (arbitrage overlay), **taxation status**, gold-holding mechanism |

Save the raw pull to `Mutual Fund/TickerTape Data/MultiAsset_Screener_API_<date>.csv`.

### Stage 1 — Hard Filters (applied in order)

| Filter | Threshold | Rationale | vs prior studies |
|--------|-----------|-----------|------------------|
| Expense Ratio | **ER ≤ 1.2% (Direct)** | Softer than MidCap's 1.0% because the counterfactual is a *multi-leg DIY basket* (whose all-in cost + rebalancing tax is higher than a single 0.20% index fund), not a cheap single tracker. Still a ceiling — >1.2% is hard to justify vs DIY | **New calibration** (FlexiCap 1.5%, Mid/SmallCap 1.0%) |
| AUM minimum | **AUM ≥ ₹500 Cr** | Operational viability | Same as siblings |
| AUM maximum | **None** | Capacity is a non-issue: the equity book is large/mega-cap-tilted, debt and gold ETFs are effectively unlimited. The MidCap 150-stock capacity ceiling has **no analog here** | **Dropped** (unique to this study) |
| Track record | **≥ 36 months** (revised from ≥60mo at screening — see below) | 3-year floor for the framework's 3Y metrics; covers the Sep-2024–Mar-2025 correction. Funds 36–59mo carry a `no-2022-data` flag into Modules 1/2 | **Replaced ≥60mo** — the post-2023 launch wave (only 8/35 funds ≥60mo) forced it; MidCap `no-2018-data` precedent |
| Sharpe Ratio | **Sharpe ≥ 0** | Below risk-free is disqualifying — but note it **bites far less** here: lower volatility structurally lifts Sharpe, so a near-zero Sharpe in this category is a *real* red flag | Same threshold, different meaning |

> **Note on the AUM filter:** with no upper bound and a low floor, Stage 1 will thin the universe less than in equity studies. Expect more of the funnel to happen at Stage 2 and in the modules.

### Stage 2 — Performance / Fitness Filters

Raw CAGR is the **wrong** primary screen for a risk-reduction product. Stage 2 is re-specified:

| Filter | Threshold | Rationale |
|--------|-----------|-----------|
| 5Y CAGR | **> full-universe median** | Kept, but as a floor not a ranker — a multi-asset fund far below median return is failing even on its own risk-adjusted terms |
| **Risk-adjusted: Sharpe OR Sortino > universe median** | **>0.5× isn't enough — must beat median** | The category-appropriate primary screen: for an all-weather product, risk-adjusted return is the fitness test, not CAGR |
| Age covers 2020 **or** 2022 | at least one asset-divergence stress year | A multi-asset fund that has never seen equity and debt fall together (2022) or equity crash while gold rallied (2020) is unproven at its core job |

**Not used as filters (studied in modules):** max drawdown (inception-biased, Module 2), equity/debt/gold split (the *subject* of Module 3, not a filter), tax status (segmentation variable, not a cut).

**Expected funnel:** ~25–30 → ~12–15 → **5–8 shortlisted** (segmented into equity-oriented vs conservative if both sub-types survive).

### Deliverables

`screening/methodology.md`, `screening/stage1_hard_filters.md`, `screening/stage2_performance.md`, `screening/all_funds_data.md` — same format as prior sets, **plus a segmentation table** (equity-oriented vs conservative, with tax status per fund).

---

## Phase 2 — The 6 Modules

### ✅ LOCKED — Module weights (multi-asset re-weight, set Jul 28 2026)

The prior four studies held weights constant at 25/20/20/15/15/5. For a *risk-reduction, allocation-driven* product that would let Returns dominate a fund whose job is smoother compounding. **User decision (Jul 28 2026): adopt the multi-asset re-weight below.** Cross-study scores are therefore NOT directly comparable to the four equity categories — note this in every README.

| Module | Prior-study weight | **Multi-Asset weight (LOCKED)** | Why the change |
|--------|-------------------|-------------------------------|----------------|
| 2 — Risk Profile | 20% | **25%** | The value proposition itself — elevated to top weight |
| 1 — Returns & Allocation Alpha | 25% | **20%** | Return matters, but risk-adjusted, and vs the DIY basket — not raw CAGR |
| 3 — Asset Allocation Engine & Portfolio DNA | 15% | **20%** | The defining module of the category (analog of MidCap's active share) |
| 4 — Cost & **Tax** Efficiency | 20% | **20%** | Same weight, but now carries the decisive tax-shield analysis |
| 5 — Fund Manager / Team Quality | 15% | **10%** | Allocation is more model/mandate-driven than single-manager stock-picking |
| 6 — AMC Trustworthiness | 5% | **5%** | Unchanged; mostly carry-forward |

**Scale:** 1 = Poor · 2 = Below Avg · 3 = Average · 4 = Good · 5 = Excellent

---

### Module 1 — Returns & Allocation Alpha (proposed 20%)

**What's the same:** CAGR 3Y/5Y/10Y, rolling returns, calendar-year decomposition, MFAPI-computed verification (the canonical method).

**What's different — the benchmark is a construction problem:**

1. **Build the blended benchmark** per fund from its *stated* strategic weights (e.g. 65% Nifty 500 TRI / 25% NIFTY Composite Debt TRI / 10% domestic gold), using MFAPI index-fund NAVs as legs. Compute alpha vs *this*, not vs a single equity index.
2. **Decompose the alpha:** how much came from **asset-allocation timing** (over/under-weighting the right class at the right time) vs **security selection** (the equity/debt sleeves beating their own legs). A fund whose entire edge is one lucky gold overweight is fragile.
3. **The DIY-basket test** (from Phase 0.2): does the fund beat a *naïve static 65/25/10 annually-rebalanced* basket **post-tax**? Naïve static allocation is a brutally hard benchmark — beating it is the real bar.
4. **Post-tax returns are computed here, not deferred** — because tax status can flip the ranking (an equity-taxed 11% fund can beat a debt-taxed 12% fund for a high-bracket investor).

**Key calendar years — chosen for asset-class divergence, not equity direction:**

| Year | Cross-asset event | Why it matters for Multi Asset |
|------|-------------------|-------------------------------|
| 2019 | Equity up, gold +24%, debt steady | Did the fund hold enough gold to benefit, or was it closet-equity? |
| **2020** | **COVID: equity crashed then V-recovered; gold rallied hard** | **The rebalancing test — did the fund buy equity into the crash and harvest gold?** |
| 2021 | Equity bull, gold flat/down | Opportunity-cost check — how much did the non-equity drag cost in a raging bull? |
| **2022** | **Equity down + debt down (rate hikes) + gold up in ₹** | **THE multi-asset stress year — the only period all three classes diverged sharply; separates real allocation from static holding** |
| 2023 | Broad recovery + gold strength | Participation |
| 2024 | Equity top (Sep-2024), gold +20%+ | Did gold cushion the Q4 equity fall? |
| 2024–25 | Sep 2024 – Mar 2025 equity correction, gold at highs | The freshest, universal stress test — every incumbent manager was on duty |
| 2025–26 YTD | Recovery | Current positioning |

**Module 1 Scorecard:**

| Sub-dimension | Weight | Scoring guide (recalibrate to actual medians at export) |
|---------------|--------|--------------------------------------------------------|
| 5Y CAGR vs category median | High | Top quartile = 5, above median = 4, at median = 3 |
| **Alpha vs the fund's blended benchmark** | Critical | >2% ann. = 5; 1–2% = 4; ±1% = 3; negative = 2 |
| **Beat the DIY static basket, post-tax?** | Critical | Comfortably = 5; roughly tie = 3 (*why pay?*); loses = 2 |
| Allocation-timing contribution (positive & repeatable) | High | Documented good calls in 2020/2022 = 5; one-off luck = 3 |
| 2022 asset-divergence year | Critical | Positive/flat while equity fell = 5; fell with equity = 2 |
| 2020 rebalancing behaviour | High | Bought the crash / harvested gold = 5 |
| Post-tax return (bracket-adjusted) | High | Equity-taxed & competitive = 5 |
| Inception-bias adjustment | Modifier | Discount for post-2020 launches (never saw 2020) |

---

### Module 2 — Risk Profile (proposed 25% — the thesis module)

**The whole point of the category. Judged vs equity, not vs peers alone.**

| Risk metric | Pure equity (Nifty 500) | **Multi Asset "good"** | Multi Asset "alarming" |
|-------------|------------------------|------------------------|------------------------|
| Max Drawdown | −35% to −40% | **< −20%** | > −28% (it's barely dampening) |
| Volatility | 14–16% | **8–11%** | > 13% (closet equity) |
| Downside capture vs Nifty 500 | 100% | **< 65% excellent** | > 80% |
| Recovery time | 12–24 mo | **< 9 mo** | > 15 mo |

**Multi-asset-specific risk questions:**

1. **Drawdown reduction is the headline** — max DD vs the Nifty 500 *and* vs a Balanced Advantage / Aggressive Hybrid fund (the nearest cousins). If a multi-asset fund draws down like an aggressive hybrid, its gold sleeve isn't earning its place.
2. **True decorrelation** — compute the correlation of the fund's *non-equity* return stream; measure how much gold+debt actually cushioned each equity drawdown (2020, 2022, 2024–25) in NAV terms.
3. **The 2022 test** — the year debt *also* fell. Did the fund's debt sleeve add duration risk at the wrong time? Duration + credit quality of the debt book is a risk input, not just a Module-3 portfolio note.
4. **Gold concentration risk** — gold is volatile too (it can draw −15% to −20%). A fund over-leaning gold trades equity risk for commodity risk; quantify.
5. **Correlation to existing sleeves** — R²/correlation vs Parag Parikh FlexiCap and the chosen equity picks (the International/MidCap method). This feeds the decision tree's "how much real diversification" verdict — the single most important cross-sleeve number in this study.

**Module 2 Scorecard:**

| Sub-dimension | Weight | Scoring guide |
|---------------|--------|---------------|
| Max Drawdown (inception-adjusted) | Critical | < −18% = 5, −18 to −24% = 4, −24 to −30% = 3, > −30% = 2 |
| Downside capture vs Nifty 500 | Critical | < 65% = 5, 65–75% = 4, 75–85% = 3, > 85% = 2 |
| Volatility | High | < 9% = 5, 9–11% = 4, 11–13% = 3, > 13% = 2 |
| Sharpe / Sortino vs category | High | Above category median = 4+; top quartile = 5 |
| Recovery time from max DD | Medium | < 9 mo = 5, 9–12 = 4, 12–15 = 3, > 15 = 2 |
| 2020 & 2022 realised cushioning | Critical | Materially softer than equity in both = 5 |
| Debt-sleeve quality (duration + credit) | Medium | High-grade, sensible duration = 5; credit reach for yield = 2 |
| Correlation to existing equity sleeves | Informational | Feeds decision tree, not the fund score |

---

### Module 3 — Asset Allocation Engine & Portfolio DNA (proposed 20%)

**The category's defining module — the analog of MidCap's active share. *How* the fund decides the equity/debt/gold split IS the fund.**

1. **The allocation model — the headline classification:**
   - **Static bands** (fixed e.g. 65/25/10, mechanical rebalancing) — cheap, predictable, but no skill claim; the DIY basket does this for less.
   - **Valuation-driven** (equity weight flexes on P/E, P/B, yield-gap models) — a genuine, testable process.
   - **Discretionary / macro** — manager judgement; hardest to underwrite, highest key-person risk.
   - **In-house quant model** — check if it's real or marketing.
2. **Net vs gross equity** — is the ≥65% equity real, or arbitrage/derivative padding to win equity taxation? Not a criticism (tax efficiency is good) but it must be *disclosed and understood*: net equity is the true risk exposure.
3. **Gold/commodity mechanism** — physical-backed gold ETF vs gold futures/ETCDs vs Sovereign Gold Bonds vs silver. Cost, tracking error, and liquidity differ. Some funds add silver or international — note it.
4. **Debt book** — duration, credit quality, government vs corporate. This is where hidden risk lives.
5. **Range & dynamism** — actual historical min/max of each asset class from trailing factsheets. A "multi-asset" fund that has sat at 74% equity for 5 years is a closet equity fund with a gold garnish.
6. **Equity-sleeve DNA** — large/mid/small split and top holdings of the equity book (for the overlap analysis vs existing sleeves).
7. **Rebalancing discipline** — frequency, rules-based vs discretionary, and evidence it actually happened at the right moments (2020, 2022).

**Module 3 Scorecard:**

| Sub-dimension | Weight | Scoring guide |
|---------------|--------|---------------|
| **Allocation model — clarity & testability** | Critical | Documented, repeatable, evidence it works = 5; static-band closet equity = 2 |
| **Dynamism (realised asset-class range)** | Critical | Meaningful, well-timed flexing = 5; static ±5% = 3 |
| Net-vs-gross equity transparency | High | Clearly disclosed, understood true exposure = 5 |
| Gold mechanism quality | Medium | Low-cost physical-backed = 5; futures roll drag = 3 |
| Debt-book quality | Medium | High-grade, sensible duration = 5; credit reach = 2 |
| Equity-sleeve overlap with existing funds | Informational | Reported per fund; scored in the decision tree |
| Rebalancing discipline (evidence) | High | Rules + proof of good execution = 5 |

---

### Module 4 — Cost & **Tax** Efficiency (proposed 20%)

**The module where a multi-asset fund can *win* despite a higher ER — because of two things the DIY basket cannot do.**

1. **ER vs the all-in DIY cost:** the DIY basket also costs money (equity index ~0.2% + debt fund ~0.3% + gold ETF ~0.5% ≈ blended ~0.3%). The multi-asset ER premium over this is the fee to beat.
2. **The internal-rebalancing tax shield (the decisive number):** a DIY investor rebalancing annually **realises capital gains every year**; the fund rebalances internally **tax-free**. Model this explicitly over 10Y — for an active rebalancer it can be worth more than the entire ER difference.
3. **Equity-taxation status (the second shield):** if the fund holds ≥65% gross equity, its *entire* corpus — gold and debt included — is taxed at equity rates (12.5% LTCG) rather than slab/debt rates. For a high-bracket investor holding gold and debt directly, this is a large, permanent edge.
4. **Net verdict:** ER premium **minus** rebalancing-tax-shield **minus** equity-taxation-shield = the *true* cost of the fund vs DIY. This can be **negative** (the fund is cheaper all-in) — the finding that would justify the category's existence.

**ER impact modelled on ₹15–20K/month, 10Y, ~11% gross (lower than equity by design).**

**Module 4 Scorecard:**

| Sub-dimension | Weight | Scoring guide |
|---------------|--------|---------------|
| Expense Ratio (Direct) | High | ≤0.60% = 5, 0.60–0.85% = 4, 0.85–1.05% = 3, 1.05–1.2% = 2 |
| **True cost vs DIY (ER − both tax shields)** | Critical | Net cheaper than DIY = 5; roughly tie = 3; net dearer = 2 |
| Equity-taxation status | Critical | Equity-taxed & structurally stable ≥65% = 5; debt-taxed = 2 |
| Rebalancing tax-shield magnitude | High | Large & documented = 5 |
| Gold/commodity holding cost embedded | Medium | Low-cost mechanism = 5 |
| Exit load | Low | Standard |
| AUM trajectory / viability | Low | Healthy, stable = 5 |

---

### Module 5 — Fund Manager / Team Quality (proposed 10%)

**Multi-asset needs a *team*, not a stock-picker — usually an equity manager + a debt manager + a commodity/dedicated allocation lead.**

| Dimension | Multi-Asset importance |
|-----------|------------------------|
| Allocation-call track record | **Critical** — did they add gold before 2020/2022? cut equity near the Sep-2024 top? These calls, not stock picks, are the job |
| Team depth & structure | High — single-manager multi-asset is a key-person red flag; who runs debt, who runs gold? |
| Tenure across a full cross-asset cycle | High — must have managed through 2022 (all-classes-diverge year) |
| Philosophy clarity (the allocation model, documented) | High — mirrors Module 3; a clear, followed model = conviction |
| Sell/rebalance discipline | Medium |
| Skin in the game / communication / SEBI record | Low–Medium — same as siblings |

**Key question:** are the historical allocation shifts *evidence of a repeatable process*, or post-hoc drift? Reconstruct the equity/debt/gold path from trailing factsheets and match it against what a skilled allocator *should* have done at each turn.

**Module 5 Scorecard:** allocation-call track record (Critical), team depth (High), tenure through 2022 (High), philosophy clarity (High), rebalance discipline (Medium), skin-in-game/communication/regulatory (Low each) — same 5-point scale.

---

### Module 6 — AMC Trustworthiness (5%)

Same framework as siblings; **carry-forward first** (the AMC bench is now very deep across four studies — ICICI, HDFC, Edelweiss, HSBC, Nippon, SBI, Kotak, DSP, etc. likely recur). Multi-asset-specific additions:

1. **Fixed-income & commodity credibility** — a strong equity AMC may run a weak debt desk. Check the AMC's debt-fund track record for credit blowups (the category imports the AMC's fixed-income competence).
2. **Launch-timing honesty** — did the AMC launch/relaunch its multi-asset fund at a market top to harvest "safe-haven" flows? Governance signal.
3. **Category commitment** — is multi-asset a serious franchise or a defensive-flows product left on autopilot?

---

## Study Order (to be set post-screening)

Assign after the shortlist is known. Sequencing principles (from prior studies):

1. **Longest, most cycle-complete record first** — the fund that saw 2020 *and* 2022 in full builds the category reference frame (the Nippon-first logic from MidCap).
2. **The screening leader second** — best risk-adjusted profile, to test whether it's genuine.
3. **The instructive contrast** — a *conservative/debt-oriented* fund studied alongside the equity-oriented ones to make the segmentation concrete (analog of Motilal Oswal's cautionary role in MidCap).
4. **AMC continuations** — funds from already-studied AMCs, to lean on carry-forward and isolate the fixed-income/commodity delta.
5. **The confirm-the-elimination laggard last.**

*(Likely universe names to expect at screening: ICICI Pru Multi-Asset — the category giant/longest record; SBI, HDFC, Nippon, Tata, Kotak, Quant, UTI, Axis, Motilal Oswal, WhiteOak Multi Asset. Do not pre-commit — the screen decides.)*

---

## Module Writing Reference

For each fund, 6 module files + README (written last):

```
Mutual Fund/MultiAsset/funds/<fund_name>/
├── README.md          ← Fund summary, scorecard, verdict (written last)
├── module1_returns.md
├── module2_risk.md
├── module3_allocation.md   ← (renamed from portfolio: the allocation engine is the DNA)
├── module4_cost_tax.md     ← (cost AND tax)
├── module5_manager.md
└── module6_amc.md
```

Each module carries the standard apparatus: MFAPI-computed NAV metrics (CAGR, calendar years, rolling, drawdown/recovery, SIP XIRR), **the constructed blended benchmark and the DIY-basket comparison**, mermaid scorecard charts, comparative tables vs already-studied funds, and a provisional score footer.

> **Completeness gate:** every fund's 6 modules must cover **every dimension** enumerated in [dimensions_covered.md](dimensions_covered.md) — the full inherited apparatus of the four prior studies plus the 12 multi-asset-specific NEW dimensions listed there. That file is the extraction of all dimensions ever used across FlexiCap/SmallCap/International/MidCap.

---

## Phase 3 — Decision Tree

After all shortlisted funds are studied, `decision_tree.md` must answer, in order:

1. **The sleeve question (evidence-backed):** does the best multi-asset fund add enough *non-equity, non-duplicated* diversification over the existing four sleeves to earn a slot — or is the honest answer "add a gold ETF + a debt fund yourself," or "do nothing"?
2. **Fund vs DIY:** did any fund beat the naïve static DIY basket **post-tax** after fees? If none did, the recommendation is DIY — a legitimate, category-defining outcome (parallel to MidCap's "the index fund is a co-equal default").
3. **Sub-type choice:** equity-oriented (tax-efficient, overlaps more) vs conservative (diversifies harder, taxes worse) — which fits the stated goal from Phase 0.1?
4. **If a fund, which one, sizing, and mechanics** — SIP date, step-up, and how it fits the ₹65K cross-sleeve budget (this feeds `Portfolio/allocation_options.md`).
5. **Review triggers:** allocation-model drift toward closet-equity, tax-status change (dropping below 65% gross equity), debt-book credit deterioration, manager/team exit, plus the standing sibling triggers.

---

## Data Sources per Fund

| Source | What to pull |
|--------|-------------|
| Tickertape screener API (fresh Multi Asset export) | Screening quantitative data |
| MFAPI (mfapi.in) | Fund NAV history — own CAGR/rolling/drawdown/SIP-XIRR |
| Index-fund NAVs via MFAPI (Nifty 500 TRI, NIFTY Composite Debt, domestic gold ETF) | **The constructed blended benchmark + DIY-basket legs** |
| AMC monthly factsheet + SID/SAI | **Equity/debt/gold split & its history, net-vs-gross equity, allocation model, gold mechanism, debt duration/credit, team structure, taxation** |
| ValueResearch / Morningstar India | Ratings, capture ratios, independent verification |
| AdvisorKhoj | Rolling returns, SIP XIRR cross-check |
| CBDT / fund SID | Taxation status confirmation (equity vs debt/hybrid) |
| Business Standard / Mint / ET | Manager/team changes, AMC governance, launch-timing history |
| SEBI/BSE/NSE | Regulatory actions |

---

## Execution Checklist

- [x] **Decisions locked (Jul 28 2026):** module re-weight adopted (Risk 25 / Returns 20 / Allocation 20 / Cost+Tax 20 / Manager 10 / AMC 5); BOTH sub-types in scope, segmented; Phase 0 DEFERRED to decision-tree time
- [~] **Phase 0:** Prior-question analysis → DEFERRED (0.2 DIY-basket + 0.4 tax-status survive inside every Module 1/4)
- [x] **Phase 0:** Data acquisition — Tickertape screener API, Jul 28 2026 → `TickerTape Data/MultiAsset_Screener_API_28_07_2026.csv` (35 funds; 109 raw rows)
- [x] **Phase 1:** `screening/methodology.md` v2.0 — **age filter REPLACED** with ≥36mo track-record floor + `no-2022-data` flag (the post-2023-launch-wave finding forced it)
- [x] **Phase 1:** `stage1_hard_filters.md` (35 → 11) + `stage2_performance.md` (11 → 6, 3Y fitness floor) + `all_funds_data.md`
- [x] **Phase 1:** README + shortlist + study order set
- [x] **Phase 1 outcome:** shortlist = **6**: Quant, Nippon, WOC (conservative), ABSL, UTI, SBI. Segmentation covered by the rule (no special relaxation). **ICICI Pru (₹84K flagship) screens OUT → instructive.** Also instructive: HDFC, DSP
- [ ] **Phase 2:** Deep studies — 6 modules + README per fund, in study order
- [ ] **Phase 2 (optional):** Instructive case — a conservative/debt-oriented fund to make the segmentation concrete
- [ ] **Phase 3:** `decision_tree.md` — sleeve verdict, fund-vs-DIY verdict, sub-type choice, deployment, feed into `Portfolio/allocation_options.md`

---

*Study plan version: 1.0 | Created: July 28, 2026 | Status: PLAN ONLY — screening not started; two open decisions to lock | Framework: 6-Module Weighted Scoring (Multi-Asset adaptation) | Defining constraints: no single benchmark → blended-benchmark construction; DIY basket replaces the index-fund counterfactual; tax is a first-class scored variable; Risk + Allocation Engine carry the thesis, not Returns | Prior question: the most consequential of the five studies*
