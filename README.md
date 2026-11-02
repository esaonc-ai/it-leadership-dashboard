# IT & Technology Program Leadership Dashboard

Existing anonymous weekly dashboard: https://esaonc-ai.github.io/it-leadership-dashboard/, repo `esaonc-ai/it-leadership-dashboard`, branch `main`. Public branding, existing design, repo and Pages URL remain unchanged. Static HTML/JavaScript; no framework/runtime dependencies.

Current prepared source: **IT & Technology Project_Portfolios_2026_v1.0 (30Oct2026 PST).xlsx**, reporting week **30 October 2026**. Newest available workbook; one upload exists for that date. Full values/formulas/caches/styles/conditional-rule comparison against prior 26 October _6 found substantive changes. **154 records: 77 Amber, 73 Green, 4 Red**, up from 144; Infrastructure now has 77 records, WCS 11 and eHub 10. All eight uploaded originals remain unchanged. [QA_REPORT.md](QA_REPORT.md) contains comparison totals, exact current source-issue anchors and QA evidence; `SOURCE_COMPARISON.json` contains machine details.

Exactly one **Team** and one **RAG** dropdown cascade available options and reset unavailable selections. Source worksheet names remain exact and fully readable in dropdowns, chart labels and table rows on desktop/mobile. All valid source rows remain, including duplicate identifiers and optional blank notes. No business corrections or deduplication are guessed. All filters, search, KPIs, charts, rows and details share the weekly snapshot. Numeric completion and KPI percentages display as whole numbers; source completion text, dates, TBD/N/A/relative delivery estimates remain faithful. Effective direct/conditional RAG fonts/fills are preserved without a visible style legend or raw color strings.

**Download source workbook** returns original bytes under the exact 30Oct filename; stable path `Weekly_Leadership_Source_Workbook.xlsx`. SHA-256: `91513727651ec6c4fcad0ff8b107d56ea89aae02e420229f48dc26050e710ada`. **Download IT & Technology Program Leadership Dashboard** returns self-contained HTML with exact embedded source, working offline for filters, details and workbook download. Local browser uploads validate week/workbook, show loading/disabled controls and success/errors, and preserve the last valid snapshot on error; they do not publish.

All sheets/cells/styles were inspected. IoT N6 remains an image formula cached #NAME?, with no embedded asset. Current source RAG/narrative conflicts, repeated IDs, completion conflicts, optional blanks and mixed chronology are documented neutrally. Prior issues were rechecked; resolved findings are not carried forward as current warnings.

## Local verification

**32,065 Playwright assertions passed**, independent source row/field/color/date reconciliation, all 36 Team/RAG states, cascade/reset/options, exact full worksheet-name readability, desktop/mobile, both downloads and offline operation. Zero browser errors or failed requests. All Python/JS syntax checks pass; no package.json/framework build/lint/typecheck applies. Existing tooling reused without upgrades. Tracked evidence: `QA_LOCAL_RESULTS.json`; full ignored evidence: `qa-local/30oct/`.

Application directory `/home/user/workspace/it-leadership-dashboard`. Optional managed preview, port **3000**, arbitrary Host headers accepted:

```bash
python -m http.server 3000 --bind 0.0.0.0 --directory /home/user/workspace/it-leadership-dashboard
```

Temporary QA server stopped and awaited. From the app directory, using existing openpyxl/Playwright/Chromium:

```bash
python scripts/audit_workbook.py '/path/to/weekly.xlsx' --output qa-local/30oct
python scripts/qa_dashboard.py http://127.0.0.1:3000/ --workbook '/path/to/weekly.xlsx' --report-date 2026-10-30 --audit qa-local/30oct/workbook-audit.json --output qa-local/30oct
python -m py_compile scripts/*.py
node --check scripts/workbook_reader.js
```

Inline JS was extracted and checked separately. After comparison, refresh with `python scripts/refresh_dashboard.py LATEST --report-date YYYY-MM-DD`; original bytes are copied/embedded, never re-saved through Excel libraries.

## Publication state

The **30 October / 154-record refresh is local and unpublished**. Last live-verified baseline: **26 October / 144 records**, commit `9250e6b50dfa7137a4c4f74e49d106eec9282330`, workflow 40466318754. The four report files left uncommitted after that successful live QA are preserved byte-for-byte under [reports/26oct-2026](reports/26oct-2026/LIVE_QA_REPORT.md), with a hash manifest. Historical root `LIVE_QA_REPORT.md` is also retained. `QA_PUBLIC_RESULTS.json` explicitly records NOT_RUN_FOR_THIS_REFRESH and links the historical deployed PASS.

Existing mechanism: **GitHub Pages, main, root /**, generated **pages-build-deployment** workflow (`dynamic/pages/pages-build-deployment`, ID `357658072`), Jekyll build → artifact → deploy. No alternate site/host/provider. No remote Git/auth/push/deployment occurred during this refresh. The coordinator owns resolver confirmation, native ibisGitTool push and post-publication verification.
