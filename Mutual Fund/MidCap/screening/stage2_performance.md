# Stage 2 — Performance Filters: 15 → 7

**Both conditions must be met:**

| Filter | Threshold | Value used |
|--------|-----------|------------|
| 5Y CAGR | **strictly > full-universe median** | 17.63% (median of 25 non-null values across all 33 funds) |
| 3Y CAGR ÷ universe mean 3Y | **> 1.0x** | mean = 20.27% (29 non-null values) — computed substitute for Tickertape's premium "returns vs sub-category 3Y" field |

---

## Results (15 survivors, sorted by 5Y CAGR)

| Fund | 5Y CAGR | vs median 17.63% | 3Y ratio | Verdict |
|------|---------|------------------|----------|---------|
| **Invesco India Midcap** | 21.91% | ✅ | 1.327x ✅ | **PASS** |
| **Nippon India Growth Mid Cap** | 21.48% | ✅ | 1.140x ✅ | **PASS** |
| **Edelweiss Mid Cap** | 20.64% | ✅ | 1.186x ✅ | **PASS** |
| **HSBC Midcap** | 20.44% | ✅ | 1.366x ✅ | **PASS** |
| **Mahindra Manulife Mid Cap** | 20.17% | ✅ | 1.168x ✅ | **PASS** |
| **Sundaram Mid Cap** | 19.31% | ✅ | 1.099x ✅ | **PASS** |
| **ICICI Pru Midcap** | 19.01% | ✅ | 1.221x ✅ | **PASS** |
| Union Midcap | 17.73% | ✅ (+0.10) | 0.974x ❌ | Out — passed 5Y by a whisker, failed 3Y |
| Baroda BNP Paribas Mid Cap | 17.63% | ❌ (= median exactly) | 1.046x ✅ | Out — **the nearest miss**; its 5Y *is* the median and the rule is strictly-greater |
| Mirae Asset Midcap | 17.43% | ❌ | 0.974x ❌ | Out — failed both narrowly; also no 2018 data (85mo) |
| ITI Mid Cap | 17.36% | ❌ | 1.161x ✅ | Out — good 3Y momentum, insufficient 5Y |
| Tata Mid Cap | 17.24% | ❌ | 0.949x ❌ | Out |
| Aditya Birla SL Midcap | 16.73% | ❌ | 0.942x ❌ | Out |
| Axis Midcap | 15.66% | ❌ | 0.891x ❌ | Out — the former category darling; quality-growth style out of favour since 2021 |
| DSP Midcap | 13.28% | ❌ | 0.918x ❌ | Out — **worst 5Y of all Stage-1 survivors**; ironic given DSP Small Cap ranked #1 in the SmallCap study — AMC quality does not transfer across categories |

---

## Final Shortlist (7 funds)

| # | Fund | AUM (Cr) | ER% | 10Y | 5Y | 3Y | 1Y | Sharpe | Vol | Mid%* |
|---|------|----------|-----|------|------|------|------|--------|------|------|
| 1 | **Invesco India Midcap** | 12,397 | 0.49 | **20.34%** | **21.91%** | 26.91% | 10.01% | 0.408 | 16.9% | 52.1 |
| 2 | **Nippon India Growth Mid Cap** | 47,415 | 0.73 | 19.32% | 21.48% | 23.10% | 7.21% | 0.264 | 15.7% | 58.1 |
| 3 | **Edelweiss Mid Cap** | 16,849 | 0.48 | 19.88% | 20.64% | 24.05% | 5.16% | 0.135 | 15.2% | 60.9 |
| 4 | **HSBC Midcap** | 14,249 | 0.56 | 18.47% | 20.44% | **27.68%** | **17.50%** | **0.848** | 16.2% | 51.4 |
| 5 | **Mahindra Manulife Mid Cap** | 4,866 | **0.42** | — (103mo) | 20.17% | 23.67% | 9.60% | 0.405 | 15.9% | 72.2 |
| 6 | **Sundaram Mid Cap** | 13,687 | 0.88 | 15.63% | 19.31% | 22.27% | 6.41% | 0.210 | 15.2% | 66.3 |
| 7 | **ICICI Pru Midcap** | 7,789 | 0.87 | 17.78% | 19.01% | 24.75% | 11.36% | 0.456 | 17.5% | 68.7 |

*\*Mid% per Tickertape's own cap classification (not AMFI) — apparent sub-65% values are a classification artifact, verified per fund in Module 3.*

**Category St Dev: 15.26% | Category PE: 33.76**

---

## Shortlist Observations (questions for the deep studies)

1. **Invesco leads both long windows** (20.34% 10Y, 21.91% 5Y) at a cheap 0.49% — and Invesco India Smallcap made that study's shortlist too. Same AMC-sale-to-Hinduja-group question carries forward from the SmallCap study's Module 6.
2. **HSBC's Sharpe (0.848) is the Union-SmallCap anomaly repeated** — triple the shortlist's typical level, driven by a 17.5% 1Y return (best in the universe by far). Whether this is durable style positioning or a hot streak is HSBC's central study question. Note: HSBC Midcap = the former L&T Midcap Fund (L&T MF was acquired by HSBC AMC in 2022) — the long track record belongs partly to another house.
3. **Nippon is the capacity question personified** — ₹47,415 Cr, just under the cut. Its Module 4 forced-deployment and active-share-decay analysis effectively doubles as the HDFC/Kotak instructive case from inside the shortlist.
4. **Mahindra Manulife is the value pick profile** — cheapest ER (0.42%), smallest AUM (₹4,866 Cr, maximum agility), ~Dec-2017 inception (near-full 2018-winter coverage), but the youngest record and an AMC never studied before.
5. **Sundaram repeats its SmallCap pattern** — passes screening on recent form, but the weakest 10Y (15.63%) and the priciest ER (0.88%) of the shortlist; likely the confirm-the-elimination study again.
6. **Five of seven AMCs are known quantities** — Edelweiss, HSBC, Invesco, Sundaram have full AMC verdicts from prior studies; ICICI was touched in the International foundation. Only Nippon and Mahindra Manulife AMCs need ground-up Module 6 work.
7. **All seven passed both filters with margin except Sundaram/ICICI on 5Y** — the shortlist has a clear top-4 (Invesco, Nippon, Edelweiss, HSBC) and a bottom-3 on raw screening numbers; deep study will test whether that ordering survives risk, cost, and manager scrutiny.

---

## Eliminated-but-instructive (optional deep-dives)

| Fund | Why instructive | Analog |
|------|----------------|--------|
| **HDFC Mid Cap** (₹97,350 Cr) | What does the category's largest AUM do to a 150-stock mandate? Active share, holding count, index-hugging | quant Small Cap study |
| **Motilal Oswal Midcap** (Sharpe −0.69) | The momentum-concentration style: best 5Y CAGR in the universe → worst 1Y; what the 2024–25 correction did to a 20-stock high-conviction book | none — new failure mode |

---

*Stage 2 completed: July 3, 2026 | 15 → 7 | Median 5Y = 17.63% (full universe, n=25) | Mean 3Y = 20.27% (n=29) | Data: Tickertape API (Direct Growth), July 3, 2026*
