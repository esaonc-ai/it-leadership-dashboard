# Portfolio Dashboard QA and Source Issues — Week of 08Nov2026

**Publication verified: PASS.** The existing public IT & Technology Program Leadership Dashboard at **https://esaonc-ai.github.io/it-leadership-dashboard/** serves the new **Week of 08Nov2026** snapshot: **179 records — 88 Amber, 91 Green, 0 Red**. Full live end-to-end QA passed **42,275 assertions**, with **2,842 additional assertions** in a separate fresh mobile context (**45,117 combined**). Verification covers actual public content and downloads, beyond the coordinator's successful push.

**Exact URL, timing and served-content proof.** The first anonymous response at **2026-11-16 23:16:23 UTC** still served the previous 01Nov/164-record snapshot. The next exact-URL check at **2026-11-16T23:16:59.152461+00:00** returned 08Nov/179 records, byte-identical to the pushed application commit **1a1183e8f2817179ebc95eb806a419ec4b512b78**. The full live suite completed at **2026-11-16T23:17:51.469984+00:00**. A separate fresh mobile context verified the exact query-free production URL again at **2026-11-16T23:18:00.240782+00:00**. No cache-busting query or authentication is required for the verified result.

Public HTML SHA-256:

`1caa8b104c9043abbe73547c44df096c738fd5d7a27b2f6f864ac05096c7a1b1`

The canonical public root and **https://esaonc-ai.github.io/it-leadership-dashboard/index.html** returned HTTP 200 and matched pushed HTML bytes. Direct original workbook distribution URL **https://esaonc-ai.github.io/it-leadership-dashboard/Weekly_Leadership_Source_Workbook.xlsx** returned anonymous HTTP 200 and exact original bytes. HTTP headers, request timestamps and propagation observations are retained in the evidence directory.

**Source selection, revision comparison and immutable workbook.** Newest available original attachment is **IT & Technology Project_Portfolios_2026_v1.0 (Week of 08Nov2026 PST).xlsx**, 126,350 bytes. Original source SHA-256 before refresh, after local QA and after this live QA remains:

`a2c669002b25f78ebe4dc0397daa3f98fd59385af690d149a1a9f1881e0b08bd`

The original attachment was never edited or re-saved. Direct public HTTP workbook, embedded workbook, desktop/mobile download buttons, offline downloaded dashboard's workbook and the browser-local uploaded-snapshot download all match the original byte-for-byte. Actual download suggestions retain the original supplied filename. The stable `Weekly_Leadership_Source_Workbook.xlsx` path is the existing distribution URL, not an altered source file.

Workspace discovery distinguished the two uploaded originals (01Nov and 08Nov) from repository copies, prior QA downloads and deliberately invalid fixtures. **Only one 08Nov original upload was available**; no same-date alternative was assumed identical or silently selected. The 08Nov workbook is a substantive update from the 01Nov original and actual prior published baseline: **179 versus 164 records**, 614 changed value/type cell anchors, 1,824 formatting anchors, 36 effective RAG anchors, 27 changed ZIP parts; resolved conditional rules changed on five sheets and extended formatting on three. Formula/cache content is unchanged. Both available original attachment hashes were rechecked unchanged during live QA. Detailed candidate hashes and exact semantic differences are in `SOURCE_COMPARISON.json`; this comparison does not create reporting history.

**Independent source reconciliation.** A fresh read-only worksheet audit, raw-XLSX browser parsing and actual rendered browser styles reconcile the live snapshot to the original. All 60 documented source-owner findings were rechecked against **212 distinct exact cell values and caches**. Findings distinguish management directives from explicitly labeled reviewer assessments; neither is used to invent a replacement RAG.

**Source coverage and reconciliation.** Inspected all eight visible worksheets, 2,648 populated/styled cells, formulas and cached errors, headers, excluded nonempty rows, standard and extended conditional-format rules and effective RAG colors. Freshly discovered worksheet names are retained verbatim in TEAM options, health chart, table, drilldowns and CSV:

| Exact worksheet / TEAM label | Records | Amber | Green | Red |
|---|---:|---:|---:|---:|
| IT Security | 13 | 1 | 12 | 0 |
| Infrastructure & Cloud | 98 | 61 | 37 | 0 |
| IoT | 5 | 0 | 5 | 0 |
| R&D AI | 9 | 0 | 9 | 0 |
| WCS Engineering | 11 | 9 | 2 | 0 |
| IT Compliance Program | 17 | 12 | 5 | 0 |
| UNIS.CO Email & Ticketing | 16 | 2 | 14 | 0 |
| UNIS ITEM- eHub integration | 10 | 3 | 7 | 0 |
| **Total** | **179** | **88** | **91** | **0** |

