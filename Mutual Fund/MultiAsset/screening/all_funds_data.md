# All Funds Data — Multi Asset Allocation (Screening Snapshot)

**Source:** Tickertape screener API, subsector "Multi Asset Allocation Fund", Direct Growth, pulled **July 28, 2026**.
**Raw files:** `TickerTape Data/MultiAsset_Screener_API_28_07_2026.csv` (35 clean) · `..._raw_all_variants.csv` (109 rows).

**Column notes:**
- `~G+C+A%` = 100 − %Equity − %Debt = the **gold + cash + arbitrage + international** sleeve the API does not expose (`percOtherH` returns 0 for every fund). Not a clean gold figure — a Module-3 factsheet task.
- `%Eq` is likely **net** equity; gross (with arbitrage) determines the ≥65% equity-tax status.
- `age` caps at 163 (≥13.6y). `bench` = the fund's self-selected benchmark (note the inconsistency — a Module-1 problem).
- `—` = data not available (typically <5y history for 5Y CAGR, or brand-new fund).

---

## All 35 funds (sorted by AUM)

| Fund | AUM | ER | age | %Eq | %Debt | ~G+C+A | 5Y | 3Y | 1Y | Sharpe | Sortino | stdDev | Benchmark | S1 | S2 |
|------|-----|----|----|-----|-------|--------|----|----|----|--------|---------|--------|-----------|----|----|
| ICICI Pru Multi-Asset | 83,884 | 0.79 | 163 | 67.2 | 14.1 | 18.7 | 17.9 | 15.7 | 7.7 | 0.29 | 0.03 | 9.8 | NIFTY 200 TRI | ✅ | ❌ fitness → **instructive** |
| SBI Multi Asset | 19,354 | 0.74 | 161 | 46.8 | 32.8 | 20.4 | 14.2 | 16.2 | 12.3 | 0.93 | 0.09 | 9.0 | BSE 500 TRI | ✅ | **✅ SHORTLIST** |
| Nippon India Multi Asset | 16,000 | 0.43 | 72 | 56.2 | 19.6 | 24.1 | 16.4 | 19.2 | 15.0 | 0.88 | 0.09 | 11.1 | BSE 500 TRI | ✅ | **✅ SHORTLIST** |
| Kotak Multi Asset | 14,309 | 0.60 | 35 | 70.6 | 10.5 | 19.0 | — | — | 20.1 | 0.95 | 0.09 | 15.4 | NIFTY 500 TRI | ❌ age | — |
| DSP Multi Asset | 10,105 | 0.49 | 35 | 45.2 | 14.1 | 40.8 | — | — | 17.3 | 1.17 | 0.12 | 10.7 | NIFTY 500 TRI | ❌ age | — |
| WOC Multi Asset | 7,763 | 0.67 | 39 | 26.4 | 29.6 | 43.9 | — | 16.7 | 13.3 | 1.20 | 0.12 | 6.9 | CRISIL ST Bond | ✅ ⚠no-2022 | **✅ SHORTLIST** |
| Aditya Birla SL Multi Asset | 6,989 | 0.68 | 43 | 67.8 | 11.3 | 20.9 | — | 16.5 | 14.8 | 0.89 | 0.09 | 12.6 | BSE 200 | ✅ ⚠no-2022 | **✅ SHORTLIST** |
| UTI Multi Asset | 6,890 | 0.88 | 163 | 66.4 | 10.4 | 23.1 | 14.4 | 16.5 | 7.6 | 0.36 | 0.04 | 11.4 | BSE 200 TRI | ✅ | **✅ SHORTLIST** (borderline) |
| HDFC Multi-Asset | 5,881 | 1.04 | 163 | 68.0 | 14.6 | 17.4 | 12.1 | 12.4 | 5.5 | 0.20 | 0.02 | 9.0 | NIFTY 50 TRI | ✅ | ❌ fitness |
| Quant Multi Asset | 5,615 | 1.16 | 163 | 52.7 | 10.5 | 36.9 | 20.3 | 22.7 | 19.9 | 1.52 | 0.17 | 9.9 | NIFTY 500 TRI | ✅ | **✅ SHORTLIST** |
| Tata Multi Asset | 5,155 | 0.61 | 77 | 66.2 | 9.2 | 24.6 | 13.7 | 14.1 | 9.1 | 0.43 | 0.04 | 10.1 | BSE 200 | ✅ | ❌ fitness |
| Bandhan Multi Asset | 3,491 | 0.79 | 31 | 67.1 | 8.4 | 24.5 | — | — | 15.1 | 0.95 | 0.09 | 10.3 | NIFTY 500 TRI | ❌ age | — |
| Mirae Asset Multi Asset | 3,478 | 0.60 | 31 | 68.8 | 15.0 | 16.2 | — | — | 12.0 | 0.81 | 0.08 | 10.1 | NIFTY 500 TRI | ❌ age | — |
| Sundaram Multi Asset | 3,268 | 0.70 | 31 | 69.4 | 10.2 | 20.3 | — | — | 8.1 | 0.38 | 0.04 | 13.0 | NIFTY 500 TRI | ❌ age | — |
| HSBC Multi Asset | 3,041 | 1.16 | 30 | 76.2 | 10.6 | 13.2 | — | — | 16.0 | 0.93 | 0.09 | 13.3 | BSE 200 TRI | ❌ age | — |
| Edelweiss Multi Asset | 2,863 | 0.81 | 38 | 22.1 | 52.0 | 25.9 | — | 7.7 | 6.6 | 0.86 | 0.10 | 2.6 | CRISIL ST Bond | ✅ ⚠no-2022 | ❌ fitness (basically a debt fund) |
| Franklin India Multi Asset | 2,826 | 0.43 | 13 | 68.9 | 13.2 | 17.9 | — | — | — | 0.54 | 0.05 | 12.4 | NIFTY 500 TRI | ❌ age | — |
| Axis Multi Asset | 2,384 | 1.44 | 163 | 63.9 | 14.9 | 21.1 | 10.8 | 13.8 | 12.3 | 0.69 | 0.07 | 12.4 | NIFTY 500 TRI | ❌ ER | — |
| Bajaj Finserv Multi Asset | 1,875 | 0.75 | 26 | 67.3 | 6.6 | 26.1 | — | — | 11.9 | 0.69 | 0.07 | 12.5 | NIFTY 50 TRI | ❌ age | — |
| Baroda BNP Paribas Multi Asset | 1,447 | 0.93 | 44 | 67.7 | 11.6 | 20.7 | — | 15.3 | 9.7 | 0.53 | 0.05 | 12.0 | NIFTY 500 TRI | ✅ ⚠no-2022 | ❌ fitness |
| Canara Rob Multi Asset | 1,306 | 0.95 | 15 | 72.6 | 10.7 | 16.8 | — | — | 10.7 | 0.63 | 0.06 | 11.0 | BSE 200 TRI | ❌ age | — |
| Mahindra Manulife Multi Asset | 1,152 | 0.36 | 29 | 55.5 | 22.2 | 22.2 | — | — | 15.8 | 1.15 | 0.11 | 10.2 | NIFTY 500 TRI | ❌ age | — |
| Invesco India Multi Asset | 1,127 | 0.53 | 20 | 37.4 | 15.9 | 46.7 | — | — | 15.4 | 0.99 | 0.10 | 11.4 | NIFTY 200 TRI | ❌ age | — |
| Union Multi Asset | 978 | 1.28 | 23 | 69.5 | 9.3 | 21.2 | — | — | 14.4 | 0.85 | 0.08 | 13.0 | NIFTY 50 TRI | ❌ age+ER | — |
| LIC MF Multi Asset | 964 | 1.04 | 18 | 67.7 | 12.0 | 20.3 | — | — | 8.0 | 0.37 | 0.04 | 14.1 | NIFTY 500 TRI | ❌ age | — |
| 360 ONE Multi Asset | 468 | 0.60 | 12 | 23.5 | 33.2 | 43.3 | — | — | — | 1.48 | 0.15 | 12.7 | Gold-India | ❌ age+AUM | — |
| Samco Multi Asset | 410 | 2.49 | 20 | 68.6 | 11.1 | 20.3 | — | — | 3.5 | −0.05 | −0.01 | 12.1 | NIFTY 50 TRI | ❌ age+ER+Sh+AUM | — |
| Groww Multi Asset | 403 | 0.95 | 11 | 61.0 | 9.1 | 29.9 | — | — | — | −0.04 | −0.00 | 12.8 | NIFTY 500 TRI | ❌ age+Sh+AUM | — |
| Bank of India Multi Asset | 365 | 1.02 | 30 | 42.5 | 39.9 | 17.6 | — | — | 12.0 | 0.90 | 0.09 | 8.8 | NIFTY 500 TRI | ❌ age+AUM | — |
| PGIM India Multi Asset | 281 | 0.82 | 9 | 56.0 | 9.9 | 34.1 | — | — | — | 0.26 | 0.03 | 14.3 | NIFTY 500 TRI | ❌ age+AUM | — |
| The Wealth Company Multi Asset | 176 | 0.88 | 8 | 57.0 | 22.9 | 20.0 | — | — | — | 0.58 | 0.06 | 14.4 | Nifty ST Debt | ❌ age+AUM | — |
| Shriram Multi Asset | 139 | 0.62 | 35 | 66.7 | 7.8 | 25.5 | — | — | 9.8 | 0.58 | 0.06 | 11.6 | NIFTY 50 TRI | ❌ age+AUM | — |
| Quantum Multi Asset | 57 | 0.48 | 29 | 51.8 | 30.8 | 17.4 | — | — | 4.8 | 0.13 | 0.01 | 9.4 | NIFTY Composite Debt | ❌ age+AUM | — |
| Capitalmind Multi Asset | 37 | 0.82 | 5 | 55.7 | 15.9 | 28.4 | — | — | — | −0.98 | −0.10 | 6.9 | NIFTY 500 TRI | ❌ age+AUM+Sh | — |
| JM Multi Asset | ~0 | — | 1 | — | — | — | — | — | — | −1.17 | −0.24 | 8.2 | NIFTY 500 TRI | ❌ all | — |

