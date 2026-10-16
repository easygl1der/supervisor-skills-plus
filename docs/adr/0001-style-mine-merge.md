# ADR 0001: journal-adapt merged into style-mine; stub kept

Status: accepted
Date: 2026-10-16
Deciders: owner (SPEC §3.4), Claude Code (stub details)

## Context
The reading upgrade adds `paper-quickread --style`, which dissects one
paper's writing style. A second style store next to journal-adapt would
compete with it (SPEC D4). Installed links, check-loop configurations and
notes name `journal-adapt`.

## Options considered
1. New `style-mine` beside journal-adapt: two style memories (rejected, D4).
2. Rename in place, no stub: breaks installed links and old prompts.
3. Rename with `git mv`, keep a pointer-only `journal-adapt` skill.

## Decision
Option 3. All files moved to `skills/style-mine/`; SKILL.md regrouped into
dissect, accumulate and apply loops; every mode kept. `skills/journal-adapt/SKILL.md`
is a valid skill (frontmatter passes lint) that only points to style-mine,
so `install.sh` links it like any other skill. Live references were renamed;
history (CHANGELOG, PROGRESS, notes 01 to 08, handoff) keeps the old name.

The SPEC said journal-adapt's Step 2 already used `mineru_parse_documents_smart`.
Checked with `rg`: it did not; it listed optional converters and asked for
Markdown when they failed. Replaced by the shared MinerU-only rule in
`research-core/references/core/inputs-mineru.md`, which also covers
paper-quickread and study.

## Consequences
- 22 skill folders (21 with workflows plus the pointer).
- Remove the stub after one release when no installed link uses the old name.

## Do not
- Do not add rules to the stub.
- Do not keep a second style store (writing memory, global style file).
