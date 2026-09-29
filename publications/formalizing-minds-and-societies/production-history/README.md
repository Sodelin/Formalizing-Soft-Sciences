# Historical production materials

These files preserve the writing and rendering work that preceded the finished publications.

- `article-draft.md`: the article input used by the assembly script.
- `assemble_manuscripts.py`: the session's manuscript, inventory, and bibliography assembly script.
- `refine_manuscripts.py`: a one-time revision script that expects earlier exact text and updates several files in place. It is not an idempotent rebuild command.
- `theorem_source_index.json`: the declaration index used during assembly.
- `inspected-source/`: the source copies used for reading and extraction, pinned in the manuscripts to the recorded Git revision. Each has one extra terminal newline relative to that revision.
- `records/`: the original build report, quality-check report, and generated EPUB stylesheet. Absolute paths in these historical reports describe the original temporary workspace.
- `original-pdf/`: the original locally rendered PDFs, preserved alongside the saved-and-restored reading editions.

The assembly and revision scripts originally ran in the session workspace with their inputs at its root. Their paths and one-time edits are preserved as historical code. Use the finished Markdown manuscripts and the current package-root `build_publications.py` to rebuild a reading edition. Consult `../RECOVERY.md` for the version relationships.
