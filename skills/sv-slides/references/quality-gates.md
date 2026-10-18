# Quality gates

Table of contents: compile loop, log parser, lint, visual, claims,
sv-write-humanize-slides, ship rule.

## Compile-check loop (at most 4 rounds)

1. `scripts/build.sh` (`latexmk -xelatex`). A PDF that exists after a
   non-zero exit is still a failure.
2. `scripts/check_log.py` on the `.log` (run with `max_print_line=10000`).
3. `scripts/lint_deck.py` on the `.tex`.
4. `scripts/render_pages.sh` at 150 dpi; inspect in batches of 3.
5. After any fix, discard the old PDF audit and re-check the affected
   batch (and later batches if page count shifted).

`build.sh` refuses and names the missing tool or package (`xelatex`,
`latexmk`, `moloch`, `beamertheme-simpleplus`, `ctex`, `pdftoppm`). It
does not install anything.

Setup without admin rights (tested on macOS 13, 2026-10-17): TinyTeX from
the official `rstudio/tinytex` installer into `~/Library/TinyTeX`, then
`tlmgr install beamer moloch ctex xecjk fandol booktabs pgf pgfopts
etoolbox`. Put `~/Library/TinyTeX/bin/universal-darwin` on `PATH` yourself;
pass no argument to the installer script (its first positional argument is
a folder for keeping the downloaded archive). Page rendering falls back to
PyMuPDF when poppler's `pdftoppm` is missing. On macOS 13 Homebrew builds
poppler from source and poppler 26.10 fails there (it needs a newer C++
standard library than Xcode 15.2 provides), so use PyMuPDF
(`python3 -m pip install pymupdf` in a virtual environment) on such machines.

A warning is reported on the page whose `[N` shipout marker follows it in
the log (TeX prints the marker after building the page).

## Log parser

Overfull `\hbox` greater than 10pt is critical; 1 to 10pt is a warning;
under 1pt is ignored. Underfull is informational unless badness is 10000.
Map each warning to a page via `[N` shipout markers. Undefined control
sequence, undefined citation, and multiply-defined labels are critical.

Blind spots (visual pass required): warnings suppressed inside Beamer
blocks; vertical clip with no warning; `\toprule` colliding with the
title bar.

## Source lint (`lint_deck.py`)

Overlay commands = 0; bullets per frame <= 7; coloured boxes per frame
<= 2; `\tiny` = 0; text-only share <= 30%.

## Visual checklist (per page)

Edges, box interiors, CJK glyphs (no missing-glyph boxes), table and
equation width, TikZ overlaps, font consistency, contrast, clutter.
For paper-talk figure slides: open the original figure, then the rendered
page, and compare crop and labels.

## Claims and titles

Never upgrade language beyond the evidence. Associational is not causal.
Title verb strength <= claim level:

- proved: "X implies Y", "is";
- numerical evidence: "In simulation, ...", "reduces ... by ... (n=...)";
- causal under stated assumptions: "Under A1-A3, Z increases Y";
- exploratory / presenter's reading: "suggests", "is consistent with".

Causal verbs on a results slide without listed assumptions fail.

## sv-write-humanize-slides

`audit` with profile `slides` on the deck. `\note{}` with `academic`.
Frame titles may be edited only to downgrade claim strength.

## Ship

No critical overfulls, lint exit 0, visual pass on every box, outline was
approved. Score heuristic: start at 100; compile fail -100; overfull >10pt
-10; ship at 90 or above after at most 4 rounds.
