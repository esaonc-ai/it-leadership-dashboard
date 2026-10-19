# Weekly refresh — 18 October 2026, third supplied attachment

## Source choice and comparison

Existing repository `esaonc-ai/it-leadership-dashboard`, branch `main`, and public site https://esaonc-ai.github.io/it-leadership-dashboard/ retained. Starting revision: `d07f9d8`.

Selected **IT_Project_Portfolios_2026_v1.0 (18Oct2026 PST)_2.xlsx** because it is the latest user-supplied revision among equally dated v1.0 workbooks. Date/version and explicit user submission order were used; neither mtime nor suffix alone determined selection. The file was present locally and inspected directly; no download was needed.

Compared the three attached 18 October sources plus every distinct workbook in repository history: four 21 September revisions, 28 September, 5 October and 12 October. `SOURCE_COMPARISON.json` contains all 10 candidates, SHA-256 values, before/after integrity checks, values/formulas/cache/style comparisons and per-sheet reconciliation. Historical versions remain historical and are not merged into the weekly dashboard.

| Attachment | Bytes | SHA-256 |
|---|---:|---|
| Original 18 October | 101974 | `53855338f8ad05aa88b6cdb52a1a084e4d7e52a5dc8e78356aa6412df4d80147` |
| Second attachment `_1.xlsx` | 101764 | `4fe46088545543f9fa98fc545f05d1f5f092d8f9010c89a995351634f0a0faa3` |
| **Selected third attachment `_2.xlsx`** | **101703** | **`e556f16524b5975b9a8a8db9baa1d7daea7d4b49fd74d307ee822e4f87c22759`** |

The selected workbook is not byte-identical to `_1.xlsx`. Meaningful changes:

- Worksheet/team **Security → IT Security**, reflected in all nine records, the Team dropdown, chart, table and detail views.
- **IT Security C9/F9/G9:** Ticket 23527 Monitoring Access Review changes from Authorization Review / TBD / 20% to Completed / N/A / 100%.
- **IT Security C11/C12:** Dedicated Teams Room PC Security and Amazon SP-PII Security Certification 2026 statuses change to Completed; each already had 100% completion.
- **Infrastructure & Cloud F32/G32:** Laptop Image to Virtual Machine changes from TBD / 60% to N/A / 100%; its status was already Completed.
- Total: seven changed cell values across four records, plus the team rename. No records added/removed, no RAG value changes, no formula/cache changes, no direct cell-format changes and no effective RAG fill/font changes. Conditional rules are compared with resolved differential styles, ranges and priorities rather than numeric style IDs alone.
- IT Security K2:K5/K10 and N2:N4 retain the second attachment's “Mike Wang's replacement pending” wording exactly.

No source workbook was modified or re-saved through an Excel library. The selected original bytes are copied to `Weekly_Leadership_Source_Workbook.xlsx` and embedded unchanged in the downloaded dashboard. All source files are hashed before and after comparison and QA.

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

All 133 percentages are numeric; source precision is retained in the XLSX and dashboard percentages are whole numbers. Source starts: 77 calendar dates, 56 TBD. Delivery/completion values: 4 calendar dates, **102 TBD/qualified TBD, 21 N/A**, 6 text/relative estimates. The two new N/A values are retained exactly. No blank date cells or invalid ISO date literals. Relative/text values at Infrastructure & Cloud F41, R&D AI F3/F5:F7, WCS Engineering F8 remain unchanged, including WCS's separate October test target and early-December deployment qualification. No calendar dates are inferred from durations or narrative text.

Six effective source RAG fill/font combinations remain: 71 Amber with dark amber font, 3 Amber with black font; 42 Green with dark green font, 9 Green with black font, 5 IoT Green with its distinct pale-green style; 3 Red. Rendered badge fill/font, chart segments and KPI strips are checked against raw source XLSX XML independently of Python generation. Unsupported-extension warnings were investigated: extended data bars affect F/G/K, not RAG D; original XML/image bytes remain intact in downloads. No RAG style legend, color-code strings or “Source RAG styles” heading appears in the dashboard.

## Current source issues, freshly re-audited

