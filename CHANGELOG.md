# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed (ADR 0021: skill groups)
- The 26 skills are regrouped into twelve `sv-` groups plus `research-core`.
  Each group has one auto-invocable entry `sv-<group>` that routes and says
  which sub-command it chose, and slash-only sub-commands
  `sv-<group>-<name>` (`disable-model-invocation: true`), 50 in all. Names
  are identical in Claude Code and Cursor. Old SKILL.md bodies are kept
  verbatim as `references/procedure.md` files with a `Moved from` header;
  references duplicated across skills now live once per group.
- Old to new names: `research-supervisor`, `research-records`,
  `lessons-harvest` -> `sv-supervisor` (`-brief`, `-init`, `-records`,
  `-harvest`); `paper-quickread` -> `sv-quickread` (`-card`, `-style`);
  `study`, `research-bridge` -> `sv-study` (`-quick-explain`, `-paper`,
  `-chapter`, `-visual-explain`, `-drill`, `-bridge`); `idea-evaluator` ->
  `sv-idea` (`-evaluate`, `-fatal-flaws`); `deep-research` ->
  `sv-litreview` (`-survey`, `-map`); `proposal-writer` -> `sv-proposal`
  (`-kaiti`, `-grant`, `-statement`); `experiment-workflow` ->
  `sv-experiment` (`-freeze`, `-runs`, `-numbers`, `-replication`);
  `paper-writer`, `intro-drafter`, `tech-paper-template`,
  `benchmark-paper-template`, `paper-polish`, `deai-writing`, `style-mine`
  -> `sv-write` (`-skeleton`, `-intro`, `-section`, `-polish`,
  `-translate`, `-critique`, `-humanize-paper`, `-humanize-report`,
  `-humanize-slides`, `-humanize-letter`, `-humanize-audit`, `-style-mine`,
  `-style-apply`); `figure-designer`, `drawio-reconstruction` and the study
  visual kit -> `sv-figure` (`-design`, `-drawio`, `-plot`, `-tikz`,
  `-html`, `-poster`, `-explain`); `pre-submission-reviewer`, `check-loop`
  -> `sv-review` (`-once`, `-loop`); `feedback-to-revision`,
  `rebuttal-guidance` -> `sv-feedback` (`-revise`, `-guidance`,
  `-rebuttal`); `group-beamer` -> `sv-slides` (`-weekly`, `-talk`);
  `vibe-research-workflow` -> `research-core`
  `references/core/ai-collaboration.md` and `references/vibe/`.
- `research-core` is hidden from the slash menu (`user-invocable: false`)
  and stays model-invocable. The eleven always-visible descriptions are at
  most 60 words.
- `sv-figure-plot`, `sv-figure-html` and `sv-figure-poster` only combine
  existing rule files; the poster sub-command says that no poster-specific
  rules exist yet.
- Skills are no longer synced from upstream HKUSTDial/Supervisor-Skills;
  `handbook/` still follows upstream PhD.Skills.

### Added
- `sv-experiment-prereg`: pre-registration of confirmatory analyses (estimand,
  hypotheses, exact primary analysis, decision rule, stopping, multiplicity)
  frozen as a git commit, with an audit (FROZEN, STAMP, INTEGRITY,
  CHRONOLOGY, DATA) before any confirmatory claim; unregistered analyses are
  exploratory. Vendors `prereg.sh` from K-Dense-AI/science-superpowers (MIT).
  Implements research-core IN-09 and, for causal work, CI-01. Chosen from the
  survey in `docs/plans/2026-10-19-hot-skills-research.md`.
- `scripts/sync_agent_links.py`: plans (dry run by default) or applies the
  committed relative links in an agent-sync tree plus a per-machine
  `external/` link; never touches entries it did not create.
- `scripts/lint_skills.py` group rules: entry descriptions at most 60 words
  and bodies at most 120 lines; sub-commands slash-only, at most 100 lines
  (`sv-figure-drawio` exempt), listed in their entry's routing table; every
  routed name exists; `See: ../<skill>/references/...` pointers resolve.
- `scripts/install.sh` removes links into this repo whose skill no longer
  exists.
