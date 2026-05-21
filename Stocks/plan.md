# Stock Research Framework

## Goal

Select the best momentum stocks per sector for **swing trades**, using the same structured screening + deep study approach as the mutual fund research.

**Mapping from mutual fund framework:**
| Mutual Fund | Stocks |
|-------------|--------|
| Fund category (FlexiCap) | Sector (e.g., Banking, IT) |
| Individual fund | Individual stock |
| 46 funds in category | All stocks in sector (~50–500) |
| 2-stage screening → 9 shortlisted | 2-stage screening → 5–12 shortlisted |
| 6-module deep study per fund | 6-module deep study per stock |
| Weighted score → final pick | Weighted score → final pick |

---

## Data Source

17 CSV files exported from **Tickertape** on **May 21, 2026**, covering **5,749 stocks**.

| File | Contents |
|------|----------|
| Base file | Name, Ticker, Sub-Sector, Market Cap, ROE, ROCE, Margins, ROA, ROI (profitability) |
| File (1) | Revenue/EBITDA/EPS/OCF growth — 1Y forward, 1Y historical, 5Y historical |
| File (2) | PE, PB, PS, EV/EBITDA, EV/EBIT, Dividend Yield, premiums vs sector/sub-sector |
| File (3) | Enterprise Value, EV/FCF, Price/CFO, TTM PE, sub-sector premiums |
| File (4) | Ownership: Promoter/FII/DII/MF holdings + 3M/6M changes, insider trades, bulk deals, pledging |
| File (5) | Derivatives: Futures OI/volume/basis, Options PCR/OI strikes/changes |
| File (6) | Price & returns: 1D/1W/1M/6M/1Y returns (abs + vs Nifty), 5Y CAGR, 52W high/low, volume |
| File (7) | Balance sheet ratios + Tickertape scores: Current/Quick ratio, D/E, turnover ratios, Fundamental Score, Earnings Quality Rank, Momentum Rank |
| File (8) | Analyst recommendations: % Buy/Sell/Hold, % Upside, analyst count |
| File (10) | Technicals: SMA, MACD, RSI, Bollinger, SuperTrend, Stochastic, Alpha, Volatility, Sharpe |
| File (12) | Cash flow & balance sheet: Operating/Investing/Financing CF, PP&E, CapEx, Liabilities |
| File (15) | Income statement: Revenue, EBITDA, PBIT, PBT, Net Income, EPS, DPS, cost breakdown |

**Reliability:** Tickertape data sourced from AMFI/exchanges — reliable for screening and relative comparison. Cross-verify on Trendlyne/Screener.in before final trade decisions.

---

## The 13 Macro-Sectors

163 Tickertape sub-sectors grouped into 13 macro-sectors for study:

| # | Sector | Key Sub-Sectors | Approx. Stocks |
|---|--------|-----------------|----------------|
| 1 | **Banking & Financial Services** | Private Banks, Public Banks, Consumer Finance, Insurance, AMC, Payment Infrastructure, Home Financing, Investment Banking, Stock Exchanges | ~200 |
| 2 | **Information Technology** | IT Services, Software Services, Application Software, Data Processing, IT Consulting | ~150 |
| 3 | **Pharma & Healthcare** | Pharmaceuticals, API, Hospitals, Diagnostics, Healthcare Services | ~220 |
| 4 | **Energy** | Oil & Gas (Refining, E&P, Storage), Coal Mining, Gas Distribution, Renewable Energy, Power Gen/Transmission/Distribution | ~180 |
| 5 | **Metals & Mining** | Steel, Iron & Steel, Aluminum, Copper, Diversified Metals, Precious Metals, Gold, Silver | ~120 |
| 6 | **FMCG & Consumer Staples** | FMCG Foods, Household Products, Personal Products, Tobacco, Beverages (Soft Drinks, Alcoholic, Tea & Coffee) | ~180 |
| 7 | **Automobiles** | Four Wheelers, Two Wheelers, Three Wheelers, Trucks & Buses, Tractors, Auto Parts, Agricultural Machinery | ~130 |
| 8 | **Capital Goods & Defense** | Heavy Machinery, Industrial Machinery, Electrical Components, Electronic Equipment, Aerospace & Defense, Batteries | ~160 |
| 9 | **Chemicals & Specialty** | Commodity Chemicals, Diversified Chemicals, Specialty Chemicals, Agrochemicals, Fertilizers | ~130 |
| 10 | **Infrastructure & Real Estate** | Real Estate Development, Ports, Airports, Roads, Rail, Logistics, Dredging | ~150 |
| 11 | **Consumer Discretionary** | Apparel & Accessories, Footwear, Retail (Food/General/Jewellery), Hotels/Resorts, Restaurants, Home Electronics, Housewares | ~200 |
| 12 | **Cement & Building Materials** | Cement, Paints, Building Products, Sanitary Ware, Pipes, Tiles | ~80 |
| 13 | **Telecom & Media** | Telecom Services, OTT/Broadcasting, Publishing, Printing | ~60 |

