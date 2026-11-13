"""Phase 2: put fund share counts on a split/bonus-adjusted basis and attach NSE tickers.

A fund holding 100 shares before a 1:5 split holds 500 after it without buying anything.
Every month-end quantity is converted to *today's* share units:
    qty_adj = qty x (product of split/bonus/consolidation factors with ex-date after that month-end)
so month-to-month changes in qty_adj reflect real buying and selling only.

Adds to holdings_amc / holdings_scheme: qty_adj, symbol (latest NSE ticker), listed (traded on NSE
within 10 days of the month-end), close_me (raw close at month-end).
"""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
P = ROOT / "data/processed"


def month_end_factors(px: pd.DataFrame, months: pd.Series) -> pd.DataFrame:
    """For each issuer and month-end: share factor still to come, and the month-end close."""
    px = px.sort_values(["issuer", "date"]).copy()
    # product of share-count factors strictly AFTER each trading day
    px["cum_sh_after"] = px.groupby("issuer")["f_shares"].transform(lambda s: s[::-1].cumprod()[::-1].shift(-1).fillna(1.0))
    me = pd.DataFrame({"ym": sorted(months.unique())})
    me["me_date"] = pd.PeriodIndex(me["ym"], freq="M").to_timestamp(how="end").normalize()
    out = []
    for iss, g in px.groupby("issuer", sort=False):
        m = pd.merge_asof(me, g[["date", "cum_sh_after", "close", "f_shares"]], left_on="me_date", right_on="date",
                          direction="backward")
        m["issuer"] = iss
        # before the first trading day: all of the issuer's events still lie ahead
        m.loc[m["date"].isna(), "cum_sh_after"] = g["f_shares"].prod()
        out.append(m)
    f = pd.concat(out, ignore_index=True)
    f["listed"] = (f["me_date"] - f["date"]).dt.days.le(10)
    return f[["issuer", "ym", "cum_sh_after", "close", "listed"]].rename(columns={"close": "close_me"})


def main():
    px = pd.read_parquet(P / "prices_adj.parquet", columns=["date", "issuer", "symbol", "close", "f_shares", "value"])
    amc = pd.read_parquet(P / "holdings_amc.parquet")
    sch = pd.read_parquet(P / "holdings_scheme.parquet")
    f = month_end_factors(px[px["issuer"].isin(set(amc["issuer"]))], amc["ym"])
    sym = px.sort_values("date").drop_duplicates("issuer", keep="last").set_index("issuer")["symbol"]
    for name, df in (("holdings_amc", amc), ("holdings_scheme", sch)):
        df = df.drop(columns=[c for c in ("qty_adj", "symbol", "listed", "close_me", "cum_sh_after") if c in df.columns])
        df = df.merge(f, on=["issuer", "ym"], how="left")
        df["cum_sh_after"] = df["cum_sh_after"].fillna(1.0)
        df["qty_adj"] = df["qty"] * df["cum_sh_after"]
        df["symbol"] = df["issuer"].map(sym)
        df["listed"] = df["listed"].astype("boolean").fillna(False).astype(bool)
        df.to_parquet(P / f"{name}.parquet", index=False)
        if name == "holdings_amc":
            amc = df
    # check: around split/bonus events, does the fund-house quantity still jump?
    a = amc.sort_values(["amc", "issuer", "ym"]).copy()
    for c in ("qty", "qty_adj", "cum_sh_after"):
        a[f"prev_{c}"] = a.groupby(["amc", "issuer"])[c].shift(1)
    ev = a[(a["prev_cum_sh_after"] / a["cum_sh_after"]).round(4) != 1].dropna(subset=["prev_qty"])
    raw_jump = (np.log(ev["qty"] / ev["prev_qty"]).abs() > np.log(1.4)).mean()
    adj_jump = (np.log(ev["qty_adj"] / ev["prev_qty_adj"]).abs() > np.log(1.4)).mean()
    print(f"fund-house holdings spanning a split/bonus: {len(ev):,}")
    print(f"  share count changed >40% month-on-month: raw {raw_jump:.1%}  ->  adjusted {adj_jump:.1%}")
    print(f"holdings with an NSE ticker: {amc['symbol'].notna().mean():.1%}; "
          f"traded within 10 days of month-end: {amc['listed'].mean():.1%}")


if __name__ == "__main__":
    main()
