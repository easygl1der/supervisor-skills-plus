---
name: sv-supervisor-harvest
description: >-
  Turns a project's feedback tables, guidance records, decision records,
  review-loop logs, STATUS and git history, plus expert notes, into sourced
  and deduplicated rule candidates for research-core, classifies where each
  belongs, and proposes the change on a learn branch for the owner to
  approve. Also starts a new field profile. Use when a milestone is reached,
  after a submission, or when a new field needs a profile.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-supervisor-harvest

Formerly `lessons-harvest`. The full procedure, unchanged, is
`references/procedure.md` (inputs, steps 1 to 9, `--new-field`); the
detailed harvest steps are in `references/harvest-procedure.md`. Load both
and follow the procedure's Step 0.

Candidate finder, from the repository root:
`python skills/sv-supervisor-harvest/scripts/find_rule_candidates.py <project_dir>`

See: references/procedure.md
See: references/harvest-procedure.md

## Rules that never bend

- Never merge on its own: show the diff and wait for the owner.
- Never write names or project details into the library.
- Never state a rule without a source.

## Hand-offs

- Venue or field profiles from exemplar papers: `sv-write-style-mine`.
