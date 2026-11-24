#!/usr/bin/env python3
"""Read-only source review; exact cell anchors, no workbook save calls."""
import argparse, hashlib, json, re
from collections import Counter
from datetime import date,datetime
from pathlib import Path
from zipfile import ZipFile
from openpyxl import load_workbook
from refresh_dashboard import build_records, text, source_style

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('workbook',type=Path)
    parser.add_argument('--previous',type=Path)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();args.output.mkdir(parents=True,exist_ok=True)
    before=hashlib.sha256(args.workbook.read_bytes()).hexdigest()
    w=load_workbook(args.workbook);c=load_workbook(args.workbook,data_only=True)
    records=build_records(args.workbook);findings=[]
    def add(category,summary,sheet,refs):
        findings.append({'category':category,'summary':summary,'cells':{sheet+'!'+ref:{'value':text(w[sheet][ref].value),'cachedValue':text(c[sheet][ref].value)} for ref in refs}})
    # Match explicit current management RAG instructions rather than unrelated words.
    for r in records:
        m=r['attention'];directive=re.search(r'\b(?:maintain|keep|retain)\b.{0,32}?\b(Amber|Red|Green)\b',m,re.I)
        if directive and directive[1].lower()!=r['rag'].lower():
            n=str(r['sourceRow']);add('RAG cell versus management directive',f"D{n} is {r['rag']}; M{n} directs {directive[1]}. Preserve both; ask source owner to reconcile.",r['team'],['B'+n,'D'+n,'G'+n,'M'+n])
        reviewer=re.search(r'\bReviewer (Red|Amber|Green)\b',m,re.I)
        if reviewer and reviewer[1].lower()!=r['rag'].lower():
            n=str(r['sourceRow']);add('Separate reviewer assessment',f"D{n} is {r['rag']}; M{n} describes {reviewer[1]} reviewer risk. This is a narrative assessment, not a confirmed incident or replacement RAG.",r['team'],['D'+n,'M'+n,'N'+n])
    for r in [14]:
        add('Closure / completion conflict','G14 is 100% and D14 Green, while C14 says conference-room troubleshooting not started; N14 says no later closure evidence. No correction inferred.','Infrastructure & Cloud',[f'{col}{r}' for col in ['B','C','D','G','I','J','N']])
    add('Internally mixed closure wording','C31 says both remote desktop unavailable and successful-session test complete; J31 still requests troubleshooting and a successful-session test. G31 is 85%, not 100%. Clarify current outcome.','Infrastructure & Cloud',['C31','D31','G31','I31','J31','N31'])
    for r in range(91,99):
        add('Completion evidence caveat',f'G{r} remains 60%; N{r} explicitly says completion is not quantifiable from supplied evidence. This caveat is retained alongside the numeric source cell.','Infrastructure & Cloud',[f'G{r}',f'N{r}'])
    for r in [4,5,6]:
        add('Scope / acceptance clarification',f'G{r} is 100% and H{r} says Completed; J{r} retains UAT, sizing or procurement next steps. Ask whether those steps are outside completed scope.','IoT',[f'G{r}',f'H{r}',f'I{r}',f'J{r}'])
    with ZipFile(args.workbook)as z:
        assert z.testzip() is None
        media=[n for n in z.namelist() if re.search(r'\.(png|jpe?g|gif|bmp|webp|tiff?|emf|wmf)$',n,re.I)]
        zip_parts=z.namelist()
    add('Unavailable image formula','N6 DISPIMG caches #NAME?; the ZIP has no image binary or cellimages part. The referenced image cannot be recovered from this attachment.','IoT',['N6'])
    add('Source chronology clarification','I14 describes a Thursday (10/8) pickup, while N14 dates the meeting notes 11-Sep-2026. Confirm pickup/source chronology; do not calculate a new delivery date.','IT Compliance Program',['I14','N14'])
    add('Reporting label versus later evidence','The supplied filename is Week of 15Nov2026 PST, but current cells explicitly cite 22/23 November evidence. Preserve the reporting label without asserting an as-of-15-Nov cutoff.','Infrastructure & Cloud',['I4','N65','N89'])
    refs=[f'N{r}' for r in range(91,99)]
    add('External provenance unavailable','These source notes refer to Infrastructure Review for S-source filenames. No worksheet with that name or the external evidence files is in this workbook.','Infrastructure & Cloud',refs)
    rechecks=[]
    for sheet,refs,note in [
      ('Infrastructure & Cloud',['C65','D65','G65','I65','M65'],'Prior Green versus Red/offline conflict is absent: D65 Amber, G65 20%, unresolved outage/decommission decision explicit.'),
      ('Infrastructure & Cloud',['C17','G17','C19','G19'],'Prior 100% closure conflicts changed: G17 55%, G19 65%; unresolved work remains explicit.'),
      ('WCS Engineering',['D7','G7','M7','D11','G11','M11'],'Prior D7/D11 management conflicts are absent: both Green/100% with matching IT closure directions.'),
      ('WCS Engineering',['D8','G8','I8','M8','G12','M12'],'Prior 85% versus 80% mismatch is absent. G8 and I8/M8 say 85%; D8 Green versus M8 Amber remains. G12 is now 25%.'),
      ('IT Compliance Program',['G2','I2'],'Prior 80% versus 59% mismatch is absent: G2 and I2 now agree on 59%.'),
      ('IoT',['A1','A2'],'Prior stale August reporting banner is absent: A2 now only identifies Team Lead Yabin Liu; A1 is a title, not a date.')]:
        rechecks.append({'summary':note,'cells':{sheet+'!'+r:text(w[sheet][r].value)for r in refs}})
    previous=None
    if args.previous:
        pw=load_workbook(args.previous);pr=build_records(args.previous);changes=[]
        for s in w:
            ps=pw[s.title]if s.title in pw.sheetnames else None
            for row in s:
                for cell in row:
                    old=ps[cell.coordinate].value if ps else None
                    if cell.value!=old:changes.append({'sheet':s.title,'cell':cell.coordinate,'previous':text(old),'current':text(cell.value)})
        previous={'previousSha256':hashlib.sha256(args.previous.read_bytes()).hexdigest(),'previousRecords':len(pr),'previousTeams':pw.sheetnames,'currentTeams':w.sheetnames,'addedTeams':[s for s in w.sheetnames if s not in pw.sheetnames],'cellValueChanges':changes}
        (args.output/'source-comparison.json').write_text(json.dumps(previous,indent=2))
    result={'sourceFile':args.workbook.name,'sourceSha256':before,'records':len(records),'rags':dict(Counter(r['rag']for r in records)),'findings':findings,'resolvedOrChangedPriorFindings':rechecks,'imageParts':media,'zipParts':zip_parts,'zipIntegrity':'PASS','sourceSha256After':hashlib.sha256(args.workbook.read_bytes()).hexdigest()}
    assert result['sourceSha256After']==before
    (args.output/'source-issues.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({'records':len(records),'findings':len(findings),'currentRags':result['rags'],'sourceUnchanged':True}))
if __name__=='__main__':main()
