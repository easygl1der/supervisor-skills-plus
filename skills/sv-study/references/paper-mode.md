# Paper mode

## Contents
1. Files
2. Order of work
3. insights.md
4. method.md
5. qa.md (optional)
6. reflection.md
7. Follow-up questions

## 1. Files

In the paper folder (shared with `sv-quickread`):

| File | Written | Purpose |
|---|---|---|
| `quickread.md` | if missing, by `sv-quickread` first | the nine-section card |
| `insights.md` | always | the 3 to 5 ideas that matter most |
| `method.md` | when the paper has a method or proof worth reconstructing | derivation, step by step |
| `qa.md` | only when the learner asks | self-check questions |
| `reflection.md` | always | four questions about the paper's future |
| `deep-dive-<topic>.md` | per follow-up thread | never overwritten |
| `fig-*.html/png` | per figure | |

Each key concept of the paper also goes through the protocol and gets a
concept note in the vault.

## 2. Order of work

1. **Primary source first.** Run `source-priority.md` (resolve PDF →
   MinerU → session opener). Use `quickread.md` only to pick concepts and
   reading order; verify every claim and number against the paper before
   teaching. `summary.md` and `transcript.md` are orientation and
   cross-links, not evidence.
2. Choose the 2 to 4 concepts the paper's argument depends on (for a causal
   paper typically: the estimand, the identifying assumption, the
   estimator's key move, the inference method).
3. For each, run the protocol; write `insights.md` and `method.md` as the
   concepts settle, not before.
4. End with `reflection.md`.

See: `source-priority.md` (conflicts, assigned-readings packs).

## 3. insights.md

3 to 5 entries, each:

- **Insight** in one sentence.
- **Why it works**: the mechanism, with the location in the paper.
- **What it changes**: the shift from the usual way of thinking.
- **Trade-off**: what it costs (assumptions, variance, computation,
  generality).

## 4. method.md

- Copy each displayed equation with its number; under it, say what each term
  does and what changes if it is removed.
- Fill missing steps between equations; mark every added step 补 and say
  which fact it uses.
- For a proof: the chain of lemmas, the step that does the work, and which
  assumption each step uses. Use `skills/sv-figure-explain/kit/templates/stepper-proof.html` when the
  learner wants to see the derivation step by step.
- For an algorithm: pseudocode copied from the paper, then a trace
  (`stepper-trace.html`) on a tiny input.

## 5. qa.md (optional)

Only on request. Five basic, five intermediate, five advanced questions,
answers folded in `<details>`; each answer cites the paper location.
Purpose: self-check, not grading.

## 6. reflection.md

1. Where could this go next (extensions)?
2. Which assumption is most fragile, and what would happen without it?
3. In which setting would the method fail?
4. How does it compare with the closest prior work, in one table?

Our judgements are labelled as such; nothing is attributed to the authors
unless they wrote it.

## 7. Follow-up questions

Each new thread ("why the time weights are not regularized") gets its own
`deep-dive-<topic>.md`; add its concept to the vault if it is reusable.

Credit: the insight triad, the four reflection questions and the
three-level Q&A follow claude-paper's study skill (MIT); see
`THIRD_PARTY.md`.
