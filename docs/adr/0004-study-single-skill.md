# ADR 0004: study is one skill with submodules in references/

Status: accepted; partly superseded by ADR 0021 (the visual kit, visuals.md and visual-scenarios.md moved to sv-figure-explain) (paths updated by ADR 0021 on 2026-10-18)
Date: 2026-10-16
Deciders: owner (SPEC D3, D6), Claude Code (submodule split)

## Context
Learning from a paper and from a textbook chapter share the same loop
(plan concepts, explain, restate, diagnose, redraw, save). The SPEC rejected
separate `study-paper` and `study-book` skills (D3) and made drills optional
switches rather than the core (D6). The full protocol is too long for one
SKILL.md.

## Options considered
1. Several skills (study-paper, study-book, a drill skill): duplicated protocol,
   the user must pick one.
2. One SKILL.md holding everything: too long to load each time.
3. One skill; SKILL.md holds triggers, mode choice and the main loop; detail
   loads on demand from `references/`.

## Decision
Option 3. `skills/sv-study/SKILL.md` detects paper or book mode itself and points
with `See:` lines to `references/protocol.md`, `diagnosis.md`,
`learner-profile.md`, `session-save.md`, `paper-mode.md`, `book-mode.md`,
`options.md` (socratic, feynman, self-test switches), `visuals.md`,
`visual-scenarios.md` and `learning-science.md`.

## Consequences
- One entry point for all learning requests; the router names one skill.
- Submodules must stay consistent with each other (vault order, save rules).

## Do not
- Do not split a mode into its own skill; add a reference file instead.

## Sources
`skills/sv-study/SKILL.md`, `skills/sv-study/references/`.
The 2026-10-16 reading-upgrade SPEC (D3, D6) was a working note and was later
removed; this ADR is the surviving decision.
