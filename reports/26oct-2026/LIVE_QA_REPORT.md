# Live QA — IT & Technology Program Leadership Dashboard

**PASS — published and verified at 2026-10-27T07:21:06.895410+00:00.**

Existing URL: https://esaonc-ai.github.io/it-leadership-dashboard/  
Published commit: **9250e6b50dfa7137a4c4f74e49d106eec9282330**  
Pages workflow: [40466318754](https://github.com/esaonc-ai/it-leadership-dashboard/actions/runs/40466318754), **completed / success** for that exact SHA. Build and deploy jobs both succeeded. Existing **main / root** Pages mechanism and branding remain unchanged. The coordinator performed the push; this verification run used no remote Git, auth, deployment or alternate site.

The first read-only fetch still showed 18 October / 133 records. Bounded polling confirmed the latest artifact on the second attempt, at **2026-10-27T07:19:26.343741+00:00**; both canonical URL and cache-bypassed requests then returned the exact committed HTML. This report's PASS applies to the published latest revision, not the former baseline.

## Live snapshot and exact artifacts

**Reporting week: 26 October 2026. Source: IT & Technology Project_Portfolios_2026_v1.0 (26Oct2026 PST)_6.xlsx.**

| Snapshot | Records | Amber | Green | Red |
|---|---:|---:|---:|---:|
| Verified live _6 | **144** | **79** | **55** | **10** |

Published HTML is byte-identical to `9250e6b:index.html`, SHA-256 **`56438cda12441fbb289251ecd4c287dae8efbcc42513739212d0937ef336e704`**. HTTP page and direct workbook requests return **200**. Direct HTTP and browser desktop/mobile/offline workbook downloads are byte-identical to the original uploaded _6 and the committed source workbook, SHA-256 **`077f4dbf228a5f33be2940d519b17ad83f60a3cd4529da555e0ed9c43e64a4dc`**.

The real browser dashboard download SHA-256 is **`1a0de216042cf77343499c9c50e68a7039af7d6208af1b5dfd301030b0930824`**. It is byte-identical to the prior locally verified dashboard download, preserves all 144 records and embeds the exact original workbook bytes. Its HTML is a self-contained browser snapshot; it is checked against that snapshot, while served HTML is checked against committed HTML. File:// offline filtering, cascade/reset, details and source download pass. A separately locally uploaded/offline browser snapshot also preserves exact XLSX bytes.

All seven supplied original hashes remain unchanged after live QA. Local `index.html` and `Weekly_Leadership_Source_Workbook.xlsx` remain byte-identical to the published commit.

## Browser coverage

**25,934 assertions passed** with a clean anonymous Playwright Chromium context, no login cookies, desktop **1440×1000** and mobile **390×844**. **Zero page/console errors, failed requests or HTTP error responses.** Screenshots were visually inspected. No live implementation or publication blockers remain.

Independent raw XLSX XML/style extraction and the Python source audit reconcile every source row and mapped field, record order, details, delivery date/estimate, completion, RAG font/fill, chart counts/styles and KPI counts/shares/average. Duplicate Infrastructure identifiers remain as separate source rows; the three optional-note records remain visible.

All **36 TEAM/RAG states** are audited: **26 reachable states**, **14 specific team/RAG pairs**, **10 impossible pairs excluded from options**. All **24 cascading transitions** verify preservation or reset of the prior RAG plus resulting rows and KPIs. The filter/cascade suite repeats on desktop, mobile and offline. Exactly **one Team and one RAG dropdown**, reset/search/card interactions, visible empty states, modal/keyboard controls and mobile overflow pass.

Weekly-only reporting, exact branding/source filename, whole-number numeric completion and KPI percentages, source-faithful dates/TBD/N/A/relative estimates, actual effective conditional/direct RAG colors and absence of any style legend/raw color strings pass. Current _6 has 144 numeric completions; uncertain date text remains unchanged. Narrative percentages are source facts, not reformatted metrics.

Both actual browser download buttons and visible download feedback pass. Browser-only upload validation checks missing week, loading/disabled controls, success, invalid-file errors and preservation of the last valid in-memory snapshot. These transform only an isolated browser snapshot and send no service writes. All remote requests in this run were read-only GETs; no operational-system mutation occurred. No preview server was started.

## Remaining source-owner findings

These are present in the supplied _6 workbook and preserved as source facts. They do not indicate a deployment or dashboard QA failure.

| Significant anchors | Source finding |
|---|---|
| Infrastructure & Cloud A23:A24, A26:A27, A35:A36, A37:A38, A52:A53, A54:A55, A62:A63, A67:A68 | Repeated identifiers with different row narratives/completions; some pairs also differ in RAG. All retained for owner decisions. |
| Infrastructure & Cloud C65/D65/G65 versus I65/J65; C31/D31/G31 versus I31/J31 | Completed/Green/100% while Sparks IDF remains offline or remote desktop connection still fails. |
| Infrastructure & Cloud C32/G32/I32/J32 | Completed/60% while work remains in progress and requirements are unclear. |
| Infrastructure & Cloud C61/D61/G61/I61/J61 versus Email C17/D17/G17/J17/M17 | Overlapping Teams invitation work differs: Infra Amber/75% pending approval/implementation; Email Completed/Green/100%, with M17 explicitly saying “Keep Amber.” |
| WCS Engineering C5/D5/G5 versus I5/L5 | Resolved/Green/100% versus recurring-error and negative-economics text. Source F5 handover wording remains exact. |
| IT Security G2 versus C2/I2/M2; WCS Engineering G8 versus I8/N8 | Numeric/narrative percentages conflict: 60% versus 59%, and 80% versus 65%. |
| IoT A2; N6 | Stale 23-Aug banner; DISPIMG cached #NAME? with no embedded image asset. |
| IT Security D6/N6, D7/N7 | Orphan RAG/notes without identifier/project; documented but not invented into records. |
| IT Security K2:K5/K10; IT Compliance Program K2/K4/K7/K9:K12/K15:K16 | Replacement-pending ownership text remains. |
| IT Compliance Program I14/N14 | Pickup 10/8 versus notes dated 11-Sep; chronology remains as supplied. |

Other completed-status versus unfinished-narrative review candidates have full anchors in `QA_REPORT.md`. **Optional blank notes:** `IoT!N8`, `IT Security!N11:N12`; these are not business contradictions, and all three records remain included. Infrastructure/WCS sheet duplication and eHub/compliance misgrouping from _5 are resolved in _6 and are not current findings. No QBerg/Qbert reference exists in _6.

## Evidence and local report state

Tracked live summary: `QA_PUBLIC_RESULTS.json`. Full ignored receipts and artifacts: **`qa-public/26oct-revision6/`** — `publication-receipt.json`, `publication-poll-history.json`, successful workflow/job receipts, `qa-results.json`, `live-qa-final-summary.json`, independent `workbook-audit.json`, desktop/mobile/detail screenshots, downloaded dashboard and workbook files, and HTTP receipts.

Only report/evidence files were updated locally; no additional commit or push was made for these results. The dashboard/source remain unchanged at **9250e6b50dfa7137a4c4f74e49d106eec9282330**. `QA_LOCAL_RESULTS.json` retains the original local verification separately from these live results.
