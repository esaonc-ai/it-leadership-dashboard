# IT & Technology Program Leadership Dashboard

Existing app/repo: `esaonc-ai/it-leadership-dashboard`, `main`, https://esaonc-ai.github.io/it-leadership-dashboard/. Exact branding and existing design retained; static HTML/JavaScript, no framework dependencies.

Latest source **IT & Technology Project_Portfolios_2026_v1.0 (Week of 30Oct2026 PST).xlsx**, reporting week **30 October 2026**. Complete comparison proves it is **byte-identical** to the previously published `(30Oct2026 PST).xlsx`: **154 records — 77 Amber / 73 Green / 4 Red**, same sheets/cells/caches/styles/conditional formatting. Only embedded **sourceFile** metadata changes so visible source label and actual workbook download use the latest supplied filename. Exact source bytes remain SHA-256 **`91513727651ec6c4fcad0ff8b107d56ea89aae02e420229f48dc26050e710ada`**; all nine originals unchanged.

Weekly-only reporting preserves every valid source row, duplicate identifiers, optional blanks, whole percentages, source text/date estimates and effective RAG styles. Precisely one TEAM and one RAG dropdown cascade/reset applicable options. Full worksheet names remain readable desktop/mobile; no style legend/raw color strings. Exact original workbook and self-contained offline dashboard downloads retained. No business facts corrected. Current anchored source findings and comparison: [QA_REPORT.md](QA_REPORT.md), `SOURCE_COMPARISON.json`.

**32,065 local Playwright assertions PASS**, all source rows/fields/KPIs/colors/dates, all 36 filter states / 24 cascade transitions, desktop/mobile names, downloads/hash/offline and feedback/error states. Zero console/request errors. Python/JS syntax passes; no framework build/typecheck applicable or dependency upgrade. [QA_LOCAL_RESULTS.json](QA_LOCAL_RESULTS.json), full ignored evidence `qa-local/30oct-latest-revision/`.

Latest filename update remains **local and unpublished**. Previous successful **30Oct / 154** live evidence for commit `7658d77a11f348eaa9816fa4a94957069129a0f2` and old source filename is preserved byte-for-byte in [reports/30oct-2026-published/LIVE_QA_REPORT.md](reports/30oct-2026-published/LIVE_QA_REPORT.md); root LIVE_QA_REPORT.md remains unchanged. `QA_PUBLIC_RESULTS.json` distinguishes last live PASS from current local QA. No fresh live check is claimed. Existing GitHub Pages **main / root /** mechanism unchanged; coordinator owns resolver, ibisGitTool push and post-publication QA. No remote Git/auth/push/deploy in this run.

Application directory `/home/user/workspace/it-leadership-dashboard`; managed preview command, port **3000**:

```bash
python -m http.server 3000 --bind 0.0.0.0 --directory /home/user/workspace/it-leadership-dashboard
```

Temporary QA server stopped and awaited. Re-run with existing tooling from app directory:

```bash
python scripts/audit_workbook.py '/path/to/weekly.xlsx' --output qa-local/30oct-latest-revision
python scripts/qa_dashboard.py http://127.0.0.1:3000/ --workbook '/path/to/weekly.xlsx' --report-date 2026-10-30 --audit qa-local/30oct-latest-revision/workbook-audit.json --output qa-local/30oct-latest-revision
python -m py_compile scripts/*.py
node --check scripts/workbook_reader.js
```
