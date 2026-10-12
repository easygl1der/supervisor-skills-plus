---
name: journal-adapt
description: >-
  Builds a corpus-grounded dynamic writing skill from exemplar papers of a
  target venue, revises a manuscript section by section without adding facts
  or changing technical content, writes venue profiles and field-profile
  proposals for research-core under a consensus threshold, extracts
  methods-borrowing cards, and runs a report-only venue-fit check for
  check-loop. Use when adapting a paper to a journal or conference, building
  a venue or field profile from exemplars, or borrowing analysis methods from
  related work.
license: MIT
argument-hint: "e.g. 'build a venue profile from these 6 accepted papers' or 'revise my intro for the target journal'"
---

# Journal Adapt

## Overview

Venue fit is learned from the papers a venue actually accepts, not from a
generic style guide. This skill reads a small corpus of exemplar papers,
describes each one on a structural **Paper Style Card**, aggregates the cards
into a **Style Profile**, and generates a reviewable
`dynamic_writing_skill.md` for one manuscript and one destination. After a
human gate it revises the manuscript one section at a time and logs every
change.

Strengthened for this library (DESIGN section 4.9):

1. **Profile output.** The Style Profile becomes a research-core venue
   profile ("Style from exemplars") and field-profile proposals. Each rule
   cites the exemplars that support it (`lit:<key>`) and passes a consensus
   threshold (at least k of n exemplars); splits go to Known disagreements.
2. **Methods-borrowing card mode.** Borrow analysis methods from related
   work without importing findings.
3. **Check mode.** A report-only venue-fit check that `check-loop` runs as
   round 2.

The core promise is unchanged: this skill never adds facts and never changes
technical content.

Credit: written by the library owner as the standalone `journal-adapt`
skill (MIT, see `README.md`); vendored here and extended. [src: note:n02§1; user:2026-10-12]

## Hard rules (apply at all times)

1. **Never add facts.** No new empirical claims, results, citations or data
   that are not already in the manuscript.
2. **Never change technical content.** Equations, LaTeX commands, citation
   keys, variable names, notation, numerical results, proposition statements
   and footnotes stay verbatim.
3. **Never paraphrase corpus papers.** Cards, profiles and rules describe
   structure and rhetoric only: no quotes, no paraphrases, no findings, no
   numbers from the exemplars.
4. **One section at a time** in Phase 2: diagnose, revise and log a section
   fully before moving on.
5. **No rule without support.** Every profile rule names its supporting
   exemplars by `lit:` key and its support count; patterns below the
   threshold are never stated as rules.
6. **Research-core is changed only through review.** Venue profiles and
   field proposals are shown as a diff and handed to `lessons-harvest`;
   nothing is merged without the owner's approval.

## When to use this skill

- Adapting a manuscript to a target journal or conference.
- Building or refreshing `venues/<venue>.md` "Style from exemplars", or
  filling a new or stub field profile from exemplar papers (often called by
  `lessons-harvest --new-field`).
- Borrowing analysis methods from a related-work corpus to strengthen
  research questions or a measurement design.
- Round 2 of `check-loop` (venue and field style fit).

## When NOT to use this skill

- Removing AI tells: `deai-writing` (this skill only applies its own P5 list).
- Single-pass language polish: `paper-polish`.
- Drafting missing content or arguments: `paper-writer` or `intro-drafter`.
- Checking claims against evidence: `check-loop` round 1 and the
  `integrity` checklist.
- Submission formatting and desk-reject checks: `pre-submission-reviewer`.

## Modes

| Mode | Trigger | Writes | Section |
|---|---|---|---|
| Build | "learn the style of this venue" | cards, style profile, dynamic skill | Phase 1 |
| Revise | "revise my paper for <venue>" | revised sections, logs, rule candidates | Phase 2 |
| Profile | "make a venue profile", `--new-field` | venue profile draft, field proposals | Profile output |
| Method card | "borrow methods from related work" | method cards, transfer matrix, brief | Methods-borrowing |
| Check | called by `check-loop`, or "does this fit the venue?" | report only | Check mode |

Build runs before Revise, Profile and Check when no dynamic skill exists for
the destination.

## Step 0: Load context

1. Load `research-core`: `references/core/precedence.md`,
   `references/core/claims-evidence.md`, `references/core/body-text.md`; the
   field profile named by `research.yaml` `field`; the venue profile for
   `venue` when it exists; overlays in `style.overlays`; the `writing`
   checklist (and `venue-submission` items in Profile mode).
2. From `research.yaml` read `field`, `subfield`, `venue`, `venue_year`,
   `paper_type`, `review.page_budget`, `style.exemplars` (corpus folder),
   `style.dynamic_skill` (output folder, for example `.style/fse/`) and
   `style.overlays`.
3. Read `docs/adr/` and the term table: these are P1 (never flipped).
4. Report what was loaded and each profile's status (`evidenced`,
   `partial`, `stub`). Without a `research.yaml`, ask the questions in
   Step 1 and use the folder layout of the original skill.

