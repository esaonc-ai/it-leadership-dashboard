# Portfolio Dashboard QA and Source Issues — 08Nov2026, revision 1

**Publication and live end-to-end QA: PASS.** The actual public URL **https://esaonc-ai.github.io/it-leadership-dashboard/** serves the latest **`_1.xlsx` same-week revision**, **179 valid records / 85 Amber / 94 Green / 0 Red**. Canonical public HTML is byte-identical to coordinator-pushed application commit **`3b8e6fe2f814e81bbd638f66bbccef7456b86ccf`**. This conclusion follows actual HTTP/browser/download checks, beyond the reported successful push.

Report completed: **2026-11-16T23:38:00.594420+00:00**. Full live suite completed: **2026-11-16T23:36:09.626538+00:00**. Independent fresh mobile/offline checks completed: **2026-11-16T23:36:20.003329+00:00**. Existing application directory: `/home/user/workspace/it-leadership-dashboard`. No source edit, application/test code change, feature addition, dependency upgrade, remote Git operation or operational-system write test occurred in this verification run.

## Actual deployment proof and propagation

At **2026-11-16T23:34:49.809193+00:00**, the first anonymous exact-URL check still served the original 08Nov snapshot (**88 Amber / 91 Green**, source hash `a2c669002b25f78ebe4dc0397daa3f98fd59385af690d149a1a9f1881e0b08bd`). The second check at **2026-11-16T23:35:04.997459+00:00**, about 15 seconds later, served the new **85 Amber / 94 Green** revision and exactly matched the pushed HTML. The subsequent full browser suite and fresh mobile context used the canonical query-free URL and confirmed the revision again. No cache-busting URL or authentication is needed.

Public HTML SHA-256: `891324979ee9e91f9304fde3a55c0bef57e52976df5db9f6cec4b9fa17b6df20`.

The following direct anonymous URLs all returned **HTTP 200**, no authentication or redirect, and exact expected bytes. Headers and timestamps are retained in `direct-public-checks.json`:

| Public URL | Verified UTC | Bytes | Result |
|---|---|---:|---|
| https://esaonc-ai.github.io/it-leadership-dashboard/ | 2026-11-16T23:35:55.114145+00:00 | 516,528 | Exact pushed HTML / original workbook bytes |
| https://esaonc-ai.github.io/it-leadership-dashboard/index.html | 2026-11-16T23:35:55.341173+00:00 | 516,528 | Exact pushed HTML / original workbook bytes |
| https://esaonc-ai.github.io/it-leadership-dashboard/Weekly_Leadership_Source_Workbook.xlsx | 2026-11-16T23:35:55.522212+00:00 | 126,410 | Exact pushed HTML / original workbook bytes |

## Selected source and revision comparison


Selected latest supplied same-week revision **IT & Technology Project_Portfolios_2026_v1.0 (Week of 08Nov2026 PST)_1.xlsx**, 126,410 bytes, week **2026-11-08**. Both 08Nov uploads were compared bytewise and through independent read-only full-cell/type, formula/cache, direct-style, effective-RAG, worksheet metadata, conditional-format and ZIP-part inventories. The `_1` suffix alone was not treated as proof of identical content or a different reporting week.

| Original uploaded candidate | Bytes | Records | Amber | Green | SHA-256 |
|---|---:|---:|---:|---:|---|
| IT & Technology Project_Portfolios_2026_v1.0 (Week of 01Nov2026 PST).xlsx | 115,853 | 164 | 89 | 75 | `04d0a8be91c203387eb6d27bf2543eab822772f07407e9769254d68b06620467` |
| IT & Technology Project_Portfolios_2026_v1.0 (Week of 08Nov2026 PST).xlsx | 126,350 | 179 | 88 | 91 | `a2c669002b25f78ebe4dc0397daa3f98fd59385af690d149a1a9f1881e0b08bd` |
| IT & Technology Project_Portfolios_2026_v1.0 (Week of 08Nov2026 PST)_1.xlsx | 126,410 | 179 | 85 | 94 | `bf5fdec3238aff668760b3b0a110bf0aac52eab822b79d41399a59e50f3d2550` |

The revision changes exactly three value/type cells: **`WCS Engineering!D7`, `D8`, `D11`: Amber → Green**. These same three cells have direct-format and effective-RAG changes. All other cell values/types and all formula/cache content are unchanged. There are 16 differing ZIP parts, worksheet metadata changes on eight sheets, and resolved conditional-format differences on IT Compliance Program, IoT and WCS Engineering; extended conditional-format XML is unchanged. This is a genuine revision with three effective status changes, not a claim that only three ZIP bytes changed. No record was added or removed; no history was fabricated. No weekly upload newer than 08Nov is available among the three original workspace attachments. Workbook discovery distinguishes originals from repository/download/test copies.