Every valid identifier/project row is retained in source order; optional blanks or overlapping project names never remove a record. Current IDs are unique within each sheet. Repeated project names in `Infrastructure & Cloud!B23:B24`, `B37:B38`, `B54:B55`, `B62:B63` have distinct identifiers and remain separate source rows. Rows 54/55 explicitly caution against summing overlapping delivery scope; the dashboard counts records and reports the average supplied numeric completion, without asserting independent project scope or deduplicating records.

`IoT!A1/A2` are a title/banner, and `IoT!D8` is an orphan Green cell without ID/project at A8/B8. No project or assignment was invented for it. Yard Management is now at row 9; all five valid IoT records remain, including blank optional `IoT!N9`. The excluded row and its exact cells are in the [workbook audit](/home/user/workspace/it-leadership-dashboard/reports/08nov-2026-live/workbook-audit.json).

There are **166 numeric completion values** and **13 source text values**. Numeric metrics and completions display whole percentages; unfiltered average rounds to **75%**, excluding nonnumeric records. Source text remains exactly “Not verified” at `IT Security!G5/G7:G9` and `Infrastructure & Cloud!G5:G6/G11:G12/G40/G65`, and “Not quantified” at `IT Security!G11/G13:G14`. These are not converted into 0%, dropped, or treated as invented RAG buckets. Current RAG shares round to **49% Amber / 51% Green**. Source business narratives, including 8.75% tax and fractional modeled savings/carrier shares, remain verbatim; whole-number reporting applies to completion and calculated dashboard metrics.

Estimated delivery values: **12 calendar dates, 137 TBD including qualified TBD, 10 N/A, 20 source text/relative/conditional estimates**. Starts: 107 calendar, 71 TBD, one source-text value (`IT Security!E14`: “Aug-2026 — exact test date not supplied”). The dashboard preserves all calendar dates, delivery target weeks, qualified TBD, dependencies, relative ETDs and conditional estimates exactly in table, details and CSV; none becomes an inferred firm date. Source status strings are unchanged.

Effective conditional RAG colors reconcile between Python extraction, raw-XLSX browser parsing, computed badge fonts/fills, chart segments and KPI color proportions:

| Source RAG | Effective fill | Effective font | Records |
|---|---|---|---:|
| Amber | `#FFE699` | `#7F6000` | 86 |
| Amber | `#FFF2CC` | `#7F6000` | 1 |
| Amber | `#FFE699` | `#000000` | 1 |
| Green | `#C6E0B4` | `#006100` | 82 |
| Green | `#C6E0B4` | `#000000` | 9 |

Color codes appear in QA evidence only, not product text. No source-style heading or RAG-style legend is rendered. The new exact-equality conditional rule at `IT Security!D4` yields the distinct pale Amber fill above; it must not be replaced with another Amber style. Reviewer Red/Amber narratives do not override actual source RAG cells. There are no source Red records, so Red is unavailable in the dropdown rather than invented as a bucket.


**Current source-owner findings.** All findings below come from current cell values and caches; final verification rechecked 212 distinct anchored cells. The source cells remain authoritative for dashboard data; contradictory narratives are preserved neutrally for owner review. [SOURCE_ISSUES.json](/home/user/workspace/it-leadership-dashboard/SOURCE_ISSUES.json) provides exact expanded sheet/cell anchors and source values for each finding, including distinctions between a management directive and an explicitly labeled reviewer assessment.