## Input and dependency check

Determine whether corpus and manuscript are already Markdown or text.

- Markdown, text or LaTeX: no converter is needed; go to Phase 1.
- PDF: ask whether to convert now or whether the user has Markdown.
  Optional converters:
  - the `mineru-document-extractor` skill (if installed). Its default mode
    uploads documents to a remote API, so use it for published exemplar
    PDFs; ask before sending an unpublished manuscript;
  - a local MinerU install (`mineru --version`), converting one PDF at a
    time, for example
    `python3 -m mineru.cli.pdf_to_md "<paper.pdf>" --output-dir "<corpus>/converted/<paper_id>/"`.
- If no converter works, ask for Markdown or text. Do not stop the workflow.

Every converted file passes the readability gate (sections readable, order
intact, equations, tables and citations not corrupted) before it enters
Phase 1. Report the conversion summary.

See: references/style-card.md

## Phase 1: Corpus analysis and dynamic skill

### Step 1: Collect inputs

Ask, and wait for all answers:

1. Target journal, conference or track (and year).
2. Primary corpus folder: accepted papers from the target venue. Five to
   ten papers is the target; fewer than three produce no rules.
3. Optional secondary corpus: field-top or topic-similar papers.
4. Optional user or lab exemplars (unpublished ones stay private).
5. Optional static base rules (loaded as P4):
   1. General academic: `references/base_rules/general_academic.md`
   2. Economics: `references/base_rules/economics.md`
   3. ML / CV / NLP: `references/base_rules/ml_cv_nlp.md`
   4. CS / Engineering: `references/base_rules/cs_engineering.md`
   5. External skills the user has installed (for example
      `hanlulong/econ-writing-skill`, `Master-cai/Research-Paper-Writing-Skills`,
      `SNL-UCSB/paper-writing-skill`, `lishix520/academic-paper-skills`,
      `blader/humanizer`). These are recommendations, not dependencies; ask
      for a local path and never download one unasked.
   6. A custom file (the user's own guide or SKILL.md).
   7. None: corpus rules, the research-core field profile and P5 only.
6. The manuscript's discipline, paper type and method type (prefilled from
   `research.yaml`).

When the research-core field profile is `evidenced` or `partial`, it joins
P4 alongside (and ahead of) the static base file. If the user is unsure
about a base file, recommend General academic.

See: references/base_rules/general_academic.md
See: references/base_rules/economics.md
See: references/base_rules/ml_cv_nlp.md
See: references/base_rules/cs_engineering.md

### Step 2: Convert PDFs if needed

Follow the input check above. Assign paper IDs (`<venue>_<NNN>`,
`field_<NNN>`, `exemplar_<NNN>`) and a `lit:` citation key per published
paper, with its full reference.

### Step 3: Extract Paper Style Cards

One card per readable paper, fields A to L (A to J from the original skill;
K claims and evidence, L threats and limitations, added here). State the
extraction rule aloud before each card. Describe moves, never content.

See: references/style-card.md

### Step 4: Aggregate the Style Profile

Count each pattern across primary cards and record its support `k/n` and
paper IDs. Add the split axes, the conflict table (corpus vs static base vs
field profile) and red flags.

### Step 5: Generate the dynamic writing skill

Write `dynamic_writing_skill.md` with the priority stack P1 (hard preserve,
including ADR decisions) to P5 (always remove), section guidance, cautions
and the language register. Give each corpus rule a local `DS-nn` id with its
support so that Phase 2 logs and check mode can cite it.

See: references/style-profile.md

### Human gate

Show the dynamic skill (and the profile drafts when in Profile mode) and
say:

> Phase 1 is complete. This is the dynamic writing skill I will apply.
> Please review it; you can edit the file directly. Reply "confirmed" to
> proceed, or tell me what to change.

Do not start Phase 2, Profile output or Check mode until the user confirms.

## Phase 2: Manuscript revision

Load only the dynamic skill and the manuscript. For each section: Round 1
diagnosis (problem type, severity, rule, venue match score 1 to 5), Round 2
revision under P1 to P5 with no new content, Round 3 a per-paragraph log
with a "Rule candidate" field. Collect rule candidates in
`revision_summary.md`; they feed `lessons-harvest`.

LaTeX sources in a git repo may be edited in place with a minimal diff when
the user agrees; otherwise output Markdown sections.

See: references/revision-phase.md

## Profile output (venue profile and field proposals)

After the human gate:

1. **Threshold.** n = readable primary cards; default
   `k = max(3, ceil(0.6 * n))` (4 of 6, as in the archived exemplar-corpus
   method). No rules when n < 3. [src: note:n02§8]
2. **Classify each pattern.** Support at least k: rule line. Two or more
   but below k with a competing pattern: Known disagreements (both sides,
   with exemplars). Below k without competitor: Unknown. Single paper: card
   only.
