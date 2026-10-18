# DESIGN: Supervisor-Skills Plus

Status: draft v1 for discussion (Phase 3). Nothing here is implemented yet.
Skill names below are the pre-ADR-0021 names; the current layout and the old-to-new map are in `docs/adr/0021-sv-skill-groups.md`.
Skill names below are the pre-ADR-0021 names; the current layout and the old-to-new map are in `docs/adr/0021-sv-skill-groups.md`.
Inputs: `notes/01`–`notes/08`. Evidence citations use the formats in `notes/03-archive-map.md` §4 (`msr:<sha>`, `ol:<sha>`, `res:<sha>`, `chat:group@<ts>`, `<file>:<line>`, `<ID>@v2`) plus `[nNN §x]` for a note section. Roles, never names: Student, Senior co-author A, Senior co-author B, Advisor (relayed).

## Contents
1. Goals and design principles
2. Final skill tree and folder structure
3. Shared foundation: `research-core` (core rules, field and venue profiles, checklists, templates)
4. Skills one by one (inputs, procedure, checklist, outputs, evidence)
5. Checklists and their links to skills
6. The check loop
7. Records outside the paper, and the Linear recommendation
8. Experiments, data and tool integration; `research.yaml`
9. Handbook additions (case 6.4) and the private case file
10. New skills found missing, and what to strengthen in upstream skills
11. Repo mechanics: lint, sync, upstream merges, install
12. Open questions

---

## 1. Goals and design principles

One private, installable skill library that runs on every paper, assignment and experiment, in any of the user's fields (SE/MSR, ML, mathematics, statistics, causal inference, others).

Principles, each grounded in what went wrong or right in the evidence:

1. **Field-neutral core, field-specific profiles.** Upstream is tuned to AI/ML and DB writing (`[n01 §5.1]`); the local SE skills were overfitted to two specific papers and contradicted each other (`[n02 §11]`). Rules that hold everywhere live in one core; field and venue rules live in profiles; project rules live in the project repo.
2. **Every rule has a source.** Rules from our project cite the archive; rules from literature cite the paper; rules with no source are marked `unsourced` and are not enforced as checklist items. The archive showed how quickly unsourced claims drift: checklist v2 provenance misattributes items (`CF-01@v2`, `CF-14@v2` "Who: Hao (乐绎华)") and an agent change report claimed 11 fixes that never landed (`[n05 §5.5]`).
3. **Evidence before prose.** Drafting starts from a claim ledger (claim, number, scope, source script). Missing in the local SE skills (`[n02 §11.5]`); its absence produced an untraceable agreement number in the paper (`[n04 §1.6]`, `FINAL-CHECKLIST-2026-10-02.md` B1).
4. **Verify the diff, not the report.** Every "done" is checked against the actual diff, because commit subjects and agent reports misdescribed patches repeatedly (`msr:5262231` "add todo", `msr:815305e` "cursor-safety: checkpoint", REVISION-SUMMARY; `[n05 §5.5]`, `[n06 §0]`).
5. **The paper holds only the newest correct content; history lives in `docs/`.** Anti-accretive body text; records in `docs/STATUS.md`, `docs/adr/`, `docs/log/`.
6. **Checklists are the backbone, and every skill ends by running its checklist.** The project's best moment was a read-only pre-submission check one day early that predicted the anonymity leak (`FINAL-CHECKLIST-2026-10-02.md` B2); its worst was not acting on it (`[n08 §3]`).
7. **Bounded loops.** Every iterative skill has a round budget and stop reasons. Different editors undid each other's edits in this project (numbers trimmed then restored, hedges deleted then restored, "snapshot" vs "dataset" flipping; `[n06 §2.3, §2.6, §2.8]`).
8. **Follow upstream conventions** so upstream merges stay cheap: `skills/<name>/SKILL.md` + `references/`, lint rules, Conventional Commits, Keep a Changelog, bilingual handbook (`[n01 §2]`).

## 2. Final skill tree and folder structure

### 2.1 Skill tree (26 skills)

| Stage | Skill | Origin | One line |
|---|---|---|---|
| Entry | `research-supervisor` | new | Reads `research.yaml` and `docs/STATUS.md`, works out the stage, routes to the right skill, starts new projects |
| Foundation | `research-core` | new | Core rules, field profiles, venue profiles, checklists, templates; loaded by every other skill |
| Idea | `idea-evaluator` | upstream, strengthened | Evaluate an idea; field-aware fatal flaws (adds empirical-study and theory routes) |
| Idea | `deep-research` | upstream | Literature and evidence research with quality gates |
| Experiments | `experiment-workflow` | new | Corpus freeze, gold sets, prompt/model versioning, runs log, number-to-script traceability, data placement, compute backends, replication artifact |
| Writing | `paper-writer` | upstream + se-paper-writing + paper | Draft a paper from a claim ledger, using the field profile's skeleton |
| Writing | `intro-drafter` | upstream, strengthened | Introduction; adds the RQ-driven empirical intro pattern |
| Writing | `tech-paper-template` | upstream | Technique-paper thinking template (field: ai-ml/systems) |
| Writing | `benchmark-paper-template` | upstream | Benchmark/evaluation template (field: ai-ml) |
| Style | `style-mine` | local, strengthened | Build venue and field profiles and a dynamic style skill from exemplar papers |
| Style | `deai-writing` | merge of deai-paper-writing + avoid-ai-writing + humanize-paper | Remove AI tells by intent, with a claim ledger and an editing contract |
| Polish | `paper-polish` | upstream + se-paper-refinement | Single-pass polish of sections against core, field and venue rules |
| Polish | `check-loop` | new | Bounded multi-round loop: research fit, venue/field fit, language; reports what changed |
| Figures | `figure-designer` | upstream + tikz-diagram-review + figure rules from the archive | Plan, critique and check figures; figure-mirrors-methodology rule |
| Figures | `drawio-reconstruction` | upstream + drawio-figure-replication | Rebuild figures as editable draw.io with fingerprint and module QA |
| Feedback | `feedback-to-revision` | new (+ parse-pdf-comments, collaborative-review-notes) | Ingest comments, ID, triage, one change per comment, verify, response table |
| Review | `pre-submission-reviewer` | upstream + se-paper-reviewer | Full review with sub-checklists: threats, double-blind, artifact, venue formatting, integrity, submission day |
| Rebuttal | `rebuttal-guidance` | upstream, strengthened | Rebuttal and revision letters; consumes the feedback table |
| Records | `research-records` | anti-accretive-docs + architecture-decision-records + research-docs-linear-lifecycle | `docs/STATUS.md`, `TODO.md`, `adr/`, `log/`; source-of-truth rules; optional Linear mirror |
| Workflow | `vibe-research-workflow` | upstream | Agent-assisted research habits; links to records and experiments |
| Learning | `lessons-harvest` | new | After each paper or when expert notes arrive, turn feedback, logs and notes into sourced rule candidates for `research-core` (§3.4) |
| Reading | `paper-quickread` | new | Nine-section quick read of one paper (700-character target); `--style` adds a style card for `style-mine` |
| Reading | `study` | new | Understanding-first study of a paper, textbook chapter or concept: restatement, three-layer diagnosis, correction, learner profile in a separate study vault, HTML visual kit |
| Reading | `research-bridge` | new | From what was read or studied to the current project: transfer checks and a minimal validation experiment with a kill criterion |
| Proposal | `proposal-writer` | new | Thesis proposals, research plans and grant applications from RQ to timeline and risks |
| Meetings | `group-beamer` | new | Beamer decks for group meetings: weekly report that loads last week's next steps, and critical paper talk; compile and box checks; meetings logged through `research-records` (ADR 0020) |

