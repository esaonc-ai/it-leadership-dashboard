# IT & Technology Program Leadership Dashboard — 30 October 2026 refresh

## Current state

**LOCAL QA PASS — 154 records: 77 Amber, 73 Green, 4 Red.** Reporting week **30 October 2026**, as supplied. The 30 October attachment supersedes 26 October. Existing application `/home/user/workspace/it-leadership-dashboard`, repository `esaonc-ai/it-leadership-dashboard`, branch `main`, existing public URL https://esaonc-ai.github.io/it-leadership-dashboard/ and exact public branding **IT & Technology Program Leadership Dashboard** are preserved. No alternate site, repo, provider or deployment is introduced.

Started from published commit `9250e6b50dfa7137a4c4f74e49d106eec9282330`. The four uncommitted report files left by successful 26 October live QA were preserved byte-for-byte in **`reports/26oct-2026/`**, with `preserved-report-hashes.json`. Historical root `LIVE_QA_REPORT.md` is also retained unchanged. No destructive reset was used. The original successful live evidence remains separate from this local refresh.

This refresh has **not been pushed or deployed**. No remote Git, auth, workflow dispatch or publishing was attempted. Last verified live baseline: **26 October, 144 records (79 Amber / 55 Green / 10 Red)** at commit 9250e6b. No current live QA is claimed for 30 October; `QA_PUBLIC_RESULTS.json` says **NOT_RUN_FOR_THIS_REFRESH** and points to the preserved prior deployed results. Local content is ready for coordinator resolver and native ibisGitTool push, with source-owner caveats below.

## Selection, comparison and source integrity

Selected original **IT & Technology Project_Portfolios_2026_v1.0 (30Oct2026 PST).xlsx**, **116,484 bytes**, SHA-256 **`91513727651ec6c4fcad0ff8b107d56ea89aae02e420229f48dc26050e710ada`**. Workspace/repo workbook files were inventoried. Only **one 30 October upload** exists, so there is no same-date revision pair to compare. Seven earlier 26 October uploads and historical QA copies are older sources, not candidates for the newest reporting week.

Compared the new file with the prior selected 26 October `_6` source, SHA-256 `077f4dbf228a5f33be2940d519b17ad83f60a3cd4529da555e0ed9c43e64a4dc`, reading all sheets/cells and comparing raw values/types, formulas/caches, resolved direct font/fill/border/alignment/protection/number format, priority-ordered conditional rules with differential styles, extended conditional XML and effective RAG fill/font semantics. Difference totals: **22 ZIP parts**, **548 value/type coordinates**, **785 formatting coordinates**, **0 formula/cache differences**, **3 sheets with standard conditional-rule differences**, **0 extended-rule differences**, **41 effective-RAG coordinates**. Coordinate totals include additions/removals and are not counts of changed projects. Full machine evidence: `SOURCE_COMPARISON.json` and the two complete inventories in `qa-local/30oct/`.

Original hashes before and after comparison/generation/QA match for **all eight supplied workbooks**. No original was changed or saved through an Excel library; no factual correction was guessed. Selected bytes are copied directly to `Weekly_Leadership_Source_Workbook.xlsx` and embedded unchanged in the dashboard. Generator output is byte-idempotent. Original/downloaded XLSX caches, formulas, styles and extension XML remain intact.

## Complete workbook and record reconciliation

All **8 visible sheets**, every cell and all **2,311 populated/styled cells** in the new file were inspected, including banners, orphan notes, formula caches, formatted empty rows and conditional formats. No hidden sheets or embedded image assets were found. IoT headers start at row 3; other headers start at row 1; A:N field mapping is independently checked.

