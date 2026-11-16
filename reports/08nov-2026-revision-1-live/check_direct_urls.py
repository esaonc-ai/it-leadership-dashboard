from pathlib import Path
from datetime import datetime,timezone
from urllib.request import Request,urlopen
import hashlib,json,base64,re
out=Path('qa-public/08nov-2026-revision-1');base='https://esaonc-ai.github.io/it-leadership-dashboard/';checks=[];expected=Path('index.html').read_bytes();workbook=Path('/home/user/workspace/IT & Technology Project_Portfolios_2026_v1.0 (Week of 08Nov2026 PST)_1.xlsx').read_bytes()
for suffix in ('','index.html','Weekly_Leadership_Source_Workbook.xlsx'):
 url=base+suffix
 with urlopen(Request(url,headers={'Cache-Control':'no-cache'}),timeout=30) as response:
  body=response.read();entry={'url':url,'finalUrl':response.url,'status':response.status,'verifiedAtUtc':datetime.now(timezone.utc).isoformat(),'headers':dict(response.headers),'bytes':len(body),'sha256':hashlib.sha256(body).hexdigest()}
 assert entry['status']==200 and entry['finalUrl']==url
 assert body==(workbook if suffix.endswith('.xlsx') else expected),url
 if suffix.endswith('.xlsx'):(out/'direct-public-workbook.xlsx').write_bytes(body)
 else:
  data=json.loads(re.search(r'/\* DASHBOARD_DATA_START \*/(.*?)/\* DASHBOARD_DATA_END \*/',body.decode(),re.S)[1]);assert base64.b64decode(data['sourceWorkbookBase64'])==workbook
 checks.append(entry)
(out/'direct-public-checks.json').write_text(json.dumps({'status':'PASS','authentication':'None; anonymous urllib GETs with no credentials or cookies','checks':checks},indent=2)+'\n');print(json.dumps([{k:v for k,v in e.items() if k!='headers'} for e in checks],indent=2))
