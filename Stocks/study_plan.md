# Deep Study Plan: 6-Module Framework for Stocks

## Context
After sector selection and 2-stage screening, each shortlisted stock is studied across 6 modules before a final scored comparison — identical structure to the mutual fund framework.

**Investment context:** Momentum / swing trades. This shifts module weights compared to long-term SIP investing — Technical Setup and Momentum carry more weight; Valuation and Governance carry less.

---

## The 6 Modules

### Module 1 — Momentum & Returns (25%)

Price performance across multiple time horizons, relative to both sector peers and Nifty.

| Metric | Source | Scoring Guide |
|--------|--------|---------------|
| 1D / 1W / 1M / 6M / 1Y absolute return | File (6) | Positive across 4+ horizons = strong |
| 1M / 6M / 1Y return vs Nifty | File (6) | Positive alpha across all = outperforming market |
| 5Y CAGR | File (6) | > 15% = durable compounder |
| Price Momentum Rank | File (7) | > 80th = excellent, 60–80 = good, < 40 = weak |
| % from 52W High | File (6) | < 5% = near peak (strong); > 20% = in correction |
| Return consistency | Computed | How many of 1M/6M/1Y are positive vs sector median |

> **Why 25%:** For swing trades, recent price momentum is the primary signal. A stock in a strong trend across multiple horizons has the highest probability of continuation.

---

### Module 2 — Risk Profile (20%)

How much risk you're taking per unit of return.

| Metric | Source | Scoring Guide |
|--------|--------|---------------|
| Volatility (200D annualized) | File (10) | Lower is better — smoother price action |
| Volatility vs Nifty | File (10) | < 0 = less volatile than market |
| Beta | File (10) | 0.8–1.2 = moderate; > 1.5 = high risk; < 0.5 = defensive |
| Sharpe Ratio (2Y) | File (10) | > 1.0 = excellent; 0.5–1.0 = acceptable; < 0 = fail |
| 1Y Max Loss | File (10) | < -15% = moderate; -15 to -30% = high; > -30% = severe |
| % from 52W Low | File (6) | > 50% = well above floor; < 20% = near bottom (risky or reversal) |

> **Why 20%:** Risk management is critical for swing trades. A stock with high Sharpe and low max drawdown offers better risk/reward for position sizing.

---

### Module 3 — Technical Setup (20%)

Current chart posture — is the stock technically positioned for an entry?

**Core Technicals (all stocks):**

| Metric | Source | Scoring Guide |
|--------|--------|---------------|
| Price vs SMA-50 / SMA-200 | File (10), (11) | Price > SMA50 > SMA200 = golden cross (5); Price < both = bearish (1) |
| RSI-14D | File (9) | 50–70 = ideal momentum (5); 40–50 = neutral (3); > 80 = overbought (2); < 30 = oversold (1–2) |
| MACD (Trend Line + Signal) | File (10) | MACD positive + above signal = bullish (5); negative + below = bearish (1) |
| SuperTrend | File (10) | Buy signal = 5; Sell signal = 1 |
| ADX Rating | File (9) | > 40 = strong trend (5); 25–40 = trending (4); < 20 = no trend (2) |
| Relative Volume | File (9) | > 1 = expanding (confirms trend); < 1 = declining (weakening) |
| Stochastic %K / %D | File (9), (10) | Confirmation signal — aligns with RSI direction |
| Bollinger Band position | File (10) | Price near upper band + expanding bands = breakout potential |
| OBV Change (1W) | File (9) | Positive = accumulation; Negative = distribution |
| A/D Line Change (1W) | File (9) | Positive = buying pressure; Negative = selling pressure |

**F&O Sentiment Overlay (173 stocks with derivatives data only):**

For F&O stocks, the following metrics from File (5) supplement the core technicals. When available, they can shift the Module 3 score by up to +0.5 or -0.5.

