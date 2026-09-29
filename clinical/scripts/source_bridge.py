"""Extract a bounded declarative fragment without executing upstream MATLAB.
The exact source SHA256 and git commit are pinned. Unknown expression tokens fail.
This checks transcription of tables only; it is not a MATLAB/SPM compiler proof.
"""
from pathlib import Path
import hashlib, re, sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE_COMMIT = '82a0a3d75b0bdc08d2b78cdf2201d7aa626c27a3'
EXPECTED_SHA256 = 'faba14894224ccf1a20594d390a5f7e3a74eed665205fa24285ddfa1d36513e5'

def render(source_path):
    raw = Path(source_path).read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != EXPECTED_SHA256:
        raise ValueError(f'Upstream source hash changed: {actual}')
    text = raw.decode().replace('\r\n', '\n')
    def matrix(name):
        matches = re.findall(re.escape(name) + r'\s*=\s*\[([^\]]+)\];', text)
        if len(matches) != 1:
            raise ValueError(('Ambiguous matrix', name))
        body = re.sub(r'%[^\n]*', '', matches[0])
        return [row.split() for row in body.strip().split(';') if row.strip()]
    def rows(name, symbolic=False):
        data=matrix(name)
        converted=[]
        fixed={'0':'0','1':'1'}
        symbols={'0':'0','1':'10*u','.1':'u','.9':'9*u','CABi':'c','1-CABi':'10*u-c'}
        mapping=symbols if symbolic else fixed
        for row in data:
            if len(row)!=6: raise ValueError(('Wrong width', name, row))
            converted.append('['+', '.join(mapping[token] for token in row)+']')
        return '['+',\n  '.join(converted)+']'
    result=['import ClinicalModels.PublishedCBT\n\nnamespace ClinicalModels.SourceTables\n']
    for label, name, symbolic in [
        ('spiderDanger','A{1}(:,:,2,1)',False),('spiderSafe','A{1}(:,:,2,2)',False),
        ('arousalDanger','A{2}(:,:,2,1)',False),('arousalSafe','A{2}(:,:,2,2)',False),
        ('affectDanger','A{3}(:,:,2,1)',False),('affectSafe','A{3}(:,:,2,2)',False),
        ('transitionApproach','B{1}(:,:,1)',False),('transitionAvoid','B{1}(:,:,2)',False),
        ('implicitDanger','a{3}(:,:,2,1)',True),('implicitSafe','a{3}(:,:,2,2)',True)]:
        params=' (u c : Int)' if symbolic else ''
        result.append(f'def {label}{params} : List (List Int) :=\n  {rows(name,symbolic)}\n')
    # Record the remaining selected assignments; these are explicit source guards.
    for expected in ["A{4}(:,:,i,j) = eye(6);", "a{3} = a{3}*5;", "d{3} = [1-Psafe Psafe]';", "d{3} = d{3}*50;", "T = 4;", "rng('shuffle')"]:
        if expected not in text: raise ValueError(('Source guard absent',expected))
    result.append('end ClinicalModels.SourceTables\n')
    return '\n'.join(result)

if __name__=='__main__':
    if len(sys.argv)!=3 or sys.argv[1] not in ['--write','--check']:
        raise SystemExit('Usage: source_bridge.py --write|--check /path/to/pinned/CBT_model.m')
    result=render(sys.argv[2]); target=ROOT/'ClinicalModels/SourceTables.lean'
    if sys.argv[1]=='--write': target.write_text(result)
    elif target.read_text()!=result: raise SystemExit('Generated source tables do not match upstream')
    print('PASS: 10 exact source matrices and 6 selected assignments match pinned upstream bytes.')