| Exact source worksheet | Records | Amber | Green | Red |
|---|---:|---:|---:|---:|
| IT Security | 9 | 2 | 6 | 1 |
| Infrastructure & Cloud | 77 | 49 | 28 | 0 |
| IoT | 5 | 0 | 5 | 0 |
| R&D AI | 9 | 0 | 9 | 0 |
| WCS Engineering | 11 | 7 | 4 | 0 |
| IT Compliance Program | 17 | 14 | 0 | 3 |
| UNIS.CO Email & Ticketing | 16 | 2 | 14 | 0 |
| UNIS ITEM- eHub integration | 10 | 3 | 7 | 0 |
| **Total** | **154** | **77** | **73** | **4** |

Net increase **10**: Infrastructure **70→77**, WCS **9→11**, eHub **9→10**; other team counts remain unchanged. All current source values/styles are used, rather than imposing prior counts or RAGs. Notable revisions include **IT Security D2 Red**, Infrastructure containing **no Red RAG cells**, updated SOC 2 task/scope narratives, **TSP closure** rows eHub 3–9 at Green/100%, and new Infrastructure/WCS/eHub workstreams. Closed TSP opportunities are preserved as closure decisions, not silently described as implemented integrations or realized savings.

Every valid identifier/project row remains, including duplicates and missing optional notes. Repeated IDs are **not deduplicated**: Infrastructure row pairs 23/24, 26/27, 35/36, 37/38, 52/53, 54/55, 62/63, 67/68, plus **WCS rows 10/11 (ID 9)**. Separate source row/index keys reconcile every record. IT Security orphan rows 6/7 lack identifier/project and remain audit evidence without invented records. Banner and formatting-only rows are excluded from records but inspected.

All **154 numeric completions** display as whole percentages; default numeric average **75%**. No text completion is present in this source, while the parser continues preserving source text such as TBD without inventing a numeric value. Narrative numbers remain source facts.

Start values: **99 calendar dates, 55 TBD**. Delivery: **11 calendar dates, 116 TBD/qualified TBD, 14 N/A, 13 text/relative estimates**. Calendar dates are faithful ISO representations; past dates, qualified targets, lead times, `TBD`, `N/A`, WCS handover wording and ongoing/relative text remain unchanged in meaning. No inferred deadlines or report-week arithmetic is used. `Source_Field_Gaps.csv` classifies all optional blanks and non-calendar estimates.

Actual direct and conditional RAG formatting produces **7 fill/font variants**: Amber 59/17/1, Green 59/9/5, Red 4. Ascending rule priority, relative formulas and per-property overrides are resolved; browser-computed badges, chart segments and KPI proportions match an independently parsed raw XLSX reader. Unsupported-extension warnings are recorded; raw XML shows extended rules are data bars outside RAG column D. Original extension bytes remain in the workbook downloads. No unsupported RAG rule was skipped, and no generic palette overrides a source cell.

## Current source-owner findings

These were rechecked from the **30 October file**, not carried forward from prior reports. They remain as supplied pending owner decisions.

