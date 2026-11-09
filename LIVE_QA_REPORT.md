# Portfolio Dashboard QA and Source Issues — Week of 01Nov2026

**Publication verified: PASS.** The existing public IT & Technology Program Leadership Dashboard at **https://esaonc-ai.github.io/it-leadership-dashboard/** serves the new **01Nov2026 weekly snapshot: 164 records, 89 Amber, 75 Green, 0 Red**. Full live anonymous desktop/mobile browser QA passed **38,172 assertions**. This verifies served content and actual downloads after publication, in addition to the coordinator's successful push.

**Verification times and deployment evidence (UTC).** The first HTTP response at **2026-11-09 19:43:19 UTC** still contained the older 25Oct/154-record snapshot. Reasonable follow-up requests at **2026-11-09 19:43:51 UTC** returned the new snapshot from both the exact public URL and a diagnostic query URL. The full browser suite used the exact public URL above, with no query parameter or login. Browser QA completed at **2026-11-09T19:44:10.502164+00:00**; final fresh anonymous exact-URL recheck passed at **2026-11-09T19:44:50.671879+00:00**. This report does not assume that push success alone proves Pages deployment.

Public HTML is byte-identical to `index.html` from pushed application commit **832566659d7670543e2a851d588c3d82de49a436**, SHA-256 **`472153819ac872aff8854f7a33955b3ed78a28642ad992b7957095c567b6ee79`**. The canonical root, direct `index.html`, and direct source-workbook URLs returned anonymous HTTP 200. No authentication or saved session was supplied; fresh browser contexts required no cookies. The public response and browser evidence identify the correct original filename, reporting week and record counts.

**Original source and immutable downloads.** Selected attachment: **IT & Technology Project_Portfolios_2026_v1.0 (Week of 01Nov2026 PST).xlsx**, 115,853 bytes. The original was read only and never re-saved or edited. Its SHA-256 remains:

`04d0a8be91c203387eb6d27bf2543eab822772f07407e9769254d68b06620467`

Direct public workbook: **https://esaonc-ai.github.io/it-leadership-dashboard/Weekly_Leadership_Source_Workbook.xlsx**. Direct HTTP response, real desktop/mobile download buttons, downloaded offline dashboard's workbook, and the browser-local uploaded snapshot's workbook are all byte-for-byte identical to the original. The embedded base64 workbook also hashes identically. Downloaded workbook filenames preserve the supplied original attachment name; the stable public URL is an existing distribution path, not a renamed or modified original.

The 01Nov source is substantively different from the prior actual 25Oct baseline: 164 versus 154 records, with 770 changed value/type cell anchors, 533 changed formatting anchors and 47 changed effective RAG cell anchors. Only one 01Nov upload was available in the workspace and the supplied transcript discovery found no alternative; no same-date equality or revision precedence is assumed. Prior comparison evidence is preserved. This remains a single weekly snapshot, with no fabricated reporting history.

**Source reconciliation and owner findings.** The live dashboard was reconciled independently to the unchanged original with raw XLSX parsing, a fresh Python worksheet audit, and actual computed browser colors. All current source finding values and cached values were freshly rechecked against **153 distinct anchored cells**. The findings below distinguish source contradictions, optional blanks, and resolved historical issues; none was silently corrected in the workbook or dashboard.

**Complete source reconciliation.** All eight visible worksheets, 2,565 populated/styled cells, formulas/caches, standard and extended conditional formatting were inventoried. There are no hidden worksheets. All valid ID/project rows are retained in workbook order, including the optional blank note and overlapping workstreams. No orphan ID/project rows were found; only IoT's title and banner precede its header. Styled blank rows do not become records.

| Exact worksheet / TEAM label | Records | Amber | Green | Red |
|---|---:|---:|---:|---:|
| IT Security | 9 | 4 | 5 | 0 |
| Infrastructure & Cloud | 87 | 59 | 28 | 0 |
| IoT | 5 | 0 | 5 | 0 |
| R&D AI | 9 | 0 | 9 | 0 |
| WCS Engineering | 11 | 8 | 3 | 0 |
| IT Compliance Program | 17 | 13 | 4 | 0 |
| UNIS.CO Email & Ticketing | 16 | 2 | 14 | 0 |
| UNIS ITEM- eHub integration | 10 | 3 | 7 | 0 |
| **Total** | **164** | **89** | **75** | **0** |

All 164 completion values are numeric, shown as whole-number percentages; average completion rounds to **76%**. RAG shares are **54% Amber / 46% Green**. Original business narratives remain verbatim, including the 8.75% tax in `WCS Engineering!I5` and fractional modeled savings/carrier shares in `UNIS ITEM- eHub integration!I10/L10`; these are source facts, not fractional dashboard completion metrics.

Delivery values: 12 calendar dates, 119 TBD (including qualified TBD), 17 N/A, 16 source text/relative/conditional estimates. Starts: 107 calendar, 56 TBD, one N/A. All conditional targets, dependencies, target deployment weeks and relative ETDs remain unchanged in table, drilldowns and CSV; no inferred dates or conversion of text to a firm deadline. Every original status string is retained.

