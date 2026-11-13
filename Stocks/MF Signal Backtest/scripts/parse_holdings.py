"""Phase 1: parse every downloaded monthly-portfolio file into one raw holdings table.

For each workbook (xls / xlsx / xlsb, or a zip of them) and each sheet:
  1. find the header row (has an ISIN column plus quantity and %-of-NAV columns);
  2. read the scheme name from the rows above it (or the file name for one-scheme files);
  3. keep rows whose ISIN is an Indian equity share (INE......01..);
  4. record a per-sheet summary (rows, sum of equity %, sum of all ISIN rows %) for checks.

% of NAV is stored as a percent (8.56 = 8.56%). Sheets that report fractions
(sum of all rows ~= 1) are scaled by 100.

Outputs (data/interim/):
  holdings_raw.parquet  - amc, ym, file, sheet, scheme_raw, isin, name, industry, qty, mv_lakhs, pct
  sheets_raw.parquet    - one row per parsed sheet with the summary numbers
  parse_errors.csv      - files that could not be read
Run: .venv/bin/python -I scripts/parse_holdings.py [--amc hdfc] [--limit N]
"""
import argparse
import csv
import io
import re
import sys
import zipfile
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
INTERIM = ROOT / "data" / "interim"
ISIN_RE = re.compile(r"^IN[E9][A-Z0-9]{9}$")
SCHEME_WORD = re.compile(r"\b(fund|scheme|plan|taxgain|tax saver|taxsaver|elss|portfolio)\b", re.I)
NOT_SCHEME = re.compile(r"^(sbi|hdfc|nippon india|reliance|ppfas|dsp( blackrock)?|aditya birla sun life|birla sun life|"
                        r"icici prudential|axis|uti)?\s*"
                        r"(mutual fund|asset management.*|amc.*)$|portfolio (statement )?as (on|at)|"
                        r"monthly portfolio|^name of|back to index", re.I)


def to_num(v):
    if v is None:
        return None
    s = str(v).strip().replace(",", "").replace("%", "")
    if s in ("", "-", "--", "NIL", "nan", "None"):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def clean_scheme(s: str) -> str:
    s = re.sub(r"\s+", " ", str(s)).strip()
    s = re.sub(r"^(scheme name|name of the scheme|scheme)\s*:?\s*", "", s, flags=re.I)
    s = re.split(r"\s*\((an )?(open|close)[ -]?ended", s, flags=re.I)[0]
    s = re.sub(r"\s*\(formerly.*$", "", s, flags=re.I)
    return s.strip(" -:")


def find_cols(cells):
    """Map column roles from a header row (list of lower-cased strings)."""
    cols = {}
    for i, c in enumerate(cells):
        if not c or re.search(r"coupon|yield|ytm|ytc|brsr|esg", c):
            continue
        if "isin" in c and "isin" not in cols:
            cols["isin"] = i
        elif ("name of" in c or "instrument" in c or "issuer" in c or c == "name" or "security" in c) and "name" not in cols:
            cols["name"] = i
        elif ("industry" in c or "rating" in c or "sector" in c) and "industry" not in cols:
            cols["industry"] = i
        elif ("quantity" in c or c in ("qty", "no. of shares", "units")) and "qty" not in cols:
            cols["qty"] = i
        elif ("market" in c or "fair value" in c or "value" in c) and "%" not in c and "mv" not in cols:
            cols["mv"] = i
        elif ("%" in c or "percent" in c or "to nav" in c or "net assets" in c or "to aum" in c) and "pct" not in cols:
            cols["pct"] = i
    return cols


