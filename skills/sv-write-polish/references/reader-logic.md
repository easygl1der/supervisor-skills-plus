# Reader logic

Rules about how a reader follows a paragraph of results or methods: what a
unit is, how many numbers a sentence carries, which comparison word fits
the data, where interpretation and advice go. They catch problems that a
grammar pass misses and that do not change the science, so a polishing
pass can fix most of them; when a fix would change a claim, flag it
instead (the faithfulness rule in SKILL.md wins).

Origin: the owner's former revision skill built from one advisor's
comments on an SE paper (`skill:se-paper-refinement`) and the comparison
table in `skill:se-paper-writing`. Only rules that survived the
contradiction pass in the evidence notes are kept (note:n02§10-11), restated
in neutral vocabulary with invented placeholder examples. Rules from a
single advisor are `candidate` (advisory); rules also stated as core rules
are `confirmed`.

## Contents
1. Keep analysis units stable
2. Number density
3. Comparison words
4. Define a metric before its first finding
5. Attribute findings and hedge only interpretations
6. No implications in results
7. Rule before exception, claim before detail
8. Motivate an operation before using it
9. Chain the research questions
10. Keep references alive
11. Not carried over from the source skills

## 1. Keep analysis units stable

Define each unit (item, record, submission, group, run, split, cohort,
cutoff) before using it and never switch its name. Two units with
different denominators or roles need different names. Write the unit as a
noun phrase before drafting a method or result: "30 random splits at each
cutoff", not "30 runs per quarter" when "run" could mean something else.
[src: skill:se-paper-refinement; note:n02§10] (candidate)

- Bad: "Each submission is evaluated ... the agents improve over time"
  (submission and agent used as if they were the same unit).
- Good: "Each submission (one entry to the leaderboard) ... unique agents,
  counted after merging repeated submissions, ..."

Polish check: search for each unit name and its near-synonyms; flag every
place where the text switches.

## 2. Number density

- One number per claim sentence; exact counts live in tables.
  [src: arc:@senior-a-comments:79-100; note:n06§2.3] (candidate)
- At most four or five percentages in a paragraph. Report the extremes and
  skip the middle; summarize a run that only rises or only falls as a
  range; aggregate when the total is the point.
  [src: skill:se-paper-refinement; note:n02§10] (candidate)
- One item or one shared pattern per sentence; do not chain several
  groups' trajectories in one sentence with stacked clauses.
  [src: skill:se-paper-refinement] (candidate)
- Bold headers state the claim in words, not a row of numbers.
  [src: skill:se-paper-refinement; arc:msr:0f96193] (candidate)

Polish moves: split, move a number to the table, or replace a list with a
range. Deleting a number the author printed is a meaning-risk edit: flag
it and say where the number already appears.

## 3. Comparison words

Each comparison word needs a specific kind of evidence.
[src: skill:se-paper-writing; note:n02§10] (candidate)

| Word | Needs |
|---|---|
| "proportional to" | a ratio compared across two or more pairs |
| "consistent with" | one pair whose values agree |
| "follows the same pattern" | a second pair mirroring the first |
| "disproportionate" | a share that departs from its reference share |

- Bad: "A's share of problems is proportional to its adoption." (one pair)
- Good: "A's share of problems is consistent with its adoption, and B
  follows the same pattern."

When the data do not support the word in the draft, propose the weaker
word and flag it (it changes the claim).

## 4. Define a metric before its first finding

Before a non-standard metric appears in a finding, state its numerator,
denominator, unit, direction (what a larger value means) and aggregation
level. Prefer the orientation that matches the reader's mental model; a
value below one for something that sounds like a count is a warning sign.
Never print an unlabeled "margin", "rate", "coverage" or "overlap": name
both sides and the unit. [src: skill:se-paper-refinement; note:n02§10] (candidate)

- Bad: "The margin is 8 points."
- Good: "The resolved-rate margin of the router over the fixed baseline is
  8 percentage points."

A missing definition is not invented while polishing: leave a note asking
the author for it.

## 5. Attribute findings and hedge only interpretations

Three kinds of claim, three treatments:

1. Established background: a general statement, with a citation.
2. A study observation: plain, with an evidence-matched subject or the
   condition ("we observe", "our data show", "in the simulation"). One
   scope statement can cover the evidence that follows it; restate scope
   when the dataset, period, comparison or unit changes.
