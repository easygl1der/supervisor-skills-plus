# Checklist: writing

Items for prose: framing, structure, terms, numbers in sentences, hedging,
citations and the de-AI pass. Each item turns a core rule into a check.

Run by: sv-write-section, sv-write-intro, sv-write-polish, sv-write-humanize-paper, sv-review-loop

## Contents
1. Before drafting
2. Framing and structure
3. Terms
4. Numbers and claims
5. Abstract and conclusion
6. Citations
7. Style and de-AI

## 1. Before drafting

### WR-01 Claim ledger first
- [ ] Check: Each section being drafted or revised has a claim ledger with
  the number, scope, source (script and output, or citation) and commit for
  every claim; every sentence with a number maps to a ledger row.
- Why: Without a ledger, fluent prose arrives first and numbers and scope are
  patched in later, if at all.
- Status: confirmed
- Scope: core
- Owner: sv-write-section, sv-review-loop
- Src: up:skills/sv-write/references/evidence-discipline.md; skill:deai-paper-writing; note:n02§11.5; note:n07§A.1

### WR-02 Numbers and tables in the manuscript before prose
- [ ] Check: The copyable numbers and tables a section needs are in the
  manuscript (or the ledger) before a writing skill drafts the prose around them.
- Why: A writing skill fills gaps with plausible numbers when real ones are
  not in front of it.
- Status: candidate
- Scope: core
- Owner: sv-write-section, experiment-workflow
- Src: arc:04-comms/20260920-msritp-meeting/README.md; note:n08§5#28

## 2. Framing and structure

### WR-03 Outsider question answered first
- [ ] Check: The introduction answers why the studied object matters to the
  venue's general audience before it describes methods.
- Why: A reviewer outside the niche stops reading if the first page does not
  say why they should care.
- Status: candidate
- Scope: core
- Owner: sv-write-intro, sv-write-section
- Src: arc:@senior-a-comments:8-29; arc:CF-01@v2; arc:01-checklist/checklist.md A2

### WR-04 Research questions in full in the introduction
- [ ] Check: Every research question (or contribution) is stated in full in
  the introduction, not only in the design section.
- Why: Readers judge the paper against its questions; they need them early.
- Status: candidate
- Scope: core
- Owner: sv-write-intro, sv-write-section
- Src: arc:CF-03@v2; arc:01-checklist/checklist.md A2; note:n07§B.5

### WR-05 Exemplar for introducing the niche
- [ ] Check: How published papers at the target venue introduce the paper's
  niche topic was read from at least one named exemplar, and the introduction
  follows a comparable path.
- Why: Venue readers expect a familiar on-ramp to an unfamiliar topic.
- Status: candidate
- Scope: core
- Owner: sv-write-intro, deep-research
- Src: arc:@senior-a-comments:4; arc:CF-04@v2

### WR-06 Why before how
- [ ] Check: Each method choice opens with the reason it is needed, then the
  procedure, then the number it produced.
- Why: A procedure without its reason reads as arbitrary.
- Status: candidate
- Scope: core
- Owner: sv-write-section, sv-write-polish, sv-review-loop
- Src: arc:@senior-a-comments:33-50; arc:ol:5ecaf3f; arc:msr:0f96193; note:n06§2.1

### WR-07 Current content only, outward framing
- [ ] Check: No revision narration ("we now", "as updated") and no history of
  the study plan ("the plan predicted") in the manuscript; changed facts are
  rewritten in place, not corrected by an appended sentence.
- Why: Reviewers read one version; history belongs in `docs/`.
- Status: confirmed
- Scope: core
- Owner: sv-write-section, sv-write-polish, sv-review-loop
- Src: skill:anti-accretive-docs; arc:@senior-a-comments:54-75; arc:ol:5ecaf3f; arc:CF-05@v2

### WR-08 Results sections follow one shape
- [ ] Check: Each results section runs question, why it matters, minimal
  method, one or two findings, implication, and opens with substance rather
  than procedure.
- Why: A fixed shape lets reviewers find the finding in seconds.
- Status: candidate
- Scope: core
- Owner: sv-write-section, sv-write-polish
- Src: arc:@senior-a-comments:104-120; arc:@senior-a-comments:141-157; arc:01-checklist/checklist.md W2

### WR-09 Paragraphs build on each other
- [ ] Check: Consecutive paragraphs connect (each uses what the previous one
  established); no list-like run of disconnected paragraphs; a paragraph that
  adds nothing is merged or cut.
- Why: A listicle structure reads as generated and hides the argument.
- Status: candidate
- Scope: core
- Owner: sv-write-polish, sv-write-humanize-paper
- Src: arc:CF-22@v2; arc:01-checklist/checklist.md W7; arc:msr:0f96193

### WR-10 Each caveat once
- [ ] Check: Each caveat is stated once, precisely, where it matters; longer
  disclaimers sit in methods or threats and are not repeated in results.
- Why: Repeated caveats dilute the findings and waste pages.
- Status: candidate
- Scope: core
- Owner: sv-write-polish, sv-review-loop
- Src: arc:@senior-a-comments:158-171; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H11

