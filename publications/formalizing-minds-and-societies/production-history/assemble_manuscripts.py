from pathlib import Path
import csv, json, re, unicodedata

ROOT=Path(__file__).parent
P=ROOT/'reading-pack'
refs=json.loads((ROOT/'references-data.json').read_text())
byid={r['id']:r for r in refs}
sortkey=lambda r: unicodedata.normalize('NFKD',r['author']).casefold()
refs.sort(key=sortkey)

def cite_replace(s):
    def f(m):
        ids=[]
        for a,b in re.findall(r'R(\d{2})(?:[–-]R(\d{2}))?',m[0]):
            ids.extend(f'R{i:02}' for i in range(int(a),int(b or a)+1))
        return '('+'; '.join(r['cite'] for r in sorted((byid[i] for i in set(ids)),key=sortkey))+')'
    s=re.sub(r'\[R\d{2}(?:[–-]R\d{2})?(?:[,; ]+R\d{2}(?:[–-]R\d{2})?)*\]',f,s)
    # Existing narrative citations must not gain an immediately redundant parenthesis.
    s=s.replace('Benzmüller et al. (2020) describe a framework using higher-order logic and automated reasoning to investigate normative theories. This establishes a route for extending the project into explicit normative theories. (Benzmüller et al., 2020)', 'Benzmüller et al. (2020) describe a framework using higher-order logic and automated reasoning to investigate normative theories. This establishes a route for extending the project into explicit normative theories.')
    return s

small={'a','an','the','and','or','but','as','at','by','for','from','in','of','on','to','up','with','into','per','via','versus'}
def titlecase(s):
    # Keep identifiers and labels intact; capitalize the explanatory heading.
    parts=re.split(r'(`[^`]+`)',s)
    result=[]
    for j,p in enumerate(parts):
        if j%2: result.append(p); continue
        words=p.split(' ')
        for i,w in enumerate(words):
            if w and (i==0 or w.lower() not in small or words[i-1].endswith(':')):
                words[i]=w[0].upper()+w[1:]
        result.append(' '.join(words))
    return ''.join(result)

def clean_headings(s,strip_numbers=True):
    def f(m):
        hashes,title=m.groups()
        if strip_numbers and not re.match(r'\d{2}\. `',title):
            title=re.sub(r'^\d+(?:\.\d+)*\.?\s+','',title)
        return hashes+' '+titlecase(title)
    return re.sub(r'^(#{1,6}) (.+)$',f,s,flags=re.M)

def bibliography(selected):
    return '# References\n\n'+ '\n\n'.join(r['apa'] for r in refs if r['id'] in selected)+'\n'

def table_captions(s, titles):
    count=0
    def f(m):
        nonlocal count
        title=titles[count]
        count+=1
        return m[0].rstrip()+'\n\nTable: '+title+'\n'
    s=re.sub(r'(?m)^\|[^\n]+\|\n\|[-:| ]+\|\n(?:\|[^\n]+\|\n?)+',f,s)
    assert count==len(titles),(count,len(titles))
    return s

article=(ROOT/'article-draft.md').read_text()
article=article.replace('The source contains 67 named', 'The earlier reader\'s guide supplied the explanatory baseline for this synthesis (Formalizing Soft Sciences Project, 2026). The source contains 67 named')
article=article.replace('same base model', 'same base model')
abody,app=article.split('# Appendix A',1)
article_ids={r['id'] for r in refs if r['cite'] in article or re.search(re.escape(r['cite'].split(', ')[0].replace(' & ',' and '))+r' \('+re.escape(r['year'])+r'\)',article)}
# Et-al narrative detection is covered above; two named narrative authors are explicit.
article_ids.update(['R04','R05','R12','R16','R18','R19'])
article=abody.rstrip()+'\n\n'+bibliography(article_ids)+'\n# Appendix A'+app
article=clean_headings(article)
article=table_captions(article,['Distribution and Scientific Role of the 67 Declarations'])