3. An interpretation: hedged once ("may", "suggests", "is consistent
   with"), kept apart from the observation.

[src: skill:se-paper-refinement; note:n02§10] (candidate)

Hedge interpretations, never measured facts; verb strength matches
evidence strength. [src: skill:humanize-paper; note:n02§10] (confirmed)

- Bad: "Category A may account for 40% of items." (hedged measurement)
- Bad: "A accounts for 40% of items, showing that developers neglect it."
  (unhedged, untested interpretation)
- Good: "A accounts for 40% of items. One possible reason, which our data
  do not test, is ..."

Do not vary attribution by escalating ("proves", "establishes") or by
adding causal verbs; that is a meaning edit.

## 6. No implications in results

Results report what was observed. Advice ("teams should ...", "tool
builders need ...") moves to Implications. A comparison still needs its
direct meaning ("the least adopted strategy"), but not an untested cause.
[src: skill:se-paper-refinement; note:n02§11] (candidate)

Test: does the sentence tell the reader what to do? In Results, rewrite it
as what the data show, or flag it for the Implications section.

Also cut sentences that are not findings: a pointer-only sentence (fold
the reference into the data sentence: "Figure N shows that ..., with X%
..."), a bridge that narrates the paragraph's structure, a closing
sentence that restates the previous one. The figure sentence that carries
numbers stays; this resolves the earlier conflict between "point at the
figure" and "cut pointers". [src: skill:se-paper-refinement; note:n02§11] (candidate)

## 7. Rule before exception, claim before detail

- State the general pattern before its exception; a summary box that
  mentions only the exception distorts the result.
  [src: skill:se-paper-refinement] (candidate)
- A bold header is a contract: the paragraph develops what the header
  says, in the header's order. In an "A, but B" header the more concrete
  clause reads as the finding; if the paragraph is about B, make A the
  brief concessive clause. [src: skill:se-paper-refinement] (candidate)
- Explanation, then the numbers that support it; the bold claim comes in
  words, the figure or table sentence brings the numbers.
  [src: skill:se-paper-refinement; arc:msr:0f96193] (candidate)
- Discuss each entity in one place; keep listed items parallel; make every
  "this" and "it" point at an obvious noun. [src: skill:se-paper-refinement] (candidate)

Reordering inside a paragraph is a structural edit: do it when the meaning
is unchanged, and mention it in the change notes.

## 8. Motivate an operation before using it

Before a taxonomy, grouping, baseline or metric appears, the reader knows
the problem it solves: the task or limitation, the evidence that it
matters, what comparison is needed, then the method, then its result. A
later sentence cannot motivate an earlier method. Announce all levels of a
comparison before presenting the first.
[src: skill:se-paper-refinement; note:n06§2.1] (candidate)

## 9. Chain the research questions

For sequential RQs, the transition is an evidence chain, not a
table-of-contents sentence: the current RQ establishes a condition, the
condition leaves a concrete open problem, the next RQ tests it, and the
text does not claim the next method works before its evaluation.
[src: skill:se-paper-refinement; note:n02§10] (candidate)

RQs that are related but not dependent need no chain; do not invent one.

## 10. Keep references alive

After cutting or rewriting a sentence that carried a `\ref` or `\cite`,
check that every `\label` in the section is still referenced and every
citation still appears; fold the reference into the nearest surviving
data sentence. [src: skill:se-paper-refinement] (candidate)

## 11. Not carried over from the source skills

- Punctuation and connector bans (no semicolons, no dashes, no colons as
  consequence connectors, "use , so / , meaning / , with"): they made
  generated prose uniform. They live in an optional research-core overlay
  and apply only when a project switches it on.
  [src: note:n02§11.4; user:2026-10-13] (confirmed)
- Rules for one specific paper (the source skill's project section),
  person-specific quotes and the source paper's vocabulary.
  [src: note:n02§11.2] (candidate)
- "Fix every comment as requested, do not argue": comment triage belongs
  to `feedback-to-revision`. [src: note:n02§11.8; note:n02§10] (candidate)
- "Eliminate hedging" and "numbers first, interpretation second": both
  contradicted by the rules above. [src: note:n02§11.1] (confirmed)
- Present-tense-only for findings: tense is unresolved for SE; the field
  profile or venue decides. [src: note:n02§11.4] (candidate)
