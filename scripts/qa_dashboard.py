#!/usr/bin/env python3
"""Anonymous browser QA against independently read source XLSX cells and XML styles."""
import argparse
import base64
import hashlib
import json
import re
from collections import Counter
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import urljoin

from playwright.sync_api import sync_playwright

parser = argparse.ArgumentParser()
parser.add_argument('url')
parser.add_argument('--workbook', type=Path, required=True)
parser.add_argument('--report-date', required=True)
parser.add_argument('--audit', type=Path, default=Path('qa-local/workbook-audit.json'))
parser.add_argument('--output', type=Path, default=Path('qa-local'))
args = parser.parse_args()
out = args.output
out.mkdir(parents=True, exist_ok=True)
source = args.workbook.resolve()
sha = hashlib.sha256(source.read_bytes()).hexdigest()
audit = json.loads(args.audit.read_text())
reader = (Path(__file__).parent / 'workbook_reader.js').read_text()
errors, checks, failures, combinations, cascade_cases = [], [], [], [], []


def check(condition, label):
    if not condition:
        raise AssertionError(label)
    checks.append(label)


def rgb(value):
    return 'rgb(' + ', '.join(str(int(value[i:i + 2], 16)) for i in (1, 3, 5)) + ')'


def observe(page):
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
    page.on('requestfailed', lambda r: failures.append({'url': r.url, 'failure': r.failure}))
    page.on('response', lambda r: failures.append({'url': r.url, 'status': r.status}) if r.status >= 400 else None)