f=cite_replace((P/'01-fields-and-formalization.md').read_text())
f=clean_headings(f)
f=f.replace('# Findings','# Mathematical and Computational Approaches')
f=f.replace('# Introduction — The Scientific Opportunity','# Formalizing Minds and Societies')
atlas=cite_replace((P/'02-theorem-atlas.md').read_text())
atlas=re.sub(r'^## 4\.7[^\n]+','# The Complete Atlas of 67 Theorems',atlas,flags=re.M)
atlas=re.sub(r'^### ([A-G])\. (.+)',r'## \2',atlas,flags=re.M)
atlas=atlas.replace('### What the count means after reading the atlas','## What the Count Means After Reading the Atlas')
atlas=clean_headings(atlas)
worked=cite_replace((P/'03-worked-arguments.md').read_text())
worked=worked.replace('## 4.8 Worked investigations in what a proof can reveal','# Worked Investigations')
worked=re.sub(r'^### ', '## ',worked,flags=re.M)
worked=clean_headings(worked)
anatomy=(P/'03a-anatomy-of-proofs.md').read_text()
ai=cite_replace((P/'04-ai-and-research-roadmap.md').read_text())
ai=ai.replace('## 4.9 What verified social-science models could contribute to AI','# Verified Social-Science Models and AI')
ai=re.sub(r'^### ', '## ',ai,flags=re.M)
ai,tail=ai.split('# 5. Conclusion',1)
conclusion,tail=tail.split('# 6. Deconstructive analysis',1)
routes,glossary=tail.split('# 9. Glossary',1)
routes='# Research Program\n\n## Deconstructive analysis'+routes
routes=routes.replace('# 7. Reconstructive analysis','## Reconstructive analysis').replace('# 8. Middle-out synthesis','## Middle-out synthesis')
reflection=(P/'05-reflections-and-appendices.md').read_text().split('# 11. ',1)[1]
reflection='# '+reflection
reflection,tail2=reflection.split('# 13. Zotero and Obsidian Integration',1)
integration,appendices=tail2.split('# 14. Appendices',1)
appendices=re.sub(r'^## Appendix ([A-D]) — (.+)$',r'# Appendix \1\n\n## \2',appendices,flags=re.M)
source_access='# Appendix H\n\n## Source Access and Evidence Roles\n\nThe following register records the material inspected for this synthesis. The source identifiers connect the manuscript to the accompanying metadata files.\n\n'
for r in refs:
    source_access+=f"**{r['id']}: {r['cite']}.** {r['access']}\n\n"
brief=(P/'00-decision-brief.md').read_text().split('\n',1)[1]
body='\n\n'.join([f,atlas,worked,anatomy,ai,clean_headings(routes),clean_headings(reflection),'# Conclusion\n'+conclusion])
book=body+'\n\n'+bibliography(set(byid))+appendices
book+='\n# Appendix E\n\n## Glossary\n'+glossary
book+='\n# Appendix F\n\n## Reference Management and Research Notes\n'+integration
book+='\n# Appendix G\n\n## Executive Summary\n'+brief
book+='\n'+source_access
book=clean_headings(book)
book=table_captions(book,[
    'Three Complementary Forms of Formalization',
    'Neighboring Research Approaches and Their Connection to the Library',
    'Formal Approaches Across Biological and Social Disciplines',
    'Synthetic Rates Used in the Aggregation Counterexample',
    'Complete Response Table for Two Binary Causal Models',
    'Routes From a Verified Library to an AI System',
    'Formal Objects and Their Roles in the Source',
    'Evidence and Research Uses at a Glance'])

# Record final titles and scholarly metadata once for both output formats.
meta={
 'article':dict(title='From Social Explanations to Checkable Proofs: A 67-Theorem Framework for Scientific Reasoning',short='CHECKABLE PROOFS IN SOCIAL SCIENCE',author='Formalizing Soft Sciences Project',subtitle='Research Article',date='September 28, 2026',filename='research-article'),
 'dissertation':dict(title='Formalizing Minds and Societies: 67 Lean Proofs and Their Scientific Uses',short='FORMALIZING MINDS AND SOCIETIES',author='Formalizing Soft Sciences Project',subtitle='A Dissertation-Style Methodological Monograph',date='September 28, 2026',filename='dissertation')}
for kind,text in [('article',article),('dissertation',book)]:
    assert not re.search(r'\[R\d+',text)
    # The exact code identifiers remain the stable anchors across editions.
    (P/(meta[kind]['filename']+'.md')).write_text(text)
    meta[kind]['words']=len(text.split())

(ROOT/'manuscript-metadata.json').write_text(json.dumps(meta,indent=2))

