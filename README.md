# Deadline-Constrained Online Allocation

Private theoretical manuscript by Kamiar Asgari on online allocation with
lossless scalar storage and a hard service deadline for every arrival.
The manuscript compares the controller with fixed distributions over service
ages, each evaluated on its own storage trajectory.

This repository contains a draft paper, not an implementation or an empirical
evaluation. The author disclosure in the manuscript states that AI generated the
paper apart from the author's overarching problem idea. That disclosure remains
part of the source.

## Files

- [main.tex](main.tex): manuscript entry point, statements, and proofs.
- [references.bib](references.bib): BibTeX references.
- [main.pdf](main.pdf): tracked PDF; rebuild after source changes.
- [novelty-check.md](novelty-check.md): dated literature comparison and its limits.

## Build

Use PDFLaTeX and BibTeX with the packages listed at the top of `main.tex`.
From the repository root, create a temporary output directory and run:

```text
mkdir tmp
mkdir tmp/build
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=tmp/build main.tex
bibtex tmp/build/main
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=tmp/build main.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=tmp/build main.tex
```

If the directories already exist, skip the `mkdir` commands. The result is
`tmp/build/main.pdf`; the tracked `main.pdf` is not replaced. Check the final
`main.log` and `main.blg` for unresolved references, citations, and warnings.
For MiKTeX, add `--disable-installer` to compiler commands when an offline build
is required; install missing packages separately before building.

A November 1, 2026 PDFLaTeX/BibTeX check produced 38 pages with no unresolved
citations or references. The final log retained one underfull line warning and
the expected package warning about disabled shell escape. The tracked PDF was
not replaced, and no mathematical or visual review is claimed by that check.

## Before publication

The literature note is a dated comparison, not proof of priority or mathematical
correctness. Author review of the assumptions, proofs, attribution, and AI
disclosure remains necessary. In particular, the stated storage lower bound
allows signed state marginals; it does not establish the same result for ordinary
nonnegative holding costs. The action-only bounds retain a deadline-dependent
gap, so the draft should not be described as fully minimax optimal.

Choose the final manuscript version, venue, license, and publication timing
separately. This repository remains private.
