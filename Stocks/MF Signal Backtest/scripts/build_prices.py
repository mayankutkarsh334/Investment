"""Phase 2: build the daily price table and split/bonus/demerger-adjusted prices.

Part 1 (raw): read every NSE bhavcopy (old format and UDiFF), keep Indian equity shares
  (ISIN INE.......01.., series EQ/BE/BZ/BT/SM/ST) -> data/processed/prices_raw.parquet
Part 2 (adjusted): per company (issuer = ISIN[:7], stable across splits and renames)
  - factor on each ex-date: splits, bonuses, consolidations from corp_actions.parquet;
    demergers measured from the price drop (prev close / ex-day open) when the drop is >= 3%;
  - adjusted price = raw price / product of factors with ex-date AFTER that day
    (so today's prices are unchanged and older prices are scaled down);
  - dividends per adjusted share, and a total-return index (dividends reinvested).
  -> data/processed/prices_adj.parquet
Run: .venv/bin/python -I scripts/build_prices.py [--raw-only]
"""
import io
import sys
import zipfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
BHAV = ROOT / "data/raw/nse/bhav"
OUT = ROOT / "data/processed"
SERIES = {"EQ", "BE", "BZ", "BT", "SM", "ST"}
OLD = {"SYMBOL": "symbol", "SERIES": "series", "ISIN": "isin", "OPEN": "open", "HIGH": "high", "LOW": "low",
       "CLOSE": "close", "PREVCLOSE": "prevclose", "TOTTRDQTY": "volume", "TOTTRDVAL": "value"}
NEW = {"TckrSymb": "symbol", "SctySrs": "series", "ISIN": "isin", "OpnPric": "open", "HghPric": "high",
       "LwPric": "low", "ClsPric": "close", "PrvsClsgPric": "prevclose", "TtlTradgVol": "volume", "TtlTrfVal": "value"}


def read_one(path: Path):
    d = pd.Timestamp(path.name[:10])
    with zipfile.ZipFile(path) as z:
        raw = z.read(z.namelist()[0])
    df = pd.read_csv(io.BytesIO(raw), dtype=str)
    df.columns = [c.strip() for c in df.columns]
    m = NEW if "TckrSymb" in df.columns else OLD
    df = df[[c for c in m if c in df.columns]].rename(columns=m)
    for c in ("symbol", "series", "isin"):
        df[c] = df[c].astype(str).str.strip()
    df = df[df["series"].isin(SERIES) & df["isin"].str.match(r"^INE[A-Z0-9]{4}01[A-Z0-9]{3}$")]
    for c in ("open", "high", "low", "close", "prevclose", "volume", "value"):
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["date"] = d
    return df


def build_raw():
    files = sorted(BHAV.rglob("*.csv.zip"))
    with ProcessPoolExecutor(max_workers=7) as ex:
        parts = list(ex.map(read_one, files, chunksize=20))
    px = pd.concat(parts, ignore_index=True)
    px["issuer"] = px["isin"].str[:7]
    # one row per issuer per day (if two lines exist, keep the more traded one)
    px = px.sort_values("value", ascending=False).drop_duplicates(["date", "issuer"]).sort_values(["issuer", "date"])
    px.to_parquet(OUT / "prices_raw.parquet", index=False)
    print(f"raw prices: {len(px):,} rows, {px['issuer'].nunique():,} companies, {px['date'].nunique():,} days")
    return px


