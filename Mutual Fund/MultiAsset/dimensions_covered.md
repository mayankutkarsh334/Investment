# Master Dimension Inventory — Every Dimension Covered in Prior Studies

**Purpose:** an exhaustive checklist of *every* analytical dimension used across the four completed studies (FlexiCap, SmallCap, International, MidCap), so the Multi Asset study inherits **all** of them. Extracted directly from the actual module files (primarily DSP SmallCap — the most granular fund studied — cross-checked against Franklin International and Edelweiss MidCap for category-unique dimensions).

**How to read the tables:**
- **Dimension** — the thing measured.
- **Seen in** — U = universal (every study) · SC/FC/INTL/MC = introduced/emphasised in that category.
- **Multi-Asset translation** — how it must be adapted here, or ✅ carry as-is. **NEW** = a multi-asset-specific dimension with no prior analog.

> Weights for this study (LOCKED): **Risk 25 · Returns 20 · Allocation-Engine 20 · Cost+Tax 20 · Manager 10 · AMC 5.** See [study_plan.md](study_plan.md).

---

## §0 — The decisive dimensions (Tier 1)

The tables below are exhaustive, but ~150 dimensions have no ranking. These **ten decide the verdict** for a multi-asset fund — if a write-up is thin, it must be thin somewhere else, never here. Everything else is supporting evidence.

| # | Decisive dimension | Module | The question it answers |
|---|---|---|---|
| 1 | **Max drawdown + downside capture vs Nifty 500** | M2 | Does it actually dampen, or is it closet-equity? |
| 2 | **Realised 2020 & 2022 cushioning** | M2 | Did the non-equity sleeves work at the exact moments that matter? |
| 3 | **Correlation / real diversification vs existing sleeves** | M2 | Does it add the *non-equity* the portfolio lacks, or duplicate equity you own? |
| 4 | **Beat the post-tax DIY basket?** | M1 × M4 | The existential test — why pay a fund vs assembling 65/25/10 yourself? |
| 5 | **The tax triad** (equity-tax status · rebalancing shield · true-cost-vs-DIY) | M4 | The structural edge that can justify the whole category |
| 6 | **Allocation model — real/dynamic/testable vs static closet-equity** | M3 | Is there a skill claim at all, or just a garnish of gold on an equity fund? |
| 7 | **Net-vs-gross equity** | M3 | What is the *true* risk exposure behind the ≥65% tax-driven headline? |
| 8 | **Allocation-call track record** (added gold pre-2020/22? cut equity at the top?) | M5 | Is the dynamism repeatable skill or post-hoc drift? |
| 9 | **Debt-book credit + duration quality** | M2/M3 | Where the hidden risk lives — did it add duration into 2022? |
| 10 | **Gold mechanism + gold-concentration risk** | M3/M2 | Is gold cheap/physical-backed, and is the fund over-leaning it? |

> If forced to cut scope on any fund, cut from the Standard/Informational rows below — **never** from these ten.

---

## §0.1 — Data provenance for the NEW dimensions (read before screening)

The inherited dimensions come from the usual stack (Tickertape API, MFAPI, ValueResearch, AdvisorKhoj). The **multi-asset-specific NEW dimensions are mostly NOT in any API** — they require factsheet/SID work per fund. Budget for this.

| NEW dimension | Primary source | Effort |
|---|---|---|
| Blended benchmark + DIY basket legs | Index-fund NAVs via MFAPI (Nifty 500 TRI, NIFTY Composite Debt, domestic gold ETF) | Low (compute) |
| Net-vs-gross equity | Monthly factsheet / full portfolio disclosure (derivatives line) | Medium |
| Realised asset-class range/dynamism | **Trailing 12–36 monthly factsheets**, month-over-month | High (manual) |
| Allocation-model classification | SID + factsheet commentary + manager interviews | Medium |
| Gold mechanism (ETF/futures/SGB/silver) | Factsheet holdings + SID | Low |
| Debt duration + credit quality | Factsheet debt-quality/maturity table | Low |
| Rebalancing evidence (did it fire at turns?) | Month-over-month factsheet weight deltas | High |
| Allocation-vs-selection alpha split | Reconstructed: factsheet weights × each leg's index return | High |
| Asset-class return attribution | Same reconstruction, historical | High |
| Arbitrage/hedged-equity sleeve size & drag | Factsheet derivatives / hedged-equity disclosure | Medium |
| Taxation status + continuity | SID + CBDT rules + gross-equity history | Low |
| Allocation-call track record | Reconstructed asset-path vs market turning points | High |

