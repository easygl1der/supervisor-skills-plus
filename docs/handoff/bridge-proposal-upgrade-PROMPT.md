# Claude Code prompt — light polish of research-bridge & proposal-writer

Paste this to Claude on the SG machine (or any machine with the repo). Skills stay in **English**; chat/report to the user in **Chinese**.

```
You are in ~/Projects/supervisor-skills-plus (private fork). Work directly on main: no branches, no PRs.

LANGUAGE
- Every skill file you edit or add (SKILL.md, references/*.md) must stay in English.
- Eval sample cards may stay bilingual as today (Chinese body + English terms).
- Your final report to me: Chinese.

0) Sync and read first
- git pull
- Read ALL of:
  - /workspace is not on this machine; the upgrade SPEC may be copied to docs/handoff/bridge-proposal-upgrade-SPEC.md OR given in chat. If you do not have it yet, treat the following as the SPEC summary and still read the live skills.
  - skills/research-bridge/** (every file)
  - skills/proposal-writer/** (every file)
  - docs/adr/0016-proposal-draft-markers.md
  - existing evals under skills/study/evals/bridge/ and skills/study/evals/proposal/
  - skills/research-supervisor/SKILL.md routing rows for these two
  - DESIGN.md sections that mention reading / proposal if any
- Also skim: paper-quickread, study (hand-offs), idea-evaluator, experiment-workflow, deep-research literature-map — only enough to avoid breaking hand-offs.

VERDICT YOU MUST RESPECT (do not argue for a rewrite)
- research-bridge and proposal-writer are already mature v1 skills, not thin stubs.
- Evidence: full workflows, theory-backed refs, real evals (SDID bridge, MLE general bridge, kaiti proposal + self-critique that patched the skill), ADR 0016, supervisor routing.
- Your job is LIGHT POLISH only. Do not redesign phases, do not merge skills, do not replace with an external grant-writing skill pack.

1) External verify (search + open pages; cite URLs)
- Re-check NSFC 2026 application body structure (三部制 claim in genres.md §5) against an official NSFC guide/template PDF or the current ISIS help text. If only secondary news exists, downgrade wording to "reported; confirm against the year's official template".
- Confirm Heilmeier still matches https://www.darpa.mil/about/heilmeier-catechism
- For NSF/ERC/NIH page limits: do not hard-code stale numbers; write "verify against current PAPPG / Info for Applicants / FOA" and keep examples as examples.
- Optional skim of open grant skills for ideas to borrow (numbered 创新点, Broader Impacts as its own NSF section) — e.g. wanshuiyin Auto-claude-code-research-in-sleep grant-proposal, k-dense / mzane research-grants pages. Borrow checklist items only; do not copy large copyrighted text; do not add budget/biosketch scope.

2) Implement polish (from SPEC)

research-bridge
- RB-P1: Move or pointer-link evals into skills/research-bridge/evals/ (keep SDID + MLE content).
- RB-P2: Confirm lit sources where possible (DOI); mark confirmed vs candidate consistently with repo conventions.
- RB-P3: Add a short coding/process/pipeline "common breaks" subsection in transfer-checks.md (§3).
- RB-P4: Add one short non-estimator bridge eval (coding habit, experiment pipeline, or figure pipeline → current project).
- RB-P5: Add an Evals section to SKILL.md; one sentence that full transportability formulas / do-calculus are out of scope.
- RB-P6 (optional): one before/after PNG via study kit for the SDID bridge.

proposal-writer
- PW-P1: Move or pointer-link evals into skills/proposal-writer/evals/.
- PW-P2: Fix NSFC 2026 claim after official verify.
- PW-P3: Soften stale funder page limits to "verify against current call".
- PW-P4: Add references/zh-kaiti-register.md — English filename; Chinese/English sentence patterns for 选题依据 (problem first), gap-organized lit review, numbered 创新点 on one axis each, technical roadmap expectation, milestones as deliverables not activities. Inspired by common CN kaiti practice / user textbook context; do NOT paste copyrighted textbook prose.
- PW-P5: Tighten reviewer-lens "school form wins" if needed; keep single-source gap.
- PW-P6 (optional): P2 roadmap + P7 Gantt PNGs for the kaiti eval.
- PW-P7: Evals section + link ADR 0016 from SKILL.md.

DO NOT
- Deep rewrite, merge into idea-evaluator, delete five-verdict system, delete Draft markers, invent school word counts, add budget/CV chapters, force figures every run, use Manim, force-push, open a PR.

3) Test
- Re-read existing SDID bridge + kaiti eval; ensure links still work after moves.
- Produce the new RB-P4 eval (and optional PNGs if you take P6).
- Run: python scripts/lint_skills.py && python scripts/check_sources.py && python scripts/check_checklists.py && python scripts/check_shared_sync.py (and any other lint scripts the repo documents). Fix failures you introduce.

4) Commit and push
- Logical commits, e.g.:
  1) chore(evals): house bridge/proposal evals under their skills
  2) polish(research-bridge): sources, process breaks, non-estimator eval, SKILL evals link
  3) polish(proposal-writer): NSFC verify, zh-kaiti-register, funder limit wording, SKILL/ADR links
  4) docs: CHANGELOG + skills README if counts/paths change
- git push origin main (no --force)

5) Report in Chinese
- What you changed vs deliberately left alone
- Official URLs used for NSFC/Heilmeier/etc.
- Eval paths (old → new)
- Lint results
- Open issues (e.g. still-candidate sources)
```

If the SPEC file is available on the machine, copy it first:

```
# From the box or Mac where the SPEC was written:
# docs/handoff/bridge-proposal-upgrade-SPEC.md
# docs/handoff/bridge-proposal-upgrade-PROMPT.md
# docs/handoff/bridge-proposal-upgrade-SUMMARY.md
```

Prefer the SPEC file over this prompt when they disagree on a detail; this prompt is the execution wrapper.