The reading skills (`paper-quickread`, `study`, `research-bridge`, `deep-research` literature-map mode) work without `research.yaml`; `research-supervisor` routes them by intent before stage (`docs/adr/`).

Retired as separate skills (stay installed on the machine; not vendored): `se-paper-writing`, `se-paper-refinement`, `se-paper-reviewer`, `deai-paper-writing`, `avoid-ai-writing`, `humanize-paper`, `parse-pdf-comments`, `collaborative-review-notes`, `drawio-figure-replication`, `tikz-diagram-review`, `anti-accretive-docs`, `architecture-decision-records`, `research-docs-linear-lifecycle`, `paper`. Not merged at all: `drawio-architecture`, `drawio-flowchart`, `linear`, `aris-auto-research`, `takenotes`, `writing-beats`, `writing-fragments`, `storytelling`, `writing-shape` (one rule moves to core), `nn-models-drawio-library` and `scientific-illustration-ppt` (pointers only), `lecture-paper-revision` (rules paraphrased into `fields/se.md`). Project-only (stay in the project repo, not the library): `adams-sail-issue-mining`, `msr-tpa-rq-method-borrow`; their method (rules from a corpus of exemplar papers with a consensus threshold) becomes the `style-mine` procedure. Reasons per skill: `notes/02-local-skills-verdicts.md` §9–§10.

Why this many and not fewer: each new skill owns a distinct state file or loop (`feedback` table, `check-loop` round log, `docs/STATUS.md`, runs log). Folding them into existing skills would push those SKILL.md files past the 500-line lint limit (`[n01 §2.1]`).

### 2.2 Repository layout

```
supervisor-skills-plus/
├── README.md, README.en.md          upstream, plus a "Plus" section
├── DESIGN.md, PROGRESS.md, INSTALL.md, CHANGELOG.md
├── CONTRIBUTING.md                  amended: Co-Authored-By allowed in this fork; provenance rule
├── handbook/, handbook-en/          upstream + 6.4 (zh/en)
├── skills/
│   ├── research-core/
│   │   ├── SKILL.md                 how to load context; precedence rules
│   │   ├── references/core/         rules true in every field (§3.1)
│   │   ├── references/fields/       se.md, ai-ml.md, math.md, stats.md, causal.md, _template.md
│   │   ├── references/venues/       fse.md (evidenced), _template.md; others generated by style-mine
│   │   ├── references/checklists/   master, writing, figures, threats, double-blind, artifact, venue-submission, integrity, records
│   │   └── assets/templates/        research.yaml, STATUS.md, TODO.md, adr-0000.md, log-entry.md, response-table.md
│   └── <19 other skills>/SKILL.md + references/ (+ scripts/)
├── scripts/
│   ├── lint_skills.py               upstream (unchanged where possible)
│   ├── check_shared_sync.py         upstream (map extended only if needed)
│   └── check_checklists.py          new: item IDs unique, required fields, provenance present
├── notes/                           Phase 1–2 evidence notes (private repo only)
└── private/                         gitignored: non-anonymized case file
```

Decision to discuss (open question Q1): the brief puts `core/`, `fields/` and `checklists/` at the repo root. I recommend putting them inside one skill, `research-core`, instead:
- upstream requires each skill directory to be self-contained (`scripts/check_shared_sync.py` docstring; `[n01 §2.3]`), and installs work per skill folder (symlink or copy into `~/.claude/skills/`, `~/.codex/skills/`, `~/.cursor/skills/`). Files at the repo root are invisible to an agent that only sees the skills folder;
- the lint script then also checks the profiles and checklists (em-dash, ToC for long files, pointer resolution);
- one canonical copy instead of N synced duplicates.
Cost: every other skill depends on `research-core` being installed. Upstream already has such a cross-skill dependency (`intro-drafter` reads `paper-polish` tone files, `[n01 §2.3]`), and the library is installed as a whole (§11.4).

## 3. Shared foundation: `research-core`

### 3.1 Core rules (`references/core/`), true in every field

