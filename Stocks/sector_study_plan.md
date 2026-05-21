# Sector Deep Study Plan

## Purpose

Before screening individual stocks, we need to determine **which sectors are worth investing in right now** for momentum/swing trades. This is the equivalent of choosing "FlexiCap" as the fund category in the mutual fund study — except here we study all 13 sectors and rank them.

A sector that is structurally weak, in a cyclical downturn, or facing policy headwinds will drag even the best stock in it. Conversely, a rising sector lifts mediocre stocks. For momentum trading, **sector selection is arguably more important than stock selection**.

---

## Study Structure

Each sector goes through **5 phases** of study. Phases 1–3 are done for all 13 sectors. Phases 4–5 produce the final ranking and selection.

| Phase | Name | Data Source | Output |
|-------|------|-------------|--------|
| 1 | Sector Identity & Structure | Web research | Understand what the sector does, what drives it |
| 2 | Quantitative Health Check | Tickertape CSVs | Numbers-driven snapshot of current sector state |
| 3 | Macro, Policy & Cycle Analysis | Web research | External forces acting on the sector right now |
| 4 | Sector Scorecard | Phases 1–3 combined | Score each sector 1–5 on 8 dimensions |
| 5 | Comparative Ranking & Selection | All 13 scorecards | Rank sectors, pick top 3–4 to proceed with stock screening |

---

## Phase 1 — Sector Identity & Structure

**Objective:** Build a mental model of the sector before looking at any numbers. Understand its DNA — what makes it tick, what kills it, what drives cycles.

**Data source:** Entirely web research (no CSV data needed)

### 1.1 — Sector Overview

| Question | What to Document |
|----------|-----------------|
| What does this sector produce/do? | Core business activity in 1–2 sentences |
| Revenue model | How do companies in this sector make money? (e.g., interest spread for banks, subscription for SaaS, project-based for infra) |
| Domestic vs export split | Is revenue primarily India-driven or global? (affects currency, global demand sensitivity) |
| Customer type | B2B, B2C, or B2G (government)? Affects order visibility and payment cycles |
| Capital intensity | High (infra, energy) vs low (IT, FMCG)? Affects ROE, debt levels, capex cycles |

### 1.2 — Sector Structure

| Question | What to Document |
|----------|-----------------|
| Key players | Top 5–7 companies by market cap (these set the sector tone) |
| Concentration | Is the sector dominated by 2–3 giants or fragmented across 50+ players? |
| Sub-sector diversity | Are sub-sectors homogeneous (e.g., cement) or varied (e.g., BFSI has banks, insurance, AMCs)? |
| Entry barriers | High (banking licenses, spectrum) vs low (textiles, trading)? |
| Regulatory body | Who regulates this sector? (RBI for banks, SEBI for markets, TRAI for telecom, etc.) |

### 1.3 — Key Drivers (what moves this sector)

| Driver Category | Examples |
|----------------|----------|
| **Macro drivers** | GDP growth, interest rates, inflation, currency, global commodity prices |
| **Policy drivers** | Government schemes (PLI, housing push, defense indigenization), tax changes, regulatory shifts |
| **Demand drivers** | Demographics, urbanization, per-capita income, seasonal patterns |
| **Supply drivers** | Capacity utilization, capex cycles, raw material availability |
| **Global linkage** | Export dependency, foreign competition, global cycle correlation |

### 1.4 — Cyclical vs Defensive Classification

| Type | Characteristics | Examples |
|------|----------------|----------|
| **Cyclical** | Revenue swings with economic cycle; high beta; big moves in both directions | Metals, Real Estate, Autos, Capital Goods |
| **Defensive** | Stable demand regardless of cycle; low beta; steady but smaller moves | FMCG, Pharma, IT (partially) |
| **Interest-rate sensitive** | Directly impacted by RBI rate decisions | Banking, Real Estate, Autos (financing) |
| **Commodity-linked** | Revenue/margins driven by commodity prices | Energy, Metals, Chemicals |
| **Policy-driven** | Government spending/regulation is the primary demand driver | Defense, Infrastructure, Renewable Energy |