- `group-beamer` (now `sv-slides`): Beamer decks for group meetings in two modes, `weekly-report`
  (with the `progress` variant; loads last week's next steps from the
  research-records log and marks them done / partial / dropped) and a critical
  `paper-talk` (paper card, ranked identifying assumptions, results without
  causal verbs, reproducibility slide, closing discussion question); advisor
  or peer audience; Moloch (installed), vendored SimplePlus and an own
  SYSU-like theme; `build.sh`, `check_log.py` (boxes mapped to pages,
  undefined citations and references), `lint_deck.py`, `render_pages.sh`,
  `export_notes.py`. ADR 0020. `research-records` Task 8 and the research-core
  `group-meeting-log.md` template store each meeting.
- `group-beamer` evals compiled with TinyTeX (`evals/2026-10-17-weekly/`,
  `evals/2026-10-17-paper-talk-sdid/`). Fixes found by the run: scripts were
  not executable; `check_log.py` reported warnings on the previous page;
  `export_notes.py` numbered notes by order instead of by frame and kept
  LaTeX escapes; `build.sh` picked a theme from comments; the Moloch wrapper
  now fills blocks so decision questions show as a box; the weekly skeleton
  gained a kill-criterion column and lost an unsourced number;
  `render_pages.sh` uses `pymupdf` instead of the deprecated `fitz`.
  `lint_deck.py` exempts frames marked `% gb:text-ok <reason>` from the
  text-only share, and the sample decks lost their filler formulas.
- `deai-writing` `slides` profile: Beamer detection, a `slides` column in the
  tolerance matrix, and protected deck elements in the editing contract.
- `style-mine` intake without MCP: `scripts/intake_search.py` (Crossref +
  OpenAlex; Semantic Scholar with a key) searches the top-4 statistics
  journals or an author and filters a publication list into exemplars;
  append-only queue, human-gated promotion. Author profiles and the
  author/venue conflict table (`references/author-profile.md`). ADR 0018.
- Light polish of `research-bridge` and `proposal-writer` (architecture
  unchanged): process/pipeline common breaks; a non-estimator bridge eval
  (`evals/general-process/`); `references/zh-kaiti-register.md` for Chinese
  kaiti sentence frames; Evals sections and ADR 0016 cross-links.
- Plan for causal style mining and top-4 stats journal monitoring:
  `docs/plans/2026-10-17-causal-style-mining-and-monitor.md`, Claude session
  prompt `docs/plans/2026-10-17-causal-style-mining-and-monitor-CLAUDE.md`,
  and handoff pointer `docs/handoff/causal-style-mining-plan-2026-10-17.md`.
  Follow-up investigation
  `docs/plans/2026-10-17-causal-style-mining-investigation.md`: ranked intake
  (Crossref + OpenAlex recommended; Apify not default), external style-skill
  borrow list, and Liu corpus discovery via `hanzhong-liu-research`
  `publications.json` (no invented paper list). Promote gate unchanged.
  No skill rewrites; no daily auto-merge into research-core.

- Reading-and-learning layer that works without `research.yaml`:
  `paper-quickread` (nine-section quick read, `--style` style card,
  `check_quickread.py`, append-only `index_append.py`), `study`
  (understanding-first protocol, three-layer diagnosis, learner profile in a
  separate study vault via `vault.py`, paper / book / concept modes, HTML
  visual kit with steppers and a render checker), `research-bridge`, and a
  literature-map mode in `deep-research`.
- `proposal-writer` for thesis proposals, research plans and grant
  applications.
- `research-core` `inputs-mineru.md` (MinerU-only input, precision CLI route,
  stop on failure, table readability gate) and filled `fields/causal.md` and
  `fields/stats.md` candidate rules.
- Eval runs with real outputs in `skills/study/evals/` (SDID paper, Murphy
  PML1 ch. 4, Lomuto partition stepper, literature map) and, after the
  2026-10-17 polish, bridge/proposal cards under each skill's `evals/`.
- `THIRD_PARTY.md` at the root; ADRs in `docs/adr/`.

### Removed
- `skills/journal-adapt/` pointer stub; `style-mine` is the only name (ADR 0019).

