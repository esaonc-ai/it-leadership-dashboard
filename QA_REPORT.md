# Weekly dashboard refresh — 18 October 2026, latest supplied revision

## Source selection and integrity

Existing repository and static dashboard retained: https://github.com/esaonc-ai/it-leadership-dashboard. Public URL: https://esaonc-ai.github.io/it-leadership-dashboard/.

Selected `IT_Project_Portfolios_2026_v1.0 (18Oct2026 PST)_1.xlsx`, the latest supplied revision among equally dated 18 October v1.0 sources. Compared both available 18 October attachments and the historical 12 October repository workbook (128 records, 78 Amber / 48 Green / 2 Red). Filesystem/document modification times were not selection criteria. The attachment was already present; no download was needed.

The new attachment is **not byte-identical** to the earlier 18 October source: 101,764 versus 101,974 bytes; prior SHA-256 `53855338f8ad05aa88b6cdb52a1a084e4d7e52a5dc8e78356aa6412df4d80147`. Eight cell values change across five Security records: **K2:K5, K10, N2:N4** now refer to “Mike Wang’s replacement pending.” These values are displayed exactly as supplied. No records, RAG values, completion values, dates, or effective RAG styles changed. Both attachments were read only. `SOURCE_COMPARISON.json` records the candidates, hashes, exact cell changes, ZIP-part differences, and historical comparison.

Direct cell styles match the previous 18 October source. Raw formatting IDs changed (59 conditional rules renumbered), and duplicate WCS data-bar rules were serialized in another order. Resolved conditional-rule multisets, priorities, differential styles and all 133 effective RAG styles are unchanged. Raw workbook/table metadata changes remain in the byte-identical download.

Original SHA-256 before refresh, after audit/QA, copied workbook, embedded workbook and downloaded workbook:

`4fe46088545543f9fa98fc545f05d1f5f092d8f9010c89a995351634f0a0faa3`

The workbook is read only, copied/embedded byte for byte and never re-saved through an Excel library. Unsupported extension warnings were investigated in raw XML: the extended rules are data bars in F/G/K, not RAG column D; original XML extensions and images remain in the unchanged download.

## All-worksheet reconciliation

| Team / worksheet | Records | Amber | Green | Red | Included rows |
|---|---:|---:|---:|---:|---|
| Security | 9 | 3 | 6 | 0 | 2–5, 8–12 |
| Infrastructure & Cloud | 63 | 43 | 20 | 0 | 2–64 |
| IoT | 5 | 0 | 5 | 0 | 4–8 |
| R&D AI | 9 | 0 | 9 | 0 | 2–10 |
| WCS Engineering | 8 | 3 | 4 | 1 | 2–9 |
| Compliance Program | 16 | 14 | 0 | 2 | 2–17 |
| UNIS.CO Email & Ticketing | 14 | 2 | 12 | 0 | 2–15 |
| UNIS ITEM- eHub integration | 9 | 9 | 0 | 0 | 2–10 |
| **Total** | **133** | **74** | **56** | **3** | |

All eight worksheets are visible and use A:N: identifier A, project B, status C, RAG D, start E, completion/delivery F, percentage G, objective H, progress I, next steps J, owner K, risk L, attention M, notes N. IoT has a row-3 header; the others have row-1 headers. All valid rows, including records with absent optional notes, are included. Security rows 6–7 contain only Green in D and old note references in N, without identifier, project or workstream details; audited as orphan remnants, not invented records or reassigned notes. R&D AI rows 11–15 contain formatting only. IoT rows 1–2 are title/banner rows.

Compared with 12 October: Infrastructure adds IDs 62–64 and no longer contains former ID 19 (UNIS.CO Email Transition & Ticketing Integration); R&D AI adds IDs 8–9; eHub adds ID 9. Net change +5. This reports the current workbook, without merging history into weekly totals.

Effective source RAG fills/fonts include six combinations: 71 Amber with dark amber font, 3 Amber with black font; 42 Green with dark green font, 9 Green with black font, 5 IoT Green with its distinct pale green fill/font; 3 Red. Colors are audited independently from raw XML (including rule priorities and translated formulas) and checked against actual computed browser styles. No style legend or color strings appear in the dashboard.

