# Weekly dashboard refresh — 12 October 2026

## Source integrity and reconciliation
- Existing dashboard/repository retained; no replacement site created.
- Newest supplied attachment is the 12 October weekly workbook. Current payload is 128 genuine workstream records across eight teams. No valid records were excluded because of unspecified optional fields.
- 78 Amber, 48 Green, 2 Red. Previous 5 October payload: 111 records (62 Amber, 47 Green, 2 Red). Infrastructure increases from 51 to 61 and eHub integration from 1 to 8.
- Team counts: Infrastructure & Cloud 61; Compliance Program 16; UNIS.CO Email & Ticketing 14; Security 9; WCS Engineering 8; eHub integration 8; R&D AI 7; IoT 5.
- Attachment and public copy SHA-256: `d3b5b52ae2416337da56c1af981ee328aa7fae566f47256a7fb64be2175cba7d`.
- Workbook bytes are copied/embedded unchanged, not re-saved. Source edits were neither authorized nor made.

## Prior IoT issues rechecked against both workbooks
| Prior issue | 12 October finding |
|---|---|
| Five shifted data rows 2–6 | Resolved in the supplied source: title rows 1–2, headers row 3, records rows 4–8; completion now G, owners K, notes N. Dashboard discovers the header instead of dropping IoT. |
| No start dates | Still no actual dates: E4:E8 are explicitly TBD. Estimated delivery F4:F8 is also TBD. No dates fabricated from target text in C. |
| M4 image formula cached #NAME? | Persists at N6: `_xlfn.DISPIMG` formula, cached `#NAME?`. Dashboard uses a neutral workbook-image reference; original image/formula bytes retained. |
| Row 6 missing notes (M6) | Persists for the same Phase 2 workstream, now N8 blank. No substitute notes created. |

Additional IoT observation: A2 still states reporting date 2026-08-23 and references an August roadmap. Dashboard weekly scope uses the supplied 12 October file, not this stale sheet banner. Source change to note: Phase 2 workstream is now Green / 20%, versus Amber / 90% in the previous workbook. Both new values are faithfully reported; confirm with the owner if unexpected.

## Optional source-field gaps, not missing records
- Start dates: 82 valid calendar dates; 46 TBD; zero blank/invalid date literals.
- Estimated delivery: 6 valid calendar dates, 105 TBD, 13 N/A, 4 relative/unscheduled estimates (R&D AI F3, F5:F7). No invalid calendar date literals. Text is displayed as supplied, not converted to guessed dates.
- Eight nonnumeric completion cells: Infrastructure & Cloud G10, G53:G57, G59:G60. G10 states "TBD - 3 AP replacements remaining"; the other seven state TBD. Preserved as text; excluded from the numeric completion average (120 numeric records; displayed average 74%).
- Source/notes gap: IoT N8. Cached formula error: IoT N6 only in A:N across included sheets.
- `Source_Field_Gaps.csv` lists exact coordinates and supplied values for every unspecified/relative/not-applicable date.

## QA
Initial refresh local standalone end-to-end QA passed: 5,071 assertions, 13 represented Team → RAG combinations, all 128 detail views, then-existing per-card controls, invalid prior RAG reset, deliberately empty search, restoration, computed badge/chart colors, named chart totals, KPI color-strip proportions, whole percentages and estimated delivery values. Independent expected RAG styles were evaluated from raw XLSX XML using the browser reader, separately from the Python generation path. 37 cells have conditional fill overrides; eight effective RAG fill/font variants are retained. Unsupported XML extensions were inspected; they affect data bars in F/G/K or repeated columns, not canonical RAG D cells.

Triggered workbook and dashboard downloads work; downloaded HTML reopens offline and produces a byte-identical workbook. Valid future-week local upload and snapshot downloads work; invalid upload leaves the last validated payload unchanged. Desktop/mobile screenshots inspected. No console/page errors. Neutral dashboard/download labels; no separate RAG-style/color-code legend; no CDN/internal runtime API/login dependency.

## Public deployment verification
Verified anonymous URL: https://esaonc-ai.github.io/it-leadership-dashboard/

GitHub Pages served the 12 October build with 128 records before public tests ran. Deployed build commit: `0095678`. Public end-to-end QA passed **5,071 assertions**, all 13 represented Team/RAG combinations and 128 detail views, zero browser console/page errors. Publicly triggered downloads, downloaded offline HTML, upload snapshots and byte-identical workbook downloads passed. The anonymous static workbook URL also returned HTTP 200 with the same source hash. Repo and Pages are public; no authentication is needed. See `QA_PUBLIC_RESULTS.json`.

**Remaining blockers:** none for deployment or dashboard QA. Remaining issues are the source-field gaps and IoT caveats above; edits require source-owner authorization. Confirm the IoT Phase 2 Green/20% change and stale August sheet banner with its owner if needed.


## Filter simplification requested after refresh
Regenerated the same dashboard with exactly **one shared Team dropdown and one shared RAG dropdown**. Removed all duplicate per-card dropdowns; cascading Team → RAG options remain. No data refresh or other feature changes were made. Payload and original/source workbook bytes are unchanged.

Verified build `3cd0971` anonymously at the same public URL. Local and deployed end-to-end QA each passed **5,090 assertions**, including exactly two dropdowns after filtering and offline reopening, all 13 Team/RAG combinations, 128 details, source RAG colors, dates and whole percentages, both download actions, future-week upload and invalid-upload protection. Zero browser errors; no new issues. `QA_PUBLIC_RESULTS.json` now contains these latest results.