3. **Write rule lines** in the research-core format, citing every supporting
   exemplar: `- <move> (<x> of <n> exemplars). [src: lit:<a>; lit:<b>; ...] (candidate)`.
   Search existing rules first: same direction means add sources to the
   existing line; opposite direction means a Known disagreement.
4. **Venue profile.** Fill `venues/<venue>.md` with the
   `venues/_template.md` headings unchanged. Call sections come only from
   the official call, fetched now, quoted with URL and fetch date, unclear
   items marked CONFIRM. "Style from exemplars" lists the exemplars with
   full references, then the rule lines, lengths as measured ranges, and
   split axes. Checkable rules become checklist items with
   `Scope: venue:<name>` and `Status: candidate`.
5. **Field proposals.** Write `field-proposals.md` keyed by the field
   profile headings (Sources, Typical structure, Tone and phrasing, Rigor
   and threats, Checklist additions, Known disagreements, Unknown), with a
   duplicates-and-conflicts table. Patterns seen in one venue only stay in
   that venue's profile.
6. **Lifecycle.** Exemplar rules enter as `candidate`; they become
   `confirmed` when a second independent corpus or project agrees, the call
   or a published guide states them, or the owner decides (`user:<date>`).
7. **Hand-off.** Show the diff, then hand both files to `lessons-harvest`,
   which bumps Version and Changelog and commits on `learn/<source>`.

See: references/profile-output.md

## Methods-borrowing card mode

For a related-work corpus, write one Method Card per paper or cluster (unit
of analysis, sampling, measurement, QA, analysis, validity handling,
artifact, transfer notes; never findings). Then:

- **Phase A**: a transfer matrix (technique, source `lit:` keys, target RQ
  or design element, feasibility Now / Near / Future, data needed, threat if
  misapplied).
- **Phase B**: ranked borrowings in three tiers (implementable without new
  data; strengthens interpretation; position only, do not import).
- **Phase C**: on request only, an implementation brief with files, tests,
  power note, threats paragraph, a pre-set acceptance bar and a "Not doing"
  list. Wait for confirmation before editing anything.
- **Phase D**: optional prose hand-off to Phase 1 of this skill.

Locked design choices (ADRs, P1) are not reopened; propose an ADR instead.

See: references/method-card.md

## Check mode (check-loop round 2)

Report-only. Inputs: target sections, the dynamic skill (or, if missing, the
venue and field profiles with reduced coverage), ADRs and the term table,
and the round number from `check-loop`. Check structure, lengths against
budget, contribution format, results paragraph shape, tone, citation form
and the P5 phrases. Each finding gets `JA-r<round>-<nn>`, a location, the
rule it deviates from (`DS-nn` with support, or a profile rule with its
source), observed vs expected, severity and status (`open`, `locked`,
`advisory`, `repeat`). Never edit; return the report to `check-loop`, or
write `docs/log/<date>-journal-adapt-check.md` when run alone.

See: references/check-mode.md

## Checklist

Run and report each item as pass, fail, n/a or unknown, with evidence (file
and line, diff, or the card IDs):

- From research-core `checklists/writing.md`: the items whose Owner list
  includes `check-loop` that concern structure and framing (for example
  WR-06 why before how, WR-07 current content only, WR-12 one name per
  concept, WR-22 results and implications kept apart), in Revise and Check
  modes.
- Field and venue checklist additions whose Owner includes `journal-adapt`
  (for example SE-18 and FS-03 on appendices as padding, when the project's
  field and venue match).
- In Profile mode, the research-core rules for profiles: every rule line has
  a `[src: ...]` and a status; `check_checklists.py` passes for new items;
  RC-24 (provenance written by hand, not machine-matched).
- This skill's own gates: P1 content unchanged (diff shows no change to
  citations, math, numbers, labels); support counts match the source keys;
  no corpus text quoted.

## Outputs

- `<style.dynamic_skill>/cards/*.md`, `style_profile.md`,
  `dynamic_writing_skill.md`.
- `<manuscript>_revised/`: revised sections or in-place diffs, section logs,
  `revision_summary.md` with rule candidates.
- Profile mode: a venue profile draft in research-core format and
  `field-proposals.md`, plus the diff shown to the user.
- Method card mode: `method-cards/*.md`, `transfer-matrix.md`, and
  implementation briefs on request.
- Check mode: a findings report (returned to `check-loop` or written to
  `docs/log/`).

## Hand-offs

- Writing profile changes into research-core: `lessons-harvest`.
- Multi-round checks and applying check-mode findings: `check-loop`.
- AI-tell removal beyond P5: `deai-writing`.
- Missing content or arguments found in diagnosis: `paper-writer`,
  `intro-drafter`.
- Implementing a borrowed method: `experiment-workflow`; recording the
  design change: `research-records` (ADR).
- Final formatting and submission checks: `pre-submission-reviewer`.
