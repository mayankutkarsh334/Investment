"""Phase 3: monthly buy signals A-D, the 'funds start selling' flags, action dates and eligibility.

One row per (company, portfolio month M) for M = Dec-2013 .. Oct-2026.

Fund-house votes (from fund_actions.parquet, one vote per house):
  houses_new, houses_inc, houses_buy (= new + increase), houses_cut, houses_exit, houses_sell
  agg_rel  = total shares held by all pilot houses now / (held last month x flow)   [flow-adjusted]

Buy signals (each tested separately; rank 1 = the month's pick among eligible stocks that are NOT
flagged sell_default the same month)
  A  group buying     qualifies: houses_buy >= 2   (variant A3: >= 3)
                      rank: houses_buy, then houses_new, then Rs value bought
  B  biggest bets     qualifies: some diversified fund holds it >= 3 percentage points above the
                      average weight of all pilot active-equity funds
                      rank: that excess weight ('active_w')
  C  small new bets   qualifies: >= 1 house opened a new position at < 2% weight (the original idea:
                      positions funds start small); rank: number of such houses, then Rs value
  D  steady buying    qualifies: aggregate shares up >= 5% (flow-adjusted) for >= 3 consecutive months
                      (variant D2: >= 2); rank: streak length, then total rise over the streak

Selling flags (for the exit rule)
  sell_default : houses_sell >= 2  OR  agg_rel <= 0.80
  sell_3h      : houses_sell >= 3
  sell_10pct   : houses_sell >= 2  OR  agg_rel <= 0.90

Timing and eligibility
  action_date : first trading day on/after the 11th of month M+1 (SEBI: portfolios due by the 10th)
  ref_close   : last close before action_date (no look-ahead); adv20_cr: avg daily traded value of
                the 20 sessions before action_date (Rs crore)
  monthly_amt : the user's stepped-up monthly investment for the action date's year:
                Rs 2,000 in 2014 rising ~7.94% every January to Rs 5,000 in 2026 (2,000 x 2.5^((year-2014)/12))
  eligible    : trades on action_date, series EQ/BE (not BZ/SME), ref_close <= monthly_amt (one share must be
                affordable), adv20 >= Rs 1 crore
Output: data/processed/signals.parquet
"""
import re
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
P = ROOT / "data/processed"
START, END = "2013-12", "2026-10"
PILOT = ["hdfc", "sbi", "nippon", "absl", "dsp", "ppfas"]
NEW = ["icici", "axis", "uti"]
DATASETS = {  # name -> (fund houses, first signal month, output file)
    "PILOT": (PILOT, "2013-12", "signals.parquet"),
    "NEW": (NEW, "2014-05", "signals_NEW.parquet"),
    "ALL": (PILOT + NEW, "2013-12", "signals_ALL.parquet"),
}
BASE_AMT, BASE_YEAR, TARGET_AMT, TARGET_YEAR = 2000.0, 2014, 5000.0, 2026
STEP_UP = (TARGET_AMT / BASE_AMT) ** (1 / (TARGET_YEAR - BASE_YEAR)) - 1  # ~7.94% a year


def monthly_amount(year: int) -> float:
    """User's monthly investment in a calendar year (steps up every January), rounded to the rupee."""
    return float(round(BASE_AMT * (1 + STEP_UP) ** (year - BASE_YEAR)))
THEMATIC = re.compile(
    r"bank|financ|pharma|health|infra|power|tech|\bit\b|digital|consum|fmcg|psu|energy|resource|media|"
    r"mnc|housing|transport|logistic|defen|manufactur|business cycle|esg|innovat|quant|momentum|"
    r"conglomerate|automotive|reform|special situation|special opportunit|resurgent|t i g e r|tiger|natural|nri|"
    r"retirement|children|bal bhavishya|minimum variance|comma|global|commodit|millennium|gennext|generation next|india opportunities|buy india|new resources|micro cap", re.I)


def action_dates(trading_days: pd.DatetimeIndex, months: list) -> pd.Series:
    out = {}
    td = trading_days.sort_values()
    for m in months:
        nxt = (pd.Period(m, "M") + 1).to_timestamp()
        target = nxt + pd.Timedelta(days=10)  # the 11th
        i = td.searchsorted(target)
        out[m] = td[i] if i < len(td) else pd.NaT
    return pd.Series(out, name="action_date")