### WR-11 Page budget filled by priority
- [ ] Check: When pages are short, space is filled in this order: thin results
  expanded with explanation and examples, then method detail, then
  background, then implications and threats; never with padding material.
- Why: Late fills went to low-value material when no priority was set.
- Status: candidate
- Scope: core
- Owner: sv-write-section, sv-write-polish
- Src: arc:chat:group@2026-10-02T22:44; arc:msr:d0d4c03; note:n08§5#29

## 3. Terms

### WR-12 One name per concept
- [ ] Check: A term table (term, definition, rejected readings) exists; each
  concept and each measure has one name throughout; after every co-author
  pass the text is searched for the rejected readings.
- Why: Synonym drift makes reviewers think two things are being measured.
- Status: candidate
- Scope: core
- Owner: sv-write-section, sv-write-polish, sv-review-loop
- Src: arc:@senior-a-comments:1-3; arc:AH-01@v2; arc:01-checklist/checklist.md W10; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H19

### WR-13 Define before use
- [ ] Check: Every concept is defined before a later passage relies on it.
- Why: A forward dependency forces the reader to guess.
- Status: confirmed
- Scope: core
- Owner: sv-write-section, sv-review-loop
- Src: skill:writing-shape

### WR-14 Macros for repeated labels
- [ ] Check: Repeated labels and category names use macros so one edit
  propagates; spacing after macros is checked in the compiled PDF.
- Why: Hand-typed labels drift; macro spacing bugs are only visible in the PDF.
- Status: candidate
- Scope: core
- Owner: sv-write-polish, sv-write-section
- Src: arc:chat:group@2026-09-29T12:26; arc:msr:c93ef1f; arc:AH-02@v2; note:n08§5#36

### WR-15 No internal jargon
- [ ] Check: Project codenames, internal tool names and internal sample names
  are replaced by reader language; an outside reader is the test.
- Why: Internal names mean nothing to reviewers.
- Status: candidate
- Scope: core
- Owner: sv-write-polish, sv-review-loop
- Src: arc:@advisor-glimpse; arc:ol:e03c20a

## 4. Numbers and claims

### WR-16 Number diet
- [ ] Check: One number per claim sentence; no strings of percentages in a
  sentence; exact counts live in tables.
- Why: Dense numbers hide the finding.
- Status: candidate
- Scope: core
- Owner: sv-write-section, sv-write-polish
- Src: arc:@senior-a-comments:79-100; arc:CF-08@v2; arc:01-checklist/checklist.md W3; note:n06§2.3

### WR-17 Denominator named
- [ ] Check: Every share cited in prose names its denominator (of what, which
  subset).
- Why: A share without a denominator cannot be checked or compared.
- Status: candidate
- Scope: core
- Owner: sv-write-section, sv-review-loop
- Src: arc:@senior-a-comments:38-43; note:n07§B.5

### WR-18 Hedge interpretations, not measurements
- [ ] Check: Measured facts are stated plainly; interpretations are hedged
  once; verb strength matches evidence strength.
- Why: Hedged facts sound unsure; unhedged interpretations overclaim.
- Status: confirmed
- Scope: core
- Owner: sv-write-section, sv-write-polish, sv-write-humanize-paper
- Src: skill:humanize-paper; note:n02§10; up:skills/sv-write-section/references/verification-checklist.md

### WR-19 Claims scoped to what was studied
- [ ] Check: General claims carry scope words (which population, which
  subset, pooled or per group); when a pooled result does not hold in every
  group, the same sentence says so.
- Why: Unscoped claims are the first thing a reviewer attacks.
- Status: candidate
- Scope: core
- Owner: sv-write-section, sv-review-loop
- Src: arc:msr:24d8c65; note:n06§2.6; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H2

### WR-20 Nothing claimed that was not measured
- [ ] Check: No sentence claims a construct the study did not measure (for
  example severity, effort or size when only labels or elapsed time were
  measured).
- Why: Reviewers check claims against the method section.
- Status: confirmed
- Scope: core
- Owner: sv-write-section, sv-review-loop, sv-review-once
- Src: arc:CF-12@v2; arc:01-checklist/checklist.md W9; arc:msr:9c69675; user:2026-10-13 (promoted: failure had a clear bad outcome)

### WR-21 Causal words need a causal design
- [ ] Check: Causal verbs appear only with a causal design; otherwise the
  association is written and any explanation is labelled as untested.
- Why: An observational study cannot carry causal language.
- Status: candidate
- Scope: core
- Owner: sv-write-section, sv-review-loop
- Src: arc:msr:9c69675; note:n06§2.6

### WR-22 Results and implications kept apart
- [ ] Check: Results paragraphs report findings; implication paragraphs add
  no new numbers and no mechanisms the study did not test.
- Why: New numbers in implications have no method behind them.
- Status: candidate
- Scope: core
- Owner: sv-write-section, sv-review-loop
- Src: arc:01-checklist/checklist.md C6; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H4

### WR-23 Effect-size words match a stated scale
- [ ] Check: Adjectives for effect size ("small", "large") follow a scale
  named in the method.
