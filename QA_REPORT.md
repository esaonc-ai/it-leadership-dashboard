# Weekly refresh — 18 October 2026, fourth supplied attachment

## Source choice and comparison

Existing repository `esaonc-ai/it-leadership-dashboard`, branch `main`, and public site https://esaonc-ai.github.io/it-leadership-dashboard/ retained. Starting revision: `cac0fbd`.

Selected **IT_Project_Portfolios_2026_v1.0 (18Oct2026 PST)_3.xlsx** because it is the latest explicitly user-supplied revision among equally dated v1.0 workbooks. Date/version and user submission order were used; neither mtime nor suffix alone determined selection. The file was present locally and inspected directly; no download was needed.

Compared all four attached 18 October sources plus every distinct workbook in repository history: four 21 September revisions, 28 September, 5 October and 12 October. `SOURCE_COMPARISON.json` contains all **11 candidates**, SHA-256 values, before/after integrity checks, values/formulas/cache/style comparisons and per-sheet reconciliation. Historical versions are not merged into the weekly dashboard.

| Attachment | Bytes | SHA-256 |
|---|---:|---|
| Original 18 October | 101974 | `53855338f8ad05aa88b6cdb52a1a084e4d7e52a5dc8e78356aa6412df4d80147` |
| Second attachment `_1.xlsx` | 101764 | `4fe46088545543f9fa98fc545f05d1f5f092d8f9010c89a995351634f0a0faa3` |
| Third attachment `_2.xlsx` | 101703 | `e556f16524b5975b9a8a8db9baa1d7daea7d4b49fd74d307ee822e4f87c22759` |
| **Selected fourth attachment `_3.xlsx`** | **101722** | **`fc545f7cd6d74df3738b5149b28576060696a9977c7ae58b6f97e62567c963c4`** |

The selected workbook is not byte-identical to `_2.xlsx`. Exactly two cell values change, both in Infrastructure & Cloud row 64:

- **B64:** “Tenant Wi-Fi PPSK and VLAN Governance” → “Tenant Wi-Fi and VLAN Governance.”
- **K64:** the owner list replaces “QBerg-Qbert Team” with “Cubework IT Installation Team”; other named owners remain as supplied.

No records, sheet names, RAG values, dates, completion values, formulas or formula caches changed. Direct cell formats, resolved conditional-rule multisets (including ranges, priorities and differential styles) and all 133 effective RAG fill/font combinations match `_2.xlsx`. Raw ZIP metadata/worksheet serialization differences are retained in the exact source download. The revised title and owner appear in the table, search and detail view. Source I64 still includes the historical “QBerg/Qbert was believed to handle passwords” narrative; K64 contains the updated team reference. Both are preserved as supplied.

No source workbook was modified or re-saved through an Excel library. The selected original bytes are copied to `Weekly_Leadership_Source_Workbook.xlsx` and embedded unchanged in the downloadable dashboard. All compared source files are hashed before and after comparison and QA.

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
- **IT Security K2:K5/K10:** replacement remains pending, as supplied.
- **Source status/narrative alignment:** IT Security C9/G9 now say Completed/100% while I9/J9/M9 still describe undocumented authorization and required access controls. C11/G11 say Completed/100% while I11/J11/M11 retain account/control actions. C12 says Completed while I12/J12/M12 still describe review/final-acceptance follow-up. Infrastructure & Cloud C32/G32 say Completed/100% while I32/J32/K32/M32 retain work-in-progress, validation and request-owner text. These coexist in the source and are displayed faithfully; no dashboard interpretation replaces them.
- **IoT E4:E8 and F8:** TBD; F4:F7 N/A. **IoT D8/G8:** remains Green/20%. Historical Amber/90% is not substituted.

`Source_Field_Gaps.csv` contains exact cells for all date uncertainty/not-applicable values and absent optional fields. Full row mapping, every formula/cache, excluded nonempty rows, styles and extension ranges: `qa-local/revision-3/workbook-audit.json`.

## QA and deployment

Existing audit, generator, raw-XML reader and Playwright scripts were inspected. They remain applicable: current headers/layouts are supported, all 133 completion cells are numeric, all RAG rules/colors resolve, and filter expectations derive from current source team names and values. The Python audit independently reconciles source cells to the payload; Playwright expectations parse the original attachment's raw XLSX XML separately from Python generation. No application logic/design or dependency changes were necessary.

Python scripts compile, the workbook reader passes `node --check`, and all inline scripts pass `node --check` after data generation. No framework build/typecheck applies to this static HTML/JavaScript app.

Fresh local QA: **PASS, 18,212 assertions**, zero browser errors/failed requests. Reconciled every record from raw workbook XML, all 14 available Team/RAG combinations and 24 cascade transitions, all details/delivery values, effective RAG styles, integer percentages, desktop/mobile layouts, empty/search/date states, local upload validation, offline downloaded dashboard filters, and byte-identical online/offline/mobile workbook downloads. Desktop/mobile screenshots were visually inspected. Evidence: `qa-local/revision-3/qa-results.json`, `workbook-audit.json`, `desktop.png`, `mobile.png`, `mobile-detail.png`, `http.json`, and `page-snapshot.html`. Tracked summary: `QA_LOCAL_RESULTS.json`.

Anonymous public QA is pending deployment of this attachment; `QA_PUBLIC_RESULTS.json` explicitly marks it pending. Browser-only local uploads do not write to operational systems. The bounded local verification server is stopped before publishing; no separate preview is needed after public verification.
