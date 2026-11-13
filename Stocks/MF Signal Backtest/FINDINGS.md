# Findings and Lessons: Copying Mutual-Fund Stock Picks (2014–2026)

> **Study period:** Nov-2026. Phases 0–6 (details in the `phaseN_*.md` files).
> **Data:** 9 fund houses' monthly portfolios (HDFC, SBI, Nippon, ABSL, DSP, PPFAS, ICICI, Axis, UTI), every NSE stock's daily price 2013–2026 (incl. delisted), corporate actions, Nifty total-return indices, and the flagship funds' NAVs.
> *Historical research, not investment advice.*

---

## 1. The question and the short answer

**Question:** if I buy, every month, the stock that mutual funds seem most keen on (₹2,000 → ₹5,000 a month, −10% stop-loss ladder, sell when funds start selling, max 24 months), do I beat simply investing the same money in funds?

**Answer:** no, not in a way that's worth it.

- **Funds' biggest overweight bets (signal B) do beat random stocks.** This was replicated on independent fund houses (99.9th percentile).
- **But under these rules the edge is tiny in rupees.** About ₹18,000–31,000 over 12 years on ₹5 lakh invested, and the final return ties a plain small-cap fund SIP.
- **The original idea fails.** Buying what funds start small (signal C) is no better than random stocks.

---

## 2. Investment findings

### 2.1 Signal results (₹2K→₹5K/month, idle money in a small-cap fund, post-tax)

| Signal | What it buys | Avg return per buy | vs random (same months, same size band) | Verdict |
|---|---|---|---|---|
| **B: biggest bets** | Stock a diversified fund holds ≥ 3 pts above the all-fund average | +4.1% (pilot 6 houses) · **+5.8% (new houses)** · +4.9% (all 9) | 98.7th · **99.9th** · 99.9th percentile | Real edge, but post-tax XIRR ≈ small-cap SIP → **not worth it under these rules** |
| D: steady buying | Total fund holdings up ≥ 5% for 3 months running | +2.5% | 92nd pct | Not beyond luck |
| A: group buying | 2+ fund houses bought it the same month | +2.3% | 87th pct | Not beyond luck |
| C: small new bets (original idea) | A fund house opened a < 2% position | +1.5% (with stops); no-stop: 60th / 23rd pct on new / all houses | 71st pct | **Rejected** |

**About B:**
- Its picks are mostly large, liquid stocks: TVS Motor, Motherson, Axis Bank, Reliance, Power Grid, Muthoot, HDFC Bank.
- It's concentrated: 22–32 different stocks over 150+ months, with a few long-held convictions repeated.
- The edge survives removing the top 3 stocks, but about half the gains came from buys made in **2023**.
- In the pilot it depended on TVS Motor; the new-houses test showed it doesn't need any single stock.

### 2.2 The exit rule mattered more than the stock choice

- **A −10% stop ends most buys fast.** On stocks moving 2–4% a day, a −10% stop (with the +15% → +5% … ladder) ends the median buy in about **1 month**. 85–97% of exits are stop-losses.
- **Random stocks under these rules average +0.5% per buy**, so the strategy becomes "small-cap fund + many small, short trades".
- **Without the stop, every signal and every random stock earned far more per buy** in 2014–2026 (+16% to +30%), because the market mostly rose.
- **But removing the stop does not create a stock-picking edge.** Random stocks held the same way did just as well (C without stops: 60th / 23rd percentile).
- **Variants don't change the picture.** Exit variants on B (5-point steps, 2×/3× ATR stop, 3/6/12-month caps, different "funds selling" thresholds, one buy per stock) moved XIRR by only ±0.1 points.

### 2.3 Benchmarks (same stepped-up monthly amounts, same dates, post-tax, Jan-2014 → Nov-2026)

| SIP into… | Post-tax XIRR | ₹5.09 lakh became |
|---|---|---|
| Nifty Midcap 150 index | 16.3% | ₹13.4 lakh |
| Nifty Smallcap 250 index (0.3% fee) | 14.7% | ₹12.2 lakh |
| 6 flagship flexi/multi-cap funds (direct) | 14.4% | ₹11.9 lakh |
| Nifty 500 index | 12.3% | ₹10.4 lakh |
| Nifty 50 index | 10.9% | ₹9.6 lakh |

Individual funds (post-tax SIP XIRR): Parag Parikh Flexi Cap 15.9%, HDFC Flexi Cap 15.8%, Nippon Multi Cap 15.1%, ABSL Flexi Cap 14.2%, DSP Flexi Cap 13.4%, SBI Flexicap 11.7%.

### 2.4 Costs of small, frequent stock trades (real rupees)

