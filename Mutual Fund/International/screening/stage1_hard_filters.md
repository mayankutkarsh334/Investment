# Stage 1 — Hard Filters (International Funds)

**Universe:** 53 International equity funds (Direct, Growth) | **Data:** Tickertape, May 21, 2026
**Result:** 53 → **10 survivors** (all actively managed)

Filters applied in order: (1) Open to SIP → (2) Age ≥ 5Y → (3) AUM ≥ ₹100 Cr → (4) Sharpe ≥ 0 → (5) ER ≤ 1.75%.

Full per-fund data and the pass/fail flag for every fund is in [all_funds_data.md](all_funds_data.md).

---

## Headline: The SEBI Overseas Limit Dominates

| Elimination reason | Funds removed |
|--------------------|---------------|
| **Closed to SIP** (SEBI $7bn overseas cap) | **43 of 53** |
| < 5 years old | (overlaps heavily with closed) |
| AUM < ₹100 Cr | a handful of micro-feeders |
| Sharpe < 0 / ER > 1.75% | none binding after the above |

> **The single most important screening fact:** 43 of 53 international equity funds — **including every passive NASDAQ-100, S&P-500, and MSCI-World index tracker** — are currently **closed to fresh SIP**. The closure is concentrated in the passive lane (passive funds buy overseas *ETFs* and hit the tighter $1bn sub-limit). What survives is almost entirely the **active offshore-feeder** lane.

---

## The 10 Stage-1 Survivors (all open to SIP)

| # | Fund | Region | Lane | AUM (Cr) | ER% | Age (mo) | 5Y | 3Y | 10Y | Sharpe | MaxDD% | Benchmark |
|---|------|--------|------|---------|-----|---------|-----|-----|-----|--------|--------|-----------|
| 1 | **Franklin U.S. Opportunities** | US | Active | 4,408 | 0.50 | 161 | 13.8% | 25.7% | 17.8% | 1.28 | 38.4% | Russell 3000 Growth |
| 2 | **Edelweiss US Technology** | US (tech) | Active | 3,897 | 1.48 | 75 | 19.0% | 35.3% | — | 1.50 | 45.3% | Russell 1000 Tech |
| 3 | **PGIM India Global Equity Opp** | Global | Active | 1,694 | 1.38 | 161 | 11.5% | 20.7% | 15.7% | 0.93 | 43.4% | MSCI ACWI |
| 4 | **PGIM India Emerging Markets** | EM | Active | 1,390 | 1.29 | 161 | 7.0% | 30.1% | 8.8% | 1.77 | 48.9% | MSCI EM |
| 5 | **Franklin Asian Equity** | Asia | Active | 521 | 1.39 | 161 | 7.5% | 20.4% | 11.6% | 2.09 | 40.2% | Asia ex-Japan¹ |
| 6 | **Edelweiss Europe Dynamic** | Europe | Active | 237 | 1.52 | 148 | 15.8% | 23.2% | 13.2% | 1.56 | 35.7% | MSCI Europe |
| 7 | **Edelweiss Emerging Markets Opp** | EM | Active | 221 | 1.47 | 143 | 10.6% | 28.0% | 13.8% | 2.81 | 38.8% | MSCI EM |
| 8 | **Edelweiss US Value** | US (value) | Active | 218 | 1.46 | 154 | 14.3% | 19.3% | 14.0% | 2.15 | 34.8% | Russell 1000 |
| 9 | **Edelweiss India+World Healthcare** | Thematic | Index² | 172 | 0.51 | 68 | 13.7% | 22.8% | — | 1.25 | 16.3% | MSCI India+World HC |
| 10 | **Edelweiss ASEAN** | ASEAN | Active | 146 | 1.60 | 161 | 11.0% | 14.6% | 9.8% | 1.47 | 36.1% | MSCI ASEAN |

¹ Tickertape mislabels Franklin Asian Equity's benchmark as "NIFTY 500"; the actual mandate is Asia ex-Japan equity (verify in deep study).
² Edelweiss India+World Healthcare is technically an index FoF but ~half its exposure is **Indian** healthcare — a hybrid, not pure-international (flagged for Stage 2 / deep study).

---

## Observations from the Survivor Set

- **The Edelweiss offshore-feeder family dominates** (6 of 10). Edelweiss runs a broad suite of offshore feeder funds (US Tech, US Value, Europe, EM, ASEAN, Healthcare) that remained open while passive trackers closed — so AMC-level concentration is a theme to watch, the inverse of the FlexiCap/SmallCap diversity.
- **Geographic spread is good:** US (3 — growth, tech, value), Global (1), EM (2), Europe (1), Asia/ASEAN (2), Thematic (1).
- **The cheapest investable active US exposure is Franklin US Opportunities (0.50% ER)** — an order of magnitude below the Edelweiss feeders (1.46–1.60%), because Franklin's underlying is an in-house Franklin Templeton fund (no third-party layer).
- **Every survivor is active.** The passive index lane (which would have been the *cheapest* way to own NASDAQ/S&P) is entirely closed — a structural disadvantage for the international sleeve vs the domestic ones, where cheap index options exist.

---

## Notable Eliminations (closed, but high-quality — revisit on cap reset)

These are the passive/active funds an investor would *want* but currently cannot SIP into:

| Fund | Region | Why eliminated | Re-open priority |
|------|--------|----------------|------------------|
| Motilal Oswal Nasdaq 100 FOF | US | Closed to SIP | High — cheapest, largest NASDAQ route (0.19% ER) |
| Kotak US Specific (NASDAQ) | US | Closed to SIP | High — 0.24% ER NASDAQ passive |
| Motilal Oswal S&P 500 Index | US | Closed to SIP | High — broad US passive |
| Mirae S&P 500 Top 50 / FANG+ | US | Closed to SIP | Medium — 0.02–0.03% ER, concentrated |
| HDFC Developed World Passive | Global | Closed to SIP | Medium — 0.21% ER MSCI World |
| ICICI Pru US Bluechip (active) | US | Closed to SIP | Medium — long active S&P 500 record |

> These are catalogued so the study can re-screen instantly if/when the SEBI overseas cap is raised or reset and SIPs reopen.

---

*Stage 1 complete: 53 → 10 | All survivors actively managed | Next: [stage2_performance.md](stage2_performance.md)*
