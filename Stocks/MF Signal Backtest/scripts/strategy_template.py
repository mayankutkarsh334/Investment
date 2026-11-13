"""TEMPLATE: test a new stock-picking idea on 2014-2026 NSE data with the same engine and the same
honest comparison used in Phases 5-6.

How to use (see PLAYBOOK.md):
  1. Copy this file to scripts/idea_<name>.py
  2. Write the idea down in PLAYBOOK form FIRST (rule, exits, pass/fail) - before running anything.
  3. Edit IDEA, RULES, OPTIONS and rank_stocks() below. rank_stocks() may only use data from BEFORE
     the action date (the engine buys at that day's open).
  4. Run:  .venv/bin/python -I scripts/idea_<name>.py [runs]     (default 1,000 random portfolios)
  5. Record the result in a results note; never edit the rule after seeing it and re-run as the "same" test.

What you get: average return per buy vs 1,000 random portfolios (same months, same liquidity band,
same exits), the G1-G4 gates, post-tax XIRR vs Nifty 500 / 6 flagship funds / small-cap SIPs.

The example below is a plain 12-month price-momentum rule (no mutual-fund data at all).
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import engine as E  # noqa: E402
import evaluate as V  # noqa: E402
import runner as R  # noqa: E402

# ------------------------------------------------------------------ 1. describe the idea
IDEA = "12-month momentum (example)"
RULES = E.Rules(
    use_stops=True,          # your -10% / +15%->+5% ... ladder; False = hold to the time cap
    five_point=False,        # 5-point steps above +30%
    atr_mult=None,           # e.g. 3.0 = initial stop at 3x ATR instead of -10%
    cap_months=24,           # sell after this many months
    sell_flag=None,          # None for non-fund ideas; "sell_default" = sell when funds start selling
)
OPTIONS = R.Options(
    rules=RULES,
    max_lots=3,              # up to 3 open buys of one stock
    park="NIFTY SMALLCAP 250",   # where idle money waits (None = cash at 0%)
)
SIGNALS_FILE = E.P / "signals.parquet"   # only used for the monthly action dates / funds-selling flags


# ------------------------------------------------------------------ 2. the ranking rule
def build_rankings(pr: E.Prices, uni: pd.DataFrame) -> dict:
    """Return {ym: [issuer, issuer, ...]} best first, using ONLY data before each action date.
    `uni` = every NSE stock you could buy that month (price <= monthly amount, >= Rs 1 cr/day traded,
    EQ/BE series) with columns ym, date (= action date), issuer, adv20_cr, liq_q."""
    px = pd.read_parquet(E.P / "prices_adj.parquet", columns=["date", "issuer", "tr_index"]).sort_values("date")
    out = {}
    for ym, g in uni.groupby("ym"):
        d = pd.Timestamp(g["date"].iloc[0])
        end = d - pd.Timedelta(days=1)                    # last close BEFORE the buy day
        start = d - pd.Timedelta(days=365)
        hist = px[(px["date"] <= end) & (px["date"] >= start - pd.Timedelta(days=10)) & px["issuer"].isin(g["issuer"])]
        last = hist.groupby("issuer")["tr_index"].last()
        first = hist[hist["date"] <= start + pd.Timedelta(days=10)].groupby("issuer")["tr_index"].first()
        mom = (last / first - 1).dropna()
        out[ym] = list(mom.sort_values(ascending=False).index)
    return out


# ------------------------------------------------------------------ 3. plumbing (no need to edit)
def make_chooser(rankings: dict, pr: E.Prices, max_lots: int):
    def choose(ym, d, budget, open_count):
        for iss in rankings.get(ym, []):
            if open_count[iss] >= max_lots:
                continue
            i = pr.idx(iss, d)
            if i is None:
                continue
            px = pr.a[iss]["open_raw"][i]
            if px + E.buy_cost(px) <= budget:
                return iss
        return None
    return choose


def main(runs: int = 1000):
    E.SIGNALS = SIGNALS_FILE
    pr = E.Prices()
    cache = R.LotCache(pr)
    uni = R.universe(pr)
    rankings = build_rankings(pr, uni)
    res = V.evaluate(IDEA, runs=runs, opt=OPTIONS, pr=pr, cache=cache, uni=uni,
                     picks_override=make_chooser(rankings, pr, OPTIONS.max_lots))
    print(f"\n=== {IDEA} ===")
    print(f"buys {res['buys']} | avg per buy {res['avg_per_buy']:.2%} (median {res['median_per_buy']:.2%}, "
          f"win {res['win_rate']:.0%}, median days {res['median_days']:.0f})")
    print(f"random portfolios: median {res['random_avg_median']:.2%}, 5th-95th {res['random_avg_p5_p95'][0]:.2%} .. "
          f"{res['random_avg_p5_p95'][1]:.2%} -> beats {res['random_percentile']:.1%} (t {res['t_stat_vs_random']:.2f})")
    print(f"halves 2014-19 {res['avg_2014_19']:.2%} (random {res['rand_2014_19']:.2%}) | 2020-26 {res['avg_2020_26']:.2%} "
          f"(random {res['rand_2020_26']:.2%}) | without top-10 buys {res['avg_without_top10']:.2%}")
    print(f"post-tax XIRR {res['xirr']:.2%} (random median {res['random_xirr_median']:.2%}) | final Rs {res['final_value']:,.0f} "
          f"on Rs {res['invested']:,.0f}")
    print("SIPs:", {k: f"{v:.2%}" for k, v in res["benchmarks"].items()})
    print("gates:", {k.split(' ')[0]: bool(v) for k, v in res["gates"].items()}, "-> PASSED" if res["passed"] else "-> not passed")
    return res


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1000)
