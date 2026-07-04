# Full Universe Data — All 33 Mid Cap Funds

**Data:** Tickertape screener API, **July 3, 2026** (Direct plan, Growth option). Raw CSV: `Mutual Fund/TickerTape Data/MidCap_Screener_API_03_07_2026.csv`.

**Universe notes:** 37 raw rows → 33 funds after removing 1 duplicate (Nippon India Growth listed twice) and 3 SIF long-short products (iSIF/Qsif/WSIF "Equity Ex-Top 100 Long-Short" — Specialized Investment Funds misfiled under the Mid Cap subsector, not comparable mutual funds).

- `Age` caps at **163 months** (~13.6y): 163 = "at least 13.6 years old"
- `Mid%*` per Tickertape's own market-cap classification, not AMFI's — sub-65% values are a classification artifact, not mandate breaches (verified per fund in Module 3)
- `Alpha`, `Sharpe`, `Sortino`, `Vol` as computed by Tickertape over its trailing window
- **Category St Dev: 15.26% | Category PE: 33.76**

## Screening summary

- **Stage 1** (ER ≤ 1.0%, ₹500 Cr ≤ AUM ≤ ₹50,000 Cr, age ≥ 60mo, Sharpe ≥ 0): 33 → 15
- **Stage 2** (5Y CAGR > 17.63% universe median, strictly; 3Y CAGR > 1.0× universe mean 20.27%): 15 → **7 shortlisted**

---

