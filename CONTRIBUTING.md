# Contributing

This repository welcomes issues, pull requests, and discussions. Please read this guide before opening a PR.

## Scope

The current skill set contains eleven anchor skills under `skills/`: `idea-evaluator`, `deep-research`, `vibe-research-workflow`, `intro-drafter`, `paper-writer`, `tech-paper-template`, `benchmark-paper-template`, `paper-polish`, `figure-designer`, `drawio-reconstruction`, `pre-submission-reviewer`. Adding a new skill requires:

1. Discussion via issue first; confirm the skill fills a real gap and is not covered by an existing skill.
2. Clear attribution for any content not derived from `handbook/`.
3. Adherence to the SKILL.md conventions below.

## Authoring a skill

Each skill directory at `skills/<name>/` contains:

- `SKILL.md`, English, under 500 lines, with valid YAML frontmatter containing `name` and `description`.
- `references/*.md`, on-demand depth. Files over 100 lines must begin with a table of contents.
- Optional `scripts/*.py` for deterministic helpers and `assets/*` for templates.

## Hard rules (enforced by CI)

- SKILL.md body under 500 lines.
- `description` between 40 and 80 words, written in third person, contains at least one "Use when..." clause.
- No em-dash (U+2014) in `SKILL.md` or `references/*.md`; use commas or periods.
- No Chinese characters in SKILL.md (the canonical Chinese curriculum lives at `handbook/`; English mirror at `handbook-en/`).
- All `See: references/X.md` pointers must resolve to existing files.
- No nested references (`SKILL.md -> refs/a.md -> refs/b.md` is illegal).
- Reference files shared across skills are duplicated per consuming skill (skills stay self-contained); each copy carries a header naming its canonical, and copies must stay byte-identical to the canonical below the header (`python scripts/check_shared_sync.py`).
- Upstream rule: commits must not contain "Claude", "Co-Authored-By: Claude", or Anthropic attribution. **This private fork (Supervisor-Skills Plus) allows a `Co-Authored-By` trailer in commit messages** (owner decision 2026-10-12). Skill and reference files still must not contain attribution strings; `lint_skills.py` enforces that.

## Running the linter

```bash
python -m pip install -r requirements-lint.txt
python scripts/lint_skills.py
python scripts/check_shared_sync.py
```

The linter exits non-zero on any violation and is invoked by `.github/workflows/lint.yml` on every PR.

## Bilingual content

The Chinese `handbook/` is the canonical curriculum, preserved verbatim from the methodology author. The `handbook-en/` directory is a faithful English mirror and follows the same chapter and file structure. Keep the two trees symmetric in any PR that edits the curriculum.

When re-syncing `handbook/` from upstream `HKUSTDial/PhD.Skills`, the only permitted local edit remains the image-path rewrite; its target is now `../../assets/` (images sit directly under `assets/`, no `images/` subfolder). Chapter-local asset references (`./assets/...`) stay as upstream.

## License

All contributions are licensed under CC BY-NC-SA 4.0. By submitting a PR you agree to license your contribution under these terms and to provide attribution consistent with the original repository's convention.

## Commit conventions

Conventional Commits:
- `feat(skill): <name> ...` for new skills
- `feat(<area>): ...` for new non-skill features
- `fix(<area>): ...` for bug fixes
- `docs(<area>): ...` for documentation
- `build: ...` for build system, CI, tooling
- `chore: ...` for routine maintenance
- `refactor(<area>): ...` for refactoring

Upstream: commits must not include any Claude or Anthropic attribution. In this fork a `Co-Authored-By` trailer is allowed (see Hard rules).

## Supervisor-Skills Plus additions

- Shared rules, field and venue profiles, checklists and project templates live in `skills/research-core`. Do not put project-specific rules there; those belong in the project repo (`docs/adr/`, overlays).
- Every rule and checklist item carries a source (`[src: ...]` or `- Src:`), in the formats listed in `skills/research-core/references/core/precedence.md`, and a status (`candidate`, `confirmed`, `deprecated`). Rules without a source go under "Unknown".
- Never write a person's name in skill files; use roles. Archive paths that contain names are cited through the aliases in `scripts/check_sources.py`.
- Run all four checks before merging: `lint_skills.py`, `check_shared_sync.py`, `check_checklists.py`, `check_sources.py`.
- New rules usually arrive through `lessons-harvest` on a `learn/<source>` branch.