- Buying and selling a ₹5,000 position costs **₹27** (₹5.93 buy + ₹21.11 sell, including the ₹15.93 depository fee). That's 0.55% per round trip, or about 1% on ₹2,000.
- **Short-term capital-gains tax (20% + cess)** hits every stop-out profit within 12 months. Holding funds or indices defers tax to the end.
- **Small amounts limit the upside.** Even a genuine +3 to +5 points per buy edge adds little in rupees when each buy is small and short.

---

## 3. Lessons about testing ideas honestly (reuse these every time)

1. **Write the rule and the pass/fail test before running it.** Every idea here was fixed first. Rules changed after seeing results are new ideas and need new data.
2. **Compare against luck, not against zero.**
   - 1,000 random portfolios buying random affordable stocks in the same months, same size band, same exits.
   - In a rising market almost anything "makes money"; random stocks made 14.4% XIRR here.
3. **Choose a metric that separates skill from noise.**
   - When most money sits in a fund, XIRR barely moves (random portfolios: 14.2–14.7%).
   - **Average return per buy vs random** is the sharper test; XIRR answers "is it worth my money".
4. **Use several gates, not one number:**
   - ≥ 95% of random (G1);
   - works in both halves of the period (G2);
   - survives removing the 10 best buys (G3);
   - beats the simple alternatives after tax (G4);
   - doesn't depend on one stock (G5).
   - Example: 12-month momentum beat 98% of random but failed G3. It was a few lucky winners.
5. **Many tests mean many lucky passes.** At a 95% bar, 1 in 20 random ideas "passes". Tighten the bar when testing several rules (97.5% for 2), and treat the best of many variants with suspicion. About 20 variants of B produced 2–3 "passes" by tiny margins.
6. **Replicate on data that played no part in the design.** Phase 6 re-ran B on three fund houses never used before, which is far more convincing than tweaking on the same data.
7. **No look-ahead:**
   - trade only after information was public (portfolios by the 10th → buy on the 11th+);
   - use the previous day's close and liquidity;
   - assume the stop fills at the gap-down open, and that the stop hits before a new high on the same day.
8. **Keep the losers in the data.** Delisted and collapsed stocks (Yes Bank, DHFL, Jet Airways) stay in the price data. Dropping them would inflate every result.
9. **Test the test.** A placebo "signal" (random picks) must fail, and it did (65th percentile). Hand-check real trades against raw prices.
10. **Watch the period.** 2014–2026 was mostly a bull market, which flatters "hold longer" and punishes stop-losses. Only live tracking tests a new period.

---

## 4. Data lessons (gotchas found and fixed)

| Area | Lesson |
|---|---|
| Fund archives | No central dataset. Each house publishes differently (direct links, JSON APIs, session-protected APIs, zips inside zips, one file per scheme). Kotak and Mirae have no history online; Canara is CAPTCHA-protected (not bypassed). |
| Mislabelled files | DSP's "jan2016" file held Jan-2017 → always trust the "Portfolio as on …" date inside the sheet. |
| Layout drift | Column order changes; % of NAV is sometimes a fraction (0.054), sometimes a percent (5.4); some months leave the ISIN column unlabelled; HDFC's "Coupon (%)" column mimics "% to NAV"; UTI stacks all schemes in one sheet; ICICI has sub-tables. |
| Missing/incomplete months | A month with big schemes missing (UTI Oct-2023) fakes a sell-off → treat as unpublished. |
| Scheme identity | Renames are constant (SEBI 2018 and 2025). A brand-new fund's first portfolio is not "buying" → detect launches vs renames by holdings overlap. Measure signals per fund house so renames cancel out. |
| Fund types | Exclude index funds, ETFs, arbitrage, hybrids, closed-ended series, FoFs. Names lie ("New Millennium" = tech fund; "Equity Linked **Savings** Scheme" = ELSS). Combine name rules with % in Indian equity and % in bonds. |
| Company identity | ISIN changes at a split → key companies by the first 7 characters of the ISIN (issuer). |
| Splits and bonuses | NSE's previous close is not adjusted. NSE's corporate-action feed has abbreviations ("Fv Splt Frm"), combined lines ("Div Rs 6 + Split Rs 10 → Re 1"), missing demergers → validate every factor against the actual price gap (98.7% match). |
| Fund share counts | Convert to today's share units, or splits look like buying (87% → 22% false jumps). |
| Benchmarks | Use total-return indices (dividends reinvested), minus a realistic fund fee. |

---

## 5. Open questions worth testing later (each is a new idea and needs a new test)

- **B with different money rules:** larger amount per pick, or a fixed share of the portfolio, so the edge matters in rupees. This must be tested live (paper-trade), since the 2014–26 data has already been seen.
- **B's time profile:** how many weeks after disclosure does the excess return appear and fade? That would inform the holding period.
- **Non-fund ideas** on the same engine: momentum, quality/value screens, index rotation. Use `scripts/strategy_template.py`.
- **More fund houses** (Tata, Motilal, Bandhan, HSBC, Invesco…), if their archives can be reached without bypassing protections.
