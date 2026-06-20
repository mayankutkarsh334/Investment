# Small Cap Fund Category

## What is a Small Cap Fund?

A Small Cap Fund must invest **minimum 65% in small-cap stocks** — defined by SEBI as the 251st company onwards by market capitalisation. The remaining 35% can be deployed across mid-cap, large-cap, or debt instruments at the manager's discretion.

**SEBI mandate:** Minimum 65% in small-cap equities. No upper limit — some funds run 80%+ in small cap.

## Why Study Small Cap for SIP?

Small cap funds are the highest-risk, highest-reward category in equity mutual funds. Over a 10+ year SIP horizon:
- They deliver the best CAGR in bull markets (outperforming FlexiCap by 3-5% in strong cycles)
- They suffer the deepest drawdowns (40-60% max DD vs 30-42% for FlexiCap)
- They require the longest holding period to smooth out volatility (minimum 7-10 years)
- Manager quality matters disproportionately — small caps have minimal analyst coverage, forcing the fund manager to do original research

**Context:** This is a parallel study alongside the FlexiCap research. The eventual goal is a two-portfolio framework — one FlexiCap SIP (defensive core, consistent compounder) and one Small Cap SIP (aggressive satellite, maximum long-run CAGR).

---

## Universe

- **Total Small Cap funds in India (May 2026):** 36 funds (Direct, Growth plan)
- **After Stage 1 hard filters:** 13 funds
- **After Stage 2 performance filters:** **8 shortlisted funds**

---

## Data Source

All CSV files used for screening are in `Mutual Fund/TickerTape Data/` — exported from **Tickertape** on **May 21, 2026**.

| File | Contents |
|------|----------|
| `Mutual_Funds_Screener_21_05_2026.csv` | AUM, ER, NAV, fund manager, inception, exit load, AMC |
| `Mutual_Funds_Screener_21_05_2026 (1).csv` | Alpha, CAGR 10Y/5Y/3Y, rolling 3Y avg, absolute returns 1Y/6M/3M |
| `Mutual_Funds_Screener_21_05_2026 (2).csv` | Max drawdown, volatility, category St Dev |
| `Mutual_Funds_Screener_21_05_2026 (3).csv` | Sharpe, Sortino, PE ratio, returns vs sub-category (1Y/3Y/5Y/10Y) |
| `Mutual_Funds_Screener_21_05_2026 (4).csv` | % Away from ATH, largecap %, midcap %, top-10 concentration |
| `Mutual_Funds_Screener_21_05_2026 (5).csv` | Smallcap %, equity %, debt %, cash %, top-3/top-5 concentration |

---

## Final Shortlist (8 funds, sorted by 5Y CAGR)

| # | Fund | AUM (Cr) | ER% | 10Y CAGR | 5Y CAGR | 3Y CAGR | Roll 3Y | Sharpe | Max DD |
|---|------|----------|-----|----------|---------|---------|---------|--------|--------|
| 1 | **Bandhan Small Cap** | 25,346 | 0.34 | — | 23.52% | 30.95% | 35.92% | 0.325 | 24.34% |
| 2 | **Invesco India Smallcap** | 11,038 | 0.40 | — | 22.11% | 24.50% | 29.08% | 0.302 | 37.66% |
| 3 | **Bank of India Small Cap** | 1,770 | 0.49 | — | 20.88% | 22.45% | 24.60% | 0.491 | 32.37% |
| 4 | **HSBC Small Cap** | 16,394 | 0.73 | 19.82% | 20.34% | 17.85% | 23.01% | 0.111 | **52.45%** |
| 5 | **Edelweiss Small Cap** | 5,952 | 0.82 | — | 19.80% | 20.12% | 24.12% | 0.265 | 37.09% |
| 6 | **Union Small Cap** | 1,980 | 0.80 | 17.40% | 19.56% | 21.72% | 21.69% | **0.805** | 44.71% |
| 7 | **Sundaram Small Cap** | 3,563 | 0.85 | 16.10% | 19.46% | 21.27% | 23.84% | 0.464 | 57.06% |
| 8 | **DSP Small Cap** | 17,906 | 0.64 | 17.55% | 19.18% | 20.64% | 23.27% | 0.379 | 49.06% |

> **Category St Dev:** 16.00% (all funds are SEBI "Very High" risk)

---

## ⚠ Critical Warning: Inception Bias in Bandhan and Invesco

| Fund | Inception (approx) | Key Period MISSING |
|------|--------------------|--------------------|
| Bandhan Small Cap | ~Jan 2020 | 2018 IL&FS crash + NBFC crisis |
| Invesco India Smallcap | ~Sep 2018 | Partial 2018 crash only |
| Bank of India Small Cap | ~Nov 2018 | Partial 2018 crash only |
| Edelweiss Small Cap | ~Sep 2018 | Partial 2018 crash only |

