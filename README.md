# IT & Technology Program Leadership Dashboard

Existing app/repo `esaonc-ai/it-leadership-dashboard`, main, https://esaonc-ai.github.io/it-leadership-dashboard/. Same public branding/layout and GitHub Pages main/root, no alternate app or host.

Latest attachment **IT & Technology Project_Portfolios_2026_v1.0 (Week of 25Oct2026 PST).xlsx** is **byte-identical** to both 30Oct uploads, SHA-256 **`91513727651ec6c4fcad0ff8b107d56ea89aae02e420229f48dc26050e710ada`**. Per explicit user instruction for identical uploads, corrected dashboard reporting week to **25 October 2026** and source/download filename accordingly. **154 records: 77 Amber / 73 Green / 4 Red** unchanged. Only sourceFile/reportDate metadata changes; source bytes, app code, records, dates/styles and all 10 originals unchanged. This is not a historical rollback.

**Internal chronology caveat:** unchanged source has 30Oct task/closure evidence (Infrastructure I22/eHub I3), as of 01Nov Infrastructure I4 and 02Nov WCS I8, plus stale 23Aug IoT A2 banner. The 25Oct label is supplied correction only; internal source dates are preserved and not asserted to be as of 25Oct. Full exact anchors/current business source concerns: [QA_REPORT.md](QA_REPORT.md). No facts guessed or corrected.

Weekly-only, all valid rows/duplicate IDs/optional blanks, whole percentages/TBD, source-faithful delivery dates, effective conditional RAG colors, exactly one TEAM and one RAG cascading dropdown, full worksheet names desktop/mobile, no style legend/raw color strings and exact XLSX/offline HTML downloads preserved.

**32,065 local Playwright assertions PASS**, full source row/field/KPI/color/date reconciliation, all 36 filter states / 24 cascades, desktop/mobile, new reporting label/filename, real downloads/hash/offline/console checks. Zero console/request failures; syntax passes; no framework build/typecheck applies or dependencies changed. [QA_LOCAL_RESULTS.json](QA_LOCAL_RESULTS.json), full ignored evidence qa-local/25oct-attachment-audit/.

**25Oct label correction is local/unpublished.** No fresh live check claimed. Last live PASS: commit `7d121d0b89dc5df99f6e06522f0f9168b94bc82a`, 30Oct / 154 records and previous filename. Report-only dirty evidence from that live QA preserved byte-for-byte under reports/30oct-2026-filename-published/ with hashes; root LIVE_QA_REPORT.md remains historical evidence. QA_PUBLIC_RESULTS.json separates prior live PASS from current local QA. Coordinator owns resolver/push/post-publication verification. No remote Git/auth/push/deploy in this run.

Application directory `/home/user/workspace/it-leadership-dashboard`; optional managed preview, port **3000**:

```bash
python -m http.server 3000 --bind 0.0.0.0 --directory /home/user/workspace/it-leadership-dashboard
```

Temporary QA server stopped and awaited. Existing tooling from application directory:

```bash
python scripts/audit_workbook.py '/path/to/weekly.xlsx' --output qa-local/25oct-attachment-audit
python scripts/qa_dashboard.py http://127.0.0.1:3000/ --workbook '/path/to/weekly.xlsx' --report-date 2026-10-25 --audit qa-local/25oct-attachment-audit/workbook-audit.json --output qa-local/25oct-attachment-audit
python -m py_compile scripts/*.py
node --check scripts/workbook_reader.js
```