> **Implication for study order:** funds with clean, long factsheet archives (ICICI Pru Multi-Asset, the category's longest record) are cheaper to study first and build the reconstruction templates the later funds reuse.

---

## Cross-cutting apparatus (applies to every module)

| Dimension | Seen in | Multi-Asset translation |
|---|---|---|
| Fund Identity block (full name, AMC, benchmark, manager, inception Direct + Regular, AUM, ER) | U | ✅ + add **taxation status** and **stated strategic asset-allocation** to the identity block |
| Raw-data table with **per-metric source attribution** | U | ✅ |
| **Cross-source verification** (Tickertape vs MFAPI vs ValueResearch vs AdvisorKhoj, flag anomalies) | U | ✅ — extra care: Tickertape's single-benchmark alpha is *meaningless* for multi-asset; flag it |
| **MFAPI NAV self-computation** as canonical (3,000+ daily NAVs) | U | ✅ the backbone method |
| Mermaid scorecard / xychart per module | U | ✅ |
| **Comparison vs already-studied funds** (cross-category table) | U | ✅ — and vs the DIY basket |
| Per-sub-dimension 1–5 scorecard + weighted module score | U | ✅ |
| **Points For / Points Against** explicit lists | U | ✅ |
| "SIP Implication" + "One-Line Verdict" closers | U | ✅ |
| **Provisional-score footer + post-hoc retrofit/correction** when later modules change earlier conclusions | MC | ✅ (Edelweiss's cross-module retrofit discipline) |

---

## MODULE 1 — Returns (+ Allocation Alpha)

### 1A. Core return metrics (universal)
| Dimension | Seen in | Multi-Asset translation |
|---|---|---|
| CAGR 1Y / 3Y / 5Y / 10Y / since-inception | U | ✅ |
| CAGR trajectory / compression analysis (why 3Y ≠ 10Y) | U | ✅ |
| Rolling 3Y & 5Y returns — mean, median, min, max, full distribution | U | ✅ |
| Rolling-window distribution buckets (% windows ≥12%, ≥15%, negative) | U | ✅ (thresholds lower — this is a lower-return product) |
| **Probability of loss by holding period** (1Y/3Y/5Y) | U | ✅ — should be *dramatically* better than equity; that's the thesis |
| Calendar-year returns, full history, vs benchmark, with event annotation | U | ✅ — **years re-chosen for asset-class divergence** (see 1C) |
| Best/worst rolling 1M/3M/6M/1Y windows | U | ✅ |
| Absolute short-term trend (3M/6M/1Y) | U | ✅ |
| **SIP XIRR vs Lumpsum CAGR** (₹/month, Newton-Raphson), corpus table by period | U | ✅ |
| Up-year outperformance vs down-year protection (symmetry) | U | ✅ |
| Manager-tenure return attribution ("whose record is this?") | U/MC | ✅ |
| Inception-bias adjustment (discount post-2020 launches) | U | ✅ |

### 1B. Benchmark & alpha (the biggest adaptation)
| Dimension | Seen in | Multi-Asset translation |
|---|---|---|
| Alpha vs a single benchmark index | U | ⚠️ **Replaced:** build a **blended benchmark** (e.g. 65% Nifty500 + 25% debt + 10% gold) from index-fund NAV legs |
| "Beat its own benchmark?" central question | INTL | ✅ vs the blended benchmark |
| **"Why not the index/DIY?"** counterfactual | INTL/MC | ⚠️ **Replaced by the DIY-basket test:** beat a naïve static 65/25/10 annually-rebalanced basket, **post-tax** — **NEW as scored line** |
| Two-proxy / multi-proxy index robustness test | MC | ✅ — test blended benchmark under alternative weight assumptions |
| Alpha-persistence decomposition (is alpha consistent or one lucky year?) | MC | ✅ |
| **Benchmark appropriateness critique** | INTL | **Elevated** — is the fund's *stated* blended benchmark honest, or gamed (e.g. a debt-heavy benchmark to flatter an equity-heavy book)? |
| **Allocation-vs-selection alpha decomposition** | — | **NEW** — split alpha into asset-allocation timing vs security selection |
| **Asset-class return attribution** | — | **NEW** — decompose total return into equity / debt / gold / arbitrage contribution, per year |
| Post-tax return (bracket-adjusted) | INTL (tax) | **NEW as a Module-1 line** — equity-taxed 11% can beat debt-taxed 12% |

### 1C. Stress-window analysis (re-specified for cross-asset divergence)
| Dimension | Seen in | Multi-Asset translation |
|---|---|---|
| Category-defining crash deep-dive (IL&FS 2018 / 2022 growth-bear / midcap winter) | U | ⚠️ **Replaced by cross-asset years:** 2020 (equity crash + gold rally), **2022 (equity ↓ + debt ↓ + gold ↑ — THE test)**, 2024–25 |
| Recovery time from each crash | U | ✅ |
| **Rebalancing behaviour in the crash** (did it buy equity / harvest gold?) | — | **NEW** |
| "No-GFC/no-dotcom" missing-tail caveat | INTL | ✅ analog: has the fund seen a real bond+equity joint drawdown (2022)? |

---

## MODULE 2 — Risk Profile *(top weight, 25%)*

### 2A. Core risk metrics (universal)
| Dimension | Seen in | Multi-Asset translation |
|---|---|---|
| Volatility (multiple sources + MFAPI daily annualised + annual-by-year regime) | U | ✅ — should be structurally **low** (8–11%); high vol = closet equity |
| **Max Drawdown** — magnitude, multi-source, honest context | U | ✅ — **the headline value-prop metric; judged vs equity, must be < −20%** |
| Two-event / anatomy decomposition of the max DD | SC | ✅ |
| Recovery time / underwater duration | U | ✅ |
| Sharpe (cross-source reconciliation + category avg) | U | ✅ — structurally higher here; a low Sharpe is a *real* red flag |
| Sortino (+ why it matters for SIP) | U | ✅ |
| Calmar ratio (3Y/5Y/10Y) | U | ✅ |
| Alpha / Beta / R² vs benchmark | U | ✅ vs blended benchmark |
| Tracking error + Information Ratio (derived) | U | ✅ |
| Downside deviation, semi-deviation, VaR (95%) | SC | ✅ |
| Daily return distribution (up/down days, >2% days, worst/best single day) | U | ✅ |
| % from ATH (portfolio-health signal) | U | ✅ |
| **Upside/Downside capture ratios** vs benchmark | U | ✅ **vs Nifty 500 — downside capture <65% is the target** |
| PE valuation buffer of the equity sleeve | U | ✅ (equity book only) |
| SEBI risk category label | U | ✅ (will be lower than equity) |
| Risk-vs-alpha quadrant chart + full peer risk matrix + per-metric rank | U | ✅ |

### 2B. Structural / correlation risk
| Dimension | Seen in | Multi-Asset translation |
|---|---|---|
| **Structural buffer analysis** (bonds/international/cash as shock absorbers) | FC/SC | ✅ — **this IS the product**: quantify how much gold+debt cushioned each equity drawdown |
| **Correlation / R² to existing sleeves** (PP FlexiCap, DSP, etc.) | INTL/MC | ✅ — the single most important cross-sleeve number; how much *real* diversification |
| Correlation to Indian equity (decorrelation centerpiece) | INTL | ✅ measure the non-equity return stream's decorrelation |
| "No structural buffer / no-hedge" reality check | SC | ✅ inverted — here the buffer is the point |
| Redemption/liquidity-spiral risk | SC | ✅ note LOW (large-cap + gold ETF + debt are liquid) and move on |
| FoF daily-pricing caveat (if fund-of-funds structure) | INTL | ✅ if any gold/international leg is via FoF |
| **Cousin-category comparison** | — | **NEW** — benchmark risk vs Balanced Advantage/DAAF, Aggressive Hybrid, Equity Savings, Conservative Hybrid; multi-asset must beat these on downside for the same equity |

### 2C. Multi-asset-specific risk (NEW)
| Dimension | Multi-Asset translation |
|---|---|
| **Gold concentration risk** | **NEW** — gold itself draws −15/−20%; over-leaning gold swaps equity risk for commodity risk |
| **Debt-sleeve duration + credit risk** | **NEW** — the 2022 test: did the debt book add duration risk at the wrong time? credit quality of the book |
| **Realised cushioning in 2020 & 2022** | **NEW** — did the non-equity sleeves actually soften both, in NAV terms |
| Cushioning vs a Balanced Advantage / Aggressive Hybrid cousin | **NEW** — if it draws down like an aggressive hybrid, the gold isn't earning its place |
| **Equity-taxation continuity risk** | **NEW** — risk of gross equity slipping below 65% and the corpus losing equity taxation; a standing review trigger, priced as risk |

---

## MODULE 3 — Allocation Engine & Portfolio DNA

### 3A. Universal portfolio dimensions
| Dimension | Seen in | Multi-Asset translation |
|---|---|---|
| Asset allocation split (equity/debt/cash/…) | U | ✅ — **equity/debt/gold/silver/cash/REIT + its full history** |
| Top-10/20 holdings stock-by-stock with thesis | U | ✅ for the **equity sleeve** |
| Top-5/10/20 concentration | U | ✅ |
| Total stock count (is it over/under-diversified?) | U | ✅ (equity book) |
| Sector allocation + vs category + key over/underweights | U | ✅ (equity book) |
| Sub-sector deep dives on the biggest bets | U | ✅ as relevant |
| **Portfolio turnover** + implied holding period | U | ✅ — includes rebalancing-driven turnover |
| Portfolio PE / valuation character | U | ✅ (equity book) |
| Cash holding — level, purpose, history | U | ✅ |
| **AUM scalability** / position-size arithmetic / stress-test liquidity | U/SC | ✅ — note capacity is a **non-issue** here (large-cap + ETF); document why |
| Mandate-compliance check (actual vs SEBI minimum) | U | ✅ **two lines here:** the SEBI **≥3 asset classes, ≥10% each** rule, AND the **≥65% gross-equity** tax line |
| Mandate-change history | MC | ✅ (category/strategy reclassifications) |
| Cross-sleeve **overlap** (name-level vs existing funds) | INTL/MC | ✅ — equity book overlap with FlexiCap/MidCap picks |
| Look-through mechanism (if it holds other funds/ETFs) | INTL | ✅ for gold ETF / debt / international legs |

### 3B. The allocation-model core (the category's defining module — NEW)
| Dimension | Multi-Asset translation |
|---|---|
| **Allocation model classification** | **NEW** — static bands vs valuation-driven (P/E, P/B, yield-gap) vs discretionary/macro vs in-house quant |
| **Net vs gross equity** (arbitrage/derivative overlay) | **NEW** — is ≥65% real exposure or a tax-driven overlay? net equity = true risk |
| **Realised asset-class range/dynamism** (min/max of each class from trailing factsheets) | **NEW** — a fund stuck at 74% equity for 5yrs is closet-equity |
| **Gold/commodity mechanism** | **NEW** — physical-backed ETF vs futures/ETCD vs SGB vs silver; cost, tracking error, liquidity |
| **Debt-book construction** | **NEW** — duration, credit quality, govt vs corporate (also a risk input) |
| **Rebalancing discipline** — rules vs discretionary, frequency, evidence it fired at 2020/2022 turns | **NEW** |
| Active share vs a static-allocation benchmark | MC-analog | **NEW** — how far the fund's live weights deviate from its own strategic weights |
| **Arbitrage / hedged-equity sleeve** — size, cost drag, return contribution | **NEW** — the low-return sleeve used to clear 65% gross equity; quantify its drag on returns |
| **Asset-class breadth** — silver / REIT-InvIT / international inclusion beyond the equity-debt-gold core | **NEW** — extra diversification or complexity; note and assess each |
| **Structure: direct-holding vs fund-of-funds** for each non-equity leg | INTL-analog | **NEW** — drives tax classification, cost layering, and NAV-pricing lag |

---

## MODULE 4 — Cost **& Tax** Efficiency

### 4A. Universal cost dimensions
| Dimension | Seen in | Multi-Asset translation |
|---|---|---|
| Expense Ratio (Direct) — cross-source, peer rank | U | ✅ |
| **ER glide path over time** (has ER fallen as AUM grew?) | MC | ✅ |
| Regular-plan ER + **Direct-vs-Regular gap** + ₹ lost to distributor | U | ✅ |
| **Flow story — net inflows/outflows as a signal** ("is the market buying or leaving it?") | MC | ✅ |
| **10-Year SIP cost simulation** (identical gross CAGR, ER-only drag, ₹ corpus) | U | ✅ (use ~11% gross, not 18%) |
| ER savings across SIP amounts (₹5K–₹50K) | U | ✅ |
| SEBI TER slab positioning + buffer vs ceiling | U | ✅ |
| Exit load structure | U | ✅ |
| **Turnover-adjusted "true all-in cost"** (ER + hidden impact cost) | U | ✅ + rebalancing cost |
| Minimum SIP / lumpsum accessibility | U | ✅ |
| AUM trajectory & capacity | U | ✅ (capacity = strength here) |
| Double-layer cost (FoF wrapper + underlying) | INTL | ✅ if gold/intl legs are FoF |
| Fund revenue estimate / AMC economics from this fund | U | ✅ |

### 4B. The tax core (elevated to decisive — NEW/INTL)
| Dimension | Seen in | Multi-Asset translation |
|---|---|---|
| Taxation of the structure (equity vs debt/hybrid; LTCG/STCG rates) | INTL | ✅ **elevated to a scored, decisive line** |
| **Equity-taxation status** (≥65% gross equity → whole corpus at equity rates) | — | **NEW** — a permanent edge; gold+debt taxed at equity rates |
| **Internal rebalancing tax-shield** (fund rebalances tax-free vs DIY realising gains yearly) | — | **NEW** — model over 10Y; can exceed the ER premium |
| **True cost vs DIY = ER − both tax shields** (can be *negative*) | — | **NEW** — the finding that would justify the category |
| Cost vs the passive/DIY alternative, explicit | INTL/MC | ✅ vs the DIY basket |

---

## MODULE 5 — Fund Manager / Team Quality

| Dimension | Seen in | Multi-Asset translation |
|---|---|---|
| Manager identity, role, tenure on *this* fund | U | ✅ |
| Career timeline / full arc | U | ✅ |
| Credentials in context (vs peer managers) | U | ✅ |
| **Tenure-attribution** (which CAGR windows are actually theirs) | U/MC | ✅ |
| Investment philosophy — explicit, documented framework | U | ✅ — **the allocation model's philosophy** (mirrors M3) |
| Philosophy under stress (did they hold the line in each crash?) | U | ✅ |
| Sell / rebalance discipline | U/MC | ✅ **critical** — allocation timing IS the job |
| Cross-fund performance consistency (other schemes they run) | U | ✅ |
| Crisis experience (2008 GFC / prior cycles) | U | ✅ |
| **Co-manager / team depth & key-person risk** | U | ✅ **elevated** — needs equity + debt + commodity leads; solo = red flag |
| Succession plan / transition roadmap | U | ✅ |
| Skin in the game / co-investment | U | ✅ |
| Investor communication quality (letters, interviews, candour) | U | ✅ |
| Investor-base / retail-accountability character | SC | ✅ (retail SIP base vs HNI/institutional) |
| SEBI/regulatory record (personal) | U | ✅ |
| Two-layer manager structure (feeder operator vs real decision-maker) | INTL | ✅ if any sleeve is sub-advised/FoF |
| Manager accessibility / translation gap | INTL | ✅ |
| **Allocation-call track record** (added gold pre-2020/2022? cut equity at the top?) | — | **NEW** — reconstruct the equity/debt/gold path and grade the calls |

---

## MODULE 6 — AMC Trustworthiness

| Dimension | Seen in | Multi-Asset translation |
|---|---|---|
| AMC identity, corporate history, ownership type & structure | U | ✅ |
| Heritage / institutional longevity | U | ✅ |
| Ownership independence (bank/PSU/foreign/family) | U | ✅ |
| **Carry-forward verdict** for already-studied AMCs (update only the delta) | U/MC | ✅ — deep AMC bench exists; don't re-research |
| Total AUM, scheme count, AUM-per-scheme, fund-manager bench, employee count | U | ✅ |
| **Skin-in-the-game policy** (firm-wide) | U | ✅ |
| **Regulatory record** — SEBI actions, severity, context | U | ✅ |
| Fund-suite coherence / franchise commitment (serious vs flows-harvesting) | MC | ✅ — **is multi-asset a serious franchise or a defensive-flows autopilot product?** |
| Launch-timing honesty (did they launch at a top?) | MC | ✅ |
| Investor-first signals / flow-restriction discipline / gating history | U/SC | ✅ |
| Investor communication (quarterly letters, blog, CEO candour) | U | ✅ |
| AMC financial health / stability / revenue | U | ✅ |
| Custodian / RTA / trustee quality | U | ✅ |
| Global-parent vs local-entity trust split | INTL | ✅ if applicable |
| Major-scar deep-dive (e.g. Franklin 2020 debt freeze) | INTL | ✅ **and category-relevant** — check the AMC's **fixed-income desk** for credit blowups (multi-asset imports the debt competence) |
| **Commodity/gold-desk credibility** | — | **NEW** — does the AMC run gold/commodity seriously? |

---

## Summary — what is NEW for Multi Asset (no prior analog)

These have **no template** in the four prior studies and must be built from scratch:

1. **Blended-benchmark construction** (M1) — no single index exists.
2. **DIY-basket counterfactual, post-tax** (M1/M4) — replaces "why not the index fund?".
3. **Allocation-vs-selection alpha decomposition** (M1).
4. **Asset-class return attribution** — equity/debt/gold/arbitrage contribution per year (M1).
5. **The allocation-model classification** — static/valuation/discretionary/quant (M3, the defining dimension).
6. **Net-vs-gross equity & the arbitrage overlay** (M3), incl. the arbitrage sleeve's size & drag.
7. **Realised asset-class range/dynamism** from trailing factsheets (M3).
8. **Asset-class breadth** — silver/REIT/international beyond the core three (M3).
9. **Direct-holding vs FoF structure per leg** — drives tax, cost, pricing (M3).
10. **Gold mechanism** + **debt duration/credit** as first-class (M3/M2).
11. **Rebalancing discipline with evidence** (M3/M5).
12. **The tax triad** — equity-tax status, internal rebalancing shield, true-cost-vs-DIY (M4) — the decisive edge.
13. **Equity-taxation continuity risk** — slipping below 65% gross equity (M2, review trigger).
14. **Allocation-call track record** for the manager/team (M5).
15. **Gold/commodity-desk + fixed-income-desk credibility** at the AMC (M6).
16. **Gold-concentration & joint equity+debt (2022) drawdown** risk (M2).
17. **Cousin-category comparison** — BAF/DAAF, Aggressive Hybrid, Equity Savings (M2).
18. **SEBI ≥3-asset-class / ≥10%-each mandate compliance** (M3).

Everything else in the tables above is **inherited unchanged or lightly adapted** — the full apparatus of the four prior studies carries into Multi Asset.

---

## How to use this file as a gate

- **Per fund:** before a fund's README is written, confirm all six module files cover their rows above. A row may be answered with "N/A + one-line reason" (e.g. no FoF leg) — but it must be *addressed*, not silently skipped.
- **The Tier-1 ten (§0) are mandatory** and must be prominent in the README scorecard, not buried.
- **NEW dimensions** carry a data-effort cost (§0.1) — factor into study order; build the reconstruction templates on the first (longest-record) fund.
- Treat this as versioned: if a fund surfaces a dimension not listed here, add it and note which fund introduced it (the Edelweiss retrofit discipline).

---

*Created: July 28, 2026 · refined v1.1 same day (added §0 Tier-1 decisive set, §0.1 data-provenance, 12 gap dimensions, coverage-gate convention) | Source: DSP SmallCap (all 6 modules, most granular), cross-checked vs Franklin International (currency/tax/FoF/SEBI-cap) and Edelweiss MidCap (active-share, cross-module retrofit, carry-forward AMC). This checklist is the completeness gate for every fund's 6-module write-up in this study.*
