# FlexiCap Fund Category

## What is a FlexiCap Fund?
A FlexiCap fund can invest across market capitalizations — largecap, midcap, and smallcap — with no fixed allocation. The fund manager decides the mix based on market conditions and valuations.

**SEBI mandate:** Minimum 65% in equities. No cap-wise restriction.

## Universe
- Total FlexiCap funds in India (as of May 2026): **46 funds**
- After Stage 1 + Stage 2 screening: **9 shortlisted funds**

## Data Source
All CSV files in the `FlexiCap/` folder are exported from **Tickertape** on **May 10, 2026**.

| File | Contents |
|------|----------|
| `FlexiCap_10_05_2026_schemaInfo.csv` | AUM, ER, NAV, fund manager, inception, SIP details |
| `FlexiCap_Screener_return_10_05_2026.csv` | Alpha, CAGR 3Y/5Y/10Y, absolute returns, rolling returns |
| `FlexiCap_Mutual_Funds_Screener_Rato-1_10_05_2026.csv` | Sharpe, Sortino, PE ratio, returns vs sub-category |
| `FlexiCap_Mutual_Funds_Screener_Ratio-2_10_05_2026.csv` | % away from ATH, YTM, average maturity |
| `FlexiCap_Mutual_Funds_Screener_Composition-1_10_05_2026.csv` | Cap allocation, concentration (top 3/5/10 holdings) |
| `FlexiCap_Mutual_Funds_Screener_risk_10_05_2026.csv` | Volatility, max drawdown, tracking error |
| `FlexiCap_Mutual_Funds_Screener_Composition-2_10_05_2026.csv` | Cash, debt quality, sovereign/corporate/A-rated bonds |

## Tickertape Reliability Note
- Owned by Anchorage Technologies (Smallcase subsidiary) — AMFI registered
- Data sourced from AMFI — industry standard
- Known limitations: occasional data delays, computed ratios (Sharpe/Sortino) not independently audited
- **Verdict:** Reliable for screening and relative comparison. Cross-verify on Valueresearchonline before final decision.
