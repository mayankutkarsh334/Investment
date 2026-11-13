"""Phase 1: build the download manifest from links_<amc>.csv and fetch every file.

Selection rules
- PPFAS: when a month has a consolidated workbook, take only that; otherwise take the
  equity-scheme files (Flexi Cap PPFCF, ELSS PPTSF, Large Cap PPLCF) and skip liquid,
  arbitrage, hybrid and dynamic-asset files.
- Everyone else: take every monthly link (the parser later keeps one copy per scheme-month).

Files land in data/raw/files/<amc>/<yyyy-mm>/<name>. Existing files are skipped, so the
script can be re-run after an interruption. Writes data/raw/manifest.csv.
Run: .venv/bin/python -I scripts/download.py [amc ...]   (writes manifest_<amc>.csv)
"""
import csv
import re
import subprocess
import time
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote, unquote, urljoin, urlparse

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"
AMCS = ["hdfc", "sbi", "nippon", "absl", "dsp", "ppfas", "icici", "axis", "uti"]
PPFAS_EQUITY = re.compile(r"^(PPFCF|PPTSF|PPLCF)_", re.I)
PPFAS_OTHER = re.compile(r"^(PPLF|PPAF|PPCHF|PPDAAF|PPMAAF|PPAAF)_", re.I)


def select(rows):
    if rows[0]["amc"] != "ppfas":
        return rows
    names = [Path(urlparse(r["url"]).path).name for r in rows]
    cons = [r for r, n in zip(rows, names) if r["text"].lower().startswith("consolidated")
            or re.match(r"^(PPFAS_Monthly|Monthly-Portfolio|Monthly_Portfolio|PPFAS-Monthly)", n, re.I)]
    if cons:
        return cons[:1]
    return [r for r, n in zip(rows, names) if PPFAS_EQUITY.match(n) or not PPFAS_OTHER.match(n)]


def main():
    import sys
    amcs = [a for a in sys.argv[1:] if a in AMCS] or AMCS
    manifest = []
    for amc in amcs:
        groups = defaultdict(list)
        for r in csv.DictReader(open(RAW / f"links_{amc}.csv")):
            groups[(int(r["year"]), int(r["month"]))].append(r)
        for (y, m), rows in sorted(groups.items()):
            for r in select(rows):
                name = unquote(Path(urlparse(r["url"]).path).name)
                name = re.sub(r"[^\w.\-() &]+", "_", name)[:150]
                dest = RAW / "files" / amc / f"{y}-{m:02d}" / name
                manifest.append({"amc": amc, "ym": f"{y}-{m:02d}", "text": r["text"], "url": r["url"],
                                 "path": str(dest.relative_to(ROOT))})
    import os
    shard = os.environ.get("SHARD")  # e.g. "0/4": take every 4th file starting at 0
    if shard:
        i, n = map(int, shard.split("/"))
        manifest = manifest[i::n]
    tag = ("_".join(amcs) if len(amcs) < len(AMCS) else "all") + (f"_s{shard.replace('/', 'of')}" if shard else "")
    with open(RAW / f"manifest_{tag}.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["amc", "ym", "text", "url", "path", "status"])
        w.writeheader()
        todo = [m for m in manifest if not (ROOT / m["path"]).exists()]
        print(f"manifest: {len(manifest)} files, {len(todo)} to download", flush=True)
        done = 0
        for m in manifest:
            dest = ROOT / m["path"]
            if dest.exists() and dest.stat().st_size > 0:
                m["status"] = "ok"
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                code = "000"
                url = m["url"]
                if not url.startswith("http"):  # UTI lists some files with site-relative paths
                    url = urljoin("https://www.utimf.com/", url)
                url = quote(url, safe=":/?&=%#~+,;@!$'()*")  # spaces etc. in file names
                for attempt in range(3):
                    res = subprocess.run(
                        ["curl", "-sL", "-A", UA, "--max-time", "120", "-o", str(dest), "-w", "%{http_code}", url],
                        capture_output=True, text=True)
                    code = res.stdout.strip()
                    if code == "200" and dest.exists() and dest.stat().st_size > 500:
                        break
                    time.sleep(2 * (attempt + 1))
                m["status"] = "ok" if code == "200" else f"http_{code}"
                if m["status"] != "ok" and dest.exists():
                    dest.unlink()
                done += 1
                if done % 50 == 0:
                    print(f"  {done}/{len(todo)} downloaded", flush=True)
                time.sleep(0.3)
            w.writerow(m)
    bad = [m for m in manifest if m.get("status") != "ok"]
    print(f"finished: {len(manifest) - len(bad)} ok, {len(bad)} failed")
    for m in bad[:20]:
        print("  FAILED", m["amc"], m["ym"], m["status"], m["url"][:120])


if __name__ == "__main__":
    main()
