# Weekly refresh — 18 October 2026, fifth supplied attachment

## Source choice and comparison

Existing repository `esaonc-ai/it-leadership-dashboard`, branch `main`, and public site https://esaonc-ai.github.io/it-leadership-dashboard/ retained. Starting revision: `fddf031`.

Selected **IT_Project_Portfolios_2026_v1.0 (18Oct2026 PST)_4.xlsx**, the latest explicitly user-supplied revision among equally dated v1.0 workbooks. Reporting date/version and user submission order determine selection; neither mtime nor suffix alone determines it. The locally present attachment was inspected directly, including every worksheet and historical caveat cell.

Compared all five attached 18 October workbooks and every distinct source workbook in repository history: four 21 September revisions, 28 September, 5 October and 12 October (**12 candidates**). `SOURCE_COMPARISON.json` records hashes, comparisons of values/formulas/caches/direct and effective RAG styles, conditional rules, and record reconciliation. Historical records are not merged into the weekly dashboard.

| Attachment | Bytes | SHA-256 |
|---|---:|---|
| IT_Project_Portfolios_2026_v1.0 (18Oct2026 PST).xlsx | 101974 | `53855338f8ad05aa88b6cdb52a1a084e4d7e52a5dc8e78356aa6412df4d80147` |
| IT_Project_Portfolios_2026_v1.0 (18Oct2026 PST)_1.xlsx | 101764 | `4fe46088545543f9fa98fc545f05d1f5f092d8f9010c89a995351634f0a0faa3` |
| IT_Project_Portfolios_2026_v1.0 (18Oct2026 PST)_2.xlsx | 101703 | `e556f16524b5975b9a8a8db9baa1d7daea7d4b49fd74d307ee822e4f87c22759` |
| IT_Project_Portfolios_2026_v1.0 (18Oct2026 PST)_3.xlsx | 101722 | `fc545f7cd6d74df3738b5149b28576060696a9977c7ae58b6f97e62567c963c4` |
| IT_Project_Portfolios_2026_v1.0 (18Oct2026 PST)_4.xlsx | 101863 | `bfa717b9374fa262449994b49b8965b4f1d631e2281795d555950f2d542236ec` |

The fifth attachment differs from `_3.xlsx` in **31 cell values**: 20 Infrastructure & Cloud owners and nine Compliance Program owners now include “Mike Wang's replacement pending”; Compliance Program **I3/I13** apply the same substitution inside progress narratives. Exact before/after text and cell coordinates are recorded in `SOURCE_COMPARISON.json`.

No records, sheet names, RAG values, dates, completion values, formulas or cached results change. Direct cell formatting and resolved conditional-rule multisets (including ranges, priorities and differential styles) match `_3.xlsx`, as do all 133 effective RAG fill/font combinations. Raw ZIP/serialization differences remain intact in the original source download. Prior Infrastructure & Cloud B64/K64 title/Cubework owner updates remain present; I64 still contains the historical QBerg/Qbert narrative.

No source workbook is modified or saved through an Excel library. The selected attachment bytes are copied directly to `Weekly_Leadership_Source_Workbook.xlsx` and embedded unchanged in the downloadable dashboard. Source files are hashed before comparison and after comparison, local QA and public QA.

## Record reconciliation and source formatting

| Team | Records | Amber | Green | Red | Included source rows |
|---|---:|---:|---:|---:|---|
| IT Security | 9 | 3 | 6 | 0 | 2–5, 8–12 |
| Infrastructure & Cloud | 63 | 43 | 20 | 0 | 2–64 |
| IoT | 5 | 0 | 5 | 0 | 4–8 |
| R&D AI | 9 | 0 | 9 | 0 | 2–10 |
| WCS Engineering | 8 | 3 | 4 | 1 | 2–9 |
| Compliance Program | 16 | 14 | 0 | 2 | 2–17 |
| UNIS.CO Email & Ticketing | 14 | 2 | 12 | 0 | 2–15 |
| UNIS ITEM- eHub integration | 9 | 9 | 0 | 0 | 2–10 |
| **Total** | **133** | **74** | **56** | **3** | |

All eight worksheets inspected. IoT headers are row 3; all others row 1. All use A:N: identifier A, project B, status C, RAG D, start E, delivery/completion F, percentage G, objective H, progress I, next steps J, owner K, risks L, attention M, notes N. All records with an identifier/project are included, including incomplete optional notes. IT Security rows 6–7 have only D/N fragments without an identifier/project, so no records or reassigned notes are invented. IoT rows 1–2 are banners; R&D AI rows 11–15 contain formatting only.

