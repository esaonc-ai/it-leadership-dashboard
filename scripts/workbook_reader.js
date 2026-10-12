/* Local XLSX reader: original bytes remain unchanged; unsupported RAG rules block upload. */
function parseWeeklyWorkbook(bytes) {
 const zip=fflate.unzipSync(bytes), dec=new TextDecoder();
 const xml=p=>{if(!zip[p])throw Error('Missing workbook part: '+p);return new DOMParser().parseFromString(dec.decode(zip[p]),'application/xml');};
 const nodes=(p,n)=>Array.from(p.getElementsByTagNameNS('*',n));
 const txt=(p,n)=>nodes(p,n)[0]?.textContent||'';
 const shared=zip['xl/sharedStrings.xml']?nodes(xml('xl/sharedStrings.xml'),'si').map(x=>nodes(x,'t').map(t=>t.textContent).join('')):[];
 const styles=xml('xl/styles.xml'), group=n=>nodes(styles,n)[0];
 const fills=Array.from(group('fills').children),fonts=Array.from(group('fonts').children),xfs=Array.from(group('cellXfs').children),dxfs=group('dxfs')?Array.from(group('dxfs').children):[];
 const color=x=>{if(!x)return null;if(x.hasAttribute('rgb'))return '#'+x.getAttribute('rgb').slice(-6).toUpperCase();if(x.hasAttribute('theme')||x.hasAttribute('indexed'))throw Error('Unsupported RAG theme/indexed color; validate before using.');return null;};
 const fill=(x,diff=false)=>{let p=nodes(x,'patternFill')[0];if(!p||(!diff&&p.getAttribute('patternType')!=='solid'))return null;return color(nodes(p,diff?'bgColor':'fgColor')[0])||color(nodes(p,'fgColor')[0]);};
 const font=x=>color(nodes(x,'color')[0]);
 const clean=v=>v==null||['nan','none','null'].includes(String(v).trim().toLowerCase())?'':String(v).trim();
 const coord=a=>{let m=a.replaceAll('$','').match(/^([A-Z]+)(\d+)$/);return [Array.from(m[1]).reduce((a,c)=>a*26+c.charCodeAt(0)-64,0),+m[2]];};
 const letters=c=>{let s='';while(c){c--;s=String.fromCharCode(65+c%26)+s;c=Math.floor(c/26);}return s;};
 const inRange=(a,r)=>{let [c,y]=coord(a),[lo,hi]=r.split(':'),[l,b]=coord(lo),[h,t]=coord(hi||lo);return c>=l&&c<=h&&y>=b&&y<=t;};
 const numeric=v=>clean(v)!==''&&Number.isFinite(Number(String(v).replace('%','')));
 const percent=v=>{if(!numeric(v))return null;let n=Number(String(v).replace('%',''));if(!String(v).endsWith('%')&&Math.abs(n)<=1)n*=100;if(n<0||n>100)throw Error('Completion outside 0–100');return Math.round(n);};
 const bool=f=>{if(f==='True'||f==='False')return f==='True';let m=f.match(/^(OR|AND|NOT)\((.*)\)$/);if(!m)throw Error('Unsupported RAG expression');let parts=[],depth=0,start=0;for(let i=0;i<m[2].length;i++){let c=m[2][i];if(c==='(')depth++;if(c===')')depth--;if(c===','&&!depth){parts.push(m[2].slice(start,i));start=i+1;}}parts.push(m[2].slice(start));let v=parts.map(bool);return m[1]==='OR'?v.some(Boolean):m[1]==='AND'?v.every(Boolean):!v[0];};
 const wb=xml('xl/workbook.xml'),rels=nodes(xml('xl/_rels/workbook.xml.rels'),'Relationship'),records=[];
 for(const sheet of nodes(wb,'sheet')){
  let rid=sheet.getAttribute('r:id'),rel=rels.find(x=>x.getAttribute('Id')===rid),target=rel.getAttribute('Target');let path=target.startsWith('/')?target.slice(1):'xl/'+target;
  let doc=xml(path),cells=new Map(),rawCells=new Map();
  for(let c of nodes(doc,'c')){let a=c.getAttribute('r'),type=c.getAttribute('t'),v=txt(c,'v');rawCells.set(a,c);cells.set(a,type==='s'?shared[+v]:type==='inlineStr'?nodes(c,'t').map(t=>t.textContent).join(''):v);}
  let header=Array.from({length:20},(_,i)=>i+1).find(r=>['#','Project / Workstream','Status','RAG Status'].every((v,c)=>cells.get(letters(c+1)+r)===v));if(!header)continue;
  const value=a=>clean(cells.get(a));
  const effective=a=>{
   let c=rawCells.get(a),xf=xfs[+(c?.getAttribute('s')||0)],f=fill(fills[+xf.getAttribute('fillId')]),ft=font(fonts[+xf.getAttribute('fontId')]),fs=false,ts=false,rules=[];
   for(let cf of nodes(doc,'conditionalFormatting')){let range=cf.getAttribute('sqref');if(!range){let sr=txt(cf,'sqref');if(sr.split(/\s+/).some(r=>r&&inRange(a,r)))throw Error('Extended RAG formatting unsupported');continue;}if(range.split(/\s+/).some(r=>inRange(a,r)))for(let rule of Array.from(cf.children).filter(x=>x.localName==='cfRule'))rules.push({rule,origin:range.split(/\s+/)[0].split(':')[0]});}
   rules.sort((a,b)=>+a.rule.getAttribute('priority')-+b.rule.getAttribute('priority'));
   for(let {rule,origin} of rules){let type=rule.getAttribute('type'),match=false;
    if(type==='containsText')match=value(a).toLowerCase().includes((rule.getAttribute('text')||'').toLowerCase());
    else if(type==='expression'){
     let [ac,ar]=coord(a),[oc,or]=coord(origin),formula=txt(rule,'formula').replace(/(\$?)([A-Z]+)(\$?)(\d+)/g,(all,dc,c,dr,r)=>letters(dc?coord(c+'1')[0]:coord(c+'1')[0]+ac-oc)+(dr?+r:+r+ar-or));
     formula=formula.replace(/ISNUMBER\(SEARCH\("([^"]*)",([A-Z]+\d+)\)\)/g,(all,s,ref)=>value(ref).toLowerCase().includes(s.toLowerCase())?'True':'False').replace(/([A-Z]+\d+)<>""/g,(all,ref)=>value(ref)?'True':'False');match=bool(formula);
    }else throw Error('Unsupported RAG rule: '+type);
    if(!match)continue;let d=dxfs[+rule.getAttribute('dxfId')];if(d){if(!fs){let ff=fill(d,true);if(ff){f=ff;fs=true;}}if(!ts){let tf=font(d);if(tf){ft=tf;ts=true;}}}if(rule.getAttribute('stopIfTrue')==='1')break;
   }return [f,ft];
  };
  const dateValue=a=>{let v=value(a),c=rawCells.get(a);if(c&&numeric(v)&&!c.getAttribute('t')){let xf=xfs[+(c.getAttribute('s')||0)],fmt=+xf.getAttribute('numFmtId'),custom=nodes(styles,'numFmt').find(x=>+x.getAttribute('numFmtId')===fmt)?.getAttribute('formatCode')||'';if((fmt>=14&&fmt<=22)||/[yd]/i.test(custom))return new Date(Date.UTC(1899,11,30)+Number(v)*86400000).toISOString().slice(0,10);}return v;};
  for(let r of nodes(doc,'row').map(x=>+x.getAttribute('r')).filter(r=>r>header)){
   if(!value('A'+r)||!value('B'+r))continue;
   let v=Array.from({length:14},(_,c)=>value(letters(c+1)+r)),explicit=v[3],shift=explicit&&numeric(v[5])&&!numeric(v[6]),rag=explicit||(v[2].match(/\b(Red|Amber|Green)\b/i)||[])[1]||null, offset=shift||!explicit?-1:0;
   let [ragFill,ragFont]=rag?effective((explicit?'D':'C')+r):[null,null],src=letters(14+offset)+r;
   records.push({index:records.length,id:v[0],project:v[1],team:sheet.getAttribute('name'),status:v[2],rag,ragFill,ragFont,start:offset?'':dateValue('E'+r),finish:dateValue(letters(6+offset)+r),completion:percent(v[6+offset]),completionSource:v[6+offset],objective:v[7+offset],progress:v[8+offset],next:v[9+offset],owner:v[10+offset],risks:v[11+offset],attention:v[12+offset],source:(rawCells.has(src)?txt(rawCells.get(src),'f'):'').startsWith('_xlfn.DISPIMG')?'Embedded workbook image; view in source workbook':v[13+offset],sourceRow:r,sourceLayout:shift?'shifted':'standard'});
  }
 }
 if(!records.length)throw Error('No compatible weekly records found');return records;
}