| Metric | Source | Scoring Guide |
|--------|--------|---------------|
| Put-Call Ratio (PCR) | File (5) | < 0.7 = bullish (call-heavy); 0.7–1.0 = neutral; > 1.5 = extreme bearish or contrarian bullish |
| Future OI Change (1D + 1W) | File (5) | Rising OI + rising price = long buildup (bullish); Rising OI + falling price = short buildup (bearish) |
| Futures Basis | File (5) | Positive (premium) = bullish expectation; Negative (discount) = bearish |
| Rollover Cost | File (5) | Higher rollover = stronger conviction to carry positions forward |
| Call OI vs Put OI at key strikes | File (5) | Highest Put OI strike = support; Highest Call OI strike = resistance |
| 1W Change in Call OI / Put OI | File (5) | Relative buildup shows where smart money is positioning |

> **Why 20%:** This module is unique to stocks (not in the MF framework). For momentum/swing trades, the technical entry timing is a first-class criterion. A fundamentally strong stock in a bad technical setup is a bad trade. The F&O overlay adds a sentiment dimension for liquid stocks — OI and PCR often lead price moves by 1–2 days.

---

### Module 4 — Business Fundamentals (15%)

Quality filter — avoid momentum in junk companies. Covers backward-looking quality, forward growth trajectory, and the most recent quarterly snapshot.

**Profitability & Quality (backward-looking):**

| Metric | Source | Scoring Guide |
|--------|--------|---------------|
| ROE + 5Y Avg ROE | Base file | > 15% = good; > 20% = excellent; < 10% = weak |
| ROCE | Base file | > 15% = efficient; > 20% = excellent; < 10% = capital destruction |
| Net Profit Margin + 5Y Avg | Base file | Positive and stable/growing = good; declining = concern |
| Debt to Equity | File (7) | < 0.5 = conservative; 0.5–1.0 = moderate; > 2.0 = risky (sector-adjusted) |
| 5Y Revenue CAGR | File (1) | > 15% = strong growth; 10–15% = moderate; < 5% = stagnant |
| Earnings Quality Rank | File (7) | > 70th percentile = high quality; < 30th = low quality |
| Fundamental Score | File (7) | > 7/10 = strong; 5–7 = average; < 4 = weak |

**Earnings Growth Trajectory (forward-looking, ~940 analyst-covered stocks):**

| Metric | Source | Scoring Guide |
|--------|--------|---------------|
| 1Y Forward EPS Growth | File (1) | > 20% = strong expected growth; < 0% = earnings contraction expected |
| 1Y Forward Revenue Growth | File (1) | > 15% = strong; < 5% = stagnant |
| EPS Acceleration | Computed: Fwd EPS Growth minus 1Y Historical EPS Growth | Positive = accelerating (bullish catalyst); Negative = decelerating |
| 1Y Forward EBITDA Growth | File (1) | > 15% = strong operating profit growth |

> For stocks without analyst coverage (no forward estimates), this sub-section is skipped and the score is based on the backward-looking and quarterly metrics only.

**Quarterly Snapshot (most recent quarter):**

| Metric | Source | Scoring Guide |
|--------|--------|---------------|
| Revenue (Q) | File (16) | Compare vs previous quarter and same quarter last year |
| EPS (Q) | File (16) | Positive and growing QoQ = healthy |
| EBITDA (Q) | File (16) | Improving margin vs annual average = business gaining strength |
| Net Income (Q) | File (16) | Positive; check vs annual Net Income / 4 for run-rate |

> Quarterly data answers the question: "Is this business improving *right now*?" A stock with strong momentum and improving quarterly results has the highest probability of sustained trend continuation. A stock with strong momentum but deteriorating quarters is a reversal risk.

> **Why 15%:** Even for momentum trades, fundamentals act as a safety net. Momentum in a company with deteriorating fundamentals is a short squeeze or pump-and-dump risk. The forward estimates and quarterly snapshot catch inflection points that backward-looking metrics miss — earnings acceleration is often the catalyst that launches a momentum move.

---

### Module 5 — Valuation (15%)

Is the price reasonable relative to earnings and peers?

