<!-- Moved from skills/sv-write-intro/references/procedure.md by ADR 0021 (2026-10-18); licence CC-BY-NC-SA-4.0. Section text unchanged; pointers updated. -->

# Introduction Drafter

## Contents

- Overview
- Evidence rules (inherited)
- When to use this skill
- When NOT to use this skill
- Step 0: Load context
- Choose the route
- Pre-check: STEM or not
- Core procedure (STEM technique and new-problem papers)
- Empirical route (RQ-driven studies)
- What the user receives
- Outline mode (on explicit request)
- Tone references
- Cross-skill handoffs
- Output language
- Checklist
- Outputs
- Hand-offs

## Overview

The Introduction is the compressed version of the entire paper. In one and a
half to two pages it must state the research object, why the problem
matters, why existing work falls short, what the paper contributes, and how
the contributions map to sections. Reviewers decide whether to keep reading
by the end of the Introduction, so the logical throughline has to be
airtight.

This skill is a **prose generator**, not an outline generator. It takes a
small set of inputs (research area, limitations, key idea, challenges,
solution overview, optional references) and produces **six paragraphs of
real Introduction prose**. The six-paragraph flowchart works underneath as
an internal scaffold and never appears in the output.

The delivered text must read as if a researcher wrote it: flowing
paragraphs, no inline tags, no "Paragraph 1: Background" headings, no
severity tables, no consistency reports. Just the Introduction.

An explicit outline is still available: see "Outline mode" below.

## Evidence rules (inherited)

This skill follows the shared evidence discipline: every factual claim
traces to the user's materials, this session's verified retrieval, or field
common knowledge; model memory is never a source; delivered prose carries
zero bracketed placeholder tags; details the user did not provide (specific
scenarios, mechanisms, magnitudes, procedures, identifiers) are omitted, not
invented.

See also `skills/sv-write/references/evidence-discipline.md` and skills/sv-write/references/prose-delivery.md
(shared with `sv-write-section`).

## When to use this skill

- "Write the Introduction." "Draft the Intro from this idea."
- The user has a paragraph of research thinking and wants finished prose,
  not bullets.
- The user has Goal and Key Idea settled but no Introduction text yet.
- The user pastes references and asks for them woven into the Introduction.

## When NOT to use this skill

- Benchmark papers: `sv-write-skeleton` (the flowchart differs).
- Any non-Introduction section: `sv-write-section`.
- Prose exists and needs polishing: `sv-write-polish`.
- The user wants a submission-readiness verdict: `pre-submission-reviewer`.

## Step 0: Load context

Load `research-core` and follow its Step 0:

1. Read `research.yaml`: `field`, `venue`, `paper_type`, `review` (page
   budget), `source_of_truth.numbers`.
2. Load the core rules `precedence.md`, `claims-evidence.md` and
   `body-text.md`.
3. Load the field profile `fields/<field>.md` (its "Paper types",
   "Typical structure" introduction line, "What reviewers and advisors
   care about" and "Known disagreements", which settle the contribution
   format) and the venue profile `venues/<venue>.md` when it exists.
4. Load the `writing` checklist and the field additions whose scope
   matches.
5. If `sv-write-section` Phase 0 produced a claim ledger, read it: findings
   and numbers in the Introduction come from it.

Without `research.yaml`, decide the route from the user's material (RQs
with findings mean the empirical route; a method with challenges means the
six-paragraph route) and say which route was taken.

## Choose the route

| Paper | Route |
|---|---|
| `technique` or new problem/setting (AI/ML, databases, systems) | Core procedure below: six paragraphs, challenges mapped to modules |
| `empirical-study` (RQ-driven mining, survey or qualitative study) | Empirical route below |
| `benchmark` | `sv-write-skeleton` |
| `theory` or `field: math` | `sv-write-section` math route (statement-driven introduction) |
| Non-STEM by method | `sv-write-section` CER planning |

The six-paragraph flowchart and its limitations-to-challenges-to-modules
chain come from AI/ML and database conference practice. Do not force an
empirical study or a theorem paper through it: an RQ-driven study has no
modules, and inventing "challenges" for it produces the wrong paper type.

## Pre-check: STEM or not

The six-paragraph model (background, limitations, goal, challenges,
solution, contributions) is built for STEM and technical papers. If the
research is non-STEM by method (humanities, social science, economics,
law), do not force it through this scaffold; hand the task to `sv-write-section`,
whose CER planning covers those paradigms, while all evidence rules still
apply. The test is the research method: experiments, benchmarks, models, or
algorithms come here; everything else routes to `sv-write-section`.