- Why: Unanchored adjectives overstate small effects.
- Status: candidate
- Scope: core
- Owner: sv-write-section, sv-review-loop
- Src: arc:RS-02@v2; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H18

### WR-24 Novelty claims scoped and stated once
- [ ] Check: Gap and novelty claims carry "to our knowledge", come after what
  prior work does, and appear once.
- Why: Absolute novelty claims invite a counterexample from a reviewer.
- Status: candidate
- Scope: core
- Owner: sv-write-intro, sv-write-section
- Src: arc:msr:9c69675; arc:RW-01@v2; arc:CF-21@v2; arc:01-checklist/checklist.md A3

## 5. Abstract and conclusion

### WR-25 Abstract shape
- [ ] Check: The abstract gives, in about one sentence each: context, gap,
  the study, how it was done, the one or two most important findings, and the
  recommendation.
- Why: Reviewers decide on the abstract; a fixed shape keeps it complete.
- Status: candidate
- Scope: core
- Owner: sv-write-section, sv-write-polish
- Src: arc:chat:group@2026-10-03T19:18; up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md

### WR-26 Conclusion answers the question
- [ ] Check: The conclusion answers the introduction's question and states
  the contribution; it is not a section-by-section recap and not a
  word-swapped copy of the abstract.
- Why: The reader has read the paper; the conclusion adds the synthesis.
- Status: confirmed
- Scope: core
- Owner: sv-write-section, sv-write-polish
- Src: up:skills/sv-write-section/references/verification-checklist.md; up:handbook-en/03_Paper_Writing/3.5_writing-details-and-checklist.md

### WR-27 Conclusion length
- [ ] Check: The conclusion is one paragraph, shorter than the abstract, about
  one sentence per research question, ending on a research direction.
- Why: A long conclusion repeats results and costs pages.
- Status: candidate
- Scope: core
- Owner: sv-write-section, sv-write-polish
- Src: arc:01-checklist/checklist.md A4; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H7; skill:se-paper-writing; unverified (human origin of the rule)

## 6. Citations

### WR-28 Every citation exists and supports its sentence
- [ ] Check: Each cited work was opened and supports the sentence that cites
  it; no reference comes from model memory; no cited work is described as a
  kind of study it is not.
- Why: Fabricated or hallucinated citations are a desk-reject ground.
- Status: confirmed
- Scope: core
- Owner: sv-review-once, sv-write-section, sv-review-loop
- Src: arc:10-requirements/venue/fse-2027-requirements.md; up:skills/sv-write-section/references/verification-checklist.md; arc:01-checklist/checklist.md R3

### WR-29 References checked against an authoritative index
- [ ] Check: Every bibliography entry was checked against an authoritative
  bibliographic index or the publisher's page, and the audit output is kept
  in `docs/`.
- Why: Metadata copied from model output or old files is often wrong; one
  wrong reference can trigger a desk reject.
- Status: confirmed
- Scope: core
- Owner: sv-review-once, sv-write-polish
- Src: arc:10-requirements/venue/fse-2027-requirements.md; arc:chat:group@2026-09-29T11:44; arc:chat:group@2026-10-03T19:18; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md G4; note:n08§5#9

### WR-30 Bibliography matches the text both ways
- [ ] Check: Every in-text citation resolves to an entry and every printed
  entry is cited; unused entries are removed.
- Why: Uncited entries and broken keys are visible formatting errors.
- Status: confirmed
- Scope: core
- Owner: sv-write-polish, sv-review-once
- Src: up:skills/sv-write-section/references/verification-checklist.md; arc:01-checklist/checklist.md R5

## 7. Style and de-AI

### WR-31 De-AI pass under the contract
- [ ] Check: A de-AI pass ran under the de-AI contract: edits are diagnosed by
  intent, protected content (numbers, citations, terms, quotes, LaTeX
  structure) is unchanged, the output is not longer than the input, and no
  repeated pattern was replaced by another uniform one.
- Why: Reviewers notice AI-flavoured prose; careless rewriting damages
  protected content.
- Status: confirmed
- Scope: core
- Owner: sv-write-humanize-paper, sv-write-polish, sv-review-loop
- Src: skill:deai-paper-writing; skill:avoid-ai-writing; skill:humanize-paper; arc:CF-23@v2; note:n02§11.4

### WR-32 Punctuation bans only from an overlay or venue
- [ ] Check: Punctuation bans (for example semicolons or dashes) are applied
  only when a style overlay or the venue profile switches them on.
- Why: They are team or advisor preferences, not core rules.
- Status: confirmed
- Scope: core
- Owner: sv-write-humanize-paper, sv-write-polish
- Src: user:2026-10-13; note:n02§11.4

### WR-33 No scaffolding or process preambles
- [ ] Check: No internal scaffolding (ledgers, notes to self), process
  preambles ("Based on the evidence collected...") or inflation words without
  evidence remain in the prose.
- Why: These are the most visible traces of generated text.
- Status: confirmed
- Scope: core
- Owner: sv-write-humanize-paper, sv-write-polish, sv-review-loop
- Src: up:skills/sv-write-section/references/verification-checklist.md
