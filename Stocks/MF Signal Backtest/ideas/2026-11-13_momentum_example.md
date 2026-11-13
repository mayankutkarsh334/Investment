# Idea: 12-month price momentum (template example)    Date: 2026-11-13    Test # in batch: 1 (smoke run)

> Example card showing the format. The run below used **100** random portfolios (a smoke run), not the full 1,000, so it isn't a formal test.

## Hypothesis
Stocks with the highest total return over the last 12 months keep beating random stocks.

## Buy rule
- Universe: affordable (price ≤ monthly amount), ≥ ₹1 cr/day traded, EQ/BE.
- Rank by: total-return index on the day before the action date ÷ value ~365 days earlier.
- Pick: rank 1 (next if 3 lots held or unaffordable).

## Exit rule
- −10% stop ladder (+15% → +5% … 10-point steps), 24-month cap, no funds-selling exit.

## Money rules
- ₹2,000 (2014) → ₹5,000 (2026), +7.94% each January; idle money in the small-cap index fund.

## Pass / fail
- G1 ≥ 95% of random on average return per buy; G2 both halves; G3 without top-10 buys; G4 post-tax XIRR beats the Nifty 500, 6-fund and small-cap SIPs.

## Result (smoke run, 100 random portfolios)

| Measure | Result |
|---|---|
| Buys | 145 |
| Average per buy | +5.73% |
| Median per buy | −10.6% |
| Win rate | 42% |
| Median days held | 11 |
| Random portfolios | median −0.22%, 5th–95th −2.35% … +1.62% → **beats 98%**, t 0.82 |
| 2014–19 / 2020–26 | −0.59% / +10.45% (random −0.69% / +0.11%) |
| Without its 10 best buys | **−1.34% → fails G3** |
| Post-tax XIRR | 15.27% vs small-cap SIP 14.69% |

**Gates:** G1 ✅, G2 ✅ (barely), **G3 ❌**, G4 ✅.

**Verdict:** not passed. A few huge winners carry the average; the typical buy loses 10% within two weeks. If pursued, it needs a properly pre-registered run (1,000 portfolios) and a replication.