def scheme_from_top(rows_above, file_hint):
    cands = []
    for cells in rows_above:
        for j, c in enumerate(cells):
            t = str(c).strip()
            if not t:
                continue
            if re.match(r"^(scheme name|name of the scheme)\s*:?\s*$", t, re.I) and j + 1 < len(cells):
                nxt = [x for x in cells[j + 1:] if str(x).strip()]
                if nxt:
                    return clean_scheme(nxt[0])
            if re.match(r"^(scheme name|name of the scheme)\s*:", t, re.I):
                return clean_scheme(t)
            if SCHEME_WORD.search(t) and not NOT_SCHEME.search(t) and len(t) < 160:
                cands.append(clean_scheme(t))
    if cands:
        return cands[0]
    for cells in rows_above:  # no 'fund'/'scheme' word: first multi-word title that isn't boilerplate
        for c in cells:
            t = str(c).strip()
            if (len(t.split()) >= 2 and not NOT_SCHEME.search(t) and not t.startswith("(")
                    and not re.search(r"\d{4}|limited|ltd|tel|fax|floor|office|road", t, re.I)):
                return clean_scheme(t)
    return clean_scheme(file_hint)


MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


def as_of_from_top(rows_above):
    """'YYYY-MM' of the 'Portfolio as on ...' date printed above the table, if any."""
    for cells in rows_above:
        line = " ".join(str(c) for c in cells if str(c).strip())
        if not re.search(r"as (on|at)|statement|portfolio", line, re.I):
            continue
        m = re.search(r"(20[12]\d)-(\d{2})-(\d{2})", line)  # 2013-11-30 00:00:00
        if m:
            return f"{m.group(1)}-{m.group(2)}"
        m = re.search(r"(?<![a-z])(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?[\s,\-]*(\d{1,2}(?:st|nd|rd|th)?[\s,\-]+)?(20[12]\d|\d{2})(?!\d)", line, re.I)
        if m:
            y = int(m.group(3))
            return f"{y + 2000 if y < 100 else y}-{MONTHS[m.group(1).lower()]:02d}"
        m = re.search(r"(?<!\d)(\d{1,2})[./\-](\d{1,2})[./\-](20[12]\d)(?!\d)", line)
        if m and 1 <= int(m.group(2)) <= 12:
            return f"{m.group(3)}-{int(m.group(2)):02d}"
    return None


def parse_sheet(df: pd.DataFrame, file_hint: str):
    vals = df.fillna("").astype(str).values.tolist()
    hdr = None
    for r, row in enumerate(vals[:40]):
        low = [c.strip().lower() for c in row]
        if any("isin" in c for c in low) and any(("quantity" in c or "qty" in c) for c in low):
            hdr = r
            break
    if hdr is None:  # some months leave the ISIN column unlabelled: header = quantity + instrument name
        for r, row in enumerate(vals[:40]):
            low = [c.strip().lower() for c in row]
            if any(("quantity" in c or "qty" in c) for c in low) and any(("instrument" in c or "name of" in c) for c in low):
                hdr = r
                break
    if hdr is None:
        return None, None
    cols = find_cols([c.strip().lower() for c in vals[hdr]])
    if "isin" not in cols:  # find the column whose values look like ISINs
        body = vals[hdr + 1: hdr + 80]
        best, best_n = None, 0
        for j in range(max(len(r) for r in body) if body else 0):
            n = sum(1 for r in body if j < len(r) and ISIN_RE.match(r[j].strip().upper()))
            if n > best_n:
                best, best_n = j, n
        if best is None or best_n < 3:
            return None, None
        # labels to the right of an unlabelled ISIN column are shifted by one in these files
        lab = [c.strip().lower() for c in vals[hdr]]
        cols = find_cols(lab)
        cols["isin"] = best
        if cols.get("name") is not None and cols["name"] >= best:
            pass
        # realign: if the label row is one cell short (no 'ISIN' label), shift labels right of the name column
        sample = [r for r in body if best < len(r) and ISIN_RE.match(r[best].strip().upper())][:5]
        for role in ("industry", "qty", "mv", "pct"):
            j = cols.get(role)
            if j is None or not sample:
                continue
            ok = sum(1 for r in sample if j < len(r) and (to_num(r[j]) is not None) == (role != "industry"))
            ok_shift = sum(1 for r in sample if j + 1 < len(r) and (to_num(r[j + 1]) is not None) == (role != "industry"))
            if ok_shift > ok:
                cols[role] = j + 1
        if "name" in cols:
            j = cols["name"]
            if sample and all(j < len(r) and to_num(r[j]) is not None for r in sample):
                cols["name"] = j + 1
    if "qty" not in cols:
        return None, None
    scheme = scheme_from_top(vals[:hdr], file_hint)
    out, tot_all = [], 0.0
    for row in vals[hdr + 1:]:
        isin = row[cols["isin"]].strip().upper() if cols["isin"] < len(row) else ""
        if not ISIN_RE.match(isin):
            continue
        pct = to_num(row[cols["pct"]]) if "pct" in cols and cols["pct"] < len(row) else None
        tot_all += pct or 0.0
        if not (isin.startswith("INE") and isin[7:9] == "01"):
            continue
        out.append({
            "isin": isin,
            "name": row[cols["name"]].strip() if "name" in cols and cols["name"] < len(row) else "",
            "industry": row[cols["industry"]].strip() if "industry" in cols and cols["industry"] < len(row) else "",
            "qty": to_num(row[cols["qty"]]),
            "mv_lakhs": to_num(row[cols["mv"]]) if "mv" in cols and cols["mv"] < len(row) else None,
            "pct": pct,
        })
    scale = 100.0 if 0 < tot_all <= 1.5 else 1.0
    for o in out:
        if o["pct"] is not None:
            o["pct"] *= scale
    summ = {"scheme_raw": scheme, "n_eq": len(out), "eq_pct": sum((o["pct"] or 0) for o in out),
            "all_pct": tot_all * scale, "scale": scale, "asof": as_of_from_top(vals[:hdr])}
    return out, summ


