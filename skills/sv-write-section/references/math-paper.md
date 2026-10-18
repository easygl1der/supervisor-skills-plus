# Mathematics paper route

Route for papers whose main contribution is a theorem and its proof
(`research.yaml` `field: math` or `paper_type: theory`), and for the
mathematical parts (definitions, statements, proofs, notation) of papers in
other fields. The field profile `research-core` `fields/math.md` holds the
conventions with their sources; this file is the drafting procedure.

Origin: the owner's former `paper` skill (manuscript workflow, writing
standards, LaTeX conventions, scaffold), plus the style and proof-review
skills that `paper` loaded. Rules use the format `[src: ...] (status)`.

## Contents
1. Proof-obligation ledger (the math form of Phase 0)
2. Definition, lemma and theorem discipline
3. Proofs in the body and the appendix
4. Notation and LaTeX
5. Scaffold for a new paper
6. Before reporting done

## 1. Proof-obligation ledger (the math form of Phase 0)

For a theorem paper the claim ledger lists proof obligations instead of
measured numbers. One row per statement:

| Id | Statement (label) | Assumptions | Depends on | Status | Source |
|---|---|---|---|---|---|
| L1 | `lem:...` | ... | D1, D2 | proved here / cited / open | section, or bib key and theorem number |

- Every structurally important step is either proved in the paper or cited
  to an exact source (bib key and theorem number). A step that is neither is
  an open obligation and is reported to the author, never smoothed over in
  prose. [src: skill:paper] (confirmed)
- A theorem-search hit is retrieval context, not a proof; confirm the
  statement in the cited source before the row becomes "cited".
  [src: skill:theorem-search-math] (confirmed)
- A result counts as formally verified only when its Lean code compiled in
  the verifier. [src: skill:formalize-lean4] (confirmed)
- When the author answers a referee or co-author critique of a proof, record
  three things separately: is the critique correct, is there a serious gap,
  how is it repaired. [src: skill:paper] (confirmed)

## 2. Definition, lemma and theorem discipline

- Define every object before a statement uses it; a definition introduces
  one object and fixes its notation. [src: skill:paper; skill:writing-shape] (confirmed)
- Each theorem, lemma and proposition states its assumptions inside the
  statement, not only in the surrounding text. Say what fails when an
  assumption is dropped where that is known. [src: skill:paper] (confirmed)
- Use the environment that matches the role: theorem for main results,
  lemma for steps, proposition for results of independent interest,
  corollary for direct consequences, definition, example, remark.
  Theorem-like environments share one counter numbered within sections.
  [src: skill:paper] (confirmed)
- Within a section keep the rhythm: motivation, intuition, formal
  definition, statement, proof idea, example or remark, pointer to the
  appendix for heavy derivation. [src: skill:academic-author-team] (confirmed)
- Introduce an equation in words before displaying it.
  [src: skill:academic-author-team; skill:style-mine] (confirmed)

## 3. Proofs in the body and the appendix

- Do not hide proof obligations behind "clearly", "obviously", "standard"
  or "it follows" when the step carries weight. Search for these words
  before delivery; each hit is proved, cited, or rewritten.
  [src: skill:paper] (confirmed)
- The body keeps the statement, the proof strategy and short proofs. Long
  computations and technical verification go to the appendix, and the body
  points to them with `\cref`. [src: skill:academic-author-team] (confirmed)
- A dependency graph of lemmas can replace a long prose list when many
  results depend on each other; nodes are real results, arrows real
  dependencies. [src: skill:academic-author-team] (confirmed)
- Report a review of a proof as "no obvious issues found", never
  "verified". [src: skill:proof-review-math] (confirmed)

## 4. Notation and LaTeX

- Each symbol has one meaning, is introduced near its first use and stays
  consistent across sections; add a notation table when more than six
  symbols are in common use. [src: skill:paper; up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md] (confirmed)
- In `.tex`, inline math uses `\(...\)` and display math `\[...\]`; in
  Markdown follow the active request. [src: skill:paper] (confirmed)
- Label sections, theorems, equations, figures and appendices and refer with
  `\cref`; never use `\tag{}` for references; every numbered equation is
  referenced. [src: skill:paper; up:skills/pre-submission-reviewer/references/latex-rules.md] (confirmed)
- BibTeX lives in `references.bib`; citation metadata is never invented.
  While drafting, a missing entry may be a visible placeholder in the draft
  file only; it is cleared before Final mode, as sv-write-section's zero-tag rule
  requires for delivered prose. [src: skill:paper; up:skills/sv-write-section/references/workflow.md] (confirmed)

## 5. Scaffold for a new paper

For a fresh folder, `scripts/scaffold_paper.py <dir> --title "..."` creates
`main.tex` (article class, `amsmath`, `amsthm`, `amssymb`, `mathtools`,
`hyperref`, `cleveref`, `booktabs`, shared theorem counter), one file per
section under `sections/` input from `main.tex`, `references.bib`,
`figures/`, `build/` and a `.gitignore` for build output. It refuses to
overwrite existing files. Skeleton:

1. Abstract.
2. Introduction: problem, context, main contributions (the main theorem
   stated informally).
3. Main results: the main theorem stated formally with all assumptions.
4. Proofs: supporting lemmas, then the proof of the main theorem.
5. Bibliography (default style `alpha`; the journal's style wins).
6. Appendix: long computations.

[src: skill:paper] (confirmed). The former scaffold did not input the
section files from `main.tex`; the vendored script does.
[src: note:n02§7] (confirmed)

Use a venue template instead of the scaffold when the venue profile names
one.

## 6. Before reporting done

Do at least one, and say which:

- compile the paper and report the PDF path;
- run a build check and report the remaining errors;
- for prose-only edits, list the touched files and the review scope.

If compilation cannot run, say why and give the exact next command.
[src: skill:paper] (confirmed)
