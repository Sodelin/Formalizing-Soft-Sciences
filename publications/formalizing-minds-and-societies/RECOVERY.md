# Recovery record — 29 September 2026

This recovery collected the completed article and monograph, their saved reading editions, the source archive, and remaining production materials into the Git repository at the request of the project owner. [Astra's handoff](../../ASTRA-HANDOFF.md) is the continuation entry point.

## Recovered artifacts

| Material | Location | Recovery status |
| --- | --- | --- |
| Article and monograph PDFs | `output/pdf/` | Restored from the previously saved editions; 17 and 77 pages |
| Article and monograph EPUBs | `output/epub/` | Restored from the previously saved editions |
| Original source pack | `archive/source-pack-as-saved.zip` | Preserved byte for byte; ZIP integrity checked |
| Finished manuscripts, chapters, references, metadata, builder and checker | Package root and `reading-pack/` | Extracted from that source pack; matching local final files agreed byte for byte |
| Earlier reader's guide | `inputs/how-we-formalized-society.md` | Preserved from the full baseline used in this session |
| Draft, assembly and revision scripts, source index and inspection copies | `production-history/` | Recovered from the still-present session workspace |
| Historical rendering records and stylesheet | `production-history/records/` | Preserved as records of the original build |

The historical source pack contains 23 files. The expanded recovery preserves 48 existing files before adding these handoff and recovery documents. Intermediate page images can be regenerated with the supplied checker; they are not included in the Git package.

## Which version is authoritative

The complete Markdown manuscripts in `reading-pack/` are the finished editable versions. The four files under `output/` are the recovered reading editions. The previous guide and the production-history directory preserve lineage; they are not replacements for the final manuscripts.

The PDF byte counts in the original `quality-record.json` describe the locally generated versions. The saved-and-restored PDFs have different byte counts. Recovery compared every page's extracted text and the complete bookmark trees with the original local PDFs: all matched, with the same 17 and 77 pages. Both original local PDFs are retained in `production-history/original-pdf/`, and the recovery manifest records both sets of hashes. No cause for the binary difference is inferred from that comparison.

The two EPUBs and original source archive agree byte for byte with their surviving original local counterparts. The historical records remain unchanged. New recovery findings and hashes are recorded separately in `recovery-manifest.json`.

The inspection copies of Lean and verification files contain one additional terminal newline relative to the pinned Git blobs. Recovery verified this exact difference. The repository's Git blobs at `780f1b83aef15a9cf455566bab9df2a47d738074` remain the authoritative source bytes; the inspection copies are explicitly historical reading inputs.

## Scope and verification

The 67 rows of the publication inventory were reconciled with the seven core source modules, including qualified names and declaration locations. The count is 16 solidarity, 9 measurement, 9 identifiability, 6 causality, 9 learning, 10 collective action, and 8 aggregation. All 67 appear in the core axiom audit.

The manuscripts report the recorded successful Lean 4.19.0 workflow at the inspected release, [run 36392008029](https://github.com/Sodelin/Formalizing-Soft-Sciences/actions/runs/36392008029). Recovery checks cover restored-file integrity, publication structure and coverage, and the repository's existing provenance checks. A fresh kernel build has its own GitHub Actions result and should be read there, rather than inferred from these document checks.

During recovery, main advanced to include the separate 18-declaration clinical extension and a current [85-result coverage map](../../PUBLICATION-COVERAGE-2026-09-29.md). The publication package was prepared against `7835157627548823f03f29dd3987e55601807b55`, preserving those changes. The seven core modules and core audit are unchanged from the manuscripts' source revision.

No live reference-manager collection, external submission, email, or message is created by this recovery. The package is available for further review and use through Git.

## Recheck recovered bytes

Run from this directory:

```sh
python3 - <<'PY'
import hashlib, json
from pathlib import Path
root = Path('.')
manifest = json.loads((root / 'recovery-manifest.json').read_text())
for record in manifest['files']:
    path = root / record['path']
    assert path.stat().st_size == record['bytes'], record['path']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == record['sha256'], record['path']
print('All recorded recovery hashes match.')
PY
```

The manifest excludes itself and generated temporary images. Each included file is independently recorded so a later edition can retain this recovery as a stable checkpoint.
