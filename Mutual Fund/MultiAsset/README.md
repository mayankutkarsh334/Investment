# Multi Asset Allocation Funds — Category Study

Fifth category study (after FlexiCap, SmallCap, International, MidCap). Same 6-module weighted framework, **re-weighted** for a risk-reduction product. See [study_plan.md](study_plan.md) and the completeness gate [dimensions_covered.md](dimensions_covered.md).

**Weights (LOCKED):** Risk 25 · Returns 20 · Allocation-Engine 20 · Cost+Tax 20 · Manager 10 · AMC 5.

---

## Status

| Phase | State |
|-------|-------|
| Study plan + dimension checklist | ✅ Done (Jul 28 2026) |
| **Phase 1 — Screening** | ✅ **Done (Jul 28 2026): 35 → 11 → 6** (age filter replaced by ≥36mo track-record floor) |
| Phase 2 — Deep modules | 🔄 **In progress** — **Nippon ≈3.71** > **SBI ≈3.66** >> **Quant ≈3.20** (all COMPLETE). Next: UTI → ABSL → WOC → instructive → decision tree |
| Phase 3 — Decision tree | ⏳ Not started |

---

## The two structural findings from screening

1. **The category is a post-2023 tax-driven launch wave.** Only **8 of 35** funds are cycle-tested (≥60 months); the rest launched after the April-2023 removal of debt-fund indexation made ≥65%-equity multi-asset the tax-efficient way to hold gold + debt. This is the multi-asset analog of International's SEBI-cap finding — and it **forced replacing the age filter** with a **≥36-month track-record floor** (+ `no-2022-data` flag), which naturally admits the conservative sub-type (WOC) so segmentation needs no special hack.
2. **The ₹84,000 Cr flagship screens out.** ICICI Pru Multi-Asset — the category's largest, longest-record fund — fails the Stage-2 fitness floor (3Y 15.7% and Sharpe 0.29, both below median). Its prominence is AUM, not risk-adjusted quality. Retained as a flagged **instructive/reference case**.

---

## The Shortlist (6)

| # | Fund | AUM (₹Cr) | ER | Net Eq% | 3Y | Sharpe | Lean | Flag |
|---|------|-----------|----|---------|----|--------|------|------|
| 1 | **Quant Multi Asset** | 5,615 | 1.16 | 52.7 | 22.7 | 1.52 | Balanced/dynamic — return leader | — |
| 2 | **Nippon India Multi Asset** | 16,000 | 0.43 | 56.2 | 19.2 | 0.88 | Balanced — cheapest, fee-for-outcome | — |
| 3 | **WOC (WhiteOak) Multi Asset** | 7,763 | 0.67 | 26.4 | 16.7 | 1.20 | **Conservative** — 26% eq / 44% gold-cash-arb, 6.9% vol | ⚠ no-2022 |
| 4 | **Aditya Birla SL Multi Asset** | 6,989 | 0.68 | 67.8 | 16.5 | 0.89 | Equity-oriented | ⚠ no-2022 |
| 5 | **UTI Multi Asset** | 6,890 | 0.88 | 66.4 | 16.5 | 0.36 | Equity-oriented — borderline (weak Sharpe) | — |
| 6 | **SBI Multi Asset Allocation** | 19,354 | 0.74 | 46.8 | 16.2 | 0.93 | Lower-equity / most debt-gold | — |

**Segmentation (falls out of the rule):** conservative (WOC) · balanced (SBI, Quant, Nippon) · equity-oriented (ABSL, UTI).

**Instructive cases (out of shortlist):** **ICICI Pru** (the ₹84K Cr flagship that screened out — size ≠ quality) · **HDFC** (underperforming veteran / flattering NIFTY-50 benchmark) · **DSP** (young "new-wave" case, ₹10,105 Cr, 35mo, DSP AMC carries forward at 4.0).

---

## Study Order (proposed)

| Priority | Fund | Rationale | Key question |
|----------|------|-----------|--------------|
| **1** | **SBI Multi Asset Allocation** | Cycle-tested (161mo — full 2022 history), strong Sharpe (0.93), lowest net equity (46.8%) — builds the reference frame (blended-benchmark, DIY-basket, factsheet-reconstruction templates) on the fund closest to a true diversifier | Does more non-equity actually decorrelate from the existing sleeves, or just lower the return? |
| **2** | **Nippon India Multi Asset** | Cheapest survivor (0.43% ER), strong risk-adjusted (Sharpe 0.88, 3Y 19.2%), cycle-tested (72mo) | Is the low fee + strong risk-adj return the genuine fee-for-outcome pick? |
| **3** | **Quant Multi Asset** | The return leader (3Y 22.7%, Sharpe 1.52), cycle-tested — but the **Quant AMC SEBI front-running probe** (Module 6 carry-forward) may veto it | Is the category-leading return real allocation skill, and does the AMC governance file kill it anyway? |
| **4** | **UTI Multi Asset** | Cycle-tested (163mo) but the **borderline pass** (Sharpe 0.36) — study after the strong cycle-tested funds to test whether long record + decent 3Y survive the weak risk-adjusted profile | Does the veteran's weak Sharpe disqualify it in Module 2, or is it an artifact of a defensive book? |
| **5** | **Aditya Birla SL Multi Asset** | Equity-oriented young fund (43mo, `no-2022-data`); studied after the cycle-tested cohort so templates exist and the 2022 gap is contextualised | Real allocation process or closet-equity? |
| **6** | **WOC (WhiteOak) Multi Asset** | The conservative representative (39mo, `no-2022-data`); 26% eq / 44% gold-cash-arb, 6.9% vol | Does a genuinely conservative fund decorrelate enough to beat DIY debt+gold — and is its 44% "other" gold or arbitrage? |
| Instructive A | **ICICI Pru Multi-Asset** | The ₹84,000 Cr flagship that screened out — the "size ≠ quality" reference | Why does the category's largest, longest-record fund post a 0.29 Sharpe and below-median 3Y? |
| Instructive B | **HDFC Multi-Asset** | Confirm-the-elimination; the clearest flattering-benchmark case | Why does the 13.6y veteran lag, and is its NIFTY-50 self-benchmark honest? |
| Instructive C | **DSP Multi Asset** | The post-2023 tax-driven cohort; DSP AMC verdict carries forward (4.0 from SmallCap) | Is the young cohort's high Sharpe genuine or a bull-market-only artifact (never saw 2022)? |

---

## Screening artifacts

- [screening/methodology.md](screening/methodology.md) — thresholds, category-specific calibrations, the two structural findings
- [screening/stage1_hard_filters.md](screening/stage1_hard_filters.md) — 35 → 11 (≥36mo track-record floor)
- [screening/stage2_performance.md](screening/stage2_performance.md) — 11 → 6 (3Y fitness floor)
- [screening/all_funds_data.md](screening/all_funds_data.md) — full 35-fund data snapshot
- Raw: `TickerTape Data/MultiAsset_Screener_API_28_07_2026.csv`

---

*Category study README | Screening complete Jul 28 2026 (35 → 11 → 6; age filter replaced by ≥36mo track-record floor) | Shortlist: Quant, Nippon, WOC, ABSL, UTI, SBI | Instructive: ICICI (flagship that screened out), HDFC, DSP | Deep studies not started*
