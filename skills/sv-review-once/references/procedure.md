<!-- Moved from skills/pre-submission-reviewer/SKILL.md by ADR 0021 (2026-10-18); licence CC-BY-4.0. Section text unchanged; pointers updated. -->

# Pre-Submission Reviewer

## Contents

- Overview
- When to use this skill
- When NOT to use this skill
- Step 0: Load context
- Core procedure
- Severity taxonomy
- Integrity gate
- Output format
- One day before the deadline
- Submission day
- Checklist
- Outputs
- Hand-offs

## Overview

Three to five days before a submission deadline is the window where
a careful external review pays off most. This skill takes a full
paper or key sections and produces a structured review across five
dimensions, each with severity-tagged findings and concrete
rewrite suggestions. It enforces the mechanical rules from the
writing-checklist section (no em-dashes, no banned AI-tone
vocabulary, leading text per paragraph, topic-sentence discipline,
citation-format uniformity) and surfaces the patterns that
non-native English-speaking authors most commonly violate
(articles, subject-verb agreement, tense consistency, which versus
that, Chinglish phrasing).

The output is not a rewrite. It is a prioritised list of findings
with severity tags; the author decides which to fix. CRITICAL items
should block submission until addressed.

This fork adds four things on top of the five dimensions: Step 0 loads
`research-core` (field and venue profiles, checklists); Step 7a runs the
research-core sub-checklists (threats, double-blind, artifact,
venue-submission, integrity) by item ID; Step 7b runs a devil's-advocate
pass; and a submission-day runbook covers the last 24 hours. The five
dimensions remain the review's core; their DB/ML-conference defaults
(Introduction flowchart, ablations, three or more datasets) yield to the
field profile when one is loaded.

## When to use this skill

- Three to five days before a submission deadline.
- The user asks to 'review this paper', 'audit before submission',
  'check the draft', 'find issues', 'proofread'.