| Current anchors | Finding |
|---|---|
| IT Security D2/G2 versus C2/I2/M2 | RAG cell is **Red**, M2 says **Maintain Amber**; numeric completion is **60%**, while status/progress/attention say **59%**. Dashboard uses actual D2/G2 and preserves the narratives. |
| Infrastructure & Cloud D10/D23:D24/D27 versus corresponding M cells | Cells are **Green**, while management notes explicitly say maintain/keep **Amber**. |
| Infrastructure & Cloud D28/D36/D53/D55/D62:D64 versus corresponding M cells | Cells are **Amber**, while notes retain **Red** leadership gates. No Red is inferred from the notes. |
| Infrastructure & Cloud C65/D65/G65 versus I65/J65/M65 | Completed/Green/100%, while Sparks IDF remains offline and M65 says Red until diagnosis/restoration. |
| Infrastructure & Cloud C31/D31/G31 versus I31/J31 | Completed/Green/100%, but remote desktop still fails after reinstall attempts and troubleshooting is pending. |
| Infrastructure & Cloud C32/G32 and C33/G33 versus I/J/M | Completed with **60%** and **35%**, respectively, while migration requirements or ISO scope/ownership remain unclear and work is pending. |
| Infrastructure & Cloud C5:C6, C8, C11:C12, C14:C15, C17, C19:C20, C30, C40 with G/I/J/M | Completed/100% versus still-described planning, heatmap, validation, unstarted troubleshooting, migration/optimization, SFTP requirements or support/phone resolution. These are review candidates; no closure or failure is inferred. |
| UNIS.CO Email & Ticketing D12/D17 versus M12/M17 | Both cells Green while notes say **Keep Amber** for fallback readiness or invitation reply/test behavior. Row 17 is also Completed/100% despite remaining response-path validation. |
| WCS Engineering C5/D5/G5 versus I5/L5 | “Resolved all errors” / Green/100%, while progress says errors recurred and risk text still describes recurring failures/negative economics. Source handover F5 remains unchanged. |
| WCS Engineering G8/I8/M8/N8 | G8 = **80%**; I8 dated **02-Nov-2026** says the portfolio remains **65%**; M8 says hold **80%**; N8 still cites an 18-Oct thread/65% from 12-Oct. All statements retained. |
| Infrastructure A23:A24, A26:A27, A35:A36, A37:A38, A52:A53, A54:A55, A62:A63, A67:A68; WCS A10:A11 | Repeated identifiers and overlapping narratives with differing percentages. WCS audit-program rows 10/11 report **25% versus 30%**. All valid revisions retained by source row. |
| WCS C7/G7 versus I7/J7/M7; Email C7:C9/G7:G9 versus I/J; IoT H4:H6 versus J4:J6 | Completed or 100% text coexists with remaining feature tests, notification wording, OTP/account/monitoring validation, UAT, sizing or procurement actions. |
| IoT A2 | Stale **23-Aug-2026** reporting banner/roadmap reference. Dashboard reporting week follows the selected 30 October attachment. |
| IoT N6 | Image formula cached **#NAME?**, referenced asset absent. |
| IT Security D6/N6 and D7/N7 | Orphan Green/notes without identifier/project; no record or reassignment is invented. |
| IT Compliance Program K4/K7/K9:K12/K15:K16 | Replacement-pending ownership remains in these cells. **The former IT Security pending-replacement wording is gone** and is not reported as current. |
| IT Compliance Program I14/N14 | Pickup narrative 10/8 versus notes dated 11-Sep. Relative certificate timing and chronology remain as supplied. |
| Infrastructure I4 and WCS I8 | Attachment dated 30 October contains updates explicitly as of **01-Nov** and **02-Nov**. Preserve this mixed chronology; do not silently relabel the reporting week or alter source facts. |

**Optional blank notes only:** `IoT!N8`, `IT Security!N11:N12`; all three records remain included and details show “Not provided.” These blanks are distinct from significant contradictory source statements.