def main(dataset: str = "PILOT"):
    houses, start, out_file = DATASETS[dataset]
    fa = pd.read_parquet(P / "fund_actions.parquet")
    fa = fa[(fa["ym"] >= start) & (fa["ym"] <= END) & fa["amc"].isin(houses)]

    # ---- fund-house votes and aggregate change ----
    is_ = lambda a: fa["action"].isin(a)  # noqa: E731
    fa["v_new"] = is_(["new"]).astype(int)
    fa["v_inc"] = is_(["increase"]).astype(int)
    fa["v_cut"] = is_(["cut"]).astype(int)
    fa["v_exit"] = is_(["exit"]).astype(int)
    fa["v_new_small"] = (is_(["new"]) & (fa["max_pct"] < 2)).astype(int)
    fa["buy_val"] = np.where(is_(["new", "increase"]), fa["value_chg_cr"].clip(lower=0), 0.0)
    fa["qprev_flow"] = fa["qty_prev"] * fa["flow"]
    g = fa.groupby(["issuer", "ym"])
    sig = g.agg(houses_new=("v_new", "sum"), houses_inc=("v_inc", "sum"), houses_cut=("v_cut", "sum"),
                houses_exit=("v_exit", "sum"), houses_new_small=("v_new_small", "sum"),
                buy_value_cr=("buy_val", "sum"), qty_cur=("qty_cur", "sum"), qprev_flow=("qprev_flow", "sum"),
                houses_holding=("qty_cur", lambda s: int((s > 0).sum())),
                houses_held_prev=("qty_prev", lambda s: int((s > 0).sum()))).reset_index()
    sig["houses_buy"] = sig["houses_new"] + sig["houses_inc"]
    sig["houses_sell"] = sig["houses_cut"] + sig["houses_exit"]
    sig["agg_rel"] = np.where(sig["qprev_flow"] > 0, sig["qty_cur"] / sig["qprev_flow"], np.nan)

    # ---- D: consecutive months of aggregate buying ----
    sig = sig.sort_values(["issuer", "ym"])
    up = (sig["agg_rel"] >= 1.05) | ((sig["houses_held_prev"] == 0) & (sig["houses_holding"] > 0))
    sig["up"] = up
    # streak resets when a month is not 'up' or when the next row is not the next month
    per = pd.PeriodIndex(sig["ym"], freq="M")
    gap = (per - pd.PeriodIndex(sig.groupby("issuer")["ym"].shift(1).fillna("1900-01"), freq="M")).map(lambda x: x.n)
    brk = (~sig["up"]) | (gap != 1)
    grp = brk.groupby(sig["issuer"]).cumsum()
    sig["d_streak"] = sig["up"].astype(int).groupby([sig["issuer"], grp]).cumsum()
    lr = np.log(sig["agg_rel"].where(sig["up"] & (sig["agg_rel"] > 0), 1.0).clip(upper=10))
    sig["d_rise"] = np.exp(lr.groupby([sig["issuer"], grp]).cumsum()) - 1

    # ---- B: conviction (excess weight in a diversified fund over the pilot-wide average) ----
    hs = pd.read_parquet(P / "holdings_scheme.parquet", columns=["amc", "ym", "scheme_key", "issuer", "pct"])
    hs = hs[(hs["ym"] >= start) & (hs["ym"] <= END) & hs["amc"].isin(houses)]
    n_sch = hs.groupby("ym").apply(lambda d: d[["amc", "scheme_key"]].drop_duplicates().shape[0])
    avg_w = hs.groupby(["ym", "issuer"])["pct"].sum() / n_sch.reindex(hs.groupby(["ym", "issuer"]).size().index.get_level_values(0)).values
    hs = hs.merge(avg_w.rename("avg_w").reset_index(), on=["ym", "issuer"], how="left")
    hs["active_w"] = hs["pct"] - hs["avg_w"]
    div = hs[~hs["scheme_key"].str.contains(THEMATIC)]
    b = div.groupby(["issuer", "ym"]).agg(active_w=("active_w", "max"), max_div_pct=("pct", "max")).reset_index()
    sig = sig.merge(b, on=["issuer", "ym"], how="left")

    # ---- qualification ----
    sig["q_A"] = sig["houses_buy"] >= 2
    sig["q_A3"] = sig["houses_buy"] >= 3
    sig["q_B"] = sig["active_w"] >= 3
    sig["q_C"] = sig["houses_new_small"] >= 1
    sig["q_D"] = sig["d_streak"] >= 3
    sig["q_D2"] = sig["d_streak"] >= 2
    sig["sell_default"] = (sig["houses_sell"] >= 2) | (sig["agg_rel"] <= 0.80)
    sig["sell_3h"] = sig["houses_sell"] >= 3
    sig["sell_10pct"] = (sig["houses_sell"] >= 2) | (sig["agg_rel"] <= 0.90)

    # ---- action date and eligibility ----
    px = pd.read_parquet(P / "prices_adj.parquet", columns=["date", "issuer", "symbol", "series", "open", "close", "value"])
    px = px.sort_values(["issuer", "date"])
    ad = action_dates(pd.DatetimeIndex(px["date"].unique()), sorted(sig["ym"].unique()))
    sig["action_date"] = sig["ym"].map(ad)
    px["adv20_cr"] = px.groupby("issuer")["value"].transform(lambda v: v.rolling(20, min_periods=15).mean().shift(1)) / 1e7
    px["ref_close"] = px.groupby("issuer")["close"].shift(1)
    on_day = px.rename(columns={"date": "action_date"})[["issuer", "action_date", "symbol", "series", "open",
                                                         "ref_close", "adv20_cr"]]
    sig = sig.merge(on_day, on=["issuer", "action_date"], how="left")
    sig["monthly_amt"] = sig["action_date"].dt.year.map(lambda y: monthly_amount(int(y)) if pd.notna(y) else np.nan)
    sig["eligible"] = (sig["open"].notna() & sig["series"].isin(["EQ", "BE"]) & (sig["ref_close"] <= sig["monthly_amt"])
                       & (sig["adv20_cr"] >= 1.0))

    # ---- ranks among eligible qualifiers (1 = the month's pick) ----
    def rank(q, keys):
        # skip stocks other fund houses are selling the same month (user decision): take the next-ranked
        r = sig[sig[q] & sig["eligible"] & ~sig["sell_default"]].sort_values(["ym"] + keys, ascending=[True] + [False] * len(keys))
        return r.groupby("ym").cumcount() + 1
    sig["rank_A"] = rank("q_A", ["houses_buy", "houses_new", "buy_value_cr"])
    sig["rank_A3"] = rank("q_A3", ["houses_buy", "houses_new", "buy_value_cr"])
    sig["rank_B"] = rank("q_B", ["active_w"])
    sig["rank_C"] = rank("q_C", ["houses_new_small", "buy_value_cr"])
    sig["rank_D"] = rank("q_D", ["d_streak", "d_rise"])
    sig["rank_D2"] = rank("q_D2", ["d_streak", "d_rise"])

    sig = sig.drop(columns=["up", "qprev_flow"])
    sig.to_parquet(P / out_file, index=False)
    print(f"dataset {dataset}: houses {houses}, from {start} -> {out_file}")

    months = sig["ym"].nunique()
    print(f"signal rows: {len(sig):,} | months: {months} | eligible stock-months: {sig['eligible'].mean():.1%}")
    for s in ["A", "A3", "B", "C", "D", "D2"]:
        q = sig[sig[f"q_{s}"]]
        e = q[q["eligible"]]
        per_m = e.groupby("ym").size().reindex(sorted(sig["ym"].unique()), fill_value=0)
        print(f"  {s:3}: qualifying/month median {q.groupby('ym').size().median():5.0f} | eligible median "
              f"{per_m.median():4.0f} | months with no eligible pick: {(per_m == 0).sum()}")
    print(f"sell_default flagged: {sig['sell_default'].mean():.1%} of held stock-months")


if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else "PILOT")
