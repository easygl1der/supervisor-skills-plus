# Field profile: Mathematics

Code: MT
Status: partial
Version: 0.1 (2026-10-13)
Scope: papers whose main contribution is a theorem and its proof, and the
mathematical parts (definitions, statements, proofs, notation) of papers in
other fields. Expository and survey papers are not covered yet.

## Contents
Sources; Paper types; Typical structure; What reviewers and advisors care
about; Tone and phrasing; Citation norms; Figures and tables; Rigor and
threats (with LaTeX and notation conventions); Checklist additions; Known
disagreements; Unknown; Changelog.

Rules follow `references/core/precedence.md`. No exemplar mathematics
papers have been supplied; every rule comes from the owner's skills and
upstream notation rules. Core rules are not repeated here.

## Sources
1. Owner skill `paper`: manuscript workflow, writing standards, LaTeX
   conventions and the `scaffold_paper.py` skeleton.
2. Owner skill `academic-author-team`, `references/style-profile.md`: the
   owner's mathematical prose style, which `paper` loads before drafting.
3. Owner skills `proof-review-math`, `theorem-search-math` and
   `formalize-lean4`: proof review, theorem retrieval and Lean checking.
4. Owner skill `style-mine`, base rules `general_academic.md`.
5. Upstream notation and equation rules:
   `handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md`,
   `skills/pre-submission-reviewer/references/latex-rules.md`,
   `skills/paper-writer/references/verification-checklist.md`.
6. Gap analysis of upstream for mathematics: `notes/01-upstream-map.md` §5.2.

## Paper types
- Theorem paper: the contribution is a result together with its proof
  technique. Upstream has no scaffold for this type.
  [src: note:n01§5.2] (candidate)
- For theory papers, the proofs play the role that experiments play
  elsewhere: review the proofs, and never call the evidence thin because
  there is no results table.
  [src: up:skills/pre-submission-reviewer/SKILL.md] (confirmed)
Other types (expository, survey, problem papers, computational
mathematics) are Unknown.

## Typical structure
- Default skeleton: abstract; Introduction (problem, context, main
  contributions); Main Results with the main theorem stated; Proofs with
  supporting lemmas; bibliography; appendix.
  [src: skill:paper] (confirmed)
- Within a section, follow the rhythm: problem or motivation, intuition,
  formal definition, core statement, proof idea in the main text, example or
  remark, pointer to the appendix for heavy derivation.
  [src: skill:academic-author-team] (confirmed)
- The main body holds motivation, conceptual explanation, theorem
  statements, proof strategy, examples and remarks. Long computations, proof
  expansions and technical verification go to the appendix, and the body
  points to them with `\cref` or a footnote.
  [src: skill:academic-author-team] (confirmed)
- Put major sections in `sections/*.tex` once the paper is longer than a
  few pages; figures in `figures/`; build output out of version control.
  [src: skill:paper] (confirmed)
- When a paper depends on many earlier results, a dependency graph of
  sections or lemmas can replace a long prose list; nodes are real results
  and arrows real dependencies. [src: skill:academic-author-team] (confirmed)

## What reviewers and advisors care about
No referee reports or advisor comments for mathematics papers are on
record. The concerns below come from the owner's proof-review workflow.

- Logical gaps and critical errors in proofs come first, then citation and
  source problems, then symbol and notation consistency.
  [src: skill:proof-review-math] (confirmed)
- When answering a critique, separate three questions: is the critique
  correct, is there a serious gap, and how is it repaired.
  [src: skill:paper] (confirmed)
- Assumptions of each theorem are stated explicitly; say what fails when
  an assumption is dropped where that is known.
  [src: skill:paper; skill:style-mine] (confirmed)

## Tone and phrasing
- Dense, rigorous working-note voice: enough motivation to orient the
  reader, then precise notation, assumptions and definitions. Do not
  over-explain standard background to an advanced reader.
  [src: skill:academic-author-team] (confirmed)
- Do not hide proof obligations behind "clearly", "standard" or "it
  follows" when the step is structurally important.
  [src: skill:paper] (confirmed)
