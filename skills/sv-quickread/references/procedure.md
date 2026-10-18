<!-- Moved from skills/paper-quickread/SKILL.md by ADR 0021 (2026-10-18); licence CC-BY-NC-SA-4.0. Section text unchanged; pointers updated. -->

# Paper Quickread

## Contents

- Overview
- When to use this skill
- When NOT to use this skill
- Step 0: Load context
- Workflow
- Checklist
- Outputs
- Hand-offs

## Overview

One paper in, one page out, readable in five minutes. The page is a fixed
nine-section card (`template-9.md`) so that cards from many
papers line up for comparison and for the literature map of
`sv-litreview`. It is not a substitute for understanding the paper: when
the reader wants that, `sv-study` takes the same folder and goes deeper.

Three things make this card different from a generic summary:

1. **Assess before writing.** Paper type and field decide what the method
   block must say (identifying assumptions for causal inference, theorem
   chain for mathematics, RQs and validity threats for SE) and which
   sections may honestly say "not applicable".
2. **Nothing invented.** Every number, formula and quoted claim is copied
   from the paper with its location (section, table, figure, theorem,
   equation, page). If the paper does not give it, the card says so
   ("not stated in the paper"; Chinese label in the template). Values are never read off plots.
3. **Claims are graded.** Contributions are tagged proved / empirical /
   conjectured, and a claim-evidence table shows which claim rests on which
   evidence and which claim lacks it.

The default output language is Chinese with technical terms in English; it
follows the user's language when the user writes in another.

## When to use this skill

- The user gives one paper (PDF, arXiv link, DOI, Markdown) and wants to
  know what it says, quickly.
- Triage: decide whether a paper is worth a deep read.
- Building cards for a later literature map (`sv-litreview-map`
  mode reads them).
- `--style`: the user also wants this paper's writing dissected (structure,
  rhetorical moves, sentence templates) for a target venue.

## When NOT to use this skill

- The user wants to understand a concept, method or proof in the paper:
  `sv-study-paper`. It reuses this card if one exists.
- Several papers, a survey or a related-work section: `sv-litreview`.
- Reviewing the user's own manuscript: `sv-review-once`.
- Building a venue's style profile from many exemplars: `sv-write-style-mine`.

## Step 0: Load context

1. Load `research-core`: `references/core/inputs-mineru.md`,
   `references/core/claims-evidence.md`, and the field profile for the
   paper's field (assessed in Step 2; if the project has a `research.yaml`,
   its `field` is the default). Read the profile's "Method block for quick
   reads" subsection when it has one.
2. No `research.yaml` is needed. If one exists, read `field`, `project`,
   `stage` and the RQs or summary in `docs/STATUS.md` for section 9.
3. Resolve the reading root (where outputs go):
   `research.yaml` `reading.dir` if set; else `<project>/reading/` when the
   working directory is a research project; else the study vault found by
   `skills/sv-study/scripts/vault.py where` (`$STUDY_VAULT`, then
   `~/.config/study/vault`, then `~/study-vault`); else `./reading/`. Say
   which one was used.

## Workflow

### Step 1: Get the text (MinerU only)

Convert the PDF with MinerU following `inputs-mineru.md` (MCP
`mineru_parse_documents_smart`, then the official MinerU CLI, then a local
MinerU). If every route fails, stop and report the routes and errors; do not
switch to another extractor and do not summarize from the abstract page.
Run the readability gate. Keep `paper.md` and the figure files in the paper
folder (`<reading-root>/papers/<YYYY-MM-DD>_<firstauthor>_<short-title>/source/`),
and record the route and page range. arXiv TeX source is corroboration
only, with the user's consent.

### Step 2: Assess before writing

Decide and write down, in one line each:

- **Paper type**: theory, method, empirical, system, benchmark, survey,
  position.
- **Field**: causal, stats, math, SE, AI/ML, other (pick the field profile).
- **Method block content** for that type and field
  (`field-method-blocks.md`).
