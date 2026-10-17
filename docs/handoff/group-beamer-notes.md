# group-beamer: reference notes (Step 1)

Date: 2026-10-17. Prompt: `docs/handoff/group-beamer-PROMPT.md`. Every
LICENSE was opened and checked; cloned and fetched content was read as data.
Part A covers layout, pipeline and templates; Part B covers statistics and
causal talk writing plus the humanizer.

## Corrections to the prompt's assumptions

1. **TeX is not installed** on SG, the Mac Studio or the iMac (`latexmk`,
   `xelatex`, `kpsewhich`, `pdftoppm`, `chktex` all missing). Step 4 needs
   an install decision first.
2. **SimplePlus** lives at `pm25/SimplePlus-BeamerTheme` (Unlicense), also on
   CTAN as `beamertheme-simpleplus`.
3. **SYSU template is not cleanly CC0**: the repo LICENSE says CC0 but
   `sysu.sty` says LPPL and/or GPL (inherited from ruc.sty), and the logos are
   university marks. Do not vendor; reuse only facts (colours).
4. **Moloch** ships as `.dtx` only (generate 7 `.sty` with docstrip) and is
   on CTAN/TeX Live. Unmodified vendoring is aggregation (files stay
   CC-BY-SA); any modified Moloch must stay BY-SA, which our NC-SA cannot
   carry. A separate wrapper that only sets colours can stay NC-SA.
5. **Overlays**: beamer-skill and the prompt ban `\pause`; Ramdas allows
   builds. Proposed: no overlay commands, use frame duplication with muted
   earlier items (beamer-skill pattern).
6. **No box-size checker exists** in any reference; all only count
   `Overfull \hbox` lines. Beamer also suppresses warnings inside blocks, so
   a visual pass is mandatory. A log parser is our own work.
7. **paper-to-latex-ppt renders with PyMuPDF**, not pdftoppm.
8. **"Critic workflow attack checklist"**: not found in this repo; the
   only match is the MSR-TPA annotation Critic Attack/Judge (labels, not
   papers). Proposed substitute: `pre-submission-reviewer`
   `devils-advocate-pass.md` plus `research-core` `fields/causal.md` "What
   reviewers and advisors care about".
9. `deai-writing` profile selection sends every `.tex` to `academic`; a
   `slides` profile needs Beamer detection first.

# Part A: layout, pipeline, templates

Date: 2026-10-17. All repos were shallow-cloned into `scratchpad/refs/` and read as untrusted data. I opened every LICENSE file myself.
Environment note: on SG, `latexmk`, `xelatex`, `kpsewhich`, `pdftoppm` and `chktex` are **not on PATH**, so nothing was compiled here. Every claim below comes from reading the source.

## License summary

| Repo | Verified license | Copyright line | Can we copy text/code? |
|---|---|---|---|
| Noi1r/beamer-skill | MIT (`LICENSE`) | `Copyright (c) 2026 Noi1r` | Yes, if we keep the MIT notice |
| Master-cai/Arxiv2beamer | **No license** (no LICENSE file; README/SKILL.md never mention a license) | none (all rights reserved by default) | **No.** Ideas only, and we restate them in our own words |
| moyoo0/paper-to-latex-ppt | MIT | `Copyright (c) 2026 moyoo0` | Yes, if we keep the MIT notice |
| pedrohcgs/claude-code-my-workflow | MIT | `Copyright (c) 2026 Pedro H. C. Sant'Anna` | Yes, if we keep the MIT notice |
| takashiishida/paper2slides | MIT | `Copyright (c) 2024 Takashi Ishida` | Yes, if we keep the MIT notice |
| jolars/moloch | CC-BY-SA-4.0 (`LICENSE` full legal text; every `.dtx` header says the same) | `Copyright 2015 Matthias Vogelgesang and the LaTeX community` (Metropolis lineage) + `Copyright 2024 Johan Larsson and contributors` (2025 for highcontrast) | Unmodified vendoring is OK, but those files stay BY-SA (see Templates) |
| pm25/SimplePlus-BeamerTheme (canonical; `pm25/SimplePlusTheme` does not exist) | Unlicense (public domain) | sty header: `Author: Pin-Yen Huang`, v1.1 2025-01-07, "released into the public domain" | Yes, with no obligations |
| yxnchen/sysu-beamer-template | Repo `LICENSE` = CC0 1.0, **but** the `sysu.sty` header says "LaTeX Project Public License and/or GNU Public License" (inherited from ruc.sty) | `Author: Yixian Chen`, 2020, "Modified from ruc.sty" | **Ambiguous. Do not vendor** (see Templates) |

Our repo is CC-BY-NC-SA-4.0. MIT material can be included as long as each copied file or block keeps its MIT notice. That notice is the only obligation, and the NC/SA terms then cover only our own additions. Paraphrased rules and numbers are not copyrightable expression, but credit the source anyway in `NOTICE`/README.

Lineage note: beamer-skill's 13-pattern pedagogy table, the "spacing-first" fix order, and the "max 2 boxes" and "no \pause" rules match pedrohcgs's `pedagogy-reviewer.md`, `slide-auditor.md` and `content-invariants.md` nearly word for word. Both are MIT, so credit both.

---

## 1. Noi1r/beamer-skill (MIT)

Files read: `LICENSE`, `beamer/SKILL.md` (1049 lines, read in full), `beamer/references/review-actions.md` (head), grep over `beamer/AGENTS.md` and `references/create-workflow.md`.