| Metric | Source | Scoring Guide |
|--------|--------|---------------|
| PE Ratio vs Sub-sector avg | File (2) | At or below sector = fair/cheap; > 2x sector = stretched |
| PB Ratio vs Sub-sector avg | File (2) | Context-dependent — high PB acceptable if ROE justifies |
| EV/EBITDA | File (2) | < 10 = cheap; 10–20 = moderate; > 30 = expensive |
| Dividend Yield vs sector | File (2) | Higher = margin of safety (less critical for momentum) |
| Price/Free Cash Flow | File (2) | Lower = more cash per rupee of price |
| Price to Intrinsic Value Rank | File (7) | Lower percentile = more undervalued |

> **Why 15%:** Momentum can override valuation short-term, but extreme overvaluation increases drawdown risk. This module prevents buying at 80x PE when sector trades at 25x.

---

### Module 6 — Promoter & Governance (5%)

Management quality and institutional trust signals.

| Metric | Source | Scoring Guide |
|--------|--------|---------------|
| Promoter Holding % | File (4) | > 50% = high alignment (5); 35–50% = moderate (3); < 25% = weak (2) |
| Pledged Promoter Holding % | File (4) | 0% = clean (5); < 10% = acceptable (3); > 20% = red flag (1) |
| Promoter Holding Change 3M + 6M | File (4) | Increasing = positive; stable = neutral; decreasing = warning |
| FII 3M Change + DII 3M Change | File (4) | Net institutional buying = strong tailwind |
| % Buy Recommendations | File (8) | > 70% = strong consensus (5); 50–70% = moderate (3); < 30% = bearish (1) |
| Insider Trades 3M cumulative | File (4) | Net buying = management confidence; net selling = concern |

> **Why 5%:** Same weight as AMC module in MF. For swing trades, governance is a disqualifier (pledge > 40% = avoid) rather than a differentiator. One red flag eliminates; otherwise it barely moves the score.

---

## Scoring Rubric

Same scale as the mutual fund framework:

| Score | Meaning | Description |
|-------|---------|-------------|
| 5 | Excellent | Top of sector on most metrics, no concerns |
| 4 | Good | Above sector average, minor concerns |
| 3 | Average | In line with sector, nothing special |
| 2 | Below Average | Below sector on key metrics, some flags |
| 1 | Poor | Fails multiple criteria, significant risks |

---

## Final Scoring Formula

| Module | Weight |
|--------|--------|
| 1 — Momentum & Returns | 25% |
| 2 — Risk Profile | 20% |
| 3 — Technical Setup | 20% |
| 4 — Business Fundamentals | 15% |
| 5 — Valuation | 15% |
| 6 — Promoter & Governance | 5% |
| **Total** | **100%** |

**Weighted Total** = (M1 x 0.25) + (M2 x 0.20) + (M3 x 0.20) + (M4 x 0.15) + (M5 x 0.15) + (M6 x 0.05)

**Maximum possible score:** 5.00

---

## Hard Disqualification Filters (Run Before Scoring)

Same concept as the MF "Hard Filters" in `decision_tree.md`. Any "yes" eliminates the stock regardless of score.

| Filter | Threshold | Rationale |
|--------|-----------|-----------|
| Active SEBI/regulatory investigation on promoter? | — | Legal risk to stock price |
| Pledged promoter holding > 40%? | — | Forced selling cascade risk |
| Negative operating cash flow for 3+ consecutive years? | — | Business not generating cash |
| Auditor qualification / going concern note? | — | Existential risk |
| Operator-driven stock (no institutional holding)? | FII + DII + MF < 5% | Manipulation risk |
| Circuit-hitting stock (frequent upper/lower circuits)? | — | Cannot exit when needed |

---

## Comparison to Mutual Fund Framework

