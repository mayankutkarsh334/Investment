# Phase 6: Results (Replication on New Fund Houses)

> **Run:** Nov-13-2026, once, with the two tests and five gates fixed beforehand in [phase6_plan.md](phase6_plan.md).
> **Datasets:**
> - **NEW** = ICICI Prudential, Axis and UTI only (never used in designing anything); signals from May-2014.
> - **ALL** = all 9 fund houses; signals from Dec-2013.
>
> Same rules as Phase 5: ₹2,000 → ₹5,000 a month (+7.94% each January), idle money in the small-cap fund, today's tax rules.
> *Historical test, not investment advice.*

---

## 1. Verdict

| Test | NEW (independent houses) | ALL (9 houses) | Outcome under the pre-set rule |
|---|---|---|---|
| **H1: B (biggest bets) with your rules** | Passes G1, G2, G3, G5 · **fails G4** | Passes G1, G2, G3, G5 · **fails G4** | **Inconclusive** (not confirmed, not rejected) |
| **H2: C (small new bets) without stop-losses** | **Fails G1** (60th percentile) | Fails G1 (23rd percentile) | **Rejected** |

**In plain words:**

1. **B's stock-picking edge is real.**
   - On three fund houses that played no part in designing the test, the stocks a diversified fund holds far above average went on to beat random stocks by about **+5 points per buy**.
   - That beats **99.9%** of 1,000 random portfolios, both before and after 2020.
   - It is **not** a one-stock result.
   - The same holds with all 9 houses combined.
2. **But under your rules it still doesn't make you more money than a small-cap fund.**
   - B's post-tax XIRR is **14.50% (NEW) and 14.62% (ALL)**, vs **14.56% / 14.69%** for a plain SIP into the small-cap fund.
   - Each buy is small (₹2,000–5,000) and usually stopped out within ~2–3 months (89% stop exits).
   - So the edge adds only about **₹31,000 over 12 years** on ₹5 lakh invested, while the money waiting in the small-cap fund earns about as much anyway.
3. **Your original idea (C) doesn't survive.** Phase 5's promising "C without stops" result was the 2014–2026 bull market, not the signal. On the new houses C does no better than random stocks held the same way.

---

## 2. Data added

| Fund house | Months | Notes |
|---|---|---|
| **ICICI Prudential** | Apr-2014 → Oct-2026 (150 of 151) | Site download API; May-2017 not published |
| **Axis** | Jan-2013 → Oct-2026 (161 of 166) | Site API via the page's own session. Missing: Nov-2013 (unreadable), Jul-2014 (password-protected), Mar-2019, Sep-2019, Apr-2023 |
| **UTI** | Jan-2014 → Oct-2026 (150 of 154) | Consolidated zips to Sep-2023, then scheme-wise files (the zips stopped including holdings). Missing: Sep-2014, Apr-2019, Jul-2024; **Oct-2023 excluded** (incomplete: Flexi Cap and MNC files absent) |
| Canara Robeco | — | Excluded: archive behind a reCAPTCHA, not bypassed |
| Tata, Motilal, Bandhan, Sundaram, Invesco, HSBC, quant, Edelweiss | — | Archives not exposed on their landing pages; not added (possible future work) |

**Checks:**
- **Sizes match their real growth:** ICICI's active equity went from ~₹30,000 crore to ₹3.9 lakh crore, Axis from ~₹2,000 crore to ₹1.8 lakh crore, UTI from ~₹26,000 crore to ₹88,000 crore.
- **Top holdings match:** ICICI Bluechip 2019 (HDFC Bank 8.5%, ICICI Bank, Infosys, Axis Bank), Axis Bluechip 2020 (HDFC Bank, Bajaj Finance, Infosys, Kotak) and UTI Flexi Cap 2024 (ICICI Bank, HDFC Bank, Bajaj Finance, Zomato).
- **Classification:** 128 new active-equity schemes (ICICI 59, Axis 25, UTI 44); 96 genuine launches excluded across all houses.
- **Phase 5 unaffected:** the 6 pilot houses' data is unchanged by the parser updates (same month counts and flags). Phase 5's signals file is backed up as `signals_PILOT_phase5.parquet`.

**Parser upgrades needed:**
- UTI stacks every scheme in one sheet → split into blocks at each "SCHEME:" title. Only when every table has its own title, so ICICI's sub-tables aren't split.
- Zips inside zips (UTI).
- ICICI, Axis and UTI fund-house titles not mistaken for scheme names.
- UTI links with spaces or relative paths.

---

## 3. Results in detail

### H1: B (biggest bets), your original rules

