# Guidance mode

## Contents
1. Why guidance records
2. Writing a record
3. Interpreting what the expert means
4. Actions and follow-up
5. Example (anonymized)

## 1. Why guidance records

Advice from an advisor, a senior co-author or a reviewer in a meeting is the
most valuable and the most easily lost feedback. The owner asked to be able
to record it locally, understand what was meant and in what scenario, know
what to watch and by when, and check later whether it was done.
[src: user:2026-10-13]

In the evidence project, early meetings were barely archived, and a relayed
advisor reading targeted an outdated version. The one decision that was
written down well (a data-coverage gap moved into threats to validity, with
mechanism, who decided, and a list of approaches not to pursue) is the one
everyone could later cite. [src: arc:GAPS.md; note:n05§5.1; arc:@threats-pivot] (confirmed)

## 2. Writing a record

Template: `research-core` `assets/templates/guidance-record.md`.
File: `docs/guidance/YYYY-MM-DD-<role>-<topic>.md`. Roles, never names, in
any file that may be shared; the raw transcript can stay in a private folder
and be linked.

Order of filling:

1. Scenario: what was shown (commit, PDF version, figure, run id) and the
   question asked. Without this, the advice cannot be re-read correctly later.
2. Verbatim quotes with times, in the original language, short.
3. Interpretation, separate from the quotes.
4. Points to notice.
5. Actions.
6. Decision.

Record it the same day. If it was a call, write the quotes from the recording
or from notes taken live, and mark paraphrases as such.

## 3. Interpreting what the expert means

For each point write:

- **Literal request**: what they asked for.
- **Underlying concern**: the reader or reviewer problem behind it (for
  example "the method figure and text are not synced" means a reviewer cannot
  map each step to a box).
- **Scope**: this paragraph, this paper, or every paper (a candidate rule for
  `sv-supervisor-harvest`).
- **Confidence**: high when they said it explicitly, low when inferred.
- **To clarify**: what to ask them next time.

## 4. Actions and follow-up

- Action ids `G-<YYYYMMDD>-<n>`; each with owner, due date or milestone, and
  a done-criterion someone else could check ("each workflow box has a
  same-named method step, verified by count").
- Link actions to `TODO.md`, to FB IDs when they touch the manuscript, and to
  run ids when they touch experiments.
- `scripts/guidance_review.py <project_dir>` lists open and overdue actions
  and done actions without evidence. `sv-supervisor` runs it at the
  start of a session.
- Close an action only with evidence: a commit, a run id, a file, or the
  expert's confirmation (record when and how).
- When the expert repeats a point, reopen the earlier action.

## 5. Example (anonymized)

```
# Guidance 2026-09-10 senior-b and senior-a: data coverage gap

Channel: group chat (screenshots archived)

Scenario: the student reported that more than 16% of closed issues have no
linked pull request or commit (likely repository migration), that matching
commits by closing time also failed, and asked how to proceed (22:19).

What they said
- [22:37] senior-b: "只能放到 threat of validity 里面吧" / "继续搞其他的 rq 验证吧" / "rq2 之类的"
- [23:55] senior-a: agrees with threats; mechanism: branch deleted or not
  pushed, commits squashed
- [00:24] senior-a: it depends on the purpose of the label (paraphrase):
  for the problem only, label these unknown; for problem and fix, set them
  aside and state in the approach that they are out of scope

What they mean
- The gap is a validity threat, not a method defect that more crawling will
  fix; stop chasing it. (high)
- The main line moves to an RQ that does not need the fix link. (high)
- The unknown-versus-out-of-scope choice is made per RQ by the purpose of the
  label, not globally. (medium; interpretation recorded in the notes)

Points to notice
- Do not guess fix labels to make the coding look complete.

Actions (illustrative ids)
| G-20260910-1 | Describe the gap and its mechanism in threats | student | full draft | threats paragraph names the mechanism | |
| G-20260910-2 | Re-scope the fix-related RQ to the covered subset; state scope in the approach | student | next meeting | approach text and analysis script updated | |

Decision: accept (recorded in an ADR in a real project).
```

Source of the example: the threats-pivot notes in the evidence archive,
rewritten with roles; quotes and times are from the archived screenshots' transcription, action rows are illustrative. [src: arc:@threats-pivot] (confirmed)