**Resolved/changed prior findings:** Security row 9 is now Authorization Review/**20%**, row 11 explicitly Security Review/In Progress and row 12 Submitted/Pending Review, so the old “Completed” labels there are not carried forward. Email Phase 1 rows 5/11 now explicitly distinguish completed scope from follow-on change requests; eHub TSP rows explicitly close the declined opportunity, so future re-engagement tasks are not treated as current implementation failures. Infrastructure row 22 now documents completed Willow gateway replacement/10G upgrade; remaining post-change monitoring is not the former offline-device claim. R&D AI row 9 now records completed delivery with support-only follow-up. No QBerg/Qbert reference occurs anywhere. Source sheet names match their current subject areas.

Fresh issue evidence: `qa-local/30oct/source-issue-recheck.json`; full values/caches: `all-cell-content.txt`; every included field/excluded nonempty row: `workbook-audit.json`.

## Images and exact downloads

No media/drawing/cell-image ZIP parts or embedded images exist, so there are no image assets to extract. The only formula remains `IoT!N6`: `=_xlfn.DISPIMG("ID_BFCB287FF50949ACB47F716BD1E40440",1)`, cached `#NAME?`. Dashboard note remains neutrally **“Workbook image formula; see original workbook.”** Original formula and cache bytes are unchanged in downloads.

The exact original workbook download retains the supplied **30Oct filename**; the stable path remains `Weekly_Leadership_Source_Workbook.xlsx`. Direct HTTP and browser desktop/mobile/offline/local-upload-offline workbook downloads all match SHA-256 **`91513727651ec6c4fcad0ff8b107d56ea89aae02e420229f48dc26050e710ada`**. The branded dashboard download is self-contained with exact original XLSX bytes embedded. It loads via file:// with the browser offline and supports all filter/cascade/reset/detail/source-download checks. Downloaded HTML hashes are recorded in `QA_LOCAL_RESULTS.json`.

## Exhaustive local QA

**PASS — 32,065 Playwright assertions**. Existing Playwright **1.64.0**, Chromium **156.0.8078.4**, clean anonymous desktop **1440×1000** and mobile **390×844**. **Zero page/console errors, failed requests or HTTP error responses.** No dependencies were installed/upgraded. Static HTML/JS has no package.json/framework build/lint/typecheck; all Python scripts, workbook-reader JS and final extracted inline scripts pass syntax checks.

Independent Python cell audit plus separately parsed raw XLSX XML/style expectations reconcile every source row/index/order, detail field, table field, delivery/date/text, whole completion/average, RAG fill/font, KPI/share and chart count/style/proportion. Duplicate source identifiers are retained, and optional-note records have explicit inclusion evidence.

All **36 Team/RAG states** are covered: **27 reachable states**, **15 specific team/RAG pairs**, **9 unavailable pairs** excluded from options. All **24 cascading transitions** verify applicable selection preservation or reset plus resulting rows/KPIs. The suite repeats on mobile and the offline downloaded dashboard. Search, summary-card filtering, reset, visible empty states, modal/keyboard interaction and internal table scrolling without page overflow pass.

New explicit readability checks verify **exact worksheet names** in every table row and dropdown option, the selected full name fits the dropdown, and all chart worksheet labels wrap without clipping. These checks run on desktop, mobile and offline; no UI truncation was found, so no layout redesign was necessary. Additional mobile evidence: `mobile-full-team-name.png`, `mobile-team-chart.png`. Desktop/mobile/detail/name screenshots were visually inspected.

Both real browser download buttons, original filenames and visible download feedback pass. Browser-only local uploads verify missing week, loading/disabled controls, success, invalid-file errors and preservation of the last valid in-memory snapshot. No operational-system writes or live upload tests occurred. Local HTTP page/workbook return 200; arbitrary Host headers return identical HTML.

Full ignored evidence: **`qa-local/30oct/`** — `qa-results.json`, independent `workbook-audit.json`, inventories, issue evidence, screenshots, exact downloaded artifacts, HTTP/Host receipts and extracted scripts. Tracked summary: `QA_LOCAL_RESULTS.json`. Originals and historical report-copy hashes are unchanged; generator output is byte-idempotent. Transient outputs and secrets are excluded from the commit.

The temporary server was **stopped and awaited**, and port 3000 is closed. No local QA failure remains.

## Publishing and handoff

Preserve **GitHub Pages, `main`, repository root `/`**, generated **pages-build-deployment** workflow (`dynamic/pages/pages-build-deployment`, ID `357658072`): Jekyll build → artifact upload → deploy. Existing host/repo/URL and branding remain unchanged. Historical run **40466318754** successfully published commit 9250e6b; its prior 26 October live PASS is preserved separately.

The coordinator owns authenticated resolver confirmation, native ibisGitTool push, and post-publication exact HTML/source plus live browser verification. This run performs none of those remote operations. Ready to publish the local refresh, with the current source-owner findings above retained as evidence.

Application directory: **`/home/user/workspace/it-leadership-dashboard`**. Optional managed-preview command, port **3000**:

```bash
python -m http.server 3000 --bind 0.0.0.0 --directory /home/user/workspace/it-leadership-dashboard
```

Verification server exited before handoff.