## Source issues and date fidelity

Freshly re-audited every cell in all eight worksheets. Historical issues below were checked against the new attachment; none were assumed to persist.

- **Security K2:K5, K10:** the new revision explicitly says Mike Wang’s replacement is pending. **N2:N4** contain the revised source-note wording. No replacement person was invented.

- **IoT A2:** still states 23 August 2026 and an August roadmap. Dashboard reporting week uses the 18 October source date.
- **IoT E4:E8:** TBD. **F4:F7:** now N/A, replacing the historical TBD. **F8:** TBD. No dates inferred from status or attention text.
- **IoT N6:** `_xlfn.DISPIMG` image formula still has cached `#NAME?`. This is the sole formula/cached error across all worksheet cells. The detail view uses “Embedded workbook image; view in source workbook”; original workbook bytes retain the formula/image.
- **IoT N8, Security N11:N12:** source notes absent. Records remain included; detail views explicitly show “Not provided.” Security orphan notes N6:N7 are not guessed to belong to other rows.
- **IoT D8/G8:** current source remains Green / 20%. Historical Amber / 90% is not substituted or used as a current discrepancy.
- Source starts: 77 calendar dates, 56 TBD. Delivery/completion: 4 calendar dates, 104 TBD or qualified TBD values, 19 N/A, 6 text/relative estimates. No blank date cells or invalid ISO calendar literals. All text estimates remain exact; no relative estimate is converted to an invented date.
- Relative/text delivery cells: Infrastructure & Cloud F41; R&D AI F3, F5:F7; WCS Engineering F8. WCS F8 retains both the 31-Oct test target and early-Dec arrival/deployment qualification.
- All 133 completion values are numeric and displayed rounded to whole percentages. Source UNIS.CO G6/G14 fractional completion values remain untouched in the XLSX.
- `Source_Field_Gaps.csv` lists every date uncertainty/not-applicable value and absent optional field by exact sheet/cell. `qa-local/revision-1/workbook-audit.json` includes every source row mapping, all non-record nonempty rows, formula caches and extended formatting ranges.

## Validation and publishing

Local Playwright QA passed **18,212 assertions** with zero console/page errors or failed requests. Independently reconciled all 133 records and fields; tested all 14 represented Team/RAG combinations plus unavailable options, all 24 cascade transitions, reset, summary-card filters, search and empty states; opened every record detail and checked exact dates/notes; verified actual rendered badge/chart/KPI colors and whole percentages. Desktop 1440×1000 and mobile 390×844 passed, including mobile details/download and internal table scrolling. Downloaded HTML passed the complete filter matrix offline, keyboard detail interaction and byte-identical workbook download. Valid local upload, reporting-week validation, visible loading/disabled feedback, invalid-upload protection and offline uploaded snapshots passed. Screenshots were visually inspected. Anonymous direct workbook HTTP and triggered downloads match the attachment hash.

Python scripts compile; the workbook reader and every inline HTML script pass `node --check`. There is no framework build/typecheck step in this static app, and no app dependency changes were made. No operational-system write smoke tests were used; uploads are local browser-only snapshots.

Local evidence: `qa-local/revision-1/qa-results.json`, `workbook-audit.json`, `http.json`, `page-snapshot.html`, `page-text.txt`, `desktop.png`, `mobile.png`, `mobile-detail.png`, `dashboard.html`, `public-workbook.xlsx`, `offline-workbook.xlsx`, `mobile-workbook.xlsx`, and uploaded snapshot/download artifacts. Summary: `QA_LOCAL_RESULTS.json`.

Fresh local QA against this newly supplied attachment passed all checks above. The existing audit and browser scripts were inspected and remain applicable: all eight headers still map A:N, all 133 completion cells are numeric, and supported raw-XML RAG formatting resolves without fallbacks. No application logic, design or dependency changes were necessary. Only the data payload, embedded workbook/public XLSX and source/QA evidence are refreshed.

Publishing and fresh anonymous public QA for this revision are pending. The existing `main` branch and GitHub Pages configuration are retained.
