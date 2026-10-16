# Check mode (check-loop round 2)

## Contents
1. Contract
2. Inputs
3. What is checked
4. Finding format
5. Report format
6. Standalone use

## 1. Contract

Check mode is **report-only**. It reads text and reports where the text
deviates from the dynamic writing skill and the venue profile. It never
edits files, never proposes replacement wording that adds facts, and never
touches P1 content. `check-loop` decides which findings become edits and
applies them through its own authorized-edit step. [src: up:DESIGN.md]

It runs as the second check of each check-loop round: research fit first,
then venue and field style fit (this mode), then language and de-AI.

## 2. Inputs

- Target files or sections (paths, or section labels inside a LaTeX tree).
- `dynamic_writing_skill.md` (from `research.yaml` `style.dynamic_skill`).
  If it does not exist, say so and fall back to the venue profile's "Style
  from exemplars" and the field profile; report reduced coverage.
- `research-core/references/venues/<venue>.md` and the field profile.
- Locked decisions: `docs/adr/` and the project's term table. A finding that
  would flip a locked decision is reported as `locked`, not as a deviation.
- From check-loop: the round number and the spans changed in the previous
  round (to support its oscillation guard).

## 3. What is checked

Per section, in this order:

1. **Structure**: section order and presence (for example, related work
   position, a threats section), paragraph functions, roadmap.
2. **Lengths**: section and abstract lengths against measured ranges and the
   venue page budget (counted on the PDF when available).
3. **Contribution format**: list vs RQ-carried vs prose, as decided for this
   venue.
4. **Results paragraph shape**: order of claim, figure pointer and detail.
5. **Tone**: voice, hedging level, sentence length, transitions, number
   density, against the language register.
6. **Citation form**: as the venue profile states it.
7. **P5 phrases** from the dynamic skill (only those; the full de-AI audit is
   round 3 and belongs to `deai-writing`).

Rules below the consensus threshold (Cautions and conflicts) are reported at
severity LOW and marked `advisory`.

## 4. Finding format

```
| ID | Location | Rule | Observed | Expected | Severity | Status |
|---|---|---|---|---|---|---|
| JA-r2-01 | sec:intro, para 3 | DS-04 (5/6) | contributions itemized as 4 bullets | carried by numbered RQs | MED | open |
```

- `ID`: `JA-r<round>-<nn>`; stable within the round.
- `Location`: file and line, or section label and paragraph number.
- `Rule`: a `DS-nn` id with its support, or a venue or field rule (file and
  heading, with its `[src: ...]`), or a checklist ID.
- `Observed` and `Expected`: structural descriptions. Short quotes from the
  manuscript are allowed to locate the span; quotes from corpus papers are
  not.
- `Severity`: HIGH (blocks venue fit, e.g. over the page budget or a missing
  required section), MED (weakens fit), LOW (minor or advisory).
- `Status`: `open`, `locked` (conflicts with an ADR), `advisory` (below
  threshold), `repeat` (reported in an earlier round for the same span).

## 5. Report format

```
# style-mine check: <target> (round <r>, <date>)
Dynamic skill: <path, date>   Venue profile: <file, version>   Field: <code, status>
Coverage: full | reduced (<reason>)

## Section scores
| Section | Venue match before (1-5) | Findings HIGH / MED / LOW |

## Findings
<table from section 4>

## Not checked
<what was out of scope or had no rule>
```

Return the report to `check-loop`, which records it in its round log.

## 6. Standalone use

Run outside check-loop when the user asks "does this section fit the
venue?". Write the report to `docs/log/<date>-style-mine-check.md` (use
the research-core `log-entry.md` header) and make no edits. To act on the
findings, use Phase 2 of this skill (one section at a time, with a revision
log) or `check-loop`.