| Aspect | Mutual Fund | Stocks |
|--------|-------------|--------|
| Category | FlexiCap (fund type) | Sector (e.g., Banking) |
| Unit of study | Individual fund | Individual stock |
| Module 1 | Returns Consistency (25%) | Momentum & Returns (25%) |
| Module 2 | Risk Profile (20%) | Risk Profile (20%) |
| Module 3 | Portfolio DNA (15%) | **Technical Setup + F&O Sentiment (20%)** |
| Module 4 | Cost & AUM Impact (20%) | **Business Fundamentals + Fwd Estimates + Quarterly (15%)** |
| Module 5 | Fund Manager Quality (15%) | **Valuation (15%)** |
| Module 6 | AMC Trustworthiness (5%) | Promoter & Governance (5%) |
| Key differences | — | Technical Setup is new (M3); F&O overlay for 173 stocks; forward estimates + quarterly earnings added to M4 |
| Investment horizon | 10-year SIP | Swing trades (days to weeks) |
| CSV files used | 7 MF-specific CSVs | **14 of 17 Tickertape CSVs** (see Data Coverage below) |

---

## Study Order (within a sector)

Study shortlisted stocks in order of their **Stage 2 composite rank** (strongest momentum first), same logic as studying Parag Parikh first in MF (to build a reference frame).

| Priority | Logic |
|----------|-------|
| 1st stock | Strongest momentum in shortlist — sets the benchmark |
| 2nd stock | Second strongest — comparison begins |
| 3rd+ stocks | In descending order — each new study builds the comparative grid |
| Last stock | Weakest in shortlist — often gets eliminated during study |

After all stocks are studied, create a **decision_tree.md** with the comparative scorecard, mermaid charts, and final picks.

---

## Data Coverage by Module

Which of the 17 Tickertape CSV files feed into each module:

| Module | Files Used | Files Not Used |
|--------|-----------|---------------|
| M1 — Momentum & Returns | File (6): returns, File (7): Momentum Rank | — |
| M2 — Risk Profile | File (9): RSI/Beta/Vol, File (10): Sharpe/technicals, File (11): SMAs/Max Loss | — |
| M3 — Technical Setup | File (9): RSI/ADX/OBV/Vol, File (10): MACD/SuperTrend/Bollinger, File (11): all SMAs/EMAs, **File (5): F&O data** | — |
| M4 — Business Fundamentals | Base file: profitability, File (1): growth + forward estimates, File (7): ratios/scores, **File (16): quarterly results** | — |
| M5 — Valuation | File (2): PE/PB/EV multiples, File (3): EV/FCF/TTM PE | — |
| M6 — Promoter & Governance | File (4): ownership/pledging/insider trades, File (8): analyst recommendations | — |
| **Screening stages** | File (6): returns, File (7): Momentum Rank, File (10): 200D SMA | — |

**Files used:** Base, (1), (2), (3), (4), (5), (6), (7), (8), (9), (10), (11), (15), (16) — **14 of 17 files**

**Files not directly used in modules:**
| File | Contents | Why excluded |
|------|----------|-------------|
| File (12) | Cash flow & balance sheet (Operating CF, CapEx, Liabilities) | OCF check is a hard disqualification filter, not a scored metric; balance sheet deep dive too granular for swing trades |
| File (13) | Balance sheet detail (Total Assets, Debt, Equity, Receivables) | Debt/Equity already in File (7); remaining detail too granular |
| File (14) | Balance sheet detail (Cash, Inventory, FCF, Book Value) | FCF captured via File (2) Price/FCF; Book Value via PB ratio |

> Files (12), (13), (14) contain long-term fundamental data most useful for value investing or credit analysis. For momentum/swing trades, the relevant signals (Debt/Equity, FCF yield, cash position) are already captured through ratio-level metrics in the active files.

---

## Web Research & Cross-Verification

Tickertape CSVs are the primary data source for screening and scoring, but they have limitations:
- **Point-in-time snapshot** — exported May 21, 2026; markets move daily
- **Computed ratios not audited** — Sharpe, Sortino, Alpha are Tickertape's calculations
- **Missing qualitative data** — no governance events, management quality, or news catalysts
- **No delivery %** — critical for swing trades (shows if buying is genuine or speculative)