All 133 percentages are numeric; source precision is retained in the XLSX and dashboard percentages are whole numbers. Source starts: 77 calendar dates, 56 TBD. Delivery/completion values: 4 calendar dates, **102 TBD/qualified TBD, 21 N/A**, 6 text/relative estimates. All N/A values are retained exactly. No blank date cells or invalid ISO date literals. Relative/text values at Infrastructure & Cloud F41, R&D AI F3/F5:F7, WCS Engineering F8 remain unchanged, including WCS's separate October test target and early-December deployment qualification. No calendar dates are inferred from durations or narrative text.

Six effective source RAG fill/font combinations remain: 71 Amber with dark amber font, 3 Amber with black font; 42 Green with dark green font, 9 Green with black font, 5 IoT Green with its distinct pale-green style; 3 Red. Rendered badge fill/font, chart segments and KPI strips are checked against raw source XLSX XML independently of Python generation. Unsupported-extension warnings were investigated: extended data bars affect F/G/K, not RAG D; original XML/image bytes remain intact in downloads. No RAG style legend, color-code strings or “Source RAG styles” heading appears in the dashboard.

## Current source issues, freshly re-audited

- **IoT A2:** still references 23 August and an August roadmap. Weekly reporting date uses the selected 18 October attachment.
- **IoT N6:** sole worksheet formula/cached error: `_xlfn.DISPIMG` with cached `#NAME?`. Dashboard shows the neutral workbook-image reference; formula/image bytes remain in the original download.
- **IoT N8; IT Security N11:N12:** notes remain absent. Records remain included; details show “Not provided.”
- **IT Security D6/N6 and D7/N7:** orphan Green/note fragments remain. They are audited, not counted as workstreams or guessed to belong elsewhere.
- **Replacement pending wording:** IT Security K2:K5/K10 remains unchanged. Newly updated owner fields: Infrastructure & Cloud **K2:K3, K5:K6, K8:K9, K11:K17, K19:K20, K34, K58:K61**; Compliance Program **K2, K4, K7, K9:K12, K15:K16**. These remain source statements, not dashboard assignments.
- **Compliance Program I3/I13:** newly revised text says “Mike Wang's replacement pending left before completing…” technical sections. This awkward narrative is preserved exactly; no interpretation or correction is introduced.
- **Source status/narrative alignment:** IT Security C9/G9 say Completed/100% while I9/J9/M9 still describe undocumented authorization and required access controls. C11/G11 say Completed/100% while I11/J11/M11 retain account/control actions. C12 says Completed while I12/J12/M12 still describe review/final-acceptance follow-up. Infrastructure & Cloud C32/G32 say Completed/100% while I32/J32/K32/M32 retain work-in-progress, validation and request-owner text. These coexist in the source and are displayed faithfully; no dashboard interpretation replaces them.
- **IoT E4:E8 and F8:** TBD; F4:F7 N/A. **IoT D8/G8:** remains Green/20%. Historical Amber/90% is not substituted.

`Source_Field_Gaps.csv` contains exact cells for all date uncertainty/not-applicable values and absent optional fields. Full row mapping, every formula/cache, excluded nonempty rows, styles and extension ranges: `qa-local/revision-3/workbook-audit.json`.

## QA and deployment

Existing generator, all-sheet audit, independent raw-XML reader and Playwright scripts were inspected for applicability. All eight sheets retain supported A:N headers, numeric completion values and resolvable RAG rules. Python audit independently compares every source cell and row to the payload; Playwright separately parses raw XML from the original attachment, independently of Python generation.

The QA script now additionally checks every displayed detail field (team, status, RAG, objective, next steps and management attention added to existing date/owner/progress/risk/notes checks), detail font colors, and HTTP error responses. No application logic/design or dependencies changed.

Python compilation, `node --check` for the workbook reader and every generated inline script passed. This static HTML/JavaScript app has no framework build/typecheck step.

Fresh local QA: **PASS, 19,143 assertions**, zero browser errors, failed requests or HTTP error responses. Reconciled all 133 records and every source field; all 14 available Team/RAG combinations, all 24 cascade transitions and resets; actual badge fill/font, chart and KPI styles; integer percentages; every displayed detail field and delivery estimate; empty/search/date/upload validation states; desktop/mobile layouts and screenshots; offline downloaded dashboard filters; and exact direct/button/offline/mobile workbook downloads. Screenshots were visually inspected. Evidence: `qa-local/revision-4/qa-results.json`, `workbook-audit.json`, `source-caveats.json`, `desktop.png`, `mobile.png`, `mobile-detail.png`, `http.json`, `page-snapshot.html`, and downloaded artifacts. Tracked summary: `QA_LOCAL_RESULTS.json`.

Anonymous public QA is pending deployment of this source; `QA_PUBLIC_RESULTS.json` explicitly marks it pending. Browser-only uploads are local snapshots and do not mutate operational systems. The bounded local verification server is stopped and awaited before publishing.
