# IT Program Leadership Dashboard

Public, no-login, weekly-only leadership dashboard. The site is fully static and can be opened directly from `index.html` or served by GitHub Pages.

## Public usage

- Use the Team filter first; the RAG filter then lists only values represented for that team.
- Counts, whole-number percentages, team health bars, and the record table update immediately.
- Use **Download source workbook** for the public `Weekly_Leadership_Source_Workbook.xlsx` copy.
- Use **Download IT Program Leadership Dashboard** for a standalone HTML snapshot. The exact source workbook bytes are embedded; both downloads work offline.

## Weekly refresh

Requires Python 3 and `openpyxl`. From this directory, run:

```bash
python3 scripts/refresh_dashboard.py /path/to/current-week.xlsx --report-date YYYY-MM-DD
```

The refresh includes every compatible-sheet workbook row with an identifier and Project / Workstream value, supports the standard schema and shifted schemas where RAG may be embedded in Status or an explicit RAG is present while Start Date is omitted, converts decimal or whole completion values to whole-number percentages, copies the workbook under the neutral public filename, and retains effective source-cell RAG fill/font colors, including matching conditional formatting. Records without a supported source RAG remain neutral.

Before publishing, verify record and Team/RAG totals against the workbook, check browser console output, test the cascading filters, and trigger both public downloads. No build step, server, authentication, or external service is required.

Current reporting week: **12 October 2026**. Refreshed from the newest attached weekly workbook. 128 records: 78 Amber, 48 Green, 2 Red across 8 teams. Both explicit-RAG schemas and title/header rows are discovered; completion text (including TBD) is preserved and excluded from numeric averages.

IoT now has its headers on row 3 and five records in rows 4–8. Columns are normalized in the attachment (completion G, owner K); no source edits were made by the dashboard. Start/delivery E4:F8 remain TBD. The former image error is now at N6 (cached #NAME?); N8 notes remain blank. A2 still carries a 23 August reporting date. See `QA_REPORT.md` for reconciliation and remaining source-field gaps.

Local upload of a compatible future-week XLSX is supported. Choose the reporting week then upload. Parsing and validation occur entirely in the browser; the exact original bytes replace the download payload only after validation. Download the refreshed standalone HTML to retain the snapshot. This does not publish local uploads to GitHub. Unsupported RAG formatting blocks upload rather than recoloring records.

Exactly one shared Team dropdown and one shared RAG dropdown control the dashboard; RAG options cascade from Team. Duplicate per-card dropdowns have been removed. Charts and cards retain all effective fill variants. No separate RAG-style legend or source-color-code labels are shown.

QA (requires Python Playwright/Chromium):

```bash
python3 scripts/qa_dashboard.py https://esaonc-ai.github.io/it-leadership-dashboard/ --output qa-public
```

The source workbook is never re-saved through an Excel library; its byte hash is checked against both online and offline downloads.
