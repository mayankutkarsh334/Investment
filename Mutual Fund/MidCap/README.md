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
| **1** | **Edelweiss Mid Cap** | **≈4.05 / 5** | ✅ **Complete** (6 modules + README) — the **consistency leader**; provisional **#1**, no weak high-weight module |
| 2 | **Invesco India Midcap** | **≈3.97 / 5** | ✅ **Complete** (6 modules + README) — the screening leader; **dead heat with Nippon** for #2 |
| 3 | **Nippon India Growth Mid Cap** | **≈3.96 / 5** | ✅ **Complete** (6 modules + README) — the reference frame |
| 4 | **Mahindra Manulife Mid Cap** | **≈3.83 / 5** | ✅ **Complete** (6 modules + README) — best structure (cost+capacity), weakest warranty (manager+AMC); **the challenger that needs one clean year** |
| 5 | **ICICI Pru Midcap** | **≈3.55 / 5** | ✅ **Complete** (6 modules + README) — manager-better-than-fund; a **skilled active regime-bet at the highest price**; clearly above HSBC, a step below the leaders |
| 6 | **HSBC Midcap** | **≈3.49 / 5** | ✅ **Complete** (6 modules + README) — the recency ramp; **#6**, dominated on M1/M2 |
| — | Sundaram Mid Cap | Pending | Next (study #7) — confirm-elimination |

> **Edelweiss in one line:** the consistency leader — it wins the composite (≈4.05) not by topping any single module but by having **no weak one**: it passes the "why not the index?" test with the group's most *persistent* alpha (+2.87%/yr, positive in every sub-window), runs the trio's **most defensive** risk profile (lowest vol, below-1 beta, a *genuine* 86% down-capture that cushioned the correction HSBC amplified, 7/7 index-dominance), carries the **cheapest ER (0.42%) and best fee-for-alpha of the study**, and is run by the **best-verified manager of the studied midcaps** — Trideep Bhattacharya beats the buyable index in all three Edelweiss funds he runs (+2.6% to +3.2%), disproving the prior "thin-alpha" verdict. Its two honest caveats compound into one watch-item — a **moderate ~55% active share on a fund being flooded** toward the constraint zone (~1.2y), the "quietly becomes the index" risk — and its best pre-2021 years belong to the departed Patwardhan (the fund is the former JPMorgan India Mid & Small Cap). Carries a hidden JPMorgan lineage (2007), a 2018 Mid+Small→Mid mandate change, and the study's best AMC communication (Radhika Gupta). See [funds/edelweiss/README.md](funds/edelweiss/README.md).

> **Nippon in one line:** a superb machine on a clock — +2.1%/yr defensive alpha over the investable index for 13.4 years, #1 risk-adjusted metrics of the shortlist at 3–10× peer size, active share 54.1% — discounted for an ungated ₹673 Cr/month AUM trajectory that breaches this study's own ₹50K Cr cap within months, a thrice-changed manager seat, and a live AMC settlement. See [funds/nippon/README.md](funds/nippon/README.md).

> **Invesco in one line:** the best engine on the riskiest chassis — #1 shortlist returns at both horizons, the largest (but episodic, manager-coupled) index alpha, the highest active share studied (79.5%), the best SIP record and cost-capacity position — keyed entirely to one 2.6-year solo manager (Khemani; co-manager Ganatra left for HDFC twelve weeks post-IIHL) running a PE-49 momentum book inside a 2.4/5 AMC. See [funds/invesco/README.md](funds/invesco/README.md).

> **The standings (6 of 7 studied):** Edelweiss ≈4.05 leads on **balance** — the only fund with no high-weight module below 4.0 *and* the best manager module (3.7). Behind it, Invesco (≈3.97) and Nippon (≈3.96) remain a **statistical dead heat for #2** with opposite shapes — Invesco wins the fund-level modules, Nippon the institution-level ones. **Mahindra Manulife (≈3.83) lands #4** — structure-strong (best capacity runway, subsidized ER, 66.6% AS) but warranty-weak (departed author, 7-month team, loss-making AMC). **ICICI Pru (≈3.55) lands #5** with a fourth distinct shape — **manager-and-book-strong, economics-weak**: a decisively active 73.9% cyclical book run by a verified cross-fund cycle-timer (Lalit Kumar's Business Cycle Fund, positive every year since 2021), but failing the canonical index test (−0.35%/yr) at the study's highest true cost (~1.08%), so its recent turnaround reads as a regime-contingent capex bet you pay top price to own. **HSBC (≈3.49) is #6.** All six are R² ~90–92% correlated: **the midcap slot is single-occupancy** — the decision tree weighs Edelweiss's capacity trajectory vs Invesco's key-person trigger vs Nippon's capacity clock vs MM's manager warranty vs ICICI's cost-and-regime dependence. One fund remains (Sundaram — expected below the leaders, confirm-elimination).

> **Mahindra Manulife in one line:** the "orphaned author, surviving process" fund — a rising matched-index alpha (+2.06→+3.46%/yr, the only improving trajectory studied) earned in a genuinely active (66.6% AS) value-financials book that **omits both exchanges** (the inverse of Edelweiss), on the **best capacity runway of the entire study** (smallest AUM ₹4,866 Cr, gentlest flows, no clock) at a sponsor-subsidized 0.43–0.46% ER — discounted for a record whose author (Manish Lodha, verified +2.09/+7.38/+1.69%/yr across three funds) resigned Dec-2025, a fake NFO-cash 2018 winter, no 10Y history, and a **loss-making AMC** (FY25 −₹10.1 Cr) that lost two senior managers in 14 months. The counterweights: the weak 2025 was Lodha's own final year, the new team swept all three MM funds in its first 7 solo months, Sanghavi (CIO since 2020) supervised the whole record, and the sponsors are deepening (Nov-2025 life-insurance JV — the anti-Invesco). See [funds/mahindra/README.md](funds/mahindra/README.md).

> **HSBC in one line:** the recency ramp — the entire trailing crown (3Y/1Y #1, Sharpe 0.848) is a 2024+2026 spike on a record that **fails the matched-index test** (−0.22%/yr net alpha over the buyable index fund), carries the trio's worst risk-adjusted metrics (Sharpe 6th/7, Calmar below the index fund, deepest drawdown), hides a ~0.76% true cost behind a cheap ER (~110% turnover, the study's highest), and spans **four AMCs and five teams**. Rescued from the low-3s by a distinctive active portfolio, the best (unlimited) capacity of the trio — because "the market isn't buying it" — and a manager (Cheenu Gupta) verifiably **better than the fund** (a good 2020 COVID crisis record the weak legacy predates). Now **#6**, dominated on the two heaviest modules; R² 91% to each. See [funds/hsbc/README.md](funds/hsbc/README.md).

> **ICICI Pru in one line:** manager-better-than-the-fund at the study's highest price — a fund that fails the canonical index test (−0.35%/yr) and carries the highest true cost of the studied midcaps (~1.08%, high ER *and* 75% turnover), yet is run by a verified cross-fund cycle-timer (Lalit Kumar's Business Cycle Fund has beaten the market every year since 2021, +13.2 alpha in 2023 while his midcap lagged −10.4) through a decisively active 73.9% book whose ~46% cyclical thesis — built on the exact two exchanges (BSE + MCX) Mahindra Manulife omits — makes its +5.63%/yr recent turnaround a **regime-contingent capex bet**, not durable selection. Genuine assets (a real fully-invested 2018–19 winter pass, a 20-year 13.6% anchor, the cohort's fastest 2024–25 recovery at 2.6mo, and the deepest institutional backing of the entire study — India's #1 active AMC, a ~56%-margin profit machine, a 19-year-stable CEO) against real liabilities (worst 5Y Sharpe of the shortlist 0.752, the repo's deepest tail −75.1% in 2008, a negative base-case fee bet, and one investor-facing scar — the 2018 ICICI Securities IPO bailout). **#5** — clearly above HSBC on skill and book quality, a full step below the cheaper positive-alpha leaders. See [funds/icici/README.md](funds/icici/README.md).

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
