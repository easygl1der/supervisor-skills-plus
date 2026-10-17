# Weekly report mode

Default audience: advisor. Length: 6 to 10 slides (about 10 to 15 min).
`progress` is the same spine at topic level, 10 to 14 slides, still under
this mode.

## Inputs

- `docs/STATUS.md` and `docs/TODO.md`.
- Latest `docs/log/<date>-group-meeting.md` "Next steps" list.
- `git log` since that meeting date (paper and code repos in `research.yaml`).
- Linear issues if `records.linear.enabled`.
- Missing facts are `TODO`. No invented numbers.

## Spine (advisor)

1. Title (project, date, presenter).
2. Conclusions this week (what changed; lead with the claim).
3. Last week's next steps, each marked done / partial / dropped, with a
   one-line reason for partial or dropped.
4. Results (numbers with table, script, or commit; else `TODO`).
5. Blockers.
6. Decisions needed from the advisor (explicit questions).
7. Next steps (dated, owner, kill criterion when it is an experiment).
8. Optional: one method or figure slide if it is the week's substance.

Technical derivations and extra tables go to `\appendix` (see audience.md).

## Peer variant

Keep the spine, but move one method or derivation slide into the main body
and shorten "decisions needed".

## Last-week load

If no prior group-meeting log exists, say so on slide 3 and skip the marks.
Do not reconstruct next steps from memory.

Partial items carry forward into the new Next steps with their original
date. An item partial three meetings in a row becomes a blocker or a
decision for the advisor. A dropped item is shown once with its reason,
then leaves the list.

## `progress` variant

Replace "this week" with the topic status: what is locked, what is open,
what the next experiment or lemma is. Still conclusion first for advisor.
