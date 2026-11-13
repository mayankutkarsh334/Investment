"""Phase 5: run every signal once against 1,000 random portfolios and the SIP benchmarks.

Usage: .venv/bin/python -I scripts/run_phase5.py [signals...]   (default: A B C D A3 D2)
Writes data/results/phase5_<signal>.pkl (full result incl. trades) and phase5_summary.csv.
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


def main():
    sigs = sys.argv[1:] or ["A", "B", "C", "D", "A3", "D2"]
    OUT.mkdir(parents=True, exist_ok=True)
    pr = E.Prices()
    cache = R.LotCache(pr)
    uni = R.universe(pr)
    rows = []
    for s in sigs:
        t = time.time()
        res = V.evaluate(s, runs=1000, pr=pr, cache=cache, uni=uni)
        pickle.dump(res, open(OUT / f"phase5_{s}.pkl", "wb"))
        g = res["gates"]
        rows.append({
            "signal": s, "buys": res["buys"], "avg_per_buy": res["avg_per_buy"], "median_per_buy": res["median_per_buy"],
            "win_rate": res["win_rate"], "median_days": res["median_days"],
            "random_avg_median": res["random_avg_median"], "random_p5": res["random_avg_p5_p95"][0],
            "random_p95": res["random_avg_p5_p95"][1], "percentile": res["random_percentile"], "t_stat": res["t_stat_vs_random"],
            "avg_2014_19": res["avg_2014_19"], "rand_2014_19": res["rand_2014_19"], "avg_2020_26": res["avg_2020_26"],
            "rand_2020_26": res["rand_2020_26"], "avg_wo_top10": res["avg_without_top10"],
            "xirr": res["xirr"], "random_xirr_median": res["random_xirr_median"], "final_value": res["final_value"],
            "invested": res["invested"], "taxes": res["taxes"], "charges": res["charges"],
            **{k.split(" ")[0]: v for k, v in g.items()}, "passed": res["passed"],
            **{f"bench_{k}": v for k, v in res["benchmarks"].items()},
        })
        print(f"{s}: done in {time.time() - t:.0f}s | avg/buy {res['avg_per_buy']:.2%} | pct {res['random_percentile']:.1%} "
              f"| t {res['t_stat_vs_random']:.2f} | XIRR {res['xirr']:.2%} | passed {res['passed']}", flush=True)
        pd.DataFrame(rows).to_csv(OUT / "phase5_summary.csv", index=False)


if __name__ == "__main__":
    main()
