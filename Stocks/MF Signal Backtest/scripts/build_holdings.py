"""Phase 1: build the clean holdings tables and the validation report.

Steps
  1. Keep only schemes classified as actively managed Indian equity (schemes.csv).
  2. When the same scheme-month appears in more than one file (re-uploads, HDFC's
     consolidated + per-scheme files), keep the copy with the most complete equity book.
  3. Merge duplicate lines of the same ISIN within a scheme (e.g. locked-in + free shares).
  4. Add `issuer` = first 7 characters of the ISIN (e.g. INE090A for ICICI Bank). It stays the
     same when a split or face-value change creates a new ISIN, so a split never looks like a sale.
  5. Roll up to fund-house level: total shares and value each fund house holds in each company.

Outputs (data/processed/):
  holdings_scheme.parquet  amc, ym, scheme_key, scheme_raw, isin, issuer, name, industry, qty, mv_lakhs, pct
  holdings_amc.parquet     amc, ym, issuer, isin, name, qty, mv_lakhs, n_schemes, max_pct
  checks.csv               per amc-month: schemes, stocks, equity value, month-on-month changes, flags
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
INTERIM = ROOT / "data" / "interim"
OUT = ROOT / "data" / "processed"

import sys  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parent))
from classify_schemes import scheme_key  # noqa: E402


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    h = pd.read_parquet(INTERIM / "holdings_raw.parquet")
    sh = pd.read_parquet(INTERIM / "sheets_raw.parquet")
    schemes = pd.read_csv(INTERIM / "schemes.csv")
    active = set(map(tuple, schemes.loc[schemes["active_equity"], ["amc", "scheme_key"]].values))

    # 0. trust the 'Portfolio as on ...' date printed in the sheet over the link's month
    #    (e.g. DSP's 'jan2016' zip actually holds the January 2017 portfolio)
    sh["ym_file"] = sh["ym"]
    ok = sh["asof"].notna() & sh["asof"].between("2012-01", "2026-12")
    sh.loc[ok, "ym"] = sh.loc[ok, "asof"]
    moved = sh[(sh["ym"] != sh["ym_file"]) & (sh["n_eq"] >= 10)]
    moved.groupby(["amc", "ym_file", "ym"]).size().rename("sheets").reset_index().to_csv(
        OUT / "relabelled_months.csv", index=False)
    print(f"sheets relabelled to their printed month: {len(moved)} "
          f"({moved.groupby('amc').size().to_dict()})")
    keymap = sh[["file", "book", "sheet", "ym"]].drop_duplicates(["file", "book", "sheet"])
    h = h.drop(columns="ym").merge(keymap, on=["file", "book", "sheet"], how="inner")

    for df in (h, sh):
        df["scheme_key"] = df["scheme_raw"].map(scheme_key)
    sh = sh[[(a, k) in active for a, k in zip(sh["amc"], sh["scheme_key"])]]

    # 2. one source per (amc, ym, scheme): most equity rows, then highest equity %
    sh = sh.sort_values(["n_eq", "eq_pct"], ascending=False)
    best = sh.drop_duplicates(["amc", "ym", "scheme_key"])[["amc", "ym", "scheme_key", "file", "book", "sheet"]]
    h = h.merge(best, on=["amc", "ym", "scheme_key", "file", "book", "sheet"], how="inner")

    # 3. merge duplicate ISIN lines inside a scheme
    h = (h.groupby(["amc", "ym", "scheme_key", "isin"], as_index=False)
           .agg(scheme_raw=("scheme_raw", "first"), name=("name", "first"), industry=("industry", "first"),
                qty=("qty", "sum"), mv_lakhs=("mv_lakhs", "sum"), pct=("pct", "sum")))
    h["issuer"] = h["isin"].str[:7]
    h = h.sort_values(["amc", "ym", "scheme_key", "pct"], ascending=[True, True, True, False])
    h.to_parquet(OUT / "holdings_scheme.parquet", index=False)

    # 5. fund-house level
    amc = (h.groupby(["amc", "ym", "issuer"], as_index=False)
             .agg(isin=("isin", "last"), name=("name", "first"), qty=("qty", "sum"), mv_lakhs=("mv_lakhs", "sum"),
                  n_schemes=("scheme_key", "nunique"), max_pct=("pct", "max")))
    amc.to_parquet(OUT / "holdings_amc.parquet", index=False)

    # checks
    c = (h.groupby(["amc", "ym"]).agg(schemes=("scheme_key", "nunique"), stocks=("issuer", "nunique"),
                                       eq_value_cr=("mv_lakhs", lambda s: s.sum() / 100))
           .reset_index().sort_values(["amc", "ym"]))
    for col in ("schemes", "stocks", "eq_value_cr"):
        c[f"{col}_chg"] = c.groupby("amc")[col].pct_change()
    c["flag"] = ""
    c.loc[c["schemes_chg"].abs() > 0.3, "flag"] += "schemes jump; "
    c.loc[c["stocks_chg"].abs() > 0.3, "flag"] += "stocks jump; "
    c.loc[c["eq_value_cr_chg"].abs() > 0.3, "flag"] += "value jump; "
    allm = pd.period_range("2013-09", "2026-10", freq="M").astype(str)
    missing = []
    for a, g in c.groupby("amc"):
        start = g["ym"].min()
        missing += [{"amc": a, "ym": m, "flag": "MISSING MONTH"} for m in allm if m >= start and m not in set(g["ym"])]
    c = pd.concat([c, pd.DataFrame(missing)], ignore_index=True).sort_values(["amc", "ym"])
    c.to_csv(OUT / "checks.csv", index=False)

    print(f"scheme-level rows: {len(h):,}  fund-house rows: {len(amc):,}")
    print(c.groupby("amc").agg(months=("schemes", "count"), first=("ym", "min"), last=("ym", "max"),
                               schemes_med=("schemes", "median"), stocks_med=("stocks", "median"),
                               flags=("flag", lambda s: (s.str.len() > 0).sum())).to_string())


if __name__ == "__main__":
    main()