| File | Rule set | Main evidence |
|---|---|---|
| `claims-evidence.md` | Claim ledger; every claim has a number, scope and source (script + data/code SHA, or citation); hedge interpretations, never measured facts; "as the source describes" hedges for model-read data; novelty claims carry "to our knowledge"; speculation labelled untested | upstream `paper-writer/references/evidence-discipline.md`; humanize-paper rule; `[n06 §2.6]`; FINAL B1 |
| `body-text.md` | Anti-accretive body text: the paper says what is true now, no revision narration, no "plan predicted" voice; why before how; define each concept before use; term table with rejected readings; macros for labels | anti-accretive-docs; `comments_hao.md:1-3`, §2.2, §2.3; `[n06 §2.1, §2.2, §2.8]`; writing-shape concept-grounding rule |
| `deai.md` | Short summary of the de-AI contract and the S1–S7 diagnosis vocabulary; full method in `deai-writing` | `[n02 §10 De-AI]` |
| `feedback-loop.md` | Feedback-to-revision principles: stable IDs, one change per comment, verify against diff, never hide an unresolved reviewer note, conflicts surfaced not resolved silently | `[n05 §6]` |
| `figures.md` | Figure clarity rules that hold in every field (self-contained captions, dual encoding, names match text, one figure per message, vector, no AI-look markers, figure numbers from scripts) | upstream handbook 4.4; `[n07 A.8]` FR1–FR21 (general ones) |
| `records.md` | Records outside the paper; one writable source of truth per phase, switches recorded; dashboards are views, files are state | `[n08 §1, §5 #1, #24]` |
| `integrity.md` | Agreement numbers need raw independent label sets; held-out gold frozen before viewing model output; acceptance bars written before runs; AI use in methodology disclosed; every printed number traceable | `[n08 §5 #17–#21]`; `overlay-high14-review.md`; FINAL B1, G9 |
| `precedence.md` | Order when rules conflict: venue call > advisor/co-author decision recorded in an ADR > venue profile > field profile > core > style overlay. Checklist items beat skill suggestions (as the team's own skill README stated, `03-skills/README.md`) | `[n02 §11.1]` contradictions; `[n05 §5.4]` conflicts |

### 3.2 Field profiles (`references/fields/<field>.md`)

Fixed headings so skills can load a section by name:

```
# Field profile: <field>
Status: evidenced | partial | stub        Sources: <list with IDs>
## Paper types              (e.g. empirical study, tool, technique, theory, survey)
## Typical structure         (section skeleton, paragraph functions, lengths if evidenced)
## What reviewers and advisors care about
## Tone and phrasing         (tense, hedging, "we", number density)
## Citation norms            (e.g. DBLP-checked bib for CS venues)
## Figures and tables
## Rigor and threats         (field-specific validity, statistics, reproducibility)
## Checklist additions       (item IDs added to the shared checklists)
## Known disagreements       (where sources or venues disagree, decided per venue)
## Unknown                   ("no evidence" items; do not guess)
```

Every rule line ends with `[src: ...]`. A rule without a source is listed under "Unknown" instead.

| Profile | Status | Sources |
|---|---|---|
| `se.md` (empirical SE/MSR first) | evidenced | archive (`[n05]`, `[n06 §3]` skeleton and word counts, `[n08]`), local SE skills rules that survive the contradiction pass (`[n02 §10 SE]`), exemplar-corpus method from adams-sail (rules only, no project numbers) |
| `ai-ml.md` | partial | upstream skills and handbook (they are the AI/ML/DB evidence base, `[n01 §5.1]`), style-mine `base_rules/ml_cv_nlp.md` |
| `math.md` | partial | `paper` skill (proof-obligation rule, scaffold), style-mine `general_academic.md`; needs exemplar corpus |
| `stats.md` | stub | none in hand; Phase 4 builds it with style-mine from user-supplied exemplars |
| `causal.md` | stub | none in hand; same |
| `_template.md` | — | headings above |

Known SE decisions to record in `se.md` "Known disagreements" (resolved once, from `[n02 §11.1]`): claim-first bold sentence then figure/table sentence then digging deeper (`msr:0f96193`); explanation before numbers; no implications inside Results (implications section instead); hedge interpretations only; contribution list varies by sub-venue (style-mine decides per venue); no appendix at venues with an all-in page limit (`chat:group@2026-10-01T08:56`, `chat:group@2026-10-02T01:51`).

Style overlays (`references/fields/overlays/`): optional, per advisor or team, e.g. "no semicolons or em-dashes" (team rule `CF-23@v2`). Off by default, because blanket punctuation bans produced monotone prose (`[n02 §11.4]`). Open question Q4.

### 3.3 Venue profiles (`references/venues/<venue>.md`)

Generated by `style-mine` from the venue call plus exemplar papers; dated; each item from the call is quoted with the URL and fetch date; uncertain items marked CONFIRM. Seed: `fse.md` from `10-requirements/venue/fse-2027-requirements.md` (page limit 18+4, acmart options, double-anonymous rules, Data Availability section, AI-use policy, desk-reject causes), with the lesson that a deadline heard in a meeting is not a source (`[n04 §1.1]`).

### 3.4 Keeping `research-core` growing: new papers, new fields, expert notes

The library must get better with every paper, assignment and new field (user request 2026-10-13). Mechanism:

1. **New skill `lessons-harvest`** (21st skill). Run at milestones (after submission, after reviews, after an assignment is graded) or whenever expert notes arrive. Inputs: the project's `docs/feedback/` tables, ADRs, `docs/log/` (check-loop reports), `STATUS.md`, git history; plus **expert notes** (advisor or reviewer comments, talk notes, published writing guides, a senior's checklist). Procedure: extract candidate rules; dedupe against existing rules; attach sources; propose where each goes (core / field / venue / checklist / overlay / project-only); show the diff for approval; write on a branch `learn/<project-or-source>`; merge after the user approves.
2. **Rule lifecycle**, recorded per rule: `candidate` (one project or one expert) → `confirmed` (seen in ≥ 2 projects, or stated by a published guide or the venue) → `deprecated` (contradicted later; kept with the reason). Checklists enforce only `confirmed` items; `candidate` items are advisory.
3. **Expert notes store:** `research-core/references/experts/<field>/<source-id>.md` holds anonymized digests (roles, not names; paraphrase, short quotes only); raw notes stay in the private project or archive repo and are referenced by id.
4. **New fields:** `lessons-harvest --new-field <name>` copies `fields/_template.md`, asks for exemplar papers and expert sources, and runs `style-mine` to fill the profile (status `stub` → `partial` → `evidenced`).
5. **Versioning:** each profile and checklist carries a version and a short changelog block; the repo `CHANGELOG.md` gets one line per harvest. Our content lives in `research-core` and new skills, so upstream merges rarely touch it.

### 3.5 Templates (`assets/templates/`)

`research.yaml` (§8.2), `STATUS.md`, `TODO.md`, `adr-0000-template.md`, `log-entry.md`, `response-table.md` (feedback/rebuttal table, §4 feedback-to-revision), `guidance-record.md` (expert guidance, §4.15), `claim-ledger.md`, `runs-log.md`, `data-manifest.tsv`.

## 4. Skills one by one

Common step 0 for every skill except `research-core`: read `research.yaml` (if absent, ask or offer `research-supervisor` init), load `research-core` core rules, the active field profile and the venue profile, and the relevant checklist. Common last step: run the checklist subset named below, report pass/fail/not-applicable per item ID, and write state changes to `docs/STATUS.md` through `research-records` conventions.

### 4.1 `research-supervisor` (new, optional entry point)
- **Inputs:** `research.yaml`, `docs/STATUS.md`, `docs/TODO.md`, repo state (git log, open reviewer markers), user request.
- **Procedure:** (1) If no `research.yaml`: interview for field, venue, repos, data location, backend, records mode; write files from templates. (2) Determine stage from explicit `stage:` and signals (no draft → idea/design; runs log active → experiments; draft present → writing; markers or comments present → feedback; deadline within 7 days → submission; reviews present → rebuttal). (3) Show stage, blockers from STATUS, and the next 1–3 skills with why. (4) Hand off.
- **Checklist:** `records` items (STATUS current, SoT named, deadline from a dated source).
- **Outputs:** routing decision; initialized project files.
- **Evidence:** the project had nine stages with very different needs (`[n04 §5]` S1–S10); source of truth and deadline confusion (`[n04 §1.1, §1.5]`).
- **Worth building?** Yes, but thin (about 150 lines): with 20 skills, stage routing and project init are the main entry cost. It must never do the work itself.

