---
name: study
description: >-
  Understanding-first study partner: works through a paper, a
  textbook chapter or a single concept one idea at a time (motivation, plain
  principle, example, links to what the learner knows, a picture), then has
  the learner restate it, diagnoses the restatement as a mental model
  (mechanism, conditions, boundaries) and corrects from the learner's own
  associations. Keeps a learner profile in a separate study-vault repo. Use
  when the user says 我想搞懂, explain this concept, study this paper or
  chapter, or 精读.
license: CC-BY-NC-SA-4.0
---

# Study

## Overview

The goal is understanding for research, not exam practice: after a session
the learner can explain the idea in their own words, say when it holds and
when it breaks, and connect it to what they already use. Flashcards, quizzes
and spaced review exist only as options.

One concept at a time, each round follows the same protocol
(`references/protocol.md`):

0. Locate: why this concept now, what the learner already knows.
1. Plain principle in at most two sentences, no jargon.
2. Motivation and history: what was stuck before, why older tools failed.
3. Minimal example, then the general case, then the formal definition (only
   when a fitting example exists; never a forced one).
4. Links to known concepts: same, different, and where the analogy breaks.
5. Pictures: one motivation figure and one structure figure.
6. **The learner restates it** in their own words. Required.
7. Diagnosis against the expert mental model (mechanism, conditions,
   boundaries), with four labels per point.
8. Correction, starting from the learner's own associations; redraw the
   mental model in three colours (was right, corrected, new).
9. Loop 6 to 8 until no misconception remains.
10. Save the session to the study vault.

Defaults that hold in every mode: give hints, not answers; ask one question
at a time; keep replies short; copy formulas and numbers from the source
with locations; mark steps you add as added; never invent a citation, year
or number. **Paper mode:** name the loaded PDF and MinerU route in the
session opener (`source-priority.md` §5); do not teach claims from
`summary.md` or `transcript.md` alone.

## When to use this skill

- "I want to understand X", "explain X so that I really get it", a close reading of a
  paper, study chapter N of a textbook, prepare to use a method in research.
- After `paper-quickread`, when the reader wants depth on one part.
- When the learner says a restatement or an explanation does not click.

## When NOT to use this skill

- A five-minute overview of a paper: `paper-quickread`.
- A literature survey or a map of many papers: `deep-research`.
- Applying a learned method to the current project: `research-bridge`.
- Exam-style drilling only: use the options in `references/options.md`, or
  a dedicated flashcard tool; this skill does not default to it.

## Step 0: Load context

1. Load `research-core`: `references/core/inputs-mineru.md` and
   `references/core/claims-evidence.md`, and the field profile of the
   material (`causal`, `stats`, `math`, `se`, `ai-ml`). No `research.yaml`
   is needed; when one exists, read `field`, `project` and the RQs in
   `docs/STATUS.md` for step 0 of the protocol.
2. Find the study vault: `python scripts/vault.py where` (environment
   variable `STUDY_VAULT`, then `~/.config/study/vault`, then `~/study-vault`;
   otherwise fall back to `./reading/` and say so). Read
   `profile/knowledge.yaml`, `profile/misconceptions.md`, and the concept
   notes related to today's topic.
3. Material: in **paper mode**, follow `references/source-priority.md`
   (official PDF first; MinerU Markdown second; repo `summary.md`,
   `transcript.md`, `quickread.md` for orientation only). PDF text via
   `research-core` → `references/core/inputs-mineru.md`; stop if no route
   works. Reuse `source/paper.md` only when the MinerU route and PDF path
   are on record. **Concept/book** modes: user text or chapter PDF as
   today; summaries still cannot be sole evidence for numbers or theorems.

See: references/learner-profile.md
See: references/source-priority.md (paper mode)

## Mode

Decide once at the start and say which mode you chose (`--mode` overrides):

| Mode | Signals | Reference |
|---|---|---|
| paper | abstract and references, up to about 60 pages, arXiv or journal | `references/paper-mode.md` |
| book | table of contents, chapters, "chapter N", lecture notes | `references/book-mode.md` |
| concept | no material, only "I want to understand X" | protocol only; knowledge, web search, and the vault |

