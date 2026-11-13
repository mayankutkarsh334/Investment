# MF Signal Backtest → Strategy Lab

A backtesting lab built on 13 years of Indian market data. It first answered one question: *can a small monthly investor beat funds by copying what mutual funds buy?* It's now reusable for testing **any** stock-picking or allocation idea on the same data, with the same honest rules.

## Start here

| Read | For |
|---|---|
| **[FINDINGS.md](FINDINGS.md)** | Everything learned: investment results, benchmarks, testing lessons, data gotchas |
| **[PLAYBOOK.md](PLAYBOOK.md)** | How to test a new idea: idea card, code template, gates, checklist, data refresh |
| [`ideas/`](ideas/) | One card per idea tested (write it **before** running) |
| [study_plan.md](study_plan.md) | The original plan and rules (user-confirmed decisions) |

## Headline result (Nov-2026)

- **Signal B (funds' biggest overweight bets) beats random stocks**, replicated on independent fund houses (99.9th percentile).
- **But with ₹2K→₹5K/month and −10% stops it only ties a plain small-cap fund SIP** after tax (~14.5–14.7% XIRR).
- **The original "buy what funds start small" idea (C) doesn't beat random stocks.**
- **Stop-loss rules shaped outcomes more than stock picks** in the 2014–2026 bull market.

## Phase reports

| Phase | Report |
|---|---|
| 0 Data audit | [data_audit.md](data_audit.md) |
| 1 Fund holdings (6 houses) | [phase1_holdings.md](phase1_holdings.md) |
| 2 Prices, corporate actions, benchmarks | [phase2_prices.md](phase2_prices.md) |
| 3 Signals A–D, sell flags, eligibility | [phase3_signals.md](phase3_signals.md) |
| 4 Engine (fills, costs, tax, idle money, random control) | [phase4_engine.md](phase4_engine.md) |
| 5 Results (pilot) + 14 exit variants | [phase5_results.md](phase5_results.md) |
| 6 Replication on ICICI, Axis, UTI | [phase6_plan.md](phase6_plan.md) · [phase6_results.md](phase6_results.md) |

## Quick start

```bash
cd "Stocks/MF Signal Backtest"
.venv/bin/python -I scripts/test_engine.py                 # 19 engine tests should pass
cp scripts/strategy_template.py scripts/idea_myidea.py     # edit IDEA / RULES / OPTIONS / build_rankings
.venv/bin/python -I scripts/idea_myidea.py 1000            # ~2 minutes; prints gates and benchmarks
```

`data/` (≈ 4 GB raw + 0.5 GB processed) and `.venv/` are git-ignored. Rebuild steps are in PLAYBOOK §5.

*Historical research, not investment advice.*
