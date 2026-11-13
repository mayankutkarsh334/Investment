# Phase 3: Buy Signals and "Funds Selling" Flags

> **Done:** Nov-12-2026 (updated same day for the stepped-up monthly amount). For every month from Dec-2013 to Oct-2026, each signal now has a ranked list of eligible stocks. The #1 is that month's ₹5,000 pick, and lower ranks are used when you already hold 3 lots of the #1. Every stock-month also carries a "funds selling" flag for the exit rule.
> **Deliberately not done yet:** no returns have been looked at. The rules below were fixed **before** seeing any performance, so they can't be tuned to make the results look good.

---

## 1. What each fund house did each month (`fund_flows.py` → `fund_actions.parquet`)

Each fund house (HDFC, SBI, Nippon, ABSL, DSP, PPFAS) gets **one vote per company per month**. Its split-adjusted shares this month are compared with its previous published month:

| Action | Rule |
|---|---|
| **new** | held now, not last month, worth ≥ ₹1 crore (smaller = `new_tiny`, not a vote) |
| **increase** | shares up ≥ 10% beyond the house's normal flow, and ≥ ₹50 lakh added |
| **cut** | shares down ≥ 10% beyond flow, and ≥ ₹50 lakh removed |
| **exit** | held last month, not now |
| **hold** | anything else |

**Two corrections make the votes trustworthy:**

1. **New fund launches are excluded in their first month.** A brand-new fund's first portfolio is bought with fresh investor money, not a change of view. Treating it as buying would flood the signal (e.g. HDFC Defence 2023, Manufacturing 2024, Multi Cap 2021).
   - A scheme is a **rename, not a launch**, when at least 50% of its holdings match a scheme that disappeared the same month. Renames carry over normally.
   - This also catches HDFC "Mid Cap Opportunities", which alternates between two spellings. Without the check, the second spelling looked like HDFC dumping its whole mid-cap book.
   - 51 genuine launches found.
2. **Flow adjustment.** "Increase" is measured against the house's typical share growth that month, so inflows that make a fund buy a bit of everything don't count as conviction. In practice the median is 1.00: funds mostly leave holdings untouched month to month.

**Missing months:** across Nippon's 2 and SBI's 3 unpublished months, the next month is compared with the last published one. The house simply has no vote in the missing month.

---

## 2. The four buy signals (`signals.py` → `signals.parquet`)

**Skip rule (user-confirmed):** a stock flagged "funds selling" in the same month is skipped and the next-ranked stock is taken. This affected about 4 (A), 11 (B), 4 (C) and 0 (D) of ~155 monthly #1 picks. After the skip, months with a pick: A 155, A3 148, B 155, C 155, D 153, D2 154 (of 155). **Each signal is run as a separate strategy** in the first backtest.

| Signal | Qualifies when | Ranked by | Eligible candidates / month (median) |
|---|---|---|---|
| **A: group buying** | **2+ fund houses** bought (new or increase) the same month | number of houses buying → houses opening new positions → ₹ bought | 24 |
| A3 (variant) | 3+ houses | same | 4 (4 months with none) |
| **B: biggest bets** | a **diversified** fund holds it **≥ 3 percentage points above** the average weight across all pilot funds | that excess weight | 73 |
| **C: small new bets** (your original idea) | a house **opened a new position at < 2% weight** | number of such houses → ₹ bought | 19 |
| **D: steady buying** | total fund shares up ≥ 5% (flow-adjusted) for **3+ months in a row** | streak length → total rise over the streak | 10 (2 months with none) |
| D2 (variant) | 2+ months in a row | same | 26 |

**Differences from the original plan:**
- **B:** the plan said "≥ 2× its benchmark weight", but historical index weights aren't publicly available. B instead uses **weight above the average of all 6 houses' funds**, which also measures how much a fund departs from the crowd.
  - Sector and thematic funds are excluded from B. A banking fund holding 20% in HDFC Bank is its mandate, not conviction.
  - That exclusion caught two disguised funds: ABSL's "New Millennium" is a technology fund (it made Infosys the B pick in 52 months), and DSP's "India T.I.G.E.R." is an infrastructure fund.
- **C:** "stocks funds hold at < 2%" is mostly a permanent state, not a monthly decision. So C uses the **moment** a fund house starts a small (< 2%) position, a fresh starter bet. This is the closest testable version of your idea.

**What the picks look like:**

| Signal | Different stocks picked over 155 months | Most repeated picks | Example |
|---|---|---|---|
| A | 114 | Kotak Bank 4, ITC 3, Bank of Baroda 3 | Jun-2020 Kotak Bank: 4 houses bought ₹7,284 crore (the 2020 block deal) |
| B | 23 | TVS Motor 37, HDFC Bank 18, HDFC 14, Axis 13 | Very persistent; your 3-lot cap will push it to the next-ranked stock |
| C | 134 | Jubilant Foodworks 4, Tata Steel 3 | Mostly mid and small caps being started small |
| D | 87 | Jubilant Foodworks 5, Newgen 4, Coal India 4 | Often smaller stocks funds keep building up |

---

## 3. "Funds selling" flags (for the exit rule)

| Flag | Rule | How often it fires on held stock-months |
|---|---|---|
| **sell_default** | 2+ houses cut or exit, **or** total fund shares fall ≥ 20% | 6.8% |
| sell_3h (variant) | 3+ houses cut or exit | — |
| sell_10pct (variant) | 2+ houses, or total fall ≥ 10% | — |

**Checks:**
- **Yes Bank:** fires in **Sep-2018 and Oct-2018**. 4 of 6 houses cut, and total fund holdings fell to 30% of the previous month. A follower would have sold by about mid-October 2018, long before the 2020 collapse.
- **Infosys Sep-2018 bonus month:** no false sell. The split adjustment works.

---

## 4. Timing and eligibility (no look-ahead)

- **Action date** = first trading day on or after the **11th of the next month** (portfolios are due by the 10th). In practice it falls on the 11th–14th, always in the next month.
- **Reference price** = previous day's close, and **liquidity** = average traded value of the 20 sessions **before** the action date. Neither uses data from the buy day itself.
- **Eligible to buy:**
  - trades on the action date;
  - normal series (EQ/BE), not BZ (non-compliant) or SME (lot sizes far above ₹5,000);
  - **price ≤ that year's monthly amount** (₹2,000 in 2014, rising ~7.94% each January to ₹5,000 in 2026), so one share is affordable;
  - **average daily traded value ≥ ₹1 crore**.
- 79% of signal stock-months pass (67% in 2014 with the ₹2,000 cap, 89% in 2026). Every signal except A3 and D has a candidate in every month.

---

## 5. Known limitations

1. **Scheme classification used the full history.** Whether a scheme counts as "active equity" was decided once using all its months, which is a mild look-ahead. In practice a scheme's type doesn't change.
2. **No market-cap buckets yet.** The random-stock control (Phase 4) will draw from eligible stocks in the same **liquidity band** (20-day traded value quintile) as a size proxy.
3. **Signals see only month-end snapshots.** A fund that buys and sells within a month leaves no trace.
4. **B is persistent by design.** Conviction bets last years, so B's #1 repeats. The cap of 3 lots per stock handles this in the simulation.

---

## 6. Files

- `scripts/fund_flows.py` → `data/processed/fund_actions.parquet` (231,946 house-company-month rows)
- `scripts/signals.py` → `data/processed/signals.parquet`: 95,935 company-month rows with votes, all signal scores, `q_*` (qualifies), `rank_*` (1 = pick), sell flags, action date, reference price, liquidity and eligibility
