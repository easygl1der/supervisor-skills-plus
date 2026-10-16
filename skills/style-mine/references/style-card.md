# Paper Style Card

## Contents
1. Paper IDs and citation keys
2. Extraction rule
3. Card format (fields A to L)
4. Where cards are saved
5. Readability gate for converted papers

The Paper Style Card is the unit of evidence for every rule this skill
produces. Fields A to J come from the original skill (then called journal-adapt). Fields K
(claims and evidence) and L (threats and limitations) were added because
style cards that only describe rhetoric missed the evidence conventions that
reviewers check. [src: note:n02§1]

## 1. Paper IDs and citation keys

Each exemplar gets two names:

- A **paper ID** for files: primary corpus `<venue_abbr>_<NNN>` (for example
  `fse_001`), secondary corpus `field_<NNN>` or `<venue_abbr>_<NNN>`,
  user or lab exemplars `exemplar_<NNN>`.
- A **citation key** `lit:<firstauthor><year><firstword>` (lowercase ASCII,
  for example `lit:smith2021mining`). Rules in profiles cite exemplars only
  by this key. The full reference (authors, title, venue, year, DOI) goes
  into the Sources list of the profile that uses it.

Unpublished lab or advisor exemplars get no `lit:` key. Cite them as
`proj:<project>/<path>` and never copy their text into a shared profile.

## 2. Extraction rule

Before extracting, state:

> I will describe only structure and rhetorical patterns. I will not quote,
> paraphrase, or reproduce any content from this paper.

Describe moves, not content. "Opens with a process puzzle in one sentence"
is a structural description. Anything that restates the paper's topic,
data, numbers or findings is not allowed on a card.

## 3. Card format (fields A to L)

```
## Paper Style Card: <paper_id>

METADATA
- Paper ID: <paper_id>
- Citation key: lit:<key>
- Authors: <LastName, F.; ...>
- Year: <YEAR>
- Venue: <venue and track>
- Corpus role: primary_target_venue | secondary_field | user_exemplar
- Conversion status: converted_checked
- Paper type: empirical study | technique | tool | benchmark | theory | survey | mixed
- Method type: theory | simulation | empirical | calibration | qualitative | mixed

A. ABSTRACT STYLE
- Opening move: <e.g. "opens with a policy-relevant phenomenon, one sentence">
- Structure: <sequence of moves, e.g. phenomenon -> gap -> method -> finding -> implication>
- Tense pattern: <e.g. present for context, past for findings>
- Contribution placement: <e.g. finding in sentence 4, no explicit "contribute" framing>
- Length: <approx word count>
- Register: technical | policy-accessible | mixed

B. INTRODUCTION ARCHITECTURE
- Hook type: phenomenon | puzzle | policy-failure | theoretical-debate | empirical-gap
- Opening move: <how the first paragraph is built>
- Contribution placement: early (para 2-3) | late (para 5+) | embedded
- Contribution format: numbered list | prose | bullets | embedded | RQ list
- Literature positioning: standalone section | integrated into intro | both
- Roadmap: explicit section-by-section | narrative | absent
- Intro length: <approx paragraphs>
- Move sequence: <one tag per paragraph, in order, e.g. M1-territory, M1-centrality, M2-gap, M2-question, M3-purpose, M3-findings, M3-structure>
- Paragraph functions and transitions: <one line per paragraph: function, and how it hands over to the next>

C. CONTRIBUTION EXPRESSION
- Voice: "we show" | "this paper" | "our model" | mixed
- Claim strength: strong assertion | hedged | conditional
- Number of contributions: 1 | 2-3 | 4+

D. LITERATURE REVIEW
- Structure: standalone section | embedded in intro | woven throughout
- Position in paper: early (after intro) | late (before conclusion)
- Organization: by theme | by method | chronological
- Critical engagement: just-cite | compare-contrast | synthesize

E. METHOD / MODEL
- Entry point: intuition first | formal setup first
- Notation density: heavy | moderate | light
- Exposition style: theorem-proof | proposition-then-proof | walkthrough | pipeline figure
- Assumption justification: explicit | brief | implicit

F. RESULTS
- Primary vehicle: prose | tables | figures | mixed
- Narrative style: result -> mechanism -> implication | result-only
- Paragraph shape: <e.g. claim sentence, then figure sentence, then detail>
- Mechanism emphasis: central | mentioned | absent
- Robustness signaling: main text | appendix | brief

G. DISCUSSION
- Function: mechanism deepening | implications | limitations | future scope
- Scope of claims: stays close to the data | extends broadly
- Implications language: academic | policy-accessible | practitioner-facing
- Limitation acknowledgment: proactive | minimal | absent

H. LANGUAGE STYLE
- Voice: active-dominant | passive-dominant | mixed
- Sentence length: short-direct | long-complex | varied
- Hedging level: low | medium | high
- Transition style: explicit connectives | implicit flow | structural headers
- Mathematical density: heavy | moderate | light | absent

I. WHAT THIS PAPER DOES NOT DO
<3-5 writing patterns notably absent, described structurally, no quotes>

J. DISTINCTIVE PATTERNS
<2-4 rhetorical or structural moves specific to this paper, described as moves, no quotes>
- Sentence templates (3-5): <abstracted with placeholders, e.g. "Although [prior approach] handles [case], it requires [assumption], which fails when [condition]." Never a copied sentence; no topic words left in the template>

K. CLAIMS AND EVIDENCE CONVENTIONS
- Number reporting: <exact values | rounded | ranges; denominators named or not>
- Statistics reported: <tests, effect sizes, intervals, as categories, no values>
- Hedging target: <interpretations only | measured facts too>
- Causal language: <avoided | used with a causal design | used loosely>
- Data and artifact statement: <section, footnote, absent>

L. THREATS AND LIMITATIONS
- Placement: own section | inside discussion | absent
- Framework: <e.g. four validity categories | free-form | per RQ>
- Order of items: <list of categories in the order used>
- Style: operational (what was done about each threat) | generic
```

### Move tags

Introduction moves follow Swales' CARS model (Create a Research Space):
M1 establish a territory (claim centrality, generalize, review prior work),
M2 establish a niche (counter-claim, indicate a gap, raise a question,
continue a tradition), M3 occupy the niche (state purpose, announce
findings, state value, outline structure). Use these tags for field B's
move sequence; add a free tag only when no CARS move fits, and say so.
[src: lit:swales1990genre]

Sources: Swales, J. M. (1990). *Genre Analysis: English in Academic and
Research Settings*. Cambridge University Press.

## 4. Where cards are saved

- With a `research.yaml`: `<style.dynamic_skill>/cards/<paper_id>.md`
  (for example `.style/fse/cards/fse_001.md`).
- Without one: `<corpus_folder>/_style_cards/<paper_id>_style_card.md`, as in
  the original skill.
- From `paper-quickread --style`: next to the quickread note
  (`<reading-dir>/papers/<paper>/style-card.md`); Accumulate copies it into
  the venue corpus when the venue is aggregated.

Cards hold only structural descriptions, so they may be kept in a project
repo. Converted full texts of copyrighted papers stay out of any public repo.

## 5. Readability gate for converted papers

Only fully readable conversions enter extraction:

- major sections are readable;
- section order is intact;
- equations, tables, citations and technical terms are not badly corrupted.

If a file fails, retry the conversion, use another converter, ask the user
for Markdown or text, or replace the paper. Failed and partial conversions
never enter a card, and the conversion summary is reported before Phase 1
continues.
