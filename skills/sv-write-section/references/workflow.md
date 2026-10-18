<!-- Moved from skills/paper-writer/SKILL.md by ADR 0021 (2026-10-18); licence CC-BY-NC-SA-4.0. Section text unchanged; pointers updated. -->

# Paper Writer

## Contents

- Overview
- Hard rules
- When to use this skill
- When NOT to use this skill
- Step 0: Load context
- Capability check (run once per session)
- Workflow
- Proactive literature searching
- Citations and references
- Output language
- Boundaries with sibling skills
- Checklist
- Outputs
- Hand-offs

## Overview

This skill turns a researcher's ideas and materials into submittable paper
prose. One paragraph works; a full manuscript works.

It is not an outline generator and not a writing tutor. It writes the text,
under one non-negotiable condition: every written word must be traceable to
evidence. The author owns the substance (ideas, designs, results,
conclusions); this skill owns the linguistic realization of that substance,
and nothing more.

## Hard rules

These hold for every task this skill performs:

1. Every factual claim has one of three origins: the user's materials, this
   session's verified retrieval, or field common knowledge that carries no
   numbers, names, or comparisons. Model memory is never a source.
2. Delivered prose contains zero bracketed placeholder tags of any kind. A
   claim without a source is resolved by searching, rewriting, or deleting,
   never by tagging.
3. Concrete details the user did not provide are not written: no invented
   scenarios, mechanisms, magnitudes, procedures, or identifiers.
4. Claim strength never exceeds evidence strength.
5. Real results and planned or expected results are phrased differently and
   never mixed.
6. Internal planning never leaks into the output.

The full discipline, including the evidence hierarchy and the Evidence Map:
see skills/sv-write/references/evidence-discipline.md.

## When to use this skill

- "Write this idea into an English introduction paragraph."
- "Draft the Discussion in the style of a specific venue."
- "Write a full first draft of the paper."
- "Turn these notes into a Methods section."
- "Produce an abstract."

## When NOT to use this skill

- The user wants an Introduction specifically: `sv-write-intro` owns that
  section (this skill routes there automatically).
- The paper is a benchmark paper still being planned: `sv-write-skeleton`
  first, then return here for the prose.
- Existing prose needs language polishing: `sv-write-polish`.
- The logic skeleton is not settled: `sv-write-skeleton` first.
- The idea itself is unvetted: `sv-idea`.

## Step 0: Load context

Before Phase 1, load `research-core` and follow its own Step 0:

1. Read `research.yaml` at the project root: `field`, `subfield`, `venue`,
   `paper_type`, `stage`, `review` (page budget, appendix rule),
   `source_of_truth.numbers`, `style.overlays`.
2. Load the core rules this skill applies: `precedence.md`,
   `claims-evidence.md`, `body-text.md`, `integrity.md`.
3. Load the field profile `fields/<field>.md` (its "Paper types", "Typical
   structure", "Tone and phrasing" and "Known disagreements" sections drive
   Phase 3 and Phase 4) and the venue profile `venues/<venue>.md` when it
   exists. Overlays load only when `style.overlays` names them.
4. Load the `writing` checklist plus the field additions whose scope
   matches (for example `SE-` or `MT-` items).
5. Tell the user which profiles loaded and their status. A `stub` profile
   adds no rules; say so instead of guessing field conventions.

Without `research.yaml`, ask for field, venue and paper type in one
question, or offer the research-core template. When a profile and this
skill disagree, the order in `precedence.md` decides (venue call, recorded
decision, venue profile, field profile, core, overlay, this skill).

## Capability check (run once per session)

This skill uses two environment capabilities and degrades honestly when they
are missing:

- **Literature search**: a scholarly search tool if the harness provides
  one; otherwise web search against scholarly indexes; otherwise shell access
  to public APIs (Crossref, Semantic Scholar, arXiv, DBLP). If none exist,
  operate closed-book: cite only user-supplied references, keep citation
  claims at citation level, and disclose in the delivery note that no
  independent retrieval was possible.
- **Fresh-context sub-agents**: used for independent citation verification.
  Without them, fall to the same-context grounding rung. The ladder and its
  disclosure rules: see skills/sv-write/references/verification-ladder.md.

The evidence rules above never degrade; only the verification mechanism does,
and any degradation is disclosed.

## Workflow

Six phases, preceded by Phase 0 whenever the text reports results, numbers
or proofs. A full paper walks all of them explicitly; a single section runs
the same phases in lighter form, but never skips the claim ledger, Evidence
or Review.

### Phase 0: Claim ledger, numbers before prose

Fluent prose written before the numbers are fixed is the main reason
generated drafts fail: numbers and scope get patched in afterwards, or
plausible ones get invented. [src: note:n02§11.5; note:n07§A.1] (confirmed)