### 4.2 `research-core` (new)
- **Inputs:** none directly; read by other skills.
- **Procedure (SKILL.md):** how to resolve the active field/venue; precedence (§3.1); how to cite sources; how to add a rule (needs `[src:]`); how to mark "no evidence".
- **Outputs:** none. **Checklist:** n/a.

### 4.3 `idea-evaluator` (upstream, strengthened)
- **Add:** an empirical-study route (RQ set, population and sampling frame, construct validity, data availability, threats foreseeable at design time), and a theory route (result + proof technique). Field profile supplies venue-fit criteria.
- **Evidence:** the RQ framing and frozen-corpus decisions (`[n04 §5 S1–S2]`); the coverage-wall pivot showed a design-time threat that should have been flagged early (`04-comms/20260910-zhimin-d4d5-threats/README.md`).
- **Checklist:** existing gate + `threats` design-time items.

### 4.4 `deep-research` (upstream)
No functional change. Field profiles feed its evidence standards; cite aris' "artifact per phase + fresh reviewer" idea as an optional mode (`[n02 §10 Records]`).

### 4.5 `experiment-workflow` (new)
- **Inputs:** `research.yaml` (`experiments`, `data`, `repos.research`, `repos.artifact`), research repo.
- **Procedure:**
  1. *Freeze.* Record corpus snapshot id, time window, population count, selection criteria in an ADR; never extend silently (`[n04 §5 S1]`).
  2. *Sample and gold.* Document sampling allocation and seed; build gold; freeze the held-out split before any model output is viewed; record agreement only from raw independent label sets kept in the repo.
  3. *Model/prompt versioning.* Version log with per-version agreement, rollback reason; acceptance bar written before the run and enforced by the run script (`GOLD_BAR_OK` pattern, `[n08 §5 #21–#22]`).
  4. *Disagreement → rule file.* Each annotation trap becomes a numbered rule (`[n08 §5 #23]`).
  5. *Runs log.* `docs/runs.md`: run id, command, code SHA, data version, backend, status (ran / failed / partial), outputs. Failed runs are recorded, not deleted.
  6. *Numbers to paper.* Every number in the paper comes from a script; a `numbers.json` (or equivalent) with code+data SHA; diff against the TeX before submission (`RP-11`: 42 cells exact match).
  7. *State over dashboards.* The authoritative state is a diffable file (DB export, state JSON), not a web UI (`[n08 §5 #24]`, 199 vs 582 incident).
  8. *Data placement* (§8.3) and *backend* (§8.4).
  9. *Replication artifact.* Build the anonymized package from a manifest: code that regenerates every printed number, data or download script, README; run it from a clean clone; anonymize (grep for names, paths, account names, page URLs, licence author); publish via an anonymous mirror (`[n08 §3]`).
  10. Verified results go to `docs/STATUS.md` "Verified numbers" first; only then into the paper (brief H).
- **Checklist:** `integrity`, `artifact`.
- **Outputs:** ADRs, runs log, numbers file, artifact repo.
- **Evidence:** `[n08 §2]`; `[n04 §5 S3–S5]`; integrity flags (κ = 0.74 with no computation record, first introduced in `msr:393f596` replacing a sentence that said no human–human agreement was reported; 14 gold cells changed after viewing model output, `overlay-high14-review.md`).
- **Colab/MCP:** no project evidence (`[n08 §2]`); designed from the available `colab-mcp-workflow` skill and CLI, see §8.4.

### 4.6 `paper-writer` (upstream + se-paper-writing generative parts + `paper`)
- **Add:** Phase 0 claim ledger (from `docs/STATUS.md` verified numbers and `numbers.json`); paper type from `research.yaml` selects the skeleton from the field profile (SE empirical skeleton: `[n06 §3]`); math route (definition/lemma/proof obligations from `paper`); "numbers into the manuscript before prose" (`[n08 §5 #28]`, `20260920-msritp-meeting/README.md`).
- **Remove from the SE source material:** project-specific vocabulary, the contradictions listed in `[n02 §11.1]`, punctuation bans (to overlay), and advice that pushes overclaiming (`[n02 §11.8]`).
- **Checklist:** `writing` + field additions; ends by offering `check-loop`.
- **Evidence:** why-before-how and finding-first patterns (`[n06 §2.1, §2.4]`).

### 4.7 `intro-drafter` (upstream, strengthened)
- **Add:** RQ-driven empirical intro pattern: context for an outsider → phenomenon figure → why this data source matters to the field → gap with cited assumptions → RQ blocks (bold question, one "…, so we…" why sentence, 2–3 findings) → one-sentence method → contributions → roadmap (`[n06 §3]` intro paragraph functions; `comments_hao.md` §2.1, §2.6; `CF-01@v2`, `CF-03@v2`).
- **Evidence:** advisor readability check that internal jargon blocks outsiders (`04-comms/20260926-jimmy-advisor-paper-glimpse/README.md`).

### 4.8 `tech-paper-template`, `benchmark-paper-template` (upstream)
Unchanged procedures; descriptions say "field: ai-ml/systems"; `research-supervisor` routes empirical SE, math and statistics papers elsewhere. Dedupe `paper-types.md` and `worked-examples.md` only if upstream does (avoid merge pain).

### 4.9 `style-mine` (local, strengthened)
- **Keep:** corpus-grounded dynamic style skill; never adds facts or changes technical content.
- **Add:** (1) output a venue profile (`venues/<venue>.md`) and propose additions to a field profile, each rule with the exemplar papers that support it and a consensus threshold (adams-sail method: a rule needs ≥ k of n exemplars, disagreements recorded); (2) a "methods-borrowing card" mode (from msr-tpa-rq-method-borrow); (3) a check mode used by `check-loop` round 2 that reports deviations from the dynamic skill.
- **Licence:** user-authored (decision 2026-10-12); MIT text in its README stays.
- **Evidence:** `[n02 §1]`; SE contribution-list disagreement resolved per venue (`[n02 §10 SE]`).