## Core procedure (STEM technique and new-problem papers)

This procedure is AI/ML/systems-oriented (the challenges-to-modules
chain). Empirical studies use the empirical route further below.

Internal thinking first, prose second. None of the intermediate thinking is
printed.

### Step 1: paper-type positioning (internal)

See also `paper-types.md` for the Technique versus New Problem/Setting
distinction and worked examples from Alpha-SQL, AFlow, and LEAD.

- **Technique paper**: the contribution is a new method for an existing
  problem; the narrative axis is the key idea; Paragraph 3 is a short
  bridge.
- **New Problem/Setting paper**: the contribution is the problem
  formulation itself; Paragraph 3 is load-bearing.

### Step 2: plan the six paragraphs (internal)

See also `flowchart.md` for each paragraph's purpose, writing points,
and common failures.

For each paragraph, settle: its purpose; two to four concrete writing
points drawn from the user's inputs; and its gaps (what the inputs do not
yet cover). Gaps are reported to the user after the prose, never inside it.

1. Background and motivation; running example; why the problem matters.
2. Limitations of existing work (at most three).
3. Problem essence and goal; hard constraints explicit.
4. Key challenges (at most three).
5. Solution overview; one module per challenge.
6. Contributions (three or four, each mapping to a section).

### Step 3: the running example (internal)

See also `running-example.md` for the design principles and patterns.

If the user has not provided a running example, **do not fabricate one**.
The reference file's first principle is that the example is real, drawn
from real data or a real deployment. Write the background paragraph from
the user's own abstract problem description, and in the closing note ask:
"a concrete running example would make Paragraph 1 stronger; can you share
a real case from your experiments or deployment?"

### Step 4: alignment checks (internal, before writing)

See also `contribution-patterns.md` for strong versus weak
contribution patterns.

Verify silently: the running example from Paragraph 1 reappears in
Paragraph 5 or 6; every challenge answers a limitation or a hard
constraint; the goal aligns with contribution 1; challenges map one-to-one
to modules; contributions number three or four, each tied to a section,
none of them vague ("extensive experiments" is not a contribution).

A failed check is fixed in the plan before any prose is written. Never
write around a broken chain.

### Step 5: write the prose

Six flowing paragraphs, under these disciplines:

