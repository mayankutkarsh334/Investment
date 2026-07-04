# Mid Cap Fund Category

## What is a Mid Cap Fund?

A Mid Cap Fund must invest **minimum 65% in mid-cap stocks** — defined by SEBI as companies ranked **101st to 250th** by full market capitalisation (per the AMFI list, updated every six months). The remaining 35% can be deployed across large-cap, small-cap, or debt at the manager's discretion.

**SEBI mandate:** Minimum 65% in mid-cap equities. No upper limit — some funds run 75%+ in mid cap.

**The band in rupee terms (approx., 2026):** roughly ₹30,000 Cr to ₹1,00,000 Cr market cap — established, exchange-covered companies that are past the small-cap survival stage but before large-cap maturity.

---

## ⚠ The Defining Constraint: The 150-Stock Pond

Every category study in this repo has one structural fact that shapes everything:

| Category | Defining constraint |
|----------|--------------------|
| SmallCap | The AUM ceiling — large funds can't execute genuine small-cap |
| International | The SEBI $7bn overseas cap — the passive lane is closed |
| **MidCap** | **The investable universe is FIXED at 150 stocks** |

SEBI's rank-based definition means every mid-cap fund selects from the **same 150 names**. Small-cap managers differentiate by hunting in a ~750+ stock ocean; a mid-cap manager's entire opportunity set is publicly listed, analyst-covered, and shared with every competitor. Consequences the study must test per fund:

