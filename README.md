# IT Program Leadership Dashboard

Public, anonymous, weekly-only dashboard at https://esaonc-ai.github.io/it-leadership-dashboard/. This is the existing static GitHub Pages app; no build or runtime dependencies are required. Its design and downloads are retained.

Current source: **IT_Project_Portfolios_2026_v1.0 (18Oct2026 PST)_2.xlsx**, reporting week **18 October 2026**. Selected by reporting version/date and the user's explicit latest-supplied revision order among equal-date attachments, not filesystem timestamps or suffix alone. Compared all three attached 18 October workbooks and all distinct source-workbook versions retained in repository history (21/28 September, 5/12 October). This revision renames Security to **IT Security** and updates seven status/completion/delivery cells; effective RAG styles and totals remain **133 records: 74 Amber, 56 Green, 3 Red** across eight teams. See `SOURCE_COMPARISON.json` for exact differences and hashes.

Use the single **Team** dropdown followed by the single **RAG** dropdown. Available RAG values cascade from Team; an unavailable previous RAG resets. Search, summary cards, reset, charts and detail views use the same selection. Percentages are whole numbers. Dates, TBD, N/A and relative estimates retain source meaning. Optional missing fields do not exclude records.

**Download source workbook** returns the original XLSX bytes. **Download IT Program Leadership Dashboard** saves a standalone HTML snapshot with the exact workbook embedded; it works offline, including filters, details and workbook download. There is no RAG-style legend or color-code text. Badges, chart segments and summary strips retain effective source-cell formatting, including conditional formatting.

Local workbook upload parses entirely in the browser. Choose a reporting week, upload a compatible XLSX, then download the dashboard to retain the snapshot. Loading, success, validation and failure states are visible; invalid input preserves the last validated snapshot. Local upload does not publish to GitHub.

## Refresh and QA

Requires Python 3 with `openpyxl`; browser QA additionally requires `playwright` and its Chromium browser. From the application directory:

```bash
python scripts/refresh_dashboard.py '/path/to/weekly.xlsx' --report-date YYYY-MM-DD
python scripts/audit_workbook.py '/path/to/weekly.xlsx' --output qa-local
python -m http.server 3000 --bind 0.0.0.0
```

In a second shell, run:

```bash
python scripts/qa_dashboard.py http://127.0.0.1:3000/ --workbook '/path/to/weekly.xlsx' --report-date YYYY-MM-DD --output qa-local
python scripts/qa_dashboard.py https://esaonc-ai.github.io/it-leadership-dashboard/ --workbook '/path/to/weekly.xlsx' --report-date YYYY-MM-DD --output qa-public
```

The audit reads every worksheet, checks row mapping and cached formula errors, and writes `Source_Field_Gaps.csv` plus a detailed JSON audit. Browser expectations independently read raw source XLSX XML and effective formatting, separately from Python generation. Evidence directories contain HTTP/page snapshots, screenshots, downloaded offline dashboards/workbooks, and QA results. They are excluded from publication. See `QA_REPORT.md`, `QA_LOCAL_RESULTS.json`, and `QA_PUBLIC_RESULTS.json` for this refresh's outcomes and remaining source issues.

No build/typecheck step applies to this plain HTML/JavaScript app. Use `python -m py_compile scripts/*.py` and `node --check` for JavaScript syntax, including extracted inline scripts. Stop temporary verification servers after QA. For a managed preview, run the static-server command above from the application directory on port **3000**. It accepts arbitrary Host headers.
