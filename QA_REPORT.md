# Portfolio Dashboard QA and Source Issues — 08Nov2026, revision 1

**Local refresh and QA: PASS. This revision is not published or live-verified.** Existing application: `/home/user/workspace/it-leadership-dashboard`, repository `esaonc-ai/it-leadership-dashboard`, branch `main`. No new site, separate Item-hosted dashboard, operational write test, remote Git operation, feature addition or dependency upgrade occurred. The coordinator handles push and requests subsequent live QA.

Report completed: **2026-11-16T23:33:07.146438+00:00**. Full-suite verification: **2026-11-16T23:29:05.021684+00:00**. URL tested locally: `http://127.0.0.1:3000/`. Production destination: https://esaonc-ai.github.io/it-leadership-dashboard/.

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

## Executed QA

**47,867 browser assertions PASS: 42,227 established-suite assertions plus 5,640 fresh mobile/offline assertions.** Four focused conditional-expression regression tests also pass. There were **zero console errors, page errors, failed requests or HTTP error responses** in either browser run.

- Established Chromium suite: desktop 1440×1000, mobile 390×844, downloaded offline dashboard, all 179 source rows and all 179 drilldowns. Source reader and independent cell/XML audit reconcile fields, status strings, completion, delivery estimates, conditional fill/font colors, chart counts and KPI percentages.
- Every TEAM/RAG matrix entry: **36 entries**, **25 available / 11 unavailable**, **14 specific TEAM/RAG pairs**, **16 cascade transitions**, reset behavior and source-only available options. Full matrix runs desktop, mobile and offline; independently repeated in a fresh mobile context. Red is absent and therefore unavailable throughout.
- Anonymous desktop and independent fresh mobile contexts require no cookies/login or stored auth. A separate fresh mobile offline context verifies the downloaded dashboard and revised WCS Green filter/download.
- Actual browser CSV downloads: all records, WCS Amber (now **6**), empty result, mobile and offline. Every exported field, source row, whole/text completion and delivery string reconciles.
- Actual dashboard and workbook downloads, filenames and visible feedback; offline filtering, keyboard detail, CSV and workbook download. Public-copy local HTTP GET, mobile, desktop, offline and browser-local uploaded-snapshot workbook downloads are byte-identical to the selected original.
- Search, no-results state, numeric-unavailable completion filtering, missing report-week validation, disabled/loading feedback, successful browser-local upload, invalid XLSX rejection and preservation of last valid snapshot pass. Upload tests operate only in the local browser; no operational backend writes occurred.
- Python compile, reader and all three extracted inline JavaScript syntax checks pass. Idempotent regeneration preserves exact HTML bytes. Arbitrary Host request returns HTTP 200 and exact HTML. Framework build/lint/typecheck commands do not apply: this existing repository has no package.json/framework build/compiler/linter configuration.
- Desktop, mobile labels/health and changed-WCS detail screenshots were captured; desktop/mobile screenshots were visually reviewed. Temporary server stopped and awaited; port 3000 closed.

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

## Integrity, preserved evidence and reproduction

Selected original, distributed copy, embedded source and all five actual workbook download paths share SHA-256:

`bf5fdec3238aff668760b3b0a110bf0aac52eab822b79d41399a59e50f3d2550`

All three original upload hashes matched before/after comparison and final QA. Source files were read/copied only, never serialized or saved through a spreadsheet library. Openpyxl extension warnings refer to in-memory interpretation; original ZIP bytes, styles, formula caches and extensions remain unchanged.

Current evidence: `reports/08nov-2026-revision-1/` (audits, exact revision changes, all/filter/empty/mobile/offline CSVs, screenshots, full matrix results, source-integrity and artifact hashes). Prior root reports are archived byte-for-byte with verified hashes in `reports/08nov-2026-original-published-baseline/`. Earlier `reports/08nov-2026/`, `reports/08nov-2026-live/` and older weeks remain unchanged. Root `LIVE_QA_REPORT.md` remains historical verification of the original 08Nov upload; current `QA_PUBLIC_RESULTS.json` explicitly marks this revision unverified publicly.

Reproduce from `/home/user/workspace/it-leadership-dashboard` (static production files; port **3000**):

```bash
python -m http.server 3000 --bind 0.0.0.0 --directory /home/user/workspace/it-leadership-dashboard
```

In a separate shell in that application directory:

```bash
qa-local/venv/bin/python scripts/qa_dashboard.py http://127.0.0.1:3000/ --workbook '/home/user/workspace/IT & Technology Project_Portfolios_2026_v1.0 (Week of 08Nov2026 PST)_1.xlsx' --report-date 2026-11-08 --audit reports/08nov-2026-revision-1/workbook-audit.json --output qa-local/08nov-2026-revision-1-rerun
qa-local/venv/bin/python reports/08nov-2026-revision-1/fresh_mobile_check.py
python scripts/test_rag_expressions.py
```

The supplemental script uses this revision's retained `qa-local/08nov-2026-revision-1/` audit/download directory. No preview server is left running. Push and subsequent live verification are still required before this revision can be called published.
