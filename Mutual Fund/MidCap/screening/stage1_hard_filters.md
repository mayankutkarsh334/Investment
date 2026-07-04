# Stage 1 — Hard Filters: 33 → 15

**Filters (applied in order):** ER ≤ 1.0% (Direct) → AUM ≥ ₹500 Cr → AUM ≤ ₹50,000 Cr → Age ≥ 60 months → Sharpe ≥ 0

**Data:** Tickertape API, July 3, 2026 (Direct, Growth). Note: `age` caps at 163 months (~13.6y) — 163 means "at least 13.6 years."

---

## Elimination Log (18 funds out)

| Fund | AUM (Cr) | ER% | Age (mo) | Sharpe | Failed filter(s) |
|------|----------|-----|----------|--------|------------------|
| **HDFC Mid Cap** | **97,350** | 0.73 | 163 | 0.092 | **AUM > ₹50,000 Cr** — the category giant; ⭐ instructive-case candidate |
| **Kotak Midcap** | **64,749** | 0.39 | 163 | 0.214 | **AUM > ₹50,000 Cr** — note the excellent 0.39% ER; capacity still disqualifies |
| **Motilal Oswal Midcap** | 36,458 | 0.75 | 150 | **−0.694** | **Sharpe < 0** — the universe's best 5Y CAGR (23.0%) but 1Y −8.8%, alpha −4.8; the momentum book unwound in the 2024–25 correction. ⭐ instructive elimination |
| SBI Midcap | 23,417 | 0.85 | 163 | **−0.129** | Sharpe < 0 (also weak 5Y 15.96%) |
| Franklin India Mid Cap | 12,231 | 0.82 | 163 | **−0.305** | Sharpe < 0 |
| UTI Mid Cap | 11,605 | 0.91 | 163 | **−0.200** | Sharpe < 0 |
| PGIM India Midcap | 10,822 | 0.56 | 152 | **−0.222** | Sharpe < 0 (contrast: PGIM's *international* feeders are shortlisted in that study) |
| Quant Mid Cap | 8,109 | **1.10** | 163 | −0.213 | ER > 1.0% + Sharpe < 0 (consistent with quant's confirmed elimination in SmallCap) |
| WhiteOak Capital Mid Cap | 5,293 | 0.51 | **47** | 0.502 | Age < 60mo (2022 launch — bull-market-only record) |
| Canara Robeco Mid Cap | 4,622 | 0.52 | **44** | 0.154 | Age < 60mo |
| Bandhan Midcap | 2,205 | 0.49 | **48** | 0.264 | Age < 60mo (the SmallCap study's inception-bias poster child repeats here) |
| Helios Mid Cap | 1,490 | 0.66 | **17** | 0.757 | Age < 60mo (2025 launch) |
| JM Midcap | 1,217 | 0.56 | **45** | 0.381 | Age < 60mo (JM FlexiCap ranked #3 in that study — this fund is simply too young) |
| Bank of India Mid Cap | 722 | **1.07** | **12** | 0.056 | ER > 1.0% + Age < 60mo (BOI AMC strong in both domestic studies — fund too young and too expensive) |
| LIC MF Midcap | 357 | **1.13** | 115 | −0.037 | ER + AUM < ₹500 Cr + Sharpe — triple fail |
| TRUSTMF Mid Cap | 241 | 0.52 | **5** | 4.254* | AUM < ₹500 Cr + Age (5 months; *Sharpe meaningless at this age) |
| Taurus Mid Cap | 125 | **1.69** | 163 | −0.541 | ER + AUM + Sharpe — triple fail |
| Samco Mid Cap | 76 | **1.74** | **6** | −0.017 | ER + AUM + Age + Sharpe — quadruple fail |

---

## Survivors (15)

| # | Fund | AUM (Cr) | ER% | Age (mo) | Sharpe | 5Y CAGR | 3Y CAGR | 10Y CAGR |
|---|------|----------|-----|----------|--------|---------|---------|----------|
| 1 | Nippon India Growth Mid Cap | 47,415 | 0.73 | 163 | 0.264 | 21.48% | 23.10% | 19.32% |
| 2 | Axis Midcap | 32,852 | 0.57 | 163 | 0.090 | 15.66% | 18.05% | 18.08% |
| 3 | DSP Midcap | 19,673 | 0.60 | 163 | 0.048 | 13.28% | 18.60% | 15.21% |
| 4 | Mirae Asset Midcap | 19,003 | 0.50 | 85 | 0.338 | 17.43% | 19.74% | — |
| 5 | Edelweiss Mid Cap | 16,849 | 0.48 | 163 | 0.135 | 20.64% | 24.05% | 19.88% |
| 6 | HSBC Midcap | 14,249 | 0.56 | 163 | 0.848 | 20.44% | 27.68% | 18.47% |
| 7 | Sundaram Mid Cap | 13,687 | 0.88 | 163 | 0.210 | 19.31% | 22.27% | 15.63% |
| 8 | Invesco India Midcap | 12,397 | 0.49 | 163 | 0.408 | 21.91% | 26.91% | 20.34% |
| 9 | ICICI Pru Midcap | 7,789 | 0.87 | 163 | 0.456 | 19.01% | 24.75% | 17.78% |
| 10 | Aditya Birla SL Midcap | 6,398 | 0.87 | 163 | 0.183 | 16.73% | 19.08% | 14.72% |
| 11 | Tata Mid Cap | 5,732 | 0.55 | 163 | 0.114 | 17.24% | 19.23% | 17.32% |
| 12 | Mahindra Manulife Mid Cap | 4,866 | 0.42 | 103 | 0.405 | 20.17% | 23.67% | — |
| 13 | Baroda BNP Paribas Mid Cap | 2,461 | 0.49 | 163 | 0.464 | 17.63% | 21.20% | 17.17% |
| 14 | Union Midcap | 1,771 | 0.68 | 77 | 0.327 | 17.73% | 19.74% | — |
| 15 | ITI Mid Cap | 1,395 | 0.57 | 65 | 0.313 | 17.36% | 23.53% | — |

---

## Observations

1. **The Sharpe filter removed a third of the category's AUM.** Motilal (₹36K Cr), SBI (₹23K Cr), Franklin, UTI, PGIM, Quant — all currently below risk-free on a risk-adjusted basis. The 2024–25 midcap correction is still separating disciplined funds from momentum riders in the trailing numbers.
2. **Eleven of 15 survivors have full 13.6y+ records** (age-capped at 163mo) — meaning they carry genuine Jan-2018 midcap-winter data. Only Mirae (85mo), Mahindra Manulife (103mo), Union (77mo), and ITI (65mo) have gaps, and Mahindra Manulife's ~Dec-2017 inception means it *almost* fully covers the winter.
3. **The big-brand fallout is striking:** HDFC, Kotak, SBI, Motilal, Franklin, UTI, Axis (survives Stage 1, dies in Stage 2), DSP (same) — the household names largely fail. The mid-cap category's marketing hierarchy and its performance hierarchy are very different things.
4. **AMC continuations available:** Edelweiss, HSBC, Sundaram, Invesco (all studied in SmallCap and/or FlexiCap), Union (both), plus new AMCs Nippon, ICICI Pru, Mahindra Manulife, Tata, Baroda BNP, ITI, Mirae, ABSL.

---

*Stage 1 completed: July 3, 2026 | 33 → 15 | Data: Tickertape API (Direct Growth), July 3, 2026*