> **Why this matters for momentum:** Cyclical sectors in an upswing offer the strongest momentum trades. Defensive sectors offer steadier but smaller moves. Knowing the type helps set expectations for Module 1 (Momentum) and Module 2 (Risk) scoring at the stock level.

---

## Phase 2 — Quantitative Health Check

**Objective:** Score the sector's current health using hard numbers from Tickertape CSVs. This is the data-driven complement to Phase 1's qualitative understanding.

**Data source:** All calculations aggregated at the sector level from the 17 CSV files.

### 2.1 — Momentum & Returns (sector-level)

All metrics computed as **sector median** (more robust than mean for skewed distributions).

| Metric | Source | What to Compute |
|--------|--------|-----------------|
| Sector 1Y Return (median) | File (6) | Median 1Y return of all stocks in sector |
| Sector 1Y Return vs Nifty | Computed | Sector median 1Y return minus Nifty 1Y return (alpha) |
| Sector 6M Return (median) | File (6) | Recent momentum direction |
| Sector 1M Return (median) | File (6) | Very recent momentum (are flows accelerating or fading?) |
| Momentum Rank (median) | File (7) | Tickertape's composite momentum percentile |
| % of stocks positive 1Y | File (6) | Breadth — what fraction of the sector is participating in the move? |
| Sector 5Y CAGR (median) | File (6) | Long-term sector trajectory |

### 2.2 — Breadth & Trend Health

| Metric | Source | What to Compute |
|--------|--------|-----------------|
| % stocks above 200D SMA | File (10), (11) | Structural uptrend breadth — > 60% = healthy; < 40% = weak |
| % stocks above 50D SMA | File (10), (11) | Short-term breadth — divergence from 200D SMA shows momentum shift |
| % stocks with RSI > 50 | File (9) | How many stocks have bullish RSI |
| % stocks with SuperTrend Buy | File (10) | Confirmation of broad-based trend |
| % stocks within 10% of 52W High | File (6) | How many stocks are near their peak (sector-wide strength) |
| % stocks within 10% of 52W Low | File (6) | How many are near their bottom (sector-wide weakness) |

### 2.3 — Institutional Flow (sector-level)

| Metric | Source | What to Compute |
|--------|--------|-----------------|
| Avg FII 3M holding change | File (4) | Are foreign institutions buying or selling this sector? |
| Avg DII 3M holding change | File (4) | Are domestic institutions accumulating? |
| Avg MF 3M holding change | File (4) | Mutual fund flows into sector |
| Avg Promoter 3M holding change | File (4) | Are insiders buying their own sector? |
| % stocks with net institutional buying (FII+DII > 0) | File (4) | Breadth of institutional interest |

### 2.4 — Profitability & Quality (sector-level)

| Metric | Source | What to Compute |
|--------|--------|-----------------|
| Median ROE | Base file | Sector profitability baseline |
| Median ROCE | Base file | Capital efficiency |
| Median Net Profit Margin | Base file | How much revenue converts to profit |
| Median Debt/Equity | File (7) | Sector leverage level |
| Median Fundamental Score | File (7) | Tickertape's composite quality (1–10) |
| Median Earnings Quality Rank | File (7) | Earnings sustainability |
| % stocks with ROE > 15% | Base file | What fraction of sector is "good quality" |

### 2.5 — Valuation (sector-level)

| Metric | Source | What to Compute |
|--------|--------|-----------------|
| Median PE Ratio | File (2) | Is the sector cheap or expensive? |
| Median PB Ratio | File (2) | Price relative to book value |
| Median EV/EBITDA | File (2) | Enterprise-level valuation |
| Median Dividend Yield | File (2) | Income return component |
| Median Price to Intrinsic Value Rank | File (7) | Tickertape's undervaluation signal |

### 2.6 — Growth Trajectory (sector-level)

| Metric | Source | What to Compute |
|--------|--------|-----------------|
| Median 5Y Revenue CAGR | File (1) | Long-term growth track |
| Median 1Y Historical Revenue Growth | File (1) | Recent revenue momentum |
| Median 1Y Forward Revenue Growth | File (1) | Analyst expectations (for ~940 covered stocks) |
| Median 1Y Forward EPS Growth | File (1) | Earnings acceleration signal |
| % stocks with positive forward EPS growth | File (1) | How broad is the growth expectation |
| Median Revenue (Q) trend | File (16) | Most recent quarterly direction |

