# ADR 0005: Learner profile in a separate study-vault repo, found by a fixed order

Status: accepted
Date: 2026-10-16
Deciders: owner (SPEC D13), Claude Code (resolution order, push behaviour)

## Context
Study keeps personal records: knowledge levels, misconceptions, sessions,
concept notes. Kept inside the skill or `research-core`, a skill upgrade could
overwrite them and they would not follow the learner across machines and
tools (SPEC D13).

## Options considered
1. Store the profile in the skill folder: lost on upgrade, public with the repo.
2. Store it in each project: split across projects.
3. A private git repo `study-vault`, found by a fixed lookup order.

## Decision
Option 3. `skills/study/scripts/vault.py` resolves the vault in this order:
`$STUDY_VAULT`; the path in `~/.config/study/vault`; `~/study-vault`; else
`./reading` with a warning on stderr. `vault.py init` creates the layout;
`vault.py where --set` records the path. `vault.py save` stages, commits, and
when a remote exists pushes with `push -u <first remote> HEAD`; if the push
fails the commit stays local and the retry command is printed.

## Consequences
- Records survive skill upgrades and are shared across Claude Code, Cursor and Codex.
- Without a configured vault, notes land in `./reading` and are not shared.
- `paper-quickread` and the literature map use the same order after their
  project-local roots (ADR 0006).

## Do not
- Do not write learner records into this repository.
- Do not discard a commit because a push failed.

## Sources
`skills/study/scripts/vault.py` (docstring, `where`, `save`),
`skills/study/references/learner-profile.md`, `skills/study/references/session-save.md` §4,
SPEC D13.
