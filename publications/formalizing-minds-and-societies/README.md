# Formalizing Minds and Societies: Source Pack

This package accompanies the 17-page research article and the 77-page dissertation-style methodological monograph. The monograph expands *How We Formalized Questions About Society* and explains all 67 named Lean declarations in the inspected release.

Start with [the reading guide](reading-pack/README.md), [the complete article](reading-pack/research-article.md), or [the complete monograph](reading-pack/dissertation.md).

| Reading edition | PDF | EPUB |
| --- | --- | --- |
| Research article, 17 pages | [Download PDF](output/pdf/research-article.pdf) | [Download EPUB](output/epub/research-article.epub) |
| Dissertation-style monograph, 77 pages | [Download PDF](output/pdf/dissertation.pdf) | [Download EPUB](output/epub/dissertation.epub) |

The [Astra handoff](../../ASTRA-HANDOFF.md) records the recovered work and continuation instructions. The [recovery record](RECOVERY.md) and [manifest](recovery-manifest.json) document restored-file checks and version relationships. The current repository also contains a separate clinical extension; these editions retain their original 67-result scope.

The PDFs use APA 7 professional-manuscript conventions: title page and author note, abstract, running head and page number, 1-inch page margins, 12-point Times-family type, double-spaced prose, hierarchical headings, author-date citations, hanging-indent references, and separately labeled appendices. The EPUBs preserve the scholarly structure and citations with reflowable text and navigable sections.

The author note identifies the AI-assisted preparation of the manuscripts. The public repository remains the source of record for the Lean development and its authorship. The code was inspected at commit 780f1b83aef15a9cf455566bab9df2a47d738074, with successful CI run 36392008029; this edition reports that verification evidence and adds explanatory synthesis.

The reading folder also includes an exact theorem inventory, a source-access register, the search log, an interpretive relationship map, and RIS/BibTeX metadata for 21 sources. The article cites 17 of these sources. All examples presented as illustrative are synthetic, and the proposed AI study is a research protocol.

## Rebuilding the reading editions

`build_publications.py` consumes the two complete Markdown manuscripts and `manuscript-metadata.json`. It writes PDF and EPUB editions to `output/`. Its dependencies are Python 3, ReportLab, Matplotlib, Pillow, Pandoc, Nimbus Roman Type 1 font files, and DejaVu fonts. The font paths are specified near the top of the script and can be adjusted for another system.

`check_publications.py` checks page geometry, theorem coverage, EPUB XML and internal links, and produces contact sheets. It additionally uses PyMuPDF, lxml, and Poppler's `pdftoppm`. The supplied quality record summarizes these checks; the finished PDFs were also visually inspected.

Run these commands from this directory to render a new edition from the finished manuscripts:

```sh
python3 build_publications.py
python3 check_publications.py
```

To check the existing restored editions without rebuilding, first create the checker's temporary directory with `mkdir -p tmp/pdfs`, then run `python3 check_publications.py`. Rebuilding overwrites the two PDF and two EPUB files in `output/`; preserve the recovery checkpoint in Git before making a revised edition.

## Preserved inputs and production history

The [earlier reader's guide](inputs/how-we-formalized-society.md), [production history](production-history/README.md), and [original source archive](archive/source-pack-as-saved.zip) retain the development of this edition. The original source ZIP is unchanged. Its source-pack README has been expanded here with repository download links and recovery instructions.