**The 2018 small cap crash** (Jul 2018–Mar 2019, Nifty SmallCap 250 fell ~45%) is the definitive stress test for this category. Any fund launched after mid-2018 has NO track record through this event. Bandhan's spectacular 23.52% 5Y CAGR covers only the post-COVID bull market (May 2021–May 2026) — one of the strongest bull markets in history. This creates severe survivorship/inception bias. Module 1 must address this explicitly for each fund.

---

## Module Status (All Funds)

| Module | Weight | Status (all funds) |
|--------|--------|--------------------|
| 1 — Returns Consistency | 25% | 6 funds complete |
| 2 — Risk Profile | 20% | 6 funds complete |
| 3 — Portfolio DNA | 15% | 6 funds complete |
| 4 — Cost & AUM Impact | 20% | 6 funds complete |
| 5 — Fund Manager Quality | 15% | 6 funds complete |
| 6 — AMC Trustworthiness | 5% | 6 funds complete |

---

## Deep Study Progress

### Shortlisted Funds (8)

| Rank | Fund | Score | Status |
|------|------|-------|--------|
| 1 | **DSP Small Cap** | **4.00 / 5** | ✅ Complete |
| 2 | **Bank of India Small Cap** | **3.66 / 5** | ✅ Complete |
| 3 | **HSBC Small Cap** | **3.37 / 5** | ✅ Complete |
| 4 | **Bandhan Small Cap** | **3.33 / 5** | ✅ Complete |
| 5 | **Invesco India Smallcap** | **3.29 / 5** | ✅ Complete |
| — | Edelweiss Small Cap | Pending | Not started |
| — | Union Small Cap | Pending | Not started |
| — | Sundaram Small Cap | Pending | Not started |

### Out-of-Shortlist Studies (instructive deep-dives)

| Fund | Score | Stage-1 Elimination Reason | Status |
|------|-------|---------------------------|--------|
| **quant Small Cap** | **2.86 / 5** | AUM ₹31,774 Cr (>₹30,000 Cr cap) | ✅ Complete |

> **quant SC note:** Studied as an instructive case — highest-octane raw returns in the category (VLRT era 5Y CAGR +36%) but confirmed-eliminated on AUM, mandate drift, governance, and data-quality pattern. Score confirms Stage-1 decision: no fund should buy raw alpha at this cost.

---

## Recommended Study Order

| Priority | Fund | Rationale |
|----------|------|-----------|
| 1 | **DSP Small Cap** | Longest credible track record (161 mo = 13+ years); full 10Y CAGR; went through 2018 crash, 2020 COVID, 2022. Builds reference frame for the category. |
| 2 | **Invesco India Smallcap** | Global AMC, strong 22.11% 5Y, AUM in sweet spot (11,038 Cr). Best risk-return combination in shortlist. |
| 3 | **Bandhan Small Cap** | Top returns on paper (23.52%) but inception bias is the critical question. Must scrutinise the Jan 2020 launch date carefully. |
| 4 | **Bank of India Small Cap** | Continuation of BOI AMC thesis from FlexiCap study. Small AUM (₹1,770 Cr), key-man risk same concern. |
| 5 | **HSBC Small Cap** | Continuation of HSBC AMC thesis from FlexiCap. Highest MaxDD (52.45%) is alarming — must understand why. ER concern same. |
| 6 | **Edelweiss Small Cap** | Continuation of Edelweiss AMC thesis. AMC governance flag same. |
| 7 | **Union Small Cap** | Best Sharpe (0.805) in the shortlist; small AUM; 10Y data available. Counter-intuitive combination: high Sharpe + small cap needs explanation. |
| 8 | **Sundaram Small Cap** | Worst MaxDD (57.06%) in shortlist; 10Y CAGR lowest (16.10%). Likely lower-ranked but study confirms or refutes. |

---

## Comparative Analysis & Strategy

| Document | Purpose |
|----------|---------|
| [decision_tree.md](decision_tree.md) | **Cross-fund comparative analysis + defined ₹20K/month deployment strategy** — scorecard, deep-metric grid, hard filters, decision tree, portfolio construction (recommended: DSP 60% + BOI 40%) |

## Screening Documents

| Document | Purpose |
|----------|---------|
| [screening/methodology.md](screening/methodology.md) | Filter design rationale — why each filter was chosen, small-cap-specific differences from FlexiCap |
| [screening/stage1_hard_filters.md](screening/stage1_hard_filters.md) | Stage 1 results — 36 → 13, fund-by-fund elimination log |
| [screening/stage2_performance.md](screening/stage2_performance.md) | Stage 2 results — 13 → 8, performance filter results and shortlist |

---

*Category study started: May 2026 | Data: Tickertape, May 21 2026 | Framework: 6-Module Weighted Scoring (adapted for Small Cap)*
