---
name: sv-write-style-mine
description: >-
  Mines writing style from exemplar papers: dissects one paper into a Style
  Card, accumulates cards into venue, field or author profiles under a
  consensus threshold, finds exemplars by journal or author through public
  APIs, and borrows analysis methods as method cards. Describes moves, never
  content, and changes research-core only through review. Use when building
  a venue, field or author profile, or receiving a quickread style card.
license: MIT
disable-model-invocation: true
argument-hint: "e.g. 'dissect this exemplar', 'build a venue profile from these 6 accepted papers', 'list this journal's new papers'"
---

# sv-write-style-mine

Formerly the dissect and accumulate loops of `style-mine` (originally the
owner's MIT skill `journal-adapt`; credit in `README.md`). The full
procedure, unchanged, is `references/procedure.md`; the six hard rules are
in `references/hard-rules.md`. Load both and follow the procedure's Step 0
and input check (MinerU only).

## Load by mode

| Mode | Trigger | Load |
|---|---|---|
| Card | "dissect this paper's style", a card from `paper-quickread --style` | `style-card.md` |
| Build | "learn the style of this venue" | `style-card.md`, `style-profile.md`, `base_rules/<file>` the user picks |
| Profile | "make a venue profile", `sv-supervisor-harvest --new-field` | `profile-output.md` (after Build and the human gate) |
| Intake | "list this journal's new papers", "find this author's papers" | `intake.md`, `scripts/intake_search.py` |
| Author profile | "build a profile of this author's style" | `author-profile.md` |
| Method card | "borrow methods from related work" | `method-card.md` |

Build runs before Profile, and before `sv-write-style-apply`, when no
dynamic skill exists for the destination. Nothing goes past the human gate
without the user's "confirmed".

See: references/procedure.md
See: references/hard-rules.md
See: references/style-card.md
See: references/style-profile.md
See: references/profile-output.md
See: references/intake.md
See: references/author-profile.md
See: references/method-card.md

## Hand-offs

- Apply a profile to a manuscript, or check venue fit: `sv-write-style-apply`.
- Profile changes into research-core: `sv-supervisor-harvest`.
- Implementing a borrowed method: `experiment-workflow`; recording the
  design change: `sv-supervisor-records`.