Fresh read-only public baseline at **2026-11-16T23:26:39.969996+00:00** still matched the previous checkout and original 08Nov source: **179 / 88 Amber / 91 Green / 0 Red**, application commit `1a1183e8f2817179ebc95eb806a419ec4b512b78`, evidence commit `f72f9f1d6af79f1d6e567c1b524d90f880a032f6`. Direct public workbook SHA-256 `a2c669002b25f78ebe4dc0397daa3f98fd59385af690d149a1a9f1881e0b08bd`; HTML SHA-256 `1caa8b104c9043abbe73547c44df096c738fd5d7a27b2f6f864ac05096c7a1b1`. These baseline GETs are not publication proof for `_1`.

## Reconciliation and presentation


**179 valid records: 85 Amber / 94 Green / 0 Red.** Actual source RAG cells control the display even when notes disagree. No Red option or other source bucket was invented.

| Exact worksheet / TEAM | Records | Amber | Green | Red |
|---|---:|---:|---:|---:|
| IT Security | 13 | 1 | 12 | 0 |
| Infrastructure & Cloud | 98 | 61 | 37 | 0 |
| IoT | 5 | 0 | 5 | 0 |
| R&D AI | 9 | 0 | 9 | 0 |
| WCS Engineering | 11 | 6 | 5 | 0 |
| IT Compliance Program | 17 | 12 | 5 | 0 |
| UNIS.CO Email & Ticketing | 16 | 2 | 14 | 0 |
| UNIS ITEM- eHub integration | 10 | 3 | 7 | 0 |

All eight worksheet names were freshly discovered and retained verbatim, including punctuation, case and spaces. Full dropdown labels and health labels fit/wrap on desktop/mobile; the wide source table scrolls internally without page overflow. Existing branding and CSS are byte-identical to the baseline. Weekly-only reporting remains, with exactly one TEAM and one cascading RAG dropdown and no RAG-style legend, source-style heading or raw color strings in the UI.

Every valid identifier/project row remains in worksheet order, including optional blanks and repeated project names. IDs are currently unique within each worksheet, but no deduplication rule was introduced. Repeated `Infrastructure & Cloud` projects at rows 23/24, 37/38, 54/55 and 62/63 remain separate records; rows 54/55 caution about overlapping scope. Record counts do not assert independent delivery scope. `IoT!D8` has Green but no identifier/project at A8/B8: this orphan cell is documented without inventing a project. All five valid IoT records remain, including row 9 with blank optional N9.

Completion: **166 numeric values**, displayed as whole percentages; **13 exact source text values** (`Not verified` / `Not quantified`) remain visible and are excluded from numeric averages. Current numeric average **75%**. No inferred completion is substituted. Delivery values remain exact in table, every drilldown and CSV: **137 TBD, 20 source/relative/conditional estimates, 12 calendar dates and 10 N/A**. The three changed WCS rows retain their original delivery text, including week-of-09Nov targets and testing-dependent TBD.

## Live end-to-end QA

**47,867 live browser assertions PASS**: **42,227** established-suite assertions plus **5,640** independent fresh-mobile/offline assertions. **Zero console errors, page errors, failed requests or HTTP error responses** across both browser runs. Results are newly executed against production, not copied from local or prior live results.