### Changed
- Bridge and proposal eval cards moved from `skills/study/evals/{bridge,proposal}/`
  to `skills/research-bridge/evals/` and `skills/proposal-writer/evals/`;
  old paths keep README pointers. Shared SDID reading notes stay under
  `skills/study/evals/reading/`.
- NSFC 2026 three-part body cited from official NSFC pages (2026-10-17);
  NSF/ERC/NIH page counts treated as examples to verify against the current
  PAPPG / Information for Applicants / FOA. Heilmeier re-checked on the
  DARPA page the same day.
- Bridge literature entries marked confirmed where a DOI or publisher page
  was checked; Cartwright and Hardie remains candidate (book, full text not
  verified).
- `journal-adapt` merged into `style-mine` (Dissect / Accumulate / Apply);
  `skills/journal-adapt/` is now a pointer.
- `research-supervisor` routes reading and learning requests by intent before
  stage.
- Study kit `drawDAG`: edge labels as layout nodes (`labelsAsNodes`), per-node
  radius and `fitLabels`, `spacing`, and arrowheads spread around a node that
  many edges enter.

## [3.0.0-plus] - 2026-10-13

Supervisor-Skills Plus, private fork of HKUSTDial/Supervisor-Skills.

### Upstream sync

- Forked from upstream `main` at `5f9432d` (2026-10-12). Upstream branch
  `chore/sync-drawio-reconstruction` deliberately not merged (hard-coded
  `~/.codex` paths); revisit when upstream merges it.

### Added

- `research-core`: core rules (claims and evidence, body text, de-AI
  contract, feedback loop, figures, records, integrity, precedence and source
  formats), field profiles (`se` evidenced; `ai-ml`, `math` partial; `stats`,
  `causal` stubs), venue profiles (`fse` draft, template), nine checklists
  with sourced items and a candidate/confirmed/deprecated lifecycle, expert
  notes store, project templates (`research.yaml`, STATUS, TODO, ADR, log,
  guidance record, response table, claim ledger, runs log, data manifest).
- New skills: `research-supervisor`, `experiment-workflow`, `journal-adapt`
  (vendored from the owner's skill, MIT), `deai-writing` (merge of three de-AI
  skills; includes MIT text from avoid-ai-writing by Conor Bronsdon),
  `check-loop`, `feedback-to-revision`, `research-records`,
  `lessons-harvest`.
- Scripts: `check_checklists.py`, `check_sources.py` (resolves every
  `[src: ...]` against notes, upstream files and the private evidence
  archive), `install.sh` (symlink install for Claude Code, Codex, Cursor with
  backup of retired local skills), and per-skill scripts (PDF comment
  extraction, marker listing, guidance review, sync guard, span guard,
  numbers check, anonymity grep, data manifest, icon index, TikZ render,
  rule-candidate finder, session brief, paper scaffold).
- Handbook case 6.4 (zh/en): anonymized process case of an empirical SE paper.
- `INSTALL.md`, `DESIGN.md`, `PROGRESS.md`, evidence notes in `notes/`.

### Changed

- Strengthened upstream skills: `paper-writer`, `intro-drafter`,
  `paper-polish`, `pre-submission-reviewer`, `rebuttal-guidance`,
  `idea-evaluator`, `figure-designer`, `drawio-reconstruction`; descriptions
  of `tech-paper-template` and `benchmark-paper-template` now state their
  AI/ML and systems scope. `vibe-research-workflow` links to records and
  experiments.
- `paper-polish/references/ai-tone-guardrails.md` (canonical) now includes
  the extra words flagged by `pre-submission-reviewer`; copies re-synced.
- `CONTRIBUTING.md`: this fork allows a `Co-Authored-By` trailer in commits;
  sourcing and anonymization rules for research-core.

## [2.1.0] - 2026-07-10

### Added

- Added `drawio-reconstruction`, an MIT-licensed skill adapted from
  `sxy1499894281/drawio-reconstruction-skill`, for reconstructing
  reference images into editable Draw.io files with PNG previews and
  visual audits.
