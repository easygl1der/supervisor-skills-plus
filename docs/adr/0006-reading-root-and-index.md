# ADR 0006: Reading root resolution and an append-only index.json

Status: accepted
Date: 2026-10-16
Deciders: owner (SPEC "index.json append only"), Claude Code (resolution order, seq/supersedes)

## Context
Quickread cards are read later by `study`, `deep-research` and
`research-bridge`, so they need a predictable location and an index. Cards are
redone (a second read, a study session), and rewriting the index would lose
history and make git diffs noisy.

## Options considered
1. Always `./reading/`: cards scatter across working directories.
2. Edit index entries in place: simple, but history is lost.
3. A resolution order for the root; an index where records are only appended.

## Decision
Option 3. `skills/paper-quickread/SKILL.md` resolves the reading root:
`research.yaml` `reading.dir`; else `<project>/reading/` in a research
project; else the study vault in the same order as `study` (ADR 0005:
`$STUDY_VAULT`, `~/.config/study/vault`, `~/study-vault`); else `./reading/`,
and says which was used. `deep-research` literature-map mode uses the same order.
`scripts/index_append.py` appends to `<root>/index.json`: required fields
id, kind, title, path, date; each record gets `seq`, and `supersedes` points to
the previous record with the same id and kind. A guard checks that the old
prefix is byte-identical after the write.

## Consequences
- Readers take the latest record per id.
- The index only grows; compaction would need its own decision.
- One vault lookup for all reading skills, so cards and study notes land in
  the same root.
- Records carry `seq` and `supersedes`; `kind` is paper, book, concept or map.

## Do not
- Do not modify or delete existing index records.

## Sources
`skills/paper-quickread/SKILL.md` (reading root, index step),
`skills/paper-quickread/scripts/index_append.py`,
`skills/study/evals/reading/index.json` (two records, seq 1 and 2, supersedes 1).