def read_book(data: bytes, name: str):
    ext = name.lower().rsplit(".", 1)[-1]
    engine = {"xls": "xlrd", "xlsx": "openpyxl", "xlsm": "openpyxl", "xlsb": "pyxlsb"}.get(ext)
    if engine is None:
        raise ValueError(f"unsupported extension {ext}")
    try:
        return pd.read_excel(io.BytesIO(data), sheet_name=None, header=None, dtype=str, engine=engine)
    except Exception:
        if engine == "xlrd":  # some '.xls' are really xlsx or html
            return pd.read_excel(io.BytesIO(data), sheet_name=None, header=None, dtype=str, engine="openpyxl")
        raise


def index_map(book):
    """Scheme code -> name from an 'Index' / 'Schemes' sheet, when the workbook has one."""
    m = {}
    for sname, df in book.items():
        if not re.match(r"^(index|schemes?|scheme index|contents)$", str(sname).strip(), re.I):
            continue
        sheet_names = {str(s).strip().upper() for s in book}
        for row in df.fillna("").astype(str).values.tolist():
            cells = [c.strip() for c in row if c.strip()]
            code = next((c for c in cells if c.upper() in sheet_names), None)
            name = None
            if code:
                after = cells[cells.index(code) + 1:] + cells[:cells.index(code)]
                name = next((c for c in after if len(c) > 8 and " " in c and c.upper() not in sheet_names), None)
            if code and name:
                m[code.upper()] = clean_scheme(name)
    return m


def split_blocks(sname, df: pd.DataFrame):
    """Some fund houses (UTI) stack every scheme in one sheet. When a sheet has several holdings
    header rows, cut it into one block per scheme, starting at the scheme title just above each header."""
    vals = df.fillna("").astype(str).values.tolist()
    hdrs = [r for r, row in enumerate(vals)
            if any("isin" in c.lower() for c in row) and any(("quantity" in c.lower() or "qty" in c.lower()) for c in row)]
    if len(hdrs) < 2:
        return [(sname, df)]
    starts, titled = [], 0
    for h in hdrs:
        st = h
        for r in range(h - 1, max(h - 8, -1), -1):
            line = " ".join(c for c in vals[r] if c.strip())
            if re.search(r"^\s*scheme\s*:|scheme name", line, re.I):
                st = r
                titled += 1
                break
        starts.append(st)
    # only a sheet where (almost) every table has its own scheme title is a stacked multi-scheme sheet
    # (UTI); otherwise the extra header rows are sub-tables of one scheme (ICICI derivatives etc.)
    if titled < max(2, len(hdrs) - 1):
        return [(sname, df)]
    starts[0] = 0
    blocks = []
    for i, st in enumerate(starts):
        en = starts[i + 1] if i + 1 < len(starts) else len(vals)
        blocks.append((f"{sname}#{i + 1}", df.iloc[st:en].reset_index(drop=True)))
    return blocks