- Established unchanged Playwright suite ran against the exact public URL in fresh anonymous Chromium at desktop **1440×1000**, mobile **390×844**, and downloaded offline HTML. No saved browser profile/auth state was supplied; initial context has no cookies and needs no login. Supplemental tests launch an independent fresh mobile context plus a separate fresh mobile offline context.
- All **36 TEAM/RAG matrix entries**, **25 available / 11 unavailable**, **14 specific TEAM/RAG pairs** and **16 cascade transitions** reconcile to the source. Filtering/reset suites run desktop/mobile/offline and independently repeat in the fresh mobile context. Inapplicable Amber resets on TEAM change; absent Red stays unavailable. Exactly **one TEAM dropdown and one cascading RAG dropdown** remain throughout.
- All **179 records** reconcile field by field to independent workbook reading and source-cell audit, including optional blanks, record order and worksheet row identity. All **179 drilldowns** open and retain status, estimated delivery date/TBD/conditional text, source text completion and whole numeric percentages. Actual computed badge fill/font colors, chart counts/colors, KPI fill proportions and rounded shares match effective workbook conditional formatting, including `IT Security!D4`'s distinct Amber shade.
- Full worksheet labels match exact case/punctuation/spaces in TEAM, chart, table, details and CSV. Selected full TEAM labels fit and chart labels wrap without clipping desktop/mobile; no page overflow. No invented status bucket, RAG-style legend/source-style heading or visible raw color strings. All three revised WCS Green records retain the conflicting Amber notes in mobile details.
- Numeric completion remains **166 values**, average **75%**; all **13 “Not verified”/“Not quantified”** values remain exact and excluded from numeric averages. Portfolio RAG shares are whole **47% Amber / 53% Green**. Exact narrative percentages are not rewritten. Calendar dates, TBD, N/A, target weeks, relative/conditional delivery estimates survive table, details and CSV unchanged.
- Actual CSV downloads reconcile every source field for **179 all-record rows**, **6 WCS Engineering / Amber rows**, header-only empty results, mobile and offline. Source-row identity, exact strings, Unicode and multiline source notes survive CSV parsing. Downloads show visible feedback and retain correct weekly filenames.
- Actual workbook and standalone dashboard HTML downloads succeed from production. Downloaded `IT & Technology Program Leadership Dashboard_Weekly.html` operates with browser networking disabled from `file://`: all filters/cascades/reset, details, Enter/Escape keyboard interaction, CSV and workbook downloads pass. Fresh mobile offline checks independently verify all-row rendering, revised WCS Green filtering and byte-identical workbook download.
- Read-only search, summary-card filter, reset and visible empty/unavailable states pass. Browser-local workbook parsing validates a missing report week, shows loading/disabled feedback, succeeds with exact source bytes, preserves uploaded filename/week offline, and rejects invalid XLSX visibly while preserving the last valid snapshot. These exercises parse files in the browser and perform no operational-service mutations.
- Source workbook integrity was verified through anonymous direct HTTP, embedded bytes and actual desktop, mobile, offline, local-browser uploaded-snapshot and fresh mobile offline workbook downloads. All match the original byte-for-byte and preserve the suggested original filename.

Live screenshots were captured and visually inspected for desktop, mobile and full worksheet-label presentation. No local preview server was needed or started: the verified production site is the preview. Existing local QA, four conditional-expression regression tests, Python/JavaScript syntax checks and idempotence evidence are preserved; they were not represented as new live assertions. Framework build/lint/typecheck does not apply to this standalone HTML/JavaScript repository, which has no such configuration.

## Source issues and changes requiring source-owner review


**No source correction was made.** The following distinguishes explicit contradictions from scope/evidence questions and contextual observations; 63 anchored findings/observations are retained in `SOURCE_ISSUES.json`, with fresh values/caches. All **227 prior anchor occurrences** were reread unchanged; three new WCS findings were added. Nothing was newly resolved between the two 08Nov uploads.

| Priority source observation | Exact anchors and current evidence |
|---|---|
| **New revision conflicts** | `WCS Engineering!D7/D8/D11` are now **Green**, while `M7/M8/M11` still direct **Keep Amber** pending deployment/testing/acceptance. D7's resolution in the original 08Nov source is **reversed**; it must no longer be reported resolved. Dashboard faithfully displays Green and retains those notes. |
| **Infrastructure status conflict remains** | `Infrastructure & Cloud!D65` Green vs `I65` offline and `M65` Red. `C65/G65` now say unresolved / Not verified: old Completed/100% part stays resolved, RAG discrepancy remains. |
| **Conflicting completion** | `IT Compliance Program!G2` 80% vs `I2/N2` 59%; `WCS Engineering!G8` 85% vs `C8/I8/M8/N8` about/corrected 80%; `G12` 85% vs `M12` 80%. These remain unchanged. |
| **IoT stale banner and image error** | `IoT!A2` still labels 23-Aug-2026 and cites 30Oct roadmap; `IoT!N6` DISPIMG has cached `#NAME?`, with no `xl/media` asset in original ZIP. Both remain; no stale banner/date or picture is invented as replacement. |
| Other explicit RAG directives | `Infrastructure & Cloud!D4/D23/D24/D27/D38/D56` Green vs corresponding M cells Amber; `D36/D62/D63/D64` Amber vs corresponding M cells Red. `IT Compliance Program!D5` and `UNIS.CO Email & Ticketing!D6/D12/D17` Green vs corresponding M cells Amber. |
| Reviewer assessments, distinct from actual RAG | `Infrastructure & Cloud!D28/D41/D53/D54/D55/D89/D90/D94` Amber vs corresponding M reviewer assessment Red; `IT Security!D11/D14` Green vs M reviewer assessment Amber. These are source narratives, not permission to override actual cells or infer failed controls. |
| Completion scope/evidence review | `Infrastructure & Cloud!G14/G17/G19/G20/G31/G32` 100% vs C/I/J open/unstarted work; `C16/G16/I16/J16/N16` Completed/100% with follow-up and limited closure evidence. `G89:G99` 60% vs matching N cells saying not quantifiable. `IoT!G4:G6` 100% with H/I/J UAT/sizing/procurement next steps: clarify completed scope before treating follow-up alone as proof of a false percentage. |
| Delivery scope / chronology review | `WCS Engineering!F4` permanent yellow fence before testing vs `I4` cardboard-fence proposal; review I4/J4/M4 scope. `IT Compliance Program!I14` pickup 10/8 vs `N14` note dated 11-Sep needs chronology clarification. |
| Provenance / ownership gaps | `Infrastructure & Cloud!N89:N99` reference “Infrastructure Review”, absent from eight supplied tabs; external source files are not supplied. `IT Security!K3:K5` and `IT Compliance Program!K4/K7/K9:K12/K15:K16` retain replacement-pending owners. |
| Weekly label with later updates (context) | Week label remains 08Nov, while `Infrastructure & Cloud!I28/I53/I89` contain 13-Nov updates and `IT Security!I11` references a 16-Nov chain. No strict as-of-08Nov cutoff is claimed or inferred. |
| Orphan / optional cells (context) | `IoT!A8/B8` blank with `D8` Green is excluded as a nonrecord; valid `IoT!N9` optional blank is retained. This does not justify deleting valid rows. |

