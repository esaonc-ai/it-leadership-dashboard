#!/usr/bin/env python3
"""Read-only comparison of the supplied revisions and previous repo snapshot.

Run before refresh; complete cell/format inventories are local QA artifacts.
No workbook is ever saved through openpyxl.
"""
import argparse
import hashlib
import json
import warnings
from collections import Counter
from copy import copy
from datetime import date, datetime
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

from openpyxl import load_workbook

from refresh_dashboard import build_records, source_style, text


def digest(data):
    return hashlib.sha256(data).hexdigest()


def xml(value):
    return ET.tostring(copy(value).to_tree(), encoding="unicode") if value is not None else None


def raw_value(value):
    return {"isoDateTime": value.isoformat()} if isinstance(value, (date, datetime)) else value


def inventory(path, output):
    original = path.read_bytes()
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        formulas = load_workbook(path, data_only=False)
        cached = load_workbook(path, data_only=True)
        records = build_records(path)
    cells, sheet_meta, effective = {}, {}, {}
    for sheet in formulas:
        for row in sheet:
            for cell in row:
                if cell.value is None and not cell.has_style:
                    continue
                key = sheet.title + "!" + cell.coordinate
                cells[key] = {
                    "value": text(cell.value), "type": cell.data_type,
                    "rawValue": raw_value(cell.value),
                    "cachedValue": text(cached[sheet.title][cell.coordinate].value),
                    "rawCachedValue": raw_value(cached[sheet.title][cell.coordinate].value),
                    "cachedType": cached[sheet.title][cell.coordinate].data_type,
                    "style": {name: xml(getattr(cell, name)) for name in
                              ("font", "fill", "border", "alignment", "protection")},
                    "numberFormat": cell.number_format,
                    "comment": cell.comment.text if cell.comment else None,
                    "hyperlink": cell.hyperlink.target if cell.hyperlink else None,
                }
        sheet_meta[sheet.title] = {
            "state": sheet.sheet_state, "dimensions": sheet.calculate_dimension(),
            "mergedRanges": str(sheet.merged_cells),
            "conditionalFormatting": [
                {"ranges": str(cf.sqref), "rules": [xml(r) for r in rules]}
                for cf, rules in sheet.conditional_formatting._cf_rules.items()
            ],
            "rowDimensions": {str(k): dict(v) for k, v in sheet.row_dimensions.items()},
            "columnDimensions": {str(k): dict(v) for k, v in sheet.column_dimensions.items()},
        }
        for record in records:
            if record["team"] == sheet.title:
                key = sheet.title + "!D" + str(record["sourceRow"])
                effective[key] = source_style(sheet["D" + str(record["sourceRow"])])
    with ZipFile(path) as archive:
        parts = {name: digest(archive.read(name)) for name in archive.namelist()}
        images = []
        for name in archive.namelist():
            if name.startswith("xl/media/"):
                target = output / "images" / name.removeprefix("xl/media/")
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(archive.read(name))
                images.append(str(target))
    assert digest(path.read_bytes()) == digest(original)
    full = {"cells": cells, "sheetMetadata": sheet_meta, "effectiveRag": effective,
            "records": records, "zipParts": parts}
    target = output / (path.stem + "-inventory.json")
    target.write_text(json.dumps(full, indent=2))
    summary = {
        "path": str(path), "bytes": len(original), "sha256Before": digest(original),
        "sha256AfterComparison": digest(path.read_bytes()),
        "allCellsRead": len(cells), "sheets": list(sheet_meta),
        "records": len(records), "rags": dict(Counter(r["rag"] for r in records)),
        "teamRags": {s: dict(Counter(r["rag"] for r in records if r["team"] == s)) for s in sheet_meta},
        "imageParts": images,
        "imageFormulaReferences": {k: v["value"] for k, v in cells.items() if "DISPIMG(" in v["value"]},
        "readerWarnings": sorted(set(str(w.message) for w in caught)),
        "fullInventory": str(target),
    }
    return summary, full


def compare(a, b):
    def differences(left, right):
        return sorted(k for k in left.keys() | right.keys() if left.get(k) != right.get(k))
    values = lambda x: {k: (v["rawValue"], v["type"]) for k, v in x["cells"].items() if v["rawValue"] is not None}
    formulas = lambda x: {k: (v["rawValue"], v["rawCachedValue"], v["cachedType"])
                          for k, v in x["cells"].items() if v["type"] == "f"}
    formats = lambda x: {k: (v["style"], v["numberFormat"]) for k, v in x["cells"].items()}
    return {
        "differentZipParts": differences(a["zipParts"], b["zipParts"]),
        "differentValuesAndTypes": differences(values(a), values(b)),
        "differentFormulasAndCaches": differences(formulas(a), formulas(b)),
        "differentCellFormatting": differences(formats(a), formats(b)),
        "differentSheetMetadataAndConditionalFormatting": differences(a["sheetMetadata"], b["sheetMetadata"]),
        "differentEffectiveRagCells": differences(a["effectiveRag"], b["effectiveRag"]),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("first", type=Path)
    parser.add_argument("latest", type=Path)
    parser.add_argument("previous", type=Path)
    parser.add_argument("--report-date", required=True)
    parser.add_argument("--previous-report-date", required=True)
    parser.add_argument("--previous-source-name")
    parser.add_argument("--output", type=Path, default=Path("qa-local/26oct"))
    args = parser.parse_args()
    assert date.fromisoformat(args.report_date) >= date.fromisoformat(args.previous_report_date)
    args.output.mkdir(parents=True, exist_ok=True)
    candidates = [inventory(p.resolve(), args.output) for p in (args.first, args.latest, args.previous)]
    result = {
        "selection": str(args.latest.resolve()), "reportDate": args.report_date,
        "previousReportDate": args.previous_report_date,
        "reason": f"Newest reporting date found in workspace/repo ({args.report_date} versus previous {args.previous_report_date}); latest explicitly supplied equal-date revision selected after comparison.",
        "candidates": [s for s, _ in candidates],
        "sameDateByteEqual": args.first.read_bytes() == args.latest.read_bytes(),
        "sameDateComparison": compare(candidates[0][1], candidates[1][1]),
        "previousSnapshotComparison": compare(candidates[2][1], candidates[1][1]),
        "previousSourceName": args.previous_source_name or args.previous.name,
    }
    Path("SOURCE_COMPARISON.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"selected": result["selection"], "sameDateByteEqual": result["sameDateByteEqual"],
                      "sameDateComparison": result["sameDateComparison"],
                      "previousDifferenceCounts": {k: len(v) for k, v in result["previousSnapshotComparison"].items()},
                      "candidates": [{k: s[k] for k in ("path", "bytes", "sha256Before", "records", "rags")} for s, _ in candidates]}, indent=2))


if __name__ == "__main__":
    main()
