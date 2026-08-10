# Stage 4 — Corrected Split Adjustment, and the Category-Defining Finding

**Supersedes the rankings in [stage3_robustness.md](stage3_robustness.md).** Chasing the SBI/Axis anomaly exposed a bug in my own split adjustment. Fixing it changed every number — and collapsed the ranking.

---

## The bug

The first-pass detector divided by the **raw** NAV ratio on a split day, which bakes that day's genuine gold move into the split factor. A small factor error becomes a *permanent* level shift, and every window spanning the split inherits a spurious CAGR.

**Fix:** isolate the pure split component — `factor = (nav_t / nav_t−1) / (1 + market_return_t)`.

| Scheme | Split date | Raw factor | Corrected | **Raw was off by** |
|---|---|--:|--:|--:|
| **ICICI Gold ETF** | 2018-07-03 | 0.10758 | 0.09943 | ⚠ **+8.20%** |
| **Axis Gold ETF** | 2020-07-27 | 0.01026 | 0.00999 | ⚠ **+2.70%** |
| Invesco Gold FoF | 2019-10-25/29 | — | — | ±1.00% |
| Quantum Gold ETF | 2021-12-20 | 0.01986 | 0.01999 | −0.65% |
| ICICI Gold ETF | 2018-11-19 | 0.10069 | 0.10011 | +0.58% |
| Nippon Gold BeES | 2019-12-23 | 0.01004 | 0.01000 | +0.40% |

## Corrected rolling 3-year tracking difference (19 windows, 2014-06 → 2026-08)

| Scheme | Type | Median TD | IQR |
|---|:--:|--:|---|
| ⚠ SBI Gold Fund | FoF | 0.30% | [0.26, 0.65] |
| Axis Gold Fund | FoF | 0.43% | [0.29, 0.78] |
| Invesco Gold FoF | FoF | 0.48% | [0.34, 1.00] |
| ICICI Gold ETF | ETF | 0.49% | [0.44, 0.63] |
| Axis Gold ETF | ETF | 0.51% | [0.45, 1.37] |
| ABSL Gold Fund | FoF | 0.55% | [0.32, 0.94] |
| Kotak Gold Fund | FoF | 0.56% | [−0.19, 0.79] |
| ABSL Gold ETF | ETF | 0.56% | [0.40, 0.65] |
| Kotak Gold ETF | ETF | 0.57% | [0.49, 0.62] |
| HDFC Gold ETF | ETF | 0.59% | [0.50, 0.77] |
| Quantum Gold FoF | FoF | 0.64% | [0.49, 0.94] |
| ICICI Pru Gold FoF | FoF | 0.65% | [0.33, 0.81] |
| Quantum Gold ETF | ETF | 0.68% | [0.59, 0.71] |
| Nippon Gold BeES | ETF | 0.70% | [0.67, 0.76] |
| Nippon Gold Savings | FoF | 0.70% | [0.38, 0.87] |
| SBI Gold ETF | ETF | 0.72% | [0.63, 0.76] |

**Axis Gold ETF moved from 1.29% to 0.51%** — it was never a bad tracker, only a badly adjusted series.

## ⭐ The finding: the ranking is noise

| | Stage 3 (buggy) | **Stage 4 (corrected)** |
|---|--:|--:|
| Spread of medians across schemes | 1.00pp | **0.42pp** |
| Typical within-scheme IQR | 0.40pp | **0.43pp** |
| **Signal / noise** | 2.5× | ⚠ **1.0×** |

**Once the split artefacts are removed, the between-scheme spread equals the within-scheme dispersion.** The apparent ranking in Stages 2 and 3 was substantially an artefact of my own data handling.

> **No gold vehicle in this universe is distinguishable from another on tracking difference.** All sixteen sit inside a 0.42pp band whose measurement uncertainty is 0.43pp.

This is a category-defining outcome of the same kind the repo has produced twice before — MidCap's *"no fund has statistically significant alpha"* and MultiAsset's *"no allocation alpha anywhere."* Here: **no measurable tracking-fidelity edge anywhere.**