- **IoT A2:** still references 23 August and an August roadmap. Weekly reporting date uses the selected 18 October attachment.
- **IoT N6:** sole worksheet formula/cached error: `_xlfn.DISPIMG` with cached `#NAME?`. Dashboard shows the neutral workbook-image reference; formula/image bytes remain in the original download.
- **IoT N8; IT Security N11:N12:** notes remain absent. Records remain included; details show “Not provided.”
- **IT Security D6/N6 and D7/N7:** orphan Green/note fragments remain. They are audited, not counted as workstreams or guessed to belong elsewhere.
- **IT Security K2:K5/K10:** replacement remains pending, as supplied.
- **Source status/narrative alignment:** IT Security C9/G9 now say Completed/100% while I9/J9/M9 still describe undocumented authorization and required access controls. C11/G11 say Completed/100% while I11/J11/M11 retain account/control actions. C12 says Completed while I12/J12/M12 still describe review/final-acceptance follow-up. Infrastructure & Cloud C32/G32 say Completed/100% while I32/J32/K32/M32 retain work-in-progress, validation and request-owner text. These coexist in the source and are displayed faithfully; no dashboard interpretation replaces them.
- **IoT E4:E8 and F8:** TBD; F4:F7 N/A. **IoT D8/G8:** remains Green/20%. Historical Amber/90% is not substituted.

`Source_Field_Gaps.csv` contains exact cells for all date uncertainty/not-applicable values and absent optional fields. Full row mapping, every formula/cache, excluded nonempty rows, styles and extension ranges: `qa-local/revision-2/workbook-audit.json`.

## QA and deployment

Existing audit, generator, raw-XML reader and Playwright scripts were inspected. They remain applicable: current headers/layouts are supported, all completion cells are numeric, all RAG rules/colors resolve, and filter expectations derive from current source team names and values. No application logic/design or dependency changes were needed.

Python scripts compile, the workbook reader passes `node --check`, and all inline scripts pass `node --check` after data generation. No framework build/typecheck applies to this static HTML/JavaScript app.

Fresh local Playwright QA passed **18,212 assertions**, zero browser console/page errors and zero failed requests. Independently reconciled all 133 current records, tested all 14 available Team/RAG combinations and unavailable options, all 24 cascade transitions, reset/search/empty states, every record detail and source delivery value, exact rendered RAG fills/fonts/charts/KPI proportions, whole-number percentages, desktop 1440×1000 and mobile 390×844. Exactly one Team and one RAG dropdown remain. Downloaded standalone HTML passed the full filter matrix offline, keyboard detail interaction and exact-byte workbook extraction. Direct/triggered/mobile workbook downloads, browser-local upload validation/loading/error states and offline uploaded snapshots passed. Desktop/mobile/detail screenshots were visually inspected. All original attachment hashes remain unchanged.

Local evidence: `QA_LOCAL_RESULTS.json`, `qa-local/revision-2/qa-results.json`, `workbook-audit.json`, `http.json`, `page-snapshot.html`, `page-text.txt`, `desktop.png`, `mobile.png`, `mobile-detail.png`, standalone dashboard downloads and online/offline/mobile workbook files. Prior-run artifacts are retained. Published content commit **`7029697`** to the existing `main` branch; GitHub Pages built successfully. Fresh anonymous public Playwright QA also passed **18,212 assertions**, including the full source reconciliation/filter/detail/style/date/desktop/mobile/offline/download suite above. Zero browser console/page errors and zero failed requests. Public direct and triggered workbook downloads, offline extraction and mobile downloads are byte-identical to the selected third attachment. All 10 compared source files retain their before-task hashes after public QA.

Public evidence: `QA_PUBLIC_RESULTS.json`, `qa-public/revision-2/qa-results.json`, `deployment-content.json`, `http.json`, `page-snapshot.html`, `page-text.txt`, desktop/mobile/detail screenshots, downloaded standalone dashboard and online/offline/mobile/uploaded workbook artifacts. Final deployment verification is recorded at `qa-public/revision-2/final-verification.json`. No deployment or QA blockers remain; the source issues above remain faithfully represented. Browser-only local uploads do not write to operational systems. Temporary verification servers are stopped and awaited after bounded checks; a separate preview is unnecessary once production is verified.