- Three skills ported back from our Doubao adaptation practice, where
  they were built and field-tested (all original content):
  - `paper-writer`: evidence-gated drafting of any section or a full
    manuscript. Factual claims trace to the user's materials, verified
    retrieval, or field common knowledge; model memory is never a
    source; delivered prose carries zero placeholder tags; citations
    pass an independent verification ladder (fresh-context sub-agent,
    same-context API grounding, or closed book with disclosure).
  - `paper-polish`: meaning-preserving language polish with a hard
    faithfulness rule (meaning-risk edits are flagged, never silent),
    AI-tone removal, claim calibration, and Chinese-to-English
    rewriting.
  - `deep-research`: survey-grade literature investigation with frozen
    research questions, multi-perspective search, per-citation
    verification (grey zone means unused), MECE synthesis with
    in-sentence cross-comparison, and six internal quality gates.
- `idea-evaluator`: substitute evaluation frameworks for non-STEM
  paradigms (`references/domain-evaluation-frameworks.md`), scoring
  discipline (data-or-mechanism grounds, mechanism-based high scores
  with a named validation experiment), attribution discipline, a
  retrieval-grounded novelty check, and a data-refuted-mechanism
  short-circuit rule.
- `scripts/check_shared_sync.py`: shared reference files are duplicated
  per consuming skill with a canonical header; this checker enforces
  parity.

### Changed

- Repository layout flattened: skills moved from
  `plugins/phd-research/skills/` to top-level `skills/` (the plugin
  nesting was vestigial; no plugin manifest ever existed), the English
  handbook mirror moved from `docs/en/handbook/` to top-level
  `handbook-en/`, and images moved from `assets/images/` to `assets/`.
  All links, the linter, and the sync checker updated; the
  handbook-resync image-rewrite convention now targets `../../assets/`.
- `intro-drafter` now outputs six paragraphs of Introduction prose by
  default (the flowchart becomes an internal scaffold; the classic
  outline remains available on explicit request), never fabricates
  running examples, and inherits the shared evidence discipline.
- `pre-submission-reviewer` gains a paradigm-and-venue-fit step
  (review emphasis switches across STEM, humanities, empirical social
  science, finance/economics, and law), retrieval-grounded novelty and
  citation-completeness checks, an attribution-isolation check, and a
  severity-honesty rule; the integrity gate runs silently.
- `vibe-research-workflow` stance precisified: fabrication is
  forbidden, drafting is not. Drafting requests route to the drafting
  skills under the shared evidence discipline, with disclosure and
  author-verification duties restated.
- Delivery philosophy across evaluator skills: integrity gates run
  silently and surface as findings instead of printed gate reports.

### Fixed

- Restored `## Integrity gate` sections in six SKILL.md files
  (`intro-drafter`, `pre-submission-reviewer`, `figure-designer`,
  `idea-evaluator`, `tech-paper-template`, `vibe-research-workflow`)
  byte-for-byte from commit `6527860~1`; forward references from each
  Step body now resolve.
- Removed orphan closing triple-backtick at EOF of those six files.
- Neutralised eleven references to the nonexistent
  `disruptive-innovation-scout` skill by redirecting to
  `handbook/02_Idea_Generation/2.3`.
- Corrected three stale `../../1_Guide/...` hyperlinks in
  `handbook/03_Paper_Writing/3.2` to use relative `../06_Case_Studies/`.

## [2.0.1] - 2026-04-20

Curriculum re-sync per upstream methodology author. The `handbook/` tree
is re-aligned with the current `HKUSTDial/PhD.Skills/1_Guide/` master,
which had drifted since v2.0.0 (new passages, new figures, renamed PDF).

### Changed

- All 18 handbook MD files re-synced verbatim from upstream. The only
  local edit is an image-path rewrite `../../images/` ->
  `../../assets/images/` to preserve the Supervisor `assets/` layout;
  chapter-local refs (`./assets/5.1_vibe_research/...`,
  `./assets/5.2_meeting_notes/...`) remain as upstream.
- Companion PDF renamed
  `handbook/01_Preliminary/博士生科研入门辅导_2023年8月.pdf` ->
  `博士生科研入门辅导.pdf` to match upstream. All references in
  `README.md` and `README.en.md` updated.
- `assets/images/intro_flowchart_board.png` updated to the current
  upstream revision.

### Added

