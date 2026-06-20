# Quant Small Cap Fund — Module Research Plan

**Context:** ₹20,000/month SIP, 10+ year horizon (aggressive satellite alongside the FlexiCap core).
**Framework:** Same 6-module weighted scoring used for DSP, Invesco, Bandhan, BOI, HSBC (Small Cap study).
**Data method:** Primary = **MFAPI NAV history independently computed** (Direct Growth, scheme 120828, 3,307 points, Jan 2013 → Jun 2026), cross-verified against AdvisorKhoj / VRO / Tickertape. The Tickertape screening CSV is treated as a *secondary* source after it was found to contain errors for this fund (ER and a 2015 NAV spike — see below).

> **🔁 Plan revised 2026-06-17 after Modules 1 & 2 were researched.** The original plan (2026-06-16) was written off the Tickertape screener and assumed Quant Small Cap was a "genuine 13-year, 2018-tested, no-inception-bias" fund failing on ER + AUM. **Live NAV data overturned both assumptions:** (a) it is a **two-era fund** — a near-dead Escorts legacy (2013–2019) glued to an explosive VLRT era (2020+) — so the "long record" is largely an illusion; and (b) the Direct ER is **~0.59–0.69%** (VRO/AdvisorKhoj), not 1.13%, so it fails **only the AUM cap**, not ER. Sections below are updated; M1/M2 are now complete.

---

## ⚠️ Screening Status — READ FIRST

**Quant Small Cap is NOT in the 8-fund shortlist. On corrected data it was eliminated in Stage 1 on ONE hard filter — the AUM cap.**

| Filter | Threshold | Screener said | Corrected | Result |
|--------|-----------|---------------|-----------|--------|
| Expense Ratio | ≤ 1.0% (Direct) | 1.13% ✗ | **~0.59–0.69%** (VRO/AdvisorKhoj) | ✅ **Passes** — screener ER was wrong |
| AUM maximum | ≤ ₹30,000 Cr | ₹30,374 Cr ✗ | **₹31,774–31,913 Cr** (growing) | ✗ **Fails — the sole genuine disqualifier** |
| Fund age | ≥ 60 months | 161 months | 161 months (Jan-2013 direct inception) | ✅ Passes |
| Sharpe | ≥ 0 | 0.149 | 0.81 (computed, 3Y) | ✅ Passes |
| AUM minimum | ≥ ₹500 Cr | ₹30,374 Cr | ₹31,900 Cr | ✅ Passes |

**Why study an eliminated fund at all?** Three reasons — but note reason #1 has been *inverted* by the data:

1. **It is the cautionary "two-era" case.** The original plan called it a "genuine 13-year, 2018-tested, no-inception-bias" fund. **The NAV data says otherwise:** 2013–2019 was a near-dead Escorts legacy scheme (CAGR +2.62%; sub-2% annual volatility in 2014/2016/2017 — it wasn't really holding equities), and the explosive record belongs entirely to the **VLRT era (2020+), which effectively begins at the COVID floor.** The "13-year record" is largely an illusion. This makes Quant the study's clearest lesson in how a blended long-horizon CAGR can mask a regime change — *more* instructive than the original (false) premise.
2. **It posts the study's strongest raw VLRT-era numbers** — 5Y CAGR 21.01% (#3 of 9), the highest 10Y SIP outcome (₹90.3L), positive 5Y alpha (+5.83%), good computed Sharpe (0.81) and IR (+0.37/+0.88). It would have cleared Stage 2 (5Y > 19.15% median; 3Y vs sub-category 1.356×). The study tests whether that VLRT record overrides the **scale (₹31,900 Cr) and governance** concerns — ER is *not* the obstacle the screen implied.
3. **The AMC is already studied.** Quant Money Managers was deep-studied in the FlexiCap project (Quant Flexi Cap = **2.49/5**, AMC module **1.25/5**). The governance findings — front-running probe on CIO Sandeep Tandon (now a filed consent settlement), VLRT black-box, no succession — **carry straight over** and likely cap this study's ceiling regardless of returns.

**Framing for the verdict:** A "confirm or overturn the elimination" study. The hypothesis: *do Quant's strong VLRT-era returns earn it a place the screen denied — or do the era-contaminated record, the AUM scale, and (above all) the unverifiable black-box / front-running governance shadow confirm the elimination?* (M1 ~3.4, M2 ~3.1 so far suggest the latter.)

---

## Carry-Forward From the FlexiCap Quant Study (Do Not Re-Derive)

These were established in `Mutual Fund/FlexiCap/funds/quant/` and apply to the same AMC/manager. Update only with small-cap-specific data; do not re-research from scratch.

| Finding | FlexiCap study value | Carry-forward action for Small Cap |
|---------|---------------------|-----------------------------------|
| **AMC** | Quant Money Managers Ltd; private, Tandon ~majority owner | Reuse — same AMC. M6 starts from the FlexiCap AMC findings. |
| **SEBI front-running probe on Tandon** | "Active, unresolved" as of May 2026 | **UPDATE:** Tandon (with HNI Sumana Paruchuri) has **filed for a consent settlement, which SEBI is likely to accept** (raid Jun-2024; ₹70–80 Cr front-running found). Settlement ≠ exoneration — still the dominant M5/M6 flag. |
| **Data-deletion allegation (day before raid)** | Alleged evidence obstruction | Carry forward as governance flag. |
| **VLRT model** | Proprietary, undisclosed "black box" (Valuation, Liquidity, Risk, Time) | Same model drives Small Cap. M3/M5 must address verifiability. |
| **Key-man risk** | "Extreme" — Tandon is MD + CEO + CIO + owner; no succession | Same risk; confirm who the *named* Small Cap PM is (likely team under Tandon). |
| **Style: very high turnover, momentum/liquidity rotation** | 115–296% turnover; leveraged cash (−1.99%) | **Amplified concern in small cap** — turnover in illiquid names = large hidden impact cost. |
| **Concentration** | Top-10 71.4%; 24.56% Adani Group | Check whether Small Cap shows comparable single-group/top-10 concentration. |
| **Regulatory record (AMC, 3yr)** | Active SEBI probe; AMC module 1.25/5 | Lowest AMC score in either study; small-cap study inherits this floor. |
| **Investor communication** | None / minimal; no letters | Carry forward. |

> **Net effect:** Modules 5 (Manager, 15%) and 6 (AMC, 5%) are largely pre-determined and low (~2.0 / ~1.25–1.5), inherited from the FlexiCap sibling. The open question is whether Modules 1–4 (85% of weight) can lift the overall above the FlexiCap sibling's 2.49. **So far they partly do:** the Small-Cap M1 (~3.4) and M2 (~3.1) both score *higher* than the FlexiCap versions (3.50 / 2.00) — the SC fund has a shallower drawdown (−46.71% vs −54.6%) and positive IR. But the same governance ceiling (M5/M6) and the AUM-scale drag (M4) will pull the weighted total back toward the low-3s / high-2s. Net: better than the FlexiCap sibling, still not shortlist-grade.

---

## Verified Facts (MFAPI-computed + cross-source, as of 15-Jun-2026)

*Corrected baseline — replaces the screener figures, several of which were wrong.*

| Metric | Quant Small Cap | Source | Notes |
|--------|----------------|--------|-------|
| MFAPI scheme | **120828** (Direct G) / 100177 (Reg G) | MFAPI | 3,307 NAV points |
| Direct inception | **07-Jan-2013** (NAV ₹34.11, Escorts-era legacy level) | MFAPI | Not a fresh ₹10 launch |
| AUM (Direct) | **₹31,774–31,913 Cr** | VRO / AdvisorKhoj | **Over the ₹30K cap, growing — the sole genuine disqualifier** |
| ER (Direct) | **~0.59% (VRO) / 0.69% (AdvisorKhoj)** | VRO / AdvisorKhoj | ⚠️ **Screener's 1.13% was wrong** — resolve canonical figure in M4 |
| 5Y CAGR | **21.01%** | MFAPI (AdvisorKhoj 20.99% ✅) | #3 of 9; VLRT-era |
| 3Y CAGR | **20.68%** | MFAPI (AdvisorKhoj 20.66% ✅) | — |
| 10Y CAGR | **20.52%** | MFAPI (AdvisorKhoj 20.51% ✅) | ⚠️ Blended (dead era + sprint), SI alpha only +1.82%/yr |
| **Escorts-era CAGR (2013–19)** | **+2.62%** | MFAPI | 7 dead years; ~7.8% vol (non-equity-like) |
| **VLRT-era CAGR (2020+)** | **+36.04%** | MFAPI | The real, explosive record |
| Sharpe (computed 3Y) | **0.81** | MFAPI | Screener's 0.149 is a methodology artifact — discard |
| Sortino (computed 3Y) | **1.22** | MFAPI | — |
| Volatility (5Y / VLRT-era) | **19.34% / 19.77%** | MFAPI | **Highest in the study** |
| Max Drawdown | **−46.71%** (peak 19-Dec-2018 → trough 24-Mar-2020) | MFAPI (clean) | ✅ Matches screener once the 27-May-2015 NAV glitch is removed; transition-era, not VLRT |
| Beta / R² / IR (5Y) | **0.97 / 87.7 / +0.875** | MFAPI vs index fund | Positive Jensen alpha (+6.29%) — the anti-HSBC |
| % from ATH | **−2.74%** (peak ₹306.52, 27-Sep-2024) | MFAPI | Mild; 626 days since ATH |
| Returns vs sub-category (3Y) | 1.356× | Tickertape | Clears Stage-2 |

> ⚠️ **Data-integrity note:** the Tickertape screener mis-stated this fund's ER (1.13% vs true ~0.6%), and the raw MFAPI series contains a one-day NAV spike on **27-May-2015** (₹59.21 between ₹42.65 and ₹42.67) that must be removed before computing drawdown/volatility. All figures above use the cleaned series. **Still to pull at write time:** portfolio PE, smallcap/mid/large %, top-10 concentration, # stocks, turnover, cash/debt %, ER Regular, exit load, per-manager tenure.

---

## Module 1: Returns Consistency (25%) — ✅ COMPLETE (provisional ~3.4/5)

> **Written: [module1_returns.md](module1_returns.md).** Key findings: two-era fund (Escorts +2.62% / VLRT +36.04%); SI alpha only +1.82%/yr exposes the dead era; 5Y +5.83% / 10Y +6.57% alpha genuine; worst single relative year **2019 −23.24%** (−14.97% alpha, worst in either study); rolling 5Y **6.5% negative** (worst in study); 10Y SIP ₹90.3L (study-best but era-flattered); return-trust shadow from VLRT black-box. **New sections added:** Two-Era Fund · Is the 13-Year Record Real? · The 2019 Collapse · Misleading Capture Ratios · Returns vs Trustworthiness · 135× AUM Explosion · vs FlexiCap sibling.

### Raw Data Table (Tickertape, May 21 2026 + cross-verify)
Collect: CAGR 3Y/5Y/10Y, rolling 3Y avg, alpha (vs Nifty SmallCap 250 TRI), absolute 1Y/6M/3M, 3Y benchmark beat.

### Cross-Source Verification Table
Verify every return metric across: Tickertape | ValueResearch | Groww | IndMoney | AdvisorKhoj. Document the canonical figure and flag anomalies. **Reject Tickertape's Sharpe/Sortino if they look like methodology artefacts (as seen for Bandhan/Invesco — TT showed 0.325/0.302 vs INDmoney ~1.0+).**

### CAGR vs Benchmark Chart (Mermaid xychart-beta)
Bar = Quant SC | Line = Nifty SmallCap 250 TRI. Periods 1Y/3Y/5Y/10Y.

### The 10Y / 2018 Advantage — Quant's Strongest Card
Unlike the shortlist's inception-biased funds, Quant has a **full 13.4-year, 2018-inclusive record.** Build the case explicitly:
- 10Y CAGR (genuine, cycle-tested) vs the shortlist's 10Y funds (DSP ~19.26%, HSBC 19.57%, Sundaram 16.10%, Union 17.40%)
- **Calendar-year table 2017→2026 YTD**, with the key small-cap stress years called out:
  - **2018** (IL&FS crash, Nifty SC250 −45%) — *the* test; how deep did Quant fall, did it recover faster than peers?
  - 2020 (COVID), 2021 (bull), 2022 (rate hikes), 2023 (+47% SC rally), 2025 (−15-20% correction)
- Inception-adjustment: **none needed** — note this is a genuine edge vs Bandhan/Invesco.

### Rolling 3Y Average vs Point-to-Point
Quant's high volatility should widen the gap. Explain.

### Returns vs Peers (Sub-category Multiples) — 10Y/5Y/3Y/1Y
Values > 1.0 = outperforming category. Baseline 3Y = 1.356×.

### Returns vs Shortlist Chart
Position Quant SC's 5Y (21.64%) and 10Y CAGR against the 8 shortlisted funds — show it would rank ~#3 on 5Y, top-tier on genuine 10Y.

### "Why Is the 1Y Return What It Is?" Section
Attribute to: VLRT momentum rotation, sector bets, AUM-driven deployment drag at ₹30K Cr.

### Capture Ratios (Web research)
Upside capture, downside capture, asymmetry. **Key question:** does VLRT momentum give asymmetric capture, or symmetric high-beta (high up + high down)? Compare to BOI (best IR 0.938) and HSBC (deteriorated to 165% downside in 2025).

### SIP XIRR vs Lumpsum CAGR (3Y/5Y)
High volatility → more rupee-cost-averaging benefit. Compute SIP XIRR through the 2025 slump (BOI 16.76%, HSBC 8.71%, DSP 12.78% are the references).

### Manager Attribution
**Critical:** how much of the 13Y record was built under the current VLRT regime vs the pre-2008 rebuild? Quant Money Managers took over the erstwhile Escorts MF in 2018 — verify when *this fund's* VLRT era actually began, and whether the 10Y CAGR predates the current process.

### Module 1 Scorecard (small-cap sub-dimensions)
| Sub-dimension | Weight | Score (1–5) | Reasoning |
- 10Y CAGR (≥19%=5) · 5Y CAGR vs median (≥22%=5, 20-22%=4) · Rolling 3Y avg · **2018 performance (Critical)** · Inception bias (modifier — favourable here) · Consistency (worst year) · Alpha vs SC250 TRI · **Module 1 Overall**

---

## Module 2: Risk Profile (20%) — ✅ COMPLETE (provisional ~3.1/5)

> **Written: [module2_risk.md](module2_risk.md).** Findings (computed, clean series): Max DD **−46.71%** (peak 19-Dec-2018 → trough 24-Mar-2020, ~1.6y underwater) — *transition-era, not VLRT*; VLRT-era worst is only ~−25% (2022, 2024-25), bear-untested. **Highest volatility in the study** (5Y 19.34% / VLRT-era 19.77%); two-era split (Escorts 7.81% vol vs VLRT 19.77%). Risk-adjusted metrics genuinely good: Sharpe 0.81, Sortino 1.22, Calmar 0.45, Beta 0.89–0.97, R² 88–90, **Jensen alpha +3.78%/+6.29%, IR +0.37/+0.88** (anti-HSBC). −2.74% from ATH. **Unique events:** the 27-May-2015 data-glitch catch (fixes −51.6%→−46.71%, matches screener); the **Jun-2024 redemption shock** (₹1,400 Cr pulled in 3 days on the SEBI news — only real forced-outflow event in either study). **New sections to add:** Data-Glitch/Max-DD Reconciliation · Two-Era Risk Personality · Whose Drawdown Is It? · Jun-2024 Redemption Shock · Can You Trust the Risk Metrics? · Active Management That Works (Beta/R²/IR).

### Raw Data Table
Pre-filled: Sharpe 0.149, Max DD 46.71%. Collect: volatility (vs category 16%), Sortino, beta, downside capture, recovery time, R².

### Volatility & Beta — Is Quant the Highest-Risk SC Fund?
The FlexiCap sibling had the highest volatility (16%) and a leveraged cash position. Test whether the Small Cap fund is similarly aggressive. Chart volatility vs the 8 peers + category line (16%).

### Max Drawdown — 46.71%, and the 2018 Question
- Identify the dates of the 46.71% max DD (2018? COVID? 2022?).
- **Recovery time** — VLRT claims to rotate to cash/defensives ahead of crashes; did it actually shorten Quant's recovery, or was recovery slow (the FlexiCap sibling took 27 months, Jan-18→Apr-20)?
- Compare to the small-cap "alarming > 55%" threshold and to HSBC (52.45%), Sundaram (57.06%), BOI (32.37%).

### Downside Capture — THE Critical Small-Cap Metric
< 85% = excellent, > 105% = poor. Does VLRT's "Risk + Time" liquidity-rotation actually protect on the downside, or is the marketing untested? Quantify across 2018, 2020, 2022, 2025.

### Sharpe / Sortino
Sharpe 0.149 is low for a fund with 21%+ CAGR — meaning **high volatility is the denominator problem.** Reconcile TT vs INDmoney figures. Is the return quality genuinely poor or a volatility artefact?

### Redemption Risk at ₹30,374 Cr
Largest of any fund being studied. In a sustained-outflow bear, forced selling of illiquid small caps at a ₹30K Cr scale is acute. Document exit load (FlexiCap sibling = 0% — a *negative* for SC, since no redemption-deterrent buffer) and cash holding.

### Module 2 Scorecard
| Sub-dimension | Weight | Score | Reasoning |
- Max DD (inception-adjusted) · Volatility vs category · Sharpe · Sortino · **Downside capture (Critical)** · Recovery time · **2018 drawdown (Critical)** · Redemption risk (AUM × exit load) · **Module 2 Overall**

---

## Module 3: Portfolio DNA (15%)

### Raw Data Table
Collect: smallcap %, midcap %, largecap %, cash %, debt %, top-3/5/10 concentration, number of stocks, portfolio PE vs category (31.60), portfolio turnover, % away from ATH.

### Small-Cap Depth & Mandate Honour
- Smallcap % (70%+=5, 65-70%=4, <65%=flag). At ₹30,374 Cr, can Quant genuinely deploy into the 350th–600th rank, or is it forced toward the 250th–350th "large small-caps" (the Nippon problem)?
- Number of stocks & top-10 concentration. **Test the carry-forward concern:** FlexiCap Quant ran 71.4% top-10 with 24.56% Adani. Does Small Cap show comparable single-group/top-10 concentration? Flag any group exposure > 20%.

### Portfolio Turnover — The Hidden-Cost Bomb
FlexiCap Quant ran **115–296% turnover.** In illiquid small caps this is the single biggest hidden cost. Estimate market-impact cost (turnover × illiquidity premium) and fold into the M4 "true all-in cost." A fund turning over its book 2-3× a year in ₹500–2,000 Cr stocks at ₹30K Cr AUM is structurally expensive beyond the 1.13% ER.

### Cash & Liquidity Management
VLRT uses tactical cash/leverage. Document current cash (and whether leveraged/negative as in FlexiCap). Is cash a dry-powder edge or forced AUM-absorption?

### Sector & Valuation
Largest sector (flag if > 25%); portfolio PE vs category 31.60; % from ATH.

### Module 3 Scorecard
| Sub-dimension | Weight | Score | Reasoning |
- Genuine SC depth · Smallcap % · Mid-cap quality · Cash/liquidity · **Portfolio turnover** · Top-10 concentration · # stocks · Sector diversification · PE vs category · **Module 3 Overall**

---

## Module 4: Cost & AUM Impact (20%)

> **⚠️ Reframed:** the original plan called M4 a "double disqualifier (ER + AUM)." With the **corrected Direct ER (~0.59–0.69%, not 1.13%)**, ER is actually **competitive** (cheaper than HSBC 0.73%, DSP 0.64%; near Invesco). So M4's negative is **AUM scale alone**, plus turnover-driven true-cost — not headline ER.

### Raw Data Table
- ER Direct: **~0.59% (VRO) / 0.69% (AdvisorKhoj)** — resolve the canonical figure (and explain the screener's wrong 1.13%). ER Regular: collect. Direct–Regular gap.
- Exit load (FlexiCap sibling = 0% — verify for SC). AUM: **₹31,774–31,913 Cr**. Monthly SIP inflow estimate. Turnover (from M3). Min SIP.

### The ER Anomaly — Resolve the 1.13% vs 0.59% Discrepancy
- Document the five-source ER spread (mirror of the Invesco ER anomaly); establish the AMFI-canonical Direct ER.
- Chart ER vs the 8 shortlisted funds — Quant lands **mid-pack/cheap**, not at the expensive end. This *removes* the cost objection the screen implied.
- 10Y ₹20K SIP ER-drag calc vs Bandhan/DSP/HSBC at the corrected rate.

### True All-In Cost — Where the Real Cost Hides
- **True all-in = ER (~0.6%) + turnover impact.** FlexiCap Quant ran **115–296% turnover**; at ₹31,900 Cr in illiquid small caps this could add 0.3–0.6%, potentially pushing true all-in toward/above HSBC's 0.87% *despite* the low headline ER. Get the SC turnover figure (M3) and quantify.

### AUM Scale — The Sole Structural Disqualifier
- **₹31,900 Cr is over the ₹30,000 Cr cap and growing** (from ₹235 Cr at the 2018 takeover = ~135× in 8 years). Compute monthly forced SC deployment (~1% AUM × 65%) and assess whether VLRT's high-turnover rotation can execute at this scale without market impact (the Nippon problem).
- AUM sweet-spot scoring: ₹20,000–30,000 Cr = "constrained" (score 2); Quant is just over the top of that band.
- Tie to M1's "135× AUM Explosion vs Forward Returns" and M2's "Jun-2024 redemption shock" (₹1,400 Cr in 3 days).

### Direct vs Regular Plan
10Y corpus gap; note exit-load behaviour (confirm SC exit load; if 0% like FlexiCap, mild cost-positive but a redemption-stability negative per M2).

### Module 4 Scorecard
| Sub-dimension | Weight | Score | Reasoning |
- Expense ratio (corrected ~0.6% → ~4/5, *not* 1) · AUM sweet spot (Critical; ₹20–30K+ = 2) · Monthly forced deployment · True all-in cost (ER + turnover) · Exit load · AUM trajectory (135× growth) · **Module 4 Overall**

> **Expectation (revised):** No longer Quant's worst module on ER. **ER scores well (~4); AUM scores poorly (~2).** Net M4 likely lands **mid (~3.0–3.3)** — the cost story is better than the screen implied, but the scale story is the real drag.

---

## Module 5: Fund Manager Quality (15%)

### Raw Data Table (cross-source verified)
- Named PM(s) on **Quant Small Cap** specifically (verify — likely Sandeep Tandon as CIO + a fund manager such as Ankit Pande / Sanjeev Sharma; confirm current names and tenure on *this* fund).
- Tenure on fund · industry experience · career history · education · philosophy (VLRT) · co-managers · total schemes managed across AMC · total AUM managed · investor letters (No) · skin-in-game (not disclosed) · **personal SEBI issues (the Tandon probe)** · key-man risk.

### Carry-Forward + Small-Cap Additions
Most of this is established in the FlexiCap study. Add only:
- **2018 is moot (reframed):** the fund's 2018 "data" is from the dead Escorts era (not a real equity book), so VLRT was *not* tested in 2018. The relevant manager stress-tests are **2022 and the 2024–25 correction** (each ~−25% VLRT-era drawdowns) — assess how the team navigated those instead.
- **Research-team depth for small cap (Critical):** small caps need original research with no sell-side coverage. Does Quant have dedicated SC analysts, or does VLRT replace fundamental research with a quant signal? (The black-box question is sharper for small cap.)
- **AUM gate/close decisions:** did Quant ever restrict flows as Small Cap AUM grew to ₹30K Cr? (Likely no — a negative, like Bandhan/HSBC.)
- **Stock-discovery vs consensus:** is the SC book differentiated (like BOI) or momentum-chasing crowded names?

### The Governance Overhang (carry forward, confirm currency)
- Active SEBI front-running investigation on Tandon — status update since May 2026?
- Data-deletion allegation.
- Key-man risk: Tandon = MD + CEO + CIO + owner; black-box dies with him.

### Module 5 Scorecard
| Sub-dimension | Weight | Score | Reasoning |
- Tenure on fund · **2018 crash navigation (Critical)** · **SC research team depth (Critical)** · Philosophy clarity (VLRT = black-box penalty) · AUM gate history · Stock discovery · Skin-in-game · Investor communication · **SEBI/regulatory record (the probe)** · **Module 5 Overall**

> **Expectation:** Mirrors FlexiCap's 2.00/5 unless small-cap-specific evidence materially changes it. The active probe + black-box + key-man stack caps this module.

---

## Module 6: AMC Trustworthiness (5%)

### Carry Forward From FlexiCap (AMC module = 1.25/5)
Same AMC. Reuse the FlexiCap M6 findings; update only with anything new since May 2026:
- Private company, Tandon ~majority owner; no external governance.
- Active SEBI probe; alleged data deletion before raid.
- Scheme proliferation (33 schemes, growing).
- No meaningful investor communication.

### Small-Cap-Specific Additions
- **Fund gating history** — did the AMC ever pause SC SIPs at high AUM? (positive signal if yes; expected no).
- **SC research infrastructure** — feet-on-the-ground research vs pure quant signal.

### Module 6 Scorecard
| Sub-dimension | Weight | Score | Reasoning |
- Regulatory record (active probe) · Ownership/independence (private, owner-CIO) · Financial stability · Investor communication · Distribution conflict · Scheme focus · Gating history · **Module 6 Overall**

> **Expectation:** ~1.25–1.5/5, inherited from the FlexiCap study. This is the lowest AMC score in either project.

---

## README.md (Fund Summary File — written last)

Follow the SmallCap README template (see `dsp/README.md`, `boi/README.md`):

### Fund Identity Table
Scheme name, ISIN, scheme code (MFAPI), inception, AUM, ER Direct/Regular, exit load, benchmark (Nifty SmallCap 250 TRI), PM(s) + since, AMC, min SIP, VRO rating.

### The One-Line Context
Expected shape: *"Quant Small Cap is the highest-octane, lowest-trust fund the screen rejected — strong VLRT-era returns (21.01% 5Y, study-best 10Y SIP) whose '13-year record' is really a 6-year sprint glued to a near-dead Escorts legacy, disqualified on **scale alone** (₹31,900 Cr; the screener's ER 'fail' was a data error — true ER ~0.6%), carrying the study's highest volatility and an unverifiable black-box / front-running governance shadow that sank its FlexiCap sibling (2.49/5)."*

### Module Scores Summary + Final Scorecard (Mermaid xychart-beta)
Bars = module scores | Line = weighted total. Use the SmallCap weights: M1 25 / M2 20 / M4 20 / M3 15 / M5 15 / M6 5.

### Comparison vs Small Cap Shortlist + Score-Gap vs DSP (reference fund)
Show where Quant SC lands relative to DSP 4.00, BOI 3.66, HSBC 3.37, Bandhan 3.33, Invesco 3.29 — and note it is an *out-of-shortlist* entry.

### Hard Filter Checklist (Small Cap + carry-forward FlexiCap filters)
| Filter | Quant SC | Note |
- ER > 1.0%? → **NO (~0.6% true; screener's 1.13% was an error)**
- AUM > ₹30,000 Cr? → **YES (₹31,900 Cr, growing)** ← the sole genuine screening fail
- Regulator probe on key person? → **YES (Tandon — consent settlement filed)** *(carry-forward)*
- Data destruction / obstruction alleged? → **YES** *(carry-forward)*
- Max drawdown > 55%? → No (−46.71%)
- Single-group exposure > 20%? → check in M3 (FlexiCap had 24.56% Adani)
- Top-10 concentration > 65%? → check in M3 (FlexiCap had 71.4%)
- Black-box undocumented model? → **YES (VLRT)** *(carry-forward)*

### One-Line Verdict
Written after scoring.

---

## Research Sources Checklist

| Source | What to Pull |
|--------|-------------|
| Tickertape (downloaded) | All 6 SC CSVs — returns, risk, composition, ratios |
| ValueResearch Online | Independent returns, manager profile, fund history, rating |
| Morningstar India | Risk metrics, capture ratios, star rating |
| AdvisorKhoj | Rolling returns, SIP XIRR, calendar-year returns |
| Groww / IndMoney | Holdings, portfolio composition, cross-verify Sharpe/Sortino |
| Quant MF SID/SAI (AMFI) | Exact ER, exit load, penalties page, PM names |
| Quant MF website | Manager bios, VLRT description, fund factsheet |
| SEBI / news (BS, Mint, ET) | **Tandon front-running probe status update**, AMC news, AUM gate decisions |
| MFAPI (mfapi.in) | NAV history for 2018/COVID drawdown + recovery calculations |
| **FlexiCap Quant module files** | `Mutual Fund/FlexiCap/funds/quant/module[1-6]_*.md` — carry-forward AMC/manager findings |

---

## Module Writing Order (Recommended) — progress tracker

1. ✅ **Module 1** (Returns) — DONE (`module1_returns.md`, ~3.4/5).
2. ✅ **Module 2** (Risk) — DONE (`module2_risk.md`, ~3.1/5).
3. ✅ **Module 3** (Portfolio) — DONE (`module3_portfolio.md`, ~2.7/5). Key finding: **below the 65% SC floor (64.58%), highest large-cap of any studied fund (21.52%), mega-cap Reliance #1 (8.36%), Adani 10.62%, F&O leverage** — lowest M3 of the studied SC funds. Lone positive: below-category PE (~29.7). Turnover still undisclosed → M4. DHFL phantom-holding data flag.
4. ✅ **Module 4** (Cost & AUM) — DONE (`module4_cost.md`, ~2.8/5). ER anomaly resolved (true ~0.64%, mid-pack; screener's 1.13% wrong → fails only AUM). Regular ER 1.34%, **D-R gap ~0.65% (narrowest-tier — a positive)**. AUM ₹31,774 Cr (largest in study, over cap, 135× growth, no flow discipline) + **likely worst true all-in (~1.0–1.2% on VLRT turnover)** = lowest M4 of studied SC funds, the inverse of BOI. Turnover is data-issue #4 (AdvisorKhoj's 0.86% not credible).
5. ✅ **Module 5** (Manager) — DONE (`module5_manager.md`, ~2.3/5). Carry-forward governance floor (VLRT black box, extreme key-man, no transparency) + small-cap-specific negatives (**quant model structurally mismatched to SC** — the M3 up-cap-drift cause; two-era ~6Y meaningful tenure; no flow discipline) − partly offset by the **front-running consent settlement progressing** (≠ exoneration) + larger 7-PM team. Lowest M5 of studied SC funds, just above FlexiCap sibling (2.00). Data gap: exact per-PM start dates undisclosed (5th quant data issue).
6. ✅ **Module 6** (AMC) — DONE (`module6_amc.md`, ~1.5/5). Carry-forward FlexiCap AMC floor (1.25) + small-cap-specific (no gating at ₹31,774 Cr, largest redemption surface, no SC research bench) − settlement reportedly **accepted** (vs pending) + financial self-sustenance (beats BOI). Lowest M6 of studied SC funds. **Final weighted ≈ 2.86/5 — last of studied SC funds, above FlexiCap sibling (2.49).**
7. ✅ **README** — DONE (`README.md`). Final scorecard **≈ 2.86/5 — last of studied SC funds, above FlexiCap sibling (2.49)**. **STUDY COMPLETE** (all 6 modules + README). Verdict: Stage-1 elimination confirmed on every axis except raw returns.
7. **README** — last.

---

## Key Open Questions (updated; ✅ = answered in M1/M2)

1. ✅ **M1:** When did the VLRT regime start? **~2019–2020 (quant acquired Escorts 2018).** The 10Y/SI CAGR is a blend; SI alpha only +1.82%/yr — the dead era erased most lifetime alpha.
2. ✅ **M1/M2:** 2018 performance? **Moot — it was a dead Escorts fund in 2018** (2018 +3.10% vs −26.80% benchmark = non-participation, not protection; 2019 then −23.24%).
3. ✅ **M2:** VLRT downside protection? **VLRT-era up-capture ~148%, protective in 2022/2025; but bear-untested** (worst VLRT drawdown only ~−25%).
4. ✅ **M2:** Recovery from the −46.71% max DD? **~597 days (~1.6y)** underwater (Dec-2018 peak → Aug-2020); it's a transition-era drawdown.
5. **M3:** Single-group / top-10 concentration vs FlexiCap's 24.56% Adani / 71.4% top-10? *(open)*
6. **M3:** Actual SC portfolio turnover, and hidden impact cost at ₹31,900 Cr? *(open — feeds M4 true-cost)*
7. **M4:** Resolve the ER anomaly (canonical Direct ER) and compute true all-in (ER ~0.6% + turnover). Is true all-in still elevated despite the low headline? *(open)*
8. **M4:** At ₹31,900 Cr, can VLRT deploy into genuine 350th–600th-rank small caps, or is it forced to the large end (Nippon problem)? *(open)*
9. **M5:** Confirm the 7-PM team's tenure *on this fund*; how did they handle 2022 / 2024-25? Consent-settlement status. *(open)*
10. **Verdict:** Do strong VLRT returns overturn the **scale + governance** elimination (ER is NOT the issue)? *(Provisional: no — M1 ~3.4, M2 ~3.1 track toward a mid-low overall, consistent with the FlexiCap sibling's 2.49.)*

---

*Plan created: 2026-06-16 | Revised: 2026-06-17 after M1 & M2 research (MFAPI-computed data overturned the "genuine 2018-tested" premise and the ER "fail") | Framework: 6-module weighted scoring (Small Cap adaptation) | Status: out-of-shortlist study (eliminated Stage 1 on **AUM alone**, not ER) | Progress: M1 ✅ (~3.4) · M2 🔄 (~3.1, ready to write) · M3–M6 pending | To study: Quant Small Cap Fund*