| | NEW | ALL |
|---|---|---|
| Buys | 150 | 155 |
| **Avg return per buy** | **+5.77%** | **+4.90%** |
| Random portfolios: median (95th pct) | +0.78% (+2.89%) | +0.75% (+2.55%) |
| **Beats % of random** | **99.9%** ✅ (bar 97.5%) | **99.9%** ✅ |
| t-stat vs random (clustered by stock) | 2.18 | 2.40 |
| 2014–19 / 2020–26 (random) | +1.71% (−0.18%) / +9.05% (+1.63%) ✅ | +3.29% (+0.49%) / +6.29% (+0.93%) ✅ |
| Without its 10 best buys | +1.96% ✅ | +1.27% ✅ |
| Without its most-bought stock | Motherson ×35 removed: **+6.86%** ✅ | TVS Motor ×48 removed: **+3.05%** ✅ |
| Without its top 2–3 stocks (extra check) | +4.02% / +4.01% (still above p95) | +3.42% / +3.54% (still above p95) |
| Median days held · win rate | 79 · 56% | 53 · 52% |
| **Post-tax XIRR** | **14.50%** | **14.62%** |
| Small-cap SIP / 6-fund SIP / Nifty 500 SIP | 14.56% / 14.31% / 12.18% | 14.69% / 14.42% / 12.25% |
| **G4** | ❌ (−0.06 pt) | ❌ (−0.07 pt) |

**Caveats on H1:**
- **Concentrated in time:** about half of all gains come from buys made in **2023** (+35% average that year). 2018 and 2019 were negative.
- **Concentrated in names:** NEW's top picks were Motherson (35 buys), TVS Motor (30), Power Grid (13) and Sun Pharma (10), only 26 different stocks in 150 months. The edge survives removing the top 3, but it comes from a few long-held conviction bets.
- **Overlap with the pilot result:** TVS Motor was also the top pick in the pilot data. Fund houses partly share ideas, so NEW isn't fully independent of the pilot six.

### H2: C (small new bets) without price stop-losses

| | NEW | ALL |
|---|---|---|
| Avg return per buy | +23.9% | +12.0% |
| Random no-stop portfolios: median (95th pct) | +22.2% (+36.6%) | +15.7% (+27.8%) |
| **Beats % of random** | **59.9%** ❌ | **23.2%** ❌ |
| t-stat | 0.07 | −1.08 |
| Post-tax XIRR | 15.25% | 15.02% |
| Random no-stop XIRR (median) | 14.41% | 14.49% |

**Why H2 fails despite its high XIRR:** holding without stops did beat the small-cap SIP, but **random stocks held the same way did too**. The extra return came from the 2014–2026 rising market, not from picking the stocks funds started small. Under the plan's rule (fails G1 on NEW) H2 is **rejected**.

---

## 4. What this means for you

| Question | Answer from 2014–2026 data |
|---|---|
| Do fund managers' biggest overweight bets beat random stocks over the next few months? | **Yes, consistently** (99.9th percentile on independent fund houses, t ≈ 2.2–2.4) |
| Does copying them with ₹2,000–5,000/month, −10% stops and the funds-selling exit make more money than a small-cap fund SIP? | **No.** It ties or trails slightly (−0.06 to −0.07 pt XIRR) |
| Does "buy what funds start small" (your original idea) work? | **No.** Not better than random, with or without stops |
| Is there anything worth pursuing? | B's edge is real but small per rupee under these rules. Turning it into money would need **different rules** (larger amounts per pick, different exits). Those would be **new hypotheses**, and testing them on this same 2014–2026 data would be fitting to results already seen |

**Under the plan's outcome table, H1 is "inconclusive" → paper-trade at most, no real money.** A practical reading: a plain SIP into a good small-cap or flexi-cap fund did as well, with no monthly work, taxes on short trades, or stock-specific risk.

---

## 5. Limitations

1. **Same market period.** All data is 2014–2026, mostly rising. Only live tracking after Nov-2026 tests a new period.
2. **NEW isn't fully independent.** Fund houses share ideas (TVS Motor and Motherson appear in both). The replication is strong evidence, not proof.
3. **UTI Nov-2023** shows more cuts than usual (54 vs a typical 15–35) because two small schemes closed during its format switch. One house, one month, small effect.
4. **9 of ~40 fund houses.** Big ones are covered (HDFC, ICICI, SBI, Nippon, ABSL, Axis, UTI, DSP, PPFAS). Kotak and Mirae have no history online.
5. **Phase 4 simplifications** apply: index proxy for the small-cap fund, dividends credited at exit, per-buy tax lots, 30% slab on dividends.

---

## Files

- `scripts/icici_links.py`, `scripts/uti_schemewise.py`, Axis links (`data/raw/links_axis.csv`, built from the site API)
- `scripts/run_phase6.py` → `data/results/phase6_summary.csv`, `phase6_<NEW|ALL>_<H1|H2>.pkl`
- `scripts/signals.py NEW|ALL` → `signals_NEW.parquet`, `signals_ALL.parquet`
- `scripts/fund_flows.py`: `DROP_MONTHS` (UTI Oct-2023)
