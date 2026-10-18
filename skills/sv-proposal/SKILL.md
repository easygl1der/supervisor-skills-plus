---
name: sv-proposal
description: >-
  Entry point for research proposals: thesis proposals (kaiti reports),
  grant applications such as NSFC, NSF, ERC and NIH, and research
  statements or PhD research plans. Builds the proposal spine, evidence
  ledger, timeline and risks before drafting, then runs a reviewer pass.
  Routes to one sv-proposal sub-command and says which. Use when the user
  needs a proposal, research plan, grant or research statement.
license: CC-BY-NC-SA-4.0
---

# sv-proposal

Router of the proposal group (ADR 0021). The full workflow, unchanged from
the former `proposal-writer`, is `references/procedure.md` (Step 0,
Phases 1 to 7, checklist); real outputs are in `evals/`.

| The user says | Sub-command |
|---|---|
| kaiti report, thesis proposal, opening report | `sv-proposal-kaiti` |
| NSFC, NSF, ERC, NIH, grant, specific aims | `sv-proposal-grant` |
| research statement, PhD research proposal, fellowship plan | `sv-proposal-statement` |

Say which one was chosen in one line. Sub-commands can also be called
directly; they are not auto-selected.

See: references/procedure.md
See: references/genres.md

## Hand-offs outside this group

- Whether the idea is worth it: `sv-idea`.
- De-AI on the proposal text: `sv-write-humanize-letter`.
