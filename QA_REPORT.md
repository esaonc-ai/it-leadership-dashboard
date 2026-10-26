# IT & Technology Program Leadership Dashboard — 26 October 2026 latest attachment (_4) local refresh

## Repository and scope

Refreshed the existing checkout `/home/user/workspace/it-leadership-dashboard`, branch `main`, starting at `bfbc8d5d6e725d6900702be56e9db99c407791d7`. Repository `esaonc-ai/it-leadership-dashboard` and public URL https://esaonc-ai.github.io/it-leadership-dashboard/ are retained. Branding remains exactly **IT & Technology Program Leadership Dashboard**. This is a weekly snapshot, with no prior-week records added and no new app/provider.

No remote Git operations, push, deployment or workflow dispatch occurred. The local commit is intended for coordinator review and ibisGitTool publication after its resolver step. Public QA for this refresh remains NOT RUN; the historical public results are explicitly labeled in `QA_PUBLIC_RESULTS.json`.

## Source selection, revision comparison and integrity

Selected **IT & Technology Project_Portfolios_2026_v1.0 (26Oct2026 PST)_4.xlsx**, the newest explicitly supplied revision at the newest available reporting date, **26 October 2026**. Inventoried all workbook files in the workspace/repo and compared all five supplied same-date originals. Ignored QA-generated downloads as source candidates. The interrupted `_3` attempt left only an uncommitted comparison report; the starting dashboard still selected `_2`. This refresh selects `_4` and preserves its exact supplied download filename.

| Candidate | Bytes | SHA-256 before and after comparison/QA |
|---|---:|---|
| First supplied 26Oct2026 workbook | 76,511 | `0a9a5517d6d29304d894b840e197eb562314ac29327d304090e591dec759227c` |
| Earlier `_1.xlsx` | 76,511 | `0a9a5517d6d29304d894b840e197eb562314ac29327d304090e591dec759227c` |
| Earlier `_2.xlsx` | 76,509 | `d7b84baae22203c06aa7e9bdc98a8dd57fb3c9e9524bfa5f206e4578546606a5` |
| Earlier `_3.xlsx` | 76,509 | `d7b84baae22203c06aa7e9bdc98a8dd57fb3c9e9524bfa5f206e4578546606a5` |
| **Latest `_4.xlsx` — selected** | **76,509** | `d7b84baae22203c06aa7e9bdc98a8dd57fb3c9e9524bfa5f206e4578546606a5` |

**`_4`, `_3` and `_2` are byte-identical.** The first upload and `_1` are also byte-identical to one another. Comparing `_4` with either of those first two finds **15 changed ZIP XML parts**: core properties, styles, workbook metadata, four table definitions and all eight worksheets. These differences carry forward the metadata, style-reference remapping and conditional-rule serialization changes already inspected for `_2`; the previously recorded raw XML diff remains at `qa-local/26oct-revision2/raw-part-diff.txt`.

Fresh comparison finds **zero differences** across all five sources in raw cell values/types (including whitespace), formulas and cached results, resolved direct font/fill/border/alignment/protection/number formatting, priority-ordered conditional rules with resolved differential styles, or effective RAG appearance. No business data changed in the latest upload. Full current comparison: `SOURCE_COMPARISON.json`; five complete cell/style/ZIP inventories are in `qa-local/26oct-revision4/`.

All eight sheets and all 1,569 populated/styled cells in each revision were read. Source findings were freshly extracted from `_4`, including cached formula values, into `qa-local/26oct-revision4/source-issue-recheck.json`; complete cell content is in `all-cell-content.txt`. The 18 October comparison is historical context retained in commit `1a38e44`, not a newly supplied source candidate.

The selected bytes are copied directly to `Weekly_Leadership_Source_Workbook.xlsx` and embedded unchanged in `index.html`. All **91 records are identical** to the starting local commit; only the supplied filename changes in the dashboard. Refresh generation is byte-idempotent. No uploaded original was modified or re-saved through an Excel library; **all five initial hashes remain unchanged after QA**.

The user's permission to change the source workbook is acknowledged. No specific factual corrections were supplied, so conflicting statuses/percentages, sheet groupings, ownership and date narratives remain exactly as uploaded for user decisions. Permission alone is not treated as an instruction to guess business facts.

The direct HTTP workbook, desktop download, mobile download, offline download and locally uploaded/offline download all have selected SHA-256 **d7b84baae22203c06aa7e9bdc98a8dd57fb3c9e9524bfa5f206e4578546606a5**. The original formula/cache content and all extended formatting XML remain intact in the downloads.

## Full workbook inspection and record reconciliation