This section defines what web data is needed, which module it feeds, and where to find it. Same pattern as the mutual fund framework where Modules 5 (Fund Manager) and 6 (AMC) required web research beyond CSV data.

### What to Cross-Verify (CSV data → Web)

Data that exists in CSVs but should be confirmed from authoritative sources before making a trade decision.

| Data Point | CSV Source | Cross-Verify On | Why |
|------------|-----------|-----------------|-----|
| Promoter holding & pledging | File (4) | BSE Corporate Filings (bseindia.com) | BSE filings are the legal source; Tickertape may lag by days |
| FII / DII / MF holding changes | File (4) | Trendlyne Shareholding page | Quarterly changes may not reflect latest bulk/block deals |
| PE / PB / EV multiples | Files (2), (3) | Screener.in | Tickertape and Screener sometimes differ on TTM calculations |
| Revenue, EPS, Net Income (quarterly) | File (16) | Screener.in quarterly results | Verify the exact quarter being reported; check for restated figures |
| Forward EPS / Revenue estimates | File (1) | Trendlyne Forecaster | Confirm analyst count and estimate range (Tickertape shows median only) |
| Analyst Buy/Sell/Hold consensus | File (8) | Trendlyne Forecaster | Check if consensus has shifted since CSV export date |
| 52W High / Low and returns | File (6) | NSE India (nseindia.com) | Authoritative exchange data; verify if corporate actions (splits/bonus) affected the calculation |

### What's NOT in CSVs (Web-Only Data)

Data that doesn't exist in any Tickertape CSV and must be sourced entirely from the web. This data feeds primarily into Modules 4 and 6, and the Hard Disqualification Filters.

#### Per-Module Web Research Requirements

**Module 1 — Momentum & Returns:**
| Web Data | Source | Purpose |
|----------|--------|---------|
| Live price and intraday trend | NSE India, Google Finance | CSV is a snapshot; verify current price hasn't gapped significantly since export |
| Delivery % (5-day avg) | NSE India market data | > 50% = genuine buying; < 30% = speculative/intraday-driven (weak momentum) |

**Module 2 — Risk Profile:**
| Web Data | Source | Purpose |
|----------|--------|---------|
| Recent circuit hits (last 30 days) | NSE India circuit breaker data | Frequent upper/lower circuits = illiquid, cannot exit when needed |
| Impact cost | NSE India market depth | High impact cost = slippage risk on entry/exit; critical for position sizing |

**Module 3 — Technical Setup:**
| Web Data | Source | Purpose |
|----------|--------|---------|
| Live chart with volume profile | TradingView, ChartInk | CSV gives single-point indicators; charts show pattern context (head & shoulders, flags, etc.) |
| Sector heatmap / relative strength | Trendlyne sector dashboard | Is this stock's sector in favor? Sector tide lifts/sinks individual stocks |

**Module 4 — Business Fundamentals:**
| Web Data | Source | Purpose |
|----------|--------|---------|
| Last 4–8 quarterly results (trend) | Screener.in quarterly results | CSV has only most recent quarter; need QoQ and YoY trend to spot acceleration/deceleration |
| Earnings surprise history | Trendlyne Forecaster | Did the company beat or miss estimates in recent quarters? Consistent beats = momentum catalyst |
| Management commentary (con-call highlights) | Trendlyne, Screener.in, BSE filings | Forward guidance, order book commentary, margin outlook — not in any CSV |
| Credit rating | CRISIL, ICRA, CARE (via BSE filings) | Rating upgrade = positive; downgrade = debt risk. Not in CSVs |
| Order book / revenue visibility | Company investor presentations, BSE filings | For capital goods, infra, defense stocks — backlog drives future revenue |

**Module 5 — Valuation:**
| Web Data | Source | Purpose |
|----------|--------|---------|
| Historical PE band (5Y) | Screener.in, Trendlyne | Is current PE at the top or bottom of its own historical range? CSV gives only current PE |
| PEG Ratio | Computed: PE / Forward EPS Growth | Not directly in CSVs; needs forward estimate from File (1) verified via Trendlyne |
| Peer comparison table | Screener.in peer comparison | CSV has sub-sector averages; web gives the actual peer list with individual multiples |