---

## Sector Selection Criteria (which sector to study first)

Before picking a sector, rank all 13 by current momentum using four signals from Tickertape CSV data:

| Signal | Source | Weight | What it captures |
|--------|--------|--------|-----------------|
| **Relative Return** | File (6): avg 1Y return of sector stocks vs Nifty 1Y | **40%** | Which sector is outperforming the market |
| **Breadth** | File (10): % of stocks in sector with Price > 200D SMA | **25%** | Wide participation vs narrow rally |
| **Institutional Flow** | File (4): avg (FII + DII) 3M holding change in sector | **20%** | Smart money direction |
| **Momentum Rank** | File (7): median Price Momentum Rank (percentile 0–100) | **15%** | Tickertape's composite momentum signal |

Sectors scoring highest on the weighted composite are studied first. This ranking is documented in `sector_overview.md` once computed.

---

## Screening Pipeline (per sector)

### Stage 1 — Hard Filters

Eliminate stocks that are unsuitable for swing trading regardless of returns.

| Filter | Threshold | Rationale |
|--------|-----------|-----------|
| Market Cap | >= 5,000 Cr | Liquidity for entry/exit without slippage |
| Avg Daily Volume (3M) | >= 50 Cr traded/day | Sufficient daily turnover to absorb trades |
| Sharpe Ratio | > 0 | Generating returns above risk-free rate |
| Listing Age | > 3 years | Minimum track record across at least 1 market cycle |
| Price | > 20 | Avoid penny stocks (manipulation/circuit risk) |

**Expected reduction:** ~60–70% of sector eliminated (similar to MF Stage 1: 46 -> 17)

### Stage 2 — Momentum Quality Gates

All three criteria must pass:

| Filter | Threshold | Rationale |
|--------|-----------|-----------|
| 1Y Return | > sector median | Must outperform sector peers over key horizon |
| Price vs 200D SMA | Price > 200D SMA | In a structural uptrend |
| Price Momentum Rank | > 60th percentile (NSE-wide) | Top 40% momentum across entire market |

**Target shortlist:** 5–12 stocks per sector for deep study

---

## 6-Module Deep Study Framework

Each shortlisted stock is scored 1–5 on six modules. Weighted total determines final ranking within the sector.

| Module | Focus | Weight |
|--------|-------|--------|
| 1 — Momentum & Returns | Price performance across horizons vs sector + Nifty | **25%** |
| 2 — Risk Profile | Volatility, drawdown, beta, Sharpe | **20%** |
| 3 — Technical Setup | RSI, SMA crossovers, MACD, SuperTrend, volume | **20%** |
| 4 — Business Fundamentals | ROE, ROCE, margins, debt, earnings quality | **15%** |
| 5 — Valuation | PE/PB/EV-EBITDA vs sector, FCF yield | **15%** |
| 6 — Promoter & Governance | Promoter holding, pledging, institutional flows, insider trades | **5%** |

**Scoring rubric:** 1 = Poor, 2 = Below Average, 3 = Average, 4 = Good, 5 = Excellent

---

### Module 1 — Momentum & Returns (25%)