### 4.10 `deai-writing` (merge)
- **Spine:** deai-paper-writing S1–S7 diagnosis, claim ledger, information-gain test, "output longer than input = fail", modes diagnose / full / section / numbers / audit.
- **From avoid-ai-writing:** editing contract (candidate → finding → authorized edit; protected content), "never inject" list, tiered pattern catalog, verification block, context profiles with a new `academic` profile in which punctuation rules defer to venue and overlay.
- **From humanize-paper:** Williams' Style principles, hedge interpretations not facts, `% TODO: verify` for unverifiable superlatives, preserve plainness, minimal LaTeX diff; its comment-macro step moves to `feedback-to-revision`.
- **From upstream:** one canonical banned-word list (paper-polish `ai-tone-guardrails.md` stays canonical; pre-submission-reviewer's list merged into it).
- **Checklist:** `writing` de-AI items.
- **Evidence:** advisor "fix AI smells, e.g. `Corpus'" (`msr:0f96193`); figure palette judged "too AI" (`chat:group@2026-10-02T22:28`); `[n02 §10 De-AI]`.

### 4.11 `paper-polish` (upstream + se-paper-refinement)
- **Add:** field- and venue-aware single pass; from se-paper-refinement the reader-logic rules that survive the contradiction pass (stable analysis units, number density, comparison words, metric definitions, RQ chaining) moved to core or `se.md`; project §9 rules dropped.
- **Stays single-pass.** Multi-round work is `check-loop`.
- **Checklist:** `writing`.

### 4.12 `check-loop` (new orchestrator; see §6)

### 4.13 `figure-designer` (upstream + tikz-diagram-review + archive rules)
- **Add:** figure-mirrors-methodology rule (number the figure's boxes; one bold run-in per box in order; same names in figure and text) (`chat:group@2026-09-29T11:42`, `msr:9809b8c` todo, `msr:b5c0045`; `[n06 §2.5]`); table vs figure decision (a grid of numbers is a table, `msr:0f96193` todo → `msr:405bba7`); text → figure → table hierarchy (relayed rule C-035, verbatim source not in export, `[n04]`); legend required; colour is not the only cue; TikZ render-and-inspect loop; palette restraint; font-size floor checked after every late edit.
- **Also from the archive (`[n07 A.8]` FR1–FR21):** write Methods first and draw the overview from it (FR2); every number inside a figure comes from the same script as the text, and a number copied from a sketch, an AI image or a reference figure is a placeholder until re-sourced (FR3); AI images only for layout exploration, then native rebuild and a human redline pass (FR4); remove AI-look markers (FR5); one figure per RQ, decide instead of keeping an "alternative" (FR10); renderer, PDF, caption and preview regenerated together (FR14); one source file per figure (FR15); renderers run from the replication package (FR16).
- **Checklist:** `figures`.
- **Evidence:** the agreement value κ = 0.74 entered the paper through the figure pipeline: it first appears on a co-author's reference image (09-27), the agent-built draw.io replica copied it (its `LAYOUT_FINGERPRINT.md` says displayed values were "copied from the reference without ... validating the research"), and the commit that installed the replica (`msr:393f596`) added the same number to the Design text; the redline later removed it from the figure but not from the text (`[n07 A.1]`). Overview figure: 11+ versions in 9 days (`[n07 A.1]`).

### 4.14 `drawio-reconstruction` (upstream + drawio-figure-replication)
- **Add:** layout fingerprint, module-first build with module QA crops, SVG asset provenance (`[n02 §10 Figures]`; archive `05-figures-tables/sources/drawio/overview-reference-replica/`).
- **Icon sourcing (user request 2026-10-13).** Before tracing or inventing an icon, find a real one, in this order:
  1. draw.io built-in stencils (e.g. the GitHub logo was taken from the built-in stencil, not traced, `overview-reference-replica/LAYOUT_FINGERPRINT.md`);
  2. local icon libraries registered in `references/icon-sources.md` and located through `research.yaml` `figures.icon_libs` or env `ICON_LIBS` (no hard-coded home paths; the local skills hard-code `/Users/yitwah/...`, `[n02 §0]`): NN-Models-drawio-library (pastel NN blocks, from `nn-models-drawio-library`), BioIcons and Health Icons (from `scientific-illustration-ppt`, whose `index_assets.py` / `search_assets.py` are vendored and generalized into one icon index);
  2b. the registry is **per field** (user request 2026-10-13: "we can have more, in our research field"): each library is tagged with fields (se, ai-ml, math, stats, causal, bio, general) and kinds (logos, concept icons, NN blocks, diagrams). Phase 4 researches candidates per field with web search (for example open logo sets for software tools and platforms, general concept icon sets, draw.io stencil packs, scientific icon sets) and records each one only after reading its licence; nothing enters the registry from memory;
  3. web search for an icon repository or set when nothing local fits; clone into a cache (`~/.cache/supervisor-skills/icons/`), index it, and add it to the registry;
  4. only then draw a simple native shape.
  Every used icon gets a row in `<figure>_icons/ATTRIBUTION.tsv` (source repo, path, licence as read from the repo at fetch time, author, retrieval date); licences are read from the source, never assumed. The archive's replica already kept `SVG_ASSETS.md` provenance (`05-figures-tables/sources/drawio/overview-reference-replica/`).
- **Upstream branch `chore/sync-drawio-reconstruction`:** producer/reviewer separation with hashed PASS/FIX ledgers is valuable but regresses to hard-coded `~/.codex` paths (`[n01 §6]`). Wait for upstream to merge it; open question Q6.

### 4.15 `feedback-to-revision` (new)
- **Inputs:** comments from any channel: inline TeX macros (protocol from `research.yaml`), PDF annotations (vendored `extract_pdf_comments.py` from parse-pdf-comments), chat text, comment files, reviewer reports, agent comments; current paper source; `research.yaml` people roles.
- **Procedure:**
  1. *Ingest and ID.* `FB-<origin>-<nn>` with source pointer (file:line, commit+line, PDF page + float caption text, chat timestamp) and the paper version the commenter read.
  2. *Triage.* Type (structure, framing, terminology, claim-evidence, figure, formatting-venue, citation, anonymity, scope, page-budget), size S/M/L, needs-author-decision, duplicate-of, conflicts-with, re-raise-of, stale-version flag, image-only (needs text restatement).
  3. *Confirm.* Show the triage table; the author decides items marked needs-decision and every conflict (both positions + a compromise option). Decisions go to an ADR when they set a rule.
  4. *Apply one change per comment.* Commit message starts with the ID (`FB-B-P11: allocation table to one sentence`). Never mix with sync merges or checkpoints.
  5. *Marker lifecycle.* Agent may resolve only agent-resolvable markers; for student-only markers it drafts the fix and appends a Done note (what changed, what remains); never deletes, comments out, or hides (`\shownotesfalse`) an unresolved note.
  6. *Verify.* For each ID compare the claimed change with the actual diff; re-check after merges, because stale-base pushes and sync bots reverted verified fixes (`[n05 §5.3]`).
  7. *Page delta.* Track page effect of cuts and expansions.
  8. *Close.* Response table: ID, short quote, decision (accept / partial / decline + reason / superseded-by), change summary, location after change, commit SHA, verification status. This table becomes the rebuttal or response letter (`rebuttal-guidance`).
- **Guidance mode (user request 2026-10-13).** For expert guidance on a paper or an experiment (meeting, call, chat, email, relayed advice), write one record `docs/guidance/YYYY-MM-DD-<role>-<topic>.md` from `assets/templates/guidance-record.md`:
  - *Who and channel:* role (never a name in shared files), meeting / chat / email / relay, who relayed it.
  - *Scenario:* what we showed them (paper version or commit, figure, result, experiment state), and the question we asked.
  - *What they said:* short verbatim quotes in the original language, with timestamps.
  - *What they mean:* our interpretation, marked as interpretation; open points to clarify with them.
  - *Points to notice:* risks, red lines, assumptions they challenged.
  - *Actions:* `G-<date>-<n>` items with owner, due date or milestone, done-criterion, and links to TODO and FB IDs.
  - *Decision:* accept, partial, or decline with reason (ADR when it sets a rule).
  - *Follow-up check:* status per action (open / done with commit or run id / dropped with reason).
  `feedback-to-revision guidance-review` lists open and overdue actions and checks "done" claims against commits and runs. `research-supervisor` shows overdue guidance at session start; `lessons-harvest` reads these records. Evidence that this was missing: early meetings were only partly archived (`GAPS.md`; `[n04]`), the relayed advisor read an outdated version so one of seven points was already obsolete (`[n05 §5.1]`), and the decisive 09-10 threats pivot survived only because someone wrote `04-comms/20260910-zhimin-d4d5-threats/README.md` with decision, mechanism and "do not" list.
- **Checklist:** `master` feedback items (all IDs closed or listed open; no hidden markers; no overdue guidance actions).
- **Outputs:** `docs/feedback/<round>.md` table; commits.
- **Evidence and examples (anonymized in the skill):** 111 requests across channels, 61% verified addressed, median latency 9.5 h (`[n05 §3]`); `\hao`/`\todo` protocol and its failures (`msr:9809b8c`, `msr:815305e`, `msr:ac172bd`, `msr:5776349`; `[n05 §5.2]`); six worked examples (`[n05 §4]`).

### 4.16 `pre-submission-reviewer` (upstream + se-paper-reviewer)
- **Add sub-checklists** (§5): threats-to-validity, double-blind, artifact, venue-formatting/submission, integrity. A devil's-advocate pass (strongest counter-argument per claim) from se-paper-reviewer, with SE criteria from the field profile.
- **Add submission-day runbook:** upload a complete PDF early and replace it; one editor at a time in the last 24 h; plain-text abstract for the form; PC conflicts entered a day early; after the deadline sync the submitted version back and tag it (`[n08 §5 #3, #4, #30, #31, #40]`).
- **Rule:** run read-only one day before the deadline and turn blockers into TODOs immediately (`[n08 §5 #37]`).

### 4.17 `rebuttal-guidance` (upstream, strengthened)
- **Add:** consumes the `feedback-to-revision` table; venue-neutral formats (journal major revision letter, conference rebuttal with word limit); unfixable reviewer requests become explicit limitations in threats (from se-paper-refinement).
- **Evidence:** no reviewer reports exist yet (GAPS item 8); mark SE-specific rebuttal advice as no evidence.

### 4.18 `research-records` (merge)
See §7. Owns the `docs/` conventions, source-of-truth rules, Overleaf ↔ git sync rules, ADR procedure (confirm-before-write, ≥ 2 real alternatives, supersede chain), anti-accretive doc rewriting, optional Linear mirror.

### 4.19 `vibe-research-workflow` (upstream)
Unchanged; links to `research-records` (checkpoint before agent destructive edits; read the diffstat after any agent write to a shared document, `[n08 §5 #5, #6]`) and `experiment-workflow`.

## 5. Checklists and their links to skills

**Source material.** The project's checklists went v1 (140 one-line items) → v2 (same items, 43 ticks, machine-generated provenance, 09-29) → paper-repo `checklist.md` (~77 items, 11 revisions, 10-01 → 10-03) → `FINAL-CHECKLIST-2026-10-02.md` (27 pass, 11 fail, 34 partial) (`[n07 B.1]`). The provenance audit found that 90 of 140 v2 items carry a "Who" label that pairs Senior co-author A's name with the Student's name, 10 audited rows name the wrong person, 3 present agent output as a human comment, and 3 ticked items are contradicted by the final paper (RS-07, RS-08, RS-17) (`[n07 B.4]`). So:
- every item in our checklists is rewritten in general wording and carries a hand-verified `src:` (or `src: unverified` and is advisory only);
- ticks record evidence (a commit, a command output, a diff), not intent;
- the reusable items are already classified in `notes/07-figures-and-checklists.md` B.5 (master, writing, figures + FR1–FR21, threats, double-blind, artifact, venue-formatting, collaboration/records, experiment-integrity, field-SE) and become the seed of the files below. Project-specific items stay out (`[n07 B.5]` last list).

Planned files in `research-core/references/checklists/`, item format:

```
- [ ] WR-07 Each finding paragraph: bold claim, then a figure/table sentence, then detail.
      why: reviewers read results first   scope: field:se   owner: paper-writer, paper-polish
      src: msr:0f96193 (todo), [n06 §2.4]
```

| Checklist | Run by | Scope of items |
|---|---|---|
| `master.md` | research-supervisor, pre-submission-reviewer | index of all checklists + cross-cutting gates |
| `writing.md` | paper-writer, intro-drafter, paper-polish, deai-writing, check-loop | structure, framing, terminology, numbers, hedging, de-AI |
| `figures.md` | figure-designer, drawio-reconstruction | clarity, mirroring, table-vs-figure, fonts, palette |
| `threats.md` | idea-evaluator (design-time), pre-submission-reviewer | construct/internal/external/conclusion; data walls moved to threats |
| `double-blind.md` | pre-submission-reviewer, experiment-workflow (artifact) | PDF, sources, artifact, URLs, self-citation |
| `artifact.md` | experiment-workflow, pre-submission-reviewer | package completeness, regenerates every number, anonymized |
| `venue-submission.md` | pre-submission-reviewer | page budget, template, fonts, bib (DBLP), Data Availability, form fields, runbook |
| `integrity.md` | experiment-workflow, pre-submission-reviewer, check-loop round 1 | agreement provenance, frozen gold, pre-registered bars, AI-use disclosure, number traceability |
| `records.md` | research-records, research-supervisor | SoT named, STATUS current, ADRs for locked decisions, parked items listed |

Field profiles add items with prefixed IDs (`SE-…`, `MATH-…`).

## 6. The check loop

**Decision: a new orchestrator skill `check-loop`, not a mode inside `paper-polish`.** Reasons: the loop spans three owners (`deai-writing`, `style-mine`, `paper-polish`/`pre-submission-reviewer` rules); it needs its own state (round log, locked decisions, budget); upstream has no whole-manuscript loop with a round budget (`[n01 §4.3]`); and `paper-polish` keeps its cheap single-pass use.

**Order of checks within a round (challenge to the brief's order).** I propose research fit first, then venue/field fit, then language, because language edits made before content changes get thrown away, and content edits late in the process re-introduced defects (a duplicated sentence from `msr:ac172bd`, a doubled bold headline in the 10-04 pass, `[n06 §1]`):
1. **Research-writing fit** (field profile + `integrity` + `writing` claim items): claims within evidence, scope words, hedges on model-read data, reproducibility statements, threats coverage, numbers match `numbers.json`.
2. **Venue and field style fit** (`style-mine` check mode with the dynamic skill + venue profile): structure, section lengths vs budget, contribution format, tone, citation form.
3. **Language and de-AI** (`deai-writing` audit mode + style overlay if enabled).

**Loop control.**
- Inputs: target files or sections, `max_rounds` (default 3), locked decisions (from ADRs and the term table).
- Each round: run 1→2→3 as checks; collect findings; apply only authorized edits; record each change with check id and rule source.
- **Oscillation guard:** a span changed in round k may not be changed back in round k+1 unless a check cites a different rule; locked decisions are never flipped (the archive shows trims/restores and term flips, `[n06 §2.3, §2.8]`).
- **Regression check:** re-run round 1 after round 3 edits.
- **Stop when:** all checks pass; or a round makes no change; or oscillation detected; or budget reached. Report residual findings with IDs.
- **Output:** `docs/log/<date>-check-loop.md` (round table: check, finding, rule src, edit, diff stats) and a short summary of what changed.

## 7. Records outside the paper, and the Linear recommendation

**Per-project layout (local files are the source of truth):**

```
docs/
├── STATUS.md     current state only (replace, never append): stage; source of truth per artifact
│                 (paper: git main | Overleaf, data, numbers); verified numbers with script+SHA;
│                 runs ran/failed; blockers; parked items (\iffalse, %% PARKED); open reviewer markers;
│                 next deadline with dated source
├── TODO.md       actionable items with owner and FB/CK ids
├── adr/          NNNN-title.md: context, ≥2 alternatives, decision, consequences, supersedes
├── log/          YYYY-MM-DD-<topic>.md, append-only dated notes (meetings, check-loop reports)
├── feedback/     response tables per round (feedback-to-revision)
├── guidance/     expert guidance records with actions and follow-up (feedback-to-revision guidance mode)
└── runs.md       experiment runs log (experiment-workflow)
```

Rules: one writable source of truth per artifact and phase, switches recorded in STATUS and an ADR (the archive shows three undocumented flips in eight days, `[n08 §1.2]`); a mirror into a co-edited document must fast-forward-check or abort, never copy over (`ol:a610d1d` → `ol:214cc0c`, `chat:group@2026-10-03T19:42`); private material stays out of the shared paper repo from day one (`msr:f1c7df8` → `msr:c8adb43`); decisions are copied into the repo, never only referenced by ticket id (`[n08 §5 #35]`).

**Local-first vs Linear-first.**

| | Local-first (`docs/` + optional Linear mirror) | Linear-first |
|---|---|---|
| Agent access | Always (plain files) | Needs MCP and network |
| Diffable history | Git | Linear history, not in repo |
| Survives archiving | Yes | No: ticket ids remain in code but bodies are lost (DEM-xx in the archive, `[n08 §4]`) |
| Co-author visibility | Needs GitHub access | Good board and notifications |
| Overhead | Low | Ticket hygiene |

**Recommendation: local-first.** Linear is an optional board (`linear.enabled` in `research.yaml`): one issue per TODO or blocker, issue body links back to the `docs/` file, status flows from files to Linear, never the reverse, following research-docs-linear-lifecycle ("never two CURRENT answers").

## 8. Experiments, data and tool integration; `research.yaml`

### 8.1 Integrations
- **GitHub (`gh`):** private repos, PRs for co-author changes, Actions only for lint and build; sync bots must fast-forward-check (`[n08 §5 #2]`).
- **Overleaf:** git bridge; `research.yaml` names the source of truth; agent writes through any Overleaf MCP are followed by a diffstat check (`ol:b2ad042` −379 lines, `ol:3ae9fd3` −119 lines).
- **Linear (MCP):** optional mirror (§7).
- **Colab (CLI/MCP):** backend adapter in `experiment-workflow` using the installed `colab-mcp-workflow` skill; notebook URL and runtime recorded in the runs log. No project evidence.
- **Other MCPs:** PDF extraction (MinerU) for exemplar corpora in `style-mine`; draw.io MCP for figures; mail/chat exports as feedback inputs (read-only).

### 8.2 `research.yaml` (per project, at repo root)

```yaml
project: my-study                 # slug
field: se                         # research-core/references/fields/<field>.md
subfield: msr-empirical           # optional
venue: fse                        # research-core/references/venues/<venue>.md
venue_year: 2027
paper_type: empirical-study       # technique | benchmark | empirical-study | theory | survey | thesis
stage: writing                    # idea | design | experiments | writing | figures | internal-review | submission | rebuttal | camera-ready
deadline: {date: 2026-10-02T23:59-12:00, source: "venue call URL, fetched YYYY-MM-DD"}
review: {double_blind: true, page_budget: {body: 18, refs: 4}, appendix_allowed: false}
repos:
  paper: {url: git@github.com:org/paper.git, main_file: main.tex}
  overleaf: {git_url: <private>, sync: manual, mode: ff-only}
  research: {url: ...}
  artifact: {url: ..., anonymous_mirror: ...}
source_of_truth: {paper: git, data: research-repo, numbers: analysis/numbers.json}
data: {location: drive, manifest: data/MANIFEST.tsv, lfs_patterns: ["*.pdf", "figures/**/*.png"]}
experiments: {backend: colab, notebook: <url>, runs_log: docs/runs.md}
records: {dir: docs, linear: {enabled: false, team: , project: }}
style:
  exemplars: refs/exemplars/       # PDFs or MinerU markdown for style-mine
  dynamic_skill: .style/fse/
  overlays: []                     # e.g. [no-semicolons]
people:                            # roles only
  - {role: senior-A, comment_macro: '\hao', agent_may_resolve: true}
  - {role: student, comment_macro: '\todo', agent_may_resolve: false}
check_loop: {max_rounds: 3}
```

### 8.3 Large files, data and outputs
- In git: code, configs, manifests, small derived tables (< 5 MB), figure sources, final figure PDFs.
- Git LFS: binaries in the paper or archive repos above 5 MB (the archive already uses LFS for chat images, `MEDIA_MANIFEST.md`).
- External (Drive, Hugging Face datasets, Zenodo, object storage): raw corpora, databases, model outputs; each listed in `data/MANIFEST.tsv` (path, bytes, sha256, source, licence, how to fetch). The research repo kept its 4.5 GB data and SQLite out of git and listed it in a manifest (`11-mining-github-issue-audit/README.md`).
- Anonymized artifact: built from the manifest; large data via anonymous download link.

### 8.4 Compute backends
`local`, `colab`, `vps` (ssh), each with how to record a run (command, code SHA, data version, environment) in `docs/runs.md`.

## 9. Handbook additions (case 6.4) and the private case file

Problem: cases 6.1–6.3 are Introduction analyses built on verbatim quotes from published papers (`[n01 §1.7]`). Our paper is under double-blind review, and verbatim text, numbers or the domain fingerprint it (`[n06 §4]`).

Proposal:
- **Now:** 6.4 as a *process* case, "An empirical SE paper under deadline: co-author feedback, agents and records", in the 6.1–6.3 frame (metadata block, thinking-model paragraph, paper-type block, two-column table) but with columns "stage / what happened (paraphrased, generalized) / supervisor lesson" instead of verbatim quotes. Domain described generically ("issue trackers of a niche software ecosystem"); no numbers, titles, URLs, names. zh and en.
- **After acceptance:** optionally add the Introduction analysis in the 6.1–6.3 style.
- **Private:** `private/CASE.md` (gitignored) holds the non-anonymized mapping, real titles and links to archive evidence.
- Touch points: `README.md`, `README.en.md`, `llms.txt`, handbook 3.2/3.3 reference lists (`[n01 §1.7]`).

## 10. New skills found missing, and what to strengthen

**New (beyond the brief):** `research-core` (foundation), `experiment-workflow` (brief H made concrete), `research-records` (brief G made concrete), `check-loop` (brief E). Folded into existing skills rather than new: submission-day runbook (pre-submission-reviewer), Overleaf ↔ git sync rules (research-records), number traceability (experiment-workflow + integrity checklist), page-budget planning (feedback-to-revision + venue-submission checklist).

**Not recommended:** supervisor persona skills (e.g. one per co-author, proposed in `SUPERVISOR_SKILLS_MAPPING.md`). They would encode real people, overfit to one project, and the evidence shows co-authors disagreeing with each other (`[n05 §5.4]`). Instead: reviewer-lens checklist items with provenance, and per-project overlays.

**Strengthen upstream skills:** idea-evaluator (empirical and theory routes), paper-writer (claim ledger, field skeletons), intro-drafter (RQ-driven intro), paper-polish (field/venue awareness), pre-submission-reviewer (sub-checklists, runbook, devil's advocate), rebuttal-guidance (feedback table input), figure-designer (mirroring, table-vs-figure, TikZ loop), drawio-reconstruction (fingerprint, module QA), style-mine (profile generation with consensus threshold).

## 11. Repo mechanics

1. **Lint:** keep upstream `lint_skills.py`; add `check_checklists.py` (unique IDs, required `src:` field, owners exist). Keep `check_shared_sync.py`; the `research-core` approach avoids new shared copies.
2. **Branches:** `design` → per-skill `feat/<skill>` branches; merge to `main` after review of each group (brief §2.3).
3. **Upstream sync:** `git fetch upstream && git merge upstream/main`; our changes are mostly new skills and additive sections, so conflicts concentrate in README/CHANGELOG and the strengthened upstream skills. Record each sync in `CHANGELOG.md` under an `Upstream sync` entry.
4. **Install (Phase 5 `INSTALL.md`):** clone once; symlink each `skills/<name>` into `~/.claude/skills/`, `~/.codex/skills/`, `~/.cursor/skills/` with a small script; name clashes with existing local copies (e.g. old `se-paper-*`) handled by a `--replace` flag that backs them up.
5. **CONTRIBUTING:** amend to allow `Co-Authored-By` lines in this fork (user decision 2026-10-12) and to require `[src:]` on rules.

## 12. Decisions (2026-10-13)

Decided by the user:
- **Case 6.4:** process case now, generic domain ("a niche software ecosystem"), no paper quotes or numbers; Introduction analysis in the 6.1–6.3 style only after acceptance.
- **Field profiles now:** SE/MSR (evidenced), AI/ML, mathematics, statistics, causal inference. Statistics and causal inference stay `stub` until exemplar papers or guides are supplied; nothing is invented.
- **Expert notes:** all four sources feed `lessons-harvest` (advisor and co-author comments, reviewer reports, published writing guides, the user's own notes).
- **Old local skills:** the install script backs up and removes the old copies of merged skills (`~/.claude/skills-backup/<date>/`, same for codex and cursor).
- **drawio-reconstruction icons:** find icons through draw.io stencils, registered local libraries (NN-Models, BioIcons, Health Icons) and web search, with licence and attribution records (§4.14).
- **Growing the library:** `lessons-harvest` and the rule lifecycle (§3.4).
- Earlier: keep `Co-Authored-By` lines; local skills without LICENSE are user-authored.

Decided by Claude (user delegated: "trust yourself"), reversible:
- **Q1** `research-core` skill holds core, fields, venues, checklists, templates (not root folders).
- **Q2** Check-loop order: research fit → venue/field fit → language.
- **Q4** Punctuation bans (no semicolons, em-dashes) are an optional overlay, not an SE default.
- **Q6** Do not merge the unmerged upstream drawio branch; take it when upstream merges it, then fix its hard-coded paths.
- **Q7** `tech-paper-template` and `benchmark-paper-template` stay AI/ML-flavoured; descriptions say so.
- **Q8** Records are local-first; Linear is an optional mirror.
