"""Phase 2: download NSE daily equity price files (bhavcopy), Nov-2013 -> Oct-2026.

Two formats:
  old   content/historical/EQUITIES/YYYY/MON/cmDDMONYYYYbhav.csv.zip   (to early Jul-2024)
  UDiFF content/cm/BhavCopy_NSE_CM_0_0_0_YYYYMMDD_F_0000.csv.zip      (from Jul-2024)
Every weekday is tried; holidays return 404 and are recorded as such.
Files land in data/raw/nse/bhav/<YYYY>/; a log CSV records the outcome per date.
Run: .venv/bin/python -I scripts/download_prices.py [start YYYY-MM-DD] [end YYYY-MM-DD]
"""
import csv
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "raw" / "nse" / "bhav"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"
UDIFF_FROM = date(2024, 7, 8)


def urls(d: date):
    old = (f"https://nsearchives.nseindia.com/content/historical/EQUITIES/{d.year}/{d.strftime('%b').upper()}/"
           f"cm{d.strftime('%d%b%Y').upper()}bhav.csv.zip")
    new = f"https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_{d.strftime('%Y%m%d')}_F_0000.csv.zip"
    return [new, old] if d >= UDIFF_FROM else [old, new]


def fetch(d: date):
    dest_dir = OUT / str(d.year)
    for kind, u in zip(("udiff", "old") if d >= UDIFF_FROM else ("old", "udiff"), urls(d)):
        dest = dest_dir / f"{d.isoformat()}_{kind}.csv.zip"
        if dest.exists() and dest.stat().st_size > 1000:
            return d, kind, "cached"
    dest_dir.mkdir(parents=True, exist_ok=True)
    for kind, u in zip(("udiff", "old") if d >= UDIFF_FROM else ("old", "udiff"), urls(d)):
        dest = dest_dir / f"{d.isoformat()}_{kind}.csv.zip"
        for attempt in range(3):
            r = subprocess.run(["curl", "-s", "-A", UA, "--max-time", "60", "-o", str(dest), "-w", "%{http_code}", u],
                               capture_output=True, text=True)
            code = r.stdout.strip()
            if code == "200" and dest.exists() and dest.stat().st_size > 1000:
                return d, kind, "ok"
            if code == "404":
                break
            time.sleep(2 * (attempt + 1))
        if dest.exists():
            dest.unlink()
    return d, "-", "missing"


def main():
    start = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date(2013, 11, 1)
    end = date.fromisoformat(sys.argv[2]) if len(sys.argv) > 2 else date(2026, 11, 11)
    days = [start + timedelta(i) for i in range((end - start).days + 1)]
    days = [d for d in days if d.weekday() < 5]
    print(f"{len(days)} weekdays to check", flush=True)
    res = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        for i, r in enumerate(ex.map(fetch, days), 1):
            res.append(r)
            if i % 250 == 0:
                print(f"  {i}/{len(days)}  ok so far: {sum(1 for x in res if x[2] in ('ok','cached'))}", flush=True)
    with open(OUT.parent / "bhav_log.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["date", "format", "status"])
        for d, k, s in sorted(res):
            w.writerow([d.isoformat(), k, s])
    ok = sum(1 for r in res if r[2] in ("ok", "cached"))
    print(f"done: {ok} trading-day files, {len(res) - ok} weekdays with no file (holidays or gaps)")


if __name__ == "__main__":
    main()
