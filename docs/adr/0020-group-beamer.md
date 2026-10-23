# ADR 0020: group-beamer themes, overlays, and records

Status: accepted (paths updated by ADR 0021 on 2026-10-18)
Date: 2026-10-17
Deciders: owner (2026-10-17; proposal note later removed, decision is this ADR)

## Context
The library had no Beamer skill for group meetings. Step 2 proposed
`skills/sv-slides/` with Moloch, SimplePlus, a SYSU option, overlay
policy, and research-records accumulation. TeX is already on this Mac
(TeX Live 2026: latexmk, moloch, beamertheme-simpleplus, ctex; poppler
`pdftoppm`). The repository licence is CC-BY-NC-SA-4.0; Moloch is
CC-BY-SA-4.0; SimplePlus is Unlicense; yxnchen/sysu-beamer-template is
not cleanly CC0.

## Options considered
1. TeX: BasicTeX plus `tlmgr` of named packages, versus full MacTeX.
2. Moloch: depend on the installed package versus vendor unmodified `.sty`.
3. SYSU: own look-alike from green RGB facts versus vendor yxnchen files
   versus drop the theme.
4. Overlays: ban and duplicate frames versus allow `\pause`.

## Decision
1. Use the TeX already installed; if a package is missing, `tlmgr install`
   only what is named, and `brew install poppler` for `pdftoppm`. Do not
   install full MacTeX from this skill.
2. Depend on installed Moloch. Wrapper `templates/moloch-cjk/` only. Do
   not vendor Moloch source (ShareAlike would not fit NC-SA if modified).
3. Ship `templates/sysu-like/` as an own look-alike (SYSU green colours
   only). Logos local and untracked. Do not copy yxnchen files.
4. Ban `\pause` and other overlays; duplicate frames with muted earlier
   items.

SimplePlus `.sty` files are vendored Unlicense copies plus a CJK wrapper.
`deai-writing` gains a `slides` profile rather than a parallel skill.
Meeting artefacts go through research-records Task 8.

## Consequences
- `build.sh` fails closed and prints the `tlmgr`/`brew` line for the
  missing tool.
- SYSU branding is colour-only unless the user supplies logos they may use.
- Density and overlay rules are machine-checked; box overflow still needs
  a visual pass (Beamer hides some warnings).

## Do not
- Do not vendor Moloch or yxnchen/sysu-beamer-template.
- Do not insert overlay commands in a style pass.
- Do not force-push; open a normal PR against `main`.
- Do not install a full MacTeX tree to satisfy this skill.

## Sources
`docs/handoff/group-beamer-notes.md` (still cited by skills); owner
decisions 2026-10-17. The Step-1 prompt and Step-2 proposal files were
removed as unused.