| Metric | Source | What to look for |
|--------|--------|-----------------|
| 1D / 1W / 1M / 6M / 1Y return | File (6) | Positive across multiple horizons = sustained momentum |
| 1M / 6M / 1Y return vs Nifty | File (6) | Positive alpha = outperforming market |
| 5Y CAGR | File (6) | Long-term growth durability |
| Price Momentum Rank | File (7) | > 70th percentile = strong momentum |
| % from 52W High | File (6) | < 10% = near peak, strong trend |
| Consistency | Computed | How many of 1M/6M/1Y periods are positive vs sector peers |

---

### Module 2 — Risk Profile (20%)

| Metric | Source | What to look for |
|--------|--------|-----------------|
| Volatility (200D annualized) | File (10) | Lower = smoother ride, better risk/reward |
| Volatility vs Nifty | File (10) | Relative riskiness vs benchmark |
| Beta | File (10) | < 1 = defensive; > 1 = aggressive (context-dependent) |
| Sharpe Ratio (2Y) | File (10) | > 1 = good risk-adjusted return |
| 1Y Max Loss | File (10) | Deepest drawdown — can you hold through it? |
| % from 52W Low | File (6) | Higher = more buffer above floor |

---

### Module 3 — Technical Setup (20%)

| Metric | Source | What to look for |
|--------|--------|-----------------|
| Price vs SMA-50 / SMA-200 | File (10) | Price > SMA50 > SMA200 = golden cross (bullish) |
| RSI-14D | File (10) | 50–70 = momentum without overbought; > 70 = caution |
| MACD (Trend + Signal) | File (10) | Positive MACD + above signal = bullish |
| SuperTrend | File (10) | Buy signal = bullish confirmation |
| ADX Rating | File (10) | > 25 = trending; > 40 = strong trend |
| Relative Volume | File (6) | > 1 = volume expanding (participation increasing) |
| Stochastic %D | File (10) | Confirmation of momentum direction |
| Bollinger Band position | File (10) | Near upper band + expanding = breakout |

---

### Module 4 — Business Fundamentals (15%)

| Metric | Source | What to look for |
|--------|--------|-----------------|
| ROE + 5Y Avg ROE | Base file | > 15% = good; consistency matters |
| ROCE | Base file | > 15% = efficient capital use |
| Net Profit Margin + 5Y Avg | Base file | Positive and stable/growing |
| Debt to Equity | File (7) | < 1 preferred (sector-dependent) |
| 5Y Revenue CAGR | File (1) | > 10% = durable growth |
| Earnings Quality Rank | File (7) | Higher percentile = sustainable earnings |
| Fundamental Score | File (7) | Tickertape composite (1–10); > 6 = good |

---

### Module 5 — Valuation (15%)

| Metric | Source | What to look for |
|--------|--------|-----------------|
| PE Ratio vs Sub-sector avg | File (2) | At or below sector = fair/cheap; well above = expensive |
| PB Ratio vs Sub-sector avg | File (2) | Context-dependent (high PB acceptable if ROE justifies) |
| EV/EBITDA | File (2) | Lower = cheaper on enterprise basis |
| Dividend Yield vs sector | File (2) | Higher = margin of safety (less important for momentum) |
| Price/Free Cash Flow | File (2) | Lower = more cash generation per rupee of price |
| Price to Intrinsic Value Rank | File (7) | Lower percentile = more undervalued |

---

### Module 6 — Promoter & Governance (5%)

| Metric | Source | What to look for |
|--------|--------|-----------------|
| Promoter Holding % | File (4) | > 50% = high alignment; < 25% = weak control |
| Pledged Promoter Holding % | File (4) | > 20% = red flag (forced selling risk) |
| Promoter Holding Change 3M + 6M | File (4) | Increasing = positive; decreasing = warning |
| FII 3M Change + DII 3M Change | File (4) | Institutional buying = tailwind |
| % Buy Recommendations | File (8) | > 60% = strong analyst consensus |
| Insider Trades 3M cumulative | File (4) | Net buying = management confidence |

---

## Folder Structure

