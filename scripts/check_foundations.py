"""Read-only provenance and documentation checks. This does not replace running Lean."""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / 'projects/foundations'

def rows(name):
    with (P / name).open(newline='', encoding='utf-8') as file:
        return list(csv.DictReader(file))

declarations = {}
lean_files = [ROOT / 'Solidarity.lean', ROOT / 'SocialScience.lean',
              *sorted((ROOT / 'SocialScience').glob('*.lean'))]
for file in lean_files:
    text = file.read_text()
    assert not re.search(r'\b(sorry|admit|axiom|native_decide)\b', text), file
    namespace = re.search(r'^namespace (\S+)', text, re.M)
    if namespace:
        for name in re.findall(r'^theorem\s+(\w+)', text, re.M):
            full = namespace[1] + '.' + name
            assert full not in declarations, full
            declarations[full] = str(file.relative_to(ROOT))

inventory = rows('theorem-inventory.csv')
assert len(inventory) == 51
assert len(declarations) == 67
assert len({r['declaration'] for r in inventory}) == len(inventory)
new_names = {name for name in declarations if name.startswith('SocialScience.')}
assert {r['declaration'] for r in inventory} == new_names
guide = (P / 'theorem-guide.md').read_text()
for row in inventory:
    assert row['source_file'] == declarations[row['declaration']]
    assert row['meaning'] and row['assumptions'] and row['limitations']
    assert '`' + row['declaration'].split('.')[-1] + '`' in guide, row['declaration']

audited = re.findall(r'^#print axioms (\S+)',
                     (ROOT / 'SocialScience/Audit.lean').read_text(), re.M)
assert len(audited) == len(set(audited)) == len(declarations)
assert set(audited) == set(declarations)

manifest = json.loads((P / 'verification-manifest.json').read_text())
assert manifest['checked_theorem_count'] == len(declarations)
expected_sources = {str(f.relative_to(ROOT)) for f in lean_files}
expected_sources |= {'lean-toolchain', 'lakefile.toml'}
assert set(manifest['files']) == expected_sources
for name, expected in manifest['files'].items():
    actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
    assert actual == expected, ('Checked-source hash mismatch', name)

log = (P / 'formal-check-output.txt').read_text()
found = {}
for name, kind, dependencies in re.findall(
        r"'(SocialScience\.[^']+|Solidarity\.[^']+)' "
        r"(does not depend on any axioms|depends on axioms: \[([^\]]*)\])", log):
    deps = {x.strip() for x in dependencies.split(',') if x.strip()}
    assert deps <= {'propext', 'Classical.choice', 'Quot.sound'}, (name, deps)
    found[name] = deps
assert set(found) == set(declarations), 'Audit output must cover every declaration'

sources = rows('sources/source-register.csv')
source_ids = {s['source_id'] for s in sources}
assert len(source_ids) == len(sources) == 11
for source in sources:
    assert source['url'].startswith('https://')
    assert source['access_depth'] and source['claim_locator']
bib = (P / 'sources/references.bib').read_text()
assert set(re.findall(r'@\w+\{(F\d+),', bib)) == source_ids
for relation in rows('sources/source-relations.csv'):
    assert relation['from_source'] in source_ids and relation['to_source'] in source_ids

report = (P / 'report.md').read_text()
assert [int(n) for n in re.findall(r'^## (\d+) ', report, re.M)] == list(range(15))
for file in [ROOT / 'README.md', *(ROOT / 'psychology').glob('*.md'), *P.rglob('*.md')]:
    content = file.read_text()
    assert content.count('```') % 2 == 0, ('Unclosed code fence', file)
    for sid in re.findall(r'\bF\d{2}\b', content):
        assert sid in source_ids, (file, sid)
    for target in re.findall(r'\]\(([^)]+)\)', content):
        if re.match(r'^[a-zA-Z]+:|^#', target):
            continue
        assert (file.parent / target.split('#')[0]).is_file(), (file, target)
    table_width = None
    for line in content.splitlines():
        if line.startswith('|'):
            width = line.count('|')
            assert table_width is None or width == table_width, ('Malformed table', file, line)
            table_width = width
        else:
            table_width = None

print('PASS: 67 declarations; 51 new explanations; complete logical-dependency audit; '
      'checked source hashes; 11 references; 15 report sections; local links and Markdown structure.')
print('These checks do not establish empirical validity or scientific novelty.')
