# Screening Results — Stage 1 → Stage 2 → Shortlist

> ⚠ **SUPERSEDED in part by [stage3_robustness.md](stage3_robustness.md) (Aug 2026).** This page uses a
> single 3-year window. Robustness testing showed that window carries ±0.3pp of endpoint noise — more than
> the signal in the middle of the table — and the ranking moved. **The shortlist below is superseded**;
> the §3b "impossible tracking" exclusions are **withdrawn** (they measured noise, not data corruption).
> Stage 1, the funnel and the Nippon conclusion all stand.

**Funnel: 44 → 20 → 8 → 3.** Window 2023-08-07 → 2026-08-07. Gross gold anchor **35.26%**.
Method and caveats: [methodology.md](methodology.md).

---

## Stage 1 — Hard filters

| Filter | Result |
|---|---|
| Track record ≥ 36 months | **44 → 20** (24 cut) |
| Underlying ETF AUM ≥ ₹300 Cr | ⚠ **not applied** — AUM absent from MFAPI |

**Cut for insufficient history (24):** HSBC ETF/FoF (4mo), Edelweiss FoF (5mo), Bandhan FoF (6mo), Wealth Co FoF (6mo), Wealth Co ETF (7mo), Bandhan ETF (8mo), Choice ETF (9mo), Angel One ETF/FoF (11mo), Baroda BNP FoF (11mo), Motilal ETF (12mo), Union FoF (17mo), 360 ONE ETF (17mo), Union ETF (18mo), Groww ETF/FoF (21mo), Mirae FoF (21mo), Zerodha FoF (21mo), Zerodha ETF (29mo), Tata FoF (30mo), Baroda BNP ETF (32mo), DSP FoF (33mo), Edelweiss ETF (33mo).

> The category is a launch wave — **24 of 44 schemes are under three years old.** Same structural pattern MultiAsset found, driven here by the post-2024 gold rally rather than a tax change.

## Stage 2 — Tracking fidelity, 3y

Median TD **0.55%** · 75th-pct monthly TE **~1.6%**

| Scheme | Type | TD 3y | TE (monthly) | FoF layer | Verdict |
|---|:--:|--:|--:|--:|---|
| UTI Gold FoF | FoF | −0.01% | 6.22% | — | ❌ **impossible TD** |
| **Quantum Gold FoF** | FoF | 0.31% | 3.52% | −0.23% | ❌ **impossible layer** |
| **ICICI Gold ETF** | ETF | **0.42%** | **1.50%** | — | ✅ **SHORTLIST** |
| SBI Gold Fund | FoF | 0.44% | 2.75% | −0.35% | ❌ **impossible layer** |
| Mirae Gold ETF | ETF | 0.50% | 1.50% | — | ✅ reserve |
| ABSL Gold Fund | FoF | 0.50% | 1.56% | −0.01% | ⚠ borderline |
| **ICICI Pru Gold FoF** | FoF | 0.51% | 1.53% | **+0.09%** | ✅ **SHORTLIST** |
| **ABSL Gold ETF** | ETF | 0.52% | **0.43%** | — | ✅ **SHORTLIST** |
| Kotak Gold ETF | ETF | 0.53% | 0.46% | — | ✅ reserve |
| Quantum Gold ETF | ETF | 0.54% | 2.03% | — | pass |
| Kotak Gold Fund | FoF | 0.57% | 4.70% | +0.04% | fail TE |
| DSP Gold ETF | ETF | 0.57% | 0.45% | — | fail TD |
| LIC MF Gold FoF | FoF | 0.59% | 4.13% | — | fail both |
| HDFC Gold ETF | ETF | 0.60% | 1.36% | — | fail TD |
| Axis Gold ETF | ETF | 0.60% | 1.61% | — | fail TD |
| Axis Gold Fund | FoF | 0.74% | 4.82% | +0.14% | fail both |
| **Nippon Gold BeES** | ETF | **0.76%** | 1.50% | — | fail TD |
| **Nippon Gold Savings** | FoF | **0.77%** | 1.18% | +0.01% | fail TD |
| SBI Gold ETF | ETF | 0.79% | 1.58% | — | fail TD |
| Invesco Gold FoF | FoF | 1.16% | 2.54% | — | fail TD |

### ⭐ The Nippon question, closed independently

**Nippon Gold BeES measures TD 0.76%; the FoF on top of it 0.77%.** Against the two disputed figures — 0.25% and 0.82% — this is decisive: **0.82% is right, 0.25% is not.** Phase 0.1b reached the same conclusion by a different route (relative ranking); this reaches it in absolute terms against an independently anchored benchmark. **Both Nippon vehicles fail Stage 2.**

---

## The three finalists

| # | Scheme | Type | TD | TE | Why |
|---|---|:--:|--:|--:|---|
| **1** | **ICICI Pru Gold ETF** | ETF | **0.42%** | 1.50% | Best tracker in the universe, 15.9y record |
| **2** | **ICICI Pru Gold ETF FoF** | FoF | 0.51% | 1.53% | Best *verifiable* FoF — layer +0.09%, exactly as a clean FoF should |
| **3** | **ABSL Gold ETF** | ETF | 0.52% | **0.43%** | Tightest tracking error of all 44; different AMC as control |

**Why this trio.** Finalists 1 and 2 are the **same AMC, same underlying metal, differing only in wrapper** — which isolates Phase 0.1's unresolved ETF-vs-FoF question with zero confounding. Finalist 3 is a different AMC with the tightest TE in the universe, testing whether ICICI's edge is real or house-specific.

**Reserves:** Mirae Gold ETF (TD 0.50%, but only 41 months) and Kotak Gold ETF (0.53%, TE 0.46%).

**Excluded on data integrity, not merit:** Quantum Gold FoF (0.31%), SBI Gold Fund (0.44%) and UTI Gold FoF (−0.01%) would have ranked 1st, 2nd and 4th. **All three report physically impossible tracking.** If the artefact is resolved and their numbers survive, Quantum Gold FoF in particular would displace a finalist — this is the single most consequential open item in the screen.

---

## ⚠ Before this shortlist is acted on

1. **Apply the AUM floor** from AMFI/AMC data — not yet done, and it could remove a finalist.
2. **Resolve the three impossible-tracking schemes** — see above.
3. **Replace the estimated benchmark** with a real IBJA or MCX series; the 35.26% anchor rests on four aggregator-sourced ERs.
4. **One regime only.** Three years, all of it a gold bull market. Longer windows need the split adjustment validated first.
5. **ABSL Gold Fund** sits at a borderline −0.01% layer — resolve before treating it as a reserve.

*Screen run August 9 2026. Funnel 44 → 20 → 8 → 3.*
