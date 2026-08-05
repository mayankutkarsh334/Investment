# Screening Methodology — Multi Asset Allocation Funds

**Context:** ₹15–20K/month SIP (working assumption), 7–10+ year horizon. Fifth category study, following the FlexiCap / SmallCap / International / MidCap pipeline. Same 2-stage screening, with **the most category-specific calibrations yet** — because this is the first hybrid (equity + debt + gold) category studied.

**Universe:** 35 Multi Asset Allocation Funds (Direct plan, Growth option) — data pulled **July 28, 2026** directly from the Tickertape screener API (`api.tickertape.in/mf-screener/query`, subsector = "Multi Asset Allocation Fund"). Raw pull saved as:

```
Mutual Fund/TickerTape Data/MultiAsset_Screener_API_28_07_2026.csv           (35 Growth-plan funds, cleaned)
Mutual Fund/TickerTape Data/MultiAsset_Screener_API_28_07_2026_raw_all_variants.csv   (109 raw rows, all plan variants)
```

> **Phase 0 (portfolio-fit) is DEFERRED to decision-tree time** (user decision, Jul 28 2026 — MidCap precedent). The DIY-basket and tax-status tests survive inside every Module 1/4. This screening is the study's true starting point.

---

## Data Provenance & Cleaning

The raw API pull returned **109 rows**. Cleaning to the analysable universe:

| Step | Action | Result |
|------|--------|--------|
| 1 | Collapse plan variants (IDCW-Payout / IDCW-Reinvest / Monthly-IDCW / Quarterly-IDCW / Annual-IDCW) to the **Growth** plan per scheme | 109 rows → 40 distinct schemes |
| 2 | **Remove 3 SIF long-short products** — iSIF / DynaSIF / Qsif "Active Asset Allocator Long-Short Fund" are Specialized Investment Funds (long-short mandates, ₹10L minimums), filed under this subsector but structurally incomparable (same exclusion as MidCap's SIF removal) | 40 → 37 |
| 3 | **Remove 2 target-date lifecycle FoFs** — Zerodha Life Cycle Fund 2036 / 2041 are glide-path target-date funds, not discretionary multi-asset-allocation funds | 37 → **35** |
| 4 | Direct-plan figures confirmed | 35 final |

**Known data caveats (material — shape the whole study):**

| Caveat | Impact |
|--------|--------|
| `ageInMon` caps at **163 months** (~13.6y) | Funds showing 163 are *at least* 13.6y old; true inception verified per fund in deep study |
| **`percOtherH` returns 0 for every fund** — the API does **not** expose the gold/commodity sleeve | The single most important category field is missing at screening. `percEquityH` + `percDebtH` never sum to 100; the remainder (17–47%) is **gold + cash + arbitrage + international**, invisible here. The equity/debt/gold split is a **Module-3 factsheet task**, exactly as the study plan warned |
| `percEquityH` is likely **net** (unhedged) equity | Cannot confirm the ≥65%-**gross**-equity tax status from the API; a fund at 47% net may still clear 65% gross via arbitrage. Tax status confirmed per fund from SID/factsheet |
| Premium-gated: max drawdown, rolling returns, top-10 concentration | Computed independently from MFAPI NAV history in the deep-study modules (the canonical method) |

---

## Why Multi Asset Screening Differs from the Four Siblings

### 1. There is no common benchmark — and funds exploit that
The 35 funds report **eight different benchmarks**: NIFTY 50 TRI (HDFC, Bajaj, Union, Samco, Shriram), BSE 200 (UTI, Tata, ABSL), BSE 500 TRI (SBI, Nippon), NIFTY 200 TRI (ICICI, Invesco), NIFTY 500 TRI (Quant + most young funds), and — tellingly — **pure-debt or gold indices** for the conservative funds (Edelweiss & WOC use CRISIL Short-Term Bond; 360 ONE uses Gold-India; Quantum uses NIFTY Composite Debt). A fund that benchmarks a 68%-equity book against NIFTY 50 TRI, or a balanced book against a short-term bond index, is choosing an easy bar. **The blended-benchmark construction (Module 1) is therefore non-negotiable** — screening `alpha` figures are computed against these self-selected benchmarks and are treated as *indicative only*.

### 2. No AUM ceiling (unlike MidCap)
Capacity is a non-issue: the equity book is large/mega-cap-tilted, and debt + gold ETFs are effectively unlimited. The MidCap 150-stock capacity ceiling has **no analog**. Only an AUM **floor** (₹500 Cr) applies. This is the single biggest structural difference from the MidCap screen.

### 3. The ER ceiling is 1.2%, not 1.0%
Softer than Mid/SmallCap because the counterfactual is a **multi-leg DIY basket** (equity index + debt fund + gold ETF, whose all-in cost + rebalancing tax exceeds a single 0.20% tracker), not a cheap single index fund. Still a ceiling — above 1.2% is hard to justify.

### 4. Sharpe ≥ 0 bites far less, and means less
Multi-asset funds are structurally low-volatility (screener stdDev 9–11% for equity-oriented, 2.6–6.9% for conservative, vs ~15–16% for equity funds). Sharpe is mechanically lifted. A *near-zero* Sharpe here (Quantum 0.13, Samco −0.05, Groww −0.04, Capitalmind −0.98, JM −1.17) is a genuine red flag, not a marginal miss.

### 5. **The defining finding: the category is a post-2023 launch wave — so the age filter is replaced**
This is the multi-asset analog of International's SEBI-cap discovery — a structural fact that reshapes the study before any fund is opened.

**Only 8 of 35 funds are ≥60 months old.** The other 27 launched after ~July 2021, the overwhelming majority **after April 2023**, when the removal of debt-fund indexation benefits made a ≥65%-gross-equity multi-asset fund the most tax-efficient way to hold gold and debt. The category as it exists today was largely *manufactured by a tax change* — precisely the structural edge this study is built to interrogate.

**A rigid ≥60-month filter guts the category (35 → 7) and eliminates the entire conservative sub-type.** Its real purpose was never "60 months" — it was **data sufficiency** (the framework's 3Y-rolling / 3Y-CAGR metrics need ~3 years of NAV) plus **stress exposure**. So the age filter is **replaced** (user decision, Jul 28 2026):

- **A 3-year track-record floor (≥36 months)** — the minimum to compute the framework's 3Y metrics and to have traversed the **Sep 2024 – Mar 2025 correction** (the study plan's "universal, no-excuses stress test").
- **"Saw 2022" is demoted from a hard cut to a per-fund `no-2022-data` flag**, carried into Modules 1 & 2 (whose risk analysis then leans on 2024–25 and notes the gap). MidCap precedent: Mahindra Manulife carried a `no-2018-data` flag rather than elimination.

The ≥36-month floor — chosen over ≥24/≥30 (flood Stage 2 with funds lacking any multi-year return to rank) and ≥60 (guts the category) — doubles the survivor pool (7 → 11) and admits the conservative sub-type **naturally** (WOC, Edelweiss), so no special one-fund relaxation is needed.

---

## Stage 1 — Hard Filters (applied in order)

| Filter | Threshold | Rationale | vs siblings |
|--------|-----------|-----------|-------------|
| Expense Ratio | ≤ 1.2% (Direct) | Active fee vs a multi-leg DIY basket | Softer than Mid/SmallCap (1.0%), tighter than FlexiCap (1.5%) |
| AUM minimum | ≥ ₹500 Cr | Operational viability | Same as siblings |
| AUM maximum | **None** | Capacity is a non-issue for a large-cap + ETF book | **Dropped — unique to this study** |
| **Track record** | **≥ 36 months** (replaces ≥60mo) | 3-year floor for the framework's 3Y metrics; covers the Sep-2024–Mar-2025 correction. Funds 36–59mo carry a `no-2022-data` flag into Modules 1/2 | **Replaced** — was ≥60mo; the category-youth finding forced the change |
| Sharpe | ≥ 0 | Below risk-free is disqualifying | Same threshold, weaker bite |

**Result: 35 → 11.** The ≥36mo track-record floor eliminated **23 funds** (all <36mo — the youngest of the launch wave); **Axis** (ER 1.44%) fell on ER; **Union** (ER 1.28% + age) also out. See [stage1_hard_filters.md](stage1_hard_filters.md).

**11 survivors:** ICICI Pru, SBI, Nippon India, WOC, Aditya Birla SL, UTI, HDFC, Quant, Tata, Edelweiss, Baroda BNP Paribas. (Four carry the `no-2022-data` flag: WOC 39mo, ABSL 43mo, Edelweiss 38mo, Baroda 44mo.)

---

## Stage 2 — Performance / Fitness Filters

Raw CAGR is the wrong primary screen for a risk-reduction product (study-plan principle). Because most survivors now lack 5Y history, Stage 2 runs on a **3-year basis** (available for all 11) with a risk-adjusted co-primary — a **fitness floor**: eliminate a fund only if it is below **both** the 3Y-CAGR median **and** the Sharpe median.

| Filter | Threshold | Value (over 11 S1 survivors) |
|--------|-----------|------------------------------|
| 3Y CAGR | vs survivor median | median = **16.21%** |
| Risk-adjusted (Sharpe) | vs survivor median | median = **0.86** |
| **Elimination rule** | Below **both** medians | → eliminated |

**Result: 11 → 6.** Passing: Quant, Nippon India, WOC, Aditya Birla SL, UTI (on 3Y), SBI (on risk-adj). Eliminated: **ICICI Pru, Baroda, Tata, HDFC, Edelweiss** (each below both medians). See [stage2_performance.md](stage2_performance.md).

> **The headline elimination:** **ICICI Pru Multi-Asset — the ₹84,000 Cr category flagship — screens out** (3Y 15.7% < 16.21; Sharpe 0.29 < 0.86). On a merit basis its prominence is AUM, not risk-adjusted quality. It is retained as a **flagged instructive/reference case**, not silently dropped.

---

## The Shortlist (6) + Instructive Cases

| # | Fund | AUM (₹Cr) | ER | Age (mo) | Net Eq% | 3Y | Sharpe | Lean | Flag |
|---|------|-----------|----|----|---------|----|--------|------|------|
| 1 | **Quant Multi Asset** | 5,615 | 1.16 | 163 | 52.7 | 22.7 | 1.52 | Balanced/dynamic — return leader | — |
| 2 | **Nippon India Multi Asset** | 16,000 | 0.43 | 72 | 56.2 | 19.2 | 0.88 | Balanced — cheapest, fee-for-outcome | — |
| 3 | **WOC (WhiteOak) Multi Asset** | 7,763 | 0.67 | 39 | 26.4 | 16.7 | 1.20 | **Conservative** representative | no-2022-data |
| 4 | **Aditya Birla SL Multi Asset** | 6,989 | 0.68 | 43 | 67.8 | 16.5 | 0.89 | Equity-oriented | no-2022-data |
| 5 | **UTI Multi Asset** | 6,890 | 0.88 | 163 | 66.4 | 16.5 | 0.36 | Equity-oriented — borderline (weak Sharpe) | — |
| 6 | **SBI Multi Asset Allocation** | 19,354 | 0.74 | 161 | 46.8 | 16.2 | 0.93 | Lower-equity / most debt-gold | — |

**Segmentation now falls out of the rule:** conservative (WOC 26% eq) · balanced (SBI 47%, Quant 53%, Nippon 56%) · equity-oriented (UTI 66%, ABSL 68%). Both sub-types represented without a special relaxation.

**Instructive-case candidates (out of shortlist):**
- **ICICI Pru Multi-Asset** — **the ₹84,000 Cr flagship that screened out.** The most interesting reference case in the study: why does the category's largest, longest-record fund post a 0.29 Sharpe and below-median 3Y? Studied as the "size ≠ quality" cautionary reference.
- **HDFC Multi-Asset** — the underperforming veteran (13.6y, 3Y 12.4%, Sharpe 0.20, benchmarks NIFTY 50 TRI). Confirm-the-elimination + the clearest *flattering* self-benchmark case.
- **DSP Multi Asset** — the young "new-wave" case (₹10,105 Cr, 35mo — just below the 36mo floor, Sharpe 1.17; DSP AMC verdict carries forward at 4.0). Is the young cohort's high Sharpe genuine or a bull-market-only artifact?

---

## The Segmentation Question — resolved by the ≥36mo replacement itself

The locked decision (Jul 28 2026) was to study **both** equity-oriented and conservative/debt-oriented sub-types, segmented. Under the old ≥60mo filter this was impossible (every conservative fund was young). **Replacing the age filter with the ≥36mo track-record floor resolves it structurally** — the conservative sub-type now enters on its own merit:

- **Conservative:** WOC (26% eq / 30% debt / 44% gold-cash-arb, 39mo) is shortlisted; Edelweiss (22% eq / 52% debt, stdDev 2.6% — nearly a debt fund, 38mo) survived Stage 1 but fell at Stage 2 (3Y 7.7%, Sharpe at median).
- **Balanced:** SBI (47%), Quant (53%), Nippon (56%).
- **Equity-oriented:** UTI (66%), ABSL (68%).

No special one-fund relaxation is needed — the earlier WOC-only patch is **superseded** by the rule. Still-young conservative flavors not captured (all <36mo): Invesco (37% eq, gold-heavy), 360 ONE, Bank of India — available as instructive add-ons only if requested.

---

## What the Filters Cannot Catch (deferred to modules)

1. **Equity/debt/gold split & its history** — the defining category data; not in the API (`percOtherH` = 0). Module 3, from factsheets.
2. **Net vs gross equity / arbitrage overlay** — determines both true risk and tax status. Module 3.
3. **Gold mechanism, debt duration/credit** — Module 2/3.
4. **Blended-benchmark alpha & the post-tax DIY-basket test** — the decisive returns question. Module 1 × Module 4.
5. **Allocation model** (static vs valuation-driven vs discretionary) — Module 3.
6. **AMC carry-forward** — ICICI, SBI, Nippon, Quant, HDFC, UTI, Tata AMCs; several already have verdicts from prior studies (Quant's active SEBI front-running probe is a known negative; ICICI, Nippon referenced before). Module 6.

---

*Methodology version: 2.0 (age filter replaced with ≥36mo track-record floor) | Created July 28, 2026; revised same day | Data: Tickertape screener API, Jul 28 2026, Direct Growth | Universe: 35 (from 109 raw rows: −74 plan variants, −3 SIF long-short, −2 target-date lifecycle) | Funnel: **35 → 11 → 6** | Defining finding: post-2023 tax-driven launch wave forced replacing the ≥60mo age filter with a ≥36mo track-record floor + `no-2022-data` flag; ICICI Pru (₹84K Cr flagship) screens out on merit*