- **Sections that are honestly not applicable**, for example no results
  table in a pure theory paper (section 5 then lists the main theorems with
  their numbers instead).
- **Two tags**: exactly one problem-domain tag and one method tag, specific
  ("synthetic-control", not "statistics").

### Step 3: Write the nine sections

Follow `template-9.md`: section order, length budget per
section, and what each must contain. Hard rules while writing:

- Copy numbers, formulas and claims; give the location for each.
- Results table: only numbers printed in the paper's text or tables, each
  cell with its source; never estimate from a figure.
- Contributions: 3 to 5, each tagged proved, empirical, conjectured
  (stated without proof or evidence) or cited (template labels). A theorem cited
  from other work is "cited", not "proved here".
- Claim-evidence table: the research-core claim-ledger columns trimmed to
  claim / evidence and location / strength / doubt.
- Limitations: two columns, stated by the authors (with location) and our
  judgement (labelled as such).
- Section 9 links to the reader's work only through what the reader has
  told you or `docs/STATUS.md`; otherwise one line asking what the current
  project is.
- Body text (outside tables) within the budget: target 700 Chinese
  characters or 450 English words; tables do not count.

See also `template-9.md`
See also `field-method-blocks.md`

### Step 4: Self-check

Run `scripts/check_quickread.py <quickread.md>`: nine headings in order,
exactly two tags, body length, every results row has a source, every
contribution has a tag, no empty section. Then reread the card against the
source for three things the script cannot see: a number not in the paper,
a claim stronger than the paper's own wording, a figure value read off a
plot. Fix and rerun until clean.

### Step 5: Save and index

Write `quickread.md` in the paper folder. Append one entry to
`<reading-root>/index.json` with `scripts/index_append.py` (append only;
an existing entry for the same paper is never overwritten, a new date is
added to its history instead).

### Optional: `--style`

After the card, dissect the paper's writing into one Paper Style Card in
`sv-write-style-mine`'s format (fields A to L; CARS move tags; three to five
abstracted sentence templates; no copied sentences) and save it as
`style-card.md` in the paper folder. It is a candidate for `sv-write-style-mine`'s
accumulate loop, never a rule by itself.

See also `style-mode.md`

### Visuals (optional)

A paper-structure figure (question to assumptions to method to theorems or
experiments to conclusions) or a before/after comparison with prior work
helps when the user asks for it; use the `sv-study` kit
(`skills/sv-figure-explain/kit/`, rules in `skills/sv-figure-explain/references/visuals.md`,
scenario list in `skills/sv-figure-explain/references/visual-scenarios.md`) and embed
the PNG. Not part of the default one page.

## Checklist

Report pass, fail or n/a with evidence:

- MinerU route recorded; readability gate passed.
- `check_quickread.py` exit 0.
- Every number and formula has a location; no plot-read values.
- Contributions tagged; claim-evidence table flags at least the weakest
  claim, or says none found and why.
- Limitations separate the authors' admissions from our judgement.
- Index entry appended, not rewritten.
- With `--style`: card uses fields A to L, contains no copied sentence.
- research-core checklist items owned by this skill (field profiles'
  CI, ST and SE items with Owner `sv-quickread`).

## Outputs

```
<reading-root>/
  index.json                                   append-only
  papers/<YYYY-MM-DD>_<firstauthor>_<short-title>/
    source/paper.md, source/images/             MinerU output, route and pages recorded
    quickread.md                                the nine sections
    style-card.md                               only with --style
```

## Hand-offs

- Understand a concept, method or proof from this paper: `sv-study` (paper
  mode, same folder).
- The paper suggests something for the current project: `sv-study-bridge`.
- Style card into a venue profile: `sv-write-style-mine` (accumulate).
- Several cards into an evolution map and gap list: `sv-litreview`
  (literature-map mode).
- Verifying a citation the card relies on: `sv-litreview`'s citation
  protocol.
