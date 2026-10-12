---
name: rebuttal-guidance
description: >-
  Provides actionable peer-review rebuttal guidance (not full rebuttal prose)
  using conditional persuasion P(Z|X,Y): match reviewer mindset X, recommend
  strategy Y, optionally ground in manuscript evidence and similar successful
  historical (review, rebuttal) pairs. Use when the user pastes reviewer
  comments, asks for rebuttal help, rebuttal guidance, response to reviewers,
  how to reply to R1.W2, OpenReview rebuttal, or the reviewer ignored the rebuttal.
---

# Rebuttal Guidance

## Overview

This skill delivers **executable rebuttal guidance per concern**: structured plans,
evidence pointers, tone and strategy priorities. It does **not** produce
ready-to-paste rebuttal prose; the author writes the final text.

The core model is **conditional persuasion P(Z=1 | X, Y)**:

- **X**: reviewer mindset (behavior cluster inferred from review text)
- **Y**: rebuttal strategy vector (which tactics to emphasize)
- **Z**: success (score increase or paper accepted)

**Scope of the evidence.** The mindset library, its up-rates and the W/Q
format come from ML conference reviews on OpenReview (ICLR, NeurIPS, ICML,
EMNLP). Steps 3 and 4 are therefore ML-venue specific. For other venues
(SE conferences, journals, internal review) skip the cluster statistics,
keep Steps 1, 2, 5 and 6, and use the venue-neutral formats below. This
fork has no reviewer-report evidence of its own yet: the evidence project
had not received reviews, so no SE-specific rebuttal advice is claimed
here. [src: note:n03§5; arc:GAPS.md; note:n05§6] (confirmed)

## When to use

- User pastes Weaknesses / Questions from ICLR, NeurIPS, ICML, EMNLP, etc.
- User asks how to respond to a specific reviewer comment.
- User wants a structured plan before writing rebuttal prose.
- User asks which tone or evidence strategy fits a harsh vs. open reviewer.
- User says "reviewer ignored my rebuttal" and wants to recalibrate.
- A journal returned a major or minor revision and the user needs the
  point-by-point response letter.
- Co-authors or an advisor commented on a draft and the user wants a
  written internal response.
- `feedback-to-revision` produced a response table for a round of
  reviews and the reviewer-facing text is next.

## When NOT to use

- User wants full rebuttal text copied verbatim → output guidance first; warn
  against blind LLM paste.
- User asks to evaluate a research idea → use `idea-evaluator`.
- User asks for pre-submission paper review → use `pre-submission-reviewer`.
- No review text provided → ask for it first.

---

## Step 0: Load context

Load `research-core`: the precedence file, `core/feedback-loop.md`,
`core/claims-evidence.md`, the field profile named by `field` in
`research.yaml`, the venue profile named by `venue`, and the checklists
`threats.md` (for limitations) and `master.md`. From `research.yaml` read
`venue`, `stage` (rebuttal or camera-ready), `review.double_blind` and
`people`.

Then find the round's response table, `docs/feedback/<round>.md`, built
by `feedback-to-revision`. When it exists it is the inventory: its IDs
(`FB-R1-03`), decisions, change summaries, locations after change, commit
SHAs and verification status feed every step below. Keep the reviewer's
own numbering beside the FB ID (`FB-R1-03 = R1.W2`). When it does not
exist and the user wants changes in the paper, run `feedback-to-revision`
first; guidance on wording alone can proceed from the pasted review.

Pick the format (see "Response formats" below): conference rebuttal with a
word or character limit, journal revision letter, or internal co-author
response.

## Core procedure

### Step 1: Inventory concerns

Extract every numbered Weakness and Question from the pasted review. If the
user pasted only one reviewer's block, ask whether other reviewers exist.

Output a short table:

| ID | Type | One-line summary |
|----|------|-----------------|
| R1.W1 | W | ... |
| R1.Q1 | Q | ... |

### Step 2: Classify each concern

See: [references/concern-classification.md](references/concern-classification.md)

Tag each item as one of:
`misunderstanding | evidence_gap | novelty | baseline_fairness | scope_claim |
writing_clarity | theory | efficiency | other`

### Step 3: Match reviewer mindset (X) [ML-venue specific]

Skip this step and Step 4 outside ML conference review; note "no mindset
data for this venue" in the output.

See: [references/mindset-matching-heuristics.md](references/mindset-matching-heuristics.md)

Score the review on 5–7 behavior signals (openness, severity, constructiveness,
specificity, skepticism, harshness, actionability). Map scores to a cluster in
[references/mindset-library.md](references/mindset-library.md).

State: **matched cluster name**, confidence (high / medium / low), and the
specific phrases that triggered the match.

### Step 4: Strategy priorities for this mindset (Y) [ML-venue specific]

From the matched cluster in [references/mindset-library.md](references/mindset-library.md), read:

- **Historical up-rate**: calibrate how likely a score increase is.
- **Rule-stat diffs** (success vs. failure %): boost tactics with positive diff.
- **Cohen's d effects**: highlight dimensions with d > 0.8 in success group.
- **Success / failure patterns**: concrete do's and don'ts from data.
- **Key strategy**: one-sentence summary for this cluster.