| Exact current source anchors | Finding / owner review |
|---|---|
| `Infrastructure & Cloud!D4/D23/D24/D27/D38/D56` versus corresponding M cells | Actual Green cells while management explicitly directs Amber. D4/D27 are newly Green in this source; do not carry prior Amber as current proof. |
| `Infrastructure & Cloud!D36/D62:D64` versus corresponding M/N cells | Actual Amber while management directs Red; some notes claim RAG was aligned to Red although D remains Amber. |
| `Infrastructure & Cloud!D28/D41/D53:D55/D89/D90/D94` versus corresponding M/N cells | Actual Amber while narrative explicitly labels a reviewer Red assessment. These are source reviewer judgments, not confirmed incident severities or dashboard overrides. |
| `IT Security!D11/D14` versus `M11/M14` | Green while notes explicitly describe Amber reviewer assessments of dependencies/evidence gaps. No failed test is inferred. |
| `Infrastructure & Cloud!C65/D65/G65/I65/J65/M65/N65` | **Partly resolved:** Completed/100% has been replaced by unresolved status and “Not verified.” Green versus offline/Red leadership wording remains; no restoration claim is inferred. |
| `Infrastructure & Cloud!G14/G17/G19/G20/G31/G32` versus same-row C/I/J/N | 100% remains despite not-started/open migration/optimization, awaiting SFTP requirements, failed remote desktop, or work-in-progress VM migration. C20/C31/C32 also combine pending/unavailable/work-in-progress wording with “complete.” Source N notes lack later closure evidence. |
| `Infrastructure & Cloud!C16/G16/I16/J16/N16` | Newly Completed/100% while progress supplies no significant update and follow-up remains; owner should confirm the completed scope. |
| `Infrastructure & Cloud!G89:G99` versus corresponding N cells | All 11 new rows contain numeric 60%, while each source note says completion is not quantifiable from supplied evidence. Keep the numbers and caveats pending owner clarification. |
| `IT Compliance Program!G2/I2/N2` | Numeric completion is 80%, while progress and source note explicitly retain/correct PCI DSS v4.0.1 completion to 59%. Separate Security scope-review/SAQ-D measures are not automatically comparable. |
| `WCS Engineering!G8` versus `C8/I8/M8/N8`; `G12/M12` | Both numeric cells are now 85%; row 8 narratives still say approximately/corrected 80%, and row 12 management says keep 80%. The prior consistent row-8 80% finding is no longer current. |
| `WCS Engineering!F4/I4/J4/M4` | Progress discusses a cardboard fence while delivery estimate requires permanent yellow fence before testing; clarify approved acceptance scope. |
| `IT Compliance Program!D5/I5/J5/M5` | Green while auditor scope review remains pending and management says keep Amber. |
| `UNIS.CO Email & Ticketing!D6/D12/D17` versus corresponding I/J/M | Green while management says Amber for Phase II dependencies, outage fallback, or calendar reply/testing acceptance; row 6 still mixes completed validation with unapproved population/dependencies. |
| `IoT!G4:G6` versus same-row H/I/J | 100% alongside remaining UAT, sizing or procurement next steps; completed scope requires clarification. |
| `IoT!A2` | **Returned stale banner:** now says Reporting Date 23-Aug-2026 and cites a 30Oct roadmap. The previous source said 06Nov. Dashboard follows supplied 08Nov filename without rewriting this source. |
| `IoT!N6` | DISPIMG formula still caches `#NAME?`; no xl/media image part exists to extract. Details/CSV retain the pointer to original workbook. |
| `IT Compliance Program!I14/N14` | Pickup narrative 10/8 versus cited 11-Sep note; relative three-to-four-week estimate remains unchanged. |
| `Infrastructure & Cloud!N89:N99` | Notes point to “Infrastructure Review” for S-reference filenames, but none of the eight supplied tabs has that name. External review evidence is not embedded in this workbook; no provenance is invented. |
| `IT Security!K3:K5`; `IT Compliance Program!K4/K7/K9:K12/K15:K16` | Replacement-pending ownership remains. Current Security K2 now identifies Qingmin/Robert, so the old row-2 pending-owner finding is not carried forward. |
| `IoT!A8/B8/D8`; `N9` | Orphan Green cell has no ID/project; optional Yard Management note blank is retained. These are distinct from contradictory completion/RAG claims. |

**Resolved or changed prior concerns.** `IT Security!C5/G5`, `C7/G7`, `C8/G8`, `C9/G9` now explicitly describe unverified completion and retain source text rather than unsupported 100% closure. `C6` now distinguishes pilot completion from administrator MFA pending at 90%. `Infrastructure & Cloud!C5:C6/G5:G6`, `C11:C12/G11:G12`, `C40/G40` similarly state open or unverified scope. These prior numeric closure issues are not reported unchanged. The old Sparks Completed/100% portion is resolved at C65/G65, with its remaining RAG conflict separately documented above.

`WCS Engineering!D7` is now Amber and matches M7, resolving that prior RAG conflict. `Infrastructure & Cloud!C30/N30` explicitly limit 100% to the documented HTTPS restoration milestone while retaining stability follow-up; follow-up alone is no longer reported as a contradiction. WCS robot row 5 remains Amber/70% with unresolved scope acknowledged, so the older Green/100% “resolved all errors” claim remains absent. No duplicate-ID issue exists in current worksheets; repeated project scopes remain distinct valid records. The returned August IoT banner and newly inconsistent WCS 85%/80% values are explicitly current findings, not assumed resolved.

**Reporting-label context.** The attachment is labeled week of **08Nov2026**, but `Infrastructure & Cloud!I28/I53/I89` explicitly describe **13-Nov** actual updates and `IT Security!I11` describes a **16-Nov** email chain. Preserve the supplied weekly label and original dated content; do not assert that all facts were known as of 08Nov or create a different week from internal task dates. Future target dates/conditional estimates are retained as supplied rather than treated as confirmed delivery.


**Live end-to-end scope and outcome.** Reused the full existing Playwright suite unchanged against the exact production URL. Fresh anonymous Chromium desktop **1440×1000**, mobile **390×844**, and downloaded offline HTML all pass. The full suite begins with no authentication or stored session and confirms no login cookies are needed. The separate fresh mobile context independently starts without cookies/local storage and verifies every reachable filter state and cascade again.