try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
        context = browser.new_context(accept_downloads=True, viewport={'width': 1440, 'height': 1000})
        page = context.new_page()
        observe(page)
        response = page.goto(args.url, wait_until='networkidle')
        check(response is None or response.status == 200, 'Anonymous page HTTP 200')
        check(page.locator('h1').inner_text() == 'IT Program Leadership Dashboard', 'Existing branding')
        check(page.locator('#uploadWeek').input_value() == args.report_date, 'Selected reporting week')
        check(page.evaluate('dashboardData.reportDate') == args.report_date, 'Correct weekly source date')
        check(page.evaluate('dashboardData.sourceSha256') == sha, 'Embedded source hash')
        check(not context.cookies(), 'Anonymous access requires no login cookies')
        check('Weekly-only view.' in page.locator('#meta').inner_text(), 'Weekly-only scope')
        expected = page.evaluate('(base64) => {' + reader + '\nreturn parseWeeklyWorkbook(Uint8Array.from(atob(base64), c => c.charCodeAt(0)));}', base64.b64encode(source.read_bytes()).decode())
        actual = page.evaluate('records')
        total = len(expected)
        check(len(actual) == total == audit['records'], 'Source record count reconciled')
        check([(r['team'], r['sourceRow']) for r in expected] == [(r['team'], r['row']) for r in audit['rowMapping']], 'Every source worksheet row reconciled, including incomplete records')
        for a, e in zip(actual, expected):
            for key in a:
                if key == 'completionSource' and a['completion'] is not None:
                    continue  # XML numeric serialization may differ from Python float text.
                check(a[key] == e[key], f"{a['team']}!row {a['sourceRow']}: {key}")
        totals = Counter(r['rag'] for r in expected)
        check(dict(totals) == audit['rags'], 'RAG counts reconciled to worksheet audit')
        teams = sorted(set(r['team'] for r in expected))
        team_totals = {team: dict(Counter(r['rag'] for r in expected if r['team'] == team)) for team in teams}
        check(team_totals == {s['team']: s['rags'] for s in audit['sheets']}, 'Per-sheet reconciliation')
        body = page.locator('body').inner_text()
        check(not re.search(r'Source RAG styles|#[0-9a-fA-F]{6}|RAG styles legend', body), 'No RAG style legend, heading, or color strings')
        check(page.locator('select').count() == 2 and page.locator('label[for="team"]').count() == 1 and page.locator('label[for="rag"]').count() == 1, 'Exactly one Team and one RAG dropdown')

        def assert_view(selected, target=page):
            check(target.locator('select').count() == 2, 'Exactly two dropdowns after filtering')
            rendered = target.locator('#rows tr').evaluate_all('rows => rows.map(row => { const b=row.querySelector(".badge"), s=getComputedStyle(b); return {index:Number(row.dataset.recordIndex),rag:b.textContent,fill:s.backgroundColor,font:s.color,cells:Array.from(row.cells).map(c=>c.innerText)}; })')
            check(len(rendered) == len(selected), 'Filtered row count')
            for v, r in zip(rendered, selected):
                check(v['index'] == r['index'], 'Source row order and index')
                check(v['rag'] == r['rag'], 'Canonical source RAG label')
                check(v['fill'] == rgb(r['ragFill']), 'Rendered badge fill equals effective source XLSX fill')
                check(v['font'] == rgb(r['ragFont'] or '#000000'), 'Rendered badge font equals effective source XLSX font')
                check(v['cells'][3] == (str(r['completion']) + '%' if r['completion'] is not None else r['completionSource'] or 'Not provided'), 'Whole-number completion / faithful source text')
                check(v['cells'][4] == (r['finish'] or 'Not provided'), 'Source delivery date or estimate unchanged')
            segments = target.locator('.bar-row').evaluate_all('rows => rows.map(row=>({team:row.querySelector(".bar-label").textContent,bars:Array.from(row.querySelectorAll(".bar")).map(b=>({rag:b.dataset.rag,fill:b.dataset.ragFill,count:Number(b.dataset.count),rendered:getComputedStyle(b).backgroundColor}))}))')
            for segment in segments:
                counts = Counter((r['rag'], r['ragFill'], r['ragFont']) for r in selected if r['team'] == segment['team'])
                check(Counter((b['rag'], b['fill'], b['count']) for b in segment['bars']) == Counter((rag, fill, count) for (rag, fill, font), count in counts.items()), 'Chart segment names/styles/counts reconcile')
                for b in segment['bars']:
                    check(b['rendered'] == rgb(b['fill']), 'Actual chart segment color')
            check(sum(b['count'] for s in segments for b in s['bars']) == len(selected), 'Chart total')
            cards = target.locator('.kpi').evaluate_all('cards=>cards.map(c=>({rag:c.dataset.ragFilter,num:c.querySelector(".num").textContent,percent:c.querySelector(".percent").textContent,gradient:getComputedStyle(c).backgroundImage}))')
            check(cards[0]['num'] == str(len(selected)), 'Visible KPI total')
            for card in cards[1:]:
                subset = [r for r in selected if r['rag'] == card['rag']]
                check(card['num'] == str(len(subset)), 'RAG KPI count')
                check(card['percent'] == str(int(len(subset) / len(selected) * 100 + .5)) + '%', 'Whole-number KPI percentage')
                counts = Counter(r['ragFill'] for r in subset)
                for fill in counts:
                    check(rgb(fill) in card['gradient'], 'KPI preserves source fill variants')
                stops = re.findall(r'rgb\(\d+, \d+, \d+\) (\d+(?:\.\d+)?)%', card['gradient'])
                wanted, offset = [], 0
                for count in counts.values():
                    wanted.extend([offset, offset + count / len(subset) * 100])
                    offset += count / len(subset) * 100
                check(len(stops) == len(wanted) and all(abs(float(a) - b) < .001 for a, b in zip(stops, wanted)), 'KPI fill proportions')
            numeric = [r['completion'] for r in selected if r['completion'] is not None]
            check(target.locator('#avg').inner_text() == str(int(sum(numeric) / len(numeric) + .5)) + '%', 'Whole-number average completion')
            check(not re.search(r'\b\d+\.\d+%', target.locator('body').inner_text()), 'No visible fractional percentages')

        def filters(target=page, record_combinations=False):
            target.click('#clear')
            assert_view(expected, target)
            for rag in ('Red', 'Amber', 'Green'):
                target.select_option('#rag', rag)
                assert_view([r for r in expected if r['rag'] == rag], target)
            target.click('#clear')
            for team in teams:
                target.select_option('#team', team)
                options = target.locator('#rag option').evaluate_all('opts=>opts.map(o=>o.value).filter(Boolean)')
                rags = {r['rag'] for r in expected if r['team'] == team}
                check(set(options) == rags, 'Team cascade includes exactly available RAGs')
                for rag in ('Red', 'Amber', 'Green'):
                    check((rag in options) == (rag in rags), f'{team}/{rag}: available or unavailable as source dictates')
                target.select_option('#rag', '')
                assert_view([r for r in expected if r['team'] == team], target)
                for rag in options:
                    target.select_option('#rag', rag)
                    assert_view([r for r in expected if r['team'] == team and r['rag'] == rag], target)
                    if record_combinations:
                        combinations.append([team, rag])
            # Exercise every Team transition from each globally selected RAG.
            for team in teams:
                rags = {r['rag'] for r in expected if r['team'] == team}
                for rag in ('Red', 'Amber', 'Green'):
                    target.click('#clear')
                    target.select_option('#rag', rag)
                    target.select_option('#team', team)
                    check(target.locator('#rag').input_value() == (rag if rag in rags else ''), 'Team change preserves applicable RAG and clears unavailable RAG')
                    if record_combinations:
                        cascade_cases.append([team, rag])
            target.click('#clear')
            check(target.locator('#team').input_value() == target.locator('#rag').input_value() == target.locator('#search').input_value() == '', 'Reset clears shared filters/search')
            assert_view(expected, target)

        filters(record_combinations=True)
        for r in expected:
            page.locator(f'tr[data-record-index="{r["index"]}"]').click()
            check(page.locator('#modalTitle').text_content() == r['project'], 'Every source record detail opens')
            detail = page.locator('#detail > div').evaluate_all('ds=>ds.map(d=>({label:d.querySelector("b").textContent,value:d.innerText.slice(d.querySelector("b").innerText.length).trim()}))')
            by_label = {d['label']: d['value'] for d in detail}
            for label, key in [('Team', 'team'), ('Status', 'status'), ('RAG', 'rag'),
                               ('Estimated delivery date', 'finish'), ('Start date', 'start'),
                               ('Core objective', 'objective'), ('Current progress', 'progress'),
                               ('Key next steps', 'next'), ('Owner / DRI', 'owner'),
                               ('Key risks / blockers', 'risks'), ('Management attention', 'attention'),
                               ('Source / notes', 'source')]:
                check(by_label[label] == (r[key] or 'Not provided'), f'Detail {label}: faithful source or explicit missing state')
            check(by_label['Completion'] == str(r['completion']) + '%', 'Detail whole-number completion')
            badge = page.locator('#detail .badge')
            check(badge.evaluate('(e)=>getComputedStyle(e).backgroundColor') == rgb(r['ragFill']), 'Detail RAG source color')
            check(badge.evaluate('(e)=>getComputedStyle(e).color') == rgb(r['ragFont'] or '#000000'), 'Detail RAG source font color')
            page.click('#close')
        page.locator('[data-rag-filter="Amber"]').click()
        check(page.locator('#rows tr').count() == totals['Amber'], 'Summary card filtering')
        page.click('#clear')
        page.fill('#search', '__NO_MATCH_QA_9351__')
        check(page.locator('#rows tr').count() == 0 and page.locator('#empty').is_visible(), 'Visible no-results state')
        check(not page.locator('#cards').is_visible() and not page.locator('.grid').is_visible() and not page.locator('table').is_visible(), 'Empty panels suppressed')
        page.click('#clear')
        page.fill('#search', 'Yabin Liu')
        check(page.locator('#rows tr').count() == sum('yabin liu' in ' '.join(str(v) for v in r.values()).lower() for r in expected), 'Read-only owner search')
        page.click('#clear')
        page.screenshot(path=str(out / 'desktop.png'))
        (out / 'page-snapshot.html').write_text(page.content())
        (out / 'page-text.txt').write_text(page.locator('body').inner_text())
        (out / 'http.json').write_text(json.dumps({'url': args.url, 'status': response.status if response else None, 'headers': response.all_headers() if response else {}}, indent=2))
        if args.url.startswith('http'):
            download_response = context.request.get(urljoin(args.url, 'Weekly_Leadership_Source_Workbook.xlsx'))
            check(download_response.status == 200, 'Anonymous direct workbook HTTP 200')
            check(hashlib.sha256(download_response.body()).hexdigest() == sha, 'Direct workbook source SHA256')
        for button, filename in [('#downloadWorkbook', 'public-workbook.xlsx'), ('#downloadDashboard', 'dashboard.html')]:
            with page.expect_download() as download:
                page.click(button)
            download.value.save_as(out / filename)
            check('Download started:' in page.locator('#statusMessage').inner_text(), 'Visible download feedback')
        check(hashlib.sha256((out / 'public-workbook.xlsx').read_bytes()).hexdigest() == sha, 'Triggered workbook byte-identical')
        offline = context.new_page()
        observe(offline)
        context.set_offline(True)
        offline.goto((out / 'dashboard.html').resolve().as_uri())
        filters(offline)
        offline.locator('#rows tr').first.focus()
        offline.keyboard.press('Enter')
        check(offline.locator('#modal').is_visible(), 'Offline keyboard detail interaction')
        offline.keyboard.press('Escape')
        with offline.expect_download() as dl:
            offline.click('#downloadWorkbook')
        dl.value.save_as(out / 'offline-workbook.xlsx')
        check(hashlib.sha256((out / 'offline-workbook.xlsx').read_bytes()).hexdigest() == sha, 'Offline workbook byte-identical')
        context.set_offline(False)
        # All uploads here are local browser snapshots; no operational service writes.
        page.fill('#uploadWeek', '')
        page.set_input_files('#uploadWorkbook', source)
        page.wait_for_function('document.getElementById("statusMessage").textContent.includes("Choose the reporting week")')
        check(page.evaluate('dashboardData.sourceSha256') == sha, 'Missing reporting week validated without changing payload')
        next_week = (date.fromisoformat(args.report_date) + timedelta(days=7)).isoformat()
        page.fill('#uploadWeek', next_week)
        page.evaluate('window.loadingSeen=false;new MutationObserver(()=>{if(document.getElementById("uploadWorkbook").disabled && document.getElementById("statusMessage").textContent.includes("Loading"))window.loadingSeen=true}).observe(document.body,{subtree:true,attributes:true,childList:true})')
        page.set_input_files('#uploadWorkbook', source)
        page.wait_for_function('date => dashboardData.reportDate === date', arg=next_week)
        check(page.evaluate('window.loadingSeen'), 'Async local upload shows loading and disabled input')
        check(not page.locator('#uploadWorkbook').is_disabled(), 'Upload input restored after success')
        check(page.evaluate('records.length') == total, 'Local upload retains all source records')
        with page.expect_download() as dl:
            page.click('#downloadDashboard')
        dl.value.save_as(out / 'uploaded-dashboard.html')
        context.set_offline(True)
        offline.goto((out / 'uploaded-dashboard.html').resolve().as_uri())
        check(offline.evaluate('dashboardData.reportDate') == next_week, 'Uploaded snapshot retains selected week offline')
        assert_view(expected, offline)
        with offline.expect_download() as dl:
            offline.click('#downloadWorkbook')
        dl.value.save_as(out / 'uploaded-workbook.xlsx')
        check(hashlib.sha256((out / 'uploaded-workbook.xlsx').read_bytes()).hexdigest() == sha, 'Uploaded snapshot source bytes unchanged')
        context.set_offline(False)
        invalid = out / 'invalid.xlsx'
        invalid.write_bytes(b'not a workbook')
        page.set_input_files('#uploadWorkbook', invalid)
        page.wait_for_function('document.getElementById("statusMessage").textContent.startsWith("Workbook not loaded:")')
        check(page.evaluate('dashboardData.reportDate') == next_week and page.evaluate('dashboardData.sourceSha256') == sha, 'Invalid upload preserves validated snapshot')
        check(not page.locator('#uploadWorkbook').is_disabled(), 'Upload input restored after error')
        page.goto(args.url, wait_until='networkidle')
        page.set_viewport_size({'width': 390, 'height': 844})
        filters()
        page.screenshot(path=str(out / 'mobile.png'))
        check(page.evaluate('document.documentElement.scrollWidth <= innerWidth'), 'Mobile page fits viewport; wide table scrolls internally')
        page.locator('#rows tr').first.click()
        check(page.locator('#modal').is_visible(), 'Mobile detail opens')
        page.screenshot(path=str(out / 'mobile-detail.png'))
        page.click('#close')
        with page.expect_download() as dl:
            page.click('#downloadWorkbook')
        dl.value.save_as(out / 'mobile-workbook.xlsx')
        check(hashlib.sha256((out / 'mobile-workbook.xlsx').read_bytes()).hexdigest() == sha, 'Mobile download byte-identical')
        check(not errors, 'Zero browser page/console errors')
        check(not failures, 'Zero failed network requests')
        check(hashlib.sha256(source.read_bytes()).hexdigest() == sha, 'Original attachment unchanged after all QA')
        browser.close()
    summary = {'url': args.url, 'reportDate': args.report_date, 'sourceFile': source.name, 'sourceSha256': sha,
               'records': total, 'rags': dict(totals), 'teamRags': team_totals,
               'teamRagCombinations': combinations, 'cascadeTransitions': len(cascade_cases),
               'dropdowns': {'Team': 1, 'RAG': 1, 'total': 2}, 'viewports': ['1440x1000', '390x844'],
               'passedAssertions': len(checks), 'browserErrors': errors, 'failedRequests': failures,
               'offlineDashboard': 'PASS', 'downloadHashes': 'PASS', 'status': 'PASS'}
    (out / 'qa-results.json').write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))
except Exception as error:
    (out / 'qa-failure.json').write_text(json.dumps({'error': str(error), 'passedAssertions': len(checks), 'browserErrors': errors, 'failedRequests': failures}, indent=2))
    raise
