# IT & Technology Program Leadership Dashboard

Existing anonymous, weekly-only dashboard: https://esaonc-ai.github.io/it-leadership-dashboard/ in `esaonc-ai/it-leadership-dashboard`. This static HTML/JavaScript app has no framework build or runtime dependencies. Existing branding, design, repo and Pages URL are retained.

Current local source: **IT & Technology Project_Portfolios_2026_v1.0 (26Oct2026 PST)_4.xlsx**, week of **26 October 2026**. All five supplied same-date revisions were compared by bytes, every cell value/type, formulas/caches, resolved cell formatting, priority-ordered conditional rules and effective RAG appearance. **`_4`, `_3` and `_2` are byte-identical** (76,509 bytes). The first upload and `_1` are 76,511 bytes with different saved metadata/style-reference serialization but identical business data and effective formatting. The latest supplied exact bytes and filename are selected. The historical published snapshot is 18 October; the starting unpushed local commit `bfbc8d5` selected `_2`. The current workbook contains **91 records: 49 Amber, 38 Green, 4 Red**, across eight source sheets. No prior-week records are merged into this snapshot.

Use the single **Team** and single **RAG** dropdowns. RAG options cascade from Team, and an unavailable prior selection resets. Search, cards, charts, rows and details share those filters. All records with an identifier and project are retained, including missing optional notes. Numeric percentages are whole numbers; source completion text such as `TBD` stays text and is excluded from numeric averages. Dates, qualified targets, `TBD`, `N/A` and relative estimates preserve the source meaning. RAG appearance follows effective cell formatting, including conditional rules and source font variants. No RAG style legend or raw color labels appear in the UI.

**Download source workbook** returns the exact original XLSX bytes under the original supplied filename. The stable direct path is `Weekly_Leadership_Source_Workbook.xlsx`. **Download IT & Technology Program Leadership Dashboard** returns a standalone HTML snapshot with its source workbook embedded; filtering, details and workbook downloads work offline. Local workbook uploads stay in the browser, validate inputs, show progress/errors and preserve the last valid snapshot on failure. They do not publish anything.

Compared with 18 October, the current source has material sheet/content changes and conflicting source statements; `_4` retains the same data as all earlier 26 October uploads. In particular, Infrastructure & Cloud now contains robotics/WCS workstreams, and the eHub-named sheet contains compliance records. These are preserved as supplied. Permission to change the workbook was acknowledged, but no factual corrections were specified; the dashboard does not guess corrections. See **QA_REPORT.md** for exact cell anchors, prior-issue rechecks, source integrity and verification evidence. No embedded image asset exists; IoT N6 is an unresolved image formula with a cached error.

## Local preview and verification

Application directory: `/home/user/workspace/it-leadership-dashboard`. Start a managed static preview on **port 3000**, accepting arbitrary Host headers:

```bash
python -m http.server 3000 --bind 0.0.0.0 --directory /home/user/workspace/it-leadership-dashboard
```

The temporary QA server was stopped after verification. For repeatable audit/browser QA, from the application directory (Python `openpyxl`, `playwright`, and Playwright Chromium are required):

```bash
python scripts/audit_workbook.py '/path/to/weekly.xlsx' --output qa-local/26oct-revision4
python scripts/qa_dashboard.py http://127.0.0.1:3000/ --workbook '/path/to/weekly.xlsx' --report-date 2026-10-26 --audit qa-local/26oct-revision4/workbook-audit.json --output qa-local/26oct-revision4
python -m py_compile scripts/*.py
node --check scripts/workbook_reader.js
```

Inline JavaScript is also extracted and checked with `node --check`. No framework lint/build/typecheck command applies. Browser expectations read raw source XLSX XML separately from Python generation. The full Team/RAG matrix, cascading rows/KPIs, every source field/detail, source colors, missing notes, nonnumeric completion, desktop/mobile, errors, both downloads and offline operation are checked. **18,238 browser assertions pass**, with no page/console errors or failed requests. Tracked results: `QA_LOCAL_RESULTS.json`. Full inventories, screenshots, original/downloaded artifacts and HTTP evidence are in ignored `qa-local/26oct-revision4/`.

For later refreshes, preserve the previous workbook before updating. Compare supplied revisions with `scripts/compare_workbooks.py FIRST LATEST PREVIOUS --report-date YYYY-MM-DD --previous-report-date YYYY-MM-DD`, then run `python scripts/refresh_dashboard.py LATEST --report-date YYYY-MM-DD`. The comparison writes `SOURCE_COMPARISON.json`, full local cell/style inventories, and any image assets to the local evidence directory. The generator copies and embeds source bytes without re-saving the workbook.

## Existing publishing mechanism

GitHub Pages uses **`main`, repository root `/`**, through the GitHub-generated **`pages-build-deployment`** workflow (`dynamic/pages/pages-build-deployment`, workflow ID `357658072`): Jekyll build → upload Pages artifact → deploy to GitHub Pages. There is no checked-in custom workflow or alternate app/provider. Historical read-only receipts confirm the prior successful run on `main` and its public HTML matching the original published commit’s root `index.html`. No live check was repeated for `_4`. The historical anonymous Pages settings request returned 404, so branch/path settings must be re-resolved by the coordinator with its authenticated resolver before publishing.

This refresh is **local only**. The earlier local revision could not be published because ibisGitTool repository-write authorization was denied twice, including after secure confirmation; no auth or push was retried here. The coordinator owns ibisGitTool remote reconciliation/push and the existing Pages publication flow. No remote Git operation, push, workflow dispatch or deployment was performed. `QA_PUBLIC_RESULTS.json` explicitly marks the current refresh untested publicly and retains the historical 18 October results separately.
