# IT & Technology Program Leadership Dashboard — 08Nov2026 local refresh QA

**Local verification PASS; publication pending.** Refreshed the existing `esaonc-ai/it-leadership-dashboard` application in `/home/user/workspace/it-leadership-dashboard`. No new site or separate Item-hosted dashboard was created or changed. Existing branding, layout and weekly-only reporting remain. No remote Git operation, push, deployment or operational-system write test occurred. The coordinator will push and request live end-to-end verification separately.

**Newest source and revisions.** Selected `IT & Technology Project_Portfolios_2026_v1.0 (Week of 08Nov2026 PST).xlsx`, reporting week `2026-11-08`, 126,350 bytes. Discovered and hashed every available XLSX in the workspace, distinguishing the two original weekly attachments from repository copies, prior browser downloads and deliberately invalid QA fixtures. Exactly one original 08Nov upload is available; no same-date alternative exists to compare or declare identical. The newer attachment is substantively different from the available 01Nov original, rather than a filename-only revision.

The clean checkout began at evidence commit `fd56b34ebbfbf018ff19dae6a60d36584acc2edd`, application content commit `832566659d7670543e2a851d588c3d82de49a436`. Fresh anonymous read-only HTTP checks of https://esaonc-ai.github.io/it-leadership-dashboard/ and its direct workbook on **16-Nov-2026 23:09:23 UTC** matched that committed baseline: **01Nov, 164 records, 89 Amber / 75 Green / 0 Red**. HTML SHA-256 `472153819ac872aff8854f7a33955b3ed78a28642ad992b7957095c567b6ee79`; source hash `04d0a8be91c203387eb6d27bf2543eab822772f07407e9769254d68b06620467`. These are current baseline checks, not publication proof for this refresh.

The new source has **179 valid records: 88 Amber / 91 Green / 0 Red**. Semantic comparison found 614 changed value/type cell anchors, 1,824 formatting anchors, 36 effective RAG anchors and 27 changed ZIP parts. Resolved conditional formatting changed on five sheets; extended formatting changed on three. Formula/cache content is unchanged. Full candidate/hash discovery and exact comparison anchors: [SOURCE_COMPARISON.json](SOURCE_COMPARISON.json). No weekly history was fabricated from this comparison.

**Original source integrity.** Original, public-distribution copy, embedded workbook and actual desktop/mobile/offline/browser-local uploaded-snapshot workbook downloads all have SHA-256:

`a2c669002b25f78ebe4dc0397daa3f98fd59385af690d149a1a9f1881e0b08bd`

Original attachment hashes match before comparison and after every check for both available original uploads. The source was read only and never saved through openpyxl or another spreadsheet library; the served workbook is copied byte-for-byte. Its original filename is retained for actual download suggestions. Original ZIP extensions, formula caches and styles remain untouched. Read-only library warnings about unsupported extensions concern the in-memory representation only; raw ZIP/XML was inventoried and original bytes were preserved. [Integrity manifest](reports/08nov-2026/source-integrity.json).

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

`IoT!A1/A2` are a title/banner, and `IoT!D8` is an orphan Green cell without ID/project at A8/B8. No project or assignment was invented for it. Yard Management is now at row 9; all five valid IoT records remain, including blank optional `IoT!N9`. The excluded row and its exact cells are in the [workbook audit](reports/08nov-2026/workbook-audit.json).

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

**Necessary compatibility change.** This source introduces exact-text conditional-format expressions (`$D4="Amber"`, `"Green"`, `"Red"`) in addition to the previously supported SEARCH expressions. The existing readers initially rejected these unsupported expressions. Extended only the strict Python evaluator and browser raw-XLSX reader to handle case-insensitive exact text equality, retaining fail-closed behavior for unsupported formulas. Synchronized the existing embedded reader. No unrelated features or application dependencies changed; existing CSS, branding, controls and export logic are unchanged. Four targeted regression tests cover exact case-insensitive equality/nonmatches, relative rule translation and matching/stop behavior, existing SEARCH behavior and unsupported-formula rejection.

**Fresh source-owner findings.** All findings below come from current cell values and caches; final verification rechecked 212 distinct anchored cells. The source cells remain authoritative for dashboard data; contradictory narratives are preserved neutrally for owner review. [SOURCE_ISSUES.json](SOURCE_ISSUES.json) provides exact expanded sheet/cell anchors and source values for each finding, including distinctions between a management directive and an explicitly labeled reviewer assessment.

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

