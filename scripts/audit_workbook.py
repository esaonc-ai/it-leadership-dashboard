#!/usr/bin/env python3
"""Audit every worksheet and reconcile the embedded snapshot to source cells.

Reads only; never serializes the workbook through an Excel library.
"""
import argparse
import csv
import hashlib
import json
import re
import warnings
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from zipfile import ZipFile

from openpyxl import load_workbook


def clean(value):
    if value is None:
        return ""
    if isinstance(value, (date, datetime)):
        return value.strftime("%Y-%m-%d")
    return str(value).strip()


def date_kind(value):
    value = clean(value)
    if not value:
        return "missing"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        try:
            date.fromisoformat(value)
            return "calendar"
        except ValueError:
            return "invalid"
    if value.upper().startswith("TBD"):
        return "TBD"
    if value.upper() == "N/A":
        return "N/A"
    return "source text / relative estimate"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("workbook", type=Path)
    parser.add_argument("--output", type=Path, default=Path("qa-local"))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    before = hashlib.sha256(args.workbook.read_bytes()).hexdigest()
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        formulas = load_workbook(args.workbook, data_only=False)
        cached = load_workbook(args.workbook, data_only=True)
    root = Path(__file__).resolve().parent.parent
    html = (root / "index.html").read_text()
    payload = json.loads(re.search(r"/\* DASHBOARD_DATA_START \*/(.*?)/\* DASHBOARD_DATA_END \*/", html, re.S)[1])
    actual = {(r["team"], r["sourceRow"]): r for r in payload["records"]}
    sheets, issues, gaps, mapping, all_keys = [], [], [], [], []
    date_counts = {"start": Counter(), "finish": Counter()}
    for sheet in formulas:
        header = next((r for r in range(1, sheet.max_row + 1)
                       if [clean(sheet.cell(r, c).value) for c in range(1, 5)] ==
                       ["#", "Project / Workstream", "Status", "RAG Status"]), None)
        rows, excluded, errors, missing = [], [], [], []
        for cells in sheet:
            for cell in cells:
                cache = cached[sheet.title][cell.coordinate]
                if cell.data_type == "f" or cell.data_type == "e" or cache.data_type == "e":
                    item = {"sheet": sheet.title, "cell": cell.coordinate,
                            "formulaOrValue": clean(cell.value), "cachedValue": clean(cache.value),
                            "cachedError": cache.data_type == "e"}
                    errors.append(item)
                    if item["cachedError"]:
                        issues.append(item)
            r = cells[0].row
            populated = [c for c in cells if c.value is not None]
            if not populated or r == header:
                continue
            if header is None or r < header or not (clean(cells[0].value) and clean(cells[1].value)):
                excluded.append({"row": r, "reason": "title/banner" if header and r < header else "no identifier/project",
                                 "populatedCells": {c.coordinate: clean(c.value) for c in populated}})
                continue
            rows.append(r)
            key = (sheet.title, r)
            all_keys.append(key)
            record = actual[key]
            # This workbook's eight sheets all use A:N, verified from their headers.
            fields = {"id": "A", "project": "B", "status": "C", "rag": "D", "start": "E",
                      "finish": "F", "objective": "H", "progress": "I", "next": "J", "owner": "K",
                      "risks": "L", "attention": "M", "source": "N"}
            for field, col in fields.items():
                cell = sheet[f"{col}{r}"]
                value = clean(cell.value)
                if field == "source" and value.startswith("=_xlfn.DISPIMG("):
                    value = "Embedded workbook image; view in source workbook"
                assert record[field] == value, (sheet.title, cell.coordinate, field, record[field], value)
                if not value:
                    missing.append(cell.coordinate)
                    gaps.append([sheet.title, cell.coordinate, field, "missing", ""])
            raw = sheet[f"G{r}"].value
            n = Decimal(str(raw).rstrip("%"))
            if not str(raw).endswith("%") and abs(n) <= 1:
                n *= 100
            assert record["completion"] == int(n.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
            for field, col in (("start", "E"), ("finish", "F")):
                value = sheet[f"{col}{r}"].value
                kind = date_kind(value)
                date_counts[field][kind] += 1
                if kind != "calendar":
                    gaps.append([sheet.title, f"{col}{r}", field, kind, clean(value)])
            mapping.append({"team": sheet.title, "row": r, "index": record["index"],
                            "id": record["id"], "project": record["project"], "ragCell": f"D{r}",
                            "rag": record["rag"], "ragFill": record["ragFill"], "ragFont": record["ragFont"],
                            "startCell": f"E{r}", "start": record["start"], "deliveryCell": f"F{r}",
                            "delivery": record["finish"], "completionCell": f"G{r}",
                            "completion": record["completion"]})
        sheets.append({"team": sheet.title, "state": sheet.sheet_state, "dimensions": sheet.calculate_dimension(),
                       "headerRow": header, "recordRows": rows, "count": len(rows),
                       "rags": dict(Counter(actual[sheet.title, r]["rag"] for r in rows)),
                       "excludedNonemptyRows": excluded, "missingOptionalCells": missing, "formulas": errors})
    assert set(actual) == set(all_keys) and len(actual) == len(payload["records"])
    extensions = []
    with ZipFile(args.workbook) as archive:
        for name in archive.namelist():
            if name.startswith("xl/worksheets/sheet") and name.endswith(".xml"):
                xml = ET.fromstring(archive.read(name))
                for cf in xml.iter("{http://schemas.microsoft.com/office/spreadsheetml/2009/9/main}conditionalFormatting"):
                    extensions.append({"part": name, "ranges": [e.text for e in cf.iter() if e.tag.endswith("}sqref")],
                                       "types": [e.get("type") for e in cf.iter() if e.tag.endswith("}cfRule")]})
    after = hashlib.sha256(args.workbook.read_bytes()).hexdigest()
    copy_hash = hashlib.sha256((root / payload["sourceFile"]).read_bytes()).hexdigest()
    assert before == after == copy_hash == payload["sourceSha256"]
    result = {"sourceFile": args.workbook.name, "reportDate": payload["reportDate"],
              "sourceSha256Before": before, "sourceSha256After": after, "publicCopySha256": copy_hash,
              "records": len(actual), "rags": dict(Counter(r["rag"] for r in actual.values())),
              "sheets": sheets, "dates": date_counts, "sourceIssues": issues,
              "readerWarnings": sorted(set(str(w.message) for w in caught)),
              "extendedFormatting": extensions, "rowMapping": mapping, "status": "PASS"}
    (args.output / "workbook-audit.json").write_text(json.dumps(result, indent=2))
    with (root / "Source_Field_Gaps.csv").open("w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["Sheet", "Cell", "Field", "Classification", "Source value"])
        writer.writerows(gaps)
    print(json.dumps({k: result[k] for k in ("sourceFile", "reportDate", "records", "rags", "dates", "sourceSha256Before", "sourceSha256After", "status")}, indent=2))


if __name__ == "__main__":
    main()
