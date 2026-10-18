# ADR 0012: Evals are kept as real outputs, not a JSON test harness

Status: accepted (paths updated by ADR 0021 on 2026-10-18)
Date: 2026-10-16
Deciders: owner (SPEC test plan), Claude Code (eval set)

## Context
The reading and learning skills produce cards, notes, figures and vault
updates whose quality is judged by reading them: sourced numbers, honest
labels, figure legibility, append-only index. A JSON harness of prompts and
expected strings would test wording, not quality.

## Options considered
1. JSON eval harness with assertions on model output: brittle for prose.
2. No stored evals: nothing to compare after edits.
3. Store complete real runs in the repo and check them with the skill scripts.

## Decision
Option 3. `skills/sv-study/evals/` holds: `reading/` (SDID paper: quickread,
method, insights, reflection, style card, figures; `index.json`; `lit-map/`),
`study-vault/` (a sample vault: profile, concepts, sessions, and chapter 4 of
a probabilistic ML textbook, PML1), `demo/` (an array-partition stepper with
step PNGs), `bridge/project-ci/` (a sample project with `research.yaml`) and
`proposal/` (a proposal draft and its review). Deterministic parts are checked
by scripts with `--selftest` (`check_quickread.py`, `index_append.py`,
`vault.py`) and by `render.mjs` exit codes.

## Consequences
- Evals double as worked examples referenced from the skills.
- Reviews compare new runs against these files by reading.
- Quoted textbook material is limited by its licence (PML1 is CC BY-NC-ND;
  notes keep formulas and numbering only).

## Do not
- Do not store invented or hand-edited "expected" outputs as evals.

## Sources
`skills/sv-study/evals/` tree, `CHANGELOG.md` (eval runs line),
`skills/sv-study/evals/study-vault/books/murphy-pml1/ch04-statistics/notes.md` (licence line).
