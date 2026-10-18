# Decision records (ADR)

## When to write one

- A choice between at least two real options is about to be locked:
  sampling design, freeze date, codebook version, reporting rule, figure
  design, where the paper is edited, what goes to threats.
- A co-author or advisor settles a disagreement.
- Someone asks "why did we do X?" and the answer is not written anywhere.

Not for: variable names, following an existing convention, obvious fixes,
open explorations (those stay in `docs/notes/`). [src: skill:architecture-decision-records] (confirmed)

## Format

Template: `research-core` `assets/templates/adr-0000-template.md`.
File: `docs/adr/NNNN-<slug>.md`, index row in `docs/adr/README.md`:

```
| ADR | Title | Status | Date | Supersedes | Linear |
```

Required parts: context with evidence links, two or more options with pros
and cons, the decision with "because", consequences, and a "do not" list.
The "do not" list matters: the best-preserved decision in the evidence
project listed the approaches not to pursue (guessing fix labels, another
round of crawling, a separate prompt). [src: arc:@threats-pivot] (candidate)

## Lifecycle

`proposed -> accepted -> superseded by NNNN | deprecated`

- Confirm before writing: show the draft, write after approval.
- Never edit an accepted decision; supersede it.
- When an ADR changes what is true, rewrite the living docs the same day.
- Decisions taken in chat or meetings get an ADR within a day, linked to the
  guidance record. A decision that exists only as a tracker id or a chat
  message is lost when the tracker or the export is gone. [src: note:n08§5#33; note:n08§5#35] (confirmed)

## Typical research ADRs

- Sources of truth for paper, data and numbers (ADR 0001).
- Corpus freeze: date, population, selection criteria.
- Evaluation reference frozen; acceptance bar set before the run.
- Reporting rule for agreement values.
- Term table locked; rejected readings.
- Threats pivot: a data gap moved to threats, with its mechanism.
- Paper editing location for the final days, and the hand-over order.