Then assess, in three lines: material type and difficulty, the
prerequisites it assumes (checked against `knowledge.yaml`), and which
files this session will write.

See: references/paper-mode.md
See: references/book-mode.md

## Workflow

### 1. Plan the concepts

List the 2 to 6 concepts the material needs, in dependency order. For each
prerequisite with no vault record, ask one short multiple-choice question
(never a test battery): how well the learner knows it (not studied /
studied but rusty / can use it / can explain it to others) and where they
learned it. Use a question tool when the environment has one, plain
lettered options otherwise. Ask less as the vault fills.

### 2. Run the protocol per concept

See: references/protocol.md

The restatement (step 6) is the one place the learner must think. Skip it
only when the learner says they want notes only, and record that.

### 3. Diagnose and correct

See: references/diagnosis.md

Report per layer (for example: mechanism right, conditions 2 of 3,
boundaries missing), then each point with its label: core right, partly
right, misconception (with its level), missing link. Correct by starting
from what the learner said; for a misconception, first a counterexample
that lets them see the problem, then the new model and why it explains the
counterexample.

### 4. Draw

Hand the figure to `sv-figure-explain` (ADR 0021; it owns the kit). Default to
HTML (SVG plus KaTeX) from `skills/sv-figure-explain/kit/templates/`, rendered to PNG with
`skills/sv-figure-explain/kit/render.sh`; save both files and embed the PNG in the notes. Use a
stepper only for content with an order (derivations, algorithms, processes).
Run the render check, open the PNG and look at it, fix and rerender (at
most three rounds). Numbers in figures need a source or the label
"illustrative".

See: ../sv-figure-explain/references/visuals.md
See: ../sv-figure-explain/references/visual-scenarios.md

### 5. Save

At the end of the session write the session summary, update or append the
concept notes, update `knowledge.yaml` and `misconceptions.md`, and commit
(push when a remote exists) with `scripts/vault.py save`. In environments
that cannot write files, print the finished Markdown for the learner to
paste.

See: references/session-save.md

### Options (off by default)

Socratic dialogue throughout, Feynman explain-back, light self-test with
confidence ratings, proof reconstruction with gaps for the learner, notes
only, Anki export.

See: references/options.md

## Why it works this way

Each rule above rests on learning research, summarised with verified
references: hint-first tutoring, self-explanation, conceptual change,
bridging analogies, concreteness fading, dual coding.

See: references/learning-science.md

## Checklist

Report pass, fail or n/a with evidence:

- MinerU route recorded for any PDF; formulas and numbers have locations;
  added steps marked.
- Paper mode: opener states primary PDF (path or id) and MinerU route;
  priority-4 repo aids not used as sole evidence (`source-priority.md`).
- Every concept round had a restatement, or the notes-only choice is
  recorded.
- Diagnosis gives a per-layer result and a label per point; misconceptions
  carry a level.
- Each figure rendered with exit code 0 and was looked at; numbers sourced
  or marked illustrative.
- Vault updated: session file, concept notes appended (not duplicated),
  `knowledge.yaml` self and AI levels, misconceptions; commit made or the
  fallback Markdown printed.
- `index.json` entries appended only (`../paper-quickread/scripts/index_append.py`).
- Field profile checklist items whose Owner includes `study`.

## Outputs

```
<study-vault>/
  profile/knowledge.yaml, sources.yaml, misconceptions.md
  concepts/<prefix>-<name>.md        def- thm- lem- method- ex-
  sessions/<YYYY-MM-DD>_<concept>.md
  papers/<YYYY-MM-DD>_<author>_<short-title>/   quickread.md, insights.md, method.md, qa.md, reflection.md, figures
  books/<book-slug>/progress.md, chNN-<slug>/
  index.json                         append-only
```

When the paper belongs to a research project that already has
`reading/papers/<paper>/`, study writes into that folder and the vault keeps
the concept notes and the profile.

## Hand-offs

- A five-minute card first: `paper-quickread`.
- The learned method could change the current project: `research-bridge`.
- Several papers into an evolution map: `deep-research` literature-map mode.
- A proof that needs formal checking: the owner's Lean skills, if installed.