Read all eight worksheets and every cell, including formulas, cached values, styles, banners, orphan fragments and formatted empty cells. All sheets are visible; there are no additional hidden sheets. Each supplied revision has 1,569 populated or styled cells inventoried. IoT headers are on row 3; every other sheet uses row 1. Headers map A:N consistently to identifier, project, status, RAG, start, delivery, completion, objective, progress, next steps, owner, risks, attention and source/notes.

| Source team/sheet | Records | Amber | Green | Red | Included rows |
|---|---:|---:|---:|---:|---|
| IT Security | 9 | 3 | 6 | 0 | 2–5, 8–12 |
| Infrastructure & Cloud | 10 | 8 | 2 | 0 | 2–11 |
| IoT | 5 | 0 | 5 | 0 | 4–8 |
| R&D AI | 9 | 0 | 9 | 0 | 2–10 |
| WCS Engineering | 9 | 7 | 2 | 0 | 2–10 |
| IT Compliance Program | 17 | 13 | 0 | 4 | 2–18 |
| UNIS.CO Email & Ticketing | 16 | 3 | 13 | 0 | 2–17 |
| UNIS ITEM- eHub integration | 16 | 15 | 1 | 0 | 2–17 |
| **Total** | **91** | **49** | **38** | **4** | |

Valid records require an identifier and project. Missing optional notes do not remove records: IT Security rows 11/12 and IoT row 8 remain visible. IT Security rows 6/7 contain only RAG/notes fragments and no identifier/project, so they are recorded as orphan source content without inventing records or ownership. IoT banner rows and R&D AI formatting-only rows 11–21 are inventoried without becoming records. The 18 October count of 133 is not imposed.

The source sheet **Compliance Program** is now named **IT Compliance Program**. Infrastructure & Cloud drops from 63 infrastructure records to 10 robotics/WCS records; none of its previous exact project titles remain there. Its rows 2–9 duplicate the corresponding WCS Engineering A:N values, while row 10 is a different equipment-audit revision (30% versus WCS 25%), and row 11 is the forklift-scale workstream. The eHub-named sheet replaces all nine prior shipping/eHub project titles with 16 compliance workstreams. These are material source changes requiring source-owner review; the dashboard preserves the supplied teams/records without restoring, moving, deduplicating or merging prior entries.

### Dates, percentages and effective appearance

There are **90 numeric completion values and one text completion**: `UNIS ITEM- eHub integration!G8 = TBD`. The text remains visible in table/details, stays out of numeric averages, and its record is retained. The audit previously assumed all completions were numeric; it now explicitly validates text/missing completions. Numeric values display as whole percentages. The default numeric average is **70%**.

Start values: **64 calendar dates, 27 TBD**. Delivery values: **3 calendar dates, 74 TBD/qualified TBD, 4 N/A, 10 text/relative estimates**. Calendar dates display as ISO dates with their meaning intact; both source date representations remain unchanged in the downloadable workbook. The three calendar delivery cells are IT Compliance Program F4, eHub F4 (both 2027-01-20) and Email & Ticketing F10 (2026-08-31).

Preserved text includes Infrastructure & Cloud and WCS Engineering F4's conditional **04-Dec-2026** onsite target, F6's **5–6-week lead time after signed approval**, F8's separate **31-Oct-2026 test target and early-December deployment**, their differing F10 ongoing/post-peak estimates, and R&D AI F3/F5/F6/F7's **4 weeks / 3–4 weeks / 2 weeks / Ongoing / No ETA**. No report-date arithmetic, inferred deadline, blank replacement date or invented percentage is introduced. All uncertain/date-text cells and missing notes are listed in `Source_Field_Gaps.csv`.

Effective RAG styles are resolved using actual direct formatting plus conditional-rule priority, translated relative formulas and per-property overrides, not a generic RAG palette. Seven fill/font variants occur: 41/5/3 Amber variants, 24/9/5 Green variants, and 4 Red. Badges, chart segments and KPI strips match source styles, including IoT's distinct pale Green and the new Amber font variant. The independently read raw XLSX XML is compared with both embedded data and browser-computed fill/font values for every displayed row/state. No visible style legend, raw color strings or “Source RAG styles” heading appears.

Openpyxl warns about unsupported extensions; raw XML inspection shows the extended conditional rules are data bars on F/G/K, not RAG D. The original extension XML is preserved in the exact-byte source downloads. No unsupported RAG rule was ignored.

### Images and formula/cache inspection

There are **no embedded image/media/drawing/cell-image parts** in any of the five supplied workbook ZIPs, and openpyxl finds no sheet image objects. Therefore there is no image to extract and no extracted-image path to report. The only formula is **IoT N6**, `=_xlfn.DISPIMG("ID_BFCB287FF50949ACB47F716BD1E40440",1)`, with cached **#NAME?**. Its referenced image asset is absent. The dashboard uses the neutral note **“Workbook image formula; see original workbook”** rather than claiming an embedded image exists. Formula/cache bytes remain unchanged in the XLSX. Full local evidence includes five complete JSON inventories and `all-cell-content.txt`.