**Borrow (concrete rules and numbers):**
- Bullets: telegraphic. Each bullet <= 2 lines (about 15 words), otherwise split or rewrite.
- Per-slide upper bounds: <= 7 bullets, <= 2 display equations, <= 5 new symbols, <= 2 coloured boxes.
- Per-slide lower bound: at least one substantive element (formula, diagram, table, theorem or algorithm). A slide with <= 3 short text-only bullets must be merged or enriched. Text-only slides <= 30% of the deck. After each batch, flag the batch if more than 30% of its slides have no formula, figure or table.
- No overlays: `\pause`, `\onslide`, `\only`, `\uncover` are banned. Replacement patterns: build a formula up by duplicating the frame and greying earlier terms; reveal a list across successive frames with earlier items muted; build a TikZ diagram by duplicating it and only adding elements.
- Boxes: content inside a box is one display equation **or** 2-3 short bullets, never both. No `\qquad` inside a box. An equation wider than about 70% of `\textwidth` must be reformatted before boxing. No negative `\vspace` inside boxes. **Beamer suppresses overfull warnings inside blocks**, so every box needs a visual check.
- Pacing: about 1 slide per 1.5-2 min. Timing table: 20 min gives 13-18 slides, 45 min gives 22-30. 40-50% of time goes to core content. At most 3-4 consecutive theory slides before an example or visual break. Section divider every 5-8 slides. Worked example within 2 slides of each definition. Theorem and proof go on separate slides; a long proof gets a sketch in the main deck and the full proof in backup.
- Outline gate (Phase 2): per section, give the title, slide count, 1-2 lines of content per slide, planned figures and new notation. **Do not draft until the user approves.** Draft in batches of 5-10 slides, compiling after each batch.
- Ending: References is the second-to-last slide, then Thank-you, then `\appendix` with 3-5 backup slides behind a divider frame. Backup slides are excluded from timing and hyperlink back to the main slide they support.
- Tables: booktabs, no vertical rules, centred, `\vspace{4pt}` before a `\toprule` directly under the frame title (visual-only failure, no warning). At most 6-7 columns and 8-10 rows. On a split, repeat the header, title the slide "(cont'd)", split at group boundaries, and keep >= 3 rows on the last page. `\resizebox` is a last resort.
- Columns: 0.48/0.48 for comparisons; figure 0.45-0.55 with text 0.40-0.50; at most 3 columns of <= 0.30 each; never nested; `[T]`.
- Fonts: never `\tiny`; `\footnotesize` is the last resort. TikZ labels >= `\footnotesize`.
- TikZ: compute on-curve points with `\pgfmathsetmacro` from the same function, never hard-coded. Usable height is about 70 mm below the title at 16:9/10pt. Flow width <= 14 cm. Solid means observed, dashed or hollow means counterfactual (directly useful for causal-inference DAG and potential-outcome plots).
- Colour: blue/orange colour-blind-safe palette (0173B2, DE8F05, 029E73, CC78BC), contrast >= 4.5:1, no red/green binary pairs, 3-5 colours in total.
- Check procedure (`validate`): from `pdfinfo`, read page count against duration, aspect ratio, and file size (warn > 50 MB, critical > 100 MB). Then `grep -c` the log for `Overfull \\hbox`, `Undefined control sequence`, `Citation.*undefined` and `multiply defined`. Static source checks: overlay commands = 0, slides with > 2 boxes, `\tiny` = 0, references slide present.
- Visual check (`visual-check`): PyMuPDF renders each page at 200 dpi to `slide-NNN.jpg` (fallback: read the PDF directly), followed by an 8-item per-slide checklist (edges, box interiors, legibility, table/eq width, TikZ overlaps, font consistency, contrast, clutter).
- Quality loop: start at 100 and deduct (compile fail -100, equation overflow -20, TikZ clipped -15, undefined ref -15, overfull hbox > 10pt -10, box overflow -10/box, sparse slide -5, etc.). A score >= 90 ships, at most 3 rounds.
- Figure extraction: `pdftoppm -png -r 300 -f P -l P paper.pdf figures/page`, or `pdfimages` for raw bitmaps. Then `trim/clip`, warn if < 800 px wide, never rasterise tables, and always add a "Source:" line.

**Do NOT borrow:**
- The Madrid preamble and the hard-coded `\institute{Shanghai Jiao Tong University}` default.
- The raw `xelatex`+`bibtex`×3 sequence; we use `latexmk -xelatex`.
- The domain-specific crypto bullets (prover cost, soundness).
- The "Never end on Thank You" vs. "Thank-you slide" ambiguity. Pick one convention ourselves.

## 2. Master-cai/Arxiv2beamer (NO LICENSE: ideas only)

Files read: `SKILL.md` (175 lines in full); `README.md`/`README_CN.md` grepped for a license (none found).

**Ideas to restate in our own words (do not copy any text):**
- Outline-first gate: before planning any slides, rebuild the paper's own section tree down to sub-subsection level. Where a section has no headings, use paragraph-level logical units. Then map each paper block to one or more slide groups, keeping the paper's order unless readability forces a change. This fits paper-talk mode directly.
- Visual audit in small batches of fewer than 4 pages. For each slide image, first open the **original** figure file, then the rendered page, and compare: is any semantic region missing, are labels/legends/axes/captions cropped, is the figure occluded, or did trim/clip lose content.
- Snapshot discipline: audit results belong to one immutable PDF. After any edit and recompile, discard results from the old PDF and re-audit the affected batch plus later batches if the layout shifted. Serial mode stops at the first failing batch. Parallel subagents are allowed, one batch each.
- Final report gives the rewritten range, audit rounds, and remaining risks with page numbers.
- Faithfulness: claims, numbers and method names must come only from the source; where information is missing, use conservative wording.