Cross-check dimensions in [references/strategy-dimensions.md](references/strategy-dimensions.md).

### Step 5: Per-concern guidance

For each concern, emit a guidance block (not final prose):

```
### R?.W?: [short title]
- **Concern type**: ...
- **Mindset-aware strategy**: ...
- **Recommended structure**: Acknowledge → Response → Evidence → Revision note
- **Clarify from paper?**: yes/no: where to look (section, table, appendix)
- **New experiment needed?**: yes/no: what exactly (no fabricated numbers)
- **Tone note**: ...
- **Template**: A / B / C: see references/response-templates.md
- **Avoid**: ...
```

Do **not** fabricate experimental numbers. Mark anything unverified as
`[TO VERIFY]`.

When a response table exists, add to each block: the FB ID, the decision
and the location after change from the table, and whether the change is
verified by diff. A promised change that is still `pending` is written as
a plan, never as done.

### Step 5b: Requests the revision cannot meet

Some requests cannot be met within this revision: new data that does not
exist, a study design the team cannot rerun, a population the sample does
not cover. Do not promise them and do not argue them away. Turn each into
an explicit limitation:

1. Narrow the claim the request attacks, in the text where the claim is
   made.
2. Add or extend a threats or limitations paragraph that names the
   mechanism (why it cannot be met), its likely effect on the results, and
   any partial check that was possible (TH-01, TH-04, TH-08).
3. In the response, say what was narrowed and where the limitation now
   stands; do not call it future work unless a concrete plan exists.

[src: skill:se-paper-refinement; note:n02§10; note:n08§5#25] (candidate)

### Step 6: Integrity gate

Before finalizing, run through [references/checklist.md](references/checklist.md).

Key flags:
- Every W/Q has a guidance block.
- No fabricated numbers.
- Defensive phrases (e.g., "you misunderstood") flagged.
- Overpromise risk flagged for scope_claim and evidence_gap types.

### Step 7: Output format

For a journal letter or an internal response, deliver the format from
`references/response-formats.md` instead of the cluster-based summary.
For a conference rebuttal, deliver a `## Rebuttal Guidance` section
containing:

1. **Reviewer mindset summary**: cluster name, confidence, identifying phrases.
2. **Global strategy priorities**: 3–5 bullets from mindset data.
3. **Per-concern guidance**: Step 5 blocks for each W/Q.
4. **Checklist highlights**: pass/fail on key integrity items.

---

## Reference map

| Purpose | File |
|---------|------|
| Concern type → response priority | [concern-classification.md](references/concern-classification.md) |
| Reviewer signal → mindset cluster | [mindset-matching-heuristics.md](references/mindset-matching-heuristics.md) |
| Mindset clusters with stats & patterns | [mindset-library.md](references/mindset-library.md) |
| 10 strategy dimensions (Y) | [strategy-dimensions.md](references/strategy-dimensions.md) |
| Response templates A / B / C | [response-templates.md](references/response-templates.md) |
| Pre-submit integrity checklist | [checklist.md](references/checklist.md) |
| Venue-neutral formats (conference, journal, internal) | [response-formats.md](references/response-formats.md) |

The upstream reference files are in Chinese; keep them as they are. The
templates A / B / C apply to every format; the mindset files apply to ML
conference review only.

## Response formats

Three formats share one rule: every response row traces to an FB ID in
the response table, a location after change, and a commit.

- **Conference rebuttal** with a word or character limit: prioritise the
  concerns that can move the decision, answer each in two to four
  sentences with a pointer, and track the count against the limit.
- **Journal revision letter** (major or minor revision): point by point,
  every comment quoted, each answer with the change and its location
  (section, page, line in the marked-up version), plus a summary of
  changes. Nothing is skipped.
- **Internal co-author or advisor response**: decisions and reasons per
  comment, open questions, and conflicts between commenters shown with
  both positions.

See: references/response-formats.md

## Checklist

Run `references/checklist.md` (upstream integrity items), ML-08 when the
field is ai-ml, and these research-core items, reporting pass, fail, n/a
or unknown with evidence:

- every response row has an FB ID, a decision and a location after change
  (`feedback-to-revision` table);
- every "done" claim is verified by diff, every number traced (IN-01);
- every unmet request is a stated limitation, not a promise (TH-01, TH-04,
  TH-11: the threats paragraph says what the results show);
- at a double-anonymous venue the response reveals no identity (DB-01,
  DB-02, DB-03).

## Outputs

- Conference: `## Rebuttal Guidance` as in Step 7.
- Journal or internal: a response draft skeleton in the chosen format,
  with guidance per comment, written to `docs/feedback/<round>-response.md`
  when the user asks for a file.
- A list of claims narrowed and limitations added, for `paper-writer` or
  `paper-polish`.

## Hand-offs

- Building or updating the response table, applying changes and verifying
  diffs: `feedback-to-revision`.
- Writing the narrowed claims and limitations into the paper:
  `paper-writer` (threats section), then `check-loop`.
- New experiments a reviewer asked for: `experiment-workflow`.
- Re-checking the revised paper before resubmission:
  `pre-submission-reviewer`.
