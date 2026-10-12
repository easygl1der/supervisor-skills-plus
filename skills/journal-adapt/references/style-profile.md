# Style Profile and dynamic writing skill

## Contents
1. Style Profile (aggregate of all cards)
2. Dynamic writing skill format
3. Priority stack P1 to P5
4. Where the files go

Both formats come from the original journal-adapt skill. Additions: each
pattern row carries its support count (`k/n`), every row names the paper IDs
that show it, and the dynamic skill marks which rules passed the consensus
threshold (see the profile-output reference for the threshold).

## 1. Style Profile (aggregate of all cards)

Read all Paper Style Cards and count, for each pattern, how many primary
cards show it.

```
## Style Profile: <WRITING DESTINATION>
Generated: <date> from <n> primary, <m> secondary, <e> exemplar cards.
Consensus threshold: k = <k> of n = <n> primary cards.

### Editorial identity
- Research question type: <describe>
- Methods valued: <describe>
- Implied reader: academic specialist | policy-informed | practitioner | mixed

### Introduction conventions
| Observed pattern | Support (k/n) | Corpus role | Paper IDs |
|---|---|---|---|
| <pattern> | 5/6 | primary | fse_001, fse_002, ... |

Most common intro sequence: <moves>
What intros here do not do: <3-5 absent patterns>

### Contribution expression
| Observed pattern | Support (k/n) | Corpus role | Paper IDs |
|---|---|---|---|

### Literature review
| Observed pattern | Support (k/n) | Corpus role | Paper IDs |
|---|---|---|---|

### Method / model norms
| Observed pattern | Support (k/n) | Corpus role | Paper IDs |
|---|---|---|---|

### Results and discussion norms
| Observed pattern | Support (k/n) | Corpus role | Paper IDs |
|---|---|---|---|

### Claims, evidence and threats (fields K and L)
| Observed pattern | Support (k/n) | Corpus role | Paper IDs |
|---|---|---|---|

### Language style
| Dimension | Observed norm | Support (k/n) |
|---|---|---|
| Voice | | |
| Sentence length | | |
| Hedging level | | |
| Mathematical density | | |
| Transition style | | |

### Split axes (cards disagree)
| Axis | Pattern A (paper IDs) | Pattern B (paper IDs) | Likely driver (venue, length, paper type) |
|---|---|---|---|

### Conflict table: corpus signals vs static base rules and research-core
| Dimension | Static base (P4) | Field profile | Target venue pattern (P2) | Secondary or exemplar (P3) | Resolution |
|---|---|---|---|---|---|
| Voice | | | | | |
| Contribution format | | | | | |
| Hedging | | | | | |
| Literature placement | | | | | |
| Discussion scope | | | | | |

### Red flags
<5-8 patterns absent from the primary corpus or contradicted by strong corpus evidence>
```

Save as `style_profile.md` next to the cards.

## 2. Dynamic writing skill format

```
# Dynamic Writing Skill: <WRITING DESTINATION>
Generated: <DATE>
Primary corpus cards: <n>   Secondary: <m>   Exemplars: <e>
Static base: <file or none>   Field profile: <field> (<status>)
Venue profile: <venue file or none>
Consensus threshold: <k> of <n>

## PRIORITY RULES (non-negotiable)

### P1 HARD PRESERVE
Never modify:
- \cite{} commands and citation keys
- LaTeX math environments, variable names and notation
- numerical results and quantitative claims
- footnote content
- figure and table references (\ref{}, \label{})
- model names, dataset names, proper nouns
- decisions recorded in the project's docs/adr/ and the term table

### P2 TARGET VENUE PATTERNS
One rule per line, each with its support and paper IDs:
- DS-01 <actionable rule> (5/6: fse_001, fse_002, fse_003, fse_005, fse_006)

### P3 SECONDARY CORPUS AND EXEMPLARS
Apply when P2 is silent or weak on a dimension.
- DS-20 <rule> (<support>: <paper IDs>)

### P4 STATIC BASE AND FIELD PROFILE DEFAULTS
Apply when P2 and P3 have no guidance. Rules from the research-core field
profile keep their [src: ...] tags.

### P5 ALWAYS REMOVE
- "This paper explores..." / "In this study, we aim to..."
- "It is worth noting that..." / "It should be noted that..."
- "Furthermore," / "Moreover," / "Additionally," as empty transitions
- "contributes to the growing literature on..."
- "Future research should explore..."
- "Taken together, these findings suggest..."
- "Our results highlight the importance of..."
(The full banned-word list is owned by deai-writing; do not duplicate it here.)

## SECTION-SPECIFIC GUIDANCE
### Abstract / Introduction / Related work / Methods / Results / Discussion / Threats / Conclusion
<structure, lengths, moves>  Do not: <anti-patterns>

## CAUTIONS AND CONFLICTS
<patterns below threshold, split axes and how each was decided; apply only
after human review>

## LANGUAGE REGISTER
- Voice, sentence length, hedging, transitions, mathematical prose
```

Rule IDs `DS-nn` are local to this dynamic skill; they are what check mode
and the revision log cite. They are not research-core checklist IDs.

## 3. Priority stack P1 to P5

| Level | Source | Wins over |
|---|---|---|
| P1 | The manuscript's own technical content and the project's ADRs | everything |
| P2 | Target venue corpus (rules at or above the threshold) | P3, P4 |
| P3 | Secondary corpus and lab or advisor exemplars | P4 |
| P4 | Static base rules (`base_rules/`) and research-core field profile | nothing below P3 |
| P5 | Always-remove list | applies regardless |

The research-core precedence file still applies above this stack: the
official venue call beats any corpus pattern, and a recorded ADR beats the
venue profile. A corpus pattern never overrides a core rule on claims and
evidence (for example, if exemplars state findings without hedging, the core
hedging rule still holds for the manuscript).

The original skill's base-rule files said "P3 defaults" while the skill
loaded them as P4. This version loads them as P4 everywhere.

## 4. Where the files go

| File | With research.yaml | Without |
|---|---|---|
| Style profile | `<style.dynamic_skill>/style_profile.md` | `<corpus>/_style_cards/journal_style_card.md` |
| Dynamic skill | `<style.dynamic_skill>/dynamic_writing_skill.md` | `<manuscript_folder>/dynamic_writing_skill.md` |