### 2.7 — Risk Profile (sector-level)

| Metric | Source | What to Compute |
|--------|--------|-----------------|
| Median Volatility (200D) | File (9) | How volatile is this sector? |
| Median Beta | File (9) | Sector sensitivity to market |
| Median Sharpe Ratio | File (10) | Risk-adjusted return |
| Median 1Y Max Loss | File (11) | Worst drawdown in the sector |
| % stocks with Sharpe > 0 | File (10) | What fraction generates risk-adjusted returns |

### 2.8 — F&O Liquidity (sector-level)

| Metric | Source | What to Compute |
|--------|--------|-----------------|
| # of F&O stocks in sector | File (5) | Tradability — more F&O stocks = more liquid sector for swing trades |
| Aggregate Futures OI | File (5) | Total money positioned in sector derivatives |
| Avg Put-Call Ratio | File (5) | Sector-level sentiment |
| Avg Futures Basis | File (5) | Sector-level expectations (premium = bullish) |

---

## Phase 3 — Macro, Policy & Cycle Analysis

**Objective:** Understand the external forces acting on the sector right now. A sector can have great numbers (Phase 2) but be heading into a policy headwind or commodity downturn.

**Data source:** Entirely web research.

### 3.1 — Current Macro Environment

| Factor | What to Research | Source |
|--------|-----------------|--------|
| GDP growth outlook | Is India's GDP accelerating or slowing? Which sectors benefit? | RBI MPC minutes, IMF/World Bank forecasts |
| Interest rate trajectory | Is RBI cutting, holding, or hiking? | RBI monetary policy statement |
| Inflation trend | CPI/WPI direction — impacts margins and consumer demand | MOSPI data, RBI inflation projections |
| Currency (INR/USD) | Weakening INR helps exporters (IT, Pharma); hurts importers (Oil, Chemicals) | RBI reference rate, forex market |
| Global growth | US/EU/China growth affects export sectors | IMF WEO, OECD forecasts |
| Commodity cycle | Oil, metals, agri commodity price trends | Bloomberg Commodity Index, specific commodity charts |

### 3.2 — Sector-Specific Policy & Regulation

| Factor | What to Research | Source |
|--------|-----------------|--------|
| Government schemes | PLI (Production Linked Incentive), housing push, defense indigenization, green energy targets | Union Budget, Ministry press releases |
| Tax changes | GST rate changes, corporate tax cuts, import/export duties | Finance Ministry, CBIC |
| Regulatory shifts | New regulations, deregulation, licensing changes | Sector regulator websites (RBI, SEBI, TRAI, CERC, etc.) |
| FDI policy | FDI limit changes, ease of investment | DPIIT press notes |
| Subsidy / support | Fertilizer subsidies, KUSUM for solar, FAME for EVs | Ministry websites |

### 3.3 — Sector Cycle Position

Every sector moves through a cycle. Knowing where it is determines whether momentum is likely to continue or reverse.

| Cycle Stage | Characteristics | Momentum Implication |
|-------------|----------------|---------------------|
| **Early Recovery** | Beaten-down sector starting to turn; improving order books; contrarian buy signals | Highest momentum potential; stocks can 2-3x from bottom |
| **Mid-Cycle Growth** | Revenue and earnings growing; capacity expansion underway; institutional buying | Strong sustained momentum; best risk/reward for swing trades |
| **Late Cycle / Peak** | Record earnings; full capacity; euphoric valuations; everyone talking about it | Momentum still present but fading; risk of sharp reversal |
| **Downturn** | Falling demand; margin compression; debt stress; institutional selling | Avoid for momentum trades; even strong stocks in this sector will underperform |

For each sector, determine:
| Question | How to Assess |
|----------|--------------|
| Where is the sector in its cycle? | Compare current ROE/margins vs 5Y avg; capacity utilization data; order book growth |
| Is the cycle accelerating or decelerating? | QoQ revenue trend, forward estimates vs historical growth |
| What could trigger the next phase shift? | Policy change, commodity price move, demand shock, global event |
| How long has the current phase lasted? | Duration of outperformance/underperformance vs Nifty |