## Source issues requiring source-owner decisions: freshly checked cells

These observations were rechecked against the latest `_4.xlsx` cells and cached values. All remain unchanged; none is silently corrected in the dashboard.

| Cells | Current finding |
|---|---|
| IoT A2 | Still says reporting date **2026-08-23** and cites the 23Aug roadmap. Dashboard weekly date comes from the selected 26Oct attachment. |
| IoT N6 | Image formula, cached #NAME?, no embedded image asset. |
| IT Security D6/N6, D7/N7 | Green/meeting-note fragments without identifier/project. No workstream or note reassignment is invented. |
| IT Security K2:K5, K10 | Replacement-pending ownership wording remains. |
| IT Compliance Program K2, K4, K7, K9:K12, K15:K16 | Replacement-pending owner wording remains. The old Infrastructure pending-owner list no longer applies because that sheet's contents changed. |
| IT Compliance Program I3/I13 | Prior awkward “replacement pending left before completing” wording is **gone**. Current narratives describe Mike's departure, incomplete scoping, the TSC mismatch and pending audit assignment. |
| Infrastructure & Cloud I64 | **No longer present**: sheet ends at row 11. No QBerg/Qbert reference occurs anywhere in the current workbook. No historical text is added back. |
| Infrastructure & Cloud B2:N11; WCS Engineering B2:N10 | Robotics/WCS content now appears in Infrastructure & Cloud too. Rows 2–9 are duplicates; equipment-audit row 10 has different completion and narrative revisions. Source grouping and both revisions are retained. |
| UNIS ITEM- eHub integration B2:N17 | Sheet name indicates eHub, but contents are compliance workstreams. All nine prior shipping/eHub titles are absent. This sheet and IT Compliance Program hold different versions of overlapping work, e.g. GDPR G8/I8 is TBD/not set up versus 48%/Vanta preparation active. |
| IT Security C2/I2/M2 versus G2 | Narrative reports **59%**, while numeric completion is **60%**. Both remain visible as supplied. |
| Infrastructure & Cloud and WCS Engineering G8 versus I8/N8 | Numeric completion is **80%**, but narrative/notes say the latest explicit owner-reported completion was **65%** and no revised numeric percentage was supplied. |
| UNIS.CO Email & Ticketing C17/D17/G17 versus J17/M17 | Completed / Green / 100%, while response-path validation remains in next steps and M17 says **“Keep Amber”** until reply behavior is resolved or accepted. Effective D17 Green is preserved. |
| IT Security C9/G9 versus I9/J9/M9 | Completed/100%, while ownership, authorization and group-restricted access actions remain documented as open. |
| IT Security C10/G10 versus I10/J10 | Inventory/Compatibility Review and 100%, while endpoint population is not yet known and export/testing/planning remain in next steps. |
| IT Security C11/G11 versus I11/J11/M11 | Completed/100%, while dedicated licensed-account and unattended-use controls remain in next steps. |
| IT Security C12/G12 versus I12/J12/M12 | Completed/100% tasks submitted for initial review, while reviewer follow-up and final acceptance remain tracked. |
| Infrastructure & Cloud and WCS Engineering C7/G7 versus I7/J7/M7 | Completed/100%, while feature testing, general release and notification wording remain open. The old Infrastructure row-32 example no longer exists. |
| UNIS.CO Email & Ticketing C5/G5, I5/J5/M5; C7/G7, I7/J7; C8/G8, I8/J8; C9/G9, I9/J9/M9 | Completed/100% coexists with routing/pilot acceptance, delivery validation, account identification or monitoring-confirmation actions. Routine governance-only completed rows are not treated as contradictions. |
| UNIS ITEM- eHub integration C9/G9 versus I9/J9 | “Not Fully Closed” and 100%, while data inventory review/build actions remain. |
| IoT H4:H6 versus J4:J6 | Completed objective text coexists with UAT, selection/sizing or procurement next steps. D8/G8 remains Green/20%; all IoT F4:F8 are now TBD. |
| IT Compliance Program I14/N14; eHub I14/N14 | Compliance narrative refers to pickup on 10/8 while notes cite 11-Sep; the eHub version says “last Thursday.” Dates and relative wording are retained without resolving the chronology. |

**Blank optional fields:** `IoT!N8` and `IT Security!N11:N12` have no notes. These are not contradictory business facts; all three records are retained and details show “Not provided.” `UNIS ITEM- eHub integration!G8` contains the explicit text `TBD`, which remains text and is excluded from numeric averages.