---

## Universe statistics

| Metric | Value |
|--------|-------|
| Total funds (Direct Growth) | 35 |
| Funds ≥ 60 months (cycle-tested, saw 2022) | **8** (23%) |
| Funds ≥ 36 months (**Stage-1 track-record floor**) | **13** |
| Funds < 36 months (too new to study) | **22** (63%) |
| Funds ≥ ₹500 Cr AUM | 25 |
| ER range | 0.36% (Mahindra Manulife) – 2.49% (Samco) |
| ER median (all 35) | ~0.79% |
| Net-equity range | 22.1% (Edelweiss) – 76.2% (HSBC) |
| stdDev range | 2.6% (Edelweiss) – 15.4% (Kotak) |
| Distinct benchmarks used | **8** (NIFTY 50, NIFTY 200, NIFTY 500, BSE 200, BSE 500, CRISIL ST Bond, Nifty ST Debt, Gold-India) |
| 5Y CAGR available for | only the 8 cycle-tested funds |

## Segmentation snapshot (net-equity proxy; **bold** = shortlisted)

| Lean | Net Eq% band | Funds |
|------|--------------|-------|
| **Equity-oriented** | 63–76% | **UTI**, **ABSL**, ICICI, HDFC, Tata, Axis, Kotak, Bandhan, Mirae, Sundaram, HSBC, Franklin, Bajaj, Baroda, Canara, Union, LIC, Samco, Shriram |
| **Balanced** | 50–60% | **Nippon**, **Quant**, DSP, Mahindra, Groww, PGIM, Wealth, Capitalmind |
| **Conservative / debt-gold** | 22–47% | **SBI**, **WOC**, Edelweiss, Invesco, 360 ONE, Bank of India, Quantum |

The ≥36mo track-record floor admits the conservative sub-type (WOC shortlisted; Edelweiss reached Stage 2) — segmentation is covered across all three bands without a special relaxation.

---

*Data snapshot: July 28, 2026. All figures Direct Growth from Tickertape screener API. Gold/commodity split, net-vs-gross equity, and true taxation status are NOT in this data — they are Module-3/Module-4 factsheet tasks per [dimensions_covered.md](../dimensions_covered.md).*
