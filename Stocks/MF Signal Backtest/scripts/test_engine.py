"""Phase 4: hand-checkable tests of the engine on made-up price paths.

Run: .venv/bin/python -I scripts/test_engine.py   (prints PASS/FAIL per case)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import engine as E  # noqa: E402


class FakePrices(E.Prices):
    def __init__(self, paths: dict, sell: dict = None):
        self.a, self.sell = {}, {"sell_default": {}, "sell_3h": {}, "sell_10pct": {}}
        for iss, rows in paths.items():
            dates = pd.bdate_range("2020-01-01", periods=len(rows)).values.astype("datetime64[D]")
            o, h, l, c = (np.array([r[i] for r in rows], float) for i in range(4))
            self.a[iss] = {"date": dates, "open_raw": o, "o": o, "h": h, "l": l, "c": c,
                           "div": np.zeros(len(rows)), "gap": np.zeros(len(rows))}
        for iss, idxs in (sell or {}).items():
            self.sell["sell_default"][iss] = np.array([self.a[iss]["date"][i] for i in idxs])


def flat(n, p=100.0):
    return [(p, p, p, p)] * n


results = []


def check(name, got, want, tol=1e-9):
    ok = (got == want) if isinstance(want, str) else abs(got - want) <= tol
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: got {got}, want {want}")


d = lambda fp, i: pd.Timestamp(fp.a["X"]["date"][i])  # noqa: E731

# 1. falls 10% intraday on day 3 -> stopped at exactly -10%
fp = FakePrices({"X": flat(3) + [(99, 99, 89, 90)] + flat(600, 90)})
r = E.simulate_lot(fp, "X", d(fp, 0))
check("stop at -10%: reason", r.reason, "stop"); check("stop at -10%: ret", r.ret, 0.90)

# 2. gap down below the stop -> filled at the (worse) open
fp = FakePrices({"X": flat(3) + [(80, 82, 79, 81)] + flat(600, 81)})
r = E.simulate_lot(fp, "X", d(fp, 0))
check("gap below stop: fill at open", r.ret, 0.80)

# 3. rises to +16% (stop moves to +5%), then falls -> exits at +5%
fp = FakePrices({"X": flat(2) + [(100, 116, 100, 115)] + [(110, 110, 104, 105)] + flat(600, 105)})
r = E.simulate_lot(fp, "X", d(fp, 0))
check("+15% reached -> stop +5%", r.ret, 1.05)

# 4. same day reaches +16% high and dips to -10%: stop checked BEFORE the new peak (conservative)
fp = FakePrices({"X": flat(2) + [(100, 116, 89, 95)] + flat(600, 95)})
r = E.simulate_lot(fp, "X", d(fp, 0))
check("same-day high and low: stop first", r.ret, 0.90)

# 5. peak +47% -> stop +30% (10-point steps above +40%)
fp = FakePrices({"X": flat(2) + [(100, 147, 100, 146)] + [(140, 140, 129, 130)] + flat(600, 130)})
r = E.simulate_lot(fp, "X", d(fp, 0))
check("peak +47% -> stop +30%", r.ret, 1.30)

# 6. five-point variant: peak +47% -> stop +35%
r = E.simulate_lot(fp, "X", d(fp, 0), E.Rules(five_point=True))
check("5-point variant: peak +47% -> stop +35%", r.ret, 1.35)

# 7. peak +27% -> stop +15%
fp = FakePrices({"X": flat(2) + [(100, 127, 100, 126)] + [(120, 120, 110, 112)] + flat(600, 112)})
r = E.simulate_lot(fp, "X", d(fp, 0))
check("peak +27% -> stop +15%", r.ret, 1.15)

# 8. 'funds selling' flag on day 30 -> sold at that day's open
path = flat(30) + [(103, 104, 102, 103)] + flat(600, 103)
fp = FakePrices({"X": path}, sell={"X": [30]})
r = E.simulate_lot(fp, "X", d(fp, 0))
check("funds selling: reason", r.reason, "funds_selling"); check("funds selling: price", r.ret, 1.03)

# 9. nothing happens -> sold at the open 24 months later
fp = FakePrices({"X": flat(700, 100)})
r = E.simulate_lot(fp, "X", d(fp, 0))
check("24-month cap: reason", r.reason, "time_cap")
want_cap = pd.bdate_range(d(fp, 0) + pd.DateOffset(months=24), periods=1)[0]  # next trading day on/after
check("24-month cap: date (first trading day on/after)", str(r.exit_date.date()), str(want_cap.date()))

# 10. stock stops trading after 50 days (no later prices) -> closed at last close
fp = FakePrices({"X": flat(10, 100) + flat(40, 97)})
r = E.simulate_lot(fp, "X", d(fp, 0))
check("delisted: reason", r.reason, "delisted"); check("delisted: last close", r.ret, 0.97)

# 11. charges on a Rs 5,000 buy and sale
check("buy charges on Rs 5,000", round(E.buy_cost(5000), 2), 5.93, 0.01)
# 5000 x (0.1% STT + 0.00297% NSE + 0.0001% SEBI) + 18% GST on NSE+SEBI + Rs 15.93 DP = 21.11
check("sell charges on Rs 5,000", round(E.sell_cost(5000), 2), 21.11, 0.01)

# 12. tax: short-term loss absorbs long-term gain; LTCG exemption
b = E.Book()
b.cash = 1e6
b.realize("2020-04-01", "2020-06-01", 100000, 80000 + E.sell_cost(80000), 0)    # ST loss -20,000
b.realize("2018-04-01", "2020-07-01", 100000, 300000 + E.sell_cost(300000), 0)  # LT gain +200,000
b.settle_taxes(pd.Timestamp("2021-03-31"))
want = (200000 - 20000 - 125000) * E.LTCG_RATE
check("tax: ST loss offsets LT gain, then exemption", round(b.taxes_paid, 2), round(want, 2), 1.0)

# 13. carry-forward short-term loss used next year
b = E.Book(); b.cash = 1e6
b.realize("2020-04-01", "2020-06-01", 100000, 70000 + E.sell_cost(70000), 0)    # ST loss -30,000 (FY21)
b.realize("2021-05-01", "2021-08-01", 100000, 150000 + E.sell_cost(150000), 0)  # ST gain +50,000 (FY22)
b.settle_taxes(pd.Timestamp("2022-03-31"))
check("tax: carried-forward loss", round(b.taxes_paid, 2), round(20000 * E.STCG_RATE, 2), 1.0)

# 14. XIRR: invest 100, get 110 one year later -> 10%
check("xirr 10%", round(E.xirr([(pd.Timestamp("2020-01-01"), -100), (pd.Timestamp("2021-01-01"), 110)]), 4), 0.0999, 0.0005)

print(f"\n{sum(results)}/{len(results)} passed")