1. **Collect the verified numbers.** Read them from `docs/STATUS.md`
   ("Verified numbers": number, script, output file, commit) or from the
   numbers file named in `research.yaml` `source_of_truth.numbers` (for
   example `analysis/numbers.json`). A number found anywhere else (old
   drafts, chat, figures, memory) is not used until it is traced to one of
   these.
2. **Build the claim ledger** from the research-core template
   `assets/templates/claim-ledger.md`, saved as `docs/claims/<section>.md`:
   one row per claim with number, scope and denominator, source (script and
   output, or citation), code commit, data version, and whether a hedge is
   needed. For a theorem paper the ledger lists proof obligations instead
   (math-paper.md, section 1).
3. **Numbers into the manuscript before prose.** Put the tables and
   copyable numbers each section needs into the manuscript (or macros
   generated from the numbers file) before drafting the sentences around
   them. [src: arc:04-comms/20260920-msritp-meeting/README.md; note:n08§5#28] (candidate)
4. **Report gaps.** A planned claim with no ledger row is listed for the
   author; it is not drafted. A number that differs between STATUS and the
   numbers file stops the section until the author resolves it.

During Phase 4 every sentence with a number maps to a ledger row. The
ledger is a working file and never appears in the manuscript.

See also `skills/sv-write/references/evidence-discipline.md`

### Phase 1: Scope

Settle three things quickly, without interrogating the user:

- **Granularity**: full paper (produce working files: Evidence Map, chapter
  blueprint, then the draft) versus single section or paragraph (inventory
  mentally, deliver prose directly).
- **Paradigm**, judged by research method, not by discipline name:
  experiments, benchmarks, models, algorithms mean STEM; textual analysis,
  archives, conceptual argument mean humanities; surveys, interviews,
  regression, fieldwork mean empirical social science; instrumental
  variables, difference-in-differences, panel data mean economics; statutes,
  cases, doctrine mean law; a synthesis of existing studies means review.
  Unclear: ask one question about the core method and target venue.
- **Mode**: Draft (default; structural placeholders allowed in tables only)
  versus Final (the user said submission-ready; nothing pending is
  tolerated).

### Phase 2: Evidence

Before any words, lay out what the evidence base contains.

1. Inventory the user's materials. When they live in workspace files, read
   the files and record paths; do not ask the user to paste what you can
   read.
2. Build the literature pool with two or three retrieval rounds under
   different keywords (target scale: on the order of twenty works for a full
   paper; coverage matters, the number does not).
3. Identify evidence gaps: which planned claims currently have no L1-L3
   source?

Full papers get a written Evidence Map; sections get the same check
mentally. Template, levels, and gate: skills/sv-write/references/evidence-discipline.md.

**Gate**: a claim with no L0-L3 source is not written as fact. Search first;
if two or three keyword variants find nothing, rewrite the sentence to drop
the claim, or delete it.

### Phase 3: Blueprint

Route by paradigm and section:

| Case | Route |
|---|---|
| STEM Introduction | hand off to `sv-write-intro` (six-paragraph scaffold for technique papers; RQ-driven route for empirical studies) |
| STEM other sections | section-guidance.md content contracts |
| Non-STEM, any section | plan each paragraph on a CER skeleton: Claim (what should the reader believe), Evidence (what supports it, at which level), Reasoning (why that evidence supports it), Role (motivate, situate, propose, execute, present, interpret, qualify, or connect) |
| Benchmark papers | plan in `sv-write-skeleton`, then return here |

**Skeleton by paper type.** `paper_type` from `research.yaml` selects the
section skeleton from the field profile's "Typical structure"; the venue
profile adjusts lengths and required sections. When the field profile has
no skeleton for the type, use the matching file below and say so.

| `paper_type` | Skeleton |
|---|---|
| `empirical-study` (RQ-driven mining, survey or qualitative study) | field profile, else skills/sv-write/references/empirical-study-skeleton.md |
| `theory`, or `field: math` | field profile `math.md`, plus math-paper.md |
| `technique` | field profile; section-guidance.md; `sv-write-skeleton` for the logic chain |
| `benchmark` | `sv-write-skeleton` |
| `survey`, `thesis` | CER planning per paragraph; the field profile when it has a skeleton |

See also `skills/sv-write/references/empirical-study-skeleton.md`
See also `math-paper.md`

For a full paper, produce a chapter blueprint as a working file: section,
role, main judgment, evidence IDs (ledger rows), open gaps. Then check the
chain that fits the paper type end to end:

- **Technique papers** (the AI/ML/systems chain): limitations feed the key
  idea, the key idea raises the challenges, modules answer challenges one
  to one, contributions cover the modules.
- **Empirical studies**: the gap motivates each RQ, each RQ has a figure or
  table that answers it and ledger rows behind its findings, each RQ leaves
  the premise for the next, and each implication cites an RQ.
- **Theorem papers**: every statement has its assumptions, every
  dependency is proved or cited, and the main theorem's proof closes.

Broken links get fixed in the plan, never papered over in prose.

All of this is internal. None of it appears in the deliverable.

### Phase 4: Draft

Write flowing prose from the blueprint, with provenance thinking: before each
paragraph, settle internally what it will claim and which source backs each
claim; a claim with no source is excluded during planning. Write clean text
with no embedded markers of any kind.

Hard writing rules:

1. **Never generate content from model memory.** Three legitimate origins
   only (user, retrieval, L0). Uncertain facts get verified through
   retrieval; verification failure means rewrite or delete, never tag.
2. **Evidence level caps claim strength.** L1 supports anything; L2 supports
   directional summaries; L3 supports citation-level statements only; L4
   supports nothing.
3. **No invented specifics.** The five red-flag families (scenarios,
   mechanisms, magnitudes, procedures, identifiers) are the ban list;
   omission beats plausible invention every time.
4. **Separate real from planned results.** Confirmed results: "we observe",
   "results show". Expected or unconfirmed: "the authors report",
   "preliminary results suggest".
5. **Never oversell for the author.** Without evidence: "may", "shows
   promise for", "is expected to".
6. **Each section does its own job, once.** Introduction makes the reader
   care, shows the gap, states the goal. Methods let another researcher
   reproduce. Results report observations without why. Discussion explains
   why, connects to prior work, admits limits. Conclusion answers the
   Introduction. Abstract is a self-contained miniature written last. The
   same finding appears in at most three sections.
7. **No internal scaffolding in the output.** CER skeletons, paradigm calls,
   chain checks all stay silent.
8. **Field and venue shapes.** Paragraph shapes, tone, tense and hedging
   follow the loaded field profile and its "Known disagreements" decisions
   (for an empirical study: bold scoped finding, then the figure or table
   sentence with its numbers, then detail; no recommendations in Results).
   Punctuation bans apply only when an overlay or the venue switches them
   on.
9. **Current content only.** No revision narration and no study-plan voice
   ("the plan predicted", "as updated"); history belongs in `docs/`.

### Phase 4.5: Red flags (stop signals while writing)

| The thought | The correct move |
|---|---|
| "I remember this scale has 10 items" | Stop. Uncertain. Omit the item count |
| "I recall this paper used a meta-analysis" | Stop. No full text seen. Citation level only: "X et al. (Year) studied Y" |
| "I remember this case's citation number" | Stop. One digit off is wrong. Omit the identifier |
| "This material's conductivity is roughly..." | Stop. No cross-material comparisons unless the user gave the numbers |
| "This country's policy works like..." | Stop. Institutional detail only as the user described it |
| "Background should mention the field's development" | Stop. Background claims beyond L0 need L1-L3 sources. Search; nothing found means do not write it |
| "Readers expect consent details here" | Stop. Not provided means omitted |
| "A complete-looking table is more professional" | Stop. `--` in a cell is 100 times safer than an invented value |
| "This Discussion should be fuller" | Stop. Enrich with evidence, not invented mechanisms. Short and accurate beats long and hollow |
| "This method could apply to solar farms / autonomous driving..." | Stop. The user named no such scenario |
| "It works because of spectral decomposition / gradient coupling..." | Stop. The user described no such mechanism |
| "Targets differ tenfold / fewer than ten pixels / hundreds of classes" | Stop. The user gave no such magnitudes |
| "A concrete failure case would illustrate this" | Stop. No invented domain vignettes. Use the user's own description |

### Phase 5: Review

Three parts, in order:

1. **Source recall check plus inline checklist.** Walk
   verification-checklist.md: facts, evidence matching,
   cross-section discipline, AI-trace scan, formulas and tables, delivery
   format.
2. **Independent citation verification.** Mandatory for full papers, Final
   mode, or three or more citations; a fresh-context sub-agent receives only
   the prose and the reference list and verifies every entry through
   retrieval. Statuses, resolution routes, and the degradation ladder:
   skills/sv-write/references/verification-ladder.md. Delivery waits until no unresolved
   problem entries remain.
3. **Know what review cannot do.** Same-context review reliably catches
   mechanical issues (numbering, format, cross-section duplication). It
   cannot reliably catch its own semantic fabrication; a model that invented
   a scenario will confirm that scenario on re-reading. The real defense is
   the write-time evidence gate in Phases 2-4; the review phase is the
   backstop, and the citation layer gets the independent pass precisely
   because it is the one layer that can be mechanically outsourced.

### Phase 6: Deliver

Deliverable and prohibitions: skills/sv-write/references/prose-delivery.md.

- Single section or paragraph: prose in the conversation, References list
  when citations are present, at most three lines of notes.
- Full paper: the manuscript written to a workspace file (Markdown or
  LaTeX), References included; Evidence Map and blueprint remain separate
  working files, available on request, never embedded in the manuscript.
- Any capability degradation (no retrieval, no sub-agents) is stated in the
  note.

## Proactive literature searching

Do not wait for the user to hand over every reference. Sparse citation reads
as an opinion piece and reviewers reject it.

Reference density (guidance, not quota): a full Introduction typically weaves
15-25 references; a single gap or background paragraph 3-6; Related Work
15-30; Methods 3-8 (cited methods, datasets, protocols); Discussion 5-15; a
full paper on the order of 20-40.

**Search before writing, not after.** Before drafting any section, run three
to five retrieval rounds under different angles: core terminology; method or
model names; application domain; venue or author names. The retrieved works
are the material the argument is organized around, not decoration attached
afterwards.

Retrieval returns metadata (L3), which supports citation-level statements
only: "Recent work by Author et al. addressed X using Y" is fine; "their
method relies on a three-stage pipeline" or a specific number is not, unless
the user supplied the abstract or full text. Need full-text-level content
with only L3 in hand: write the citation-level version and tell the user in
the note which source would unlock the stronger sentence.

If a drafted section comes out visibly under-cited, go back and search
another round, then weave real findings in. Never bridge the gap with a
placeholder.

## Citations and references

Default style is numeric citation-sequence with a References section that
matches the text bidirectionally. Entry formats, author rules, missing-field
handling, and the alternate styles (APA, Chicago, Harvard, Vancouver):
skills/sv-write/references/citation-style.md.

## Output language

Follow an explicit language request first. If the target is a Chinese
journal or a Chinese thesis, write Chinese academic prose; otherwise default
to English. Never infer the output language from the language the user typed
in: describing ideas in Chinese and submitting in English is the normal
case.

## Boundaries with sibling skills

- `sv-write-intro`: Introduction prose (this skill routes STEM Introductions
  there).
- `sv-write-polish`: polishing existing prose, including Chinese-to-English.
- `sv-write-skeleton`: the pre-writing logic skeleton.
- `sv-write-skeleton`: planning benchmark papers.
- `sv-review-once`: reviewer-style audit of the finished draft.
- `sv-idea`: whether the idea is worth pursuing at all.

If drafting reveals that the problem is not "how to write it" but "does the
core claim hold", say so plainly in the delivery note and point to
`sv-review-once` or `sv-idea`. Never write a defense for a
claim the user's own data undermines.

## Checklist

Run the research-core `writing` checklist items this skill owns, plus the
field additions whose scope matches, on the drafted text:

- Before drafting: WR-01 (claim ledger first), WR-02 (numbers before prose).
- Framing and structure: WR-03, WR-04, WR-06, WR-07, WR-08, WR-11.
- Terms: WR-12, WR-13, WR-14.
- Numbers and claims: WR-16 to WR-24.
- Abstract and conclusion: WR-25, WR-26, WR-27.
- Citations: WR-28.
- Field additions: SE-01, SE-02, SE-03, SE-06, SE-08, SE-09, SE-11 to
  SE-15, SE-17 for `field: se`; MT-01, MT-04, MT-06, MT-07 for
  `field: math`; the owned items of other loaded profiles.

Report each item as pass, fail, n/a or unknown with evidence (file and
line, ledger row, command output). A tick without evidence is unknown.
`candidate` items are advisory. In Final mode, a `confirmed` item that
fails blocks delivery. The report goes to the author with the delivery
note or to `docs/log/`; it never enters the manuscript.

## Outputs

- The prose or manuscript file (Phase 6).
- `docs/claims/<section>.md`: the claim ledger or proof-obligation ledger.
- Working files on request: Evidence Map, chapter blueprint.
- The checklist report and a list of gaps (claims without ledger rows,
  open proof obligations, numbers that disagree between sources).

## Hand-offs

- After a draft: `sv-review-loop` for the multi-round research-fit, venue-fit
  and language checks; offer it at the end of every full-section delivery.
- AI tone found in the draft or in co-authors' text: `sv-write-humanize-paper`.
- Comments from co-authors, advisors or reviewers on the draft:
  `sv-feedback-revise`.
- A single light language pass: `sv-write-polish`.
- Venue style from exemplar papers, contribution-list format: `sv-write-style-mine`.
