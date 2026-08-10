# Stage 3 — Robustness, and the Revised Shortlist

> ⚠ **RANKINGS SUPERSEDED by [stage4_corrected.md](stage4_corrected.md).** The split adjustment used here
> was buggy — it divided by the raw NAV ratio on split days, baking that day's gold move into the factor
> (ICICI's was off by 8.20%, Axis's by 2.70%). Correcting it moved Axis Gold ETF from 1.29% to 0.51% and
> **collapsed signal/noise from 2.5× to 1.0×**. The endpoint-noise finding and the withdrawal of the §3b
> consistency check both stand; the ranking table does not.

**This supersedes the shortlist in [stage1_and_stage2.md](stage1_and_stage2.md).** That screen used a single 3-year window. Testing it showed the window carries more noise than signal in places, and the ranking moved.

---

## Fix #2 — The "impossible tracking" was noise, and my integrity check was wrong

**Endpoint-jitter test:** implied FoF layer, 3-year window shifted ±20 days.

| AMC | −20d | −10d | 0d | +10d | +20d | **Spread** |
|---|--:|--:|--:|--:|--:|--:|
| Quantum | −0.15% | +0.09% | −0.23% | −0.01% | −0.10% | 0.31pp |
| Nippon | +0.32% | +0.25% | +0.01% | +0.02% | −0.13% | **0.45pp** |
| Kotak | +0.35% | +0.26% | +0.04% | −0.00% | −0.02% | 0.37pp |
| SBI | −0.01% | −0.02% | −0.35% | −0.05% | −0.25% | 0.34pp |
| ICICI | +0.25% | +0.26% | +0.09% | +0.10% | +0.00% | 0.26pp |

**Moving the window by twenty days swings the measurement by 0.26–0.45pp — larger than the 0.05–0.25% signal being measured.** Every pair shows it, including the ones the earlier screen called "clean": Nippon swings +0.32% to −0.13%, and on a pre-crash window ICICI itself goes negative (−0.14%).

**Cause:** FoF NAVs are struck against the underlying ETF with a reporting lag. In a ~19%-volatility asset a one-day lag is ~1% of NAV, which annualises to ±0.3pp over three years. The largest single-day ratio jumps cluster on **2026-01-21/22/30 across nearly every pair** — the Q1-2026 gold crash, not a fund-specific defect.

> ⚠ **The `methodology.md` §3b consistency check (FoF layer ≥ −0.05%) is WITHDRAWN.** It classified schemes on noise. **Quantum Gold FoF and SBI Gold Fund were excluded on a test that does not hold.**

**And the answer to "would Quantum displace a finalist?" is no — for a different reason.** Its single-window 0.31% was noise; its rolling median is **0.63%**, mid-pack.

## Fix #4 — Nineteen overlapping windows, not one

Rolling 3-year windows stepped semi-annually, proxy built from the 15 long-history schemes, spanning **2014-06 → 2026-08** — so gold bear phases are now included.

| Scheme | Type | **Median TD** | IQR | min..max |
|---|:--:|--:|---|---|
| SBI Gold Fund | FoF | 0.29% | [0.23, 0.60] | [−0.58, 1.28] |
| Axis Gold Fund | FoF | 0.42% | [0.22, 0.78] | [−0.55, 2.34] |
| Invesco Gold FoF | FoF | 0.48% | [0.30, 0.97] | [−2.43, 1.57] |
| **ICICI Gold ETF** | ETF | **0.49%** | **[0.39, 0.57]** | [−1.05, 0.91] |
| ABSL Gold Fund | FoF | 0.55% | [0.30, 0.88] | [−0.76, 2.03] |
| Kotak Gold Fund | FoF | 0.55% | [−0.21, 0.78] | [−0.84, 1.12] |
| **ABSL Gold ETF** | ETF | 0.56% | [0.23, 0.65] | [0.13, 1.09] |
| **Kotak Gold ETF** | ETF | 0.57% | **[0.51, 0.67]** | [0.29, 1.00] |
| HDFC Gold ETF | ETF | 0.59% | [0.50, 0.80] | [0.36, 1.32] |
| Quantum Gold ETF | ETF | 0.63% | [0.38, 0.71] | [0.22, 1.37] |
| Quantum Gold FoF | FoF | 0.63% | [0.49, 0.87] | [−0.34, 1.60] |
| Nippon Gold Savings | FoF | 0.64% | [0.38, 0.87] | [−0.38, 1.45] |
| **ICICI Pru Gold FoF** | FoF | 0.64% | [0.31, 0.75] | [−0.67, 1.46] |
| SBI Gold ETF | ETF | 0.72% | [0.59, 0.76] | [0.29, 1.06] |
| Nippon Gold BeES | ETF | 0.72% | [0.67, 0.78] | [−1.10, 1.61] |
| Axis Gold ETF | ETF | 1.29% | [0.50, 1.54] | [0.23, 1.95] |

