# 15 November 2026 — GitHub Pages local QA

Prepared locally; no remote Git, deployment or current live check. This report supersedes earlier local root results; historical live reports remain evidence for their stated older week.

- Source: original 140,112-byte Week of 15Nov2026 PST XLSX; ZIP CRC integrity PASS. Before/after/public/download SHA-256: `d6390cb656cede291c142822e01f88da43b817923332d602749487e00e1ee15f`.
- Independent worksheet/header/row audit: 195 records, 9 sheets, 105 Amber / 90 Green / no Red. Every valid row is reconciled; IoT N8 is the only missing optional field. No deduplication or optional-field exclusion.
- Effective RAG fills: 85 `C6E0B4`, 5 `E2F0D9`, 81 `FFF2CC`, 24 `FFE699`; exact labels and fills are checked against the independent browser XML reader and rendered CSS. No colors/legend strings in the UI.
- Local static production layout on port 4174: 45,621 browser assertions PASS. Fresh anonymous desktop 1440×1000 and mobile 390×844 contexts; all source records, drilldowns, full TEAM names, cascading TEAM/RAG matrix, reset, search, empty state, calculated whole percentages, exact delivery values, all/full/filtered/mobile/offline CSV, downloads, original filenames and workbook hash.
- Dashboard download opens offline and returns byte-identical workbook bytes. Local upload validates missing week, loading/disabled state, success, invalid ZIP failure and preserved source. No operational writes.
- Browser console/page errors: 0; failed requests: 0. Four existing RAG-expression tests PASS; Python syntax compilation and diff whitespace checks PASS. No lint/typecheck pipeline exists for this static application.
- Source reading warnings concern unsupported openpyxl extensions. Raw XML inspection confirms these extended rules are data bars outside RAG D cells. The workbook was never saved through openpyxl.
- Initial Python browser version mismatch was corrected by matching installed Playwright 1.64.0. The final suite passed. Mobile testing now uses a separate anonymous context and resolves its filter target at call time.
- Source issues remain source-owner questions, not frontend failures: Infrastructure C14/G14 closure mismatch, C31/J31 mixed recovery wording, current RAG/management divergences, WCS D8/M8, IoT N6 cached image error/no packaged image, chronology/provenance caveats. Prior Infrastructure D65, WCS percentage and IoT stale banner claims were rechecked and changed/resolved, not carried forward as current issues. See `SOURCE_ISSUES.json` for exact current cell values.

Evidence: `reports/15nov-2026/workbook-audit.json`, `source-issues.json`, `source-comparison.json`, `workbook-discovery.json`, and `browser/qa-results.json`, screenshots, CSVs, artifact hashes. Generated downloaded XLSX/HTML remain locally available and are ignored by Git because the canonical copies already ship with the application.

Post-publish command:

```sh
/home/user/workspace/it-leadership-dashboard/scripts/qa_15nov.sh 'https://esaonc-ai.github.io/it-leadership-dashboard/' /tmp/github-pages-15nov-live-qa
```

Preview: application `/home/user/workspace/it-leadership-dashboard`; `python -m http.server 3000 --bind 0.0.0.0 --directory /home/user/workspace/it-leadership-dashboard`, port 3000. Temporary verification servers are stopped before handoff.