| Fund | AUM (Cr) | ER% | Age (mo) | 10Y | 5Y | 3Y | 1Y | Alpha | Sharpe | Sortino | Vol% | PE | Mid%* | Lg% | Sm% | Status |
|------|----------|-----|----------|-----|-----|-----|-----|-------|--------|---------|------|----|----|-----|-----|--------|
| HDFC Mid Cap Fund | 97,350 | 0.73 | 163 | 18.50 | 20.70 | 20.66 | 4.88 | 0.76 | 0.092 | 0.009 | 13.9 | 25.9 | 66.8 | 10.0 | 15.6 | Stage 1 out |
| Kotak Midcap Fund | 64,749 | 0.39 | 163 | 18.75 | 18.47 | 20.87 | 6.56 | 1.71 | 0.214 | 0.022 | 15.6 | 28.2 | 61.2 | 20.1 | 16.9 | Stage 1 out |
| Nippon India Growth Mid Cap Fund | 47,415 | 0.73 | 163 | 19.32 | 21.48 | 23.10 | 7.21 | 1.93 | 0.264 | 0.027 | 15.7 | 29.3 | 58.1 | 27.7 | 12.9 | ✅ **SHORTLIST** |
| Motilal Oswal Midcap Fund | 36,458 | 0.75 | 150 | 17.50 | 23.00 | 18.73 | -8.80 | -4.77 | -0.694 | -0.073 | 18.5 | 44.9 | 67.2 | 26.1 | 0.0 | Stage 1 out |
| Axis Midcap Fund | 32,852 | 0.57 | 163 | 18.08 | 15.66 | 18.05 | 4.86 | 3.99 | 0.090 | 0.009 | 14.3 | 39.1 | 65.5 | 22.1 | 3.6 | Stage 2 out |
| SBI Midcap Fund | 23,417 | 0.85 | 163 | 14.87 | 15.96 | 13.73 | 1.68 | -1.36 | -0.129 | -0.013 | 13.8 | 39.9 | 60.6 | 12.6 | 22.2 | Stage 1 out |
| DSP Midcap Fund | 19,673 | 0.60 | 163 | 15.21 | 13.28 | 18.60 | 4.08 | 0.67 | 0.048 | 0.005 | 15.3 | 28.7 | 66.5 | 15.7 | 13.4 | Stage 2 out |
| Mirae Asset Midcap Fund | 19,003 | 0.50 | 85 | — | 17.43 | 19.74 | 8.74 | 2.35 | 0.338 | 0.034 | 15.4 | 38.0 | 72.9 | 12.5 | 13.6 | Stage 2 out |
| Edelweiss Mid Cap Fund | 16,849 | 0.48 | 163 | 19.88 | 20.64 | 24.05 | 5.16 | 1.09 | 0.135 | 0.014 | 15.2 | 30.3 | 60.9 | 22.8 | 10.7 | ✅ **SHORTLIST** |
| HSBC Midcap Fund | 14,249 | 0.56 | 163 | 18.47 | 20.44 | 27.68 | 17.50 | 5.81 | 0.848 | 0.089 | 16.2 | 39.5 | 51.4 | 26.5 | 21.0 | ✅ **SHORTLIST** |
| Sundaram Mid Cap Fund | 13,687 | 0.88 | 163 | 15.63 | 19.31 | 22.27 | 6.41 | 0.69 | 0.210 | 0.022 | 15.2 | 35.2 | 66.3 | 16.9 | 13.6 | ✅ **SHORTLIST** |
| Invesco India Midcap Fund | 12,397 | 0.49 | 163 | 20.34 | 21.91 | 26.91 | 10.01 | 7.35 | 0.408 | 0.043 | 16.9 | 49.4 | 52.1 | 23.9 | 22.6 | ✅ **SHORTLIST** |
| Franklin India Mid Cap Fund | 12,231 | 0.82 | 163 | 15.16 | 15.62 | 18.42 | -1.25 | -1.53 | -0.305 | -0.031 | 14.9 | 32.4 | 63.9 | 13.7 | 18.4 | Stage 1 out |
| UTI Mid Cap Fund | 11,605 | 0.91 | 163 | 14.72 | 14.19 | 14.45 | 0.14 | -0.91 | -0.200 | -0.020 | 15.0 | 32.8 | 65.6 | 11.3 | 21.5 | Stage 1 out |
| PGIM India Midcap Fund | 10,822 | 0.56 | 152 | 17.18 | 13.67 | 13.01 | -0.09 | -1.07 | -0.222 | -0.023 | 15.3 | 34.7 | 62.3 | 23.4 | 11.4 | Stage 1 out |
| Quant Mid Cap Fund | 8,109 | 1.10 | 163 | 18.30 | 17.81 | 16.87 | 0.87 | -0.94 | -0.213 | -0.022 | 13.9 | 35.4 | 67.4 | 19.2 | 8.9 | Stage 1 out |
| ICICI Pru Midcap Fund | 7,789 | 0.87 | 163 | 17.78 | 19.01 | 24.75 | 11.36 | 3.47 | 0.456 | 0.048 | 17.5 | 30.1 | 68.7 | 18.9 | 10.2 | ✅ **SHORTLIST** |
| Aditya Birla SL Midcap Fund | 6,398 | 0.87 | 163 | 14.72 | 16.73 | 19.08 | 5.83 | 1.39 | 0.183 | 0.019 | 15.4 | 34.3 | 65.2 | 9.7 | 23.4 | Stage 2 out |
| Tata Mid Cap Fund | 5,732 | 0.55 | 163 | 17.32 | 17.24 | 19.23 | 5.55 | 1.02 | 0.114 | 0.011 | 14.5 | 32.3 | 68.2 | 20.4 | 9.4 | Stage 2 out |
| WOC Mid Cap Fund | 5,293 | 0.51 | 47 | — | — | 24.92 | 11.15 | 7.10 | 0.502 | 0.052 | 14.4 | 31.3 | 59.8 | 10.0 | 15.8 | Stage 1 out |
| Mahindra Manulife Mid Cap Fund | 4,866 | 0.42 | 103 | — | 20.17 | 23.67 | 9.60 | 2.83 | 0.405 | 0.041 | 15.9 | 32.1 | 72.2 | 9.8 | 15.9 | ✅ **SHORTLIST** |
| Canara Rob Mid Cap Fund | 4,622 | 0.52 | 44 | — | — | 19.87 | 5.42 | 1.94 | 0.154 | 0.016 | 15.6 | 34.0 | 60.7 | 26.6 | 9.1 | Stage 1 out |
| Baroda BNP Paribas Mid Cap Fund | 2,461 | 0.49 | 163 | 17.17 | 17.63 | 21.20 | 11.01 | 3.02 | 0.464 | 0.046 | 14.5 | 28.9 | 56.8 | 19.7 | 19.2 | Stage 2 out |
| Bandhan Midcap Fund | 2,205 | 0.49 | 48 | — | — | 20.61 | 7.71 | 5.38 | 0.264 | 0.027 | 15.6 | 45.7 | 58.0 | 25.9 | 11.9 | Stage 1 out |
| Union Midcap Fund | 1,771 | 0.68 | 77 | — | 17.73 | 19.74 | 8.12 | 3.05 | 0.327 | 0.034 | 15.8 | 37.2 | 59.7 | 21.5 | 16.6 | Stage 2 out |
| Helios Mid Cap Fund | 1,490 | 0.66 | 17 | — | — | — | 15.94 | 5.25 | 0.757 | 0.079 | 16.5 | 45.5 | 55.5 | 12.2 | 31.2 | Stage 1 out |
| ITI Mid Cap Fund | 1,395 | 0.57 | 65 | — | 17.36 | 23.53 | 7.88 | 2.28 | 0.313 | 0.031 | 16.0 | 28.1 | 61.3 | 23.2 | 11.8 | Stage 2 out |
| JM Midcap Fund | 1,217 | 0.56 | 45 | — | — | 24.02 | 9.23 | 2.89 | 0.381 | 0.040 | 17.1 | 35.1 | 57.3 | 12.4 | 29.3 | Stage 1 out |
| Bank of India Mid Cap Fund | 722 | 1.07 | 12 | — | — | — | — | -0.38 | 0.056 | 0.006 | 15.1 | 29.1 | 66.7 | 15.2 | 14.0 | Stage 1 out |
| LIC MF Midcap Fund | 357 | 1.13 | 115 | — | 14.97 | 18.96 | 2.57 | 0.16 | -0.037 | -0.004 | 16.0 | 35.7 | 56.1 | 11.9 | 27.3 | Stage 1 out |
| TRUSTMF Mid Cap Fund | 241 | 0.52 | 5 | — | — | — | — | 13.31 | 4.254 | 0.532 | 13.7 | 40.7 | 62.4 | 13.2 | 19.4 | Stage 1 out |
| Taurus Mid Cap Fund | 125 | 1.69 | 163 | 14.59 | 11.81 | 11.07 | -5.41 | -3.21 | -0.541 | -0.053 | 16.3 | 18.8 | 58.7 | 11.0 | 26.3 | Stage 1 out |
| Samco Mid Cap Fund | 76 | 1.74 | 6 | — | — | — | — | 0.67 | -0.017 | -0.002 | 21.0 | 17.0 | 75.5 | 18.8 | 4.6 | Stage 1 out |
---

*Generated: July 3, 2026 | Source: api.tickertape.in/mf-screener (subsector = "Mid Cap Fund", Growth plans, Direct figures) | 33 funds | See [methodology.md](methodology.md) for filter design and data caveats*
