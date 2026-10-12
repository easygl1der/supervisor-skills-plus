# PROGRESS

Phase log for building Supervisor-Skills Plus. Newest entries at the bottom of each phase.

## Phase 0: Setup (2026-10-12)

- Archive `~/Projects/supervisor-skills-msr-tpa`: `git pull` and `git lfs pull` report up to date at `669b29a`. Three untracked prompt files (`CLAUDE_*_PROMPT.md`) left as-is.
- Created private repo https://github.com/easygl1der/supervisor-skills-plus with `gh repo create --private` (gh 2.102.0, account easygl1der). Visibility verified: PRIVATE.
- Cloned upstream https://github.com/HKUSTDial/Supervisor-Skills. Latest upstream commit is still `5f9432d` (2026-10-12 07:55 UTC, "docs: recommend DataMagic and DeepEye research projects"); no newer commits.
- Remotes: `upstream` = HKUSTDial (push URL set to `DISABLED_no_push_to_upstream` as a guard), `origin` = easygl1der/supervisor-skills-plus. Pushed `main` to origin, tracking set.
- Baseline checks (PyYAML installed in `~/.venvs/ssp-lint`, outside the repo):
  - `scripts/lint_skills.py`: `12 skill(s) clean`, exit 0.
  - `scripts/check_shared_sync.py`: `5 copy(ies) in sync`, exit 0.
- Added `private/` to `.gitignore`. Work continues on branch `design`.
- Local skill inventory in `~/.claude/skills`:
  - The 12 "upstream copies" are not installed locally; the upstream repo is their source.
  - `msr-tpa-rq-method-borrow` and `adams-sail-issue-mining` are not in `~/.claude/skills`; they exist in the archive at `03-skills/`.
  - All other listed local skills are present. License files found only in `avoid-ai-writing` (LICENSE), `drawio-architecture`, `drawio-flowchart`, `linear` (LICENSE.txt). The rest need a frontmatter/README license check in Phase 1.

## Phase 1: Read (2026-10-12)

- User feedback on local skills (reply 2): journal-adapt and deai-paper-writing are good; wants to know what humanize-paper actually does; se-paper-* capture an SE writing style worth keeping and the writing → refinement → review structure is liked, but output quality was poor when tried with Fable 5.1. Licensing of skills without LICENSE files is still unanswered; treated as "provenance unknown" until checked.
- notes/03-archive-map.md written from the archive index files and folder survey. Found: deadline inconsistency (TIMELINE "~10-12" vs venue file 10-02 AoE and last commit 10-03 19:38), a misattributed provenance line in checklist v2 (CF-01), and the `\hao{}`/`\todo{}` review protocol in `msr:9809b8c`.
- notes/01 and notes/02 delegated to two read-only subagents; to be reviewed before reporting.

## Phase 2: Mine the evidence (2026-10-12, resumed after a pause and completed)

- notes/04-timeline-and-process.md: deadline 10-03 19:59 CST (not ~10-12); the submitted paper is not `msr:87bf139`; source of truth flipped three times; κ = 0.74 has no computation record.
- notes/05-feedback-revision-table.md: 111 revision requests with IDs; 61% verified addressed, 16% partial, 9% superseded, 2% not addressed, 12% no evidence; median latency 9.5 h; `\hao`/`\todo` protocol and its failures; six worked examples.
- notes/06-section-evolution.md: per-section timelines, 12 cross-section rewrite patterns, SE empirical paper skeleton with measured word counts, identifying-excerpt list.
- notes/07-figures-and-checklists.md: figure iteration chains, 21 figure rules (FR1–FR21), checklist version chain, provenance audit (90/140 v2 items mislabelled), classification of reusable items into target checklists. Found that κ = 0.74 entered via a reference image copied by the agent-built draw.io replica (`LAYOUT_FINGERPRINT.md`, `msr:393f596`).
- notes/08-process-tips.md: 40 candidate lessons with citations.
- Key claims spot-checked by the main session against patches and chat (title revert, sync-bot overwrite, κ introduction replacing "we do not report human--human agreement" in threats, overlay disclosure deleted in `msr:5262231`, `\todo` markers removed in `msr:815305e`, replica fingerprint wording).
- Integrity flags reported to the user (κ = 0.74; held-out gold edited after viewing model output).
- notes/partial/ removed; its content is integrated into notes/05 and notes/06.

## Phase 3: Design (2026-10-12)

- DESIGN.md v1 drafted: 20-skill tree, `research-core` foundation (core rules, field and venue profiles, checklists, templates), per-skill procedures, check-loop as a separate orchestrator, local-first records with optional Linear mirror, research.yaml schema, data placement, case 6.4 proposal, open questions Q1–Q9.
- STOP: waiting for the user's review.
- 2026-10-13: user asked for icon sourcing in drawio-reconstruction and a way to keep research-core growing with new papers, fields and expert notes; added `lessons-harvest` (21 skills) and §3.4. User answered case 6.4, fields, expert notes, old-skill handling; remaining questions decided by Claude per user delegation (DESIGN §12).

## Decisions from the user (2026-10-12)
- Keep `Co-Authored-By: Claude ...` in commit messages. This overrides upstream `CONTRIBUTING.md` lines 30 and 63 for this fork; CONTRIBUTING will be amended in Phase 4 to say so. (The lint ban on attribution strings inside SKILL.md and reference bodies still applies.)
- Every local skill without a LICENSE file is user-authored and may be vendored. Exception handling: passages that notes/02 identified as copied from third parties inside those skills (anti-accretive-docs references copied from brian-bell's skills, architecture-decision-records material based on affaan-m/ECC, the lecture-deck transcription in lecture-paper-revision, the unnamed reviewer suite behind se-paper-reviewer) are rewritten in our own words or attributed, not copied verbatim.
- 2026-10-13: user approved DESIGN.md. Added per-field icon registry (to research in Phase 4) and guidance records (`docs/guidance/`, actions with follow-up). Statistics and causal-inference profiles stay blank stubs. Phase 4 starts.

## Phase 4: Implement

### Group 1: research-core (branch feat/research-core, 2026-10-13)
- SKILL.md; core rules (8 files); field profiles se (evidenced, 55 rules, SE-01..19), ai-ml and math (partial), stats and causal (blank stubs per user); overlay no-semicolons-no-dashes; venues/_template and fse (draft, FS-01..14); 9 checklists (142 items, 49 confirmed / 93 candidate); experts/README; 10 project templates incl. guidance-record.md.
- New scripts: check_checklists.py (format, unique IDs, owners), check_sources.py (resolves arc:/note:/up:/skill: citations against notes and the private archive; role-based aliases for archive paths that contain names).
- Checks: lint 13 skills clean; check_checklists 192 items clean; check_sources 851 resolved, 0 failed; shared-sync in sync.
- Waiting for user review before merge.
- 2026-10-13: user chose option 3; 40 items with clear bad outcomes promoted to confirmed (100 confirmed of 175 items in checklists + se + fse). Merged to main.
