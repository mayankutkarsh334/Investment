# Stage 1 — Hard Filters (Fund-by-Fund Elimination Log)

**Universe:** 35 Multi Asset Allocation Funds (Direct Growth, Tickertape API, Jul 28 2026).
**Filters (in order):** ER ≤ 1.2% · AUM ≥ ₹500 Cr · AUM max = none · **Track record ≥ 36 months** · Sharpe ≥ 0.
**Result: 35 → 11.**

> **The age filter was replaced.** A rigid ≥60-month filter guts this post-2023 category (35 → 7) and eliminates the entire conservative sub-type. Its real purpose was data sufficiency + stress exposure, so it is replaced with a **≥36-month track-record floor** (enough NAV for the framework's 3Y metrics; covers the Sep-2024–Mar-2025 correction). "Saw 2022" becomes a per-fund `no-2022-data` flag, not a cut (MidCap precedent). See [methodology.md](methodology.md) §5.

---

## The funnel at a glance

| Filter | Funds eliminated | Running total |
|--------|------------------|---------------|
| Start | — | 35 |
| **Track record ≥ 36 months** | **22** (all <36mo) | 13 |
| ER ≤ 1.2% | 2 (Axis 1.44, Union 1.28) | 11 |
| AUM ≥ ₹500 Cr | 0 additional (sub-₹500 funds already out on age) | 11 |
| Sharpe ≥ 0 | 0 additional | **11** |

---

## Stage 1 survivors (11)

| Fund | AMC | AUM (₹Cr) | ER | Age (mo) | Sharpe | Flag |
|------|-----|-----------|----|----|--------|------|
| ICICI Pru Multi-Asset | ICICI Prudential | 83,884 | 0.79 | 163 | 0.29 | — |
| SBI Multi Asset Allocation | SBI | 19,354 | 0.74 | 161 | 0.93 | — |
| Nippon India Multi Asset | Nippon Life India | 16,000 | 0.43 | 72 | 0.88 | — |
| WOC (WhiteOak) Multi Asset | WhiteOak | 7,763 | 0.67 | 39 | 1.20 | ⚠ no-2022-data |
| Aditya Birla SL Multi Asset | Aditya Birla SL | 6,989 | 0.68 | 43 | 0.89 | ⚠ no-2022-data |
| UTI Multi Asset | UTI | 6,890 | 0.88 | 163 | 0.36 | — |
| HDFC Multi-Asset | HDFC | 5,881 | 1.04 | 163 | 0.20 | — |
| Quant Multi Asset | Quant | 5,615 | 1.16 | 163 | 1.52 | — |
| Tata Multi Asset | Tata | 5,155 | 0.61 | 77 | 0.43 | — |
| Edelweiss Multi Asset | Edelweiss | 2,863 | 0.81 | 38 | 0.86 | ⚠ no-2022-data |
| Baroda BNP Paribas Multi Asset | Baroda BNP Paribas | 1,447 | 0.93 | 44 | 0.53 | ⚠ no-2022-data |

The `no-2022-data` flag marks the 36–59mo funds that never traversed the 2022 all-classes-diverge year; their Modules 1/2 lean on the 2024–25 correction and note the gap.

---

## Eliminations

### By track record < 36 months (22 funds) — the youngest of the post-2023 wave

Ordered by AUM. The `~G+C+A%` column = 100 − %equity − %debt = the gold + cash + arbitrage sleeve the API hides. Note how many are **large** despite being toddlers — a flow surge into a tax-driven product.

| Fund | AUM (₹Cr) | Age (mo) | Net Eq% | Debt% | ~G+C+A% | Also fails |
|------|-----------|----------|---------|-------|---------|------------|
| Kotak Multi Asset | 14,309 | 35 | 70.6 | 10.5 | 19.0 | — (just misses 36mo) |
| DSP Multi Asset | 10,105 | 35 | 45.2 | 14.1 | 40.8 | — (just misses; → instructive case) |
| Bandhan Multi Asset | 3,491 | 31 | 67.1 | 8.4 | 24.5 | — |
| Mirae Asset Multi Asset | 3,478 | 31 | 68.8 | 15.0 | 16.2 | — |
| Sundaram Multi Asset | 3,268 | 31 | 69.4 | 10.2 | 20.3 | — |
| HSBC Multi Asset | 3,041 | 30 | 76.2 | 10.6 | 13.2 | ER 1.16 (borderline) |
| Bajaj Finserv Multi Asset | 1,875 | 26 | 67.3 | 6.6 | 26.1 | — |
| Canara Rob Multi Asset | 1,306 | 15 | 72.6 | 10.7 | 16.8 | — |
| Mahindra Manulife Multi Asset | 1,152 | 29 | 55.5 | 22.2 | 22.2 | — (cheapest ER 0.36) |
| Invesco India Multi Asset | 1,127 | 20 | 37.4 | 15.9 | 46.7 | — (conservative/gold-heavy) |
| LIC MF Multi Asset | 964 | 18 | 67.7 | 12.0 | 20.3 | — |
| 360 ONE Multi Asset | 468 | 12 | 23.5 | 33.2 | 43.3 | AUM |
| Samco Multi Asset | 410 | 20 | 68.6 | 11.1 | 20.3 | ER 2.49, Sharpe −0.05, AUM |
| Groww Multi Asset | 403 | 11 | 61.0 | 9.1 | 29.9 | Sharpe −0.04, AUM |
| Bank of India Multi Asset | 365 | 30 | 42.5 | 39.9 | 17.6 | AUM (conservative) |
| PGIM India Multi Asset | 281 | 9 | 56.0 | 9.9 | 34.1 | AUM |
| The Wealth Company Multi Asset | 176 | 8 | 57.0 | 22.9 | 20.0 | AUM |
| Shriram Multi Asset | 139 | 35 | 66.7 | 7.8 | 25.5 | AUM (just misses 36mo) |
| Quantum Multi Asset | 57 | 29 | 51.8 | 30.8 | 17.4 | AUM, near-zero Sharpe (0.13) |
| Capitalmind Multi Asset | 37 | 5 | 55.7 | 15.9 | 28.4 | AUM, Sharpe −0.98 |
| JM Multi Asset | ~0 | 1 | — | — | — | everything |

*(21 listed + Union below = the funds under 36mo; Union additionally fails ER.)*

### By ER > 1.2% — 2 funds

| Fund | ER | Age (mo) | Note |
|------|----|----|------|
| **Axis Multi Asset** | 1.44% | 163 | Cycle-tested but expensive; 5Y CAGR 10.8% (weakest old fund); benchmarks NIFTY 500 TRI. High fee + weak return — clean cut. |
| **Union Multi Asset** | 1.28% | 23 | Fails ER **and** age. |

---

## Observations

1. **Two funds just miss the 36mo line — Kotak and DSP (both 35mo, both large).** DSP (₹10,105 Cr, Sharpe 1.17) becomes the young "new-wave" **instructive case**; Kotak is noted as the largest young equity-heavy fund.
2. **The ≥36mo floor naturally admits the conservative sub-type** — WOC (39mo) and Edelweiss (38mo) both clear it, so segmentation no longer needs a special relaxation.
3. **AUM min and Sharpe never bind independently** — every sub-₹500 Cr / negative-Sharpe fund is also <36mo.
4. **Only one cycle-tested fund is lost outside age** — Axis, on ER.

---

*Stage 1 complete: 35 → 11. The ≥36mo track-record floor (replacing ≥60mo) eliminated 22; Axis & Union on ER. Next: [stage2_performance.md](stage2_performance.md).*
