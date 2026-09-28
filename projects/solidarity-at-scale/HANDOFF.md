# Handoff and reproduction

The initial project contains a manuscript, separate decision report, 35-source register and BibTeX, typed claims, quantitative extraction, historical comparison, proposed empirical protocol, staged Obsidian notes, and Lean models. Paper and report are supplied as Markdown, editable DOCX, and PDF. The branch is `research/solidarity-at-scale-2026-09-27`; changes are for review and are not to be merged automatically.

Lean: from repository root run `lake build` and `lake env lean Solidarity.lean` with Lean 4.19.0. GitHub Actions already passed the formal source at the commit recorded in formal/verification-report.md. The local hosted runner could not start Lean; do not erase that distinction. No Mathlib installation is required.

Documents: install python-docx, then run `python projects/solidarity-at-scale/scripts/build_documents.py`. Render each DOCX with LibreOffice to PDF, using a separate temporary output directory. The execution environment used its document renderer with `--emit_pdf`, then visually reviewed every output page. Copy the final PDFs to outputs/ after checking page layout. Document content is generated from the Markdown and references file; edit those sources before rebuilding.

Validation: run `python projects/solidarity-at-scale/scripts/validate_project.py`. It checks cross-file source IDs, report numbering, bibliography IDs, proof placeholders, and deliverable presence, and records SHA-256 hashes. It does not substitute for Lean, source appraisal, or visual review. Output binaries may differ across rendering environments even when text agrees.

Zotero: import sources/references.bib into a project collection. Review catalog-only and abstract-only notes before attaching full text. Import notes/ into an Obsidian vault only after choosing the destination. Directional evidence relations are in evidence/source-relations.csv; Zotero’s symmetric Related field cannot preserve their meaning without an accompanying note. No live collection or vault synchronization occurred.

Next research tasks are specific: obtain decisive abstract-only full texts; conduct an independent extraction check; expand the historical sequence and critical perspectives; preregister a coherent next review pass; then evaluate the proposed experimental design. Migration, constitutional arrangements, and the colonial coalition counterfactual remain separate studies. The promised YouTube video or transcript is still absent.

Continuation brief: keep claim types separate; preserve the user’s hypotheses as testable questions; do not turn Lean assumptions into empirical findings; compare effectiveness against stated outcomes and values; retain nulls and failed transfer; update access notes whenever a reading moves beyond an abstract; change conclusions when stronger evidence warrants it. Continue on the review branch and retain unmerged work.
