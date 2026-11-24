# IT & Technology Program Leadership Dashboard

Prepared locally for **Week of 15 November 2026 PST**. Existing repository `esaonc-ai/it-leadership-dashboard`, branch `main`, existing root GitHub Pages layout: https://esaonc-ai.github.io/it-leadership-dashboard/.

The default `index.html` and public `Weekly_Leadership_Source_Workbook.xlsx` contain the newest available source: **195 records, 9 exact worksheet teams, 105 Amber / 90 Green / 0 Red**. The supplied workbook is unchanged; embedded/public/downloaded bytes have SHA-256 `d6390cb656cede291c142822e01f88da43b817923332d602749487e00e1ee15f` (140,112 bytes).

The existing frontend, branding, weekly-only reporting, exactly one TEAM and one cascading RAG dropdown, search, upload, drilldowns, CSV and standalone/source downloads remain. All source rows, optional missing notes, effective conditional RAG fills, exact statuses, whole-number completion and delivery date/text values are retained. A ninth team, `Samba-Sharepoint Migration`, appears in full on desktop/mobile.

[Local QA and limitations](QA_REPORT.md), [results](QA_LOCAL_RESULTS.json), [cell-level findings](SOURCE_ISSUES.json), [prior-baseline comparison](SOURCE_COMPARISON.json), [new evidence](reports/15nov-2026/). Existing `LIVE_QA_REPORT.md` and `QA_PUBLIC_RESULTS.json` describe historical 08 November live verification only. The 15 November update has **not** been published or checked live. No remote Git or deployment occurred.

Application directory: `/home/user/workspace/it-leadership-dashboard`. Static preview, port **3000**:

```sh
python -m http.server 3000 --bind 0.0.0.0 --directory /home/user/workspace/it-leadership-dashboard
```

Build and read-only source audit:

```sh
python scripts/refresh_dashboard.py '/home/user/workspace/IT & Technology Project_Portfolios_2026_v1.0 (Week of 15Nov2026 PST).xlsx' --report-date 2026-11-15
python scripts/audit_workbook.py '/home/user/workspace/IT & Technology Project_Portfolios_2026_v1.0 (Week of 15Nov2026 PST).xlsx' --output reports/15nov-2026
python -m unittest discover -s scripts -p 'test_*.py'
```

Browser QA requires Python Playwright plus its Chromium browser. For this environment Python `playwright==1.64.0` matches the installed Chromium. After publishing, rerun the same checks anonymously (read-only HTTP; upload tests remain browser-local):

```sh
/home/user/workspace/it-leadership-dashboard/scripts/qa_15nov.sh 'https://esaonc-ai.github.io/it-leadership-dashboard/' /tmp/github-pages-15nov-live-qa
```

The wrapper also accepts a local URL. It uses the repository byte copy and original download name, so it needs no external upload path. QA does not start a server; stop/wait for any local server used for verification when finished.