Effective source colors, including conditional overrides, reconcile independently against raw XLSX XML and actual browser computed styles:

| Source RAG | Effective fill | Effective font | Records |
|---|---|---|---:|
| Amber | `#FFE699` | `#7F6000` | 88 |
| Amber | `#FFE699` | `#000000` | 1 |
| Green | `#C6E0B4` | `#006100` | 61 |
| Green | `#C6E0B4` | `#000000` | 9 |
| Green | `#E2F0D9` | `#375623` | 5 |

These codes appear in QA evidence only. No style legend, source-style heading or raw color codes were added to the product. No Red control option, card or invented status bucket is rendered when the source has no Red records. There is exactly one TEAM dropdown and one cascading RAG dropdown. Worksheet case, punctuation and spaces are unchanged in controls, health chart, table, details and CSV.

**Fresh source-owner findings.** The dashboard follows the actual RAG and numeric completion cells while preserving conflicting source narratives for review. No source correction was guessed. [SOURCE_ISSUES.json](/home/user/workspace/it-leadership-dashboard/SOURCE_ISSUES.json) contains exact cell values and cached values for each finding, including individually expanded anchors for grouped rows below.

| Exact source anchors | Current finding / owner review |
|---|---|
| `Infrastructure & Cloud!D23/D24/D38/D56` versus `M23/M24/M38/M56` | Green cells while management explicitly directs Amber. |
| `Infrastructure & Cloud!D36/D53/D55/D62:D64` versus corresponding M cells | Amber cells while management explicitly retains Red gates. |
| `Infrastructure & Cloud!C65/D65/G65` versus `I65/J65/M65` | Completed/Green/100% while Sparks IDF remains offline and management says Red until diagnosis/restoration. |
| `Infrastructure & Cloud!C31/D31/G31` versus `I31/J31`; `C32/G32` versus `I32/J32/M32` | Remote desktop Completed/100% despite failed connections; VM migration Completed at 60% while work/acceptance remain open. |
| `Infrastructure & Cloud!C5:C6/C11:C12/C14:C15/C17/C19:C20/C30/C40` and same-row G/I/J/M | Completed/100% versus planning, validation, unstarted troubleshooting, migration, requirements or support-resolution actions. Scope/closure review candidates; monitoring or follow-up alone does not establish failure. |
| `WCS Engineering!D7/G7` versus `C7/I7/J7/M7` | Green/95%; production deployment and site acceptance pending, M7 says keep Amber. |
| `IT Compliance Program!D5` versus `I5/J5/M5` | Green while auditor scope review remains pending and M5 says keep Amber. |
| `UNIS.CO Email & Ticketing!D6/D12/D17` versus corresponding I/J/M | Green while management says Amber for Phase II roster/dependencies, fallback approval/testing, and calendar reply/test acceptance. Row 6's status says Phase II validation completed while I6/J6 describe unapproved population/dependencies. |
| `IT Security!C6/G6/I6/J6`, `C7/G7/I7/J7/M7`, `C8/G8/I8/J8`, `C9/G9/J9/M9` | Pilot marked Completed at 90% with work open; authorization marked Completed/100% while undocumented; inventory review at 100% while endpoint population unknown; security review Completed/100% with account/control approval pending. Completed scope requires clarification. |
| `IoT!G4:G6` versus same-row H/I/J | 100% coexists with remaining UAT, sizing or procurement next steps; source does not clarify scope boundaries. |
| `IoT!N6` | DISPIMG formula has cached `#NAME?`; no image/media parts are present to extract. Detail/CSV retain a pointer to the original workbook. |
| `IT Compliance Program!I14/N14` | Pickup narrative says 10/8 while the cited note is dated 11-Sep; relative certificate timing remains source text. |
| `IT Security!K2:K5`; `IT Compliance Program!K4/K7/K9:K12/K15:K16` | Replacement-pending ownership appears in current source. This Security wording has returned in the new attachment; prior reports are not used to claim it absent. |
| `IoT!N8` | Optional blank source/notes only; record retained and detail says “Not provided.” |

**Rechecked chronology and resolved/changed historical findings.** `IoT!A2` now says **06-Nov-2026**, replacing the old stale 23Aug banner. `Infrastructure & Cloud!I7` explicitly says “As of 08-Nov”; `F76/I76` document 06Nov resolution. The attachment's supplied weekly label remains 01Nov; content dates are preserved and no as-of-01Nov cutoff is asserted. This date context warrants owner awareness, not invented date corrections.

The old Security 60%/59% conflict is absent: `IT Security!C2/D2/G2` is now Scope Review/Amber/30%. `WCS Engineering!G8/I8/M8/N8` consistently says approximately 80%; the old 65% narrative is gone. `WCS Engineering!C5/D5/G5` now acknowledges unresolved gripper/acceptance work at Amber/70%, so the prior Green/100% resolved claim is not carried forward. `Infrastructure & Cloud!C33/G33` explicitly describes scope/ownership clarification at 35%, rather than Completed.

