# Lean verification receipt

**Result: passed on GitHub Actions using official Lean 4.19.0.**

- Checked commit: `841419eea726383da96e105b3b995910b80f2ed0`.
- Run: https://github.com/Sodelin/Mathematics-of-Psychology-Formalized/actions/runs/36365007772
- Job: `108749531440`; Ubuntu GitHub-hosted runner.
- Toolchain output: `Lean (version 4.19.0, x86_64-unknown-linux-gnu, commit 6caaee842e94, Release)`.
- Commands: source scan, `lake build`, `lake env lean Solidarity.lean`.
- Build completed successfully; all 16 theorem declarations compiled. Eleven public results received explicit `#print axioms` audits.

The retained `ci-output.txt` contains relevant version, build, and axiom lines from the job output. It omits unrelated runner metadata. The workflow is in `.github/workflows/lean.yml`; it runs for research-branch pushes and pull requests. `Solidarity.lean` is unchanged between this verified formal commit and the accompanying research documents; the package manifest records its SHA-256 digest.

The source contains no `sorry`, `admit`, or custom `axiom` declaration. Some audited proofs use Lean's standard propositional extensionality (`propext`) and quotient soundness (`Quot.sound`); others report no axiom dependency. These standard logical dependencies are disclosed rather than described as an axiom-free development. No social-science proposition was introduced as an axiom.

Local execution in this hosted workspace failed before proof checking with `failed to locate application`. Downloading the official release did not resolve that runner-specific issue. Verification therefore used the independent GitHub runner, where the same source and pinned toolchain succeeded. The local failure is not reported as a local proof pass. No sandbox control or Lean trust mechanism was bypassed.

Reproduce from the repository root with the pinned toolchain installed: run `lake build`, then `lake env lean Solidarity.lean`. The model specification explains the interpretation of each theorem. A successful build verifies the formal statements; it cannot validate empirical premises, select political values, or establish the external validity of an intervention.
