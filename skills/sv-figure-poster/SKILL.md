---
name: sv-figure-poster
description: >-
  Plans and checks a research poster with the library's figure rules: one
  message per panel, figures reused from the paper under the universal
  design rules, a tool chosen from the tool matrix, and the archive figure
  rules audit. States plainly that no poster-specific rules exist yet. Use
  when the user asks to make, lay out or review a conference or group
  poster.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-figure-poster

A scaffold (ADR 0021): this library has no poster-specific rules or
evidence yet. Apply only what already exists, and say so to the user:

- universal rules: `design-rules.md`;
- tool choice: `tools.md` (PowerPoint, Keynote, Figma, TikZ);
- archive rules audit: `archive-figure-rules.md`;
- each panel's figure designed with `sv-figure-design`.

See: ../sv-figure/references/design-rules.md
See: ../sv-figure/references/tools.md
See: ../sv-figure/references/archive-figure-rules.md

Poster lessons from real use go to `sv-supervisor-harvest`, which can turn
them into rules with sources.
