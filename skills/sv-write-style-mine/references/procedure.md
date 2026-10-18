<!-- Moved from skills/sv-write-style-mine/references/procedure.md by ADR 0021 (2026-10-18); licence MIT. Section text unchanged; pointers updated. -->

# Style Mine

## Contents

- Overview
- Hard rules
- When to use this skill
- When NOT to use this skill
- Modes
- Step 0: Load context
- Input check (MinerU only)
- Phase 1: Corpus analysis and dynamic skill
- Profile output (venue profile and field proposals)
- Methods-borrowing card mode
- Checklist
- Outputs
- Hand-offs

## Overview

Venue fit is learned from the papers a venue actually accepts, not from a
generic style guide. This is the library's single style memory, in three
loops:

| Loop | Input | Output | Rules |
|---|---|---|---|
| **Dissect** | one exemplar paper, or a card from `sv-quickread-style` | a Paper Style Card (fields A to L) | `style-card.md` |
| **Accumulate** | several cards for one venue or field | Style Profile; with 5 to 10 papers and k/n support, rule lines for a venue or field profile (status `candidate` until confirmed) | `style-profile.md`, `profile-output.md` |
| **Apply** | target venue plus manuscript | `dynamic_writing_skill.md`, section-by-section revision, or a report-only check for `sv-review-loop` | `skills/sv-write-style-apply/references/revision-phase.md`, `skills/sv-write-style-apply/references/check-mode.md` |

A fourth mode borrows analysis methods from related work (method cards).

Cards are evidence, not rules: a single card never changes a profile.
Profiles reach `research-core` only through `sv-supervisor-harvest` and the
owner's approval. The core promise holds in every loop: this skill never
adds facts and never changes technical content.

Credit: written by the library owner as the standalone skill
`journal-adapt` (MIT, see `README.md`), merged here under the new name; the
old folder keeps a pointer. [src: note:n02§1; user:2026-10-12; user:2026-10-16]

## Hard rules

The six hard rules apply at all times and now live in `hard-rules.md`
(shared with sv-write-style-apply).

## When to use this skill

- Adapting a manuscript to a target journal or conference.
- Building or refreshing `venues/<venue>.md` "Style from exemplars", or
  filling a new or stub field profile from exemplar papers (often called by
  `sv-supervisor-harvest --new-field`).
- Borrowing analysis methods from a related-work corpus to strengthen
  research questions or a measurement design.
- Round 2 of `sv-review-loop` (venue and field style fit).

## When NOT to use this skill

- Removing AI tells: `sv-write-humanize-paper` (this skill only applies its own P5 list).
- Single-pass language polish: `sv-write-polish`.
- Drafting missing content or arguments: `sv-write-section` or `sv-write-intro`.
- Checking claims against evidence: `sv-review-loop` round 1 and the
  `integrity` checklist.
- Submission formatting and desk-reject checks: `sv-review-once`.

## Modes

| Loop | Mode | Trigger | Writes | Section |
|---|---|---|---|---|
| Dissect | Card | "dissect this paper's style", a card from `sv-quickread-style` | one card | Phase 1, Step 3 |
| Accumulate | Build | "learn the style of this venue" | cards, style profile, dynamic skill | Phase 1 |
| Accumulate | Profile | "make a venue profile", `--new-field` | venue profile draft, field proposals | Profile output |
| Apply | Revise | "revise my paper for <venue>" | revised sections, logs, rule candidates | Phase 2 |
| Apply | Check | called by `sv-review-loop`, or "does this fit the venue?" | report only | Check mode |
| (methods) | Method card | "borrow methods from related work" | method cards, transfer matrix, brief | Methods-borrowing |

Build runs before Revise, Profile and Check when no dynamic skill exists for
the destination.

### Cards arriving from sv-quickread

`sv-quickread-style` dissects one paper while it is being read and
writes a card in this skill's format to
`<reading-dir>/papers/<paper>/style-card.md`. Accumulate treats it exactly
like a card made here: file it under the venue or field corpus
(`<style.dynamic_skill>/cards/` or a `style/<venue>/cards/` folder in the
study vault), give it a paper ID, and count it only when the venue's corpus
is aggregated. One card never becomes a rule.

### Intake and author profiles

Exemplars can be found without any MCP server: `scripts/intake_search.py`
calls Crossref and OpenAlex (and Semantic Scholar when
`SEMANTIC_SCHOLAR_API_KEY` is set) to list a journal's new papers with a
causal keyword mark, list an author's works after a human picks the right
author ID, or filter an owner-curated publication list into an exemplar
table. Set `INTAKE_MAILTO` for the polite pools; keys stay in the
environment. Results go to `<STYLE_VAULT>/monitor/queue.jsonl` for the
owner to keep or skip. Full text, PDF caching and MinerU stay with the VPS
literature pipeline, not this skill.

An author profile is built from cards like a venue profile but kept
separate (`authors/<slug>/`), and stacks with a venue profile: venue genre
rules win over author voice, and every clash goes into the author/venue
conflict table instead of being resolved silently.

See also `intake.md`
See also `author-profile.md`

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

## Input check (MinerU only)

