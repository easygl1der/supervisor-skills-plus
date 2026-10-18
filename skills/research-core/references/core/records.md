# Records outside the paper

The procedure is in `sv-supervisor-records`. Layout of a project's `docs/`:
`STATUS.md` (current state only), `TODO.md`, `adr/`, `log/`, `feedback/`,
`guidance/`, `runs.md`.

## Sources of truth
- Name one writable source of truth for each artifact (paper, data, numbers)
  per phase in `STATUS.md`. Announce and record every switch in an ADR. In
  the evidence project the paper's source of truth changed three times in
  eight days without a record, and the build notes still named the old one.
  [src: note:n08§1.2; note:n04§1.5] (confirmed)
- Dashboards and web UIs are views; the authoritative state is a file you can
  diff (database export, state JSON). [src: note:n08§5#24] (confirmed)

## Sync between editors
- A mirror into a co-edited document must check for edits it would
  overwrite and stop, never copy over. A sync action in the evidence project
  erased a senior co-author's edits twenty minutes before the deadline.
  [src: arc:ol:a610d1d; arc:ol:214cc0c; arc:chat:group@2026-10-03T19:42] (confirmed)
- In the last 24 hours before a deadline: one channel, one editor at a time,
  hand over the pen explicitly. [src: note:n08§5#3] (candidate)
- After any agent write to a shared document, read the diffstat; a large
  deletion means a whole-file overwrite. Checkpoint before destructive agent
  edits. [src: arc:ol:b2ad042; arc:ol:3ae9fd3; note:n08§5#5-6] (confirmed)
- After the deadline, sync the submitted version back into the repository and
  tag it. [src: note:n08§5#40; note:n04§1.2] (candidate)

## What goes where
- Private material (chats, other people's papers, notes) stays out of the
  shared paper repository from day one. [src: arc:msr:f1c7df8; arc:msr:c8adb43] (candidate)
- Copy decisions into the repository; do not keep them only as ticket ids in
  an external tracker. [src: note:n08§5#35] (confirmed)
- Requirement summaries keep an explicit "superseded by" table; the latest
  entry wins. [src: arc:04-comms/past-chat-group/SUMMARY.md] (candidate)
- Meeting transcripts or verbatim notes are the record; tool-generated
  summaries are not. [src: note:n08§5#38] (candidate)
