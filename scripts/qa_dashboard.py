#!/usr/bin/env python3
"""Browser QA of public or standalone dashboard; expected RAG formatting parsed independently from raw XLSX XML in JS, not generated payload."""
import argparse, json, hashlib, re
from pathlib import Path
from collections import Counter
from playwright.sync_api import sync_playwright

parser=argparse.ArgumentParser();parser.add_argument('url');parser.add_argument('--output',default='qa');args=parser.parse_args();out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
source=next(Path.cwd().glob('IT_Project_Portfolios*12Oct*.xlsx'));sha=hashlib.sha256(source.read_bytes()).hexdigest();errors=[];checks=[]
def check(condition,label):
 if not condition:raise AssertionError(label)
 checks.append(label)
def rgb(hex):return 'rgb('+', '.join(str(int(hex[i:i+2],16)) for i in (1,3,5))+')'
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,args=['--no-sandbox']);context=browser.new_context(accept_downloads=True,viewport={'width':1440,'height':1000});page=context.new_page();page.on('pageerror',lambda e:errors.append(str(e)));page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None)
 response=page.goto(args.url,wait_until='networkidle');check(response is None or response.status==200,'Anonymous page returns 200 without login');check(page.locator('h1').inner_text()=='IT Program Leadership Dashboard','Branding preserved');check('Oct 12, 2026' in page.locator('#reportMeta').inner_text(),'Current weekly build is served');check(page.evaluate('dashboardData.sourceSha256')==sha,'Deployed embedded workbook hash equals attachment')
 expected=page.evaluate("()=>parseWeeklyWorkbook(Uint8Array.from(atob(dashboardData.sourceWorkbookBase64),c=>c.charCodeAt(0)))");actual=page.evaluate('records');check(len(expected)==len(actual)==128,'Independent source reconciliation: 128 valid records')
 for a,e in zip(actual,expected):
  for key in a:
   if key=='completionSource' and a['completion'] is not None:continue
   check(a[key]==e[key],f"{a['team']} row {a['sourceRow']}: {key} reconciled")
 check(Counter(x['rag'] for x in expected)=={'Amber':78,'Green':48,'Red':2},'78 Amber / 48 Green / 2 Red reconciled')
 def assert_view(selected):
  check(page.locator('select').count()==2,'Exactly two dropdowns retained after filtering')
  rows=page.locator('#rows tr');check(rows.count()==len(selected),'Filtered record count')
  for i,r in enumerate(selected):
   badge=rows.nth(i).locator('.badge');check(badge.inner_text()==r['rag'],'Exact canonical RAG label');check(badge.evaluate('(el)=>getComputedStyle(el).backgroundColor')==rgb(r['ragFill']),'Computed badge fill matches independently evaluated XLSX formatting');check(badge.evaluate('(el)=>getComputedStyle(el).color')==rgb(r['ragFont'] or '#000000'),'Computed badge font matches independently evaluated XLSX formatting');cells=rows.nth(i).locator('td');check(cells.nth(3).inner_text()==(str(r['completion'])+'%' if r['completion'] is not None else r['completionSource'] or 'Not provided'),'Whole-number percentage or unchanged source text');check(cells.nth(4).inner_text()==(r['finish'] or 'Not provided'),'Estimated delivery date preserved')
  bars=page.locator('.bar');bar_total=0
  for bar in bars.all():
   fill=bar.get_attribute('data-rag-fill');check(bar.evaluate('(el)=>getComputedStyle(el).backgroundColor')==rgb(fill),'Computed chart segment fill matches source');bar_total+=int(bar.get_attribute('data-count'))
  check(bar_total==len(selected),'Chart segment totals reconcile')
  for row in page.locator('.bar-row').all():
   team=row.locator('.bar-label').inner_text(); expected_segments=Counter((r['rag'],r['ragFill'],r['ragFont']) for r in selected if r['team']==team)
   actual_segments=Counter((b.get_attribute('data-rag'),b.get_attribute('data-rag-fill'),int(b.get_attribute('data-count'))) for b in row.locator('.bar').all())
   check(actual_segments==Counter((rag,fill,count) for (rag,fill,font),count in expected_segments.items()),'Named chart segment styles and counts match independent XML expectations')
  cards=page.locator('.kpi');check(cards.nth(0).locator('.num').inner_text()==str(len(selected)),'Visible-record KPI reconciles')
  for card in cards.all()[1:]:
   rag=card.get_attribute('data-rag-filter');subset=[r for r in selected if r['rag']==rag];check(card.locator('.num').inner_text()==str(len(subset)),'RAG KPI reconciles');check(card.locator('.percent').inner_text()==str(int(len(subset)/len(selected)*100+0.5))+'%','Whole-number RAG percentage');gradient=card.evaluate('(el)=>getComputedStyle(el).backgroundImage');counts=Counter(r['ragFill'] for r in subset)
   for fill in counts:check(rgb(fill) in gradient,'KPI retains all represented source-fill variants')
   stops=re.findall(r'rgb\(\d+, \d+, \d+\) (\d+(?:\.\d+)?)%',gradient)
   expected_stops=[];offset=0
   for fill,count in counts.items():expected_stops.extend([offset,offset+count/len(subset)*100]);offset+=count/len(subset)*100
   check(len(stops)==len(expected_stops) and all(abs(float(a)-b)<0.001 for a,b in zip(stops,expected_stops)),'KPI color-strip proportions match source-color counts')
  check(not re.search(r'\b\d+\.\d+%',page.locator('body').inner_text()),'No displayed fractional percentages')
 assert_view(expected)
 combinations=[]
 for team in sorted(set(r['team'] for r in expected)):
  page.select_option('#team',team);options=page.locator('#rag option').evaluate_all('(opts)=>opts.map(o=>o.value).filter(Boolean)');rags=set(r['rag'] for r in expected if r['team']==team);check(set(options)==rags,'Team → RAG applicable values')
  page.select_option('#rag','');assert_view([r for r in expected if r['team']==team])
  for rag in options:
   page.select_option('#rag',rag);assert_view([r for r in expected if r['team']==team and r['rag']==rag]);combinations.append([team,rag])
 page.select_option('#team','Infrastructure & Cloud');page.select_option('#rag','Red');page.select_option('#team','IoT');check(page.locator('#rag').input_value()=='','Inapplicable prior RAG resets when team changes')
 page.click('#clear')
 check(page.locator('select').count()==2 and page.locator('#team').count()==1 and page.locator('#rag').count()==1,'Exactly one Team dropdown and one RAG dropdown, no duplicates');page.locator('[data-rag-filter="Amber"]').click();check(page.locator('#rows tr').count()==78,'RAG card click functional');page.click('#clear')
 for r in expected:
  page.locator(f'tr[data-record-index="{r["index"]}"]').click();check(page.locator('#modalTitle').text_content()==r['project'],'Record detail opens');check(page.locator('#detail').inner_text().find('Estimated delivery date')>=0,'Details contain estimated delivery date');page.click('#close')
 page.fill('#search','__NO_MATCH_QA_9351__');check(page.locator('#rows tr').count()==0,'No-match filter has no blank records');check(not page.locator('#cards').is_visible() and not page.locator('.grid').is_visible() and not page.locator('table').is_visible(),'Empty panels suppressed in actual browser');page.click('#clear');check(page.locator('#rows tr').count()==128 and page.locator('.grid').is_visible(),'Panels return when filters cleared')
 page.screenshot(path=str(out/'desktop.png'),full_page=False)
 for button,filename in [('#downloadWorkbook','public-workbook.xlsx'),('#downloadDashboard','dashboard.html')]:
  with page.expect_download() as download:page.click(button)
  download.value.save_as(out/filename)
 check(hashlib.sha256((out/'public-workbook.xlsx').read_bytes()).hexdigest()==sha,'Triggered public workbook download is byte-identical')
 offline=context.new_page();offline.on('pageerror',lambda e:errors.append(str(e)));context.set_offline(True);offline.goto((out/'dashboard.html').resolve().as_uri());check(offline.locator('#rows tr').count()==128,'Downloaded dashboard opens offline without external dependencies');check(offline.locator('select').count()==2,'Downloaded standalone dashboard also has only Team and RAG dropdowns')
 with offline.expect_download() as dl:offline.click('#downloadWorkbook')
 dl.value.save_as(out/'offline-workbook.xlsx');check(hashlib.sha256((out/'offline-workbook.xlsx').read_bytes()).hexdigest()==sha,'Offline dashboard workbook download is byte-identical');context.set_offline(False)
 # Local future-week upload proves bytes/payload change only after valid parsing.
 page.fill('#uploadWeek','2026-10-19');page.set_input_files('#uploadWorkbook',source);page.wait_for_function("dashboardData.reportDate==='2026-10-19'");check('Oct 19, 2026' in page.locator('#reportMeta').inner_text(),'Future-week workbook upload supported');check(page.evaluate('dashboardData.records.length')==128,'Uploaded compatible source sheets discovered');
 with page.expect_download() as dl:page.click('#downloadDashboard')
 dl.value.save_as(out/'uploaded-dashboard.html');offline.goto((out/'uploaded-dashboard.html').resolve().as_uri());check('Oct 19, 2026' in offline.locator('#reportMeta').inner_text(),'Downloaded uploaded snapshot retains its reporting week');
 with offline.expect_download() as dl:offline.click('#downloadWorkbook')
 dl.value.save_as(out/'uploaded-workbook.xlsx');check(hashlib.sha256((out/'uploaded-workbook.xlsx').read_bytes()).hexdigest()==sha,'Uploaded snapshot downloads original bytes')
 invalid=out/'invalid.xlsx';invalid.write_bytes(b'not a workbook');before=page.evaluate('dashboardData.sourceSha256');page.set_input_files('#uploadWorkbook',invalid);page.wait_for_function("document.getElementById('statusMessage').textContent.startsWith('Workbook not loaded:')");check(page.evaluate('dashboardData.sourceSha256')==before,'Invalid upload does not replace workbook payload')
 page.goto(args.url,wait_until='networkidle');page.set_viewport_size({'width':390,'height':844});page.screenshot(path=str(out/'mobile.png'));check(page.locator('#downloadWorkbook').is_visible(),'Mobile download actions visible');check(not errors,'No browser console/page errors');check(hashlib.sha256(source.read_bytes()).hexdigest()==sha,'Original attachment remains unchanged')
 browser.close()
summary={'url':args.url,'sourceSha256':sha,'records':128,'rags':dict(Counter(r['rag'] for r in expected)),'teamRagCombinations':combinations,'dropdowns':{'Team':1,'RAG':1,'total':2},'passedAssertions':len(checks),'browserErrors':errors,'status':'PASS'};(out/'qa-results.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