**Local end-to-end QA.** **42,275 Playwright assertions PASS**, completed **2026-11-16T23:10:34.144985+00:00**, on the refreshed snapshot, clean anonymous Chromium desktop **1440×1000** and mobile **390×844**. Every source record/order and field reconciles against Python audit and browser raw-XLSX parsing; every record opens a source-faithful detail. Exactly **one TEAM and one cascading RAG dropdown** remain throughout. Full exact selected worksheet names fit controls and health labels wrap without clipping; mobile page fits viewport and wide table scrolls internally. Screenshots, including the new conditional DNS color and long mobile team name, were visually inspected.

Verified all **36 matrix entries** (nine TEAM choices including All × All/Red/Amber/Green): **25 reachable, 11 unavailable**, including all **14 available specific TEAM/RAG pairs**. All **16 available global-RAG-to-TEAM transitions** preserve applicable values or reset unavailable Amber. Red is unavailable globally, so no nonexistent starting selection is forced. Complete filter/cascade/reset suites repeat desktop/mobile/offline. Counts, KPI percentages and effective color proportions, bars, average completion and all delivery values reconcile at each reachable state. Unverified completion records remain searchable/visible and numeric-only averages correctly show unavailable when no numeric record remains.

Search, summary-card filters, reset, visible empty results, no invented RAG values, detail dialogs and keyboard Enter/Escape pass. Zero browser page/console errors, failed network requests or HTTP errors. Weekly-only branding/report date, source filename and no RAG-style legend/raw color strings pass. Original status names and text completion states remain exact.

Real workbook and dashboard download actions, suggested filenames and visible download feedback pass. Anonymous direct source-workbook HTTP download and actual desktop/mobile/offline/source-upload downloads are byte-identical to the original. Downloaded HTML runs from file:// with network disabled: filters/cascades/reset/details, CSV and workbook downloads all pass. Browser-only local upload validates missing date, shows loading/disabled controls, succeeds with this workbook and preserves the valid snapshot after invalid-file errors. These are local file operations; no live operational mutation smoke test was performed.

CSV reconciliation passes all fields for the full 179-row snapshot, filtered **WCS Engineering / Amber (9 rows)**, header-only empty results, mobile and offline. Source row/identifier, exact team/status, whole numeric completions or original nonnumeric text, multiline narratives and conditional estimated delivery dates survive parsing exactly. No source correction or deduplication occurs in exports.

Four focused Python regression tests pass. Python compilation, standalone workbook-reader JS and all extracted inline-script syntax checks pass. There is no package.json, framework build, TypeScript compiler or configured linter in this standalone HTML/JavaScript app; build/lint/typecheck commands therefore do not apply. Existing QA environment was reused without dependency upgrades. Regeneration is byte-idempotent. An arbitrary Host header returns HTTP 200/exact HTML. Temporary 0.0.0.0:3000 verification server was stopped and awaited; port 3000 is closed and no older copy is running.

**Evidence and handoff.** [QA_LOCAL_RESULTS.json](QA_LOCAL_RESULTS.json), [SOURCE_COMPARISON.json](SOURCE_COMPARISON.json), [SOURCE_ISSUES.json](SOURCE_ISSUES.json), [Source_Field_Gaps.csv](Source_Field_Gaps.csv), [row/cell audit](reports/08nov-2026/workbook-audit.json), [source-integrity manifest](reports/08nov-2026/source-integrity.json), and desktop/mobile screenshots in `reports/08nov-2026/`. Full inventories, downloads and raw captures remain ignored in `qa-local/08nov-2026/`. Prior root reports were preserved byte-for-byte under `reports/01nov-2026-published-baseline/` with a hash manifest; existing local/live 01Nov evidence directories remain unchanged. Root LIVE_QA_REPORT.md is retained as historical 01Nov proof; current QA_PUBLIC_RESULTS.json explicitly records **08Nov live QA not run**.

Coordinator handles the local refresh commit's push and subsequent live QA request. **No publication claim is made.** No separate preview service is needed; the existing public URL becomes the preview after successful publication and verification. For a caller-managed local reproduction only: application directory `/home/user/workspace/it-leadership-dashboard`, port **3000**, exact command:

```bash
python -m http.server 3000 --bind 0.0.0.0 --directory /home/user/workspace/it-leadership-dashboard
```

From the application directory with that server managed externally:

```bash
python scripts/audit_workbook.py '/home/user/workspace/IT & Technology Project_Portfolios_2026_v1.0 (Week of 08Nov2026 PST).xlsx' --output qa-local/08nov-2026
qa-local/venv/bin/python scripts/qa_dashboard.py http://127.0.0.1:3000/ --workbook '/home/user/workspace/IT & Technology Project_Portfolios_2026_v1.0 (Week of 08Nov2026 PST).xlsx' --report-date 2026-11-08 --audit qa-local/08nov-2026/workbook-audit.json --output qa-local/08nov-2026
python scripts/test_rag_expressions.py
python -m py_compile scripts/*.py
node --check scripts/workbook_reader.js
```
