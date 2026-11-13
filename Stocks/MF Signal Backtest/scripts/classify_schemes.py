"""Phase 1: decide which schemes are *actively managed Indian equity* funds.

A scheme qualifies when, across the months it appears, it usually (>= 60% of months)
  - has no passive / debt / hybrid / close-ended / foreign / FoF / arbitrage word in its name,
  - holds >= 60% of NAV in Indian equity shares (PPFAS holds up to 35% foreign shares), and
  - holds <= 10% of NAV in other Indian ISIN instruments (bonds, T-bills, CPs) -> rules out hybrids.
Deciding once per scheme (not month by month) stops a fund flickering in and out of the
set, which would otherwise look like the fund house buying or selling everything it holds.

Input : data/interim/sheets_raw.parquet
Output: data/interim/schemes.csv (one row per amc + scheme_key, with the decision and reasons)
"""
import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
INTERIM = ROOT / "data" / "interim"

EXCLUDE = re.compile(
    r"index|\betf\b|exchange traded|\bbees\b|r\s?\*?\s?shares|\bcnx\b|nifty|sensex|\bbse\b|\bnse\b|cpse|bharat 22|"
    r"fund of funds?|\bfof\b|feeder|arbitrage|liquid|debt|bond|gilt|income|money market|overnight|treasury|"
    r"\bcash\b|(?<!tax )savings fund$|\bfmp\b|fixed (maturity|term|horizon)|interval|capital protection|dual advantage|"
    r"monthly income|\bmip\b|balanced|hybrid|dynamic asset|asset allocation|multi[- ]?asset|gold|silver|"
    r"international|overseas|world|\bus\b|u\.s\.|nasdaq|emerging market|asia|europe|japan|china|global innovation|"
    r"series|\bsr\b|\b\d{3,4}\s?d(ays)?\b|close[ -]?ended|segregat|rajiv gandhi|rgess|"
    r"conservative|equity savings|prudence|commodit|real estate|reit|invit",
    re.I)
AMC_PREFIX = re.compile(
    r"^(hdfc|sbi|nippon india|reliance|aditya birla sun life|birla sun life|absl|dsp blackrock|dsp|ppfas|"
    r"parag parikh|icici prudential|axis|uti\s*-?)\s+", re.I)


def scheme_key(name: str) -> str:
    s = str(name).lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"\berstwhile.*$|\bformerly.*$", " ", s)
    s = AMC_PREFIX.sub("", s.strip())
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    sh = pd.read_parquet(INTERIM / "sheets_raw.parquet")
    sh = sh[sh["scheme_raw"].astype(str).str.len() > 3].copy()
    sh["scheme_key"] = sh["scheme_raw"].map(scheme_key)
    sh["other_isin_pct"] = (sh["all_pct"] - sh["eq_pct"]).clip(lower=0)
    min_eq = sh["amc"].map(lambda a: 60.0 if a == "ppfas" else 75.0)
    sh["name_ok"] = ~sh["scheme_raw"].astype(str).map(lambda s: bool(EXCLUDE.search(s)))
    sh["eq_ok"] = sh["eq_pct"] >= min_eq
    sh["other_ok"] = sh["other_isin_pct"] <= 10
    sh["pass"] = sh["name_ok"] & sh["eq_ok"] & sh["other_ok"]

    g = sh.groupby(["amc", "scheme_key"])
    out = g.agg(
        scheme_example=("scheme_raw", "last"),
        months=("ym", "nunique"),
        first_ym=("ym", "min"),
        last_ym=("ym", "max"),
        pass_share=("pass", "mean"),
        name_ok=("name_ok", "mean"),
        eq_pct_med=("eq_pct", "median"),
        other_pct_med=("other_isin_pct", "median"),
        n_eq_med=("n_eq", "median"),
    ).reset_index()
    out["active_equity"] = (out["pass_share"] >= 0.60) & (out["name_ok"] >= 0.99)
    out["reason"] = ""
    out.loc[out["name_ok"] < 0.99, "reason"] = "name: passive/debt/hybrid/close-ended/foreign"
    out.loc[(out["reason"] == "") & (out["eq_pct_med"] < 60), "reason"] = "Indian equity < 60%"
    out.loc[(out["reason"] == "") & (out["other_pct_med"] > 10), "reason"] = "holds bonds/T-bills > 10% (hybrid)"
    out.loc[(out["reason"] == "") & ~out["active_equity"], "reason"] = "passes in < 60% of months"
    out = out.sort_values(["amc", "active_equity", "scheme_key"], ascending=[True, False, True])
    out.to_csv(INTERIM / "schemes.csv", index=False)
    kept = out[out["active_equity"]]
    print(f"schemes: {len(out)} total, {len(kept)} active equity")
    print(kept.groupby("amc").size().to_string())


if __name__ == "__main__":
    main()
