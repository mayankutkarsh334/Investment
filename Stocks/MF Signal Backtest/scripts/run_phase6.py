"""Phase 6: the two pre-registered tests on the NEW (ICICI, Axis, UTI) and ALL (9 houses) datasets.

H1  signal B, original rules (stop ladder, funds-selling exit, 24-month cap)
H2  signal C, NO price stop (exit on funds-selling flag or 24 months)
Gates (phase6_plan.md): G1 avg per buy beats >= 97.5% of 1,000 random portfolios; G2 both halves;
G3 without top-10 buys; G4 post-tax XIRR beats all three SIPs; G5 still beats the random 95th
percentile after removing its most-bought stock.
Confirmed = all gates on BOTH datasets; rejected = fails G1 on NEW.
Usage: .venv/bin/python -I scripts/run_phase6.py
"""
import pickle
import sys
import time
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import engine as E  # noqa: E402

OUT = E.ROOT / "data/results"
TESTS = [("H1", "B", {}), ("H2", "C", {"rules": E.Rules(use_stops=False)})]


def main():
    import evaluate as V
    import runner as R
    rows = []
    for ds in ["NEW", "ALL"]:
        E.SIGNALS = E.P / f"signals_{ds}.parquet"
        R._NAV_CACHE.clear()
        pr = E.Prices(); cache = R.LotCache(pr); uni = R.universe(pr)
        for h, sig, kw in TESTS:
            t = time.time()
            opt = R.Options(**kw)
            res = V.evaluate(sig, runs=1000, opt=opt, pr=pr, cache=cache, uni=uni)
            tr = res["trades"]
            top = tr["issuer"].value_counts().index[0]
            wo_top = tr[tr["issuer"] != top]["ret_net"].mean()
            p95 = res["random_avg_p5_p95"][1]
            g = res["gates"]
            gates = {
                "G1 (>=97.5% random)": res["random_percentile"] >= 0.975,
                "G2 both halves": g["G2 above random median in both halves"],
                "G3 without top-10": g["G3 above random median without its 10 best buys"],
                "G4 XIRR beats 3 SIPs": g["G4 post-tax XIRR beats all three SIPs"],
                "G5 without most-bought stock": wo_top > p95,
            }
            row = {"dataset": ds, "test": h, "signal": sig, "buys": res["buys"], "avg_per_buy": res["avg_per_buy"],
                   "win_rate": res["win_rate"], "median_days": res["median_days"],
                   "random_median": res["random_avg_median"], "random_p95": p95,
                   "percentile": res["random_percentile"], "t_stat": res["t_stat_vs_random"],
                   "avg_2014_19": res["avg_2014_19"], "rand_2014_19": res["rand_2014_19"],
                   "avg_2020_26": res["avg_2020_26"], "rand_2020_26": res["rand_2020_26"],
                   "avg_wo_top10": res["avg_without_top10"], "most_bought": top,
                   "most_bought_buys": int((tr["issuer"] == top).sum()), "avg_wo_most_bought": wo_top,
                   "xirr": res["xirr"], "random_xirr_median": res["random_xirr_median"],
                   "final_value": res["final_value"], "invested": res["invested"],
                   **{f"bench_{k}": v for k, v in res["benchmarks"].items()}, **gates, "all_gates": all(gates.values())}
            rows.append(row)
            pickle.dump(res, open(OUT / f"phase6_{ds}_{h}.pkl", "wb"))
            pd.DataFrame(rows).to_csv(OUT / "phase6_summary.csv", index=False)
            print(f"{ds} {h}: {time.time()-t:.0f}s | avg/buy {res['avg_per_buy']:.2%} | pct {res['random_percentile']:.1%} | "
                  f"t {res['t_stat_vs_random']:.2f} | XIRR {res['xirr']:.3%} | gates {sum(gates.values())}/5", flush=True)


if __name__ == "__main__":
    main()
