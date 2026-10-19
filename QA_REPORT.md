# Weekly dashboard refresh — 18 October 2026

## Source selection and integrity

Existing repository and static dashboard retained: https://github.com/esaonc-ai/it-leadership-dashboard. Public URL: https://esaonc-ai.github.io/it-leadership-dashboard/.

Available candidates were the attached `IT_Project_Portfolios_2026_v1.0 (18Oct2026 PST).xlsx` and the repository's 12 October workbook (128 records, 78 Amber / 48 Green / 2 Red). Selected version v1.0 dated 18 October by reporting filename date, not filesystem or document modified timestamp. No additional workbook download was needed.

Original SHA-256 before refresh, after audit/QA, copied workbook, embedded workbook and downloaded workbook:

`53855338f8ad05aa88b6cdb52a1a084e4d7e52a5dc8e78356aa6412df4d80147`

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

- **IoT A2:** still states 23 August 2026 and an August roadmap. Dashboard reporting week uses the 18 October source date.
- **IoT E4:E8:** TBD. **F4:F7:** now N/A, replacing the historical TBD. **F8:** TBD. No dates inferred from status or attention text.
- **IoT N6:** `_xlfn.DISPIMG` image formula still has cached `#NAME?`. This is the sole formula/cached error across all worksheet cells. The detail view uses “Embedded workbook image; view in source workbook”; original workbook bytes retain the formula/image.
- **IoT N8, Security N11:N12:** source notes absent. Records remain included; detail views explicitly show “Not provided.” Security orphan notes N6:N7 are not guessed to belong to other rows.
- **IoT D8/G8:** current source remains Green / 20%. Historical Amber / 90% is not substituted or used as a current discrepancy.
- Source starts: 77 calendar dates, 56 TBD. Delivery/completion: 4 calendar dates, 104 TBD or qualified TBD values, 19 N/A, 6 text/relative estimates. No blank date cells or invalid ISO calendar literals. All text estimates remain exact; no relative estimate is converted to an invented date.
- Relative/text delivery cells: Infrastructure & Cloud F41; R&D AI F3, F5:F7; WCS Engineering F8. WCS F8 retains both the 31-Oct test target and early-Dec arrival/deployment qualification.
- All 133 completion values are numeric and displayed rounded to whole percentages. Source UNIS.CO G6/G14 fractional completion values remain untouched in the XLSX.
- `Source_Field_Gaps.csv` lists every date uncertainty/not-applicable value and absent optional field by exact sheet/cell. `qa-local/workbook-audit.json` includes every source row mapping, all non-record nonempty rows, formula caches and extended formatting ranges.

## Validation and publishing

Local Playwright QA passed **18,212 assertions** with zero console/page errors or failed requests. Independently reconciled all 133 records and fields; tested all 14 represented Team/RAG combinations plus unavailable options, all 24 cascade transitions, reset, summary-card filters, search and empty states; opened every record detail and checked exact dates/notes; verified actual rendered badge/chart/KPI colors and whole percentages. Desktop 1440×1000 and mobile 390×844 passed, including mobile details/download and internal table scrolling. Downloaded HTML passed the complete filter matrix offline, keyboard detail interaction and byte-identical workbook download. Valid local upload, reporting-week validation, visible loading/disabled feedback, invalid-upload protection and offline uploaded snapshots passed. Screenshots were visually inspected. Anonymous direct workbook HTTP and triggered downloads match the attachment hash.

Python scripts compile; the workbook reader and every inline HTML script pass `node --check`. There is no framework build/typecheck step in this static app, and no app dependency changes were made. No operational-system write smoke tests were used; uploads are local browser-only snapshots.

Local evidence: `qa-local/qa-results.json`, `workbook-audit.json`, `http.json`, `page-snapshot.html`, `page-text.txt`, `desktop.png`, `mobile.png`, `mobile-detail.png`, `dashboard.html`, `public-workbook.xlsx`, `offline-workbook.xlsx`, `mobile-workbook.xlsx`, and uploaded snapshot/download artifacts. Summary: `QA_LOCAL_RESULTS.json`.

Published content commit **`4c47d61`** to the existing `main` branch. GitHub Pages built it successfully from the existing repository root. Anonymous public Playwright QA at https://esaonc-ai.github.io/it-leadership-dashboard/ passed **18,212 assertions**, the same complete suite as local QA: 133 records, 14 represented Team/RAG combinations, 24 cascade transitions, every detail, desktop/mobile, source colors, integer percentages, direct/triggered downloads, offline dashboard filtering and workbook extraction. Zero console/page errors and zero failed requests. Original/source/online/offline/mobile workbook SHA-256 values match.

Public evidence: `QA_PUBLIC_RESULTS.json` and `qa-public/qa-results.json`, `deployment-content.json`, `http.json`, `page-snapshot.html`, `page-text.txt`, `desktop.png`, `mobile.png`, `mobile-detail.png`, `dashboard.html`, and all triggered workbook downloads. Screenshots, snapshots and workbook artifacts remain local; only appropriate app/source, scripts and QA summaries are committed.

Temporary verification server was stopped and awaited. Application directory: `/home/user/workspace/it-leadership-dashboard`. Managed preview command from that directory: `python -m http.server 3000 --bind 0.0.0.0` (port 3000, arbitrary Host accepted). No deployment blockers remain; source caveats above remain faithfully represented.