**Do NOT borrow:** stripping all `\cite`/`\bibliography` (we want a references slide); wrapping every table in `\resizebox{0.95\textwidth}` (it conflicts with the "resizebox last resort" rule); the hard dependency on a `pdf-vision` MCP; editing only after `\section{Introduction}`.

## 3. moyoo0/paper-to-latex-ppt (MIT)

Files read: `LICENSE`, `SKILL.md`, `references/workflow.md`, `scripts/inspect_pdf_pages.py`, `scripts/build_latex_pdf.py`, `scripts/add_speaker_notes.py` (first 80 lines), `assets/beamer_template/main.tex`, grep of `macros.tex` (it loads `\usepackage[UTF8]{ctex}` with Metropolis).

**Borrow:**
- Chinese group-meeting default: about 15 slides (12-18) for 15-25 min. Its 15-slide skeleton (title, background, motivation/gap, problem setup and notation, method overview figure, module 1, module 2, core formula/objective, train/infer flow, setup, main results, ablation, case/error analysis, limitations and discussion points, takeaways) is a good paper-talk default. For causal inference, swap the ML slots for identification assumptions, estimand, estimator, and theory.
- Speaker notes per page, written from the **final rendered** slides rather than the early outline. Each page's notes cover:
  - the main point;
  - each symbol in each formula, what the formula does, and how it connects to the slides before and after;
  - each figure's modules, arrows, colours, curves, axes, legend and conclusion;
  - a spoken transition sentence.
- Extra note questions from workflow.md: why does this page exist? How does the figure or formula support the claim? What is the audience likeliest to misunderstand? How do I move to the next page?
- Notes format: `# Slide N` or `## Slide N` headings (the regex also accepts `第N页`), plus an auditable `speaker_notes.md`/`.json` sidecar. For Beamer we would emit `\note{}` or a separate notes file instead of PPTX injection.
- Per-run output directory `output/YYYYMMDD_<name>/` holding `slide_plan.json`, `slides.tex`, `slides.pdf` and `page_images/`.
- Inspection script idea: render every page at 220 dpi with PyMuPDF (**not pdftoppm**, contrary to the brief). Flag pages with fewer than 10 extracted text characters (possible blank or image-only page) and pages rendered below 1200x700 px. Write `inspection.json` with `manual_review_required: true`. Its checklist adds "CJK glyphs render correctly (no missing-glyph boxes)".
- Fix strategies: break long formulas with `aligned`/`split`; crop to key subfigures; move text into the notes; set only width or height on an image, never both; add a one-line takeaway on result figures.
- Build script: try `latexmk -pdf -xelatex -interaction=nonstopmode -halt-on-error`, fall back to `xelatex`, and keep the log.

**Do NOT borrow:** the PDF-to-PPTX rasterisation, `python-pptx` note injection, and Metropolis/DeepBlue macros. Also avoid "install missing deps then continue", because global CLAUDE.md forbids unrequested installs.

## 4. pedrohcgs/claude-code-my-workflow (MIT)

Files read: `LICENSE`, `.claude/skills/credible-claims/SKILL.md`, `.claude/agents/slide-auditor.md`, `.claude/agents/pedagogy-reviewer.md` (headings), `.claude/skills/slide-excellence/SKILL.md` (first 60 lines), `.claude/skills/compile-latex/SKILL.md`, `.claude/rules/content-invariants.md`, `.claude/rules/no-pause-beamer.md`, `.claude/rules/tikz-measurement.md` (head), `scripts/quality_score.py` (overfull section), `scripts/slide-qa.py` (docstring).