def parse_file(rec):
    path = ROOT / rec["path"]
    rows, sheets = [], []
    books = []
    def from_zip(zf):   # workbooks inside a zip, including zips nested inside it (UTI)
        for n in zf.namelist():
            if n.startswith("__MACOSX") or "/." in n:
                continue
            if re.search(r"\.(xls|xlsx|xlsb|xlsm)$", n, re.I):
                books.append((n, zf.read(n)))
            elif n.lower().endswith(".zip"):
                with zipfile.ZipFile(io.BytesIO(zf.read(n))) as inner:
                    from_zip(inner)

    if path.suffix.lower() == ".zip":
        with zipfile.ZipFile(path) as z:
            from_zip(z)
    else:
        books.append((path.name, path.read_bytes()))
    for bname, data in books:
        book = read_book(data, bname)
        codes = index_map(book)
        for sname0, df0 in book.items():
          for sname, df in split_blocks(sname0, df0):
              if df.shape[0] < 3:
                  continue
              hint = Path(bname).stem if len(book) == 1 else str(sname)
              out, summ = parse_sheet(df, hint)
              if summ is None:
                  continue
              if not summ["asof"]:  # fall back to a date in the workbook's own file name
                  summ["asof"] = as_of_from_top([["portfolio " + Path(bname).stem.replace("_", " ")]])
              mapped = codes.get(str(sname).strip().upper())
              if mapped and (not summ["scheme_raw"] or summ["scheme_raw"].upper() == str(sname).strip().upper()
                             or not SCHEME_WORD.search(summ["scheme_raw"])):
                  summ["scheme_raw"] = mapped
              key = {"amc": rec["amc"], "ym": rec["ym"], "file": rec["path"], "book": bname, "sheet": str(sname)}
              sheets.append({**key, **summ})
              for o in out:
                  rows.append({**key, "scheme_raw": summ["scheme_raw"], **o})
    return rows, sheets


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--amc")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()
    recs, seen = [], set()
    for mf in sorted((ROOT / "data/raw").glob("manifest_*.csv")):
        for r in csv.DictReader(open(mf)):
            if r["status"] == "ok" and r["path"] not in seen:
                seen.add(r["path"])
                recs.append(r)
    if args.amc:
        recs = [r for r in recs if r["amc"] == args.amc]
    if args.limit:
        recs = recs[: args.limit]
    INTERIM.mkdir(parents=True, exist_ok=True)
    all_rows, all_sheets, errors = [], [], []
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(parse_file, r): r for r in recs}
        for i, f in enumerate(as_completed(futs), 1):
            r = futs[f]
            try:
                rows, sheets = f.result()
                all_rows += rows
                all_sheets += sheets
                if not sheets:
                    errors.append({**r, "error": "no holdings sheet found"})
            except Exception as e:  # noqa: BLE001
                errors.append({**r, "error": f"{type(e).__name__}: {str(e)[:200]}"})
            if i % 200 == 0:
                print(f"  parsed {i}/{len(recs)}", flush=True)
    suffix = f"_{args.amc}" if args.amc else ""
    pd.DataFrame(all_rows).to_parquet(INTERIM / f"holdings_raw{suffix}.parquet", index=False)
    pd.DataFrame(all_sheets).to_parquet(INTERIM / f"sheets_raw{suffix}.parquet", index=False)
    pd.DataFrame(errors).to_csv(INTERIM / f"parse_errors{suffix}.csv", index=False)
    print(f"files={len(recs)} sheets={len(all_sheets)} equity_rows={len(all_rows)} errors={len(errors)}")


if __name__ == "__main__":
    sys.exit(main())