Previously resolved/clarified findings that **remain** so in `_1`: `IT Security!C5/G5`, `C7/G7`, `C8/G8`, `C9/G9` explicitly unverified; `C6` distinguishes completed pilot from pending administrator MFA (90%). Infrastructure rows 5/6/11/12/40 have unverified completion rather than unsupported numeric closure; `Infrastructure & Cloud!C30/N30` explicitly scope 100% to restored HTTPS while retaining follow-up. `WCS Engineering!D5/G5` robot row remains Amber/70% with unresolved work. These do not resolve the separate remaining issues above. The IoT August banner remains stale, and WCS visitor D7 is no longer resolved.

Live source reassessment reread the complete cell/formula/cache/style/conditional-format/ZIP inventory and matched the local revision inventory exactly. All **63 findings/observations** were freshly checked against **231 distinct cell anchors (251 anchor occurrences)**, including all three new WCS RAG conflicts. None changed during deployment or QA. Explicit contradictions, reviewer assessments, scope/evidence questions and optional/context observations remain distinct; no source correction was guessed.

## Immutable source and download integrity

Selected original attachment: **IT & Technology Project_Portfolios_2026_v1.0 (Week of 08Nov2026 PST)_1.xlsx**, **126,410 bytes**. Original source, public direct workbook, embedded source, distributed copy and all actual workbook downloads share SHA-256:

`bf5fdec3238aff668760b3b0a110bf0aac52eab822b79d41399a59e50f3d2550`

All three original upload hashes were rechecked unchanged after this live run. No original workbook was saved through a spreadsheet library; original ZIP extensions, cached formulas and styles remain byte-for-byte intact. Read-only library warnings affect only in-memory interpretation, not original bytes. Workbook download suggestions retain the exact `_1.xlsx` supplied filename; the stable public distribution path is `Weekly_Leadership_Source_Workbook.xlsx`.

## Evidence, preservation and delivery

Current live results: `QA_PUBLIC_RESULTS.json`; live report: `LIVE_QA_REPORT.md`; current tracked live evidence: `reports/08nov-2026-revision-1-live/`; complete raw downloaded HTML/workbooks/page captures: `qa-public/08nov-2026-revision-1/`. Evidence includes public URL headers/times, propagation log, fresh source audit, exact source-issue recheck, actual CSV exports, all filter matrices, screenshots, download integrity and artifact hash manifests. Reproduction uses the established suite against the production URL with the unchanged source and this live audit; the exact supplemental script is preserved in the live evidence directory.

All previously tracked application/source/test files, local revision evidence, prior live evidence and local QA/source reports are protected by before/after hashes. Earlier root live/public/README files and the pre-live standalone local report are archived as `pre-live-*` under the new live directory. Prior `reports/08nov-2026/`, `reports/08nov-2026-live/`, `reports/08nov-2026-revision-1/`, original published baseline and older-week directories remain unchanged. The standalone report below is byte-identical to the current repository live report; root `QA_REPORT.md` retains its historical local pre-publication scope.

Standalone deliverable: **`/home/user/workspace/Portfolio_Dashboard_QA_and_Source_Issues_08Nov2026_Revision_1.md`**. A local follow-up commit contains documentation/evidence only; pushing that commit is for evidence synchronization and is not needed to establish the already verified application deployment. Coordinator handles remote Git. No separate preview service is required.