### ⚠ Signal-to-noise is only 2.5×

Spread of medians across schemes **1.00pp**; typical within-scheme IQR **0.40pp**.

> **Schemes within ~0.4pp of each other are not distinguishable.** The bottom of the table (Axis ETF 1.29%, Nippon 0.72%) is genuinely worse than the top (ICICI 0.49%). The middle is a cluster, not a ranking.

**ETFs measure far more cleanly than FoFs** — compare Kotak ETF's IQR [0.51, 0.67] against Kotak FoF's [−0.21, 0.78]. The FoF lag noise is real and it is not removable by choosing a better window.

### The layer test, done properly

FoF median TD − its own ETF's median TD:

| AMC | Implied layer | Verdict |
|---|--:|---|
| **ICICI** | **+0.15%** | ✅ the only coherent measurement |
| Kotak | −0.02% | ~zero |
| ABSL | −0.01% | ~zero |
| Quantum | 0.00% | ~zero |
| Nippon | −0.08% | ~zero |
| SBI | −0.43% | ❌ still impossible |
| Axis | −0.87% | ❌ still impossible |

**ICICI is the only pair whose numbers are internally consistent across 19 windows.** That is a point in its favour independent of its ranking.

## Fix #3 — The benchmark is weaker than the single window suggested

Across the same 19 windows, the four-ETF anchor disagreement is **median 0.32pp, max 2.28pp** — against the 0.17pp seen in the single 3-year window.

> **Absolute tracking-difference levels are soft to roughly ±0.3pp. Only relative rankings should be used.** A real IBJA or MCX series remains required before Module 1, and this is now a harder requirement than the original screen implied.

## Fix #1 — AUM, and a constraint the screen had missed

Individual ETF AUM is still not sourced from AMFI. But it is effectively settled for the finalists by a stronger signal:

**⚠ Six AMCs restricted gold-scheme subscriptions from early June 2026** — HDFC, ICICI Prudential, Nippon India, Tata, Axis and Aditya Birla Sun Life. HDFC capped its Gold **FoF** at ₹10 lakh per PAN per month (from 5 Jun) and its Gold **ETF** at ₹25 Cr direct subscriptions (from 8 Jun); ICICI and Tata applied the same ₹25 Cr ETF threshold. Category AUM had grown **~195% YoY to ₹1,84,571 Cr by end-May 2026**, and gold import duty rose from 6% to 15%.

**You do not cap inflows into a small fund** — appearing on that list is itself evidence of scale, so ICICI and ABSL clear a ₹300 Cr floor comfortably. Kotak Gold ETF is ~₹14,115 Cr.

**Does it bind at ₹7,500–10,000/month? No.** The caps target ₹25 Cr institutional subscriptions and ₹10 lakh/month FoF lump sums; exchange buying and existing SIPs are explicitly unaffected.

> **New review trigger:** this is the gold analogue of the International sleeve's SEBI cap. It does not bind today. **If restrictions tighten toward retail SIP levels, the sleeve's access assumption breaks** — re-check at each annual review.

---

## The revised shortlist

| # | Scheme | Type | Median TD | IQR | Why |
|---|---|:--:|--:|---|---|
| **1** | **ICICI Pru Gold ETF** | ETF | **0.49%** | [0.39, 0.57] | Best median of 16, tight, **and the only pair whose FoF layer is coherent** |
| **2** | **ICICI Pru Gold ETF FoF** | FoF | 0.64% | [0.31, 0.75] | Carries the wrapper question against finalist 1 with the only credible layer measurement (+0.15%) |
| **3** | **Kotak Gold ETF** | ETF | 0.57% | **[0.51, 0.67]** | Tightest dispersion of all 16; different AMC as control |

**Changes from the Stage-2 shortlist:** ABSL Gold ETF (median 0.56%, IQR [0.23, 0.65]) is a **statistical tie with Kotak** — Kotak is taken on measurement reliability alone, and ABSL remains a co-equal reserve. ICICI Pru Gold FoF fell from 0.51% to 0.64% and now ranks 13th of 16 on median; **it is retained for its structural role, not its ranking** — the study needs one FoF to settle Phase 0.1, and it is the only FoF measuring coherently.

**Nippon confirmed again:** Gold BeES median **0.72%**, 15th of 16, IQR [0.67, 0.78] — the tightest-measured *bad* result in the table. The 0.82% figure stands; 0.25% is dead.

## What is still open

1. **Exact AUM from AMFI** — inferred, not sourced.
2. **A real gold benchmark** — now the binding constraint on absolute numbers.
3. **SBI Gold Fund and Axis Gold Fund** still report impossible layers (−0.43%, −0.87%) across 19 windows, so this is not pure endpoint noise for those two. Unexplained; both excluded.
4. **Signal/noise 2.5×** means Module 1 must not over-read small TD differences.

*Stage 3 run August 2026. 19 overlapping 3-year windows, 2014-06 → 2026-08.*
