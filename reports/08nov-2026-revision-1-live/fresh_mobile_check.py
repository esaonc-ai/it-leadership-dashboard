from pathlib import Path
from playwright.sync_api import sync_playwright
from collections import Counter
from datetime import datetime,timezone
import json,hashlib
out=Path('qa-public/08nov-2026-revision-1');audit=json.loads((out/'workbook-audit.json').read_text());checks=[];errors=[];failures=[]
def check(ok,label):
 assert ok,label
 checks.append(label)
def observe(page):
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None)
 page.on('requestfailed',lambda r:failures.append(r.url))
 page.on('response',lambda r:failures.append(str(r.status)+' '+r.url) if r.status>=400 else None)
with sync_playwright() as p:
 browser=p.chromium.launch(args=['--no-sandbox']);context=browser.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True,accept_downloads=True);page=context.new_page();observe(page)
 response=page.goto('https://esaonc-ai.github.io/it-leadership-dashboard/',wait_until='networkidle');check(response.status==200,'Fresh anonymous mobile HTTP 200');check(not context.cookies(),'No cookies or auth state')
 records=page.evaluate('records');teams=sorted(set(r['team'] for r in records));rags=['Amber','Green'];matrix=[];cascades=[]
 def view(expected):
  check(page.locator('select').count()==2,'Exactly one TEAM and one RAG')
  actual=page.locator('#rows tr').evaluate_all('es=>es.map(e=>({index:Number(e.dataset.recordIndex),cells:Array.from(e.cells).map(c=>c.innerText),fill:getComputedStyle(e.querySelector(".badge")).backgroundColor}))')
  check(len(actual)==len(expected),'Count reconciled')
  for a,r in zip(actual,expected):
   check(a['index']==r['index'] and a['cells'][1]==r['team'],'Source row and full TEAM')
   check(a['cells'][2]==r['rag'],'Source RAG')
   check(a['fill']=='rgb('+', '.join(str(int(r['ragFill'][i:i+2],16)) for i in (1,3,5))+')','Effective source fill')
   check(a['cells'][3]==(str(r['completion'])+'%' if r['completion'] is not None else r['completionSource'] or 'Not provided'),'Whole percentage / exact text')
   check(a['cells'][4]==(r['finish'] or 'Not provided'),'Exact delivery text')
 for team in ['']+teams:
  page.click('#clear');page.select_option('#team',team)
  available=page.locator('#rag option').evaluate_all('es=>es.map(e=>e.value)')
  for rag in ['','Red','Amber','Green']:
   expected=[r for r in records if (not team or r['team']==team) and (not rag or r['rag']==rag)]
   check((rag in available)==(not rag or bool(expected)),'Cascading options source-faithful')
   matrix.append({'team':team,'rag':rag,'available':rag in available,'records':len(expected)})
   if rag in available:page.select_option('#rag',rag);view(expected)
 for team in teams:
  for rag in rags:
   page.click('#clear');page.select_option('#rag',rag);page.select_option('#team',team)
   matching=[r for r in records if r['team']==team and r['rag']==rag];selected=rag if matching else ''
   check(page.locator('#rag').input_value()==selected,'Cascade resets unavailable RAG');view(matching or [r for r in records if r['team']==team]);cascades.append([team,rag])
 page.click('#clear');page.locator('.grid').screenshot(path=str(out/'mobile-health.png'))
 page.select_option('#team','UNIS ITEM- eHub integration');page.locator('#team').scroll_into_view_if_needed();page.screenshot(path=str(out/'mobile-full-team.png'))
 page.click('#clear');page.select_option('#team','WCS Engineering');page.select_option('#rag','Green');view([r for r in records if r['team']=='WCS Engineering' and r['rag']=='Green'])
 for row in (7,8,11):
  record=next(r for r in records if r['team']=='WCS Engineering' and r['sourceRow']==row);page.locator(f'tr[data-record-index="{record["index"]}"]').click();check(page.locator('#detail').inner_text().find(record['attention'])>=0,'Changed Green record retains Amber source directive')
  if row==7:page.screenshot(path=str(out/'mobile-revision-rag-conflict.png'))
  page.click('#close')
 page.click('#clear');page.select_option('#team','IT Security');page.locator('tr[data-record-index="2"]').click();page.screenshot(path=str(out/'mobile-conditional-color.png'));page.click('#close')
 check(page.evaluate('document.documentElement.scrollWidth<=innerWidth'),'No page overflow')
 context.close()
 offline=browser.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True,accept_downloads=True,offline=True);page=offline.new_page();observe(page);page.goto((out/'dashboard.html').resolve().as_uri());view(records);check(not offline.cookies(),'Fresh mobile offline no auth');page.select_option('#team','WCS Engineering');page.select_option('#rag','Green');view([r for r in records if r['team']=='WCS Engineering' and r['rag']=='Green'])
 with page.expect_download() as dl:page.click('#downloadWorkbook')
 dl.value.save_as(out/'fresh-mobile-offline-workbook.xlsx');check(hashlib.sha256((out/'fresh-mobile-offline-workbook.xlsx').read_bytes()).hexdigest()==audit['sourceSha256Before'],'Fresh mobile offline workbook exact bytes')
 check(not errors,'Zero console/page errors');check(not failures,'Zero request failures');browser.close()
result={'status':'PASS','verifiedAtUtc':datetime.now(timezone.utc).isoformat(),'url':'https://esaonc-ai.github.io/it-leadership-dashboard/','scope':'Independent fresh mobile context plus separate fresh mobile offline context; no reused storage/auth','passedAssertions':len(checks),'matrix':matrix,'cascades':cascades,'sourceSha256':audit['sourceSha256Before'],'browserErrors':errors,'failedRequests':failures}
(out/'fresh-mobile-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ('matrix','cascades')},indent=2))
