# Source questions, predecessors and the exact contribution

Accessed 29 September 2026. These are source-to-claim comparisons, not endorsements by the cited authors. Existing F and N identifiers refer to the preserved [foundations bibliography](../../projects/foundations/sources/references.md) and [formalization bibliography](../../projects/solidarity-at-scale/sources/formalization-prior-work.md). The current audit records improved access separately from those historical reading receipts.

## Model identification and experimental design

**Wilson and Collins (2019), F02.** [Published article](https://doi.org/10.7554/eLife.49547), [open full-text XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6879303/fullTextXML). The sections on parameter recovery and arbitration between models recommend checking whether a design and fitting procedure distinguish the candidate explanations in simulated data. The exact integer probes in this repository illustrate an idealized structural issue preceding estimation. They do not resolve the authors' broader model-recovery challenge. Access improved from abstract/captions to selected full-text sections; the journal XML was read alongside the author's longer manuscript, whose section numbering differs.

## Measurement comparability

**Putnick and Bornstein (2016), F03.** [Published review](https://doi.org/10.1016/j.dr.2016.06.004), [archived article](https://pmc.ncbi.nlm.nih.gov/articles/PMC5145197/). The scalar-invariance section identifies intercept equality as part of measurement comparability. The repository verifies integer additive cancellation, shift invariance and a conditional bias interval. Those results isolate one algebraic mechanism; they do not replace a measurement model or solve the review's empirical and methodological research agenda. Access here: publisher/search-indexed full-text excerpts of the scalar-invariance section; direct PMC displayed a challenge and the Europe PMC XML request returned HTTP 500. No complete fresh reading is claimed.

## Causal non-identification

**Shalizi and Thomas (2011), F04.** [Author preprint](https://arxiv.org/html/1004.4704), sections 1-2. Their network argument shows why separating homophily and contagion requires additional assumptions. Our two Boolean models provide a simpler exact observation/effect collision, with a universal-estimator impossibility consequence. They neither implement that network model nor remove its assumptions. The existing F05 positive-identification reference remains relevant to the fact that restrictions can restore identification; no historical future-work suggestion is asserted to remain open today.

## Version-space learning and related Lean work

**Mitchell, F08.** The version-space framework retains hypotheses consistent with the observations; the original bibliography records the inspected textbook slides. A fresh route located the [author-hosted dissertation](https://www.cs.cmu.edu/afs/cs/usr/mitchell/ftp/pubs/VERSION_SPACES_MitchellPhDthesis.pdf), but its text extraction was largely unusable; no additional full reading is claimed.

**Cslib, current related formalization.** [Official API documentation](https://api.cslib.io/docs/Cslib/MachineLearning/PACLearning/VersionSpace.html) and [pinned source](https://github.com/leanprover/cslib/blob/d9be64196bf145edd019f1ccfeaee0c11166ba6b/Cslib/MachineLearning/PACLearning/VersionSpace.lean). The inspected declarations include `versionSpace_empty_sample`, `versionSpace_reindex` and `versionSpace_antitone`, directly related to our empty-evidence and monotonicity properties. This establishes related public formal content as observed today; this pass did not audit its first-commit date or independently rebuild it. No priority assertion relies on that chronology.

## Aggregation

**Simpson (1951), F09.** [Publisher record](https://doi.org/10.1111/j.2517-6161.1951.tb00088.x), [university-hosted scan](https://math.bme.hu/~marib/bsmeur/simpson.pdf), printed pages 240-241, sections 8-11. The paper analyzes how amalgamation can change the interpretation of within-stratum associations. Its example and table values differ from this repository's strict reversal. The new file verifies a synthetic instance of established aggregation behavior; it is not a solution to a newly open Simpson problem. Access improved to the relevant full-text pages.

## Published computational-model fragment

**Smith, Moutoussis and Bilek (2021).** [Paper](https://doi.org/10.1038/s41598-021-89047-0), [open full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8115057/fullTextXML), [pinned MATLAB source](https://github.com/rssmith33/Simulating_Cognitive_Behavioral_Therapy/blob/82a0a3d75b0bdc08d2b78cdf2201d7aa626c27a3/CBT_model.m). Decisive locators are the model section/Figure 2, section *Ineffective CAB interactions* (XML Sec6, paragraph 2), and Discussion (Sec11, paragraphs 2, 9, 12-13). The authors already attribute persistence of avoidance to unavailable corrective observations. Our no-perfect-classifier result states the information limitation exactly for the selected deterministic fragment; the approach theorem gives its paired recovery statement. The weight identities and four source bridges check the reconstruction. Future discussion of context, uncertainty, attention and learning is not answered by these declarations. Direct publisher/PMC retrieval failed; the open Europe PMC journal XML succeeded. This audit read the decisive model, results and discussion passages, not every cited clinical study.

## Earlier formalization precedent and venue fit

**Nipkow (2008/2009), N01.** The [Archive of Formal Proofs entry](https://isa-afp.org/entries/ArrowImpossibilityGS.html) records Isabelle/HOL proofs of Arrow and Gibbard-Satterthwaite results. **Holliday, Norman and Pacuit (2021), N02/F10.** The [primary preprint](https://arxiv.org/abs/2110.08453) describes Lean voting-theory formalization. Their relevance is established proof-assistant work in social choice; our elementary package does not supersede those developments. Entry/abstract records were freshly checked, without rebuilding the external projects.

[VibeMathed's methodology](https://vibemathed.com/methodology) provides the catalog distinction used in the publication judgment: formal verification of an already established result has a different status from a new answer to an open mathematical question. The package remains valuable and publicly inspectable under its actual formalization and source-audit claim.