- Introduce an equation in words before displaying it.
  [src: skill:style-mine; skill:academic-author-team] (confirmed)
- Each symbol has one meaning; introduce it near its first use; keep
  notation consistent across sections. Use as few symbols as possible and
  add a notation table when more than six are in common use.
  [src: skill:paper; up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md] (confirmed)
- Symbol explanations after an equation use exactly the symbols the
  equation uses. [src: up:skills/paper-writer/references/verification-checklist.md] (confirmed)
- Final exposition is narrative prose linking definitions, statements,
  proofs and examples, not an outline-like list.
  [src: skill:academic-author-team] (confirmed)

## Citation norms
- Keep BibTeX in `references.bib`; never invent citation metadata.
  [src: skill:paper] (confirmed)
- A theorem-search hit is retrieval context, not a proved answer; cite the
  direct source link or the original publication, not a vague theorem
  name. [src: skill:theorem-search-math] (confirmed)
- Default bibliography style in the scaffold is `alpha`; follow the
  journal's style when it differs. [src: skill:paper] (confirmed)

## Figures and tables
- Diagrams that illustrate formulas or theorems are drawn in TikZ so they
  match the LaTeX document. [src: up:handbook-en/04_Scientific_Plotting/4.4_plotting-checklist-and-tools.md] (confirmed)
- Formula statements stay as formulas, never as images; plots and diagrams
  that carry information stay as figures.
  [src: skill:academic-author-team] (confirmed)
Other figure conventions for mathematics papers are Unknown.

## Rigor and threats
- State theorem assumptions explicitly in the statement, not only in the
  surrounding text. [src: skill:paper] (confirmed)
- Write "no obvious issues found" for an automated or human proof review,
  never "verified"; a review is not a machine-checked proof.
  [src: skill:proof-review-math] (confirmed)
- Claim formal verification only for Lean code that compiled in the Lean
  verifier; a generated candidate is not a verified proof.
  [src: skill:formalize-lean4] (confirmed)
- If parsing or OCR of a proof fails during review, report the blocker
  instead of reviewing the wrong text. [src: skill:proof-review-math] (confirmed)
- Compile the paper before reporting it done, or state why compilation
  could not run and give the exact command.
  [src: skill:paper] (confirmed)

### LaTeX and notation conventions
- Packages by default: `amsmath`, `amsthm`, `amssymb`, `mathtools`,
  `hyperref`, `cleveref`, `booktabs`. Theorem, lemma, proposition and
  corollary share one counter numbered within sections; definitions and
  examples use the definition style; remarks the remark style.
  [src: skill:paper] (confirmed)
- In `.tex`, inline math uses `\(...\)` and display math `\[...\]`.
  [src: skill:paper] (confirmed)
- Label sections, theorems, equations, figures and appendices; refer with
  `\label` and `\cref`; never use `\tag{}` for references.
  [src: skill:paper; skill:academic-author-team] (confirmed)
- Every numbered equation is referenced in the text; otherwise use an
  unnumbered environment. [src: up:skills/pre-submission-reviewer/references/latex-rules.md; skill:style-mine] (confirmed)
- Use `\mathbf` for vectors and `\boldsymbol` for matrices (not `\bm`),
  `\mathbb{I}` for the indicator, `\mathbb{P}` and `\mathbb{E}` for
  probability and expectation, `n_1` and never Unicode subscripts, and no
  Markdown in `.tex`. [src: skill:academic-author-team] (confirmed)

## Checklist additions

### MT-01 Assumptions in every statement
- [ ] Check: Each theorem, lemma and proposition lists its assumptions in
  the statement itself.
- Why: A statement with hidden assumptions cannot be checked or reused.
- Status: confirmed
- Scope: field:mt
- Owner: paper-writer, pre-submission-reviewer
- Src: skill:paper

### MT-02 No hidden proof obligations
- [ ] Check: Search for "clearly", "obviously", "standard", "it follows";
  each structurally important step behind them is proved or cited.
