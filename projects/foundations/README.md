# Foundations I: measurement, models, and collective action

**Version 0.2 · 28 September 2026 UTC · Formalizing Soft Sciences**

This expansion moves beyond small groups into reusable foundations for psychology, sociology, ethnology, and anthropology. It adds **51 checked theorem declarations in six modules**, alongside the preserved 16 in `Solidarity.lean`. The count includes supporting lemmas and concrete examples, not 51 discoveries.

Start with the **[research report](report.md)** for the results, their uses, and their limits. The **[theorem guide](theorem-guide.md)** explains every addition. The **[research problem register](open-problems.md)** separates completed model questions from proposed extensions and unresolved field questions.

| Foundation | What the code establishes | Research use |
| --- | --- | --- |
| [Identifiability](../../SocialScience/Identifiability.lean) | Some probes leave mechanisms indistinguishable; a distinguishing probe can identify the parameters. | Design measurements that can separate rival explanations. |
| [Measurement](../../SocialScience/Measurement.lean) | An additive score has an origin ambiguity; anchors and explicit bias bounds change what can be inferred. | Explain the assumptions behind group comparisons. |
| [Causality](../../SocialScience/Causality.lean) | Two causal models can produce identical observations and different intervention effects. | Find where an observational causal claim needs additional assumptions. |
| [Learning](../../SocialScience/Learning.lean) | Exact evidence constrains hypotheses; conflicting or incorrect labels can eliminate the true model. | Distinguish logical learning models from accounts of noisy human learning. |
| [Collective action](../../SocialScience/CollectiveAction.lean) | Complementary capabilities can make cooperation feasible; total surplus alone does not ensure participation. | Separate production, distribution, and incentives. |
| [Aggregation](../../SocialScience/Aggregation.lean) | A pooled comparison can reverse both within-context comparisons; recoding cannot recover information already lost. | Check what cross-group or cross-cultural summaries conceal. |

The mathematical content is elementary and established in character. The contribution here is a checked, connected teaching and research scaffold. No field-level open problem has been solved or novel empirical law established. [Prior work and access records](sources/references.md) support that assessment; the search was targeted rather than exhaustive.

## Read and reproduce

- [All 51 new theorem explanations](theorem-guide.md) and [machine-readable inventory](theorem-inventory.csv).
- [Verification receipt](verification.md), [Lean output](formal-check-output.txt), and [source hashes](verification-manifest.json).
- [References](sources/references.md), [BibTeX](sources/references.bib), [search log](sources/search-log.md), and [source relationships](sources/source-relations.csv).
- [Psychology applications and prior-work import status](../../psychology/README.md).
- [Publication and review plan](publication.md).

From the repository root, with the pinned Lean toolchain installed:

```sh
lake build
lake env lean SocialScience/Audit.lean
python3 scripts/check_foundations.py
```

The original [Solidarity at Scale paper and report](../solidarity-at-scale/README.md) remain available. Its guide explains the original 16 theorems; this guide covers the 51 additions. The larger earlier mathematics-of-psychology corpus still awaits its original source location. This expansion does not replace or claim to import it.
