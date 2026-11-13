"""Phase 2: turn NSE corporate-action records into share-count / price factors and dividends.

Types kept
  split        'Face Value Split (Sub-Division) - From Rs 10/- To Rs 2/-'  -> factor 10/2 = 5 (shares x5, price /5)
  bonus        'Bonus 1:2' (1 new for every 2 held)                       -> factor (1+2)/2 = 1.5
  consolidation 'From Rs 1 to Rs 10' (reverse split)                       -> factor 0.1
  demerger     price drops as holders receive new-company shares; factor is measured from prices later
  dividend     'Dividend - Rs 2.50 Per Share' (all amounts in one subject are added)
Rights issues are ignored (small price effect; holders are not forced to take them).

Input : data/raw/nse/corpact/*.json
Output: data/processed/corp_actions.parquet  symbol, isin, series, ex_date, type, factor, dividend, subject
"""
import glob
import json
import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

SPLIT = re.compile(r"(?:from\s*)?(?:face value\s*)?(?:rs|re)?\.?\s*([\d]+(?:\.\d+)?)\s*/?-?.*?\bto\s*"
                   r"(?:face value\s*)?(?:rs|re)?\.?\s*([\d]+(?:\.\d+)?)", re.I)
BONUS = re.compile(r"bonus\s*(?:issue)?\s*-?\s*(\d+)\s*:\s*(\d+)", re.I)
DIV = re.compile(r"(?:dividend|\bdiv\b)\s*[-:]*\s*(?:of\s*)?(?:rs|re|inr)?\s*[.:\-]*\s*([\d]+(?:\.\d+)?)", re.I)


def parse(r):
    s = " ".join(str(r.get("subject", "")).split())
    low = s.lower()
    out = []
    kw = re.search(r"split|splt|sub-?division|consolidat", low)
    if kw:
        m = SPLIT.search(s[kw.start():])  # read the numbers only after the word 'split'
        if m:
            a, b = float(m.group(1)), float(m.group(2))
            if a > 0 and b > 0 and a != b:
                out.append(("split" if a > b else "consolidation", a / b, 0.0))
    for m in ([] if re.search(r"ncrps|debenture|preference|\bncd", low) else BONUS.finditer(s)):
        a, b = int(m.group(1)), int(m.group(2))
        if a > 0 and b > 0:
            out.append(("bonus", (a + b) / b, 0.0))
    m = re.search(r"rights\s*(\d+)\s*:\s*(\d+)\s*@\s*premium\s*(?:rs|re)?\.?\s*0\b", low)
    if m:  # rights at zero premium (issued at face value) behaves like a bonus
        a, b = int(m.group(1)), int(m.group(2))
        out.append(("rights0", (a + b) / b, 0.0))
    if re.search(r"demerg|spin.?off|scheme of arrangement", low):
        out.append(("demerger", None, 0.0))
    if "dividend" in low or re.search(r"\bdiv\b", low):
        amt = sum(float(x) for x in DIV.findall(s))
        if amt > 0:
            out.append(("dividend", None, amt))
    return out


def main():
    rows = []
    for f in sorted(glob.glob(str(ROOT / "data/raw/nse/corpact/*.json"))):
        for r in json.load(open(f)):
            if r.get("series") not in ("EQ", "BE", "BZ", "SM", "ST", "BT"):
                continue
            for typ, factor, div in parse(r):
                rows.append({"symbol": r["symbol"], "isin": r.get("isin"), "series": r["series"],
                             "ex_date": pd.to_datetime(r["exDate"], format="%d-%b-%Y", errors="coerce"),
                             "type": typ, "factor": factor, "dividend": div, "subject": r["subject"].strip()})
    df = pd.DataFrame(rows).dropna(subset=["ex_date"])
    # the same action is sometimes listed twice (e.g. 'Purpose Revised'): keep one per symbol/date/type
    df = df.sort_values(["symbol", "ex_date", "type"]).drop_duplicates(["symbol", "ex_date", "type", "factor", "dividend"])
    df = df.drop_duplicates(["symbol", "ex_date", "type"], keep="last")
    out = ROOT / "data/processed/corp_actions.parquet"
    df.to_parquet(out, index=False)
    print(df["type"].value_counts().to_string())
    print(df[df.type.isin(["split", "bonus", "consolidation"])].sample(8, random_state=1)[
        ["symbol", "ex_date", "type", "factor", "subject"]].to_string(index=False))


if __name__ == "__main__":
    main()