def build_adjusted(px: pd.DataFrame):
    ca = pd.read_parquet(OUT / "corp_actions.parquet")
    # map corporate actions to issuers: by ISIN when present, else by symbol trading on/near that date
    ca["issuer"] = ca["isin"].where(ca["isin"].astype(str).str.match(r"^INE"), None).str[:7]
    sym_map = px.drop_duplicates(["symbol", "issuer"], keep="last")[["symbol", "issuer"]]
    sym_map = sym_map.drop_duplicates("symbol", keep="last").set_index("symbol")["issuer"]
    ca["issuer"] = ca["issuer"].fillna(ca["symbol"].map(sym_map))
    ca = ca.dropna(subset=["issuer"])
    ca["ex_date"] = pd.to_datetime(ca["ex_date"]).astype("datetime64[ns]")
    px["date"] = pd.to_datetime(px["date"]).astype("datetime64[ns]")

    px = px.sort_values(["issuer", "date"]).reset_index(drop=True)
    px["prev_close_series"] = px.groupby("issuer")["close"].shift(1)
    # snap each action to the first trading day on/after its ex-date for that issuer
    days = px[["issuer", "date"]]
    snapped = pd.merge_asof(ca.sort_values("ex_date"), days.sort_values("date").rename(columns={"date": "td"}),
                            left_on="ex_date", right_on="td", by="issuer", direction="forward",
                            tolerance=pd.Timedelta(days=10))
    ca = snapped.dropna(subset=["td"])

    # share-count factors (split / bonus / consolidation), combined per issuer-day
    # rights issued at face value act like a bonus only when the share price is far above face value:
    # keep them only where the ex-day price gap confirms the ratio (within 15%)
    r0 = ca[ca["type"] == "rights0"].merge(px[["issuer", "date", "open", "prev_close_series"]],
                                          left_on=["issuer", "td"], right_on=["issuer", "date"], how="left")
    r0 = r0[(np.log((r0["prev_close_series"] / r0["open"]) / r0["factor"]).abs() < 0.15)]
    shf = ca[ca["type"].isin(["split", "bonus", "consolidation"])].groupby(["issuer", "td"])["factor"].prod()
    # rights change the price but not the shares a holder already owns -> kept apart from f_shares
    rtf = r0.groupby(["issuer", "td"])["factor"].prod()
    # demergers: measure the price drop on the ex-day
    dem = ca[ca["type"] == "demerger"][["issuer", "td"]].drop_duplicates()
    dem = dem.merge(px[["issuer", "date", "open", "prev_close_series"]], left_on=["issuer", "td"],
                    right_on=["issuer", "date"], how="left")
    dem["factor"] = dem["prev_close_series"] / dem["open"]
    dem = dem[(dem["factor"] >= 1.03) & (dem["factor"] <= 5)]
    # reviewed events missing from / mislabelled in NSE's feed (scripts/manual_corp_actions.csv):
    # factor measured as previous close / ex-day open, i.e. treated as value-neutral
    man = pd.read_csv(Path(__file__).resolve().parent / "manual_corp_actions.csv", parse_dates=["date"])
    man = man.merge(px[["symbol", "date", "issuer", "open", "prev_close_series"]], on=["symbol", "date"], how="left")
    man["factor"] = man["prev_close_series"] / man["open"]
    man = man.dropna(subset=["factor"]).rename(columns={"date": "td"})[["issuer", "td", "factor"]]
    dem = pd.concat([dem[["issuer", "td", "factor"]], man]).drop_duplicates(["issuer", "td"], keep="last")
    dem = dem.set_index(["issuer", "td"])["factor"]
    divs = ca[ca["type"] == "dividend"].groupby(["issuer", "td"])["dividend"].sum()

    px = px.set_index(["issuer", "date"])
    px["f_shares"] = shf.reindex(px.index).fillna(1.0).values
    px["f_demerger"] = dem.reindex(px.index).fillna(1.0).values
    px["f_rights"] = rtf.reindex(px.index).fillna(1.0).values
    px["div_raw"] = divs.reindex(px.index).fillna(0.0).values
    px = px.reset_index()
    px["f_day"] = px["f_shares"] * px["f_demerger"] * px["f_rights"]
    # cumulative factor of all events AFTER each row -> adjusted = raw / that
    px["cum_after"] = (px.groupby("issuer")["f_day"].transform(lambda s: s[::-1].cumprod()[::-1].shift(-1).fillna(1.0)))
    for c in ("open", "high", "low", "close"):
        px[f"adj_{c}"] = px[c] / px["cum_after"]
    px["adj_div"] = px["div_raw"] / px["cum_after"]
    # total-return index: daily return includes the dividend paid on the ex-date
    prev_adj = px.groupby("issuer")["adj_close"].shift(1)
    px["ret"] = (px["adj_close"] + px["adj_div"]) / prev_adj - 1
    # no return across a trading gap of more than 180 days (long suspension / relisting under the same ISIN)
    gap = (px["date"] - px.groupby("issuer")["date"].shift(1)).dt.days
    px.loc[gap > 180, "ret"] = np.nan
    px["gap_days"] = gap
    px["tr_index"] = (1 + px["ret"].fillna(0)).groupby(px["issuer"]).cumprod()
    keep = ["date", "issuer", "isin", "symbol", "series", "open", "high", "low", "close", "volume", "value",
            "f_shares", "f_demerger", "f_rights", "div_raw", "cum_after", "adj_open", "adj_high", "adj_low", "adj_close",
            "adj_div", "ret", "tr_index", "gap_days"]
    px[keep].to_parquet(OUT / "prices_adj.parquet", index=False)
    ev = px[(px["f_shares"] != 1) | (px["f_demerger"] != 1)]
    print(f"adjusted prices written; share-count events applied: {(px['f_shares'] != 1).sum()}, "
          f"demerger adjustments: {(px['f_demerger'] != 1).sum()}, dividend days: {(px['div_raw'] > 0).sum()}")
    return px, ca


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    raw = build_raw() if not (OUT / "prices_raw.parquet").exists() or "--rebuild-raw" in sys.argv \
        else pd.read_parquet(OUT / "prices_raw.parquet")
    if "--raw-only" not in sys.argv:
        build_adjusted(raw)