Detailed source audit, every included row/field, excluded nonempty rows, formulas/caches, warnings and extension ranges: `qa-local/26oct-revision4/workbook-audit.json`. Complete values/styles and raw ZIP-part hashes: the `*-inventory.json` files. No source issue is presented as a dashboard-derived change of ownership, deadline, status or RAG.

## Local QA evidence

**PASS — 18,238 Playwright assertions**, Playwright 1.64.0 / Chromium 156.0.8078.4, desktop **1440×1000** and mobile **390×844**, anonymous context with no login cookies. No browser page/console errors, failed network requests or HTTP error responses. Syntax checks pass for every Python script, the XLSX JS reader and every inline script extracted from the final HTML. The app is plain static HTML/JavaScript: no package.json, framework build, lint or typecheck command applies. No dependency was installed or upgraded for this revision; existing Playwright tooling was reused.

The Python audit independently reconciles every record and mapped source cell. Browser expectations separately parse raw source XLSX XML and effective styles, then reconcile every field, visible row, source order, row count, RAG KPI, whole-number share, chart segment/style/count, numeric average, delivery estimate and all record details. The three missing-note records and the text completion have explicit evidence in `QA_LOCAL_RESULTS.json`.

The suite covers the **36-state matrix**: All/8 teams × All/Red/Amber/Green. **26 states are available**, including 14 specific team/RAG pairs; **10 impossible pairs are absent from cascading options**. Every reachable state reconciles visible rows/KPIs to the independent source. All 24 changes from globally selected RAGs into teams verify preservation/reset and rows/KPIs. The filtering suite repeats on the downloaded dashboard with the browser context offline and on mobile. Reset, source-name/branding metadata, search, summary-card filtering, empty panels, keyboard/modal interactions and mobile overflow are checked.

Both browser download buttons are exercised. Suggested filenames preserve the exact source name and current dashboard branding. Source download bytes are verified for direct HTTP, desktop, mobile, offline and a differently named local upload's offline snapshot. The standalone HTML loads via file:// with the context offline, runs all filter/cascade checks and downloads the unchanged XLSX. Local uploads exercise missing reporting week, visible loading/disabled inputs, success, invalid-workbook errors and preservation of the valid snapshot. These are in-browser file operations; no operational-system write tests ran.

Read-only HTTP checks return **200** for the page and workbook; arbitrary preview/deployment Host headers also return 200 and the same HTML bytes. Desktop/mobile screenshots were visually inspected. Evidence remains in ignored `qa-local/26oct-revision4/`: `qa-results.json`, `workbook-audit.json`, `desktop.png`, `mobile.png`, `mobile-detail.png`, `http.json`, `host-checks.json`, `page-snapshot.html`, `dashboard.html`, `uploaded-dashboard.html` and downloaded XLSX files. Tracked digest and integrity summary: `QA_LOCAL_RESULTS.json`. Transient screenshots, full source inventories, temporary invalid file and downloaded artifacts are excluded from the commit.

## Existing Pages publishing and handoff

The existing mechanism is **GitHub Pages from `main`, `/` (repository root)**, using GitHub's generated **`pages-build-deployment`** workflow, ID **357658072**, path **`dynamic/pages/pages-build-deployment`**. Its observed jobs are **Jekyll build → upload Pages artifact → report build status → deploy to GitHub Pages**. There is no checked-in workflow, `docs/` app, CNAME change or alternate deployment provider.

Previously captured read-only public API receipts show successful run **39203610844**, deployment **7166266769**, branch/ref **main**, starting SHA **6fc6adaff019009492e2f7d6864c1f11542a8c56**. At that historical check, public HTML was byte-identical to the original checkout's root `index.html`; this and the root-only repository tree established the served source path. This latest refresh was not checked against the live site as if deployed. Evidence: `qa-local/26oct/pages-readonly-evidence.json` (historical receipt from the previous local refresh; not re-fetched). The historical anonymous Pages settings/build requests returned 404, so the root setting is established from published content/workflow evidence, rather than a fresh authenticated settings response. The coordinator must use its resolver to confirm current branch/path settings before publication, as requested.

After review, the coordinator uses **ibisGitTool** to reconcile/push the local commit to this same repository's **main** branch; the existing Pages workflow then handles publication at the unchanged URL. The coordinator should verify the resulting Pages SHA and anonymous HTML/workbook hashes after that publication. No push or deployment has been performed here. The authorization blocker remains for the coordinator; local content/QA is ready for its resolver and push retry, subject to the documented source-owner caveats.

Application directory: **`/home/user/workspace/it-leadership-dashboard`**. Exact managed-preview command, **port 3000**:

```bash
python -m http.server 3000 --bind 0.0.0.0 --directory /home/user/workspace/it-leadership-dashboard
```

The temporary local QA server was stopped and awaited before handoff. Source caveats remain for workbook-owner review; local dashboard QA has no outstanding failures.