- Markdown, text or LaTeX: read directly; go to Phase 1.
- PDF: convert with MinerU following research-core
  `references/core/inputs-mineru.md` (MCP `mineru_parse_documents_smart`,
  then the official MinerU CLI, then a local MinerU). Exemplars that are
  published papers may go to the remote routes; ask before sending an
  unpublished manuscript.
- If no MinerU route works, stop and report the routes tried and their
  errors. Do not use another extractor and do not continue from abstracts.

Every converted file passes the readability gate in that file before it
enters Phase 1. Report the conversion summary.

See also `style-card.md`

## Phase 1: Corpus analysis and dynamic skill

### Step 1: Collect inputs

Ask, and wait for all answers:

1. Target journal, conference or track (and year).
2. Primary corpus folder: accepted papers from the target venue. Five to
   ten papers is the target; fewer than three produce no rules.
3. Optional secondary corpus: field-top or topic-similar papers.
4. Optional user or lab exemplars (unpublished ones stay private).
5. Optional static base rules (loaded as P4):
   1. General academic: `base_rules/general_academic.md`
   2. Economics: `base_rules/economics.md`
   3. ML / CV / NLP: `base_rules/ml_cv_nlp.md`
   4. CS / Engineering: `base_rules/cs_engineering.md`
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

See also `skills/sv-write-style-mine/references/base_rules/general_academic.md`
See also `skills/sv-write-style-mine/references/base_rules/economics.md`
See also `skills/sv-write-style-mine/references/base_rules/ml_cv_nlp.md`
See also `skills/sv-write-style-mine/references/base_rules/cs_engineering.md`

### Step 2: Convert PDFs if needed

Follow the input check above (MinerU only; stop on failure). Assign paper IDs (`<venue>_<NNN>`,
`field_<NNN>`, `exemplar_<NNN>`) and a `lit:` citation key per published
paper, with its full reference.

### Step 3: Extract Paper Style Cards

One card per readable paper, fields A to L (A to J from the original skill;
K claims and evidence, L threats and limitations, added here). State the
extraction rule aloud before each card. Describe moves, never content.

See also `style-card.md`

### Step 4: Aggregate the Style Profile

Count each pattern across primary cards and record its support `k/n` and
paper IDs. Add the split axes, the conflict table (corpus vs static base vs
field profile) and red flags.

### Step 5: Generate the dynamic writing skill

Write `dynamic_writing_skill.md` with the priority stack P1 (hard preserve,
including ADR decisions) to P5 (always remove), section guidance, cautions
and the language register. Give each corpus rule a local `DS-nn` id with its
support so that Phase 2 logs and check mode can cite it.

See also `style-profile.md`

### Human gate

Show the dynamic skill (and the profile drafts when in Profile mode) and
say:

> Phase 1 is complete. This is the dynamic writing skill I will apply.
> Please review it; you can edit the file directly. Reply "confirmed" to
> proceed, or tell me what to change.

Do not start Phase 2, Profile output or Check mode until the user confirms.

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
7. **Hand-off.** Show the diff, then hand both files to `sv-supervisor-harvest`,
   which bumps Version and Changelog and commits on `learn/<source>`.

See also `profile-output.md`

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

See also `method-card.md`

## Checklist

Run and report each item as pass, fail, n/a or unknown, with evidence (file
and line, diff, or the card IDs):

- From research-core `checklists/writing.md`: the items whose Owner list
  includes `sv-review-loop` that concern structure and framing (for example
  WR-06 why before how, WR-07 current content only, WR-12 one name per
  concept, WR-22 results and implications kept apart), in Revise and Check
  modes.
- Field and venue checklist additions whose Owner includes `sv-write-style-mine`
  (for example SE-18 and FS-03 on appendices as padding, when the project's
  field and venue match).
- In Profile mode, the research-core rules for profiles: every rule line has
  a `[src: ...]` and a status; `check_checklists.py` passes for new items;
  RC-24 (provenance written by hand, not machine-matched).
- Intake and author mode: every exemplar comes from the queue or the
  owner's publication list (none typed from memory); the author ID was
  picked by a human; author and venue rules sit in separate files; each
  author/venue clash has a row in `conflicts.md`.
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
- Intake: lines appended to `<STYLE_VAULT>/monitor/queue.jsonl`; author
  mode: `authors/<slug>/exemplars.md`, `cards/`, `profile.md` (draft until
  confirmed) and `conflicts.md`.
- Method card mode: `method-cards/*.md`, `transfer-matrix.md`, and
  implementation briefs on request.
- Check mode: a findings report (returned to `sv-review-loop` or written to
  `docs/log/`).

## Hand-offs

- Writing profile changes into research-core: `sv-supervisor-harvest`.
- Multi-round checks and applying check-mode findings: `sv-review-loop`.
- AI-tell removal beyond P5: `sv-write-humanize-paper`.
- Missing content or arguments found in diagnosis: `sv-write-section`,
  `sv-write-intro`.
- Implementing a borrowed method: `experiment-workflow`; recording the
  design change: `sv-supervisor-records` (ADR).
- Final formatting and submission checks: `sv-review-once`.
