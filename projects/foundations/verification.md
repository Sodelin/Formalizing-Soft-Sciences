# Verification receipt: Foundations I

The 51 new and 16 preserved theorem declarations passed Lean 4.19.0. This receipt identifies the proof-source check; the repository's workflow separately checks subsequent documentation commits and main.

| Item | Recorded result |
| --- | --- |
| Checked source commit | [`099908b5d781adc2d5bcdecfe909e57ec75776c4`](https://github.com/Sodelin/Formalizing-Soft-Sciences/commit/099908b5d781adc2d5bcdecfe909e57ec75776c4) |
| Successful workflow | [Run 36369678567](https://github.com/Sodelin/Formalizing-Soft-Sciences/actions/runs/36369678567) |
| Job | 108763148520, conclusion `success` |
| Toolchain | Lean 4.19.0, compiler commit `6caaee842e94`, Linux x86_64 |
| Build | `lake build`, both libraries |
| Full declaration audit | `lake env lean SocialScience/Audit.lean`, all 67 declarations |
| Source policy | No admitted goals, custom axioms, or native decision shortcuts in the project's Lean sources |
| Logical dependencies | Only `propext`, `Classical.choice`, and `Quot.sound`, or no axioms |
| Existing work | `Solidarity.lean` retained unchanged; its 16 declarations remain in the audit |

The [saved check output](formal-check-output.txt) includes the build result and logical dependencies. The [manifest](verification-manifest.json) records SHA-256 digests of all nine Lean files and the two toolchain/build configuration files. Later commits may add documentation without changing those checked source bytes. The check script refuses a hash mismatch rather than assuming that a later file still has the old verification status.

The initial [staging run](https://github.com/Sodelin/Formalizing-Soft-Sciences/actions/runs/36369590300) failed because three rate comparisons needed their named predicate unfolded before Lean could select decidable arithmetic. The fix changed only those proof scripts; the next run passed. This failed attempt is part of the provenance and was not represented as a successful check.

The local Lean launcher returned `error: failed to locate application`, so no successful local compilation is claimed. Compilation occurred on GitHub Actions using the official pinned Lean release. No independent external proof checker, adversarial proof audit, or human peer review was performed. Standard kernel checks and the documented dependencies establish logical derivability of the written statements; they do not establish empirical applicability or novelty.

## Reproduce from the repository root

```sh
lake build
lake env lean SocialScience/Audit.lean
python3 scripts/check_foundations.py
python3 projects/solidarity-at-scale/scripts/validate_project.py --check-only
```

The Python checks verify documentation structure, theorem coverage, hashes, and recorded audit content. They do not run Lean themselves. The workflow runs the build and these checks separately. The earlier validation script's `--check-only` option preserves its historical manifest.