### 3.4 — Global Peer Comparison

| Question | What to Research | Source |
|----------|-----------------|--------|
| How is this sector performing globally? | Compare India sector returns vs US/global equivalents | Sector ETFs (XLF, XLK, XLV, etc.) vs Nifty sectoral indices |
| Is India outperforming or underperforming global peers? | India premium/discount | Nifty Bank vs BKX, Nifty IT vs NASDAQ, etc. |
| Any global sector rotation underway? | Are global funds moving into or out of this sector? | FII flow data, EPFR fund flow reports |

### 3.5 — Sector-Specific Risks

| Risk Type | What to Document |
|-----------|-----------------|
| **Regulatory risk** | Upcoming policy changes that could hurt (e.g., price caps, windfall taxes) |
| **Commodity risk** | Input cost spikes that compress margins (e.g., crude for chemicals, coal for power) |
| **Competition risk** | New entrants, Chinese dumping, import substitution threats |
| **Technology disruption** | EV transition (autos), digital lending (banks), AI (IT services) |
| **Geopolitical risk** | Trade wars, sanctions, supply chain disruptions affecting the sector |
| **Liquidity risk** | Thin trading, low F&O coverage, circuit-prone stocks dominating the sector |

---

## Phase 4 — Sector Scorecard

**Objective:** Convert Phase 1–3 findings into a structured score for each sector. Score each sector 1–5 on 8 dimensions.

### Scoring Dimensions

| # | Dimension | Weight | What it Measures | Inputs From |
|---|-----------|--------|-----------------|-------------|
| 1 | **Momentum & Returns** | 20% | Is this sector outperforming the market? | Phase 2.1 |
| 2 | **Breadth & Trend Health** | 15% | Is the move broad-based or narrow? | Phase 2.2 |
| 3 | **Institutional Flow** | 15% | Is smart money buying this sector? | Phase 2.3 |
| 4 | **Growth Trajectory** | 15% | Are revenues and earnings accelerating? | Phase 2.6 |
| 5 | **Profitability & Quality** | 10% | Is the sector fundamentally sound? | Phase 2.4 |
| 6 | **Cycle Position** | 10% | Is the sector in early/mid-cycle (good) or late/downturn (bad)? | Phase 3.3 |
| 7 | **Policy & Macro Tailwind** | 10% | Are external forces helping or hurting? | Phase 3.1, 3.2 |
| 8 | **Risk Assessment** | 5% | Are there red flags that could derail momentum? | Phase 3.5 |
| | **Total** | **100%** | | |

### Scoring Rubric

| Score | Meaning | Guidance |
|-------|---------|---------|
| 5 | Excellent | Top 2–3 sectors on this dimension; clear outperformance |
| 4 | Good | Above average; favorable conditions |
| 3 | Average | In line with market; no strong signal either way |
| 2 | Below Average | Underperforming or facing headwinds |
| 1 | Poor | Significant weakness; avoid for momentum trades |

### Scorecard Template

| Dimension | Weight | Score (1–5) | Weighted | Key Evidence |
|-----------|--------|-------------|----------|-------------|
| Momentum & Returns | 20% | — | — | — |
| Breadth & Trend Health | 15% | — | — | — |
| Institutional Flow | 15% | — | — | — |
| Growth Trajectory | 15% | — | — | — |
| Profitability & Quality | 10% | — | — | — |
| Cycle Position | 10% | — | — | — |
| Policy & Macro Tailwind | 10% | — | — | — |
| Risk Assessment | 5% | — | — | — |
| **Total** | **100%** | — | **—/5.00** | — |

---

## Phase 5 — Comparative Ranking & Selection

**Objective:** Put all 13 sector scorecards side by side, rank them, and select the top sectors to proceed with individual stock screening.

### 5.1 — Master Ranking Table

