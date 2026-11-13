"""Phase 6: UTI scheme-wise portfolios from Oct-2023, when UTI's consolidated zip stopped including holdings.

Scheme codes come from https://www.utimf.com/api/get_investor_scheme_fund (equity category);
files from https://www.utimf.com/api/get-scheme-portfolio-disclosure?dofa_scheme_code=..&year=..&month=..
Only .xlsx files are kept (older ones are PDFs, not needed: the consolidated zips cover up to Sep-2023).
Writes files to data/raw/files/uti/<ym>/scheme_<code>.xlsx and data/raw/manifest_uti_schemewise.csv
"""
import csv
import json
import subprocess
import time
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]


def get(url):
    r = subprocess.run(["curl", "-s", "-A", UA, "--max-time", "60", url], capture_output=True, text=True)
    return json.loads(r.stdout)


def main():
    schemes = [(x["field_fund_name"], x["field_dofa_schcode"]) for x in get("https://www.utimf.com/api/get_investor_scheme_fund")["data"]
               if str(x.get("field_scheme_fund_category", "")).lower().startswith("equity")]
    rows = []
    for y in range(2023, 2027):
        for i, mname in enumerate(MONTHS, 1):
            if (y, i) < (2023, 10) or (y, i) > (2026, 10):
                continue
            ym = f"{y}-{i:02d}"
            for name, code in schemes:
                try:
                    found = [x for x in (get(f"https://www.utimf.com/api/get-scheme-portfolio-disclosure?"
                                             f"dofa_scheme_code={code}&year={y}&month={mname}").get("rows") or [])
                             if str(x.get("type", "")).lower() in ("xlsx", "xls")]
                except Exception:
                    found = []
                if not found:
                    continue
                url = quote(found[0]["url"], safe=":/?&=%#~+,;@!$'()*")
                dest = ROOT / "data/raw/files/uti" / ym / f"scheme_{code}.xlsx"
                dest.parent.mkdir(parents=True, exist_ok=True)
                status = "ok"
                if not (dest.exists() and dest.stat().st_size > 1000):
                    code_http = subprocess.run(["curl", "-s", "-A", UA, "--max-time", "60", "-o", str(dest), "-w", "%{http_code}", url],
                                               capture_output=True, text=True).stdout
                    status = "ok" if code_http == "200" and dest.exists() and dest.stat().st_size > 1000 else f"http_{code_http}"
                    time.sleep(0.2)
                rows.append({"amc": "uti", "ym": ym, "text": f"scheme-wise {name}", "url": url,
                             "path": str(dest.relative_to(ROOT)), "status": status})
            print(ym, sum(1 for r in rows if r["ym"] == ym), "files", flush=True)
    with open(ROOT / "data/raw/manifest_uti_schemewise.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["amc", "ym", "text", "url", "path", "status"])
        w.writeheader()
        w.writerows(rows)
    print(f"{len(schemes)} equity schemes; {len(rows)} files; failed {sum(r['status'] != 'ok' for r in rows)}")


if __name__ == "__main__":
    main()
