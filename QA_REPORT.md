# IT & Technology Program Leadership Dashboard — 18 October 2026 refresh

## Source choice and comparison

Existing repository `esaonc-ai/it-leadership-dashboard`, `main`, and https://esaonc-ai.github.io/it-leadership-dashboard/ retained. Starting commit: `25ee713`.

Selected **IT & Technology Project_Portfolios_2026_v1.0 (18Oct2026 PST).xlsx**. It is the latest explicitly user-supplied revision at the newest available reporting date/version (**18 October 2026, v1.0**). Selection uses reporting version/date and user submission order, not filesystem mtime or suffix alone. The file was present locally and inspected directly.

Compared all six supplied equal-date workbooks plus all seven distinct earlier source versions retained in Git (four 21 September revisions, 28 September, 5 October and 12 October): **13 candidates**. `SOURCE_COMPARISON.json` records every hash, cell/formula/cache comparison, direct/effective RAG styles, conditional-rule comparison and per-sheet reconciliation.

| Source | Bytes | SHA-256 |
|---|---:|---|
| IT & Technology Project_Portfolios_2026_v1.0 (18Oct2026 PST).xlsx | 101898 | `cf6bda618321f23e59385d07743728f76295d58d81263e94fe8e8cb0b54987e8` |
| IT_Project_Portfolios_2026_v1.0 (18Oct2026 PST)_4.xlsx | 101863 | `bfa717b9374fa262449994b49b8965b4f1d631e2281795d555950f2d542236ec` |

The new source differs in bytes from `_4.xlsx`, with changes in ZIP parts `docProps/core.xml`, `xl/styles.xml`, `xl/workbook.xml` and table definitions 1/2/3/4/6. **No cell values, formulas, cached results, sheet names, records, dates, percentages, direct cell formats, resolved conditional-rule multisets or effective RAG fill/font styles change.** No weekly histories are merged.

The requested branding is now **IT & Technology Program Leadership Dashboard** in the visible heading, browser title/description, reporting caption, download button and standalone HTML filename (`IT & Technology Program Leadership Dashboard_Weekly.html`). The current source filename is visibly displayed with its literal ampersand, retained in the payload and used for workbook downloads. Local uploads update that filename too; saved offline snapshots retain it. The stable direct URL `Weekly_Leadership_Source_Workbook.xlsx` remains available as a byte-identical copy; source display/download names are separate from that public path.

Original workbooks are never modified or re-saved through an Excel library. The selected original bytes are copied directly and embedded unchanged in downloaded HTML. All source candidates are hashed before/after comparison and QA.

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
- **Replacement pending wording:** IT Security K2:K5/K10 remains unchanged. Existing replacement-pending owner fields: Infrastructure & Cloud **K2:K3, K5:K6, K8:K9, K11:K17, K19:K20, K34, K58:K61**; Compliance Program **K2, K4, K7, K9:K12, K15:K16**. These remain source statements, not dashboard assignments.
- **Compliance Program I3/I13:** current text says “Mike Wang's replacement pending left before completing…” technical sections. This awkward narrative is preserved exactly; no interpretation or correction is introduced.
- **Source status/narrative alignment:** IT Security C9/G9 say Completed/100% while I9/J9/M9 still describe undocumented authorization and required access controls. C11/G11 say Completed/100% while I11/J11/M11 retain account/control actions. C12 says Completed while I12/J12/M12 still describe review/final-acceptance follow-up. Infrastructure & Cloud C32/G32 say Completed/100% while I32/J32/K32/M32 retain work-in-progress, validation and request-owner text. These coexist in the source and are displayed faithfully; no dashboard interpretation replaces them.
- **IoT E4:E8 and F8:** TBD; F4:F7 N/A. **IoT D8/G8:** remains Green/20%. Historical Amber/90% is not substituted.

`Source_Field_Gaps.csv` contains exact cells for all date uncertainty/not-applicable values and absent optional fields. Full row mapping, every formula/cache, excluded nonempty rows, styles and extension ranges: `qa-local/technology-revision/workbook-audit.json`.

## QA and deployment

Existing generator, all-sheet audit, independent raw-XML reader and Playwright scripts were inspected for applicability. Every current worksheet retains supported headers/layouts, numeric completion and resolvable RAG rules. The Python audit independently reconciles every worksheet row/field/formula cache; Playwright separately parses original source XLSX XML and effective styles, independently of Python generation.

New checks cover exact heading/browser title/description/download label and filename, visible/embedded source names including ampersands, suggested workbook names online/offline/mobile, and filename retention after uploading a differently named local file and reopening its offline snapshot. Existing comprehensive record/filter/detail/style/date/mobile/offline checks remain in use. No dependencies were added.

Python scripts compile, the workbook reader passes `node --check`, and every generated inline script passes `node --check`. This plain static HTML/JavaScript app has no framework build/typecheck step.

Fresh local QA: **PASS, 19,182 assertions**, zero browser errors, failed requests or HTTP error responses. All 133 records/every field independently reconciled; all 14 available Team/RAG combinations, 24 cascade transitions and resets; every detail/delivery estimate; actual RAG fill/font, chart and KPI colors; integer percentages; empty/search/date/upload states; desktop/mobile; full offline filtering; original workbook bytes online/offline/mobile; current branding/metadata and filename display/download naming. A differently named local upload retains its own ampersand filename in the visible source label and offline snapshot/download. Screenshots visually inspected. Evidence: `qa-local/technology-revision/qa-results.json`, `workbook-audit.json`, `source-caveats.json`, `desktop.png`, `mobile.png`, `mobile-detail.png`, `http.json`, `page-snapshot.html` and downloaded artifacts. Tracked summary: `QA_LOCAL_RESULTS.json`.

Anonymous public QA is pending deployment of this attachment/branding, explicitly recorded in `QA_PUBLIC_RESULTS.json`. Browser uploads are local snapshots and do not mutate operational systems. The bounded temporary server is stopped and awaited before publishing.
