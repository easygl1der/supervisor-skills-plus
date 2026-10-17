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

### Group 2: feedback-to-revision + research-records (2026-10-13)
- feedback-to-revision (branch feat/feedback-to-revision): SKILL.md with revision mode (A1-A6) and guidance mode (B); references intake-and-triage, apply-and-verify, guidance-mode (example built from archived threats-pivot notes; action rows marked illustrative), worked-examples (6, anonymized); scripts extract_pdf_comments.py (vendored), list_markers.py (live, commented-out, iffalse, hidden-notes, parked), guidance_review.py (open/overdue/no-evidence actions; unverified feedback rows). Tested: list_markers on the archived paper snapshot finds 4 commented-out notes, 1 live note, 5 parked blocks; guidance_review on a synthetic project flags overdue and no-evidence actions.
- research-records (branch feat/research-records, based on feedback branch): SKILL.md with 7 tasks; references adr, sources-and-sync, anti-accretion (restated, third-party text not copied), linear-mirror; scripts sync_guard.py (refuses non-fast-forward sync; tested on a simulated overwrite).
- Checks: lint 15 skills clean; checklists 192 clean; sources 924 resolved, 0 failed; shared-sync clean.
- Waiting for user review before merge.

### Groups 3-8 and Phase 5 (2026-10-13, user: "merge, continue till finally done")
- Six parallel workstreams (conventions in notes/09) built: deai-writing, check-loop; paper-writer, paper-polish, intro-drafter strengthened; journal-adapt (vendored, MIT kept), lessons-harvest; figure-designer, drawio-reconstruction (icon registry of 20 libraries with licences read on 2026-10-13); pre-submission-reviewer, rebuttal-guidance, idea-evaluator, template descriptions; experiment-workflow, research-supervisor, vibe links.
- Main session: handbook 6.4 zh/en (process case, generic domain), private/CASE.md (gitignored), README/skills README/llms.txt Plus sections, CONTRIBUTING fork rules, CHANGELOG 3.0.0-plus, INSTALL.md, scripts/install.sh (tested in a fake HOME), CI runs the two new checkers.
- Quality pass: privacy grep (no names, counts or domain names in skills or 6.4), AI-tell and accretion grep (only legitimate list entries), banned-word lists unified into the canonical ai-tone-guardrails, all citations re-resolved.
- Final checks: lint 21 skills clean; check_checklists 192 items clean; check_sources 1397 resolved, 0 failed (in CI mode without the archive: arc: citations skipped); shared-sync 6 copies in sync. Smoke test: session_brief on a template project flags hidden markers, missing deadline source, stale STATUS.
- Known limits: render_tikz.py not render-tested (no TeX here); stats and causal profiles are stubs; no reviewer-report evidence for rebuttal rules.

## Phase 6: Reading and learning layer (2026-10-16 to 2026-10-17)

- Built from `docs/handoff/supervisor-plus-reading-upgrade-SPEC.md`: style-mine (journal-adapt merged), paper-quickread, study (with the visual kit), research-bridge, proposal-writer, deep-research literature-map mode, research-supervisor routing by intent. Decisions in `docs/adr/0001`-`0017`.
- SPEC claims checked and corrected: journal-adapt never called the MinerU MCP tool; the explainer page had no data block; elkjs is EPL-2.0, not MIT.
- MinerU: MCP server not reachable this session (local tunnel down); official CLI precision mode with the user's token converted SDID (69 pp.) and PML1 ch. 4 (60 pp.). Flash mode merged Table 1 cells; precision did not.
- Evals in `skills/study/evals/`: SDID quickread + study (two diagnosis rounds), PML1 ch. 4 book mode (suspected erratum in Exercise 4.9), Lomuto partition stepper, bridge (project and general), proposal (novelty risk R1 confirmed by the paper's appendix §8), literature map.
- Checks: lint_skills 26 clean; check_checklists 208 clean; check_sources 1412 resolved, 0 failed; check_shared_sync 6 in sync; all kit renders with empty warnings.

## Style-mine intake refinement (2026-10-17)

- Followed `docs/handoff/style-mine-intake-PROMPT.md`; no Academic MCP. `intake_search.py`: Semantic Scholar calls spaced 1.2 s and skipped without a key; 429/5xx wait Retry-After or 8, 15, 30 s. `--selftest` covers both offline (stubbed network and clock).
- Live smoke with `INTAKE_MAILTO`: `journal jasa --since 2026-01-01` returned 25 rows; `author` without an ID printed candidates and stopped. S2 with a key not run (no key on this machine).
- Docs aligned to `--help` (`references/intake.md` flag list; README pointed to the right script name).
