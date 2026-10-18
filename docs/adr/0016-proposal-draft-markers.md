# ADR 0016: proposal-writer keeps visible gap markers in Draft mode

Status: accepted (paths updated by ADR 0021 on 2026-10-18)
Date: 2026-10-16
Deciders: owner, Claude Code (marker wording)

## Context
`paper-writer` delivers clean prose with zero bracketed placeholder tags.
Proposals are written earlier, before the literature work is finished, so
many citations and facts are still open when the first draft is needed.
Hiding those gaps, or filling them from memory, risks invented citations.

## Options considered
1. Apply the paper-writer zero-placeholder rule: forces guessing or silent gaps.
2. Keep gaps in a separate list: easy to lose track of which sentence needs what.
3. Keep visible inline markers in Draft mode; require none in Final mode.

## Decision
Option 3. In Draft mode an unresolved citation stays as `[cite needed: <what it
must support>]` and an unresolved fact as `[to verify: <question>]`; Chinese
equivalents (for example `[待查]`) are allowed in Chinese drafts. Content the
skill adds beyond the user's material is marked as an addition. In Final mode
no marker remains: each is resolved by retrieval, by the user, or by deleting
the sentence (check PW-11).

## Consequences
- Every gap is visible to the user in the draft.
- This is a deliberate exception to `paper-writer`'s rule; the two skills differ
  on purpose.

## Do not
- Do not deliver Final mode with any marker left.
- Do not resolve a marker with a citation that was not retrieved.

## Sources
`skills/sv-proposal/SKILL.md` (Phase 5 "Draft markers", PW-11),
`skills/paper-writer/SKILL.md` (zero placeholder tags rule).
