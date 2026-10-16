# Book mode

## Contents
1. Files
2. One chapter
3. Concept map
4. Theorems and proofs
5. Examples and counterexamples
6. Exercises
7. progress.md

## 1. Files

```
<study-vault>/books/<book-slug>/
  progress.md                    whole book: where we are, open questions
  chNN-<slug>/
    notes.md                     concept map, theorems, examples, links across chapters
    exercises.md                 3 to 5 exercises with graded hints
    fig-*.html, fig-*.png
```

Book slug: author and short title, for example `murphy-pml1`. Chapter text
comes from MinerU (one chapter or a page range at a time); record the
pages converted.

## 2. One chapter

1. Read the chapter's section list; ask which sections matter for the
   learner's research (from step 0 of the protocol). Skip the rest
   explicitly in `progress.md`.
2. Build the concept map (section 3).
3. Run the protocol on the 2 to 4 concepts the map shows as central.
4. Theorems and proofs (section 4), examples (section 5), exercises
   (section 6).
5. Links forward and backward: which earlier chapter this needs, which later
   chapter uses it.
6. Update `progress.md` and save the session.

## 3. Concept map

Nodes: definitions (def-), theorems and lemmas (thm-, lem-), methods
(method-), examples (ex-). Edges: "uses", "special case of", "motivates",
labelled with a verb. Each node carries its section and equation number.
Draw with `textbook-dag.html` (up to six nodes), `auto-dag-elk.html`
(about 7 to 20), or Graphviz `dot` for a whole chapter or a map that is
still changing (`visuals.md`). Put the reading order of the map in one
sentence under it.

## 4. Theorems and proofs

For each central result: the statement copied with its number and page;
the hypotheses listed; the proof idea in two or three sentences (the step
that does the work); which hypothesis each step uses. Proofs the learner
wants to rebuild use the proof-reconstruction option (`options.md`).

### Errors in the source

Books have errata. When a statement, exercise answer or equation looks
wrong: check the converted text against the PDF page so a conversion error
is ruled out, write the derivation that disagrees, and record it under
"原文疑点（待核）" in `notes.md` and in the exercise. Never silently fix
the source; the learner checks the errata. The eval run found one in
Murphy PML1 Exercise 4.9 (`evals/study-vault/books/murphy-pml1/ch04-statistics/notes.md`).

## 5. Examples and counterexamples

One typical example per central concept (from the book, with its number),
and one counterexample that shows why a hypothesis is needed. A table with
columns concept, example, counterexample keeps them side by side. Prefer
counterexamples the book itself gives (often in a later section). If the book
gives none, construct one and mark it 补.

## 6. Exercises

3 to 5 per chapter, from the book (with numbers) or written for the
chapter's central concepts. Each has three hint levels (direction, key
fact, partial step) folded in `<details>`. Solutions written here are marked
"自解，待核" (own solution, unchecked) unless the book provides one.

## 7. progress.md

```markdown
# <book title>: progress
| Chapter | Status | Date | Central concepts | Open questions |
|---|---|---|---|---|
| 4 Statistics (§4.1-4.2) | studied | 2026-10-16 | MLE, NLL, MLE as KL minimization | Why is the MLE for the variance biased? |
Skipped on purpose: §4.6 (not needed for current project)
```
