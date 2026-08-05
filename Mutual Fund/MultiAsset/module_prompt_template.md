# Module Study Prompt — Multi Asset Allocation

Reusable prompt for commissioning each deep-study module, matching the depth of the FlexiCap / SmallCap / International / MidCap studies. **Fill the two placeholders**, paste the **Base Prompt**, then append the matching **Module Focus Block**.

- `{{FUND}}` — e.g. *SBI Multi Asset Allocation Fund (Direct-Growth)*
- `{{MODULE}}` — 1–6

**Shortlist & order:** SBI → Nippon → Quant → UTI → ABSL → WOC · instructive: ICICI Pru, HDFC, DSP.
`no-2022-data` funds (WOC, ABSL): risk/return modules lean on the Sep-2024–Mar-2025 correction and flag the missing 2022 all-classes-diverge year.

---

## BASE PROMPT (paste for every module)

> Write **Module {{MODULE}}** for **{{FUND}}** in the Multi Asset Allocation category study (`Mutual Fund/MultiAsset/`). This is the fifth category study — match the exact depth, structure, and honesty of the prior studies (see any `Mutual Fund/MidCap/funds/edelweiss/module*.md` or `SmallCap/funds/dsp/module*.md` as the quality bar).
>
> **Read first:** `MultiAsset/study_plan.md` (framework + the multi-asset adaptations), `MultiAsset/dimensions_covered.md` (the completeness gate — your module MUST address every row in its section, plus the Tier-1 §0 dimensions and the relevant NEW dimensions; a row may be "N/A + one-line reason" but never silently skipped), and `MultiAsset/screening/` (the fund's screening data + the two structural findings).
>
> **Weights (LOCKED, multi-asset re-weight):** Risk 25 · Returns 20 · Allocation-Engine 20 · Cost+Tax 20 · Manager 10 · AMC 5. Scale 1–5 (1 Poor … 5 Excellent). Note in the module that these scores are NOT directly comparable to the four equity categories.
>
> **The four framing facts that rewrite this category (apply throughout):**
> 1. **No single benchmark** — build a **blended benchmark** from index-fund NAV legs (the fund's *stated* strategic weights, e.g. 65% Nifty 500 TRI / 25% NIFTY Composite Debt / 10% domestic gold). Treat the fund's self-selected Tickertape benchmark as indicative only, and critique whether it is honest (several funds pick flattering indices).
> 2. **The counterfactual is DIY, not an index fund** — the fund must beat a **naïve static 65/25/10 annually-rebalanced basket, post-tax**.
> 3. **Tax is a first-class scored variable** — equity-tax status (≥65% gross equity), the internal tax-free-rebalancing shield, and true-cost-vs-DIY.
> 4. **Risk + the allocation engine carry the thesis, not raw return.**
>
> **Method (the canonical apparatus, proven across four studies):**
> - **Self-compute from MFAPI NAV history** (`api.mfapi.in/mf/<code>`): CAGR (1/3/5/10Y/SI), calendar-year returns, rolling 3Y/5Y distributions, drawdown + recovery, SIP XIRR (Newton-Raphson), daily-return distribution — whatever the module needs. State the scheme code and NAV count.
> - **Cross-source verification** table (Tickertape, MFAPI-computed, ValueResearch, AdvisorKhoj, Morningstar) — reconcile and flag anomalies (e.g. Tickertape Sortino/alpha quirks).
> - **Gold/debt/net-gross-equity data is NOT in the screener API** (`percOtherH` = 0). Pull it from the **AMC monthly factsheet + SID**; reconstruct the trailing asset-class path from 12–36 months of factsheets where the module needs it (see `dimensions_covered.md` §0.1 for the per-dimension provenance).
> - **Mermaid charts** (xychart-beta / pie / quadrant / timeline) for every major comparison, as in prior modules.
> - **Comparative tables** vs already-studied MultiAsset funds (and, where illuminating, vs the equity-category funds) + vs the DIY basket.
> - Handle the **`no-2022-data` flag** for WOC/ABSL: lean on 2024–25, state the gap explicitly.
>
> **Output structure (match prior modules exactly):**
> 1. `# Module {{MODULE}}: <Title> — {{FUND}}` + a provisional-score line at top.
> 2. Fund Identity / Raw Data table **with per-metric source attribution**.
> 3. Cross-source verification.
> 4. The module's analytical sections (see the Module Focus Block below) — each with data, a chart, and interpretation.
> 5. Comparative tables vs studied funds + the DIY/blended-benchmark comparison.
> 6. **Points For / Points Against** (explicit lists).
> 7. **Scorecard** — every sub-dimension scored 1–5 with one-line reasoning, a mermaid score chart, and the weighted **Module {{MODULE}} Overall** score.
> 8. Comparative module scores (vs studied funds).
> 9. **SIP Implication** + **One-Line Verdict**.
> 10. Footer: provisional score + note any cross-module retrofit (the Edelweiss discipline — if this module changes an earlier module's conclusion, say so).
>
> Save to `Mutual Fund/MultiAsset/funds/<fund_slug>/module{{MODULE}}_<name>.md`. Be honest — surface weaknesses as prominently as strengths; a flattering module is a failed module. **Not investment advice** — mechanics and evidence only.
>
> Then append the Module Focus Block below.

---

## MODULE FOCUS BLOCKS (append the one matching {{MODULE}})

### Module 1 — Returns & Allocation Alpha (20%) → `module1_returns.md`
> Focus: CAGR ladder + trajectory; rolling 3Y/5Y distributions + probability-of-loss by holding period; calendar years **chosen for asset-class divergence** (2019 gold, **2020** crash+gold rally + rebalancing behaviour, 2021 opportunity cost, **2022 all-classes-diverge — THE test**, 2023, 2024 gold cushion, **2024–25 correction**); SIP XIRR vs lumpsum.
> Category-critical: **build the blended benchmark**; **decompose alpha into allocation-timing vs security-selection**; **asset-class return attribution** (equity/debt/gold/arbitrage per year); **beat the post-tax DIY static basket?**; **post-tax return** (bracket-adjusted); benchmark-appropriateness critique. Inception-bias discount for young funds.

### Module 2 — Risk Profile (25% — the thesis module) → `module2_risk.md`
> Focus (judged vs equity, not just peers): max drawdown + downside capture **vs Nifty 500** (target DD < −20%, downside capture < 65%); volatility (target 8–11%); Sharpe/Sortino/Calmar; recovery time; daily distribution; % from ATH.
> Category-critical: **realised 2020 & 2022 cushioning** in NAV terms; **correlation / R² vs the existing sleeves** (Parag Parikh FlexiCap + the chosen equity picks) — the decisive cross-sleeve number; **debt-sleeve duration + credit risk**; **gold-concentration risk**; **cousin-category comparison** (Balanced Advantage/DAAF, Aggressive Hybrid, Equity Savings); **equity-taxation continuity risk** (slipping below 65% gross).

### Module 3 — Allocation Engine & Portfolio DNA (20% — the defining module) → `module3_allocation.md`
> Focus: equity/debt/gold/silver/cash split **and its trailing history**; equity-book holdings/concentration/sector/PE; turnover; overlap with existing sleeves; SEBI mandate compliance (**≥3 asset classes / ≥10% each** AND the **≥65% gross-equity** tax line).
> Category-critical (the analog of MidCap's active share): **classify the allocation model** (static bands vs valuation-driven vs discretionary vs quant); **net-vs-gross equity + arbitrage overlay** (size & drag); **realised asset-class range/dynamism**; **gold mechanism** (physical ETF vs futures/ETCD vs SGB vs silver); **debt-book construction**; **rebalancing discipline with evidence** it fired at 2020/2022 turns; **direct-holding vs FoF per leg**.

### Module 4 — Cost & Tax Efficiency (20%) → `module4_cost_tax.md`
> Focus: ER (Direct) + peer rank; ER glide; Direct-vs-Regular gap + ₹ lost; 10Y SIP cost simulation (~11% gross); SEBI TER buffer; exit load; turnover-adjusted true cost; flow-as-signal; min SIP; AUM/capacity (a strength here).
> Category-critical (**the module where a fund can win vs DIY**): the **tax triad** — (a) equity-taxation status (≥65% gross → whole corpus at equity rates); (b) internal tax-free-rebalancing shield modelled over 10Y; (c) **true cost vs DIY = ER − both shields** (can be *negative*). Double-layer cost if any FoF leg.

### Module 5 — Fund Manager / Team Quality (10%) → `module5_manager.md`
> Focus: identity/role/tenure/attribution; philosophy of the allocation model + under-stress discipline; sell/rebalance discipline; cross-fund record; crisis experience; skin-in-game; communication; SEBI record; investor base.
> Category-critical: **team depth** (needs equity + debt + commodity leads — solo = red flag) & key-person/succession risk; **allocation-call track record** — reconstruct the equity/debt/gold path and grade the calls (added gold pre-2020/22? cut equity at the Sep-2024 top?).

### Module 6 — AMC Trustworthiness (5%) → `module6_amc.md`
> Focus: **carry forward** the existing AMC verdict where one exists (ICICI, SBI, Nippon, Quant, HDFC, UTI, ABSL, WhiteOak) and update only the delta; ownership/heritage/independence; skin-in-game; regulatory record; financial health; custodian/RTA; communication; succession.
> Category-critical: **fund-suite coherence / launch-timing honesty** (serious franchise vs 2023-tax-wave flows-harvesting); **fixed-income-desk credibility** (a strong equity AMC can run a weak debt desk — multi-asset imports it); **gold/commodity-desk credibility**. **Quant:** the active SEBI front-running probe is a potential veto — treat prominently.

---

## After all six modules → README (written last)
> Write `funds/<fund_slug>/README.md`: fund summary, the 6-module weighted scorecard (weights 20/25/20/20/10/5 for M1–M6), final weighted score out of 5, key strengths/weaknesses, the fund-vs-DIY-basket verdict, monitoring/review triggers (allocation-model drift toward closet-equity, tax-status change below 65% gross, debt-book credit deterioration, manager/team exit), and where it sits vs the other studied MultiAsset funds. Same structure as `MidCap/funds/edelweiss/README.md`.

---

*Template v1.0 · Jul 28 2026 · reproduces the 4-study module depth with the multi-asset adaptations · pair with [dimensions_covered.md](dimensions_covered.md) (completeness gate) and [study_plan.md](study_plan.md).*