- **No paragraph labels in the output.** Natural transitions carry the
  structure ("Despite this progress, ...", "In this work, we ...", "We
  summarise our contributions as follows.").
- **Each paragraph is one block**, roughly 100-250 words, weighted by the
  paper type (see paper-types.md).
- **Citations**: numeric citation-sequence, `[1]`, `[2]`, ... by first
  appearance. A full six-paragraph Introduction typically weaves **15-25
  references**: 3-5 in the background, 5-8 in the limitations, 2-4 in each
  of paragraphs three to five, 0-2 in the contributions. A thin
  bibliography reads as an opinion piece. Search before writing: three to
  five retrieval rounds under different keywords build the pool, and the
  argument is organized around retrieved, verified works. A claim whose
  source cannot be found is rewritten to drop the need, never tagged. The
  prose is followed by a **References** list matching the marks
  bidirectionally. At three or more citations, run the independent
  citation-verification ladder defined in `sv-write-section` (a fresh-context
  check of every entry when the environment allows it, with honest
  degradation and disclosure otherwise).
- **Numbers and claims**: no invented percentages, speedups, or benchmark
  numbers. A specific gain appears only if the user reported it; otherwise
  "improves over prior baselines", with no annotation attached.
- **Tense**: past for prior work and observations; present or future for
  the paper's own unvalidated claims ("this paper proposes"). Without
  reported results, never "we achieved" or "we demonstrated".
- **Tone pass**: before finalising, strip AI-tone signals and unsupported
  superlatives, and match verbs to evidence strength (see the "Tone
  references" section below for where the shared wordlists live).

### Step 6: a short closing note (optional, three lines at most)

After the prose (and References), at most a short plain-language note:
gaps the user should fill, a paragraph written tentatively for lack of
input, or the running-example request from Step 3. No tables, no lists, no
severity labels. Nothing useful to say means no note at all.

## Empirical route (RQ-driven studies)

For papers that answer research questions rather than propose a method.
[src: note:n06§3; arc:@senior-a-comments:8-29; arc:CF-01@v2; arc:CF-03@v2] (candidate)

See also `empirical-intro.md`

Internal planning, then prose, as in the core procedure:

1. **Inputs.** The final RQs; for each RQ two or three findings with their
   claim-ledger rows; the prior work or assumption each RQ tests, with
   citations; the phenomenon figure if the author has one; one exemplar
   introduction from the target venue for a comparable niche topic. A
   missing input is reported in the closing note, never invented.
2. **Outsider question first.** The opening blocks say what the studied
   object is and why its problems cost something a general reader of the
   venue cares about, then why the data source matters to the field and
   how this domain differs, before any method.
3. **Gap.** What prior work covers and misses; the assumptions carried
   over from other domains, each cited; then "To our knowledge, no prior
   work ..." once.
4. **Scope sentence**, then "We investigate N research questions."
5. **One RQ block per research question**: the question in full and in
   bold; one sentence of the form "<why the field cares>, so we <what this
   RQ tests>"; two or three scoped "We find that ..." sentences taken
   from the ledger.
6. **Method in one sentence** (data, instrument, validation, application).
7. **Contributions in the venue's format**: itemized or not, as the venue
   profile or `sv-write-style-mine` decides; each contribution points to a
   section or artifact.
8. **Roadmap** paragraph, unless the venue's exemplars omit it.

Tense, numbers and hedging follow the field profile. Whether RQ findings
carry exact numbers is decided once for the paper, with the abstract,
summary boxes and conclusion.

## What the user receives

- Six paragraphs of Introduction prose separated by blank lines, citations
  as `[1]`, `[2]`, ... (empirical route: the blocks above, with RQ
  questions in bold and contributions in the venue's format).
- A References list right after the prose, when citations are present.
- Optionally, one one-to-three-line plain note.

Nothing else. The full prohibition list (headings, gate results, severity
summaries, placeholder tags, process preambles) lives in
skills/sv-write/references/prose-delivery.md and is binding.

## Outline mode (on explicit request)

When the user explicitly asks for an outline instead of prose ("just the
outline", "give me the skeleton first"), return the classic structure
instead: the type positioning (type, rationale, implication), then for each
of the six paragraphs its purpose, writing points, and gaps with severity,
then the five consistency checks (running-example loop,
limitations-to-challenges, goal-to-contribution-1, challenge-to-module
mapping, contribution-to-section mapping). The same internal planning,
externalized once, on request.

For the empirical route the outline lists each block's purpose and points,
each RQ with its why sentence and the ledger rows behind its findings, and
the checks in section 7 of empirical-intro.md.

## Tone references

The shared style references live with their canonical copies in
`sv-write-polish` (ai-tone-guardrails, academic-phrasebank,
section-conventions) and apply to this skill's prose pass; consult them
through that skill's references when finer wording support is needed.

## Cross-skill handoffs

- Introduction done, rest of the paper wanted: `sv-write-section`.
- Prose in place but stiff: `sv-write-polish`.
- Doubts that the idea itself can carry a top-venue paper: do not write
  that into the Introduction; put one line in the closing note and point to
  `idea-evaluator`.

## Output language

Follow an explicit language request first; a named Chinese journal or
Chinese thesis means Chinese prose; otherwise default to English. Never
infer the output language from the language of the user's message.

## Checklist

Run the research-core `writing` checklist items this skill owns, plus the
field additions whose scope matches, on the drafted Introduction:

- WR-03 outsider question answered first; WR-04 research questions (or
  contributions) stated in full; WR-05 exemplar for introducing the niche
  read; WR-24 novelty claims scoped and stated once.
- Also, because the Introduction carries findings: WR-16 number diet,
  WR-18 hedging, WR-19 scope, WR-20 nothing claimed that was not measured.
- Field additions: SE-01 for `field: se`; ML-01, ML-02, ML-06 for
  `field: ai-ml` (six-paragraph route); the owned items of other loaded
  profiles. FG-17 when the Introduction has a figure.

Report each item as pass, fail, n/a or unknown with evidence (the sentence
or block, the ledger row). `candidate` items are advisory. The report goes
to the author outside the prose; the delivered Introduction stays clean.

## Outputs

- The Introduction prose and its References list.
- An optional closing note of at most three lines.
- On request: the outline (Outline mode) and the checklist report.

## Hand-offs

- After drafting: `check-loop` for the multi-round research-fit,
  venue-fit and language checks.
- AI tone in the draft or in pasted text: `sv-write-humanize-paper`.
- Comments on the Introduction from co-authors, advisors or reviewers:
  `feedback-to-revision`.
- Contribution-list format or the venue's way of introducing a niche:
  `sv-write-style-mine`.
- The rest of the paper, or the claim ledger the findings need:
  `sv-write-section`.