**Borrow:**
- Separate review passes. `slide-excellence` dispatches single-lens agents in parallel: visual (`slide-auditor`), pedagogy, and proofreading, plus TikZ only when the deck contains `\begin{tikzpicture}`, which is checked by grep before dispatch. Each pass is read-only and reports per slide with severity and a fix. The output contract requires a findings JSON array with exact quotes, verified by the reducer.
- Spacing before font size, in priority order: (1) reduce vertical spacing, (2) consolidate lists, (3) move display equations inline, (4) shrink the image (100% to 80% or 70%), (5) font reduction as the last resort, never below 0.85em; for Beamer, never `\tiny`.
- `credible-claims` reporting-language rule: when evidence is incomplete, the options are repair, **narrower language**, more review, an exploratory or descriptive label, or declining to report. **Never upgrade language beyond the evidence**: associational is not causal, pointwise is not uniform, illustrated is not validated, imposed is not derived. Keep reproducibility, implementation, statistical performance, measurement and identification separate. This maps directly onto causal-inference slides: a slide may narrow a paper's claim but never strengthen it.
- Pedagogy patterns: motivation before formalism, <= 4-5 new symbols per slide, a worked example within 2 slides, a two-slide strategy for dense theorems (statement with `\underbrace` on slide one, term-by-term unpacking on slide two), standout slides at pivots, Socratic questions, and semantic colour.
- TikZ six-pass measurement protocol (`tikz-measurement.md`, itself adapted from Scott Cunningham's MixtapeTools "with attribution"), starting with Pass 0 cross-slide consistency: the same diagram keeps the same colours and layout across slides.

**Do NOT borrow:** the Quarto/RevealJS parity machinery, R conventions, hooks, and the issue ledger. `quality_score.py`'s overfull heuristic only flags source lines over 120 chars inside a frame; it is weak, so prefer log parsing. `slide-qa.py` is Playwright on HTML only, so it does not apply to PDFs.

## 5. takashiishida/paper2slides (MIT)

Files read: `LICENSE`, `core.py` (compile, ADDITIONAL.tex, sanitize, generate_slides), `beamer2pdf.py`, `paper2slides.py` (cmd_generate/compile and argparse), `prompts/config.yaml` in full.

**Pipeline:**
- Stage 1 generates (paper TeX plus an allowed figure-path list).
- Stage 2 refines with an "update" prompt.
- Stage 3 (only with `--use_linter`) runs `chktex -o linter.log slides.tex` with **default chktex warnings, no filtering**, and sends the full log to a "revise" prompt.
- Compile runs `pdflatex -interaction=nonstopmode` twice. **A non-zero exit still counts as success if a PDF exists.**
- No render step and no human-review step.

**Lint checks present:** only chktex defaults, plus two deterministic pre-compile fixes:
- `sanitize_frametitles()` escapes unescaped `&` in `\begin{frame}[..]{title}` and `\frametitle<..>[..]{..}`, using `(?<!\\)&`.
- `extract_definitions_and_usepackage_lines()` copies the paper's `\def`, `\DeclareMathOperator` and `\DeclarePairedDelimiter` lines plus its `\usepackage` lines into `ADDITIONAL.tex`, commenting out packages that conflict with Beamer (amsthm, color, hyperref, xcolor, ragged2e, times, graphicx, enumitem).

**Overfull-box detection: none.** It never reads the `.log`.

**Borrow:**
- The idea of harvesting the paper's macros into a side file (`paper-macros.tex`) so its notation compiles unchanged. Very useful for math and statistics papers.
- An allowed-figure whitelist from `find_image_files`, to stop invented file names.
- The `&` and `%` escaping pre-pass.
- An optional chktex pass, but filtered (e.g. `chktex -q -n1 -n8 -n36 ...`) and treated as advisory.
- `max_items: 4` per itemize as a tighter optional cap.
- The rule to replace vague claims ("significant improvement") with the actual number and benchmark.

**Do NOT borrow:**
- pdflatex, and the "PDF exists means success" fallback.
- Deleting citations.
- "No title or text on figure frames" (it clashes with Moloch frame titles and our takeaway lines).
- The fixed Berlin/dolphin preamble.
- The "do not use `-`" quirk.

## 6. Templates

### jolars/moloch (CC-BY-SA-4.0, v2.3.0, 2026-10-15)
Files read: `LICENSE` (head), `README.md` License section, `src/beamerthememoloch.ins`, the headers of `src/*.dtx`, `RequirePackage` grep, `src/beamerfontthememoloch.dtx`, `docs/getting-started.md` (grep).

- Source is shipped as `.dtx` only. The `.sty` files are generated with `tex beamerthememoloch.ins` (docstrip) or `l3build install`. Generated files: `beamerthememoloch.sty`, `beamerinnerthememoloch.sty`, `beamerouterthememoloch.sty`, `beamerfontthememoloch.sty`, `beamercolorthememoloch.sty`, `beamercolorthememoloch-tomorrow.sty`, `beamercolorthememoloch-highcontrast.sty`. `moloch-talk.sty` is only for the experimental `ltx-talk` class; skip it.
- Dependencies: `keyval`, `pgfopts`, `calc`, `etoolbox`, `tikz`/`pgf`. All are standard in TeX Live.
- **Preferred route:** do not vendor. Moloch is on CTAN and TeX Live (`tlmgr install moloch`). The skill should check `kpsewhich beamerthememoloch.sty` and, if it is missing, tell the user to install it rather than doing so silently.
- CJK/ctex: the font theme sets only size and series, loads no fonts and does not touch fontspec, so `ctex` fonts apply cleanly under XeLaTeX. The title-format options `smallcaps`, `allsmallcaps` and `allcaps` exist; avoid them for Chinese titles because CJK fonts have no small caps and `allcaps` does nothing for CJK. The docs have no CJK notes. **Not compile-tested here** (no TeX on SG).
- Share-alike reasoning:
  - BY-SA 4.0 ShareAlike attaches only to *Adapted Material* (modified Moloch).
  - Shipping **unmodified** Moloch files beside our content is aggregation. Our repo stays CC-BY-NC-SA, but those files remain CC-BY-SA and must keep their headers plus a licence link.
  - **Modified** Moloch files would have to be BY-SA 4.0 or a CC-listed BY-SA-compatible licence. CC-BY-NC-SA is *not* compatible, so our NC terms can never be applied to Moloch-derived code.
  - Our own wrapper (`\usetheme{moloch}` followed by `\setbeamercolor` overrides in a separate file that contains no Moloch code) is not an adaptation and can stay NC-SA.
  - Decks users build are unaffected (the README says so explicitly).
  - If we vendor anyway: use `vendor/moloch/` with the unmodified generated `.sty` files, the CC-BY-SA LICENSE and a NOTICE (Vogelgesang 2015 + Larsson 2024/2025, source URL, version), and add an explicit carve-out in our top-level LICENSE/README.

### pm25/SimplePlus-BeamerTheme (Unlicense)
Files read: `LICENSE`, `README.md`, `beamerthemeSimplePlus.sty`, `beamercolorthemeSimplePlus.sty`, `sample.tex` (head).
- Files to vendor: `beamerthemeSimplePlus.sty`, `beamercolorthemeSimplePlus.sty`, `beamerfontthemeSimplePlus.sty`, `beamerinnerthemeSimplePlus.sty`. Also on CTAN as `beamertheme-simpleplus`.
- Dependencies: Beamer only (built-in `structure` colour theme). `sample.tex` uses `xcolor=dvipsnames`, `hyperref`, `graphicx` and `booktabs`, but the theme itself does not require them.
- No obligations. Keep the author header as a courtesy.
- CJK: no font settings, so it is ctex-neutral. Colours in use: DarkBlue structure, block colours MediumBlue/Green/Red on Muted backgrounds. Not compile-tested.

### yxnchen/sysu-beamer-template (CC0 claimed; conflicting)
Files read: `LICENSE` (head), `README.md`, `sysu.sty` (header, theme lines, image lines), `main.tex` (preamble).
- License conflict: the repo-level LICENSE is CC0, but `sysu.sty` itself says LPPL and/or GPL (modified from `andelf/ruc-beamer-template`'s ruc.sty, whose upstream licence I did not verify). The bundled `sysu_logo.png`, `sysu_title.png` and `sysu_background.png` are Sun Yat-sen University marks, which a CC0 dedication by a third party cannot clear.
- **Recommendation:** do not vendor. If a SYSU look is wanted, write our own theme file using only non-copyrightable facts (`sysugreen` RGB 0,88,38; `sysugreendark` 5,71,25; outer theme `split`, colour themes `whale`/`orchid`, inner theme `rounded`) and let the user supply the logos locally.
- Dependencies and CJK pitfalls:
  - `main.tex` uses `\documentclass[AutoFakeBold,AutoFakeSlant]{beamer}` with `ctex` + `fontspec`, plus the obsolete `xltxtra` and `xunicode`.
  - It hard-codes Windows fonts (SimSun/SimHei/FangSong, Times New Roman, Arial), which are missing on macOS; use ctex `fontset=mac`/`fandol` instead.
  - It loads `lmodern`, `utopia` and `babel[british]`. It is XeLaTeX only: `latexmk -xelatex` or xelatex twice.

---

## Overfull/underfull detection found across the repos

- None of the five repos parses the box **magnitude** or maps warnings to frames:
  - beamer-skill and pedrohcgs: only `grep -c "Overfull \\\\hbox" FILE.log`, plus counts of `Undefined control sequence`, `Citation.*undefined` and `multiply defined`. beamer-skill states an "> 10pt" threshold but never implements it.
  - pedrohcgs `quality_score.py`: flags source lines over 120 chars inside a frame (a heuristic, not log-based).
  - paper2slides: nothing.
  - Arxiv2beamer and paper-to-latex-ppt: visual only.
- Gap to fill ourselves (proposal, not borrowed). Run with `max_print_line=10000` (and optionally `-file-line-error`) so log lines are not wrapped, then match:
  `^(Overfull|Underfull) \\([hv])box \((?:(\d+(?:\.\d+)?)pt too (?:wide|high)|badness (\d+))\) (?:in paragraph at lines (\d+)--(\d+)|in alignment at lines (\d+)--(\d+)|detected at line (\d+)|has occurred while \\output is active)`
  - Map each warning to a page by tracking `[N` page-shipout markers in the log.
  - Severity: hbox > 10pt critical, 1-10pt warn, < 1pt ignore. Underfull is informational unless badness is 10000.
- Known blind spots, which make a visual pass mandatory:
  - Beamer suppresses warnings inside blocks.
  - A frame that overflows vertically is usually clipped silently.
  - A `\toprule` that merges into the title bar produces no warning.

## Page-render visual check approaches found

- beamer-skill: PyMuPDF at 200 dpi to JPG per slide, 8-point checklist, numeric scoring with 3 rounds at most; fallback is reading the PDF directly.
- paper-to-latex-ppt: PyMuPDF at 220 dpi to PNG plus `inspection.json` (text_chars < 10 means a likely blank page; resolution check), then a mandatory manual read, 3-5 rounds.
- Arxiv2beamer (idea only): batches of fewer than 4 pages, original figure opened before the rendered page, one immutable PDF snapshot per audit round, parallel subagents per batch.
- pedrohcgs: only for HTML (Playwright measuring pixels past each edge). For Beamer it is a source-reading audit.
- Suggested for group-beamer:
  - `pdftoppm -r 150 -png deck.pdf page` (poppler, when installed), else PyMuPDF.
  - Use Arxiv2beamer-style batches of 3 with original-figure comparison.
  - Rerun the check on the new PDF snapshot after every fix.

# Part B: statistics and causal talk writing, humanizer

Date checked: 2026-10-17. All fetched content was treated as data. Our repo
is CC BY-NC-SA 4.0 (`/Users/wriseai/Projects/supervisor-skills-plus/LICENSE`);
any MIT text we adapt needs its notice kept and a row in `THIRD_PARTY.md`.
Rule for all-rights-reserved sources below: borrow ideas and field names,
paraphrase, cite; do not copy wording.

Local copies: `scratchpad/refs/pdf/ramdas.pdf`, `refs/rg2026/`,
`refs/humanizer/`, `refs/ding/src/` (arXiv TeX).

---

## 1. Ramdas, "Checklist for effectively presenting work in Stat-ML"

- URL: https://www.stat.cmu.edu/~aramdas/checklists/aadi-talk-checklist.pdf
  (1 page, Aaditya Ramdas, CMU; personal advice for his students).
- License: none stated. Treat as all rights reserved. Paraphrase + cite only.
- Items (paraphrased):
  1. Watch Jean-Luc Doumont on scientific communication.
  2. Purpose: depth set by length and audience; short talk = motivation,
     intuition, key ideas; long talk may go technical but zoom out at the end.
  3. Psychology: anticipate what the audience wants, what confuses them.
  4. Prefers Keynote over Beamer, because typing-first tools lead to
     text/formula-packed slides.
  5. Too much information: assume most of the audience will not read the
     paper; give why / why sensible / how to interpret; use simple
     sufficient conditions, not general-but-complex assumptions; not the
     most general theorem unless succinct.
  6. One idea per slide; the idea is the title (top) or takeaway (bottom);
     fewer slides than minutes; number/title slides for Q&A reference;
     titles are full phrases or sentences.
  7. Animations (appear/disappear) to control what is read; in Beamer use
     `\pause`, never show a daunting page at once.
  8. Day-of: setup 15+ min early, backup copy, clicker/charger/water.
  9. Request a microphone.
  10. Questions: encourage; defer philosophical ones to the end; paraphrase
      the question back.
  11. Humor in moderation. 12. Vary tone and pace; work on pronunciation.
  13. Eye contact; do not read slides; know your slides.
  14. Be straightforward: no overconfidence or bragging, no self-flagellation;
      honest pros and cons.
- Borrow: items 2, 5, 6, 7, 14 as lint rules for the deck (sentence titles,
  one idea/slide, slides <= minutes, slide numbers on, simplified
  assumptions on main slides with general version in backup, `\pause` /
  overlays on dense formulas/figures). Items 10, 13 as a short "delivery"
  note in the speaker-notes or rehearsal section.
- Do not borrow: the anti-Beamer advice (our skill is Beamer by design; turn
  it into the warning "Beamer makes text-packing easy: enforce the density
  lint"); day-of logistics (8, 9, 11, 12) beyond a one-line pointer; no
  quoting of the PDF.

## 2. Method Atlas, "Reading papers" guide (one-page summary)

- URL: https://methodatlas.vercel.app/guides/reading-papers
- Author: Saerom (Ronnie) Lee (Wharton). Footer: "(c) 2026 Method Atlas. All
  rights reserved." No license, no repo link on the page.
- Fields confirmed, in order (page calls it a "one-page summary", step 6):
  Question / Estimand (ATE, ATT, LATE, ...) / Identification (method + source
  of variation) / Key assumption (stated precisely) / Main result (headline
  coefficient, CI, n) / Robustness (which checks, which passed) / Biggest
  threat / External validity (who it applies to and who not).
- Its 6-step reading procedure: is the question causal -> map
  identification + assumptions + testability (DAG) -> evaluate evidence
  (data, balance/pre-trends, main result, robustness, multiple testing) ->
  external validity -> read tables like a reviewer (column changes, SEs,
  effect sizes, n shifts) -> write the summary.
- Borrow: the 8 field names as the paper-talk "paper card" slide (field
  names are not protectable; our wording for each). Add "table-reading"
  checks as presenter prep items.
- Do not borrow: page prose or layout; do not call it a Method Atlas
  template in the skill text beyond a citation. Add what it lacks: a
  "presenter's interpretation" flag on Estimand (see 3) and a "what would
  change my mind" line.

## 3. Estimand -> identification -> estimation roadmap

- Primary (verified via Europe PMC + PMC): Petersen ML, van der Laan MJ.
  Causal models and learning from data: integrating causal modeling and
  statistical estimation. *Epidemiology* 2014;25(3):418-426.
  doi:10.1097/EDE.0000000000000078. PMID 24713881, PMCID PMC4077670 (author
  manuscript; (c) Lippincott Williams & Wilkins; cite, do not copy).
- Roadmap steps (paraphrased):
  1. Specify knowledge of the system as a causal model (and where it runs out).
  2. Specify the observed data and their link to the causal model.
  3. Specify the target causal quantity (counterfactual contrast under
     hypothetical interventions).
  4. Assess identifiability (can the target be written as a functional of
     the observed-data distribution; under which assumptions).
  5. Commit to a statistical model and estimand (separate knowledge-based
     from convenience-based assumptions).
  6. Estimate, with uncertainty.
  7. Interpret: statistical reading always available; causal reading only
     under the stated assumptions.
- Key point confirmed in the paper: the gap between statistical estimand
  and causal target is itself a causal quantity, untouched by the choice of
  estimator; it can only be assessed with sensitivity analysis. (Statistical
  bias, by contrast, is reduced by better estimators.)
- Cornell: no public course page with an explicit roadmap found. Closest is
  Cornell INFO 6751 (Ian Lundberg, Fall 2022 roster:
  https://classes.cornell.edu/browse/roster/FA22/class/INFO/6751): define
  the causal question, defend assumptions, estimate the target; design the
  observational study to mimic a hypothetical experiment. Better citable
  companion (verified via Crossref): Lundberg I, Johnson R, Stewart BM.
  What Is Your Estimand? Defining the Target Quantity Connects Statistical
  Evidence to Theory. *Am Sociol Rev* 2021;86(3):532-565.
  doi:10.1177/00031224211004187 (theoretical estimand -> empirical estimand
  -> estimation strategy).
- Borrow (for the paper-talk mode, one slide each):
  - "Target" slide: causal estimand in potential-outcome notation
    (Ding defaults, section 6), with unit, population, intervention, time.
  - If the paper is vague: pick one reading, write it in potential outcomes,
    label it "presenter's interpretation", list the alternative readings in
    backup. Never silently upgrade the paper's claim.
  - "Identification" slide: assumptions -> statistical estimand (a formula
    in observed data). Mark each assumption knowledge-based vs convenience.
  - "Estimation" slide: estimator + uncertainty; distinct from identification.
  - "Gap" line: causal reading holds only under the listed assumptions; the
    size of the violation is addressed by the paper's sensitivity analysis
    (or "none reported" as a critique point). Do not imply a better
    estimator closes it.
- Do not borrow: the full TMLE/super-learner machinery or SCM-only notation
  (keep the roadmap framework-neutral; Ding notation by default).

## 4. rphilipzhang/Reading-Group-2026

- URL: https://github.com/rphilipzhang/Reading-Group-2026 (README + LICENSE
  only). License: MIT, (c) 2026 Philip R. Zhang. Verified in the clone.
- Structure: 10 weeks, 2 tracks (weeks 1-5 AI for Research; 6-10 Applied
  Empirics), two 1-hour talks per session.
- Applied Empirics talk template (the part we want):
  1. Method introduction ~15 min: identification strategy, key assumptions,
     intuition.
  2. Simulation exercise ~20 min: simulations showing why assumptions matter
     and which violations are more or less consequential.
  3. Paper replication ~25 min: speaker-chosen empirical paper; how the key
     assumptions apply or fail there; stepwise replication of main results
     (open data, else simulated data from the paper's setting).
  AI track template: technical background ~20 / implementation demo ~15 /
  applications and reflections ~25.
  Logistics: slides, code and docs uploaded to the repo one day before.
  Applied topics: PS/matching/reweighting, 2x2 DID, staggered DID/TWFE, event
  study/SC/SDID, IV (+ shift-share, examiner), RDD, DML, ML x CI, partial
  identification and sensitivity.
- Borrow: an optional "replication segment" for paper-talk mode
  (assumption-violation simulation slide + replicated main table vs paper's
  table side by side, with a match/mismatch column); the
  intro/simulation/replication time split as a default for 60-min slots;
  "materials posted 24 h before" as a checklist item. MIT allows reuse with
  notice; we only reuse the structure, so a citation in THIRD_PARTY.md is
  enough.
- Do not borrow: schedule, Zoom/sign-up links, the AI track, the reference
  lists.

## 5. Hernán, "The C-Word" (AJPH 2018)

- Verified (Crossref + PMC): Hernán MA. The C-Word: Scientific Euphemisms Do
  Not Improve Causal Inference From Observational Data. *Am J Public Health*
  2018;108(5):616-619. doi:10.2105/AJPH.2018.304337. PMID 29565659, PMCID
  PMC5888052. (c) American Public Health Association 2018; no CC license
  shown. Cite, do not copy. Same issue has replies (Begg & March p.620,
  Chiolero p.622, Jones & Schooling p.624; the last argues for keeping
  associational wording in some settings).
- Guidance relevant to slides (paraphrased):
  - If the goal is causal, say so in the title, aims and methods; do not
    hide a causal aim behind "association"/"link".
  - Results report the estimate without causal interpretation; the
    discussion argues for and against the causal reading.
  - Define the question as the effect a (hypothetical) target trial would
    estimate, including intervention and timing.
  - Choose confounders by subject-matter knowledge; do not read confounder
    coefficients causally (Table 2 fallacy).
  - Residual confounding can never be ruled out; state it once, with the
    assumptions.
- Borrow: slide rule "Question slide says causal if the aim is causal";
  "Results slide = estimate + CI, no causal verb"; separate "Causal reading"
  slide listing the assumptions it needs (ties to section 3 gap line);
  critique-mode check "does the paper use association language for a causal
  aim, or causal language without the assumptions?"; flag causal reading of
  covariate coefficients.
- Do not borrow: the target-trial emulation framework as mandatory structure
  (offer it as optional for observational papers).

## 6. Ding, A First Course in Causal Inference

- Book: Ding P. *A First Course in Causal Inference*. Chapman & Hall/CRC
  Texts in Statistical Science. Boca Raton: CRC Press; 2024. ISBN
  978-1-032-75862-6 (publisher/retailer listings; July 2024).
- Open version: arXiv:2305.18793 (v2, 3 Oct 2023), license CC BY 4.0 per the
  arXiv abs page. Code/data: Harvard Dataverse doi:10.7910/DVN/ZX3VEV.
  CC BY permits adapting notation tables with attribution; the CRC print
  edition is copyrighted, so cite the arXiv version for anything adapted.
- Notation (from `frontmatter/notation.tex` and chapters in the TeX source):
  - Units i = 1..n; covariates X_i; binary treatment Z_i; observed outcome
    Y_i = Z_i Y_i(1) + (1 - Z_i) Y_i(0); potential outcomes Y_i(1), Y_i(0).
  - tau: average causal effect, finite-population n^{-1} sum {Y_i(1)-Y_i(0)}
    or super-population E{Y(1)-Y(0)} (say which).
  - tau_T = E{Y(1)-Y(0) | Z=1} (ATT), tau_C = E{Y(1)-Y(0) | Z=0} (ATC).
  - Outcome models mu_1(X) = E(Y | Z=1, X), mu_0(X) = E(Y | Z=0, X).
  - Propensity score e(X) = pr(Z=1 | X); overlap/positivity 0 < e(X) < 1.
  - Ignorability: Z \ind {Y(1), Y(0)} | X (Ding defines a custom \ind
    independence symbol; in Beamer use `\perp\!\!\!\perp`).
  - IV: Z = assigned/encouragement, D = treatment received with D(1), D(0);
    compliance type U = (D(1), D(0)); complier effect tau_c (CACE/LATE).
  - U also = unmeasured confounder (context-dependent; slides should not
    reuse U for both in one deck).
  - Mediation: nested Y(z, M_{z'}). Probability pr(.), expectation E(.),
    var, cov; I(.) indicator.
- Borrow: these as the default notation block for `group-beamer` (a
  `notation.tex` macro file + a "Notation" backup slide); rule "translate the
  paper's notation into the default on the notation slide, or keep the
  paper's notation and show the mapping once", never mix both.
- Do not borrow: Ding's `krantz.cls` layout or picture-based `\ind` macro;
  chapter text.

## 7. blader/humanizer and the deai-writing `slides` profile

- URL: https://github.com/blader/humanizer. License: MIT, (c) 2025 Siqi Chen
  (LICENSE file; SKILL.md frontmatter `license: MIT`, version 3.1.0). Its
  patterns derive from Wikipedia "Signs of AI writing" (Wikipedia text is
  CC BY-SA 4.0; humanizer paraphrases it). Reuse: paraphrase categories,
  keep MIT notice if any text is copied, add a THIRD_PARTY.md row.
- Pattern categories (26 patterns in 6 groups):
  A. Staging instead of stating: not-X-but-Y; one-line closers and dramatic
     fragments; deep-sounding sayings; staged run-up; arguing with no one.
  B. Rhythm by rule: forced triads; repeated openings; dashes everywhere;
     stacked qualifiers; hyphenated pairs; passive / missing subjects.
  C. Inflation and borrowed authority: AI words; inflated significance;
     vague connection; shallow -ing riders; sales language; borrowed
     authority; avoiding is/are/has.
  D. Formatting by rule: decorative bold; decorative headings; curly quotes.
  E. Chat/draft leftovers: chatbot residue; knowledge-limit disclaimers;
     heading repeated in first sentence; writing about the document.
  F. Wrong reader: re-explaining what the reader knows.
  Plus "When not to act" (quotes, titles, deliberate choices; several
  tells together, not one).
- What deai-writing already has (repo
  `skills/deai-writing/`): profiles `academic`, `academic-response`, `docs`,
  `technical-blog` in `references/patterns.md` section 8 (prose + tolerance
  matrix), selection rules in `references/editing-contract.md` section 5.
  Most humanizer patterns are already covered (negative parallelism,
  -ing tails, hedge stacking, aphorisms, staccato, bold/bullets). Humanizer
  adds little beyond: "heading repeated in the first sentence" (maps to
  slide title restated in first bullet) and "arguing with no one" (already
  S3). No need to import humanizer text.
- Where `slides` fits:
  1. `references/patterns.md` section 8: add a `slides` bullet to the
     profile list and a `slides` column to the tolerance matrix.
  2. Same section, "Inference when no profile is named": add a rule before
     the `.tex -> academic` rule: a `.tex` file with `\documentclass{beamer}`
     (or `frame` environments) uses `slides`. Without this, Beamer files
     are mis-profiled as `academic`.
  3. `SKILL.md` "Pattern catalog and the academic profile": one sentence
     naming `slides` and that `group-beamer` calls `audit` with it.
  4. `references/editing-contract.md` section 4 protected content: frame
     titles are editable only for claim-level downgrades; overlays
     (`\pause`, `\only`, `<2->`), `\label`, notes (`\note{}`) protected.
- `slides` profile content (proposal):
  - Register: terse bullets and fragments pass (bullet rule = skip;
    "fragment" rules relaxed in bullets, strict in titles' claims).
  - Hedging: one hedge per claim, on the interpretation; measurements
    unhedged (same as academic, stricter on stacks: P1 -> P0 on titles).
  - Restatement (S2) extra strict at deck scope: a selling point appears in
    one place only, not title + bullet + summary slide; the summary slide
    may list results but not re-sell them.
  - Negative parallelism ("not X but Y", "not only... but"): strict, also in
    titles. One real correction of a common misreading passes.
  - One-line closers / punchy takeaways ("That's the key.", "Simple.",
    "Game-changer"): strict; a takeaway box must state a checkable claim.
  - Marketing adjectives (novel, powerful, elegant, remarkable, seamless,
    state-of-the-art) and significance inflation: extra strict; rationed
    caps apply per deck, lower than per paper (e.g., "novel" at most once).
  - Title verb strength <= claim level. Each frame title carries a claim
    level, checked against the slide's evidence:
      proved (theorem/proof shown or cited) -> "X implies Y", "is";
      numerical evidence (simulation/empirical) -> "In simulation, ...",
        "reduces ... by ... (n=...)";
      causal under stated assumptions -> "Under A1-A3, Z increases Y";
      exploratory/presenter's interpretation -> "suggests", "is consistent
        with", "Presenter's reading:".
    Causal verbs (causes, increases, leads to, effect of) on a result slide
    without listed assumptions = P0 (ties to Hernán, section 5).
  - Sentence titles allowed and encouraged (Ramdas); decorative/generic
    titles ("Results", "Overview") are P2 unless a section divider.
  - Heading repeated in first bullet: strict (humanizer E3).
  - Bold/colour emphasis: one emphasis per slide max.
  - Dashes, semicolons, colons: relaxed (bullets use colons legitimately).
  - Rhetorical questions: relaxed for an open-question or "discussion"
    slide; strict elsewhere.
  - Uniform paragraph length, transition chains, copula avoidance: skip /
    relaxed (not prose).
  - Revision narration: strict in the deck; allowed in weekly-report
    "since last week" slides (version-scoped, like `academic-response`).
  - Chatbot artifacts, placeholders, "In this talk we will explore": extra
    strict.
  - Speaker notes (`\note{}`) are prose: audit them with `academic`.
  - Never-inject list unchanged; output not longer than input (counted per
    frame).
- Do not borrow from humanizer: its voice-restoration goal (adding
  "personality"), curly-quote rule (LaTeX handles quotes), and its tone
  examples; deai-writing's contract already supersedes it.

---

## Cross-cutting decisions suggested for group-beamer

- Paper-talk spine: card (Method Atlas fields) -> target estimand
  (Petersen step 3, Ding notation) -> identification + assumptions (step 4-5)
  -> estimation (6) -> results without causal verbs (Hernán) -> causal
  reading + sensitivity / biggest threat (7) -> optional replication
  segment (Zhang) -> external validity -> questions for the group.
- Weekly-report mode: Ramdas density rules + claim-level titles + "since
  last week" slide; no paper card.
- Licensing: only Ding (CC BY 4.0, arXiv), humanizer (MIT), Reading-Group
  (MIT) permit adaptation; Ramdas, Method Atlas, Petersen, Hernán: cite and
  paraphrase only.