# Resolve the atlas reading order to the exact source namespaces and line locations.
inventory=json.loads((ROOT/'theorem_source_index.json').read_text())
byname={x['name']:x for x in inventory}
rows=[]
for n,name,label in re.findall(r'^### (\d+)\. `([^`]+)` — (.+)$',(P/'02-theorem-atlas.md').read_text(),re.M):
    item=byname[name]
    source=(ROOT/'source_snapshot'/item['file']).read_text()
    ns=re.search(r'^namespace (.+)$',source,re.M)[1]
    rows.append(dict(number=int(n),name=name,qualified_name=ns+'.'+name,file=item['file'],line=item['line'],explanation=label,url=f"https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/{item['file']}#L{item['line']}"))
assert len(rows)==67 and len({r['qualified_name'] for r in rows})==67
with (P/'theorem-inventory.csv').open('w',newline='') as out:
    w=csv.DictWriter(out,fieldnames=rows[0]);w.writeheader();w.writerows(rows)

with (P/'source-register.csv').open('w',newline='') as out:
    w=csv.DictWriter(out,fieldnames=['id','key','title','year','url','access','tags']);w.writeheader();w.writerows({k:r.get(k,'') for k in w.fieldnames} for r in refs)
relations=[('R18','R01','baseline explanation of source development'),('R02','R01','verification principles for source audit'),('R04','R01','theory-building rationale'),('R05','R01','recovery-analysis extension'),('R07','R01','psychological formalization precedent'),('R08','R01','biological model-checking precedent'),('R09','R01','Lean social-choice precedent'),('R10','R01','cultural dynamics precedent'),('R11','R01','symbolic-domain formalization precedent'),('R12','R01','metacognition measurement extension'),('R13','R01','normative-reasoning extension'),('R14','R01','verified-data training precedent'),('R15','R01','verification-feedback training precedent'),('R16','R01','substantive causal-identification context'),('R19','R01','appraisal-tool scope distinction'),('R20','R01','reporting transparency reference'),('R21','R01','study-design appraisal distinction')]
with (P/'source-relations.csv').open('w',newline='') as out:
    w=csv.writer(out);w.writerow(['source','target','interpretive_relationship']);w.writerows(relations)

bib=[];ris=[]
for r in refs:
    typ={'article':'article','preprint':'misc','webpage':'misc','software':'misc','manuscript':'unpublished'}[r['type']]
    fields={k:r[k] for k in ['author','title','year','journal','volume','number','pages','doi','url'] if k in r}
    if r['type'] in ['webpage','software','manuscript']:fields['author']='{'+fields['author']+'}'
    if fields.get('year')=='n.d.':fields.pop('year');fields['note']='Undated; accessed 2026-09-28'
    fields['keywords']=r['tags'].replace(';',', ')
    bib.append('@'+typ+'{'+r['key']+',\n'+',\n'.join('  '+k+' = {'+str(v).replace('–','--')+'}' for k,v in fields.items())+'\n}')
    rr=['TY  - '+{'article':'JOUR','preprint':'UNPB','webpage':'ELEC','software':'COMP','manuscript':'UNPB'}[r['type']], 'ID  - '+r['key']]
    rr+=['AU  - '+a for a in r['author'].split(' and ')]
    for field,tag in [('title','TI'),('journal','JO'),('volume','VL'),('number','IS'),('doi','DO'),('url','UR')]:
        if field in r:rr.append(tag+'  - '+r[field])
    if r['year']!='n.d.':rr.append('PY  - '+r['year'])
    if 'pages' in r:
        pg=r['pages'].split('–');rr.append('SP  - '+pg[0])
        if len(pg)>1:rr.append('EP  - '+pg[1])
    rr+=['KW  - '+tag for tag in r['tags'].split(';')]
    rr+=['N1  - '+r['access'],'ER  - ']
    ris.append('\n'.join(rr))
(P/'references.bib').write_text('\n\n'.join(bib)+'\n')
(P/'references.ris').write_text('\n\n'.join(ris)+'\n')
(P/'references.md').write_text(bibliography(set(byid)))

# The chapter files remain usable individually, with resolved author-date citations.
for p in P.glob('0[1-5]*.md'):
    s=cite_replace(p.read_text())
    p.write_text(s)

print(json.dumps({'manuscripts':meta,'article_references':len(article_ids),'monograph_references':len(refs),'theorems':len(rows)},indent=2))
