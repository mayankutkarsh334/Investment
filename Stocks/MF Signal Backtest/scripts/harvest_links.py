"""Phase 1: harvest monthly-portfolio file links from saved archive pages.

Reads the saved HTML pages in data/raw/pages/, extracts every link to an
Excel/zip file with its anchor text, works out the portfolio month, and keeps
only *monthly* portfolio files (drops fortnightly, debt-only, half-yearly,
close-ended/FMP, risk-parameter files). Writes data/raw/links_<amc>.csv for review.

Run: .venv/bin/python -I scripts/harvest_links.py
"""
import csv
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "data" / "raw" / "pages"

BASE = {
    "nippon": "https://mf.nipponindiaim.com/",
    "dsp": "https://www.dspim.com/",
    "ppfas": "https://amc.ppfas.com/",
    "absl": "https://mutualfund.adityabirlacapital.com/",
}

MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
EXCLUDE = re.compile(
    r"fortnight|\bfort\b|fort-portfolio|debt|half.?year|risk.?param|close.?ended|fmp|interval|"
    r"overlap|\bsif\b|annual|abridged|gift|ifsc|segregat", re.I)
MONTH_RE = re.compile(r"(?<![a-z])(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*", re.I)


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self._href, self._text = [], None, []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href") or ""
            if re.search(r"\.(xls|xlsx|zip)(\?|$)", href, re.I):
                self._href, self._text = href, []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self._href is not None:
            self.links.append((" ".join("".join(self._text).split()), self._href))
            self._href = None


def parse_month(s: str):
    """Return (year, month, day|None) from names like 'December_31_2023', 'july-31st-2023',
    '31-Oct-26', '30-11-2012', '31122014', 'feb2014'. Day is returned when present so
    mid-month (fortnightly) files can be dropped."""
    s = s.lower().split("?")[0]
    s = re.sub(r"\.(xlsx?|zip)$", "", s)
    years = re.findall(r"(?<!\d)(20[12]\d)(?!\d)", s)
    mon = MONTH_RE.search(s)
    if mon:
        mnum = MONTHS[mon.group(1).lower()]
        day = re.search(r"(?<!\d)(\d{1,2})(?:st|nd|rd|th)?(?!\d)", s)
        if years:
            d = int(day.group(1)) if day and int(day.group(1)) <= 31 else None
            return int(years[-1]), mnum, d
        m = re.search(MONTH_RE.pattern + r"[-_ .,]*(\d\d)(?!\d)", s)  # 31-Oct-26
        if m:
            d = int(day.group(1)) if day and day.start() < mon.start() else None
            return 2000 + int(m.group(2)), mnum, d
    m = re.search(r"(?<!\d)(\d{1,2})[-._ ](\d{1,2})[-._ ](20\d\d)(?!\d)", s)  # 30-11-2012
    if not m:
        m = re.search(r"(?<!\d)(\d{2})(\d{2})(20\d\d)(?!\d)", s)  # 31122014
    if m and 1 <= int(m.group(2)) <= 12 and 1 <= int(m.group(1)) <= 31:
        return int(m.group(3)), int(m.group(2)), int(m.group(1))
    return None


def main():
    for amc, base in BASE.items():
        p = PAGES / f"{amc}.html"
        if not p.exists():
            continue
        lp = LinkParser()
        lp.feed(p.read_text(errors="ignore"))
        rows, seen = [], set()
        for text, href in lp.links:
            url = urljoin(base, href.replace("\\", "/"))
            blob = f"{text} {href}"
            if EXCLUDE.search(blob):
                continue
            ym = parse_month(href.split("/")[-1]) or parse_month(text)
            if not ym or not (2013 <= ym[0] <= 2026):
                continue
            if ym[2] is not None and 12 <= ym[2] <= 17:  # mid-month = fortnightly file
                continue
            if url in seen:
                continue
            seen.add(url)
            rows.append({"amc": amc, "year": ym[0], "month": ym[1], "text": text[:120], "url": url})
        rows.sort(key=lambda r: (r["year"], r["month"], r["url"]))
        out = ROOT / "data" / "raw" / f"links_{amc}.csv"
        with out.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["amc", "year", "month", "text", "url"])
            w.writeheader()
            w.writerows(rows)
        months = {(r["year"], r["month"]) for r in rows}
        print(f"{amc}: {len(rows)} links, {len(months)} distinct months -> {out.name}")


if __name__ == "__main__":
    main()