**Module 6 — Promoter & Governance:**
| Web Data | Source | Purpose |
|----------|--------|---------|
| SEBI / regulatory actions on company or promoter | SEBI orders database (sebi.gov.in), news search | Same as MF Module 6 (AMC) — legal/regulatory risk not in CSVs |
| Related-party transactions (RPT) | Annual report, BSE filings | Excessive RPTs = governance red flag; promoter siphoning risk |
| Board composition & independence | BSE corporate governance filings | Weak independent board = less oversight |
| Promoter entity structure | BSE shareholding pattern | Complex promoter web = opaque; simple = transparent |
| Recent bulk / block deal details (who bought/sold) | BSE/NSE bulk deal data | CSV shows cumulative %; web shows the actual buyer/seller names (FII name, promoter entity, etc.) |
| Auditor changes or qualifications | BSE filings, annual report | Auditor resignation or qualified opinion = serious red flag |
| Recent news & catalysts | Moneycontrol, Economic Times, Livemint | M&A, product launches, regulatory changes, management exits — not in CSVs |
| Insider trading details | BSE SAST filings | CSV shows cumulative %; web shows who, when, and at what price |

#### Hard Disqualification Filters — Web Sources

These filters from the scoring section require web verification — they cannot be confirmed from CSVs alone:

| Filter | Web Source |
|--------|-----------|
| Active SEBI/regulatory investigation on promoter? | SEBI orders database, news search |
| Negative operating cash flow for 3+ consecutive years? | Screener.in (last 5 years cash flow statement) |
| Auditor qualification / going concern note? | BSE filings (auditor report in annual report) |
| Circuit-hitting stock? | NSE India circuit breaker logs |

### Web Research Sources — Quick Reference

| Source | URL Pattern | Best For |
|--------|-------------|----------|
| **Screener.in** | screener.in/company/TICKER | Financials, quarterly results, peer comparison, historical PE |
| **Trendlyne** | trendlyne.com/fundamentals/stock/TICKER | Shareholding, forecaster, technicals, sector dashboard |
| **NSE India** | nseindia.com/get-quotes/equity?symbol=TICKER | Live price, delivery %, market depth, circuit data, bulk deals |
| **BSE India** | bseindia.com/stock-share-price/COMPANY/TICKER | Corporate filings, shareholding pattern, board meetings, SAST |
| **SEBI** | sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=4 | Regulatory orders and adjudications |
| **Moneycontrol** | moneycontrol.com/india/stockpricequote/SECTOR/COMPANY/TICKER | News, financials, analyst estimates |
| **TradingView** | tradingview.com/chart/?symbol=NSE:TICKER | Live charts, volume profile, pattern recognition |
| **ChartInk** | chartink.com/screener/ | Custom technical scans for Indian market |

### When to Do Web Research

Web research is NOT done during screening (Stages 1–2) — that's fully CSV-driven for speed. Web research happens only during the **deep study phase** (Modules 1–6) for each shortlisted stock.

| Phase | Data Source | Web Research? |
|-------|-----------|---------------|
| Sector ranking | CSV only | No |
| Stage 1 — Hard filters | CSV only | No |
| Stage 2 — Momentum gates | CSV only | No |
| Deep study — Modules 1–3 | CSV primary + web for live price, delivery %, charts | Light |
| Deep study — Modules 4–6 | CSV primary + web for quarterly trends, governance, news | Heavy |
| Hard disqualification filters | Web required | Yes — mandatory before final scoring |
| Final trade decision | All sources | Cross-verify key numbers before committing capital |

---

*Framework version: 1.2 | Updated: 2026-05-21 | Changes: Added Web Research & Cross-Verification section — what to verify, what's web-only, per-module sources, quick reference table, and timing guidance | Adapted from: Mutual Fund/FlexiCap 6-module framework | Context: Momentum / swing trades*