```
Stocks/
├── plan.md                          ← THIS FILE — master framework
├── README.md                        ← overall goal + study progress tracker
├── sector_study_plan.md             ← 5-phase sector deep study framework
├── sector_overview.md               ← 13 sectors + sub-sector mapping + final ranking
├── study_plan.md                    ← 6-module stock deep study framework
├── tickertape_screener_filters.md   ← already exists (200+ filter reference)
├── Gemini/                          ← already exists (screener.py, backtest.py)
├── Tickertape Data/                 ← already exists (17 CSVs, 5,749 stocks)
├── Sector Studies/                  ← sector-level deep study (before stock selection)
│   ├── 01_Banking/
│   │   ├── phase1_identity.md
│   │   ├── phase2_quantitative.md
│   │   ├── phase3_macro.md
│   │   └── scorecard.md
│   ├── 02_IT/
│   │   └── ...
│   ├── ... (13 sectors)
│   └── comparative_ranking.md       ← Phase 5: final ranking + sector selection
└── <sector_name>/                   ← stock-level study (after sector selection)
    ├── README.md                    ← sector overview + final stock scorecard
    ├── screening/
    │   ├── methodology.md           ← sector-specific variable priorities
    │   ├── stage1_hard_filters.md   ← hard filter results
    │   └── stage2_momentum.md       ← momentum gate results
    ├── study_plan.md                ← sector-specific module overrides (if any)
    └── stocks/
        └── <stock_name>/
            ├── module1_momentum.md
            ├── module2_risk.md
            ├── module3_technicals.md
            ├── module4_fundamentals.md
            ├── module5_valuation.md
            └── module6_promoter.md
```

---

## Execution Phases

### Part A — Sector Selection (which sectors to invest in)

| Phase | Action | Output |
|-------|--------|--------|
| **A0** | Create framework files | README.md, sector_study_plan.md, sector_overview.md, study_plan.md |
| **A1** | Phase 2 (Quantitative Health Check) for all 13 sectors from CSVs | `Sector Studies/<sector>/phase2_quantitative.md` |
| **A2** | Phase 1 (Sector Identity) for all 13 sectors via web research | `Sector Studies/<sector>/phase1_identity.md` |
| **A3** | Phase 3 (Macro, Policy & Cycle) for all 13 sectors via web research | `Sector Studies/<sector>/phase3_macro.md` |
| **A4** | Phase 4 (Scorecard) for all 13 sectors | `Sector Studies/<sector>/scorecard.md` |
| **A5** | Phase 5 (Comparative Ranking) — rank and select top 3–4 sectors | `Sector Studies/comparative_ranking.md` + updated `sector_overview.md` |

### Part B — Stock Selection (within selected sectors)

| Phase | Action | Output |
|-------|--------|--------|
| **B1** | Apply Stage 1 hard filters in top-ranked sector | `<Sector>/screening/stage1_hard_filters.md` |
| **B2** | Apply Stage 2 momentum gates | `<Sector>/screening/stage2_momentum.md` |
| **B3** | Deep study shortlisted stocks (modules 1–6) | `<Sector>/stocks/<name>/module[1-6]_*.md` |
| **B4** | Create decision tree + comparative scorecard | `<Sector>/decision_tree.md` |
| **B5** | Repeat B1–B4 for next selected sector | Next sector folder |

---

## Key Design Decisions

1. **Module 3 is Technical Setup (20%)** — not in the MF framework. For momentum/swing trades, the technical entry signal is a first-class criterion.
2. **Valuation weight is 15%** — momentum trades care less about valuation than direction. Still included to avoid buying overextended stocks at extreme PE.
3. **Sector-specific overrides allowed** — Banks have structurally high D/E (not a red flag), Pharma has R&D spend as extra quality signal. Each sector's `methodology.md` documents these adjustments.
4. **Modules 1–5 are data-driven from CSVs** — Module 6 (Promoter) combines CSV data with web research for governance events. Same pattern as Module 6 (AMC) in the MF framework.
5. **Decision tree per sector** — after all stocks in a sector are scored, a `decision_tree.md` equivalent is created with comparative scorecard, mermaid charts, and investor-profile mapping. Same structure as `Mutual Fund/FlexiCap/decision_tree.md`.

---

*Framework version: 1.1 | Updated: 2026-05-21 | Changes: Added sector deep study (Part A) before stock selection; split execution into Part A (sector) + Part B (stock) | Mirrors: Mutual Fund/FlexiCap 6-module framework*
