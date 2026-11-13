"""Phase 1: build HDFC's monthly-portfolio link list from saved API responses.

HDFC's API (cms.hdfcfund.com .../disclosures/monthfortportfolio) was saved per year
(data/raw/pages/hdfc_api/<year>.json) and per month for 2019+ (<year>_<mm>.json).
Up to ~Jul-2021 there is one consolidated workbook per month (sometimes split
Equity / Debt). From ~Aug-2021 there is one file per scheme; we keep only schemes
that can be actively managed equity (debt, liquid, ETF, index, FoF, arbitrage,
hybrid-debt names are skipped to save downloads; final classification is in Phase 1 parsing).
"""
import csv
import glob
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from harvest_links import parse_month  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SKIP = re.compile(
    r"FMP|Interval|Close.?ended|Fixed Maturity|Fortnight|Debt|Liquid|Overnight|Money Market|Gilt|"
    r"Bond|Credit|Duration|Banking (and|&) PSU|Floating|Income|Arbitrage|ETF|Index|FoF|Fund of Fund|"
    r"Gold|Silver|Nifty|Sensex|BSE|Dynamic Debt|Ultra Short|Low Duration|Short Term|Medium Term|"
    r"Corporate|Savings|Retirement.*(Debt|Hybrid-Debt)|Hybrid Debt|Equity Savings|Conservative|Target Maturity|SDL|CRISIL",
    re.I)


def main():
    seen, rows = set(), []
    paths = sorted(glob.glob(str(ROOT / "data/raw/pages/hdfc_api/*_*.json")))  # per-month first
    paths += sorted(glob.glob(str(ROOT / "data/raw/pages/hdfc_api/20[0-9][0-9].json")))
    for p in paths:
        d = json.load(open(p))
        qm = re.search(r"(\d{4})_(\d{2})\.json$", p)  # month the API was asked for
        for f in (d.get("data") or {}).get("files") or []:
            title, fn, url = f["title"], f["file"]["filename"], f["file"]["url"]
            if url in seen:
                continue
            seen.add(url)
            per_scheme = not re.search(r"Monthly Portfolio|Portfolios for|Portfolio -|Whole Portfolio", title, re.I)
            if per_scheme:
                if SKIP.search(title):
                    continue
            elif (re.search(r"FMP|Interval|Close|Fortnight", title + " " + fn, re.I)
                  or re.search(r"\((Debt|DEBT)|\bDEBT\b|Debt Schemes\)", fn)
                  or re.search(r"(?<!than )Debt Schemes", title, re.I)):
                continue
            pm = (int(qm.group(1)), int(qm.group(2)), None) if qm else (parse_month(fn) or parse_month(title))
            if not pm or not ((2013, 9) <= (pm[0], pm[1]) <= (2026, 10)):
                continue
            rows.append({"amc": "hdfc", "year": pm[0], "month": pm[1],
                         "text": ("SCHEME: " if per_scheme else "ALL: ") + title[:100], "url": url})
    rows.sort(key=lambda r: (r["year"], r["month"], r["text"]))
    with open(ROOT / "data/raw/links_hdfc.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["amc", "year", "month", "text", "url"])
        w.writeheader()
        w.writerows(rows)
    by = {}
    for r in rows:
        k = (r["year"], r["month"])
        by.setdefault(k, [0, 0])[0 if r["text"].startswith("ALL") else 1] += 1
    allm = [(y, m) for y in range(2013, 2027) for m in range(1, 13) if (2013, 9) <= (y, m) <= (2026, 10)]
    print(f"hdfc: {len(rows)} links")
    print("missing:", [f"{y}-{m:02d}" for y, m in allm if (y, m) not in by])
    print("consolidated>1:", {f"{y}-{m:02d}": v[0] for (y, m), v in sorted(by.items()) if v[0] > 1})
    print("per-scheme counts (sample):", {f"{y}-{m:02d}": v[1] for (y, m), v in sorted(by.items()) if v[1]}.__repr__()[:400])


if __name__ == "__main__":
    main()
