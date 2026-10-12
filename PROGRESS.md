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

## Phase 2: Mine the evidence (paused 2026-10-12 by user)

Done and reviewed (key claims spot-checked against patches and chat):
- notes/04-timeline-and-process.md: deadline was 10-03 19:59 CST, not ~10-12; the submitted paper is not `msr:87bf139` (title change `ol:a610d1d` reverted by sync bot `ol:214cc0c`, restored `ol:ba3f1ee`); κ = 0.74 has no computation record (first appears in `msr:393f596`).
- notes/08-process-tips.md: source-of-truth flips, sync-bot overwrite 20 min before deadline, agent Overleaf writes deleting large parts of main.tex (`ol:b2ad042`, `ol:3ae9fd3`), index.html anonymity leak, 40 candidate lessons.
- notes/03 corrected (submitted version, deadline).
- Integrity flags reported to the user: κ = 0.74 untraceable (FINAL-CHECKLIST-2026-10-02 B1); 14 held-out gold cells changed after viewing model output with the 0.65 bar set at the same time (`11-*/tree/docs/notes/gold-review/overlay-high14-review.md`).

Incomplete (agents stopped on pause), in notes/partial/:
- 05-feedback-revision-table.PARTIAL.md (partial draft; the B-chat/PDF and group-chat sub-miners were stopped).
- 06-section-evolution.PARTIAL.md plus three saved helper reports: 06a RQ1, 06b design/methodology, 06c RQ2/RQ3. Missing: intro + conclusion (report finished but not captured), related work + appendix, threats/implications.
- 07-figures-and-checklists: not written.

To resume: rerun Phase 2 for notes/05, 06, 07 using the partial files as input, then Phase 3 (DESIGN.md, STOP).
Open questions to the user (asked, unanswered): commit attribution vs upstream CONTRIBUTING; authorship/licence of local skills without LICENSE; anonymization level for case 6.4.
