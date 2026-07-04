# Screening Methodology — Mid Cap Funds

**Context:** ₹20,000/month SIP (working assumption), 10+ year horizon. Fourth category study, following the FlexiCap / SmallCap / International pipeline. Same 2-stage screening with mid-cap-specific calibrations.

**Universe:** 33 Mid Cap Funds (Direct plan figures, Growth option) — data pulled **July 3, 2026** directly from the Tickertape screener API (see Data Provenance below).

> **Note:** The user's portfolio-fit question (Phase 0 of [study_plan.md](../study_plan.md)) is deliberately **deferred** — the current focus is the study itself; portfolio construction comes at decision-tree time.

---

## Data Provenance (differs from prior studies)

Prior studies used manual Tickertape CSV exports. This screening pulled the same fields **directly from the Tickertape screener API** (`api.tickertape.in/mf-screener/query`, subsector = "Mid Cap Fund") on **July 3, 2026**. The raw pull is saved as:

```
Mutual Fund/TickerTape Data/MidCap_Screener_API_03_07_2026.csv
```

**Adjustments made to the raw API result:**

1. **Duplicate removed** — Nippon India Growth Mid Cap appeared twice (two scheme IDs, identical data); deduplicated by name.
2. **Three SIF long-short products excluded** — "iSIF / Qsif / WSIF Equity Ex-Top 100 Long-Short Fund" are Specialized Investment Funds (long-short mandates, ₹10L minimums) that Tickertape files under the Mid Cap subsector. They are not mid-cap mutual funds and are structurally incomparable; excluded from the universe.
3. **Growth plans only** — IDCW/Bonus variants dropped.
4. **Direct-plan figures confirmed** — spot-checked expense ratios against known Direct-plan values.

**Known data caveats:**

| Caveat | Impact |
|--------|--------|
| `ageInMon` caps at **163 months** (~13.6y) | Any fund showing 163 is *at least* 13.6 years old; true inception dates verified per fund in deep study |
| `percMidcap` uses Tickertape's own cap classification, not AMFI's | Some funds show <65% mid cap (e.g. HSBC 51.4%) without being in breach; mandate compliance is checked against AMFI-classified factsheets in Module 3 |
| Premium-gated fields unavailable: max drawdown, 3Y rolling average, returns-vs-sub-category, top-10 concentration, cash % | See substitutions below; all are computed independently in the deep-study modules from MFAPI NAV history (the canonical method in all prior studies anyway) |

**Premium-field substitutions at screening:**

- **"Returns vs sub-category 3Y > 1.0x" (Stage 2)** → computed as *fund 3Y CAGR ÷ universe mean 3Y CAGR* (mean of all 29 funds with non-null 3Y data = **20.27%**). Same economic meaning as Tickertape's ratio.
- **Max drawdown / rolling returns** → not used as filters (consistent with SmallCap methodology, which rejected max-DD screening as inception-biased); studied in Modules 1–2.

---

## Why Mid Cap Screening Differs from the Siblings

### 1. The AUM ceiling is higher than SmallCap's (₹50,000 Cr vs ₹30,000 Cr)

SEBI's mid-cap band (ranks 101–250) contains 150 stocks that are far more liquid than the small-cap ocean. A ₹40,000 Cr mid-cap fund can still execute; a ₹40,000 Cr small-cap fund cannot. But capacity is not unlimited: at ₹97,350 Cr (HDFC), the 65% mandate forces ~₹63,000 Cr into 150 shared names — quasi-index behaviour with active fees. **Threshold: ₹50,000 Cr eliminates HDFC (₹97,350 Cr) and Kotak (₹64,749 Cr).** Both are flagged as instructive-case candidates, not silently discarded.

### 2. The ER ceiling stays at 1.0% — because the passive alternative is investable

Unlike International (passive lane closed) and SmallCap (indices poorly representative), mid cap has an **open, investable Nifty Midcap 150 index fund at ~0.20%**. Every basis point of active fee must buy verified alpha. ER > 1.0% makes that arithmetic nearly impossible. Eliminates Quant (1.10%), BOI (1.07%), LIC (1.13%), Taurus (1.69%), Samco (1.74%).

### 3. Fund age ≥ 60 months, and what it means here

60 months back from July 2026 = July 2021. This guarantees coverage of the **2022 rate-hike correction** and the **Sep 2024 – Mar 2025 midcap correction (~−20%)**, but NOT the **Jan 2018 – Aug 2019 midcap winter** — the category's defining stress event. Funds aged 60–102 months carry a "no-2018-data" flag into Module 1 (the SmallCap Bandhan precedent). Eliminates WhiteOak (47mo), Canara Robeco (44mo), Bandhan (48mo), Helios (17mo), JM (45mo), BOI (12mo), TRUSTMF (5mo), Samco (6mo).

### 4. Sharpe ≥ 0 — and it bites much harder here

