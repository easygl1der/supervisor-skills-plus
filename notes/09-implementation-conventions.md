# 09 Implementation conventions (for every Phase 4 skill)

Repo: /Users/wriseai/Projects/supervisor-skills-plus (private fork of HKUSTDial/Supervisor-Skills).
Read DESIGN.md (the approved design; your skill's section in §4, plus §3, §5, §6, §7, §8) and this file before writing.
Reference implementations to imitate: skills/research-core, skills/feedback-to-revision, skills/research-records.

## Hard rules (lint and CI)
- `skills/<name>/SKILL.md` with YAML frontmatter: `name` (= dir name, kebab-case), `description` (40-80 words, third person, must contain "Use when", must NOT contain the words I, my, we, our, us), `license: CC-BY-NC-SA-4.0` (keep an upstream skill's existing license field).
- SKILL.md body: at most 500 lines, English only (no CJK characters), no em-dash (U+2014), no attribution strings ("Co-Authored-By: Claude", "Generated with").
- Long material goes to `references/*.md`. Point to it from SKILL.md with a line `See: references/<file>.md` (lint checks these resolve). Reference files: no em-dash; files over 100 lines need "## Contents" within the first 20 lines; never write the literal text "See: references/" inside a reference file (nested pointers are forbidden). CJK is allowed in references (e.g. short original-language quotes).
- Shared files: upstream keeps some reference files byte-identical across skills, enforced by scripts/check_shared_sync.py (paper-polish is canonical for academic-phrasebank.md, ai-tone-guardrails.md, section-conventions.md copied into paper-writer; paper-writer is canonical for evidence-discipline.md and prose-delivery.md copied into intro-drafter). If you edit a canonical file, copy it to its copies (keep each copy's first HTML-comment header line). Only the owner of the paper-writer/paper-polish/intro-drafter workstream may touch those.
- Run before finishing (Python with PyYAML): `~/.venvs/ssp-lint/bin/python scripts/lint_skills.py`, `scripts/check_checklists.py`, `scripts/check_sources.py`, `scripts/check_shared_sync.py`. All must pass for your files.
- No git commands. Do not spawn subagents. Touch only the directories assigned to you.

## Content rules
- Every new skill has "Step 0: Load context": load `research-core` (named core files, the field profile from research.yaml `field`, venue profile, named checklists) and read the relevant research.yaml keys.
- Every skill ends with a "Checklist" section naming which research-core checklist IDs or files it runs, reporting pass/fail/n/a/unknown with evidence; and an "Outputs" and "Hand-offs" section.
- For UPSTREAM skills: strengthen, do not rewrite. Keep upstream text and structure where possible (cheap future merges from upstream). Add new sections or new reference files; edit existing lines only when they conflict with the design. Mark AI/ML-specific parts as such where the design says so. Add Step 0 (load research-core) near the top.
- Rules and examples that come from evidence carry sources in the format of skills/research-core/references/core/precedence.md: `[src: ...] (confirmed|candidate)`. Prefixes: arc:msr:<sha>, arc:ol:<sha>, arc:chat:group@<ts>, arc:<path>, arc:@senior-a-comments, arc:@advisor-glimpse, arc:@threats-pivot, arc:<ID>@v2, note:nNN§x, up:<path>, skill:<name>, lit:<key>, user:<date>. Never invent sources, quotes, numbers or dates. Evidence notes: notes/01..08. Private archive: /Users/wriseai/Projects/supervisor-skills-msr-tpa (cite, do not copy private material).
- Anonymize: roles not names (student, senior co-author A/B, advisor, reviewer); no lab names, no dataset sizes or counts from the project, no repository or ecosystem names, no paper titles, no project URLs. Domain if needed: "a niche software ecosystem's issue trackers".
- Former local skills (user-authored, may be merged): ~/.claude/skills/<name>. Third-party passages inside them (brian-bell, ECC, lecture-deck transcription, an unnamed reviewer suite) are restated, not copied. avoid-ai-writing is MIT (Conor Bronsdon): if you vendor its text, include its LICENSE file in the skill folder and credit it.
- Owner skills that exist or are planned: research-supervisor, research-core, idea-evaluator, deep-research, experiment-workflow, paper-writer, intro-drafter, tech-paper-template, benchmark-paper-template, style-mine, deai-writing, paper-polish, check-loop, figure-designer, drawio-reconstruction, feedback-to-revision, pre-submission-reviewer, rebuttal-guidance, research-records, vibe-research-workflow, lessons-harvest.
- Write plainly; no marketing tone; no AI-tell phrasing in the skill files themselves.