- 10 image assets under `assets/images/`: `aflow_existing_vs_ours.png`,
  `alpha_sql_solution_overview.png`, `dense_body_layout_example.png`,
  `experiment_canvas_bad.png`, `experiment_canvas_good.png`,
  `lead_solution_overview.png`, `performance_teaser_example.png`, plus
  `.webp` variants for `aflow_solution_overview`,
  `intro_flowchart_alpha_sql`, `intro_flowchart`.
- 11 chapter-local assets for Chapter 5:
  `handbook/05_Vibe_Research/assets/5.1_vibe_research/image1..10.png`
  and `handbook/05_Vibe_Research/assets/5.2_meeting_notes/foundation_agents_vibe_research_overview.png`.

### Unchanged

- `plugins/phd-research/skills/` (seven anchor skills, per v2.0.0
  Guide/Skill decoupling rule).
- `docs/en/handbook/` (English mirror; content-level re-translation
  tracked separately).
- `scripts/`, `.claude-plugin/`, `CONTRIBUTING.md`, `LICENSE`, `llms.txt`.

## [2.0.0] - 2026-04-20

Structural reset per upstream methodology author. The human-readable
curriculum is restored to the original wording and layout from
`HKUSTDial/PhD.Skills` (master branch); the rewritten intermediate docs
shipped in v1.0.0 are removed.

### Changed

- `README.md` reverted to the master-branch narrative of PhD.Skills, with
  a project logo added and the file tree updated to reflect the new
  Supervisor-Skills layout.
- Chinese curriculum promoted from `archive/v1-source/1_Guide/` to the
  top-level `handbook/` directory, preserved verbatim.
- English curriculum re-translated from the restored Chinese handbook
  into `docs/en/handbook/`, replacing the v1.0.0 English overviews.
- License changed from CC BY 4.0 to **CC BY-NC-SA 4.0** to match the
  upstream methodology.

### Removed

- `docs/zh/foundations/`, `docs/zh/skills/*/overview.md`,
  `docs/zh/case-studies/`, `docs/zh/README.md` (intermediate Chinese
  documentation rewritten by the v1.0.0 maintainers).
- `docs/en/foundations/`, `docs/en/skills/*/overview.md`,
  `docs/en/case-studies/`, `docs/en/README.md` (English mirror of the
  removed Chinese docs).
- `archive/v1-source/` (content promoted to `handbook/` or obsolete).
- `README.en.md` v1.0.0 version (replaced by a new English mirror of the
  restored root README).

### Unchanged

- `plugins/phd-research/skills/` (seven anchor skills and their
  `references/`, `SKILL.md`, `HOW-TO-USE.md`).
- `scripts/lint_skills.py`.
- `.claude-plugin/` manifests.

## [1.0.0] - 2026-04-19

Initial public release of `Supervisor-Skills · 博导科研技能包`.

### Included

- Seven anchor skills under `plugins/phd-research/skills/` covering the full
  paper lifecycle:
  - `idea-evaluator`: five-dimension potential analysis, lifecycle-capability
    matching, fatal-flaws audit, paradigm-shift probing.
  - `vibe-research-workflow`: Vibe Coding / Figure / Writing tool choice and
    six behavioural rules.
  - `intro-drafter`: six-paragraph Introduction outline.
  - `tech-paper-template`: technical-paper thinking table plus four
    consistency checks.
  - `benchmark-paper-template`: five-pillar audit, six-part Introduction
    logic chain, Section 2-7 skeleton, and pre-submission checklist.
  - `figure-designer`: paradigm guidance for motivated, overview, and
    experimental figures, plus a universal quality checklist.
  - `pre-submission-reviewer`: five-dimension reviewer self-check with
    severity-tagged findings.
- Bilingual reader guides under `docs/en/` and `docs/zh/` covering paper
  quality foundations, per-skill long-form overviews, and three accepted-paper
  case studies (Alpha-SQL at ICML 2025, AFlow at ICLR 2025, LEAD at VLDB 2026).
- Preserved original Chinese curriculum at `archive/v1-source/`.
- SKILL.md structural linter at `scripts/lint_skills.py`.
- Chinese-primary `README.md` with English mirror `README.en.md`.
- CC BY 4.0 license.
