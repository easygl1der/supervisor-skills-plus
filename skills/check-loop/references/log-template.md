# Log template: docs/log/YYYY-MM-DD-check-loop.md

Copy the block below into the project as `docs/log/<date>-check-loop.md`
(the `research-core` `log-entry.md` layout with `Kind: check-loop`). Fill it
while the loop runs, not afterwards. The span state file sits next to it as
`<date>-check-loop.spans.json`.

## Contents
1. Template
2. Filling rules

## 1. Template

```markdown
# YYYY-MM-DD check-loop

Kind: check-loop
Participants: <roles; agent>
Scope: <files or sections>
Base commit: <sha> on <branch>        Final commit: <sha>
Budget: max_rounds = <n> (source: user | research.yaml | default)
Mode: apply authorized edits | report only
Profiles: field <name> (<status>), venue <name> (<status>), overlays <list or none>
Inputs missing: <e.g. no dynamic skill; no numbers file> (items depending on them are unknown)

## Locked list
| Kind | Item | Source |
|---|---|---|
| ADR | <what it fixes> | docs/adr/NNNN-... |
| Term | <term> (rejected: <readings>) | term table |
| Span | <file:lines, why> | user / ADR |

## Round table
| Round | Check | Finding id | Location | Finding | Rule source (status) | Edit class | Outcome | Commit | Diff stats |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | CL-r1-c1-01 | sec/results.tex:12 "Type A issues close..." | pooled claim without scope | WR-19 (candidate, opted in) | authorized | applied | abc1234 | 1 file, +1 -1 |
| 1 | 3 | CL-r1-c3-02 | sec/intro.tex:40 "It is worth noting..." | rationed phrase | skill:deai-writing S7 DA-07 (confirmed) | authorized | applied | def5678 | 1 file, +1 -1 |
| 1 | 1R | CL-r1-c1R-01 | sec/results.tex:12 | check-3 edit removed the scope phrase | WR-19 | authorized | reverted by regression | 0a1b2c3 | 1 file, +1 -1 |

## Guard flags
| Round | span_guard output | Decision and reason |
|---|---|---|

## Per-round summary
| Round | Check 1 | Check 2 | Check 3 | Regression 1R | Edits applied | Residuals |
|---|---|---|---|---|---|---|
| 1 | <pass/fail counts> | | | | <n> | <n> |

## Stop reason
all pass | no-change round | oscillation (<finding ids>) | budget reached

## What changed
<three to eight lines: the substance of the changes, grouped by check, with
counts; page count before and after if compiled>

## Residual findings
| Finding id | Location | Rule | Edit class | Why not applied | Owner / TODO id |
|---|---|---|---|---|---|

## Checklist report
| Item | Result (pass / fail / n/a / unknown) | Evidence |
|---|---|---|

## Follow-ups
- TODO items created (with CL ids), ADRs proposed (rule conflicts, locked
  decisions questioned), hand-offs.
```

## 2. Filling rules

- One row per finding, applied or not. A finding the loop did not apply
  still gets a row with its outcome.
- Rule source is the checklist id, the profile rule's `[src:]`, the ADR
  number, or the `deai-writing` finding id with its syndrome. A row with no
  rule source is not allowed.
- Diff stats come from `git diff --stat` on the commit, not from memory.
- Paste the `span_guard.py report` table under the round table at the end;
  it must agree with the round table.
- "What changed" is derived from the commits, not from the plan.
