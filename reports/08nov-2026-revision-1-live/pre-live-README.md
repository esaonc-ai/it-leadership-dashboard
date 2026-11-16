# IT & Technology Program Leadership Dashboard

Existing static application, `esaonc-ai/it-leadership-dashboard`, main/root GitHub Pages: https://esaonc-ai.github.io/it-leadership-dashboard/.

**Local revision refreshed and verified; publication pending.** Latest supplied same-week workbook `IT & Technology Project_Portfolios_2026_v1.0 (Week of 08Nov2026 PST)_1.xlsx` contains **179 valid records, 85 Amber / 94 Green / 0 Red**. Its three changes from original 08Nov are `WCS Engineering!D7/D8/D11`: Amber → Green, with effective styles updated faithfully. Corresponding notes still direct Amber; the source-owner report documents this rather than correcting the workbook.

Original source remains untouched, SHA-256 `bf5fdec3238aff668760b3b0a110bf0aac52eab822b79d41399a59e50f3d2550`. All actual desktop/mobile/offline/source-snapshot workbook downloads match its bytes. Existing branding/CSS, weekly-only scope, exact worksheet labels, all valid rows, whole numeric and source-text completion, conditional delivery estimates, exactly one TEAM and one cascading RAG dropdown, CSV and offline dashboard operation remain. No features or dependencies changed.

**47,867 local browser assertions PASS** (42,227 full suite + 5,640 independent fresh-mobile/offline), all TEAM/RAG combinations/cascades, all 179 details, source colors/dates/text, anonymous downloads, zero console/page/request failures. Four targeted tests and all applicable syntax/idempotence/Host checks pass. Static repository has no framework build/lint/typecheck configuration.

[Current QA and source-owner report](QA_REPORT.md), [local results](QA_LOCAL_RESULTS.json), [revision comparison](SOURCE_COMPARISON.json), [exact source findings](SOURCE_ISSUES.json), [revision evidence](reports/08nov-2026-revision-1/). Remaining issues include the three new WCS RAG/directive conflicts, Infrastructure D65 Green vs Red/offline wording, Compliance/WCS percentage conflicts, IoT stale August banner and image formula error. Several prior unsupported closure statements remain clarified, while original 08Nov's WCS D7 resolution is reversed by `_1`.

Latest known published/live-verified snapshot is still the **original 08Nov upload: 179 / 88 Amber / 91 Green**, application commit `1a1183e`, evidence commit `f72f9f1`. Fresh read-only baseline GETs in this rerun matched it. [Historical live report](LIVE_QA_REPORT.md) applies only to that original upload; [current public status](QA_PUBLIC_RESULTS.json) marks `_1` not live-tested. No remote Git operation occurred; coordinator must push then request live QA.

All prior root reports are archived byte-for-byte at [original published baseline](reports/08nov-2026-original-published-baseline/); prior local/live evidence remains preserved. The standalone delivery copy is `/home/user/workspace/Portfolio_Dashboard_QA_and_Source_Issues_08Nov2026_Revision_1.md`.

Application directory `/home/user/workspace/it-leadership-dashboard`. Temporary verification server stopped and awaited, port 3000 closed. No additional preview is needed; caller-managed reproduction only:

```bash
python -m http.server 3000 --bind 0.0.0.0 --directory /home/user/workspace/it-leadership-dashboard
```
