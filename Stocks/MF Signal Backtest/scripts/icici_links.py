"""Phase 6: ICICI Prudential monthly-portfolio links via the site's download API.

POST https://apimf.icicipruamc.com/nms/v1/downloads/files (headers sourceUrl: DOWNLOADS, env: api),
one call per financial year; files are served from https://www.icicipruamc.com/blob<url>.
Keeps the consolidated 'Monthly Portfolio Disclosure <Month> <Year>' zip; where a month only has
per-category files (Feb-2019) it keeps the Equity file.
Writes data/raw/links_icici.csv
"""
import csv
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from harvest_links import parse_month  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
CAT = "26a073d7-08d2-4a95-95fa-f83a4ee51e40"


def fetch(fy):
    body = {"categoryId": f"{fy},{CAT}", "schemeCategory": "", "userType": "Investor", "fileType": "All",
            "page": "1", "size": "100", "filter": [{"FINANCIAL_YEAR": [fy]}], "categoryName": "OTHERS"}
    r = subprocess.run(["curl", "-s", "-A", UA, "-X", "POST", "https://apimf.icicipruamc.com/nms/v1/downloads/files",
                        "-H", "Content-type: application/json", "-H", "sourceUrl: DOWNLOADS", "-H", "env: api",
                        "-H", "Origin: https://www.icicipruamc.com", "-H", "Referer: https://www.icicipruamc.com/",
                        "--data", json.dumps(body)], capture_output=True, text=True)
    return json.loads(r.stdout)["success"]["data"]["files"]


def main():
    seen, by_month = set(), {}
    for y in range(2012, 2027):
        for f in fetch(f"{y}-{y + 1}"):
            title, url = f["title"]["text"].strip(), f["url"]
            if url in seen or not re.search(r"monthly portfolio", title, re.I):
                continue
            seen.add(url)
            pm = parse_month(title) or parse_month(url.split("/")[-1])
            if not pm:
                continue
            ym = (pm[0], pm[1])
            consolidated = bool(re.search(r"\.zip$", url, re.I)) and not re.search(
                r"money market|liquid|flexible income|debt|fmp|gold|fof|hybrid|arbitrage|cpof|myf", title, re.I)
            equity_only = bool(re.search(r"\bequity\b", title, re.I)) and url.lower().endswith((".xls", ".xlsx"))
            rank = 2 if consolidated else (1 if equity_only else 0)
            if rank and rank >= by_month.get(ym, (0,))[0]:
                by_month[ym] = (rank, title, "https://www.icicipruamc.com/blob" + quote(url))
    rows = [{"amc": "icici", "year": y, "month": m, "text": t, "url": u} for (y, m), (_, t, u) in sorted(by_month.items())]
    with open(ROOT / "data/raw/links_icici.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["amc", "year", "month", "text", "url"])
        w.writeheader()
        w.writerows(rows)
    allm = [(y, m) for y in range(2014, 2027) for m in range(1, 13) if (2014, 4) <= (y, m) <= (2026, 10)]
    print(f"icici: {len(rows)} months; missing: {[f'{y}-{m:02d}' for y, m in allm if (y, m) not in by_month]}")


if __name__ == "__main__":
    main()
