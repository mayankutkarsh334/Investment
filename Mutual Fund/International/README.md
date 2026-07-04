# International Fund Category

## What is an International Fund?

An International (overseas) fund gives an Indian investor exposure to **foreign equities** — US, global-developed, emerging markets, Europe, Asia — usually through one of two structures:
- **Index / passive FoF** — buys a foreign ETF (NASDAQ-100, S&P 500, MSCI World)
- **Active offshore feeder** — invests into an *underlying* foreign mutual fund managed abroad

The Indian fund is a **wrapper**; what you actually own is the underlying foreign portfolio, in rupee terms.

## Why Study International for SIP?

International equity is the **third diversifier sleeve** in a complete portfolio:
- **Geographic diversification** — India is ~3% of global market cap; this owns the other 97%
- **Currency diversification** — rupee depreciation (~3–4%/yr vs USD) is a structural tailwind to INR returns
- **Access to businesses India lacks** — global tech (the Magnificent 7), semiconductors, global brands
- **Low correlation** — foreign markets don't move in lockstep with Nifty, smoothing the blended ride

**Context:** This is the third parallel study. The framework: a **FlexiCap core** (Parag Parikh #1 at 4.20/5), a **SmallCap satellite** (DSP #1 at 4.00/5), and now an **International diversifier** — ₹20,000/month each.

---

## ⚠ The Defining Constraint: The SEBI Overseas Limit

Unlike the domestic studies, the international universe is dominated by one structural fact:

> **The industry-wide overseas investment cap (US $7bn, + $1bn for ETFs) is full.** As of May 2026, **43 of 53** international equity funds are **closed to fresh SIP** — including **every** NASDAQ-100, S&P-500, and MSCI-World **index tracker.**

This is the international equivalent of SmallCap's AUM ceiling. Because closure is concentrated in the passive lane (passive funds buy overseas ETFs and hit the tighter sub-limit), **eliminating closed funds leaves an all-active survivor set.** The cheapest way to own international (passive index funds) is currently un-investable via SIP — a structural disadvantage of this sleeve vs the domestic ones.

**Decision:** this is an **all-active study**. The passive lane is catalogued (see `screening/`) for instant re-screening if the cap resets.

---

## Universe

- **Total international equity funds (May 2026):** 53 (Direct, Growth)
- **After Stage 1 hard filters (open-to-SIP, ≥5Y, ≥₹100 Cr, Sharpe ≥ 0):** 10 (all active)
- **After Stage 2 performance filters:** **8 shortlisted funds**

---

## Data Source

All CSVs are in `Mutual Fund/TickerTape Data/` — exported from **Tickertape** on **May 21, 2026** (shared with the FlexiCap and SmallCap studies). The international-relevant fields: AUM, ER, benchmark, SIP-allowed flag, inception, **tracking error**, max drawdown, Sharpe/Sortino, CAGR 3Y/5Y/10Y, returns vs sub-category, holdings.

---

## Final Shortlist (8 funds)

| # | Fund | Region / Style | AUM (Cr) | ER% | 5Y | 3Y | 10Y | Sharpe | MaxDD | Role |
|---|------|----------------|----------|-----|-----|-----|-----|--------|-------|------|
| 1 | **Franklin US Opportunities** | US large-growth | 4,408 | 0.50 | 13.8% | 25.7% | 17.8% | 1.28 | 38.4% | Core US (cheapest active) |
| 2 | **Edelweiss US Technology** | US tech | 3,897 | 1.48 | 19.0% | 35.3% | — | 1.50 | 45.3% | US growth amplifier |
| 3 | **Edelweiss US Value** | US value | 218 | 1.46 | 14.3% | 19.3% | 14.0% | 2.15 | 34.8% | US style diversifier |
| 4 | **PGIM Global Equity Opp** | Global (MSCI ACWI) | 1,694 | 1.38 | 11.5% | 20.7% | 15.7% | 0.93 | 43.4% | Broad-global core |
| 5 | **PGIM Emerging Markets** | EM | 1,390 | 1.29 | 7.0% | 30.1% | 8.8% | 1.77 | 48.9% | EM growth |
| 6 | **Edelweiss Emerging Markets** | EM | 221 | 1.47 | 10.6% | 28.0% | 13.8% | 2.81 | 38.8% | EM (down-protection) |
| 7 | **Edelweiss Europe Dynamic** | Europe (developed) | 237 | 1.52 | 15.8% | 23.2% | 13.2% | 1.56 | 35.7% | Developed-ex-US diversifier |
| 8 | **Edelweiss India+World Healthcare** | Thematic / defensive | 172 | 0.51 | 13.7% | 22.8% | — | 1.25 | 16.3% | Defensive thematic ⚠️ ~½ India |

> **Eliminated at Stage 2:** Franklin Asian Equity (serial peer-laggard), Edelweiss ASEAN (narrowest mandate, weakest peer-relative).

> **Two structural notes:** (1) **All 8 are active** — no investable passive option exists today. (2) **5 of 8 are Edelweiss offshore feeders** — AMC-concentration risk, the inverse of the broad-AMC spread in the domestic studies; Edelweiss's governance flags from the FlexiCap/SmallCap work apply across most of this sleeve.

---

## Module Framework (weights shared with domestic studies)

| Module | Weight | International adaptation |
|--------|--------|-------------------------|
| 1 — Returns Consistency | 25% | Alpha vs **own** foreign index; **currency decomposition** |
| 2 — Risk Profile | 20% | **Currency risk** + tracking error + down-capture vs own index |
| 4 — Cost & AUM / Structure | 20% | **True all-in = feeder ER + underlying TER**; taxation; closure stability |
| 3 — Portfolio DNA & Look-Through | 15% | **Look through to the underlying fund**; overlap with domestic sleeves |
| 5 — Manager Quality | 15% | **Underlying** manager (the real engine) + feeder operator |
| 6 — AMC Trustworthiness | 5% | Offshore-partner quality; closure conduct; carry-forward AMC findings |

See [study_plan.md](study_plan.md) for the full module design and scoring rubrics.

---

## Deep Study Progress

| Rank | Fund | Score | Status |
|------|------|-------|--------|
| 1 | **Franklin US Opportunities** | **≈3.14 / 5** | ✅ Complete (6 modules + README) |
| — | PGIM Global Equity Opp | Pending | Not started |
| — | Edelweiss US Technology | Pending | Not started |
| — | PGIM Emerging Markets | Pending | Not started |
| — | Edelweiss Emerging Markets | Pending | Not started |
| — | Edelweiss US Value | Pending | Not started |
| — | Edelweiss Europe Dynamic | Pending | Not started |
| — | Edelweiss India+World Healthcare | Pending | Not started |

**Recommended study order** and rationale: see [study_plan.md](study_plan.md) (Franklin US → PGIM Global → Edelweiss Tech → PGIM EM → Edelweiss EM → Edelweiss US Value → Edelweiss Europe → Edelweiss Healthcare).

---

## Documents

| Document | Purpose |
|----------|---------|
| [study_plan.md](study_plan.md) | 6-module framework adapted for international; per-fund study order |
| [screening/methodology.md](screening/methodology.md) | Filter design — why open-to-SIP is the defining filter; international vs domestic differences |
| [screening/stage1_hard_filters.md](screening/stage1_hard_filters.md) | Stage 1 — 53 → 10; the SEBI-cap elimination log |
| [screening/stage2_performance.md](screening/stage2_performance.md) | Stage 2 — 10 → 8; peer-relative (never cross-geography) filtering |
| [screening/all_funds_data.md](screening/all_funds_data.md) | Full 53-fund universe data with per-fund pass/fail flags |
| decision_tree.md | *(to be built after the funds are studied)* — cross-fund comparison + ₹20K deployment strategy |

---

*Category study started: June 2026 | Data: Tickertape, May 21 2026 | Framework: 6-Module Weighted Scoring (International adaptation) | All-active study — passive lane closed by SEBI overseas cap*
