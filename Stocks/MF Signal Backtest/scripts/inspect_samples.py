"""Phase 0: inspect sample monthly-portfolio files from each fund house.

For every workbook under the given folder, report: number of sheets, whether
ISINs (INE...) are present, the header row that contains the holdings table,
and one example equity row. Run with `python3 -I` (the files are untrusted data).
"""
import re
import sys
from pathlib import Path

import pandas as pd

ISIN = re.compile(r"\bINE[0-9A-Z]{9}\b")
HEADER_HINTS = ("isin", "name of the instrument", "name of instrument", "quantity", "% to nav", "% to net assets")


def read_all_sheets(path: Path):
    engine = "xlrd" if path.suffix.lower() == ".xls" else "openpyxl"
    return pd.read_excel(path, sheet_name=None, header=None, engine=engine, dtype=str)


def inspect(path: Path) -> None:
    try:
        sheets = read_all_sheets(path)
    except Exception as exc:  # noqa: BLE001 - report and move on
        print(f"\n### {path}  -> UNREADABLE: {type(exc).__name__}: {str(exc)[:120]}")
        return
    n_isin = 0
    header = None
    example = None
    for name, df in sheets.items():
        txt = df.fillna("")
        for _, row in txt.iterrows():
            cells = [str(c).strip() for c in row.tolist()]
            joined = " | ".join(c for c in cells if c)
            if ISIN.search(joined):
                n_isin += 1
                if example is None and re.search(r"Ltd|Limited", joined, re.I):
                    example = (name, joined[:220])
            low = joined.lower()
            if header is None and sum(h in low for h in HEADER_HINTS) >= 2:
                header = (name, joined[:220])
    print(f"\n### {path}")
    print(f"sheets={len(sheets)}  first={list(sheets)[:4]}  rows_with_ISIN={n_isin}")
    print(f"header : {header}")
    print(f"example: {example}")


if __name__ == "__main__":
    root = Path(sys.argv[1])
    for p in sorted(root.rglob("*")):
        if p.suffix.lower() in (".xls", ".xlsx") and not p.name.startswith("~$"):
            inspect(p)
