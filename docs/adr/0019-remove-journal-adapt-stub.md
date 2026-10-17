# ADR 0019: Remove the journal-adapt pointer stub

Status: accepted
Date: 2026-10-17
Deciders: owner

## Context
ADR 0001 kept `skills/journal-adapt/` as a pointer to `style-mine` so older
notes and installs would still resolve. All live references in this
repository now name `style-mine`; the stub only added a second skill name to
every agent's skill list.

## Decision
Delete `skills/journal-adapt/`. Provenance notes ("formerly journal-adapt")
stay in `style-mine`, `THIRD_PARTY.md` and the ADRs.

## Consequences
- Installs that linked `journal-adapt` from this repo lose that link; rerun `scripts/install.sh`. Standalone copies of the old skill elsewhere are not touched.

## Sources
Owner decision 2026-10-17; ADR 0001.