| Rank | Sector | Momentum | Breadth | Inst. Flow | Growth | Quality | Cycle | Policy | Risk | **Weighted Total** |
|------|--------|----------|---------|------------|--------|---------|-------|--------|------|--------------------|
| 1 | — | — | — | — | — | — | — | — | — | —/5.00 |
| 2 | — | — | — | — | — | — | — | — | — | —/5.00 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 13 | — | — | — | — | — | — | — | — | — | —/5.00 |

### 5.2 — Selection Criteria

| Rule | Threshold |
|------|-----------|
| **Auto-select** (proceed to stock screening) | Weighted total >= 3.50 |
| **Borderline** (review case-by-case) | Weighted total 2.50 – 3.49 |
| **Auto-reject** (skip for this cycle) | Weighted total < 2.50 |
| **Maximum sectors to study** | Top 4–5 (to keep the project manageable) |
| **Minimum momentum score** | Dimension 1 score must be >= 3 (a sector with weak momentum is not worth studying for swing trades regardless of other scores) |

### 5.3 — Sector Comparison Visualizations

For the final ranking, create:
1. **Radar chart** (mermaid) — overlay top 3–4 sectors on 8 dimensions
2. **Sector heatmap** — 13 rows x 8 columns, color-coded by score
3. **Momentum vs Quality scatter** — X-axis: Dimension 5 (quality), Y-axis: Dimension 1 (momentum) — top-right quadrant = best sectors

### 5.4 — Decision Documentation

For each sector, document:
| Item | Content |
|------|---------|
| **Verdict** | Selected / Borderline / Rejected |
| **One-line rationale** | e.g., "Strong momentum + institutional buying + early cycle = proceed" |
| **Key strength** | The 1–2 dimensions that make this sector attractive |
| **Key risk** | The 1–2 dimensions that could hurt |
| **Study priority** | If selected, what order to study it in (1st, 2nd, 3rd...) |

---

## Folder Structure for Sector Study

```
Stocks/
├── sector_study_plan.md             ← THIS FILE
├── sector_overview.md               ← Updated with final ranking after Phase 5
├── Sector Studies/
│   ├── 01_Banking/
│   │   ├── phase1_identity.md
│   │   ├── phase2_quantitative.md
│   │   ├── phase3_macro.md
│   │   └── scorecard.md
│   ├── 02_IT/
│   │   ├── phase1_identity.md
│   │   ├── phase2_quantitative.md
│   │   ├── phase3_macro.md
│   │   └── scorecard.md
│   ├── ... (one folder per sector)
│   ├── 13_Telecom_Media/
│   │   └── ...
│   └── comparative_ranking.md       ← Phase 5 output: final ranking + selection
```

---

## Execution Order

| Step | Action | Scope | Output |
|------|--------|-------|--------|
| 1 | Phase 2 for all 13 sectors | CSV analysis (automated) | `phase2_quantitative.md` for each sector |
| 2 | Phase 1 for all 13 sectors | Web research | `phase1_identity.md` for each sector |
| 3 | Phase 3 for all 13 sectors | Web research | `phase3_macro.md` for each sector |
| 4 | Phase 4 for all 13 sectors | Combine phases 1–3 | `scorecard.md` for each sector |
| 5 | Phase 5 comparative ranking | All scorecards | `comparative_ranking.md` + updated `sector_overview.md` |
| 6 | Proceed to stock screening | Top-ranked sectors only | Per the existing `study_plan.md` framework |

> **Why Phase 2 first:** The quantitative health check from CSVs is fastest (fully automated). It gives us an initial signal of which sectors are strong/weak before we invest time in web research for Phases 1 and 3. If a sector scores very poorly on Phase 2, we can do a lighter Phase 1 and 3 for it (just enough to confirm it should be rejected).

---

## Relationship to Other Documents

| Document | Role |
|----------|------|
| **sector_study_plan.md** (this file) | How to study and rank sectors |
| **sector_overview.md** | Sub-sector mapping + final ranking table (populated after Phase 5) |
| **study_plan.md** | How to study individual stocks within a selected sector (used after sector selection) |
| **plan.md** | Master framework connecting everything |

---

*Created: 2026-05-21 | Purpose: Determine which sectors to invest in before individual stock screening begins*