All **36 TEAM/RAG matrix entries** pass: nine TEAM choices including All × All/Red/Amber/Green, with **25 reachable entries and 11 correctly unavailable entries**. All **14 available specific TEAM/RAG pairs** reconcile to source counts. All **16 available global-RAG-to-TEAM transitions** preserve applicable values or reset unavailable Amber. Red is absent from the source and unavailable globally. Full filter/cascade/reset suites run on desktop, mobile and downloaded offline HTML; the separate fresh mobile context repeats 25 reachable states and 16 transitions.

Verified exactly **one TEAM dropdown and one cascading RAG dropdown** throughout; full worksheet names remain exact and readable in selected controls, table, health chart, drilldowns and CSV. Health labels wrap without clipping, mobile viewport has no page overflow, and wide table content scrolls internally. Source order and every field for all 179 valid records reconcile; each record's detail opens. Computed badge fills/fonts, KPI source-color proportions and chart segments match effective source conditional formatting, including the distinct `IT Security!D4` equality-rule Amber shade.

Completion and calculated percentages are whole numbers; **166 numeric** completions contribute to the **75%** average. All **13 “Not verified”/“Not quantified”** completions remain exact text, stay visible/searchable and are excluded from numeric averages rather than guessed as zero. Unavailable numeric-only averages display a visible unavailable state. RAG shares are **49% Amber / 51% Green**. Exact source business percentages in narrative text remain unchanged.

All estimated calendar dates, qualified TBD, N/A, relative ETDs, target weeks and conditional/dependency text are source-faithful in table, details and CSV. Search, summary-card filters, reset, visible empty results, unavailable RAG states, detail dialogs and keyboard Enter/Escape pass. No RAG-style legend, source-style heading, invented bucket or user-visible raw color string is rendered. Screenshots from the live site were visually inspected, including long mobile team names and the new conditional color.

Real **CSV, dashboard HTML and workbook downloads** pass with visible feedback and correct suggested filenames. CSV parses back to exact source values for the full **179-row** snapshot, **WCS Engineering / Amber (9 rows)**, header-only empty results, mobile and offline exports. Source row identity, Unicode, quoted multiline narratives, exact status/team names, whole numeric percentages, nonnumeric completion text and conditional delivery estimates survive export unchanged.

Downloaded **IT & Technology Program Leadership Dashboard_Weekly.html** operates from `file://` with browser networking disabled: filters, cascades/reset, details, keyboard interaction, CSV and byte-identical workbook downloads pass. Browser-local upload tests validate missing date, show loading/disabled state, succeed with the original workbook, preserve uploaded filename/week in a downloadable offline snapshot, and show a visible invalid-file error without replacing the last valid snapshot. These upload exercises only parse local browser files; no operational-system create/update/delete or other live service mutation test was run.

**Zero page errors, console errors, failed requests or HTTP errors** in the full live suite. The separate fresh mobile context also recorded zero errors and made GET requests only. No application feature, test code, source workbook or dependency changed in this live-verification run. Existing local regression/syntax checks remain preserved; no framework build/lint/typecheck configuration exists in this standalone HTML/JavaScript app. No separate preview server was needed or started; the verified public site is the production preview.

**Evidence and preservation.** Application directory `/home/user/workspace/it-leadership-dashboard`. Current live summary `QA_PUBLIC_RESULTS.json`, live report `LIVE_QA_REPORT.md`, and tracked HTTP/publication/source/download reconciliation plus desktop/mobile screenshots under `reports/08nov-2026-live/`. Full downloaded artifacts, raw page captures and browser output remain in ignored `qa-public/08nov-2026/`. Prior local `QA_REPORT.md`, `QA_LOCAL_RESULTS.json`, source comparison/findings, source binary, application/test code and `reports/08nov-2026/` remain unchanged. Earlier 01Nov live evidence remains in its original report directories. The previous root live report and pre-live public status are preserved as `pre-live-*` files in the current live evidence directory; a manifest records artifact hashes.

**Owner follow-up.** Review the exact RAG/management and completion/narrative contradictions above; confirm the pending owners and missing provenance references; repair the stale IoT banner/image formula only through an authorized source edit. Optional `IoT!N9` is not a lost record. Resolved/partly resolved prior findings are separately identified so the report does not repeat obsolete claims. Dashboard publication and technical QA pass with those source inconsistencies faithfully retained.

Standalone deliverable: **/home/user/workspace/Portfolio_Dashboard_QA_and_Source_Issues_08Nov2026.md**. It is byte-identical to the repository's current live report. No remote Git command, push or deployment was performed by this verification run. Any follow-up local commit contains documentation/evidence only; it does not alter the already verified published application.
