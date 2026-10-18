---
name: proposal-writer
description: >-
  Plans and drafts research proposals: thesis proposals (kaiti reports), PhD
  research plans and research statements, and grant applications such as
  NSFC, NSF, ERC and NIH. Builds the proposal spine first (questions, aims,
  feasibility evidence, falsifiable milestones, risks with fallbacks), then
  writes in proposal register against the call's own review criteria. Use
  when the user asks to write or restructure a proposal, research plan, or
  grant section.
license: CC-BY-NC-SA-4.0
argument-hint: "e.g. 'draft my kaiti report outline', 'write the research plan for this PhD application', 'turn these notes into NSFC research content', 'review my specific aims page'"
---

# Proposal Writer

## Overview

A proposal asks a committee to bet on work that has not happened yet. A
paper reports what was found; a proposal promises what will be done, shows
why it can be done by this person in this time, and says how everyone will
know whether it worked. The same idea therefore needs a different structure
and a different register from the paper it may later become.
[src: guide:https://www.darpa.mil/about/heilmeier-catechism@2026-10-17] (confirmed)

The skill works in a fixed order: read the call, build the proposal spine,
check it against evidence and reviewers, then write prose. Prose comes last
because most rejected proposals fail on the spine (no clear question,
dependent aims, no feasibility evidence, no way to tell success from
failure), and polished paragraphs hide those faults instead of fixing them.

It covers four genres, each with a section map and length budget in
`references/genres.md`:

| Genre | Typical reader | Decides |
|---|---|---|
| Thesis proposal (kaiti report, also master's) | supervisor plus a small faculty panel | whether the student may proceed to the thesis |
| PhD research plan or research statement | admissions or hiring committee | whether the applicant can define and run a research agenda |
| Grant application (NSFC, NSF, ERC, NIH and similar) | panel and external reviewers scoring set criteria | funding |
| Internal or fellowship proposal | small committee, often non-specialist | funding or time |

## When to use this skill

- "Help me write my kaiti report", "draft the research plan", "outline the
  NSFC application", "write the specific aims page", "my research
  statement for the job market".
- An idea has passed `idea-evaluator` and now needs to become a document
  that a committee will score.
- Notes from `sv-study`, `sv-quickread` or `deep-research` should be turned
  into a literature gap and a plan.
- An existing proposal draft needs a reviewer-lens audit or a restructure
  to a new call.

## When NOT to use this skill

- Deciding whether the idea is worth pursuing at all: `idea-evaluator`
  first. This skill assumes the core idea survived that check.
- A literature survey on its own: `deep-research`.
- Writing the paper or thesis chapters that report finished work:
  `sv-write-section` (`paper_type: thesis` for a dissertation).
- Polishing language only, or Chinese-to-English translation of a finished
  draft: `sv-write-polish`.
- Budgets, institutional forms, CV and biosketch formatting: outside scope;
  the skill only checks that the narrative and the stated resources agree.

## Step 0: Load context

Load `research-core`: `core/precedence.md`, `core/claims-evidence.md`,
`core/integrity.md`, the field profile named by `field` in `research.yaml`
(its "What reviewers and advisors care about" and "Rigor and threats"
sections shape the method and risk sections), and the checklist
`threats.md` (design-time items). When `research.yaml` exists, read
`field`, `subfield`, `stage`, `deadline` and `people`; a proposal usually
sits at `stage: idea` or `design`.

Then collect the proposal facts in one message, skipping any already known:

1. Genre and the exact call or school (funder program, year, university
   and department).
2. The official call text or template, with its fetch date. If the user
   has none, search for it and show the link; never write limits or
   required headings from memory.
3. Hard limits: pages or characters, required headings, deadline with
   time zone, language.
4. Duration and the applicant's stage and resources (hours per week,
   data access, compute, collaborators).
5. Existing material: notes, quickread cards, study notes, pilot results,
   previous drafts, reviewer comments from an earlier round.

Without `research.yaml`, ask for the field in the same message, or hand off
to `sv-supervisor`.

## Precedence

The call document or school template wins over everything in this skill,
including `references/genres.md`. Then a written instruction from the
supervisor or program officer, then the research-core field profile, then
this skill's defaults. When the call and this skill disagree, follow the
call and tell the user which default was dropped.
[src: up:skills/research-core/references/core/precedence.md] (confirmed)

## Workflow

### Phase 1: Call sheet

Write a one-screen call sheet before anything else: genre, funder or
school, version and fetch date, limits, required sections in their
required order, review criteria quoted from the call, deadline, and items
the call forbids (for example URLs in the body, or a separate heading the
call removed). Every line carries its source. Unknown items stay
`unknown` with the question that would settle them.

See: references/genres.md

### Phase 2: Proposal spine

The spine is the proposal in about one page of plain sentences, written
before any section prose:

1. **Heilmeier answers.** One or two jargon-free sentences each for the
   eight questions (what, how it is done today and its limits, what is new
   and why it should work, who cares, risks, cost, duration, mid-term and
   final exams).
   [src: guide:https://www.darpa.mil/about/heilmeier-catechism@2026-10-17] (confirmed)
2. **Research question(s).** Each question is answerable within the
   duration and names its object, its comparison and the evidence that
   would answer it. For a causal question, the estimand is defined before
   any estimator (research-core CI-01).
3. **Aims.** Two to four aims that serve one goal but do not depend on
   each other's success: a failed Aim 1 must not stop Aim 2. Dependencies
   live inside an aim, not between aims. Where one aim truly feeds another,
   the downstream aim names a fallback input that does not need the
   upstream result.
   [src: guide:https://pmc.ncbi.nlm.nih.gov/articles/PMC8344099@2026-10-16; guide:https://poorvucenter.yale.edu/media/621/download@2026-10-16] (candidate)
4. **Per aim**: the question or hypothesis, the approach in two sentences,
   the feasibility evidence (pilot data, prior result, access already
   secured), a falsifiable milestone, the deliverable, and the fallback.
5. **Gap statement.** What is known, what is missing, and why the missing
   piece matters, each with a source or a retrieval note.
6. **Expected contributions**, one per aim, each phrased as something a
   reviewer could check at the end.

Run the cascade test (delete Aim 1's result; does each later aim still
produce a deliverable?) and the exam test (can every milestone fail?).
Run the novelty retrieval for the central aim now, when the environment
has a literature-search capability (the method in `idea-evaluator`, fatal
flaw F1): a proposal whose core aim turns out to be done already is the
most expensive failure, and it is cheapest to find before drafting. With
no retrieval, the spine marks the central gap "unverified" and the first
milestone becomes that check. Fix the spine before moving on.

See: references/register-and-aims.md

If the spine shows the idea itself is weak (no gap survives retrieval,
feasibility is red), stop and hand off to `idea-evaluator`; do not write
around it.

### Phase 3: Evidence ledger

Build a ledger from the research-core claim-ledger template, saved as
`docs/proposal/ledger.md`, with one extra column: claim kind.

| Kind | Example | What it needs |
|---|---|---|
| cited | "method X assumes simultaneous adoption" | a source read at full-text level, with section, equation or table |
| preliminary | "a pilot on 40 repositories gave ..." | script, output file and date, as for any result |
| gap | "no study has applied X to Y" | the retrieval that was run (keywords, index, date); scoped wording |
| commitment | "Aim 2 will release the panel" | a milestone and a month in the timeline |
| assumption | "adoption dates are recoverable from release notes" | a risk-register row if it can fail |

Rules: a cited claim never goes beyond what the source supports (L3
metadata supports citation-level statements only); a gap claim is written
as "no work retrieved under these searches" and never as "no one has ever";
a preliminary result is reported in past tense with its scope and source.
[src: up:skills/sv-write/references/evidence-discipline.md] (confirmed)

Notes from `sv-quickread` and `sv-study` already carry locations (section,
equation, table) and their reading coverage (for example "read to 4.1;
theorem conditions unchecked"). Copy both into the ledger. A statement
about a part the notes did not cover is not a cited claim; it is a gap
claim or a `[to verify]` marker, and the proposal states the coverage
when it matters ("within the sections read").

When the related-work pool is thin, hand off to `deep-research` (literature
map mode when quickread cards or study notes already exist) before writing
the gap. Never fill the gap from memory.

### Phase 4: Section map, timeline and risks

Map the spine onto the genre's sections from `references/genres.md`, set a
length budget per section, and check that each of the six core elements
(question, motivation and gap, method and feasibility, timeline and
milestones, contributions, risks and alternatives) lands in a section,
even when the call merges them.

Then build the milestone table and the risk register.

See: references/timeline-risk.md

Visuals are optional and often expected (a technical roadmap figure in a
kaiti report or NSFC application; an aims diagram; a Gantt chart). Use the
study kit's HTML-to-PNG pipeline and pick the pattern from
`skills/sv-figure-explain/references/visual-scenarios.md` (P7 timeline for the Gantt
and the method lineage, P2 for the technical roadmap, P6 for "existing
methods versus ours"). Dates and numbers on a figure come from the
milestone table or carry "illustrative". Paper-grade figures go to
`sv-figure-design`.

### Phase 5: Draft in proposal register

Write section by section from the spine and the ledger, in the register
described in `references/register-and-aims.md`: future tense for planned
work, past tense for preliminary results, measurable commitments, hedged
expectations, and the reviewer's criteria answered in the section where
the reviewer looks for them.

- Output language follows the genre and the user: Chinese for a kaiti
  report or NSFC with English terms kept; English for NSF, ERC, NIH and
  most PhD applications. Explanations to the user are in Chinese by
  default.
- When the user has funded or approved exemplars from the same program or
  department, hand them to `sv-write-style-mine` (Dissect), then `sv-write-style-apply` for the local
  register; the facts stay from the ledger.
- Field conventions (what counts as rigor, typical threats) come from the
  loaded field profile, not from this skill.
- For a Chinese thesis proposal, use the sentence patterns in
  `references/zh-kaiti-register.md` (problem first, gap-organized review,
  one innovation axis per point, deliverable milestones). Do not invent
  school word counts.

See: references/zh-kaiti-register.md

**Draft markers, a deliberate difference from paper prose.** In Draft mode
(ADR 0016; `docs/adr/0016-proposal-draft-markers.md`) an unresolved
citation stays visible as `[cite needed: <what it must support>]` and an
unresolved fact as `[to verify: <question>]`, so the user sees every gap;
the Chinese equivalents are allowed in Chinese drafts. Content the skill
adds beyond the user's material is marked as an addition. In Final mode
no marker remains: each is resolved by retrieval, by the user, or by
deleting the sentence.

### Phase 6: Reviewer pass

Score the draft as the call's reviewers would, using the criteria quoted on
the call sheet, or the generic lens when the call gives none. Each score
quotes the sentence it rests on; the output is the three weaknesses most
likely to sink the proposal, each with a fix. Run the skim test: a reviewer
reading only the first page must be able to state the question, the gap,
the approach and why this applicant can do it.

See: references/reviewer-lens.md

### Phase 7: Citations and delivery

Verify citations with the `sv-write-section` verification ladder (independent
check when there are three or more citations or the mode is Final). Check
limits against the call sheet (pages, characters, required headings).
Deliver the document plus a short note: limits met, open markers, and the
top three reviewer risks.

## Checklist

Report each item as pass, fail, n/a or unknown with evidence (section and
line, ledger row, call-sheet line). A tick without evidence is unknown.

- **PW-01 Call sheet sourced.** Every limit, heading and criterion traces
  to the call or template with a fetch date.
- **PW-02 Question answerable.** Each research question names object,
  comparison and the evidence that would answer it within the duration.
- **PW-03 Aims independent.** The cascade test passes, or each dependency
  has a named fallback input.
- **PW-04 Feasibility shown, not asserted.** Each aim cites pilot data,
  prior results or secured access; when none exists the risk register
  says so and Year 1 produces it.
- **PW-05 Falsifiable milestones.** Every milestone has a criterion that
  can fail and a month; at least one go or no-go point exists.
- **PW-06 Risks paired with fallbacks.** Every high or medium risk has an
  early signal, a mitigation and a fallback that still yields a
  deliverable.
- **PW-07 Gap claims scoped.** Each gap statement names the retrieval
  behind it; no "first ever" without that.
- **PW-08 Contributions checkable.** Each contribution maps to an aim and
  a deliverable a reviewer could verify at the end.
- **PW-09 Register.** Planned work in future tense, preliminary results in
  past tense with sources, no planned result written as found.
- **PW-10 Reviewer criteria answered.** Each quoted criterion has a named
  section that answers it.
- **PW-11 Limits met; Final mode has no markers** (ADR 0016).
- From research-core: CI-01 (estimand before estimator, `field: causal`
  or any causal question), WR-19 (claims scoped), WR-21 (causal words need
  a causal design), WR-24 (novelty scoped and stated once), WR-28 (every
  citation exists and supports its sentence), TH-01 and TH-08 at design
  time, plus the field profile's design-time items.

The report goes to the user with the delivery note or to `docs/log/`; it
never enters the proposal.

## Outputs

Under `docs/proposal/` in the project (or a folder the user names):

- `call-sheet.md`: limits, required sections, criteria, sources.
- `spine.md`: Heilmeier answers, questions, aims, gap, contributions.
- `ledger.md`: the evidence ledger with claim kinds.
- `timeline.md`: milestone table and Gantt; `risks.md`: risk register.
- The proposal draft in the genre's structure (`<genre>-<date>.md`, or
  LaTeX or Word when the template requires it).
- `review.md`: the reviewer-lens scores, top three weaknesses, and the
  Checklist report.
- Optional figures from the study kit (HTML plus PNG).

Draft mode may keep `[cite needed]` / `[to verify]` markers; Final mode
must not (ADR 0016).

## Evals

Worked draft and reviewer pass:
`evals/2026-10-16_sdid-staggered-se/` (kaiti.md, review.md). The 2026-10-17
note in kaiti.md is the example that novelty retrieval must run before
drafting. `skills/sv-study/evals/proposal/` is a pointer only.

## Hand-offs

- Related work, gap search and method lineage: `deep-research`.
- Feasibility, fatal flaws and capability match before committing:
  `idea-evaluator`.
- Pilot runs that produce preliminary data: `experiment-workflow`.
- Citation verification and, later, the paper itself: `sv-write-section`.
- Local register from funded exemplars: `sv-write-style-mine`.
- Understanding a method the proposal depends on: `sv-study`; hooking notes
  to the current project: `sv-study-bridge`.
- Scope and design decisions taken while writing (frozen RQ set, chosen
  data source): `sv-supervisor-records` as an ADR.
- Language polish and AI-tell removal on the finished draft:
  `sv-write-polish`, `sv-write-humanize-letter`.
