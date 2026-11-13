"""Phase 5 step 3: exit-rule variants for the signal that passed the stock-picking gates (B), plus
two diagnostics. Each variant is compared with 1,000 random portfolios run under the SAME rules.
Usage: .venv/bin/python -I scripts/run_variants.py
Writes data/results/variants_summary.csv and variant_<name>.pkl
"""
import pickle
import sys
import time
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import engine as E  # noqa: E402
import evaluate as V  # noqa: E402
import runner as R  # noqa: E402

OUT = E.ROOT / "data/results"
VARIANTS = [
    ("B_5point", "B", R.Options(rules=E.Rules(five_point=True))),
    ("B_atr2", "B", R.Options(rules=E.Rules(atr_mult=2.0))),
    ("B_atr3", "B", R.Options(rules=E.Rules(atr_mult=3.0))),
    ("B_cap3m", "B", R.Options(rules=E.Rules(cap_months=3))),
    ("B_cap6m", "B", R.Options(rules=E.Rules(cap_months=6))),
    ("B_cap12m", "B", R.Options(rules=E.Rules(cap_months=12))),
    ("B_no_sellflag", "B", R.Options(rules=E.Rules(sell_flag=None))),
    ("B_sell3h", "B", R.Options(rules=E.Rules(sell_flag="sell_3h"))),
    ("B_sell10pct", "B", R.Options(rules=E.Rules(sell_flag="sell_10pct"))),
    ("B_one_buy_per_stock", "B", R.Options(max_lots=1)),
    ("B_no_stops", "B", R.Options(rules=E.Rules(use_stops=False))),
    # diagnostics: do the stops hide an edge in the other signals?
    ("A_no_stops", "A", R.Options(rules=E.Rules(use_stops=False))),
    ("C_no_stops", "C", R.Options(rules=E.Rules(use_stops=False))),
    ("D_no_stops", "D", R.Options(rules=E.Rules(use_stops=False))),
]


def main():
    pr = E.Prices(); cache = R.LotCache(pr); uni = R.universe(pr)
    rows = []
    for name, sig, opt in VARIANTS:
        t = time.time()
        res = V.evaluate(sig, runs=1000, opt=opt, pr=pr, cache=cache, uni=uni)
        pickle.dump(res, open(OUT / f"variant_{name}.pkl", "wb"))
        rows.append({"variant": name, "buys": res["buys"], "avg_per_buy": res["avg_per_buy"], "win_rate": res["win_rate"],
                     "median_days": res["median_days"], "random_avg_median": res["random_avg_median"],
                     "random_p95": res["random_avg_p5_p95"][1], "percentile": res["random_percentile"],
                     "t_stat": res["t_stat_vs_random"], "avg_2014_19": res["avg_2014_19"], "avg_2020_26": res["avg_2020_26"],
                     "avg_wo_top10": res["avg_without_top10"], "xirr": res["xirr"], "random_xirr_median": res["random_xirr_median"],
                     "final_value": res["final_value"], **{k.split(" ")[0]: v for k, v in res["gates"].items()},
                     "passed": res["passed"]})
        print(f"{name}: {time.time()-t:.0f}s | avg/buy {res['avg_per_buy']:.2%} | pct {res['random_percentile']:.1%} | "
              f"XIRR {res['xirr']:.3%} | passed {res['passed']}", flush=True)
        pd.DataFrame(rows).to_csv(OUT / "variants_summary.csv", index=False)


if __name__ == "__main__":
    main()
