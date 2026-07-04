# Deep Study Plan — Mid Cap Funds

## Context

Fourth category study, following the established pipeline: **screen the universe → shortlist → 6-module deep study per fund → decision tree**. Same 6-module weighted framework as FlexiCap, SmallCap, and International, with material adjustments for mid-cap-specific characteristics.

**Investment goal (working assumption):** ₹20,000/month SIP, 10+ year horizon — a **return-enhancer sleeve** between the FlexiCap core and the SmallCap satellite.

**The two framing facts (read first):**

1. **The 150-stock pond.** SEBI defines mid cap as ranks 101–250 — a *fixed, shared* 150-stock universe. Differentiation cannot come from discovery (everything is covered); it comes from selection, weighting, the 35% flexible sleeve, and discipline. **Active share vs the Nifty Midcap 150 is a first-class metric in this study** — the category's closet-indexing risk is structural.
2. **Mid cap is a return enhancer, not a diversifier.** Correlation to the Nifty is ~0.85–0.90 (vs the International sleeve's R² of 11%). The case for the sleeve rests entirely on *incremental CAGR per unit of incremental drawdown* — and on **not duplicating** mid-cap exposure the FlexiCap and SmallCap sleeves already carry.

---

## Phase 0 — The Prior Question (before any screening)

Unlike the first three studies, MidCap starts with a gate: **does a dedicated mid-cap sleeve earn a slot in this portfolio at all?** Three analyses, done once, before fund-level work:

| # | Analysis | Method | Kill criterion |
|---|----------|--------|----------------|
| 0.1 | **Existing mid-cap exposure audit** | Pull current holdings of Parag Parikh FlexiCap + DSP Small Cap (+ any other funds actually held); classify each holding by AMFI cap band; compute the portfolio's *effective* mid-cap % | If blended portfolio already holds >20–25% effective mid-cap, the marginal sleeve is dilutive |
| 0.2 | **Index-level redundancy test** | Correlation + rolling-return spread of Nifty Midcap 150 TRI vs Nifty 500 TRI and Nifty SmallCap 250 TRI (MFAPI index-fund NAVs, 10Y+) | If midcap's 10Y rolling return sits inside the FlexiCap–SmallCap envelope with >0.9 correlation to both, the band adds little |
| 0.3 | **The passive alternative benchmark** | A Nifty Midcap 150 index fund (~0.20% ER) is *open and investable* (unlike International's closed passive lane). Every active mid-cap fund studied must beat this, not just its peers | Standing question for every Module 1: "why not the index fund?" |

> **Deliverable:** a short `phase0_prior_question.md` with a PROCEED / PROCEED-WITH-REDUCED-ALLOCATION / STOP verdict. Only on PROCEED does screening begin. This discipline is borrowed from the International study, where the SEBI-cap analysis reshaped the whole study before any fund was touched.

> **⚠ STATUS (July 3, 2026): Phase 0 DEFERRED by user decision** — the focus is the study itself; portfolio construction comes later. Analyses 0.1/0.2 move to decision-tree time. Analysis 0.3 (the passive counterfactual) survives inside every Module 1/Module 4 as the "why not the index fund?" test.

---

## Phase 1 — Screening Pipeline

### Data required (Tickertape export, ~30 funds, Direct Growth)

Same 6-file screener set as SmallCap, filtered to Mid Cap:

| File | Contents |
|------|----------|
| 1 | AUM, ER, NAV, fund manager, inception, exit load, AMC |
| 2 | Alpha, CAGR 10Y/5Y/3Y, rolling 3Y avg, absolute returns 1Y/6M/3M |
| 3 | Max drawdown, volatility, category St Dev |
| 4 | Sharpe, Sortino, PE ratio, returns vs sub-category (1Y/3Y/5Y/10Y) |
| 5 | % away from ATH, largecap %, midcap %, top-10 concentration |
| 6 | Smallcap %, equity %, debt %, cash %, top-3/top-5 concentration |

Save to `Mutual Fund/TickerTape Data/` with the export date in the filename (the May 21, 2026 CSVs are Small Cap category — **do not reuse**).

### Stage 1 — Hard Filters (applied in order)

| Filter | Threshold | Rationale | vs siblings |
|--------|-----------|-----------|-------------|
| Expense Ratio | **ER ≤ 1.0% (Direct)** | Mid-cap alpha over a 0.20% index fund is thin; paying >1% consumes it structurally | Same as SmallCap (FlexiCap: 1.5%) |
| AUM minimum | **AUM ≥ ₹500 Cr** | Operational viability, redemption resilience | Same as siblings |
| AUM maximum | **AUM ≤ ₹50,000 Cr** | 65% of ₹50,000 Cr = ₹32,500 Cr deployed across ≤150 liquid names is workable; beyond it the fund is forced toward the index + mega-mid names. Softer than SmallCap's ₹30,000 Cr because mid caps are far more liquid | **New calibration** — between FlexiCap (none) and SmallCap (₹30,000 Cr) |
| Fund age | **≥ 60 months** | Must cover at least one full correction; ideally reaches the 2018–19 midcap winter | Same as siblings |
| Sharpe Ratio | **Sharpe ≥ 0** | Below risk-free at mid-cap risk is disqualifying | Same as siblings |

> **AUM threshold note:** the exact ceiling should be sanity-checked against the actual distribution at export (the intent is to eliminate only the structurally-impaired giants, not the whole top quartile). If HDFC Mid-Cap Opportunities (~₹70–80,000 Cr) falls above the cut, study it anyway as an **out-of-shortlist instructive case** — the category's capacity question deserves a deep-dive the way quant Small Cap did.

### Stage 2 — Performance Filters (both must be met)

| Filter | Threshold | Rationale |
|--------|-----------|-----------|
| 5Y CAGR | **> full-universe median** (all ~30 funds' non-zero 5Y values) | Cycle-aware horizon; full-universe median avoids survivor-inflation (same reasoning as SmallCap) |
| Returns vs sub-category (3Y) | **> 1.0x** | Consistent peer outperformance |

**Not used as filters (studied in modules instead):** max drawdown (inception-biased — same trap as SmallCap's Bandhan), AUM inside the pass band (continuous, Module 4), alpha vs index (needs TRI care, Module 1).

**Expected funnel:** ~30 → ~12–15 → **6–9 shortlisted**.

### Deliverables

`screening/methodology.md`, `screening/stage1_hard_filters.md` (fund-by-fund elimination log), `screening/stage2_performance.md`, `screening/all_funds_data.md` — same format as the SmallCap/International sets.

---

## Phase 2 — The 6 Modules (weights unchanged)

| Module | Weight |
|--------|--------|
| 1 — Returns Consistency | 25% |
| 2 — Risk Profile | 20% |
| 4 — Cost & AUM Impact | 20% |
| 3 — Portfolio DNA | 15% |
| 5 — Fund Manager Quality | 15% |
| 6 — AMC Trustworthiness | 5% |

**Scale:** 1 = Poor · 2 = Below Avg · 3 = Average · 4 = Good · 5 = Excellent

---

### Module 1 — Returns Consistency (25%)

**What's the same:** CAGR 3Y/5Y/10Y, 3Y rolling average, alpha vs benchmark, returns vs sub-category, calendar-year decomposition, MFAPI-computed verification (the method proven across all three prior studies).

**What's different for Mid Cap:**

| Dimension | SmallCap | Mid Cap |
|-----------|----------|---------|
| Benchmark | Nifty SmallCap 250 TRI | **Nifty Midcap 150 TRI** |
| The alpha bar | Beat illiquid-universe peers | **Beat an investable 0.20% index fund** — the "why not the index?" test is sharper than in any prior study because the passive alternative is open (unlike International) and truly representative (unlike small-cap indices, which active funds beat structurally) |
| Key stress window | 2018 IL&FS (Jul 2018–) | **The 2018–19 midcap winter starts EARLIER — Jan 2018** (post-SEBI-reclassification unwind + LTCG introduction), then IL&FS compounds it; full window Jan 2018 → Aug 2019 |
| Inception bias | 2018–2020 launches | Same flag — plus **2020–21 launches** (WhiteOak, several others) that have only seen a bull market |
| Migration effect | Winners leave the mandate (grow into mid) | **Winners arrive from below** — a mid-cap fund inherits small-cap graduates with momentum; check whether returns come from holding graduates vs picking within the band |

**Key calendar years to study per fund:**

| Year | Market event | Why it matters for Mid Cap |
|------|-------------|---------------------------|
| 2017 | Mid/small bull mania | Full participation check (Nifty Midcap 100 ~+47%) |
| **2018** | **SEBI reclassification unwind + LTCG + IL&FS; midcaps fell hard while Nifty was ~flat** | **THE stress test — the largecap/midcap divergence year separates discipline from beta** |
| 2019 | Polarised market; midcaps kept falling while Nifty rose | Second consecutive test — quality visible |
| 2020 | COVID crash + V-recovery | Two extreme halves masked by full-year number |
| 2021 | Broad bull; midcaps +45%+ | Participation check |
| 2022 | Rate-hike correction | Midcap 150 roughly flat — did the fund hold up? |
| 2023 | Midcap rally (+40%+) | Should be a strong year |
| 2024 | Continuation, then Sep-2024 top | Momentum + froth management |
| 2024–25 | **Sep 2024 – Feb/Mar 2025 correction (~−20% for the band)** | The freshest stress test — every current manager was on duty for it |
| 2026 YTD | Recovery | Current positioning |

**Module 1 Scorecard:**

| Sub-dimension | Weight | Scoring guide (recalibrate to actual medians at data export) |
|---------------|--------|----------------------------------------------------------|
| 10Y CAGR (if available) | High | ≥18% = 5, 16–18% = 4, 14–16% = 3, <14% = 2 |
| 5Y CAGR vs category median | High | Top quartile = 5, above median = 4, at median = 3 |
| **Alpha vs Nifty Midcap 150 TRI** | **Critical** | >3% ann. = 5; 1–3% = 4; ±1% = 3 (**index-fund territory — why pay active fees?**); negative = 2 |
| 3Y rolling average | High | vs shortlist peers |
| 2018–19 winter performance (if available) | Critical | Shallower fall + faster recovery than index = 5; absent = flag prominently |
| 2024–25 correction performance | High | Every fund has this data — the universal, no-excuses stress test |
| Inception bias adjustment | Modifier | Discount CAGR for post-2019 launches |
| Consistency (worst year vs index) | Medium | No catastrophic single-year deviation |

---

### Module 2 — Risk Profile (20%)

**Risk thresholds sit between FlexiCap and SmallCap:**

| Risk metric | FlexiCap "good" | **Mid Cap "good"** | SmallCap "good" | Mid Cap "alarming" |
|-------------|-----------------|--------------------|-----------------|--------------------|
| Max Drawdown | <35% | **<38%** | <40% | >50% |
| Volatility | <13% | **<15%** | <16% | >18% |
| Beta (vs Midcap 150) | — | **<1.0** | — | >1.15 |
| Downside capture (vs Midcap 150) | <85% excellent | **<90% excellent** | <85% | >105% |

**Mid-cap-specific risk questions:**

1. **Drawdown vs the index, not just absolute** — the band itself draws 35–40% in bad cycles; the question is whether the fund cushions or amplifies. (Same "judge vs own index" discipline as International.)
2. **Recovery time** — midcap recoveries are faster than small-cap (better liquidity, index inclusion flows) but the 2018–19 winter took ~2 years. Compute per fund from MFAPI NAVs.
3. **The 35% sleeve as a risk dial** — a fund running its flexible 35% in *small caps* is structurally riskier than one running it in large caps, at identical "mid-cap fund" labels. Quantify: effective portfolio cap-weighted risk, not category label.
4. **Redemption/liquidity risk is LOW** — unlike SmallCap, no redemption-spiral analysis needed; note and move on. The freed attention goes to concentration: with 150 names, top-10 concentration >40% means big single-stock bets in a covered universe.
5. **Correlation to existing sleeves** — compute R²/correlation vs Parag Parikh FlexiCap and DSP Small Cap NAVs directly (the International study's method vs Franklin). This feeds the decision tree's redundancy verdict.

**Module 2 Scorecard:**

| Sub-dimension | Weight | Scoring guide |
|---------------|--------|---------------|
| Max Drawdown (inception-adjusted) | High | <35% = 5, 35–42% = 4, 42–50% = 3, >50% = 2 |
| Downside capture vs Midcap 150 | Critical | <90% = 5, 90–100% = 4, 100–105% = 3, >105% = 2 |
| Sharpe | High | vs category distribution at export |
| Sortino | Medium | Same scale |
| Recovery time from max DD | Medium | <12 mo = 5, 12–18 = 4, 18–24 = 3, >24 = 2 |
| 2018–19 winter drawdown (if available) | Critical | Beat the index's fall and recovery = 5 |
| Volatility vs category | Medium | Below avg = 5 |
| Effective risk of the 35% sleeve | Medium | Large-cap ballast = lower risk score benefit; small-cap kicker = flag |
| Correlation to existing sleeves | Informational | Feeds decision tree, not the fund score |

---

### Module 3 — Portfolio DNA (15%)

**The mid-cap-specific reframe: in a 150-stock shared pond, *how* a fund differs from the index and from its peers IS the module.**

1. **Active share vs Nifty Midcap 150** — the headline metric. <40% = closet indexer (why pay active fees?); 40–60% = moderately active; >60% = genuinely active. No prior study needed this; MidCap can't be done without it.
2. **Where in the band?** Ranks 101–150 (mega-mids, index-heavy, liquid) vs 200–250 (recent small-cap graduates, higher octane). Average holding rank / market cap tells you the fund's true aggression.
3. **The 35% flexible sleeve** — the fund's personality: large-cap ballast vs small-cap kicker vs cash. Consistency of this stance over time (tactical flip-flopping = flag).
4. **Graduation management** — what happens when a holding exits the band (up to large, or index reclassification)? Forced-ish selling vs letting winners run inside the 35%? Check turnover attributable to reclassification.
5. **Cross-sleeve overlap (the decision-tree feed)** — name-by-name overlap vs Parag Parikh FlexiCap and DSP Small Cap current portfolios. The International study proved this matters (Franklin duplicated PP's US book); mid cap is where duplication risk is highest.
6. **Standard checks** — top-10 concentration (25–35% reasonable), stock count (40–70 sweet spot given a 150-name universe; >90 = index-hugging by construction), sector caps (<25%), turnover (<70% preferred; the illiquidity penalty is milder than SmallCap).

**Module 3 Scorecard:**

| Sub-dimension | Weight | Scoring guide |
|---------------|--------|---------------|
| **Active share vs Midcap 150** | **Critical** | >60% = 5, 45–60% = 4, 35–45% = 3, <35% = 2 (closet indexer) |
| Mid-cap mandate honesty (% in band) | Medium | 65–75% with a deliberate 35% = 5; barely-65% + drift = 3 |
| Quality/intent of the 35% sleeve | High | Documented, consistent strategy = 5; opportunistic churn = 2 |
| Band positioning (101–150 vs 200–250 mix) | Medium | Deliberate and disclosed = higher; accidental index-mirror = lower |
| Top-10 concentration | Medium | 25–35% = 5, 35–45% = 4, >45% or <20% = 3 |
| Number of stocks | Low | 40–70 = 5, 70–90 = 4, >90 or <30 = 3 |
| Sector diversification | Medium | No sector >25% |
| Turnover | Medium | <50% = 5, 50–80% = 4, 80–110% = 3, >110% = 2 |
| **Overlap with existing sleeves** | Informational | Reported per fund; scored in the decision tree, not here |

---

### Module 4 — Cost & AUM Impact (20%)

**The cost story is sharper than SmallCap's** because the passive alternative is investable: a Nifty Midcap 150 index fund at ~0.20% is the permanent counterfactual. Every basis point of active ER must buy verified alpha.

**The Mid Cap AUM ladder:**

| AUM range | Status | Reasoning |
|-----------|--------|-----------|
| < ₹500 Cr | Too small | Eliminated Stage 1 |
| ₹500 – 3,000 Cr | Small but agile | Full 150-name flexibility; watch AMC commitment |
| ₹3,000 – 25,000 Cr | **Sweet spot** | Can hold meaningful positions across the whole band without moving prices |
| ₹25,000 – 50,000 Cr | Approaching constraint | Gravitates to ranks 101–180 + index-weight hugging; monitor active share decay |
| > ₹50,000 Cr | Eliminated Stage 1 | 65% mandate across 150 names forces quasi-index behaviour (study the giant separately as an instructive case) |

**Forced-deployment check (per fund):** monthly net inflow × 65% into the band; compare against average daily traded value of typical holdings. Mid-cap liquidity makes this far milder than SmallCap — quantify to confirm, then reallocate scrutiny to **active-share decay as AUM grows** (the real mid-cap capacity symptom: the fund quietly becomes the index).

**ER impact on 10Y SIP corpus (₹20K/month, 18% gross):**
- 0.20% (index fund): benchmark corpus
- 0.45% ER active: needs ~0.25%+ annual alpha just to tie
- 0.90% ER active: needs ~0.70%+ annual alpha — roughly ₹1.5–2 lakh of extra corpus to justify itself over 10 years

**Module 4 Scorecard:**

| Sub-dimension | Weight | Scoring guide |
|---------------|--------|---------------|
| Expense Ratio (Direct) | High | ≤0.45% = 5, 0.45–0.65% = 4, 0.65–0.85% = 3, 0.85–1.0% = 2 |
| **ER vs verified alpha (the index-fund test)** | Critical | Alpha (M1) comfortably exceeds ER premium over the 0.20% index = 5; alpha ≈ ER premium = 3; alpha < premium = 2 |
| AUM position on the ladder | High | Sweet spot = 5; approaching constraint = 3 |
| Active-share trend as AUM grew | High | Stable/rising = 5; decaying toward index = 2 |
| Forced deployment | Medium | Quantified vs band liquidity |
| Exit load | Low | Standard 1%/365d |
| AUM trajectory | Low | Fast growth near the ceiling = escalating constraint |

---

### Module 5 — Fund Manager Quality (15%)

| Dimension | SmallCap importance | Mid Cap importance |
|-----------|--------------------|--------------------|
| Tenure on fund | High | High |
| 2018–19 winter (was the manager there?) | Critical | **Critical — and note it starts Jan 2018, before IL&FS** |
| Original research / discovery | Critical (no coverage) | **Lower — everything is covered; the skill is selection + discipline, not discovery** |
| Sell discipline | Medium | **Critical — in a momentum-prone band, when to exit graduates and de-rate darlings is where mid-cap alpha lives** |
| Capacity stewardship | Very High (gating) | High — has the manager defended active share as AUM grew? Any soft-close history? |
| Philosophy clarity | High | High — especially the documented policy for the 35% sleeve and for graduation handling |

**Key question per manager:** through the fund's growth, did active share and band-positioning stay consistent (conviction) or drift toward the index (capacity surrender)? This is the mid-cap version of SmallCap's "did they gate the fund?" test.

**Module 5 Scorecard:**

| Sub-dimension | Weight | Scoring guide |
|---------------|--------|---------------|
| Manager tenure on this fund | High | Same scale as siblings |
| 2018–19 winter navigation (if present) | Critical | Present and outperformed = 5; absent = flag |
| 2024–25 correction navigation | High | Universal test — every incumbent has it |
| Sell/graduation discipline (documented) | High | Clear policy + evidence in turnover data = 5 |
| Philosophy clarity (incl. the 35% policy) | High | Documented and followed = 5 |
| Capacity stewardship (active-share defence) | Medium | Maintained conviction at scale = 5 |
| Skin in the game | Low | Same as siblings |
| Investor communication | Medium | Same as siblings |
| SEBI/regulatory record | High | Same as siblings |

---

### Module 6 — AMC Trustworthiness (5%)

Same framework as siblings. Mid-cap-specific additions:

1. **Carry-forward findings first** — the AMC bench is now deep: Parag Parikh, HDFC, quant, JM, Edelweiss, BOI, HSBC (FlexiCap); DSP, Invesco, Bandhan, Union, Sundaram (SmallCap); Franklin, PGIM (International). For any shortlisted fund from these AMCs, **carry the existing AMC verdict forward and update only with mid-cap-specific data** — do not re-research from scratch.
2. **Fund-suite coherence** — does the AMC run mid cap as a serious long-term franchise, or did it launch at the 2021/2024 tops to harvest flows? Launch-timing history is a governance signal.
3. **Capacity conduct** — any history of soft-closing, gating lumpsums, or honestly flagging capacity in investor communications (the Mirae Emerging Bluechip precedent — a Large&Mid fund that restricted inflows — is the category's investor-first benchmark).

---

## Study Order (set July 3, 2026, post-screening)

| Priority | Fund | Rationale | Key question |
|----------|------|-----------|--------------|
| **1** | **Nippon India Growth Mid Cap** | Longest record in the shortlist (fund dates to 1995 — pre-dates the 163mo data cap by decades); full 2018-winter, COVID, 2022, 2024–25 data; largest survivor (₹47,415 Cr, just under the AUM cut) — its capacity analysis doubles as the HDFC/Kotak giant question from inside the shortlist. Builds the category reference frame. | Can a ₹47,000 Cr fund still be genuinely active in a 150-stock pond — or is the shortlist's #2 CAGR quietly becoming the index? |
| **2** | **Invesco India Midcap** | Best 10Y (20.34%) AND best 5Y (21.91%) at 0.49% — the screening leader. AMC continuation from SmallCap (Invesco SC scored 3.29; the Hinduja-group AMC-sale question carries forward). | Is the dual-horizon leadership genuine manager skill, and does the AMC ownership change threaten it? |
| **3** | **HSBC Midcap** | The anomaly: Sharpe 0.848 (3× shortlist norm), 1Y +17.5% (best in universe), 3Y 27.68%. AMC continuation ×2 (FlexiCap + SmallCap, incl. the 52.45% SC drawdown question). Fund is the former **L&T Midcap** (acquired 2022) — the record partly belongs to another house. | Is the risk-adjusted dominance a durable style or a hot streak — and whose track record is it, L&T's or HSBC's? |
| **4** | **Edelweiss Mid Cap** | Strong balanced profile (19.88% 10Y, 20.64% 5Y, 0.48% ER). AMC continuation ×3 — Edelweiss is now studied in every category (FlexiCap 3.77, SmallCap ≈3.61, five International feeders); the governance file is thick. | Does the strongest Edelweiss fund yet override the AMC's accumulated governance flags? |
| **5** | **Mahindra Manulife Mid Cap** | Cheapest ER (0.42%), smallest AUM (₹4,866 Cr — maximum agility), ~Dec-2017 inception nearly covers the full midcap winter. Brand-new AMC for the studies. | Is this the hidden gem profile — small, cheap, agile — or small for a reason (AMC commitment, team depth)? |
| **6** | **ICICI Pru Midcap** | Highest volatility of the shortlist (17.5%) with mid-pack returns; India's second-largest AMC never deep-studied. | Why does the giant AMC's midcap fund run the highest risk for middling output? |
| **7** | **Sundaram Mid Cap** | Weakest 10Y (15.63%), priciest ER (0.88%) — the confirm-the-elimination study, mirroring Sundaram Small Cap's role. | Any reason to prefer it over the top-4? (Expected: no.) |
| Optional A | **HDFC Mid Cap** (out-of-shortlist) | ₹97,350 Cr — the capacity case study à la quant Small Cap | What does ₹63,000 Cr of forced mid-cap exposure look like vs the index? |
| Optional B | **Motilal Oswal Midcap** (out-of-shortlist) | Best 5Y CAGR in the universe → Sharpe −0.69 in one correction | The anatomy of a momentum-concentration blowup — the cautionary tale for chasing trailing CAGR |

---

## Module Writing Reference

For each fund, 6 module files + README (written last):

```
Mutual Fund/MidCap/funds/<fund_name>/
├── README.md          ← Fund summary, scorecard, verdict (written last)
├── module1_returns.md
├── module2_risk.md
├── module3_portfolio.md
├── module4_cost.md
├── module5_manager.md
└── module6_amc.md
```

Folder names assigned at shortlist (pattern: `hdfc/`, `motilal/`, `edelweiss/`, `kotak/`, `nippon/`, `sbi/`, `invesco/`, `quant/`, `pgim/`, `whiteoak/` …).

Each module carries the standard apparatus proven in the prior studies: MFAPI-computed NAV metrics (CAGR, calendar years, rolling 3Y, drawdown/recovery, SIP XIRR), mermaid scorecard charts, comparative tables vs already-studied funds, and a provisional score footer.

---

## Phase 3 — Decision Tree

After all shortlisted funds are studied, `decision_tree.md` must answer, in order:

1. **The sleeve question (from Phase 0, now evidence-backed):** does the best mid-cap fund add enough non-duplicated exposure over PP FlexiCap + DSP Small Cap + International to justify a fourth ₹20K/month sleeve — or is the honest answer "increase an existing sleeve instead"?
2. **Active vs passive:** did any active fund's verified alpha survive the index-fund test (M1 alpha vs M4 cost)? If not, the recommendation may be the Nifty Midcap 150 index fund itself — a legitimate outcome unavailable to the International study.
3. **If active and yes:** which fund(s), what split, and the standard deployment mechanics (SIP date, step-up, review triggers).
4. **Review triggers:** active-share decay, AUM crossing the constraint zone, manager exit, and the standing sibling triggers.

---

## Data Sources per Fund

| Source | What to pull |
|--------|-------------|
| Tickertape CSVs (fresh Mid Cap export) | All screening quantitative data |
| MFAPI (mfapi.in) | NAV history — own CAGR/rolling/drawdown/SIP-XIRR computations (the canonical method) |
| Nifty Midcap 150 TRI (index fund NAV via MFAPI as proxy) | Alpha, capture ratios, active-share denominator |
| ValueResearch / Morningstar India | Independent verification, ratings, capture ratios |
| AMC monthly factsheet + SID/SAI | Holdings, band positioning, the 35% policy, turnover, manager bios |
| AMFI semi-annual cap classification list | The authoritative 101–250 band list — needed for band-positioning and overlap analysis |
| AdvisorKhoj | Rolling returns, SIP XIRR cross-check |
| Business Standard / Mint / ET | Manager changes, capacity/gating news, AMC governance |
| SEBI/BSE/NSE | Regulatory actions |

---

## Execution Checklist

- [~] **Phase 0:** Prior-question analysis — **DEFERRED to decision-tree time** (user decision, Jul 3 2026: study first, portfolio later). The passive-counterfactual test (0.3) lives on inside M1/M4 per fund
- [x] **Phase 0:** Data acquisition — pulled via Tickertape screener API, Jul 3 2026 → `TickerTape Data/MidCap_Screener_API_03_07_2026.csv` (manual CSV export not needed)
- [x] **Phase 1:** `screening/methodology.md` — thresholds confirmed against actual universe
- [x] **Phase 1:** `screening/stage1_hard_filters.md` (33 → 15) + `screening/stage2_performance.md` (15 → 7) + `screening/all_funds_data.md`
- [x] **Phase 1:** README + this file updated with shortlist and study order
- [ ] **Phase 2:** Deep studies — 6 modules + README per fund, in study order (Nippon → Invesco → HSBC → Edelweiss → Mahindra Manulife → ICICI Pru → Sundaram)
- [ ] **Phase 2 (optional):** Instructive cases — HDFC Mid Cap (capacity), Motilal Oswal (momentum blowup)
- [ ] **Phase 3:** `decision_tree.md` — sleeve verdict (incl. deferred Phase-0 analyses), active-vs-passive verdict, deployment strategy

---

*Study plan version: 1.1 | Created: July 2026 | Status: screening complete (33 → 15 → 7, Jul 3 2026) — deep studies not started | Framework: 6-Module Weighted Scoring (Mid Cap adaptation) | Defining constraint: the fixed 150-stock universe → active share is first-class | Prior question deferred: study first, portfolio later*
