# IT & Technology Program Leadership Dashboard

Existing anonymous weekly dashboard: https://esaonc-ai.github.io/it-leadership-dashboard/ in `esaonc-ai/it-leadership-dashboard`, branch `main`. Existing branding, repo, design and Pages URL are retained. Static HTML/JavaScript; no framework/runtime dependencies.

Current local source: **IT & Technology Project_Portfolios_2026_v1.0 (26Oct2026 PST)_6.xlsx**, reporting week **26 October 2026**. All seven same-date uploads were compared by bytes, raw values/types, formulas/caches, direct styles, conditional rules and effective RAG appearance. `_6` is materially different: **144 records: 79 Amber, 55 Green, 10 Red**, versus the prior local 91. Infrastructure now has 70 infrastructure records and eHub 9 shipping records; WCS rows 2/5 now report Green/100%. Uploaded originals remain unchanged. Detailed comparison, counts, current source issues and evidence: [QA_REPORT.md](QA_REPORT.md), `SOURCE_COMPARISON.json`.

The single **Team** and single **RAG** dropdowns cascade available RAG options and reset unavailable selections. All valid source rows remain, including optional blank notes and repeated Infrastructure identifiers; no business facts are guessed or deduplicated. Filters, search, KPIs, charts, table and details share the snapshot. Numeric percentages render as whole numbers. Source completion text, dates, qualified TBD, N/A and relative estimates retain their meaning. Effective direct/conditional RAG fill/font styles are preserved without a visible style legend or raw color labels. Weekly-only: no prior-week rows are merged.

**Download source workbook** returns exact original bytes under the `_6.xlsx` filename; stable path `Weekly_Leadership_Source_Workbook.xlsx`. SHA-256: `077f4dbf228a5f33be2940d519b17ad83f60a3cd4529da555e0ed9c43e64a4dc`. **Download IT & Technology Program Leadership Dashboard** returns self-contained HTML with embedded workbook, working offline for filtering, details and original-workbook download. Local uploads stay in-browser, validate reporting week/workbook, show loading/disabled controls and visible success/errors, and retain the last valid snapshot after errors.

All eight sheets and every source cell/style were inspected. No embedded image asset exists; IoT N6 remains an image formula cached as #NAME?. Rechecked source conflicts, repeated IDs, missing notes and historical issues are anchored in the report. No uploaded original or ambiguous business fact was corrected.

## Local verification and preview

**25,934 Playwright assertions pass**, including independent source reconciliation, all 36 TEAM/RAG states, cascading transitions/reset, every detail field, source colors/dates/whole completions, desktop/mobile, downloads and offline operation. No browser errors or failed requests. Python and JS syntax checks pass; no package.json/framework build/lint/typecheck applies. No dependencies upgraded. Tracked evidence: `QA_LOCAL_RESULTS.json`; full ignored evidence: `qa-local/26oct-revision6/`.

Application directory: `/home/user/workspace/it-leadership-dashboard`. Optional managed preview, port **3000**, accepting arbitrary Host headers:

```bash
python -m http.server 3000 --bind 0.0.0.0 --directory /home/user/workspace/it-leadership-dashboard
```

The temporary QA server was stopped and awaited. Repeat audit/browser QA from the app directory with existing Python openpyxl/Playwright and Chromium:

```bash
python scripts/audit_workbook.py '/path/to/weekly.xlsx' --output qa-local/26oct-revision6
python scripts/qa_dashboard.py http://127.0.0.1:3000/ --workbook '/path/to/weekly.xlsx' --report-date 2026-10-26 --audit qa-local/26oct-revision6/workbook-audit.json --output qa-local/26oct-revision6
python -m py_compile scripts/*.py
node --check scripts/workbook_reader.js
```

Final inline JavaScript was also extracted and checked with `node --check`. Refresh using `python scripts/refresh_dashboard.py LATEST --report-date YYYY-MM-DD` after read-only source comparison. The generator copies/embeds original bytes without saving through an Excel library.

## Publication state

Prepared snapshot **26 October / 144 records** remains local and unpublished. A fresh anonymous read-only live check still shows **18 October / 133 records (74 Amber, 56 Green, 3 Red)**. `QA_PUBLIC_RESULTS.json` separates that current baseline from prepared-refresh QA and historical deployed QA. No live result is claimed for the unpublished refresh.

Existing publishing mechanism: **GitHub Pages, main, root /**, GitHub-generated **pages-build-deployment** workflow (`dynamic/pages/pages-build-deployment`, ID `357658072`), Jekyll build → upload artifact → deploy. Historical read-only receipts established root/main; coordinator resolver must confirm settings before publication. No new app/provider or URL change.

Prior ibisGitTool write-authorization denials remain with the coordinator. This run made no remote Git, auth, push, workflow-dispatch or deployment attempt. The coordinator owns native ibisGitTool authorization, resolver/push and post-publication verification.