Identifiers are unique within each current worksheet; the prior duplicate-ID finding is resolved. Four repeated project names remain in `Infrastructure & Cloud!B23:B24`, `B37:B38`, `B54:B55`, `B62:B63`, with distinct IDs and source rows. All eight records remain; no merging or deduplication is guessed. Security's prior orphan notes and blank N11/N12 are not current findings: the sheet now ends at row 10 with nine valid records. The only blank optional source note is IoT N8.


**Live end-to-end coverage.** Reused the existing Playwright suite without feature or test-code changes. Fresh anonymous Chromium desktop **1440×1000** and mobile **390×844** both pass. Independent browser XLSX parsing reconciles all 164 records in source order, every included field and source-row identity against the fresh worksheet audit. Each record's detail dialog opens and its exact source fields, RAG colors, whole completion percentage, dates and conditional/relative delivery estimates are checked.

All **36 TEAM/RAG matrix entries** were verified: nine TEAM choices including All × All/Red/Amber/Green, comprising **25 reachable entries and 11 correctly unavailable entries**. All **14 available specific TEAM/RAG pairs** reconcile to source counts. All **16 available global-RAG-to-TEAM transitions** correctly retain an applicable RAG or reset unavailable Amber. Red has no source records and is unavailable globally. Complete filtering/cascade/reset suites repeat on desktop, mobile and the downloaded offline dashboard.

Exactly **one TEAM and one RAG dropdown** remain throughout. Worksheet names retain exact case, punctuation and spaces in controls, table, health chart, details and CSV. Full selected names fit the dropdown, health labels wrap without clipping, and the mobile page fits its viewport with wide table content scrolling internally. Actual badges, health bars and KPI color proportions match the workbook's effective conditional formatting. Summary shares and averages use whole-number percentages; exact source business narratives are preserved.

Search, summary-card filtering, clear/reset, visible empty results, unavailable RAG choices, detail dialogs and keyboard Enter/Escape pass. Every estimated date, qualified TBD, N/A, delivery target, dependency and relative ETD remains faithful in table, details and CSV. Screenshots from the actual public site were visually inspected, including the long `UNIS ITEM- eHub integration` mobile selection and detail content.

Real **CSV, dashboard HTML and workbook downloads** pass. CSV parses back to exact full field values for the complete 164-row snapshot, filtered **WCS Engineering / Amber (8 rows)**, a header-only empty result, mobile and offline cases. Quoted multiline narratives and Unicode survive export; completion percentages are whole numbers. Download actions provide visible feedback.

Downloaded **IT & Technology Program Leadership Dashboard_Weekly.html** operates from `file://` with browser networking disabled. Source-faithful filters, cascades/reset, detail interaction, CSV and byte-identical workbook download pass offline. Browser-local upload validation, loading/disabled feedback, success, invalid-file error handling and preservation of the last valid snapshot also pass. Uploads are client-side file operations only; no operational create/update/delete or other live service mutation test was performed.

**Zero browser page errors, console errors, failed requests or HTTP errors** were recorded in the full suite. The final independent fresh context also loaded the exact query-free public URL anonymously, matched pushed HTML bytes, and made GET requests only. No app features or application dependencies changed during this live verification. Framework build/lint/typecheck is not applicable to this existing standalone HTML/JavaScript app; syntax/build-equivalent checks were already recorded in preserved local QA. No additional preview service was needed or started.

**Remaining source-owner action.** Review the anchored RAG and closure/percentage conflicts above, confirm unresolved ownership and the certificate-note chronology, and repair the `IoT!N6` image formula only through an authorized source-workbook edit. `IoT!N8` is an optional note blank, not a lost record. The corrected IoT banner, WCS 80% narrative and other resolved historical issues are expressly separated from current findings. Dashboard publication and technical QA pass despite these faithfully retained source inconsistencies.

**Evidence and preservation.** Application directory: `/home/user/workspace/it-leadership-dashboard`. Tracked live results: `QA_PUBLIC_RESULTS.json`; full live report: `LIVE_QA_REPORT.md`; HTTP headers, publication hashes, worksheet/row reconciliation, source recheck and desktop/mobile screenshots: `reports/01nov-2026-live/`. Full raw browser captures and downloaded artifacts remain under ignored `qa-public/01nov-2026/`. Prior local `QA_REPORT.md`, `QA_LOCAL_RESULTS.json`, source comparison/findings, original workbook and `reports/01nov-2026/` evidence remain unchanged. Previous public summary and live report were preserved as `pre-live-*` evidence. Artifact hashes are recorded in the live evidence directory.

This standalone deliverable is `/home/user/workspace/Portfolio_Dashboard_QA_and_Source_Issues_01Nov2026.md` and matches the repository's current live report byte-for-byte. No remote Git command, push or deployment was performed in this verification run. Any local follow-up commit contains documentation/evidence only and does not change the already verified published application.
