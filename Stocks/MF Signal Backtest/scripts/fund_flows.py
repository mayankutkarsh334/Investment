"""Phase 3 step 1: what did each fund house actually buy or sell each month?

For every fund house (amc), company (issuer) and month M, compared with that house's previous
*available* month P (usually M-1; across a missing month it is M-2):

  qty_prev  = split-adjusted shares held at P (all active-equity schemes)
  qty_cur   = split-adjusted shares held at M, EXCLUDING schemes launched in M
              (a new fund's first portfolio is bought with fresh money, not a conviction change;
               a renamed fund is not a launch - its holdings carry over and are kept)
  flow      = the house's typical growth in shares across stocks it held in both months
              (median of qty_cur/qty_prev): inflows make funds buy a bit more of everything
  rel       = (qty_cur/qty_prev) / flow  -> buying or selling beyond what flows explain

Actions (one vote per fund house):
  new       held at M, not at P                          (and worth >= Rs 1 crore)
  increase  rel >= 1.10 and value added >= Rs 50 lakh
  cut       rel <= 0.90 and value removed >= Rs 50 lakh
  exit      held at P, not at M
  hold      otherwise
Output: data/processed/fund_actions.parquet
"""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
P = ROOT / "data/processed"
INC, CUT = 1.10, 0.90
# months whose published files are incomplete (big schemes missing) -> treated as not published
DROP_MONTHS = {("uti", "2023-10")}   # UTI's format switch: Flexi Cap & MNC files absent that month
MIN_NEW_CR, MIN_CHG_CR = 1.0, 0.5


def find_launches(s: pd.DataFrame) -> set:
    """(amc, scheme_key, ym) for schemes whose first month is a genuine launch, not a rename."""
    present = s.groupby(["amc", "ym"])["scheme_key"].agg(set).to_dict()
    amc_months = {a: sorted(g["ym"].unique()) for a, g in s.groupby("amc")}
    span = s.groupby(["amc", "scheme_key"])["ym"].agg(["min", "max"]).reset_index()
    launches = set()
    for _, r in span.iterrows():
        a, k, m0 = r["amc"], r["scheme_key"], r["min"]
        ms = amc_months[a]
        i = ms.index(m0)
        if i == 0:  # the house's first month: nothing to compare with
            continue
        p = ms[i - 1]
        new = s[(s["amc"] == a) & (s["scheme_key"] == k) & (s["ym"] == m0)].groupby("issuer")["qty_adj"].sum()
        # any scheme present last month but missing this month could be the same fund under a new name
        gone = present[(a, p)] - present[(a, m0)]
        best = 0.0
        for g in gone:
            old = s[(s["amc"] == a) & (s["scheme_key"] == g) & (s["ym"] == p)].groupby("issuer")["qty_adj"].sum()
            j = new.index.intersection(old.index)
            if len(new) and new.sum() > 0:
                best = max(best, float(np.minimum(new[j], old[j]).sum() / new.sum()))
        if best < 0.5:
            launches.add((a, k, m0))
    return launches


def main():
    s = pd.read_parquet(P / "holdings_scheme.parquet")
    s = s[s["ym"] >= "2013-08"]
    s = s[[(a, m) not in DROP_MONTHS for a, m in zip(s["amc"], s["ym"])]]
    launches = find_launches(s)
    s["launch"] = [(a, k, m) in launches for a, k, m in zip(s["amc"], s["scheme_key"], s["ym"])]
    print(f"scheme launches excluded in their first month: {len(launches)}")

    px = s[["issuer", "ym", "close_me"]].dropna().drop_duplicates(["issuer", "ym"])
    tot_all = {k: g.set_index("issuer")["qty_adj"] for k, g in
               s.groupby(["amc", "issuer", "ym"], as_index=False)["qty_adj"].sum().groupby(["amc", "ym"])}
    tot_ex = {k: g.set_index("issuer")["qty_adj"] for k, g in
              s[~s["launch"]].groupby(["amc", "issuer", "ym"], as_index=False)["qty_adj"].sum().groupby(["amc", "ym"])}
    maxpct_ex = s[~s["launch"]].groupby(["amc", "issuer", "ym"])["pct"].max()

    rows = []
    for a in sorted(s["amc"].unique()):
        months = sorted(s.loc[s["amc"] == a, "ym"].unique())
        for i in range(1, len(months)):
            m, p = months[i], months[i - 1]
            prev = tot_all[(a, p)]
            cur = tot_ex.get((a, m), pd.Series(dtype=float))
            df = pd.DataFrame({"qty_prev": prev, "qty_cur": cur}).fillna(0.0)
            df.index.name = "issuer"
            both = df[(df["qty_prev"] > 0) & (df["qty_cur"] > 0)]
            flow = float(np.median(both["qty_cur"] / both["qty_prev"])) if len(both) >= 10 else 1.0
            df["amc"], df["ym"], df["prev_ym"], df["flow"] = a, m, p, flow
            rows.append(df.reset_index())
    f = pd.concat(rows, ignore_index=True)
    f = f.merge(px, on=["issuer", "ym"], how="left")
    pp = px.rename(columns={"ym": "prev_ym", "close_me": "close_prev"})
    f = f.merge(pp, on=["issuer", "prev_ym"], how="left")
    price = f["close_me"].fillna(f["close_prev"])
    f["rel"] = np.where(f["qty_prev"] > 0, (f["qty_cur"] / f["qty_prev"]) / f["flow"], np.nan)
    f["value_chg_cr"] = (f["qty_cur"] - f["qty_prev"] * f["flow"]) * price / 1e7
    f["value_cur_cr"] = f["qty_cur"] * price / 1e7
    f["action"] = "hold"
    f.loc[(f["qty_prev"] == 0) & (f["qty_cur"] > 0) & (f["value_cur_cr"].fillna(0) >= MIN_NEW_CR), "action"] = "new"
    f.loc[(f["qty_prev"] == 0) & (f["qty_cur"] > 0) & (f["action"] == "hold"), "action"] = "new_tiny"
    f.loc[(f["qty_prev"] > 0) & (f["qty_cur"] == 0), "action"] = "exit"
    f.loc[(f["action"] == "hold") & (f["rel"] >= INC) & (f["value_chg_cr"] >= MIN_CHG_CR), "action"] = "increase"
    f.loc[(f["action"] == "hold") & (f["rel"] <= CUT) & (f["value_chg_cr"] <= -MIN_CHG_CR), "action"] = "cut"
    mp = maxpct_ex.rename("max_pct").reset_index()
    f = f.merge(mp, on=["amc", "issuer", "ym"], how="left")
    f.to_parquet(P / "fund_actions.parquet", index=False)
    print(f"rows: {len(f):,}")
    print(f[f["ym"] >= "2013-12"].groupby("amc")["action"].value_counts().unstack(fill_value=0).to_string())
    print("\nmedian monthly flow factor per house:", f.groupby("amc")["flow"].median().round(3).to_dict())


if __name__ == "__main__":
    main()