- After a camera-ready revision, before sending the final version.
- After any major rewrite (rebuttal responses, Section 3 overhaul).
- When the user suspects AI-tone contamination in a section.
- One day before the deadline, as a read-only full check (see "One day
  before the deadline" below).
- On submission day, for the runbook only.

## When NOT to use this skill

- The paper is still being structured. Use `sv-write-skeleton` or
  `sv-write-intro` first.
- The user wants structural advice rather than review. Use the
  drafting skills instead.

## Step 0: Load context

Load `research-core`: the precedence file, `core/claims-evidence.md` and
`core/integrity.md`; the field profile named by `field` in `research.yaml`;
the venue profile named by `venue` (with its CONFIRM items); and the
checklists `master.md`, `threats.md`, `double-blind.md`, `artifact.md`,
`venue-submission.md` and `integrity.md`, plus field and venue additions
whose `Scope` matches (for example `SE-` and `FS-` items).

From `research.yaml` read `field`, `paper_type`, `venue`, `deadline`
(date and source), `review.double_blind`, `review.page_budget`,
`review.appendix_allowed`, `repos.artifact` (including
`anonymous_mirror`) and `source_of_truth.paper`. Name the commit or the
PDF under review; every finding refers to that version.

If `research.yaml` is missing, ask for field, venue and deadline source,
or hand off to `sv-supervisor`. A deadline without an official
source is reported as a finding (VS-01).

## Core procedure

### Step 0b: paradigm and venue fit

Before the dimensional review, settle two things. When a field profile is
loaded, it sets the paradigm and its weights (for example the SE profile
weights threats, replication and dual denominators, and a theory paper
under `math` treats proofs as the evidence); the list below is the
fallback.

**Paradigm**, judged by research method, because what counts as a
severe problem differs by paradigm:

- **STEM / technical** (CS, engineering, materials, chemistry): weight
  the Introduction chain, contribution-to-section mapping, baseline
  coverage, ablation-based attribution, figure quality. Benchmark
  papers additionally get coverage, reproducibility, and
  contamination checks; chemistry and materials get characterization
  completeness, purity, controls, replicates.
- **Humanities** (literature, history, philosophy, discourse
  analysis): weight whether the thesis is explicit and defensible,
  core concepts pinned down and stable across sections, the
  literature genuinely engaged, and the material (texts, archives,
  cases) able to carry the claims. Do **not** demand baselines or
  ablations here; check instead whether sub-arguments build on each
  other rather than sit in parallel, and whether conclusions outrun
  the material.
- **Empirical social science**: weight operationalized research
  questions, sampling and data-source justification, statistics
  matched to data types, conclusions bounded by the sample. For
  theory papers, "experiments" reads as "proofs": check the proofs,
  and never call the evidence thin merely because there is no results
  table.
- **Finance / economics**: weight identification credibility,
  endogeneity handling, robustness checks (their absence is a
  first-round flag), and economic versus merely statistical
  significance.
- **Law**: weight the accuracy of statutes, case numbers, and
  holdings (an invented or wrong citation is rejection-level), the
  clarity of the interpretive approach, and whether comparative
  arguments state their scope.

When the paradigm is unclear, ask the author before reviewing with
the wrong ruler.

**Venue fit**: if the stated target venue's scope visibly mismatches
the paper's topic or contribution type, that is a real rejection
risk, not a taste note. Flag it as a finding and suggest two or three
better-fitting venues.

### Step 1: Dimension 1 Macro logic review

See also `logic-and-structure.md` for the Logic First rule,
Self-contained rule, Leading Text rule, and Running Example rule.

Check:

- Introduction flowchart is intact (Background, Limitations, Goal
  or Key Idea, Challenges, Methodology, Contributions).
- Contributions map one-to-one with methodology modules and with
  section numbers.
- Experiments validate the paper's main claims, not tangential
  ones.
- Related Work covers the necessary prior art.
- Running example is consistent across Introduction, Methodology,
  Experiments.
- The headline result's attribution is isolated: an ablation
  separates the core mechanism from peripheral factors (a routing
  step, post-processing, a stronger base model, favorable samples).
  No such ablation: flag "attribution unverified" as MAJOR.
- Claims match their evidence: "solves" is stronger than most papers
  earn (usually "improves"); "state-of-the-art" needs the benchmark
  and conditions; "we are the first" gets checked or flagged.

Every break in the chain is CRITICAL.

**Retrieval-grounded checks** (when the environment has a
literature-search capability: a scholarly tool, web search over
scholarly indexes, or shell access to public APIs):

1. **Novelty verification**: extract two or three keyword groups from
   the paper's core method and problem setting, retrieve, and identify
   the three to five closest published works. If Related Work already
   covers them, the paper's positioning stands; a highly relevant
   uncovered work is a MAJOR finding ("missed X, Author et al.,
   Year"). Compare on difference axes; a similar title alone proves
   nothing.
2. **Citation completeness**: retrieve the field's recent
   representative works and its canonical ones, and compare against
   the reference list; a missing canonical baseline, founding paper,
   or recent survey is MAJOR.

Retrieval results support metadata-level judgments only; never quote
numbers or method details from search snippets. Without any retrieval
capability, skip these two checks and say so in the summary.

### Step 2: Dimension 2 Writing details review

See also `logic-and-structure.md` for paragraph-level rules.

Check:

- Every paragraph has a topic sentence.
- Paragraphs transition smoothly; no orphan paragraphs.
- Paragraphs are not over 10 lines; split if so.
- No repeated or redundant passages.
- Abstract covers problem, method, result.

### Step 3: Dimension 3 English grammar review

See also `grammar-rules.md` for the canonical list of errors
common to non-native English authors, with corrections and
examples.

Check the usual suspects:

- Article use (a, an, the).
- Subject-verb agreement (third-person singular).
- Tense consistency (Related Work past, method present).
- Passive-voice overuse.
- Which versus that.
- Sentence length; split long sentences at "Specifically,".
- Chinglish patterns.

### Step 4: Dimension 4 LaTeX format review

See also `latex-rules.md` for the canonical list of LaTeX-
specific issues.

Check:

- Equation numbering contiguous; every numbered equation
  referenced.
- Figures and tables have captions; captions are detailed.
- Citations use the correct command and the non-breaking tilde
  (for example, `ResNet~\cite{X}`, never `ResNet\cite{X}`).
- Labels use underscores, not spaces or hyphens.
- Vector figure format; no raster.
- Page-limit compliance.

### Step 5: Dimension 5 Figure quality review

See also `forbidden-patterns.md` for chartjunk patterns and
the full figure-quality checklist.

For each figure:

- Vector format.
- Font size large enough post-scaling.
- Colour-blind-safe palette; dual encoding.
- Self-contained caption with a finding in the first sentence.
- No chartjunk.
- Motivated example is concrete and failure-revealing.
- Solution overview has labels matching section titles.

### Step 6: Banned-vocabulary and em-dash scan

See also `forbidden-patterns.md` for the banned-word list.

Scan the full paper for:

- Em-dashes used as sentence connectors (banned; project rule).
- AI-tone words: innovative, pioneering, revolutionary paradigm,
  transformative framework, superior, surpass, excel, remarkable,
  unprecedented, breakthrough performance, general-purpose, is
  capable of, notably, yet, yielding, at its essence, encompass,
  differentiate, reveal, underscore, pave the way for, highlight
  the potential of, profound challenges, stems from, rigid,
  impede.

Flag each occurrence with a severity tag. Em-dashes are MAJOR by
default; banned AI-tone words are MAJOR if they appear three or
more times.

### Step 7: Section-by-section review

See also `section-guides.md` for the per-section writing
guides for Abstract, Introduction, Problem Formulation, Framework
or Method, Experiments, Related Work, and Conclusion.

For each section, check that the section's content matches the
guide's canonical structure (for example, Abstract's five-sentence
formula: what, why, challenges, how, results).

### Step 7a: Research-core sub-checklist passes

Run each file below item by item. Do not restate its items in the review;
cite the item ID, report pass, fail, n/a or unknown, and give the evidence
(quoted line, page, command output, commit). A tick without evidence is
`unknown`.

| File | IDs | Focus in this skill |
|---|---|---|
| `threats.md` | TH-01..TH-11 | Scope of claims, alternative explanations, threats agree with results |
| `double-blind.md` | DB-01..DB-08 | Only when `review.double_blind` is true (DB-08 always) |
| `artifact.md` | AR-01..AR-09 | Package holds and regenerates what the paper promises |
| `venue-submission.md` | VS-01..VS-11 | Official call, page limit on the PDF, template, form fields, upload timing |
| `integrity.md` | IN-01..IN-13 | Traceable numbers, agreement values, frozen reference, AI-use disclosure |

Then run the field and venue additions in scope (for SE, among others
SE-15 four threat categories, SE-17 DBLP-checked bibliography, SE-18 no
appendix as padding; for a venue profile its `FS-` style items) and the
`master.md` gate items MA-01..MA-06.

Severity mapping:

- A `confirmed` item that fails and touches a desk-reject cause named by
  the venue (anonymity, format, fabricated citations or results) is
  CRITICAL and a Blocker.
- Any other failing `confirmed` item is MAJOR.
- A failing `candidate` item is reported as advisory (MINOR); it does not
  block.
- `unknown` on a desk-reject item is treated as a Blocker until evidence
  exists.

Checks that need commands (identity search over the artifact and mirror,
page count on the compiled PDF, compile log, script output against the
manuscript) are run read-only; paste the command and a short output.
Without shell or repository access, report those items `unknown` and say
which command the author must run.

### Step 7b: Devil's-advocate pass

For each main claim (abstract, contributions, research-question answers),
write the strongest counter-argument a hostile but fair reviewer could
build from the paper's own numbers, tables and threats, and say where the
paper answers it. This is MA-05 and, for SE, SE-19.

See also `devils-advocate-pass.md`

### Step 8: Integrity gate

Run the checks in the Integrity gate section below.

### Step 9: Output

Emit the review in the Output format below, including the sub-checklist
results, the devil's-advocate pass and the Blocker list.

## Severity taxonomy

- **CRITICAL**: blocks submission. Example: contributions do not
  map to sections; introduction flowchart broken; no real-world
  running example; raster figure in final draft; missing key
  baseline; page-limit violation.
- **MAJOR**: reviewers will flag in first round. Example:
  topic-sentence absent from 3+ paragraphs; em-dash in 5+ places;
  banned AI-tone word in 3+ places; Table 1 comparison missing;
  chart type mismatched with data.
- **MINOR**: polish. Example: two long sentences that could be
  split; default Matplotlib styling; single article error.

Findings from the Step 7a sub-checklists and the Step 7b
devil's-advocate pass use the same taxonomy; Step 7a states how checklist
status maps to severity.

Severity honesty cuts both ways. A review that lists a dozen MINOR
items while missing the one rejection-level flaw sends the author to
submission with false confidence; a review that inflates taste issues
into CRITICAL destroys trust. The overall recommendation must match
the findings: any unresolved CRITICAL forbids "ready to submit", and
a near-ready verdict requires zero CRITICAL and at most two MAJOR.

## Integrity gate

Each bullet is tagged [inspection] (LLM verifies from the paper
text) or [attestation] (LLM runs the procedure and states it has
done so; user remains responsible for confirming completeness).

Before emitting the review:

1. **[inspection]** Every finding quotes specific text (sentence,
   phrase, figure name); no "the Introduction is unclear" without
   a quoted line.
2. **[inspection]** Every CRITICAL finding has a concrete fix
   suggestion, not "rewrite entirely".
3. **[inspection]** No fabricated quotes: only text actually
   present in the submitted material.
4. **[inspection]** Severity assignments follow the taxonomy;
   nothing is marked CRITICAL for taste reasons.
5. **[inspection]** Dimension 3 (grammar) findings cite the
   specific grammar rule from `grammar-rules.md`.
6. **[attestation]** Dimension 6 banned-vocabulary scan is run in
   full on the entire paper, not sampled. The skill attests the
   full scan; if the paper is extremely long, the skill states it
   chunked the input and describes the chunking strategy.
7. **[inspection]** Final score matches the CRITICAL + MAJOR
   count; a score of 9 or 10 requires zero CRITICAL and at most
   two MAJOR items.

If any [inspection] check fails, mark the output as "needs user
attention". For [attestation] bullets, the skill states the scope
of its scan and the user confirms completeness.

Run the gate silently. Do not print a per-gate pass or fail report;
a failure surfaces as a concrete finding in the affected dimension,
and the delivered review stays free of internal checking rituals.

## Output format

### Summary
- CRITICAL: <n>
- MAJOR: <m>
- MINOR: <k>
- Top three fixes first: ...

### Dimension 1: Macro logic
| # | Finding | Severity | Suggested fix |
|---|---|---|---|
| 1 | <quoted text> | CRITICAL or MAJOR or MINOR | <fix> |

### Dimension 2: Writing details
<same table shape>

### Dimension 3: English grammar
<same table shape, citing grammar-rule ID>

### Dimension 4: LaTeX format
<same table shape>

### Dimension 5: Figure quality
<same table shape>

### Banned-vocabulary and em-dash scan
<list with line references>

### Sub-checklist results (Step 7a)
| ID | Result | Evidence | Severity |
|---|---|---|---|
| DB-04 | pass or fail or n/a or unknown | <command output, page, line> | <per mapping> |

Only failing and unknown items are listed in full; passing items are
counted per file.

### Devil's-advocate pass (Step 7b)
<strongest counter-argument per main claim, the paper's answer or its
absence, and the resulting finding>

### Blockers and TODOs
| Blocker | Item or finding | Owner | TODO entry |
|---|---|---|---|

### Final score (1-10)
<score>

### Submission recommendation
- <Ready to submit | Needs 1-2 days more work | Needs major revision before submission>

## One day before the deadline

Run the whole skill read-only at least one day before the deadline,
against a named commit and its compiled PDF (MA-01). Read-only means no
edits to the paper, the artifact or the mirror during the run. When the
run ends, turn every Blocker into a `docs/TODO.md` entry with an owner and
a due time on the same day, and report the list to the authors; a Blocker
without an owner is how a predicted problem survives the deadline. In the
evidence project the final read-only check named the identity leak in the
artifact's project page; its Blockers had no owners, and the leak was
fixed only after the deadline, once a senior co-author raised it again.
[src: arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md B2; arc:chat:group@2026-10-06T05:09; note:n08§5#37; note:n07§B.3] (confirmed)

Re-run Step 7a (only the files touched since) after each later batch of
fixes, because late edits re-introduced removed font shrinking in the
evidence project. [src: arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md G3; note:n08§3] (candidate)

## Submission day

On the deadline day, switch from review to the runbook: early complete
upload, one editor at a time, plain-text abstract, metadata already
entered, anonymous mirror re-checked, and after the deadline the
submitted version synced back and tagged.

See also `submission-day-runbook.md`

## Checklist

This skill runs, and reports pass, fail, n/a or unknown with evidence:

- `master.md` MA-01..MA-06 (MA-05 is the devil's-advocate pass);
- `threats.md`, `double-blind.md`, `artifact.md`, `venue-submission.md`,
  `integrity.md` in full;
- field and venue additions whose `Scope` matches the project.

`writing.md` and `figures.md` are covered by Dimensions 1 to 5 and by
`sv-review-loop`; cite their IDs when a dimension finding matches one.

## Outputs

- The review in the Output format above, naming the commit or PDF reviewed.
- A Blocker list, each Blocker copied into `docs/TODO.md` with an owner.
- On submission day: the runbook with each step marked done, skipped with
  a reason, or open.

## Hand-offs

- Fixing findings raised as comments: `sv-feedback-revise` (each finding
  becomes an `FB-AG-<nn>` item).
- Language and style rounds after fixes: `sv-review-loop`, `sv-write-polish`.
- Artifact rebuild, anonymous mirror and number regeneration:
  `sv-experiment`.
- Recording the source-of-truth switch, the tag and the TODOs:
  `sv-supervisor-records`.
- Reviewer reports after submission: `sv-feedback-revise`, then
  `sv-feedback-rebuttal`.
