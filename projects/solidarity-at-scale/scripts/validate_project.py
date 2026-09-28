"""Check cross-file IDs, source locators, report structure, proof placeholders, and outputs."""
from pathlib import Path
import csv, hashlib, json, re

P=Path(__file__).resolve().parents[1];ROOT=P.parents[1]
def rows(name):
    with (P/name).open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
sources=rows('evidence/source-register.csv');ids={s['source_id'] for s in sources}
assert len(ids)==len(sources)==35
for s in sources:
    assert s['url'].startswith('https://') and s['access_depth'] and s['claim_locator']
for f in P.rglob('*.md'):
    for sid in re.findall(r'\bS\d{2}\b',f.read_text()):assert sid in ids,(f,sid)
claims=rows('evidence/claims.csv')
assert len({c['claim_id'] for c in claims})==len(claims)
for c in claims:
    for sid in filter(None,c['source_ids'].split(';')):assert sid in ids,(c['claim_id'],sid)
for r in rows('evidence/source-relations.csv'):
    assert r['from_source'] in ids and r['to_source'] in ids
report=(P/'report/research-report.md').read_text()
assert [int(n) for n in re.findall(r'^## (\d+) ',report,re.M)]==list(range(15))
bib=(P/'sources/references.bib').read_text()
assert set(re.findall(r'@\w+\{(S\d+),',bib))==ids
lean=(ROOT/'Solidarity.lean').read_text()
assert not re.search(r'\b(sorry|admit|axiom)\b',lean)
theorems=re.findall(r'^theorem (\w+)',lean,re.M)
assert len(theorems)==16
for f in (P/'formal').glob('*.md'):
    for theorem in re.findall(r'`(\w+)`',f.read_text()):
        if theorem.endswith('_iff'):assert theorem in theorems
expected=['solidarity-at-scale-paper.docx','solidarity-at-scale-paper.pdf','solidarity-at-scale-report.docx','solidarity-at-scale-report.pdf']
for name in expected:assert (P/'outputs'/name).stat().st_size>1000,name
manifest={'formal_checked_commit':'841419eea726383da96e105b3b995910b80f2ed0','formal_run':'https://github.com/Sodelin/Mathematics-of-Psychology-Formalized/actions/runs/36365007772','source_count':len(sources),'claim_count':len(claims),'theorem_count':len(theorems),'hash_algorithm':'sha256','files':{}}
for f in [ROOT/'Solidarity.lean',ROOT/'lakefile.toml',ROOT/'lean-toolchain',*(P/'outputs').glob('*'),P/'paper/manuscript.md',P/'report/research-report.md']:
    if f.is_file():manifest['files'][str(f.relative_to(ROOT))]=hashlib.sha256(f.read_bytes()).hexdigest()
(P/'verification-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(f'PASS: {len(sources)} sources; {len(claims)} typed claims; {len(theorems)} theorem declarations; 15 report sections; 4 rendered deliverables. This script does not run Lean or verify empirical truth.')
