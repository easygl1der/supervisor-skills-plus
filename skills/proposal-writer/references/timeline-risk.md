# Timeline, milestones and risk register

## Contents

1. Milestones that can fail
2. Milestone table
3. Gantt view
4. Risk register
5. Preliminary data as feasibility evidence
6. Figures

## 1. Milestones that can fail

A milestone is a checkable state of the world at a date, not an activity.
"Literature review in months 1 to 3" is an activity; "frozen panel of N
repositories with adoption dates, release tag v0.1, month 4" is a
milestone. Each milestone states the criterion that would count as
failure, so the plan contains its own mid-term exams.
[src: guide:https://www.darpa.mil/about/heilmeier-catechism@2026-10-16] (confirmed)

Rules:

- Every aim has at least one milestone in its first third.
- At least one go or no-go point exists, with the decision written in
  advance: what happens if the criterion fails (switch to the fallback,
  narrow the scope, drop the aim).
- Pre-set thresholds are written before the data are seen, as for any
  pre-registered bar in research-core `integrity.md`. A threshold not yet
  fixed is written as a named symbol with who fixes it and when ("bias at
  most T1, fixed in an ADR before the simulation runs"), never as a vague
  adjective such as "no obvious bias" or "comparable".
- Institutional milestones (mid-term review, pre-defense, report dates)
  are rows in the table, so slack before them is visible.
- Keep slack: the last block before a hard deadline holds only writing
  and buffer. The size of the buffer is a judgment; state it.

## 2. Milestone table

| ID | Aim | Milestone (deliverable) | Success criterion (can fail) | Month | Depends on | If it fails |
|---|---|---|---|---|---|---|
| M1.1 | A1 | ... | ... | ... | none | ... |
| M2.1 | A2 | ... | ... | ... | M1.1 or fallback F2 | ... |
| G1 | all | go or no-go review | ... | ... | M1.1, M2.1 | ... |

"Depends on" must never name another aim's milestone without an
alternative; that is the cascade test from the spine.

## 3. Gantt view

A Markdown Gantt is enough for most templates:

| Work package | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 |
|---|---|---|---|---|---|---|---|---|
| A1 data | X | X | M1.1 | | | | | |
| A2 method | | X | X | X | M2.1 | | | |
| A3 evaluation | | | | X | X | X | M3.1 | |
| Writing and buffer | | | | | | X | X | X |

Months or quarters follow the call's reporting cycle (annual for NSFC,
semester for a thesis).

## 4. Risk register

| ID | Risk | Aim | Likelihood | Impact | Early signal | Mitigation now | Fallback if it happens | Decide by |
|---|---|---|---|---|---|---|---|---|
| R1 | ... | A1 | medium | high | ... | ... | ... | M1.1 |

Rules:

- Name risks specific to this project: data access, identifying
  assumptions that may fail, compute, a dependency on another group,
  recruitment, the applicant's own skill gaps. "Experiments may not work"
  is not a risk statement.
- For a causal design, the identifying assumption that is least testable
  is always a row, with the diagnostic that will be run and the
  alternative design if it fails.
- A fallback still produces a deliverable (a narrower question, a
  descriptive result, a negative result written up).
- High-impact risks without a fallback are reported to the user as open
  problems, not hidden.

## 5. Preliminary data as feasibility evidence

Reviewers trust shown feasibility over claimed feasibility. In order of
strength: a pilot result on the real data with its numbers and source; a
working prototype or released code; secured access (data agreement, API
quota, collaborator letter); prior publications using the same method;
a stated skill.

- Report preliminary results in past tense with scope and source (script,
  output, date), exactly like a paper result.
- When no preliminary data exists, say so and make producing it the first
  milestone of the plan. A one-week pilot that answers the riskiest
  assumption is often worth more than a page of argument; plan it with
  `experiment-workflow`.

## 6. Figures

Gantt charts, technical roadmaps (the flow from data to method to
evaluation, expected in kaiti reports and NSFC applications) and aims
diagrams can be drawn with the study kit (HTML rendered to PNG); the
pattern catalog in the study skill's visual-scenarios reference lists P7
(timeline) and P2 (pipeline) for these. Every date on a figure comes from
the milestone table.
