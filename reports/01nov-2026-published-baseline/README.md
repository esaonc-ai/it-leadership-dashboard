# IT & Technology Program Leadership Dashboard

Existing static application for `esaonc-ai/it-leadership-dashboard`, GitHub Pages repository root: https://esaonc-ai.github.io/it-leadership-dashboard/.

Current **published and live-verified** snapshot uses **IT & Technology Project_Portfolios_2026_v1.0 (Week of 01Nov2026 PST).xlsx**: **164 records, 89 Amber / 75 Green / 0 Red**, eight worksheets. Original workbook unchanged; SHA-256 `04d0a8be91c203387eb6d27bf2543eab822772f07407e9769254d68b06620467`. Only one 01Nov upload was available; byte/semantic comparison proves a substantive update from the verified 25Oct checkout/public baseline. After coordinator push, the actual public HTML and source download were verified against application commit `832566659d7670543e2a851d588c3d82de49a436` on 09-Nov-2026.

Existing branding/design, weekly-only view, exact worksheet/status names, every valid source row, effective conditional RAG colors, whole completion percentages and faithful estimated-delivery dates remain. Exactly one TEAM and one cascading RAG dropdown. Workbook and standalone offline dashboard downloads preserve source bytes. Filtered CSV now exports the visible snapshot with source row identity, whole completion percentages and unchanged dates/narratives.

**38,172 local Playwright assertions PASS**, desktop/mobile/offline, all 36 filter matrix entries (including unavailable values), 16 available cascade transitions, every source row/detail, colors/dates, anonymous access, CSV and byte-identical workbook downloads. Zero console/request errors. Python/JS syntax checks and refresh idempotence pass; no framework build applies or app dependencies changed.

[Live QA/source-owner report](LIVE_QA_REPORT.md), [live results](QA_PUBLIC_RESULTS.json), [live evidence](reports/01nov-2026-live/). **38,172 live Playwright assertions PASS** at the exact public URL, fresh anonymous desktop/mobile contexts, all filtering/cascades, source colors/dates, CSV/dashboard/workbook downloads and offline downloaded HTML; zero page/console/request failures. Every workbook download matches the unchanged original. The first request showed the prior deployment; subsequent exact-URL requests and full browser QA verified the new snapshot. No app/test code changed in the live verification run.

[Preserved local QA report](QA_REPORT.md), [local results](QA_LOCAL_RESULTS.json), [revision comparison](SOURCE_COMPARISON.json), [anchored source findings](SOURCE_ISSUES.json), [local evidence](reports/01nov-2026/). Conflicting RAG/closure narratives and IoT image error are retained for owner review, freshly checked at 153 distinct cell anchors during live QA. The prior August IoT banner and WCS 65% mismatch are resolved in the new source. The supplied 01Nov weekly label coexists with source updates through 08Nov; dates are not corrected or presented as an as-of-01Nov cutoff. Earlier reports are preserved under `reports/25oct-2026-baseline/` and `reports/01nov-2026-live/pre-live-*`.

Application directory `/home/user/workspace/it-leadership-dashboard`; managed static preview on port **3000**:

```bash
python -m http.server 3000 --bind 0.0.0.0 --directory /home/user/workspace/it-leadership-dashboard
```

Temporary verification server was stopped and awaited. Reproduction commands and QA environment versions are in [QA_REPORT.md](QA_REPORT.md).
