# Screening Methodology — Gold Vehicles

**Universe:** 44 schemes (22 gold FoFs + 22 gold ETFs), Direct/Growth, all pulled from AMFI via MFAPI.
Silver, combined gold+silver FoFs and SGBs are out of scope per [Phase 0](../phase0_wrapper_and_asset.md).

---

## 1. The benchmark problem, and how it was solved

No free IBJA or MCX domestic gold series is available, and `study_plan.md` flagged this as the screen's main data risk. Two-step workaround, used throughout:

**Step 1 — a robust market proxy.** Cross-sectional **median daily return** across all Stage-1 survivors. Using the median rather than the mean makes it immune to any single scheme's data artefacts.

**Step 2 — an absolute anchor.** The proxy gives *relative* drag only. To convert to absolute tracking difference, gross gold is triangulated from ETFs whose expense ratios are independently sourced: `gross ≈ ETF CAGR + its ER`.

| Anchor ETF | 3y CAGR + ER | Implied gross gold |
|---|---|--:|
| ICICI Gold ETF | + 0.50% | 35.34% |
| Kotak Gold ETF | + 0.55% | 35.29% |
| HDFC Gold ETF | + 0.59% | 35.25% |
| SBI Gold ETF | + 0.70% | 35.17% |
| **Mean** | | **35.26%** |

**Spread across four independent anchors: 0.17pp.** That tightness is the method's validation — four different AMCs, four independently-sourced ERs, converging on one gross-gold figure. **All tracking differences in this screen are measured against 35.26%.**

> ⚠ Still an estimate. The four ERs are aggregator-sourced. A real IBJA/MCX series would supersede this and is required before Module 1.

## 2. Split adjustment

Ten schemes carried unit splits or consolidations that corrupt raw NAV series (e.g. Nippon Gold BeES 2019-12-23 at 0.01×, Kotak Gold ETF twice). A detector flags any daily ratio outside 0.6–1.6 and rescales the series forward. **Without this the 5-year window returns −50% CAGRs.** All splits found fall outside the 3-year window, so they do not affect the headline numbers — but they must be handled before any longer window is used.

## 3. ⚠ Two measurement artefacts found — and what they change

### 3a. Daily tracking error systematically penalises FoFs

| Return frequency | FoF median TE | ETF median TE |
|---|--:|--:|
| **Daily** | **6.60%** | 2.23% |
| **Monthly** | **3.13%** | 1.50% |

A FoF's NAV is struck against its underlying ETF with a reporting lag, producing large but **mean-reverting** daily differences. This is a measurement artefact, not worse tracking. On monthly returns the best FoFs (Nippon 1.18%, ICICI 1.53%, ABSL 1.56%) are indistinguishable from ETFs.

> **Rule adopted: tracking error is measured on MONTHLY returns.** A daily-TE filter would have wrongly eliminated FoFs as a class.

### 3b. Three schemes report impossible tracking

A FoF cannot outperform its own underlying ETF, and nothing can outperform gross gold.

| Scheme | Reported | Why impossible |
|---|--:|---|
| UTI Gold FoF | TD **−0.01%** | beats gross gold |
| SBI Gold Fund | FoF layer **−0.35%** | beats its own ETF |
| Quantum Gold FoF | FoF layer **−0.23%** | beats its own ETF |

**All three would otherwise rank in the top four.** Cause unresolved — candidates are stale NAV reporting, the FoF holding instruments beyond its named ETF, or an AMFI feed error. Split contamination is ruled out: every detected split predates the 3-year window.

> **Rule adopted: a FoF must pass a consistency check against its own underlying ETF (implied layer ≥ −0.05%) to be shortlisted.** Schemes failing it are excluded pending investigation, not ranked.

**Consistency results:** ✅ ICICI (+0.09%), Axis (+0.14%), Kotak (+0.04%), Nippon (+0.01%), ABSL (−0.01%, borderline) · ❌ SBI (−0.35%), Quantum (−0.23%) · no pair available: UTI, LIC, Invesco.

## 4. Filters applied

**Stage 1 — hard:** track record ≥ 36 months. ⚠ The **AUM floor (underlying ETF ≥ ₹300 Cr) was NOT applied** — AUM is not in MFAPI and must come from AMFI/AMC data before the shortlist is final.

**Stage 2 — tracking fidelity:** 3-year absolute TD better than universe median · monthly TE ≤ 75th percentile · FoF consistency check (§3b).

**Not used as filters:** returns of any period (framing fact 2 — ranking these on CAGR ranks the gold price), FoF-level AUM, stated expense ratios (Phase 0.1b showed they do not predict realised drag).

---

*Method: MFAPI NAV self-computation, split-adjusted, median-proxy benchmark anchored by four-ETF ER triangulation. Window 2023-08-07 → 2026-08-07. Aggregators used for universe discovery and the four anchor ERs only.*