- Why: These phrases hide the gaps a referee will find.
- Status: confirmed
- Scope: field:mt
- Owner: paper-polish, check-loop, pre-submission-reviewer
- Src: skill:paper

### MT-03 Proof review done and reported honestly
- [ ] Check: Every main proof went through a review pass; findings are
  split into gaps, citation issues, notation issues and repairs; the outcome
  is reported as "no obvious issues found", not "verified".
- Why: A review is not a proof check by machine.
- Status: confirmed
- Scope: field:mt
- Owner: pre-submission-reviewer, check-loop
- Src: skill:proof-review-math

### MT-04 Notation consistent and introduced
- [ ] Check: Every symbol is defined before first use, keeps one meaning,
  and a notation table exists when more than six symbols are in common use.
- Why: Symbol drift makes proofs hard to check.
- Status: confirmed
- Scope: field:mt
- Owner: paper-writer, paper-polish, check-loop
- Src: skill:paper; up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md

### MT-05 Equations referenced and labelled
- [ ] Check: Every numbered equation is referenced in the text with
  `\cref`; no `\tag{}` references remain.
- Why: Unreferenced numbers clutter the page; tags break when sections move.
- Status: confirmed
- Scope: field:mt
- Owner: paper-polish, pre-submission-reviewer
- Src: up:skills/pre-submission-reviewer/references/latex-rules.md; skill:academic-author-team

### MT-06 Body and appendix split
- [ ] Check: Long computations and proof expansions sit in the appendix; the
  body keeps the statement, proof idea and a pointer.
- Why: The reader follows the argument without losing the thread.
- Status: confirmed
- Scope: field:mt
- Owner: paper-writer
- Src: skill:academic-author-team

### MT-07 Cited results traced to sources
- [ ] Check: Every cited theorem has a real BibTeX entry or a direct source
  link; no metadata is invented; search hits are confirmed in the source.
- Why: A wrong citation for a key lemma breaks the proof.
- Status: confirmed
- Scope: field:mt
- Owner: paper-writer, pre-submission-reviewer
- Src: skill:paper; skill:theorem-search-math

### MT-08 Formal verification claims checked
- [ ] Check: Any claim that a result is formalized points to Lean code that
  compiled in the verifier.
- Why: A generated Lean candidate proves nothing until it compiles.
- Status: confirmed
- Scope: field:mt
- Owner: check-loop, pre-submission-reviewer
- Src: skill:formalize-lean4

### MT-09 Paper compiles
- [ ] Check: The paper compiles from source, or the blocker and the exact
  next command are recorded.
- Why: Done means a PDF, not a plan.
- Status: confirmed
- Scope: field:mt
- Owner: check-loop
- Src: skill:paper

## Known disagreements
- Math delimiters: the owner's `paper` skill uses `\(...\)` and `\[...\]`
  in `.tex`, while upstream paper-writer prose delivery uses `$...$` and
  `$$...$$`. In `.tex` the owner's convention applies; in Markdown follow the
  active request. [src: skill:paper; skill:academic-author-team; up:skills/paper-writer/references/prose-delivery.md]
- Missing citation data: `paper` allows a clear placeholder while drafting;
  upstream paper-writer forbids placeholder tags. Placeholders may exist in
  drafts only and are cleared before submission.
  [src: skill:paper; up:skills/paper-writer/SKILL.md]

## Unknown
- Exemplar papers: none supplied. Five to ten papers from the target
  journals are needed before structure, length, tone or reviewer concerns
  can be measured.
- Paper types other than the theorem paper, and their structures.
- Journal-specific conventions (submission formats, MSC codes, abstract
  length, whether "we" is expected).
- Referee report norms and how mathematics referees weigh novelty against
  technique.
- Citation conventions beyond BibTeX hygiene (for example review database
  identifiers or arXiv versus journal versions).
- Figure and table conventions beyond TikZ for diagrams.

## Changelog
- 0.1 (2026-10-13): created from the owner's paper, style, proof-review,
  theorem-search and formalization skills, style-mine general rules and
  upstream notation rules.