In the SmallCap screen this filter removed known laggards. Here it removed **the recent category star**: Motilal Oswal Midcap (₹36,458 Cr, 23.0% 5Y CAGR — the best 5Y in the entire universe) posts a **Sharpe of −0.69**, a 1Y return of **−8.8%**, and alpha of **−4.8%** after its concentrated momentum book unwound in the 2024–25 correction. The filter is doing exactly its job: a fund whose recent risk-adjusted return is deeply below the risk-free rate is un-investable *today*, whatever its trailing CAGR says. Also eliminates SBI (−0.13), Franklin (−0.30), UTI (−0.20), PGIM (−0.22), Quant (−0.21).

---

## Stage 1 — Hard Filters (applied in order)

| Filter | Threshold | Rationale | vs siblings |
|--------|-----------|-----------|-------------|
| Expense Ratio | ≤ 1.0% (Direct) | Active fee must be justifiable vs a 0.20% investable index fund | Same as SmallCap; tighter than FlexiCap (1.5%) |
| AUM minimum | ≥ ₹500 Cr | Operational viability | Same as siblings |
| AUM maximum | ≤ ₹50,000 Cr | 65% mandate across a fixed 150-stock pond; above this, quasi-index behaviour | New calibration (SmallCap: ₹30,000 Cr; FlexiCap: none) |
| Fund age | ≥ 60 months | Covers 2022 + 2024–25 corrections minimum; 2018-winter coverage flagged separately | Same as siblings |
| Sharpe | ≥ 0 | Risk-adjusted return above risk-free | Same as siblings |

**Result: 33 → 15.** See [stage1_hard_filters.md](stage1_hard_filters.md).

---

## Stage 2 — Performance Filters (both must be met)

| Filter | Threshold | Value | Rationale |
|--------|-----------|-------|-----------|
| 5Y CAGR | > full-universe median (strictly) | **17.63%** (n=25 non-null) | Cycle-aware horizon (covers 2021 bull, 2022 correction, 2023–24 rally, 2024–25 correction); full-universe median avoids survivor-inflation |
| 3Y CAGR vs universe mean | > 1.0x | mean = **20.27%** (n=29) | Consistent peer outperformance (computed substitute for Tickertape's premium vs-sub-category ratio) |

**Result: 15 → 7.** See [stage2_performance.md](stage2_performance.md).

---

## Key Screening Decisions

### Why full-universe median (33 funds) and not survivor median?
Same reasoning as SmallCap: Stage 1 disproportionately removes underperformers (five Sharpe-negative funds); a survivor-median would be inflated and less discriminating.

### Why is Motilal Oswal eliminated but HDFC/Kotak get instructive-case status?
HDFC and Kotak fail on a *structural* variable (size) while their fund quality may be intact — the capacity question deserves study. Motilal fails on *current risk-adjusted performance* — its 5Y CAGR (23.0%, best in universe) is a momentum artifact that the 2024–25 correction already partially unwound. It may merit a brief instructive note on momentum-style risk, but it is not a candidate.

### Why not screen on max drawdown?
Unavailable at screening (premium field) — but it would have been rejected anyway, for the SmallCap reason: max DD punishes older funds that lived through 2018 and flatters 2020+ launches. Studied properly in Module 2 with MFAPI-computed drawdowns.

### Borderline cases (documented for honesty)
- **Union Midcap:** passed the 5Y median by 0.10pt (17.73 vs 17.63) but failed the 3Y ratio (0.974x). Out.
- **Baroda BNP Paribas Mid Cap:** its 5Y CAGR (17.63%) *is* the universe median — the strictly-greater rule excludes it; its 3Y ratio (1.046x) passed. The nearest miss in the screen.
- **Mirae Asset Midcap:** 17.43% 5Y, 0.974x 3Y — failed both narrowly. Its 85-month age also means no 2018 data.

---

## What the Filters Cannot Catch (deferred to modules)

1. **Closet indexing** — the category's structural risk (150-stock shared pond). Active share vs Nifty Midcap 150 is a Module 3 first-class metric; no screener field captures it.
2. **The 35% flexible sleeve** — two funds with identical labels can run very different risk (large-cap ballast vs small-cap kicker). Module 3.
3. **Manager tenure vs the track record** — whose 5Y CAGR is it? Module 5.
4. **2018-winter coverage gaps** — Mahindra Manulife (103mo, ~Dec 2017 inception) barely covers it; the 163mo-capped funds fully cover it. Module 1 decomposes per fund.
5. **AMC governance** — five shortlisted AMCs already have verdicts from prior studies (Edelweiss, HSBC, Invesco, Sundaram from FlexiCap/SmallCap; ICICI referenced in International's foundation); carried forward in Module 6.
6. **Alpha vs the investable index fund** — the decisive test (M1 × M4): does the fund beat a 0.20% Nifty Midcap 150 tracker after its fee?

---

*Methodology version: 1.0 | Created: July 3, 2026 | Data: Tickertape screener API, July 3, 2026, Direct Growth | Universe: 33 Mid Cap Funds (after removing 1 duplicate + 3 SIF long-short products)*
