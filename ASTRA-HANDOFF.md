# Astra: recovered publications and continuation state

The article, dissertation-style monograph, all four reading editions, the original source archive, and the production materials from the document-building session are now collected in [publications/formalizing-minds-and-societies](publications/formalizing-minds-and-societies/README.md). This handoff makes the work available through the repository rather than depending on chat memory or temporary files.

## Start here

| Work | Read | Edit or inspect |
| --- | --- | --- |
| Research article, 17 pages | [PDF](publications/formalizing-minds-and-societies/output/pdf/research-article.pdf) · [EPUB](publications/formalizing-minds-and-societies/output/epub/research-article.epub) | [Complete Markdown](publications/formalizing-minds-and-societies/reading-pack/research-article.md) |
| Dissertation-style monograph, 77 pages | [PDF](publications/formalizing-minds-and-societies/output/pdf/dissertation.pdf) · [EPUB](publications/formalizing-minds-and-societies/output/epub/dissertation.epub) | [Complete Markdown](publications/formalizing-minds-and-societies/reading-pack/dissertation.md) |
| All 67 core results | [Theorem atlas](publications/formalizing-minds-and-societies/reading-pack/02-theorem-atlas.md) | [Exact inventory](publications/formalizing-minds-and-societies/reading-pack/theorem-inventory.csv) |
| Earlier book used as the baseline | [How We Formalized Questions About Society](publications/formalizing-minds-and-societies/inputs/how-we-formalized-society.md) | Preserved input, including its original source appendix |
| Recovery evidence | [Recovery record](publications/formalizing-minds-and-societies/RECOVERY.md) | [Manifest](publications/formalizing-minds-and-societies/recovery-manifest.json) |

## Resolve the 16, 67, and 85 counts

- **16**: the original `Solidarity.lean` declarations. The older solidarity PDFs explain this stage.
- **67**: those 16 plus **51** in six `SocialScience` modules. They were already on main at `780f1b83aef15a9cf455566bab9df2a47d738074`, the source revision inspected for these manuscripts.
- **85**: the 67 core declarations plus **18** in the published-CBT fragment. The clinical branch was integrated separately through PR 2 during this recovery. See the [current publication coverage map](PUBLICATION-COVERAGE-2026-09-29.md).

The recovered books explain the 67-result release. Their titles and historical source pins remain correct. They do not yet incorporate the clinical extension. The seven core proof modules and their audit have identical Git blob content at the inspected release and the integration base `7835157627548823f03f29dd3987e55601807b55`.

This document-building session produced explanatory research and publication artifacts. It did not add new Lean declarations. Its substantial addition is a connected account of every core result, its assumptions, proof structure, scientific uses, disciplinary context, and possible use in AI research.

## What was completed

The article is approximately 3,300 words and cites 17 sources. The approximately 18,200-word monograph cites 21 sources, explains all 67 named declarations, develops worked arguments and proof anatomy, and includes eight tables and eight appendices. Both include author–date citations and reference lists. The PDFs use APA 7 professional-manuscript conventions; the EPUBs preserve the scholarly structure in a reflowable format. The byline is the project, with an author note identifying AI assistance.

The package also contains the chapter files, a source-access register, search log, interpretive source map, RIS and BibTeX records, rendering and checking scripts, historical quality records, the previous reader's guide, and the session's assembly and revision scripts. The unchanged original source ZIP is retained alongside the expanded recovery.

The scientific narrative connects mathematical and computational psychology, formalization across biological and social disciplines, minimal models of social systems, proof assistants, and a proposed evaluation of verified material for AI reasoning. Context, retrieval, checker use, and parameter-updating training are distinguished. The AI transfer study remains a proposed experiment.

## Editorial direction to preserve

Write for mathematical psychologists, researchers, and serious science communicators. Lead with the most useful result and explain why it matters. Present minimal mathematical representations as productive starting points that isolate mechanisms and support deliberate extensions. Explain the strength and generality of each result inside its stated assumptions, and connect boundaries to the next research question.

Keep the prose lively, concrete, and professionally enthusiastic. State the contribution clearly: a connected, inspectable artifact combining definitions, proofs, counterexamples, explanations, and verification evidence. Attribute established mathematics and prior work accurately. The public manuscripts should address their scientific audience rather than address the requester personally.

## Continue from the finished manuscripts

1. Read the article and the [decision brief](publications/formalizing-minds-and-societies/reading-pack/00-decision-brief.md), then consult the atlas and [proof chapter](publications/formalizing-minds-and-societies/reading-pack/03a-anatomy-of-proofs.md).
2. Edit the complete Markdown manuscripts for a new edition. Use the documented publication builder to render them. The historical assembly and revision scripts are preserved for provenance; some depend on earlier text states and should not be run over the finished files.
3. If expanding to the current 85-result corpus, give the clinical material its own source audit and explanatory chapter, update the inventories and citation coverage, and issue an explicitly revised edition.
4. Before scientific distribution, arrange domain review of the interpretations and source coverage. Public repository availability and independent scientific review have separate records.

The latest clinical checkpoint retained the published-model fragment and paused an original-model proposal pending a prior-art-first review. That separate line of work is not silently restored by this recovery.

## Remaining recovery boundary

The material available from this document-building session has been recovered. A distinct, older psychology corpus mentioned in the historical repository documentation remains unlocated; see [psychology/README.md](psychology/README.md). The 67-result package is located and accounted for. Additional material from unavailable conversations must be recovered from its actual files or repositories before it can be added.

## Verify and reproduce

From the repository root:

```sh
python3 scripts/check_foundations.py
python3 projects/solidarity-at-scale/scripts/validate_project.py --check-only
```

For kernel checking, use the pinned Lean toolchain and the commands in the existing [foundations receipt](projects/foundations/verification.md) and workflow. Publication rebuilding and restored-file validation are described in the [publication README](publications/formalizing-minds-and-societies/README.md). The manifest records recovered content hashes, the historical input revision, and the recovery checks; it is not a substitute for a Lean build.
