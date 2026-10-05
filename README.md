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

Current reporting week: 5 October 2026. Source: latest attached 05Oct2026 workbook (newer than the prior 28 September deployment). IoT rows 2–6 retain the existing shifted source layout; completion is in F and owner in J. IoT M4 contains an Excel image formula with cached #NAME?; the dashboard refers users to the preserved workbook image.
