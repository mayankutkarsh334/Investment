"""Phase 4: evaluate one signal against 1,000 random portfolios and the SIP benchmarks.

Pass/fail rule (fixed before any signal result was seen; user-confirmed metric = average return per buy):
  G1  the signal's average post-cost return per buy beats >= 95% of 1,000 random portfolios
      (random stock each month from the same liquidity quintile, same months, same rules);
      reported with a t-stat of (signal buy - random average that month), clustered by stock
  G2  above the random median in BOTH halves (buys in 2014-2019 and in 2020-2026)
  G3  still above the random median after removing its 10 best buys
  G4  post-tax XIRR (idle money in the small-cap fund) beats SIPs into the Nifty 500, the 6 flagship
      funds AND the small-cap fund itself (else the result is just 'small caps did well')
Usage: evaluate(signal="A", runs=1000, opt=Options())  -> dict; nothing is run on import.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import engine as E  # noqa: E402
import runner as R  # noqa: E402


def buy_returns(trades: list) -> pd.DataFrame:
    t = pd.DataFrame(trades)
    if t.empty:
        return t
    t["ret_net"] = (t["gross"] - t["gross"].map(E.sell_cost) + t["dividends"]) / t["cost"] - 1
    t["ym_entry"] = pd.to_datetime(t["entry"]).dt.strftime("%Y-%m")
    return t


def clustered_t(diff: pd.Series, groups: pd.Series) -> float:
    """t-stat of the mean of `diff`, with standard errors clustered by stock."""
    x = diff.values - diff.mean()
    g = pd.Series(x).groupby(groups.values).sum()
    n, k = len(diff), g.size
    if k < 2:
        return float("nan")
    var = (g ** 2).sum() / n ** 2 * k / (k - 1)
    return float(diff.mean() / np.sqrt(var)) if var > 0 else float("nan")


def evaluate(signal: str, runs: int = 1000, opt: R.Options = R.Options(), seed: int = 2026,
             pr: E.Prices = None, cache: R.LotCache = None, uni: pd.DataFrame = None, picks_override=None):
    pr = pr or E.Prices()
    cache = cache or R.LotCache(pr)
    uni = uni if uni is not None else R.universe(pr)
    choose = picks_override or R.strategy_chooser(signal, pr, opt.max_lots)
    strat = R.run_portfolio(choose, pr, cache, R.Options(**{**opt.__dict__, "track_value": True}), label=signal)
    st = buy_returns(strat["trades"])
    picks = dict(zip(st["ym_entry"].map(_ym_of_action), st["issuer"]))   # signal month -> stock
    rng = np.random.default_rng(seed)
    rand_avg, rand_xirr, rand_by_month = [], [], []
    for _ in range(runs):
        r = R.run_portfolio(R.random_chooser(picks, uni, rng, pr, opt.max_lots), pr, cache, opt)
        rt = buy_returns(r["trades"])
        rand_avg.append(rt["ret_net"].mean() if len(rt) else np.nan)
        rand_xirr.append(r["xirr"])
        rand_by_month.append(rt.groupby("ym_entry")["ret_net"].mean())
    rand_avg, rand_xirr = np.array(rand_avg), np.array(rand_xirr)
    month_mean = pd.concat(rand_by_month, axis=1).mean(axis=1)

    avg = st["ret_net"].mean()
    pct = float((rand_avg < avg).mean())
    diff = st["ret_net"] - st["ym_entry"].map(month_mean)
    t = clustered_t(diff.dropna(), st.loc[diff.notna(), "issuer"])
    early = st[st["ym_entry"] < "2020-01"]["ret_net"].mean()
    late = st[st["ym_entry"] >= "2020-01"]["ret_net"].mean()
    rand_med = float(np.nanmedian(rand_avg))
    # random medians per half (same months) for a like-for-like comparison
    half = lambda lo, hi: float(np.nanmedian([m[(m.index >= lo) & (m.index < hi)].mean() for m in rand_by_month]))  # noqa: E731
    rm_early, rm_late = half("0000", "2020-01"), half("2020-01", "9999")
    top10_removed = st["ret_net"].sort_values().iloc[:-10].mean() if len(st) > 10 else np.nan

    idx, funds = R.benchmark_series()
    bench = {
        "Nifty 500 SIP": R.sip_benchmark({"NIFTY 500": idx["NIFTY 500"]}, "n500")["xirr"],
        "6 flagship funds SIP": R.sip_benchmark(funds, "funds")["xirr"],
        "Small-cap fund SIP": R.sip_benchmark({"NIFTY SMALLCAP 250": idx["NIFTY SMALLCAP 250"]}, "sc")["xirr"],
    }
    gates = {
        "G1 beats >=95% of random portfolios (avg per buy)": pct >= 0.95,
        "G2 above random median in both halves": (early > rm_early) and (late > rm_late),
        "G3 above random median without its 10 best buys": top10_removed > rand_med,
        "G4 post-tax XIRR beats all three SIPs": all(strat["xirr"] > v for v in bench.values()),
    }
    return {
        "signal": signal, "buys": len(st), "avg_per_buy": avg, "median_per_buy": st["ret_net"].median(),
        "win_rate": (st["ret_net"] > 0).mean(), "median_days": (pd.to_datetime(st["exit"]) - pd.to_datetime(st["entry"])).dt.days.median(),
        "exit_reasons": st["reason"].value_counts(normalize=True).round(3).to_dict(),
        "random_percentile": pct, "random_avg_median": rand_med,
        "random_avg_p5_p95": (float(np.nanpercentile(rand_avg, 5)), float(np.nanpercentile(rand_avg, 95))),
        "t_stat_vs_random": t, "avg_2014_19": early, "rand_2014_19": rm_early, "avg_2020_26": late, "rand_2020_26": rm_late,
        "avg_without_top10": top10_removed,
        "xirr": strat["xirr"], "random_xirr_median": float(np.nanmedian(rand_xirr)),
        "random_xirr_p5_p95": (float(np.nanpercentile(rand_xirr, 5)), float(np.nanpercentile(rand_xirr, 95))),
        "final_value": strat["final_value"], "invested": strat["invested"], "taxes": strat["taxes"],
        "charges": strat["charges"], "benchmarks": bench, "gates": gates, "passed": all(gates.values()),
        "trades": st, "values": strat.get("values"),
    }


_AD = None


def _ym_of_action(entry_ym: str) -> str:
    """Map an entry month (action date's month) back to the portfolio month that triggered it."""
    return (pd.Period(entry_ym, "M") - 1).strftime("%Y-%m")