**Consequence for the study design:** `study_plan.md` weights Module 1 (tracking fidelity) at **35%**, on the reasoning that it is the whole performance question. It is — and it turns out to discriminate nothing. **Module 1 cannot separate these funds.** The decision must fall back on what remains measurable: SID-verified two-layer cost, AUM and liquidity, operational integrity, and access constraints.

## ⚠ And the benchmark is partly circular

Gross gold is defined as `mean(anchor ETF CAGR + its stated ER)`. That construction **forces each anchor ETF's tracking difference toward its own stated ER.** ICICI Gold ETF's leading 0.49% against a stated 0.50% ER is therefore **not independent evidence** — it is close to definitional.

Anchor disagreement across 19 windows: median 0.26pp, **max 2.56pp**.

> **The ER-anchored benchmark cannot be used to rank the anchor ETFs against each other.** A true external series (IBJA / MCX) is now a hard prerequisite, not an improvement. This supersedes the more optimistic assessment in [methodology.md](methodology.md) §1.

## Status of the two anomalies

| Scheme | Stage 3 | **Stage 4** | Verdict |
|---|--:|--:|---|
| **Axis Gold Fund** | −0.87% | **−0.08%** | ✅ **Resolved** — it was the ETF's split factor. Exclusion **withdrawn** |
| **SBI Gold Fund** | −0.43% | **−0.42%** | ❌ **Unresolved** |

**SBI is not a split problem** — its ETF's factor needed no correction. And SBI Gold ETF is internally coherent: TD 0.72% against a stated ER of 0.70%, tight IQR [0.63, 0.76]. A FoF sitting on top of that ETF cannot track at 0.30%. **SBI Gold Fund's series is not trustworthy; it remains excluded.**

## AUM — still not sourced

AMFI's classified-AUM endpoint returns 404 and its scheme-wise data sits behind a form, so this could not be pulled programmatically. **It requires a manual download and remains open.**

What is established: the six AMCs that capped gold inflows in June 2026 (HDFC, ICICI, Nippon, Tata, Axis, ABSL) are large by revealed preference; Kotak Gold ETF is ~₹14,115 Cr; category AUM ~₹1,84,571 Cr at end-May 2026.

---

## What the shortlist should now be

Since tracking fidelity does not discriminate, the three finalists cannot be justified on TD. Re-grounded on what is measurable:

| # | Scheme | Type | Grounds |
|---|---|:--:|---|
| **1** | **ICICI Pru Gold ETF** | ETF | Large, capped-for-scale, 15.9y record, tight IQR [0.44, 0.63], SID-verified 0.50% ER |
| **2** | **ICICI Pru Gold ETF FoF** | FoF | The **only** coherent FoF-layer measurement (+0.16%); settles Phase 0.1's wrapper question with zero AMC confound |
| **3** | **Kotak Gold ETF** | ETF | Tightest dispersion of all 16 [0.49, 0.62]; ~₹14,115 Cr; different AMC control |

**These are chosen for measurement reliability and scale, not for a tracking edge — because no tracking edge exists.** ABSL Gold ETF and HDFC Gold ETF are equally defensible on the same grounds.

**Nippon is the one robust negative.** Gold BeES median 0.70%, IQR [0.67, 0.76] — the tightest-measured result in the table, and at the bottom. Its 0.82% underlying ER stands. That conclusion has now survived four independent tests.

## Open before Phase 2

1. **A real IBJA/MCX benchmark** — now a hard prerequisite, given the circularity.
2. **AMFI scheme-wise AUM** — manual pull required.
3. **SBI Gold Fund's series** — unexplained.
4. **Re-scope Module 1.** At 35% weight it measures something that does not vary. Either re-weight toward Modules 2–4, or narrow Module 1 to the one thing that does separate schemes: dispersion/consistency rather than level.

*Stage 4 run August 2026. Corrected split estimator; 19 overlapping 3-year windows.*
