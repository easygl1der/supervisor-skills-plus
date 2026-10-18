# Sources of truth and syncs

## Contents
1. One writable source per artifact
2. Git and a co-edited copy (Overleaf)
3. Agents writing to shared documents
4. The last 24 hours
5. After the deadline
6. Data and dashboards

## 1. One writable source per artifact

| Artifact | Typical source of truth | Recorded in |
|---|---|---|
| Paper text | git `main` or the co-edited copy, never both at once | STATUS, ADR |
| Data | research repo plus data host with manifest | STATUS, `data/MANIFEST.tsv` |
| Numbers | the numbers file produced by scripts | STATUS "Verified numbers" |
| Decisions | `docs/adr/` | ADR index |

In the evidence project the paper's writable source flipped three times in
eight days (co-edited copy, then git, then the co-edited copy again in the
last hours), and the build notes still named the old one. Record every
switch. [src: note:n08§1.2; note:n04§1.5] (confirmed)

## 2. Git and a co-edited copy (Overleaf)

- Pushing to git does not update the co-edited copy; someone must pull there
  and check. [src: arc:chat:group@2026-10-03T19:39] (candidate)
- Automated mirrors must fast-forward or stop. Run
  `scripts/sync_guard.py <repo> <remote> <branch>` before every push to the
  co-edited copy, and configure any CI sync action the same way. A copy-over
  sync action erased a senior co-author's edits, including a new title, ten
  seconds after they were saved and about twenty minutes before the
  deadline. [src: arc:ol:a610d1d; arc:ol:214cc0c; arc:chat:group@2026-10-03T19:42] (confirmed)
- Keep non-manuscript files out of the co-edited copy (sync filters).
  [src: arc:msr:c93ef1f] (candidate)
- Merge storms (many "updates from" merges in a few hours) mean two writable
  sources are active. Stop and pick one. [src: note:n04§1.4] (candidate)

## 3. Agents writing to shared documents

- Read the diffstat after every agent write. Two agent edits through an
  editor integration deleted most of the main file (hundreds of lines), and
  were restored within minutes only because someone looked.
  [src: arc:ol:b2ad042; arc:ol:3ae9fd3] (confirmed)
- Checkpoint commit before destructive agent edits, in its own commit.
  [src: note:n08§5#6] (candidate)

## 4. The last 24 hours

- One channel and one editor at a time; hand over the pen in the channel
  ("you edit now", "done, your turn"). [src: note:n08§5#3] (confirmed)
- Upload a complete PDF early and replace it later; the submission site went
  down at the deadline. [src: arc:chat:group@2026-10-03T19:45; note:n04§1.1] (confirmed)

## 5. After the deadline

Bring the submitted version back into git, tag it
`submitted-<venue>-<date>`, and record the uploaded PDF's hash. The evidence
project's repository ended before the submitted version, and the archive has
no copy or hash of the uploaded PDF. [src: note:n04§1.2; note:n08§5#40] (confirmed)

## 6. Data and dashboards

A web dashboard showed far fewer completed annotations than the local
database held, because it had not imported the latest state. The
authoritative state is the file you can diff (database export, state JSON);
dashboards are views. [src: note:n08§5#24] (confirmed)