1. **High inter-fund overlap** — many mid-cap funds hold 40–60% of the same stocks. Holding two mid-cap funds diversifies almost nothing.
2. **Closet-indexing risk** — with only 150 names and ~50–70 holdings typical, a fund can be a Nifty Midcap 150 tracker charging active fees. **Active share vs the index is a first-class metric here** (it wasn't in SmallCap).
3. **Capacity is real but softer than SmallCap** — mid caps are liquid, but the category's giants (₹60,000 Cr+ AUM) still strain against a 150-stock pond, forcing either index-hugging or drift into the 35% flexible sleeve.
4. **The 35% is the personality** — since the 65% comes from a shared pond, a fund's character often lives in what it does with the rest: large-cap ballast (defensive), small-cap kicker (aggressive), or cash (tactical). Two "mid-cap funds" can carry very different risk.

---

## Why Study Mid Cap for SIP?

Mid cap sits between the FlexiCap core and the SmallCap satellite on the risk-return spectrum:

- **Return profile:** historically outruns large-caps over 10Y+ (Nifty Midcap 150 TRI has beaten Nifty 50 TRI by ~3–5%/yr over long windows) with shallower drawdowns than small-cap
- **The "sweet spot" thesis:** companies that survived the small-cap stage, still growing at 15–25%, with institutional-grade governance — the best structural growth band in Indian equity
- **Liquidity:** manager can actually exit positions in a crisis (unlike small-cap)
- **The counter-thesis (must be tested honestly):** mid-cap correlates ~0.85–0.90 with both the Nifty and the SmallCap 250. Unlike the International sleeve (R² 11% to Nifty), **a mid-cap fund adds no meaningful decorrelation — it is a return enhancer, not a diversifier.**

**Context:** This is the **fourth category study**. Existing framework: FlexiCap core (Parag Parikh #1, 4.20/5), SmallCap satellite (DSP #1, 4.00/5), International diversifier (in progress; Franklin US ≈3.14/5). Working assumption: **₹20,000/month SIP, 10+ year horizon**, consistent with the sibling sleeves — but see "The Prior Question" in [study_plan.md](study_plan.md): whether MidCap earns a distinct slot at all is itself a study output, not an assumption.

---

## The Prior Question: Does Mid Cap Earn a Slot?

The user's portfolio already touches the mid-cap band from two directions:

| Existing sleeve | Mid-cap exposure it already carries |
|-----------------|-------------------------------------|
| FlexiCap funds | Free to hold mid caps; most hold 15–35% |
| SmallCap funds | The 35% flexible sleeve often sits in mid caps; plus small-cap winners *migrate* into the mid-cap band and managers often let them run |

So a dedicated mid-cap fund may partially **duplicate what the existing sleeves already own**. The study must quantify this before the decision tree: measured overlap of each shortlisted mid-cap fund vs the actual current portfolios of Parag Parikh FlexiCap and DSP Small Cap. This is the mid-cap analog of the International study's "Franklin overlaps PP FlexiCap's US book" finding — and it is a **gate**: if the best mid-cap fund is >40% duplicated by the existing sleeves, the honest recommendation may be "no fourth sleeve."

---

## Universe

- **Total Mid Cap funds (July 3, 2026):** 33 (Direct, Growth — after removing 1 duplicate + 3 misfiled SIF long-short products)
- **After Stage 1 hard filters (ER ≤ 1.0%, ₹500 Cr ≤ AUM ≤ ₹50,000 Cr, age ≥ 60mo, Sharpe ≥ 0):** 15
- **After Stage 2 performance filters:** **7 shortlisted funds**

> **The big-brand fallout:** HDFC (₹97,350 Cr) and Kotak (₹64,749 Cr) died on the AUM cap; **Motilal Oswal — the universe's best 5Y CAGR (23.0%) — died on a −0.69 Sharpe** after the 2024–25 correction unwound its momentum book; SBI, Franklin, UTI, PGIM also fell to negative Sharpe; Axis and DSP survived Stage 1 but failed Stage 2 on weak 5Y CAGR. The category's marketing hierarchy and its performance hierarchy are very different things.

---

## Data Source

Data pulled **directly from the Tickertape screener API** on **July 3, 2026** (Direct plan figures, Growth option) — no manual CSV export needed. Raw data: `Mutual Fund/TickerTape Data/MidCap_Screener_API_03_07_2026.csv`. Premium-gated fields (max drawdown, rolling 3Y, vs-category ratios) are substituted at screening (see [screening/methodology.md](screening/methodology.md)) and computed independently from MFAPI NAV history in the deep studies.

---

## Final Shortlist (7 funds, sorted by 5Y CAGR)

| # | Fund | AUM (Cr) | ER% | 10Y | 5Y | 3Y | Sharpe | Vol |
|---|------|----------|-----|------|------|------|--------|------|
| 1 | **Invesco India Midcap** | 12,397 | 0.49 | **20.34%** | **21.91%** | 26.91% | 0.408 | 16.9% |
| 2 | **Nippon India Growth Mid Cap** | 47,415 | 0.73 | 19.32% | 21.48% | 23.10% | 0.264 | 15.7% |
| 3 | **Edelweiss Mid Cap** | 16,849 | 0.48 | 19.88% | 20.64% | 24.05% | 0.135 | 15.2% |
| 4 | **HSBC Midcap** | 14,249 | 0.56 | 18.47% | 20.44% | **27.68%** | **0.848** | 16.2% |
| 5 | **Mahindra Manulife Mid Cap** | 4,866 | **0.42** | — | 20.17% | 23.67% | 0.405 | 15.9% |
| 6 | **Sundaram Mid Cap** | 13,687 | 0.88 | 15.63% | 19.31% | 22.27% | 0.210 | 15.2% |
| 7 | **ICICI Pru Midcap** | 7,789 | 0.87 | 17.78% | 19.01% | 24.75% | 0.456 | 17.5% |

> **Five of seven AMCs are known quantities** from prior studies (Edelweiss, HSBC, Invesco, Sundaram fully; ICICI partially) — Module 6 carry-forwards will accelerate this study. Only Nippon and Mahindra Manulife need ground-up AMC work.

---

## Deep Study Progress

| Rank | Fund | Score | Status |
|------|------|-------|--------|
| 1 | **Invesco India Midcap** | **≈3.97 / 5** | ✅ **Complete** (6 modules + README) — the screening leader; **dead heat with Nippon** |
| 2 | **Nippon India Growth Mid Cap** | **≈3.96 / 5** | ✅ **Complete** (6 modules + README) — the reference frame |
| — | HSBC Midcap | Pending | Next (study #3 — Sharpe-anomaly already half-resolved in Nippon M2: a window artifact) |
| — | Edelweiss Mid Cap | Pending | Not started |
| — | Mahindra Manulife Mid Cap | Pending | Not started |
| — | ICICI Pru Midcap | Pending | Not started |
| — | Sundaram Mid Cap | Pending | Not started |

> **Nippon in one line:** a superb machine on a clock — +2.1%/yr defensive alpha over the investable index for 13.4 years, #1 risk-adjusted metrics of the shortlist at 3–10× peer size, active share 54.1% — discounted for an ungated ₹673 Cr/month AUM trajectory that breaches this study's own ₹50K Cr cap within months, a thrice-changed manager seat, and a live AMC settlement. See [funds/nippon/README.md](funds/nippon/README.md).

> **Invesco in one line:** the best engine on the riskiest chassis — #1 shortlist returns at both horizons, the largest (but episodic, manager-coupled) index alpha, the highest active share studied (79.5%), the best SIP record and cost-capacity position — keyed entirely to one 2.6-year solo manager (Khemani; co-manager Ganatra left for HDFC twelve weeks post-IIHL) running a PE-49 momentum book inside a 2.4/5 AMC. See [funds/invesco/README.md](funds/invesco/README.md).

> **The head-to-head (≈3.97 vs ≈3.96):** a statistical dead heat with opposite shapes — Invesco wins the fund-level modules (M1 returns, M4 cost/runway), Nippon wins the institution-level ones (M2 risk, M3, M5 manager, M6 AMC). R² 90% between them: the midcap slot is single-occupancy, and the decision tree must choose between Nippon's capacity clock and Invesco's key-person trigger.

**Out-of-shortlist instructive candidates:** HDFC Mid Cap (the ₹97,350 Cr capacity case) · Motilal Oswal Midcap (the momentum-blowup case)

---

## Documents

| Document | Purpose |
|----------|---------|
| [study_plan.md](study_plan.md) | Full study strategy — screening pipeline design, 6-module framework with mid-cap adaptations, scoring rubrics, execution phases |
| [screening/methodology.md](screening/methodology.md) | Filter design, data provenance (API pull), mid-cap-specific calibrations, premium-field substitutions |
| [screening/stage1_hard_filters.md](screening/stage1_hard_filters.md) | Stage 1 — 33 → 15; fund-by-fund elimination log |
| [screening/stage2_performance.md](screening/stage2_performance.md) | Stage 2 — 15 → 7; shortlist + per-fund study questions |
| [screening/all_funds_data.md](screening/all_funds_data.md) | Full 33-fund universe data with pass/fail flags |
| decision_tree.md | *(Phase 3)* Cross-fund comparison + deployment strategy + **the sleeve-vs-no-sleeve verdict** |

---

*Category study started: July 2026 | Data: Tickertape API, July 3, 2026 | Framework: 6-Module Weighted Scoring (Mid Cap adaptation) | Screening complete: 33 → 15 → 7 | Portfolio-fit question (Phase 0) deferred by user decision — study first, portfolio later*
