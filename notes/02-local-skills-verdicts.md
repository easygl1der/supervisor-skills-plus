# 02 — Local skills audit and merge verdicts

Audit date: 2026-10-12. Scope: 27 skills under `/Users/wriseai/.claude/skills/` plus the archive folder `/Users/wriseai/Projects/supervisor-skills-msr-tpa/03-skills/`. Every file listed below was read in full (large Python scripts were read end to end; nothing in this set is a large binary or XML library). Upstream reference: the 12 skills under `skills/` in this repo (SKILL.md files skimmed for headings, frontmatter, and the de-AI and figure references).

Conventions:

- `file:line` is relative to the skill folder unless a full path is given.
- License classes: **(a)** explicit permissive license; **(b)** restrictive / forbids redistribution; **(c)** third-party source identified but no license found locally; **(d)** no provenance info found (possibly user-authored). Nothing here is guessed: when a file only hints at an origin, the hint is quoted and the class stays (c) or (d).
- Verdicts: KEEP (separate skill), MERGE INTO <target>, STRENGTHEN, RETIRE, REFERENCE-ONLY (cannot or should not vendor).

## 0. Global findings

- **No symlinks.** All 27 skills are real directories (`ls -ld`), and copies (not links) also sit in `~/.agents/skills/` and `~/.cursor/skills/`. No `.git` dir, plugin manifest, or skill lockfile with source URLs exists inside any skill folder.
- **The archive copies are identical.** `diff -rq` between `03-skills/{avoid-ai-writing,journal-adapt,se-paper-refinement,se-paper-reviewer,se-paper-writing}` and the local copies prints nothing. `03-skills/` contains: `README.md`, `adams-sail-issue-mining/`, `avoid-ai-writing/`, `journal-adapt/`, `msr-tpa-rq-method-borrow/`, `se-paper-refinement/`, `se-paper-reviewer/`, `se-paper-writing/`. `03-skills/README.md:3` calls the folder "a read-only mirror of the Cursor Agent skills", and `README.md:35` says "Last mirrored from the authors' Cursor install: 2026-10-01".
- **A foreign home directory is hard-coded in six skills:** `/Users/yitwah/...` in `parse-pdf-comments/SKILL.md:130`, `nn-models-drawio-library/SKILL.md:12`, `scientific-illustration-ppt/SKILL.md:29-38` and `scripts/index_assets.py:9`, `aris-auto-research/SKILL.md:12,20,49`, `takenotes/SKILL.md:3,12` and `:356-370`, and `paper/SKILL.md:21`. That directory does not exist on this machine. It could be the user's other machine or a collaborator's, so the paths need confirming before the skills are vendored.
- **Upstream license context.** The root `LICENSE` of this fork is CC BY-NC-SA 4.0. Individual upstream skills declare `license: CC-BY-4.0` or `CC-BY-NC-SA-4.0` in their frontmatter, and `drawio-reconstruction/LICENSE` is MIT. MIT and Apache-2.0 content can be vendored with attribution (Apache also needs a copy of the license and a statement of changes). Content in classes (c) and (d) needs its origin confirmed first.

---

## 1. Style / venue

### journal-adapt

- **Path:** `~/.claude/skills/journal-adapt/` (not a symlink; identical archive copy in `03-skills/journal-adapt/`).
- **Size:** SKILL.md 490 lines. 7 supporting files: `README.md` (78), `REPO_README.md` (236), `INSTALLATION.md` (126), and `base_rules/{general_academic,economics,ml_cv_nlp,cs_engineering}.md` (104–116 each).
- **What it does.** A two-phase, human-gated corpus-to-rules generator.
  - **Phase 1.** Collect the target venue, a primary corpus, an optional secondary corpus, optional lab exemplars, and an optional static base skill (SKILL.md:57-93). Convert PDFs one at a time with MinerU and pass each through a readability gate (:95-117). Extract one "Paper Style Card" per paper with fixed fields A–J, structure only, no quotes (:119-198). Aggregate the cards into a Style Profile with pattern/corpus-role/paper-id tables, a conflict table, and red flags (:200-267). Emit `dynamic_writing_skill.md` with priorities P1 hard-preserve, P2 target journal, P3 secondary/exemplar, P4 static base, and P5 always-remove (:269-356).
  - **Human gate** (:360-368).
  - **Phase 2.** Revise one section at a time: Round 1 diagnosis with a problem type (STYLE / JOURNAL-MISMATCH / AI-TASTE / LOGIC), severity, and a 1–5 match score; Round 2 revision; Round 3 a per-paragraph revision log with a "Rule candidate" field (:397-445). Outputs go to `<manuscript>_revised/`, including `revision_summary.md` (:447-473).
- **Strong parts to keep:**
  - "HARD RULES" (:21-28), especially rule 3, "Never paraphrase corpus papers".
  - The Paper Style Card schema (:128-196), including "I. WHAT THIS PAPER DOES NOT DO".
  - The conflict table "Corpus Signals vs Static Base Rules" (:254-261).
  - The priority stack P1–P5 (:283-313).
  - Per-paragraph revision logs with "Rule candidate" (:425-438). This is exactly the mechanism a field-profile library needs to grow.
  - The base-rule anti-pattern lists (e.g. `base_rules/general_academic.md:100-116`).
- **Weaknesses:**
  - Files it references are missing: `docs/STATIC_SKILL_RECOMMENDATIONS.md` (SKILL.md:91, README.md:31) and `examples/jeem/` (REPO_README.md:188).
  - The base-rule priority is inconsistent: `base_rules/general_academic.md:5` says "Apply these as P3 defaults" while SKILL.md:79 loads base rules as P4.
  - Style cards only describe rhetoric. There is no field for evidence/claim conventions such as threats-to-validity order or statistics reporting; adams-sail had to add these by hand.
  - Output is Markdown sections, not LaTeX edits.
- **Overlap.**
  - Upstream: none directly. paper-polish has `section-conventions.md` (static), and no upstream skill learns from a corpus.
  - Local: produced `adams-sail-issue-mining` (that skill's SKILL.md:21 says it was "Generated … from six journal-adapt Paper Style Cards"). `msr-tpa-rq-method-borrow` reuses its card idea for methods. The P5 list overlaps the de-AI word lists.
- **License:** **(a), declared but incomplete.**
  - MIT is stated in `REPO_README.md:5` (badge) and `:234-236` ("## License / MIT").
  - There is no LICENSE file, no copyright holder, and no repository URL. The only URLs are to five recommended *other* skills (`REPO_README.md:46-50`).
  - Redistribution with attribution is allowed if MIT applies, but the MIT notice requires a copyright line, so the upstream repo has to be traced first.
- **User opinion:** "good".
- **Verdict:** **KEEP + STRENGTHEN.** It becomes the generator of `fields/<field>.md` and `venues/<venue>.md` profiles.
  - Reason: it is the only skill that turns evidence (a corpus) into rules, keeps a human gate, and logs where each rule came from.
  - Strengthen by: emitting to the library's `fields/` format; adding "claim/evidence conventions" and "threats/limitations" fields to the style card; adding a method-card mode borrowed from msr-tpa-rq-method-borrow; fixing the P3/P4 inconsistency; and turning `base_rules/` into seed field profiles.

---

## 2. SE writing

### se-paper-writing

- **Path:** `~/.claude/skills/se-paper-writing/` (identical copy in `03-skills/`).
- **Size:** SKILL.md 1017 lines (55.6 KB). 0 reference files. `disable-model-invocation: true` (:9).
- **What it does.** A single long guide for TSE/TOSEM/EMSE/ICSE/FSE/ASE papers.
  - Citation hygiene (:32-69) and "Workflow 0" repository exploration (:73-119).
  - A 10-step drafting checklist (:125-136).
  - Per-section templates: abstract (:176-193), introduction (:197-219), methodology by paper type (:223-245), evaluation per RQ (:249-273), related work (:277-289), threats (:293-316).
  - Generic sentence craft from Gopen & Swan, Lipton & Steinhardt, and Perez (:352-384, :752-758).
  - A long block of results-paragraph rules mined from one empirical study of LLM evaluation harnesses (:386-750).
  - Revision discipline and punctuation bans (:762-816), venue tables (:820-864), table/figure rules (:868-895), reviewer criteria (:899-928), replication packages (:932-942), and a pre-submission checklist (:960-1017).
- **Strong parts to keep:**
  - "Terminology Consistency with Tables and Definitions", including its grep-style test (:386-395).
  - "Explicitness in Derived Quantities" (:397-404).
  - "Results Paragraphs: Organize by Finding, Not by Table Row", with the taxonomy-walk test (:428-479).
  - "Bold Topic Sentences: Claim First, Numbers Second" (:481-509).
  - The comparison-word table ("proportional to" / "consistent with" / "disproportionate", :566-578).
  - "Evidence Boundaries Across RQs" (:717-731).
  - "Severity Language: Issue vs. Failure" (:733-750).
  - Threats-to-validity categories (:293-312) and "Limitations belong in threats, not future research" (:808).
  - The "What SE Reviewers Specifically Look For" and "Common Rejection Reasons" tables (:908-928).
  - Replication-package contents (:932-942).
- **Weaknesses:** see section 9, the diagnosis. In short:
  - It contradicts itself and its sibling skills.
  - It overfits to one study, which is assumed rather than defined (S0-A codes, "harness developers", the `experiment/RQ*_summary.txt` path at :766).
  - It is mostly bans.
  - It has no evidence intake before drafting.
  - It is one 55 KB file with no progressive disclosure.
  - Its venue table is undated and unsourced (:824-840).
  - Some advice is questionable: "Cite generously: reviewers may have authored cited papers" (:287); "Avoid 'combine', 'modify', 'extend' … Use 'propose', 'develop', 'introduce'" (:384); and "frame contamination as an inevitable lifecycle issue" (:314).
- **Overlap.**
  - Upstream: paper-writer (citation verification ladder, section conventions, prose delivery), tech-paper-template (contribution and paper skeleton), intro-drafter (introduction flowchart), figure-designer (figure rules), and pre-submission-reviewer (checklist, LaTeX rules).
  - Local: se-paper-refinement (around 40% of the rules restated, some contradicted), lecture-paper-revision (abstract, intro, results, tables), adams-sail-issue-mining (SE issue-mining rhetoric), and journal-adapt `base_rules/cs_engineering.md`.
- **License:** **(d).** No license, author, URL, or "adapted from" anywhere in the file.
  - The `03-skills/README.md:3,35` mirror note says it came from "the authors' Cursor install".
  - Some generic sections cite published writing advice by name (Gopen & Swan :352, Lipton & Steinhardt :378, Perez :752), and the maxim at :328 is quoted without attribution. Where that text came from is not stated.
- **User opinion:** captures an SE-specific style worth keeping, and the writing → refinement → review structure is liked, but generated output felt poor.
- **Verdict:** **MERGE INTO paper-writer + `fields/se.md` + `checklists/se-pre-submission.md`, and retire the standalone skill.**
  - Reason: the generic 60% duplicates paper-writer, intro-drafter, figure-designer, and pre-submission-reviewer.
  - The SE-specific 40% (finding-first results, terminology-table test, issue/failure severity language, RQ evidence boundaries, threats taxonomy, replication package) belongs in an SE field profile with short good/bad pairs, stripped of the harness-study vocabulary.

### se-paper-refinement

- **Path:** `~/.claude/skills/se-paper-refinement/` (identical copy in `03-skills/`).
- **Size:** SKILL.md 508 lines (41.7 KB, very long lines). 0 references. `disable-model-invocation: true` (:10).
- **What it does.** A revision checklist distilled from one advisor's comments ("Wang's feedback reveals three core values", :15-19). Its sections are:
  - §1 banned AI patterns (:25-43).
  - §2 precision: define at first use, no vague quantifiers, no invented groupings, table-term consistency, attribution of study findings, stable analysis units (:47-116).
  - §3 logical flow: rule before exception, bold header as a sequential contract, explain before numbers, no topic bouncing, parallelism, balanced summaries, unambiguous pronouns, motivate before operation (:120-194).
  - §4 numbers: density cap, no invented causes, no implications in Results, three-layer implications, no unmeasured quantities, metric definitions (:198-280).
  - §5 structure (:284-355), §6 methodology (:359-369), §7 formatting (:373-383), §8 revision process (:387-393).
  - §9 rules specific to the SWE-Bench "Beyond the Leaderboard" paper (:397-480), and a quick checklist (:484-508).
- **Strong parts to keep. Many rules here are the best in the whole set:**
  - "2f. Attribute study findings and bound their scope" with three claim types: background, study observation, interpretation (:89-105). This is a ready-made `core/claims-match-evidence` rule.
  - "2g. Keep analysis units and labels stable" (:107-116).
  - "3a. Establish the rule before the exception" (:124-129).
  - "3b. The bold header is a sequential contract", with a two-step test (:131-149).
  - "3h. Motivate and define an operation before using it" (:182-194).
  - "4a" density cap (:200-211).
  - "4b. Interpret comparisons without inventing causes" (:213-226) and "4c. No implications in results sections" (:228-239).
  - "4d" finding → characterization → SE research connection (:241-258).
  - "4e. No unmeasured quantities" (:260-262).
  - "4f" metric definition by numerator, denominator, unit, direction, and aggregation (:264-280).
  - "5c-i. Check `\ref`/`\label` survive edits" (:307-309) and "5g. Make each RQ create the need for the next" (:348-355).
  - Inter-rater reporting (:366-367).
  - "9h" conclusion in five functions (:429-439), "9i. Revision-phase boundary", which says unfixable requests go to Threats (:441-443), the "9j" number-check table (:449), and "9m" abstract in four functions with self-labeling (:471-480).
- **Weaknesses:**
  - About a third is specific to one paper (§9, :397-480; e.g. "9g. Never merge Workflow and Reasoning" :425-427), or written in one person's voice with verbatim quotes (Wang :27-243, Bram :243; including Chinese quotations :137, :147, :243). These are privacy- and tone-sensitive if the fork is shared.
  - Mechanical punctuation bans (:33-34, :375-376).
  - "Fix every comment as requested. Do not argue — the comment's existence proves the text was unclear" (:389) conflicts with a feedback-triage loop.
  - It contradicts se-paper-writing (see section 9).
- **Overlap.**
  - Upstream: paper-polish (calibration, AI tone, section conventions) and pre-submission-reviewer (writing details, banned vocabulary).
  - Local: se-paper-writing (duplicated and contradicted rules), deai-paper-writing (restatement, closures), humanize-paper (claims match evidence), adams-sail-issue-mining (implications rules, no causal verbs).
- **License:** **(d).** Assembled by the user from advisor feedback (Wang, Bram). No license.
- **User opinion:** same as se-paper-writing.
- **Verdict:** **MERGE INTO paper-polish + `core/claims-match-evidence.md` + `fields/se.md`. Move §9 to the SWE-Bench paper's own repo.**
  - Reason: §2f, §3, and §4 are field-independent reader-logic rules that belong in `core/`, and §4d/§6 are SE-specific.
  - Personal quotes should be depersonalized into rule + rationale + example before anything is shared.

### se-paper-reviewer

- **Path:** `~/.claude/skills/se-paper-reviewer/` (identical copy in `03-skills/`).
- **Size:** SKILL.md 196 lines. 0 references. `disable-model-invocation: true` (:10).
- **What it does.** A "Devil's Advocate" reviewer that only challenges. It defines its role boundaries against other reviewers (:21-40) and gives criteria for a CRITICAL finding: foundation collapse, logic chain break, data-conclusion mismatch, stronger counter-narrative (:42-59). It then runs 8 challenge dimensions (:76-137) and outputs a 200–300-word strongest counter-argument plus CRITICAL/MAJOR/MINOR tables with locations, ignored alternatives, missing stakeholders, and observations (:152-185).
- **Strong parts to keep:** the "What Constitutes a CRITICAL Finding" criteria with non-CRITICAL examples (:42-59); "Strongest Counter-Argument" as the mandatory centerpiece (:157-158, :194); and "Specific citations: every issue must cite specific passages" (:196).
- **Weaknesses:**
  - **Nothing in it is SE-specific.** It mentions APA compliance (:40), policy and stakeholder "power structure bias" (:124-129), and "N<50" lab studies (:30).
  - It refers to agents that do not exist locally: EIC, R1/R2/R3 (:19, :36-39), `citation_compliance_agent` (:40), and "deep-research devil's_advocate_agent" (:63-72).
  - It contradicts itself. :39 says the DA does not suggest "stakeholder perspectives", yet dimension 7 (:124-129) and the output section "Missing Stakeholder Perspectives" (:178-180) require them. :19 says "only challenge", while :195 says "Acknowledge the paper's strengths".
  - It has no SE threats-to-validity lens and no checks for replication or baselines.
- **Overlap.** Upstream pre-submission-reviewer (macro-logic dimension, severity taxonomy) and idea-evaluator (fatal-flaws audit). Locally, the "9j" hostile-review instructions in se-paper-refinement (:445-449) and the "ADVERSARIAL_REVIEW.md" step in aris-auto-research (:61).
- **License:** **(d), with an external-origin caveat.** No license or author. The references to sibling agents (:19-40, :63-72) show it was lifted from a larger multi-agent reviewer suite that is not named anywhere. Trace that suite before vendoring the text verbatim.
- **Verdict:** **MERGE INTO pre-submission-reviewer** as a "devil's-advocate pass" (strongest counter-argument + CRITICAL criteria). Add SE challenges (construct/internal/external/reliability threats, baseline recency, replication) to `fields/se.md`.
  - Reason: the counter-argument mechanism is valuable, but the skill is generic and points at agents that do not exist.

---

## 3. De-AI

### avoid-ai-writing

- **Path:** `~/.claude/skills/avoid-ai-writing/` (identical copy in `03-skills/`).
- **Size:** SKILL.md 317 lines (32.6 KB). 1 reference: `references/patterns.md`, 743 lines / 106 KB. Plus `LICENSE`.
- **What it does.** A general-purpose AI-ism auditor and rewriter with three modes: rewrite, detect, and edit (:107-148).
  - An "Editing contract" (:34-105): candidate match → finding → edit only if the mode and scope authorize it; source fidelity; protected content; context and intent; voice.
  - Severity tiers P0/P1/P2 (:154-196).
  - Output contract with Verification (passes, checks, residuals, stop reason) (:220-280), and tone calibration plus a "Never inject these" list (:284-317).
  - `patterns.md` holds tiered word tables (Tier 1A frequency markers vs 1B clarity edits, :35-121; Tier 2 cluster, :122-167; Tier 3 density, :169-204), about 70 named pattern entries (:215-606), context profiles with a tolerance matrix (:610-687), and voice profiles (:692-712).
- **Strong parts to keep:**
  - The "Editing contract" (:34-105). It is the most rigorous non-fabrication rule set in the whole inventory.
  - "Never inject these" (:301-317), especially "Invented specifics … a fabricated specific is worse than the vague phrasing it replaced" (:313).
  - The Tier 1A/1B split, which keeps wordiness from being read as AI evidence (`patterns.md:37-45`).
  - "Treadmill effect" (`patterns.md:600-602`) and "Paragraph-reshuffle immunity" (`:596-598`).
  - "Over-polishing" (`patterns.md:586`).
  - The context tolerance matrix as a design pattern (`patterns.md:638-673`).
  - The Verification block format (:236-242).
- **Weaknesses:**
  - **There is no academic or paper context profile.** The profiles are linkedin, blog, technical-blog, investor-email, docs, and casual (`patterns.md:614-621`), and many entries target crypto/web3 or social copy (`:189-204`, `:403-438`).
  - Bundled tools it calls are absent locally: `scripts/normalize-quotes.js` (:137), `scripts/check-style.js` and `examples/` (:212), and `detector/validate.js` (:275). Every run must therefore report "model-only".
  - It is very long and procedurally heavy for a paper pass.
  - Its em-dash rule ("Target: zero", `patterns.md:10`) clashes with LaTeX `---` conventions, which humanize-paper protects (:34).
- **Overlap.** Upstream paper-polish `references/ai-tone-guardrails.md` (a shorter list of the same signals) and pre-submission-reviewer `references/forbidden-patterns.md` §2. Locally deai-paper-writing S7 (word list), humanize-paper principle 2, se-paper-refinement §1, and journal-adapt P5.
- **License:** **(a) MIT.** `LICENSE` reads "Copyright (c) 2026 Conor Bronsdon", and the frontmatter has `license: MIT`, `author: Conor Bronsdon`, `repository: https://github.com/conorbronsdon/avoid-ai-writing` (:5-9). Redistribution with attribution is allowed.
  - It credits its own sources: `blader/humanizer` (:295, `patterns.md:18` etc.), `brandonwise/humanizer` (`patterns.md:27`), `isatimur/de-slop` (:315), `welttowelt/stop-slop-refined`, `Aboudjem/humanizer-skill`, tropes.fyi, and Simon Willison's LLM cliché highlighter. Their licenses were not checked here, so keep the credits intact when vendoring.
- **Verdict:** **MERGE INTO the unified de-AI skill** as `references/patterns-general.md`, plus the editing contract and verification format.
  - Reason: it has the best detection catalog and editing guardrails but no paper profile, and it lacks the structural (claim-level) layer that deai-paper-writing has.

### deai-paper-writing

- **Path:** `~/.claude/skills/deai-paper-writing/`.
- **Size:** SKILL.md 50 lines. 1 kit file: `deai-paper-writing-prompt-kit.md`, 575 lines / 32.8 KB.
- **What it does.**
  - SKILL.md routes through the kit in order: CORE → TASK A (diagnose) → B (full pass) or C (one section) → D (numbers) → E (audit only on request) (SKILL.md:17-25). It restates hard constraints (:27-34) and adds rules for one manuscript (mining-github-issue / MSR4ITP: locked abstract and intro paragraphs, census N=23671 vs gold N=582) (:36-46).
  - The kit defines seven syndromes: S1 over-closed narrative loop, S2 restatement redundancy, S3 preemptive defensiveness, S4 missing storyline / experiment dumping, S5 reporting hygiene, S6 padding, S7 surface style (kit:67-187). It also gives the reasons LLM drafts look like this, with operational tests (information-gain test, asymmetry test) (:189-201), and three principles (:203-211).
  - TASK A outputs a claim ledger, a closure map, a defensiveness inventory, a density and spine audit, and surface counts (:216-266).
  - TASK B is a structure-first five-pass rewrite with a change log, statistics, and open `[AUTHOR: ...]` items (:270-340).
  - TASK C gives per-section contracts (:344-415), TASK D numbers hygiene (:419-460), and TASK E a scored audit with five tests and a gate (:464-504).
  - It ends with §7 a manual human-voice checklist (:508-529), §8 guardrails (:533-556), and §9 limits (:560-575).
- **Strong parts to keep. Nearly all of it:**
  - S1–S7 as a structural diagnosis vocabulary.
  - The "claim ledger" with one canonical location per claim (:92-97, :226-233). This also serves claims-match-evidence and anti-accretion.
  - The information-gain test (:191-196) and the asymmetry test (:197-201).
  - "If your output is longer than the input, you have failed" (:47-48).
  - S3's rule for when to keep an anticipated objection (:108-112).
  - PRIMARY / SUPPORTING / DUE DILIGENCE experiment ranking (:121-125).
  - TASK D "Precision follows variance" (:430-433) and "Comparison integrity" (:448-450).
  - TASK E tests: topic-sentence, movability, asymmetry, falsifier, deletion (:484-496).
  - §8 guardrails, e.g. "removes statistical analysis rather than relocating it" (:542) and "makes prose informal to sound human" (:547).
  - §7, which names what only the author can add (:508-529).
- **Weaknesses:**
  - The kit is framed for ML venues ("NeurIPS / ICML / ICLR / AAAI / ACL", kit:33-34), and SE conventions such as threats sections and RQ boxes are not mentioned.
  - SKILL.md:15 points to `~/.cursor/skills/...` rather than the co-located file.
  - The project block (:36-46) belongs in the project repo.
  - The S7 em-dash and "Specifically," rules may conflict with venue style.
  - It has no context or voice profile.
- **Overlap.** Upstream paper-polish (AI-tone removal, calibration, overclaiming) and pre-submission-reviewer (banned vocabulary). Locally avoid-ai-writing (S7 overlaps its word tiers), humanize-paper, se-paper-refinement §1/§5c (redundancy), and journal-adapt P5.
- **License:** **(d).** No author, license, or URL. The kit says only "Built from reviewer-side observations" (kit:4).
- **User opinion:** "good".
- **Verdict:** **MERGE INTO the unified de-AI skill as its core** (CORE block + tasks A–E + §7–§9).
  - Reason: it is the only de-AI skill that works at the level of claims and structure (redundancy, defensiveness, symmetry, reporting hygiene), which is what reviewers notice in papers.
  - Generalize "ML venue" to field-neutral wording with per-field notes, and move the MSR4ITP block out.

### humanize-paper

- **Path:** `~/.claude/skills/humanize-paper/`.
- **Size:** SKILL.md 38 lines (4.4 KB). 0 references. `disable-model-invocation: true` (:9).
- **What it actually does.** It is a short principles prompt for a single in-place editing pass over a LaTeX or Markdown manuscript "Senior A is an author of" (:14). The steps are:
  1. **Resolve the author's inline comments first.** Treat `\h{...}`, `\noteA{...}`, `% <A>:`, and `% TODO` as editing instructions. Address the intent rather than only the marked phrase, apply the fix everywhere the issue recurs (including abstract and intro), keep one name per object, then remove the markers and check for leftovers (:20-22).
  2. **Apply five principles** (:24-30):
     - Williams' *Style*: characters as subjects, actions as verbs, stress at the sentence end; one point per paragraph stated early.
     - "De-AI by intent, not by checklist": cut contrast scaffolding, cleft openers, semicolons and stacked colons, adjective triads, dramatizing adverbs, figurative idioms; vary sentence length.
     - Claims match evidence: drop unearned evaluative adjectives, hedge interpretations but never measured facts, and turn any unverifiable "first to X" / "outperforms all Y" into `% TODO: verify`.
     - Preserve voice, including its plainness, but fix real grammar errors.
     - "A paper defends; a review hedges": do not import softening moves from a sibling `humanize-review` skill. That skill is not installed anywhere on this machine.
  3. **Mechanics** (:32-34): leave LaTeX untouched (math, `\cite`, `\ref`, `\label`, macros, `~\cite`, `--`/`---`), keep one-sentence-per-line, edit only the sentences that change, and leave `% TODO` instead of inventing.
  4. **Output** (:36-38): a file edited in place, a few-sentence summary grouped by principle, and a list of the TODOs left.

  There are no word lists, no examples, no detection catalog, no scripts, and no verification step beyond the summary.
- **Strong parts to keep:**
  - The inline-comment resolution protocol (:20-22), which is a seed for the feedback-to-revision skill.
  - "The one diagnosis": test whether each sentence does one job plainly (:16-18).
  - "Hedge interpretations, never measured facts" (:28).
  - `% TODO: verify` for unverifiable superlatives (:28).
  - "A paper defends; a review hedges" (:30).
  - "Preserve the voice, including its plainness" (:29).
  - Minimal-diff mechanics (:34).
- **Weaknesses:**
  - It is tied to a named third party ("Senior A", :14, :20, :28-29, :38) and his macros.
  - It depends on a missing sibling skill (`humanize-review`, :30).
  - Its bans have no thresholds or examples, so outcomes vary with the model.
  - "semicolons and stacked colons" are listed as AI tells (:27). The same blanket ban appears in se-paper-* and contributes to the monotone output described in section 9.
- **Overlap.** Upstream paper-polish (polish faithful to meaning, AI-tone removal, calibration). Locally deai-paper-writing, avoid-ai-writing, se-paper-refinement §1, and the inline-comment workflow of collaborative-review-notes.
- **License:** **(d).** No license or source. It was written for a specific author ("Senior A"), so it was probably copied from that person's skill set; confirm before redistributing.
- **Verdict:** **MERGE INTO the unified de-AI skill** (principles 1, 3, 4, 5 become `core/` voice and calibration rules). The inline-comment protocol goes to the new feedback-to-revision skill.
  - Reason: it adds no unique detection; its value is the short set of principles and the comment-resolution step, both of which fit better elsewhere.

---

## 4. Comments / review

### parse-pdf-comments

- **Path:** `~/.claude/skills/parse-pdf-comments/`.
- **Size:** SKILL.md 167 lines. 1 script: `scripts/extract_pdf_comments.py`, 247 lines.
- **What it does.** Uses PyMuPDF to extract every PDF annotation into one Markdown file per page plus a `README.md` index. Each record has `Nearby` (8 words before and after, with `[ENCLOSED]` as placeholder), `Enclosed` (words overlapping the highlight quads), and `Comment` (the annotation content, or `to be deleted` if empty) (SKILL.md:15-21, :42-73).
  - Sticky, free-text, and ink notes get the nearest 8 words as their target (script:106-117, :176-179).
  - Quality checks: the record count equals the annotation count, and every record has all three fields (SKILL.md:143-151).
- **Strong parts to keep:**
  - The three-field record that keeps "Enclosed" and "Comment" separate ("Never infer enclosed text from the reviewer comment", :100).
  - The "Comment: to be deleted" convention for empty strikeouts (:19, :60-64).
  - Page-scoped output and a count-reconciliation check (:145).
  - The extraction priority order (:92-100).
- **Weaknesses:**
  - Hard-coded `/Users/yitwah/.codex/skills/...` path (:130).
  - The script has an unused `get_enclosed_text` (script:35-77); the main loop duplicates its logic.
  - Rule 5 (try the full annotation rectangle and choose the most coherent text, SKILL.md:98) is not implemented.
  - Reply threads (in-reply-to) and annotation dates are not captured.
  - It produces no classification or triage (that is out of scope here but needed downstream).
- **Overlap.** No upstream skill parses PDF comments; rebuttal-guidance starts from pasted reviewer text. Locally it is the input stage for collaborative-review-notes.
- **License:** **(d).**
- **Verdict:** **KEEP as a tool (STRENGTHEN)** under the new feedback-to-revision skill (`scripts/`).
  - Reason: it is the deterministic ingestion step for PDF review rounds. Fix the path, remove the dead code, and add reply threads and dates.

### collaborative-review-notes

- **Path:** `~/.claude/skills/collaborative-review-notes/`.
- **Size:** SKILL.md 140 lines. 1 reference (`references/example-entry.md`, 28 lines), 1 script (`scripts/copy_review_image.py`, 87 lines), and `agents/openai.yaml`.
- **What it does.** Turns informal review input (screenshots, PDF notes, short Chinese remarks, attached `.md` explanations) into an append-only review log with stable IDs (`R007`). Each entry records status, priority, location (PDF, source, page/theorem, text anchor), related material (Obsidian image embed, supporting note), the user's intent, the problem, why it matters, a suggested fix, an "execution hint for collaborator's Codex", and acceptance criteria (SKILL.md:70-101).
  - Images are copied into `images/` (script). Optionally it commits and pushes (:65-68).
- **Strong parts to keep:**
  - The entry template, especially "用户原意" (user intent), "验收标准" (acceptance criteria), and "给合作者 Codex 的执行提示" (execution hint for a collaborator's agent) (:89-100).
  - "Append, do not overwrite"; update status instead of deleting (:60-63).
  - "Preserve uncertainty explicitly … inferred from screenshot" (:108).
  - The comment taxonomy for math or proof notes (:109-115).
- **Weaknesses:**
  - The template is in Chinese only.
  - It is Obsidian-specific (`![[...]]`) and tied to the quantum-schubert project (:119-130).
  - `slugify` lowercases the prefix (script:12-16), so `R007-…` becomes `r007-…`, contradicting the naming convention (SKILL.md:27).
  - It has no link to the revision step (who closes an item, and which diff fixed it).
- **Overlap.** Upstream rebuttal-guidance (concern inventory and classification, R?.W? IDs). Locally parse-pdf-comments (input), humanize-paper inline comments, se-paper-refinement §8 revision process, and anti-accretive-docs/ADR (append-only history).
- **License:** **(d).**
- **Verdict:** **MERGE INTO the new feedback-to-revision skill** as its ledger format.
  - Reason: the entry schema (intent, problem, why, fix, acceptance) is the missing link between "comments" and "revision". Make it bilingual and field-neutral, and add "resolved-by commit/diff" and "declined (reason)" states.

### lecture-paper-revision

- **Path:** `~/.claude/skills/lecture-paper-revision/`.
- **Size:** SKILL.md 49 lines. 1 reference: `reference.md`, 127 lines. `disable-model-invocation: true` (:10).
- **What it does.** Revises a draft in a fixed order (title → abstract → intro → related work → method → results → threats → conclusion → references → figures and tables) following rules transcribed from a lecture deck (SKILL.md:21-34), then a style pass on every edited paragraph (:36-45).
  - Concrete targets: abstract 150–200 words in seven sentences (:26), a six-paragraph introduction (:27), 3–4 related but non-dependent RQs (:30), one finding per paragraph with a bold first sentence, and a takeaway box after each RQ (:30).
- **Strong parts to keep:**
  - "A good RQ cannot be answered yes or no, and you already know which figure or table answers it" (reference.md:91).
  - "Related, not dependent" RQs (reference.md:89).
  - "Do not put more than three nouns back to back" (reference.md:20).
  - "Do not change what a box or an arrow means between figures" (reference.md:32) and "component titles use the same words as the subsection headings" (reference.md:33).
  - "One decimal precision for the column" (reference.md:49).
  - The review anatomy (reference.md:123).
  - LaTeX label hygiene ("do not tie a label to the current layout", reference.md:127).
- **Weaknesses:**
  - "Second sentence points at a figure or table" (reference.md:97) conflicts with se-paper-refinement 4c, which cuts pure pointer sentences (:237).
  - The takeaway box "says how the findings affect developers" (reference.md:103) conflicts with refinement 4d ("not just product advice", :241-258).
  - "Cite work that likely reviewers wrote" (reference.md:81) is gaming advice.
  - The Drive file ID is embedded (SKILL.md:15).
- **Overlap.** Upstream intro-drafter, figure-designer, and pre-submission-reviewer (LaTeX rules). Locally se-paper-writing (abstract, intro, tables) and adams-sail (takeaway boxes, Motivation → Approach → Findings).
- **License:** **(c).** The source is named: `lecture2_reading_writing.pdf`, pages 11–58, Drive file `12lhS7fSs39JWfjBp-sH3H1iwHX5YhgEO` (SKILL.md:15; reference.md:3, "Transcribed from …"). No author or license is given, and the lecturer is not named.
- **Verdict:** **REFERENCE-ONLY for `reference.md`; MERGE paraphrased rules into `fields/se.md` and `checklists/`**, with provenance "lecture deck, pages 11–58, transcribed".
  - Reason: a near-verbatim transcription of a third-party lecture cannot be redistributed without permission. The individual rules (facts and ideas) can be restated with credit.

---

## 5. Figures

### drawio-figure-replication

- **Path:** `~/.claude/skills/drawio-figure-replication/`.
- **Size:** SKILL.md 91 lines. 1 reference: `references/drawio-xml-patterns.md`, 91 lines. Plus `agents/openai.yaml`.
- **What it does.** Recreates a reference image as an editable `.drawio`:
  - Create an isolated output folder with `svg/`, the `.drawio`, a PNG, and `SVG_ASSETS.md` (:16-19).
  - Write a "layout fingerprint" (canvas size, regions, coordinates, node count, connectors) and, for dense figures, a module map (:21-26).
  - Build module by module with per-module QA crops or contact sheets (:28-33).
  - Make SVG icons first (:35-39), generate uncompressed mxGraph XML (:41-46), validate with `xmllint` and export with the draw.io CLI (:54-63), then compare visually and iterate (:65-69).
- **Strong parts to keep:** the "layout fingerprint" (:24); "module-first replication" with QA crops as the primary review surface (:28-33); `SVG_ASSETS.md` recording whether each asset is original, generic, or derived (:39); "Do not trace protected logos" (:38); and the minimal XML patterns (reference file).
- **Weaknesses:** it is a subset of upstream drawio-reconstruction (which has a fidelity contract, crop scripts, `check_drawio.py`, batch mode) and has no scripts of its own. Its default output location `~/Downloads/...` (:17) is not a project path.
- **Overlap.** Upstream **drawio-reconstruction** (near-complete overlap) and figure-designer (tool choice). Locally nn-models-drawio-library, which points to it (:26).
- **License:** **(d).**
- **Verdict:** **MERGE INTO drawio-reconstruction.** Add "layout fingerprint", "module map + module QA crops", and `SVG_ASSETS.md` provenance if they are missing there.
  - Reason: same task; the upstream skill has the scripts and the verification.

### drawio-architecture

- **Path:** `~/.claude/skills/drawio-architecture/`.
- **Size:** SKILL.md 63 lines. `LICENSE.txt` (202 lines, Apache-2.0).
- **What it does.** Generic guidance for architecture, C4, UML, and cloud diagrams in the draw.io GUI: pick a template, add shapes, label arrows, add a legend, export (:18-24). One C4 XML example (:28-45) and five best practices (:53-59).
- **Strong parts to keep:** "Add a legend" and "Layer complex systems … C4 levels" (:55-58). That is all.
- **Weaknesses:**
  - The XML example uses typographic quotes (`id=”0”`, :31-42), so it is **invalid XML** if copied.
  - It is GUI-oriented ("Format > Layout"), not aimed at paper figures, and has no verification.
- **Overlap.** Upstream figure-designer (`references/solution-overview.md`, `tools.md` §4 draw.io). Locally drawio-flowchart (same template).
- **License:** **(a) Apache-2.0.** `license: Complete terms in LICENSE.txt` (:4). The copyright line in the appendix is the unfilled template "Copyright [yyyy] [name of copyright owner]". The origin is not named.
- **Verdict:** **RETIRE** (optionally fold "legend" and "one diagram, one topic" into figure-designer's rules).
  - Reason: generic, GUI-centric, broken example, and nothing a paper figure needs that figure-designer lacks.

### drawio-flowchart

- **Path:** `~/.claude/skills/drawio-flowchart/`.
- **Size:** SKILL.md 71 lines. `LICENSE.txt` (Apache-2.0, identical to drawio-architecture except for a trailing newline).
- **What it does.** Generic flowchart and swimlane steps in the draw.io GUI (:17-23), an order-processing XML example (:27-52), and five best practices (:61-67).
- **Strong parts to keep:** "Label decision branches" and "Consistent flow direction" (:63-65).
- **Weaknesses:** generic and business-process oriented; the example edges have no style or arrow settings; no verification.
- **Overlap.** Upstream figure-designer. Locally drawio-architecture.
- **License:** **(a) Apache-2.0**, same caveats as drawio-architecture.
- **Verdict:** **RETIRE.**
  - Reason: same as drawio-architecture; nothing paper-specific.

### nn-models-drawio-library

- **Path:** `~/.claude/skills/nn-models-drawio-library/`.
- **Size:** SKILL.md 33 lines. 0 other files, so there is **no asset library inside the skill**.
- **What it does.** Points at a clone of "HuanPP NN-Models-drawio-library" at `/Users/yitwah/Projects/mining-github-issue/references/drawio-skills/NN-Models-drawio-library/` (:3, :12). Open `nn_model_library.xml` as a draw.io library and reuse its pastel IEEE-style blocks (:14-33).
- **Strong parts to keep:** the "When NOT to use" boundary (:24-27), and the advice to compose panels from native rectangles and use the library only for iconographic modules (:33).
- **Weaknesses:** the referenced library is **not present on this machine** (`find /Users/wriseai -name nn_model_library.xml` finds nothing). The skill is only a pointer.
- **Overlap.** Upstream figure-designer `solution-overview.md`. Locally drawio-figure-replication.
- **License:** **(c).** The third-party source is named ("HuanPP NN-Models-drawio-library", :3), but there is no URL or license and the asset is absent, so its license cannot be checked.
- **Verdict:** **REFERENCE-ONLY.** Keep a one-line entry in figure-designer `references/tools.md` ("NN block library: HuanPP NN-Models-drawio-library — check license before bundling").
  - Reason: no content to vendor, and the library's license is unknown.

### scientific-illustration-ppt

- **Path:** `~/.claude/skills/scientific-illustration-ppt/`.
- **Size:** SKILL.md 97 lines. 1 reference (`references/asset_sources.md`, 30 lines). 3 scripts: `index_assets.py` (361), `search_assets.py` (406), `check_search_quality.py` (93).
- **What it does.** Indexes local BioIcons and Health Icons repos into a JSONL index. Each record carries license, author, source repo, attribution string, and a hand-built scientific taxonomy (`index_assets.py:12-95`, :154-278).
  - Keyword search with synonyms (including Chinese), weak terms, organ-specific penalties, deduplication, and an optional HTML contact sheet (`search_assets.py`).
  - Smoke-test queries (`check_search_quality.py:9-29`).
  - License-aware selection heuristics (SKILL.md:73-80).
- **Strong parts to keep:** per-asset attribution fields carried through to slides ("Preserve license/source/author fields so later PPT pages can carry attribution", :19); "Prefer CC0/MIT/BSD when the slide should be attribution-light" (:79); and "Do not claim RAG is ready unless …" (:22).
- **Weaknesses:**
  - Biomedical-only.
  - Hard-coded `/Users/yitwah/Projects/biomedical-image-ppt-illustration-project` (SKILL.md:29-38, `references/asset_sources.md:7,22`, `index_assets.py:9`). That project is not on this machine.
  - Step numbering repeats "5." (:63, :71).
- **Overlap.** Upstream figure-designer (`tools.md`) has no asset search. No local overlap.
- **License:** **(d)** for the skill. The assets it indexes come from third parties: BioIcons, with per-icon licenses read from metadata (`index_assets.py:219`), and Health Icons, treated as CC0 per its README (`references/asset_sources.md:30`).
- **Verdict:** **REFERENCE-ONLY / keep outside the library** as an optional domain tool. Borrow the "asset attribution record" pattern into figure-designer.
  - Reason: it is out of scope for a general research-writing library, and its paths are machine-specific.

### tikz-diagram-review

- **Path:** `~/.claude/skills/tikz-diagram-review/`.
- **Size:** SKILL.md 95 lines. 1 script: `scripts/render_tikz.py`, 106 lines.
- **What it does.** Develops TikZ figures in an isolated `tikz/{figures,wrappers,rendered,review}/` workspace (:12-39).
  - State the figure's purpose in one sentence (:43-44).
  - Render a standalone wrapper with `latexmk -xelatex` plus `pdftoppm` (script:7-16, :55-72).
  - Inspect the PNG for overlaps, symbol and prose agreement, colour-only cues, and readability (:57-64).
  - Write a review note (script:74-97), then `\input` the stable figure (:74).
- **Strong parts to keep:** the "Core rule: do not iterate on a large manuscript just to check a TikZ figure" (:10-18); "A TikZ figure is not done when it compiles. It is done when the rendered image is checked" (:90-95); "color is not the only cue" (:62); and the one-sentence purpose (:43).
- **Weaknesses:**
  - The wrapper preamble is fixed (`ctex`, amsmath, a few TikZ libraries; script:7-16), so figures that use manuscript macros fail.
  - It requires XeLaTeX and ctex.
  - It assumes cwd is the project root (script:35).
  - The `~/.codex/...` path (:54).
- **Overlap.** Upstream figure-designer (rule audit, `tools.md` §6 TikZ). No local overlap.
- **License:** **(d).**
- **Verdict:** **MERGE INTO figure-designer** as a "render-and-inspect loop" reference plus `scripts/render_tikz.py`, with an option to load the manuscript preamble.
  - Reason: it applies the figure-clarity rule mechanically, and figure-designer has no render loop.

---

## 6. Records / process

### anti-accretive-docs

- **Path:** `~/.claude/skills/anti-accretive-docs/`.
- **Size:** SKILL.md 66 lines. 2 reference copies (`references-brian-bell-docs.md`, 88 lines; `references-brian-bell-improve-docs.md`, 57 lines) and `HOUSE_NOTES.md` (4 lines).
- **What it does.** Rewrites project documentation without layering corrections.
  - **Hard rules** (:15-21): docs-only edits; source or CURRENT index is the source of truth; replace, do not append; history goes to git, changelog, ADR, notes, or archive.
  - **Pass A** accuracy sync (:23-28), **Pass B** one job per doc (:30-38), **Pass C** an anti-accretion prose check with the test "would a reader who never saw the old version notice a hole?" (:40-47), **Pass D** supersede via ADR (:49-54), then a checklist (:56-62).
- **Strong parts to keep:**
  - "Replace, do not append corrections. Final CURRENT prose must read as if it were always correct" (:19).
  - The "never saw the old version" test (:45).
  - The exception list of documents that may narrate history: ADR, changelog, methodology, research log, archive (:47).
  - The research split of CURRENT index vs notes scratch vs adr vs archive (:36).
- **Weaknesses:** it targets repo docs, not paper prose. The anti-accretive *body-text* rule for papers ("no revision narration in the manuscript") has to be restated in `core/`.
- **Overlap.** No upstream skill covers records. Locally ADR and research-docs-linear-lifecycle (the same trio, which cross-reference each other), and deai S2 (restatement).
- **License:** **(c).**
  - Third-party sources are named: "brian-bell docs + improve-docs", "JoshKarpel durable-docs", and "AgDR/ECC" (:9-10, :13, :49; `HOUSE_NOTES.md:2-4`), plus a URL to justindfuller.com on accretive editing (:19).
  - The two `references-brian-bell-*.md` files are full copies of third-party skills (they carry their own frontmatter, `name: docs` / `name: improve-docs`), and no license is included.
- **Verdict:** **KEEP** as the `core/` records skill.
  - Do not vendor the two brian-bell reference copies until their license is confirmed; cite them by name instead.
  - Reason: it is the library's anti-accretion rule for records, and its Pass C applies directly to the "records outside the paper" principle.

### architecture-decision-records

- **Path:** `~/.claude/skills/architecture-decision-records/`.
- **Size:** SKILL.md 106 lines. `HOUSE_NOTES.md` (4 lines).
- **What it does.** Nygard-style ADRs in `docs/adr/NNNN-*.md`, with a Y-statement, a mandatory "because" in the Decision, ≥2 real alternatives, consequences, and an index table (:29-95).
  - Draft first and write only after explicit approval (:72).
  - Never edit an accepted ADR; supersede it (:99-101).
  - Optional Linear field (:103-106).
  - Explicit rules for when *not* to write an ADR (:27).
- **Strong parts to keep:** "Present draft → write only after explicit approval" (:72); "document ≥2 real alternatives (no strawmen)" (:70); supersede, never rewrite (:101); "Do not ADR" boundaries (:27).
- **Weaknesses:** the examples lean toward engineering. Research-specific triggers (gold freeze, sampling design) are mentioned only in passing (:7, :23).
- **Overlap.** No upstream equivalent. Locally anti-accretive-docs (Pass D), research-docs-linear-lifecycle, and takenotes' `decision` type (`takenotes/SKILL.md:119-124, :271`).
- **License:** **(c).** "Primary base: affaan-m/ECC `architecture-decision-records`" (:13) with "AgDR-inspired" additions (:16). No license or URL is present locally.
- **Verdict:** **KEEP.**
  - Reason: research decisions (codebook, sampling, gold freeze) need a supersede chain, and nothing upstream provides one. Confirm the ECC license before vendoring the text verbatim.

### research-docs-linear-lifecycle

- **Path:** `~/.claude/skills/research-docs-linear-lifecycle/`.
- **Size:** SKILL.md 63 lines.
- **What it does.**
  - A role table: the Linear issue holds status and links only, `docs/README` is CURRENT, `docs/adr` records why, `docs/notes` is scratch that must expire, and `archive/` holds superseded material (:14-22).
  - A Linear description template with three links: CURRENT, ADR, Note (:24-32).
  - Steps for opening and concluding a branch of work: promote to CURRENT, ADR, mark the note superseded (:34-52).
  - Triage (:54-56) and anti-patterns (:58-63).
- **Strong parts to keep:** "Never maintain two CURRENT answers for the same question" (:56); notes "allowed to be dirty; must expire" (:21); the `status: scratch|superseded` frontmatter (:38-44); and "Comments: short check results and blockers only — no full research report paste" (:32).
- **Weaknesses:** it requires Linear, which the plan wants optional. The project-specific "mining-github-issue" mention (:62) should go.
- **Overlap.** Locally anti-accretive-docs and ADR. Upstream vibe-research-workflow (behaviour guidelines) partially.
- **License:** **(d).** It appears to be a house composition: there are no external references beyond sibling skills.
- **Verdict:** **MERGE INTO anti-accretive-docs** (or a small `records` skill) as "notes → CURRENT → ADR lifecycle". Rewrite the Linear section as an optional adapter and make `docs/STATUS.md` the default status board.
  - Reason: the lifecycle is the valuable part, and the Linear coupling should be optional.

### linear

- **Path:** `~/.claude/skills/linear/`.
- **Size:** SKILL.md 87 lines. `LICENSE.txt` (Apache-2.0), `agents/openai.yaml`, and `assets/linear-small.svg` and `assets/linear.png`.
- **What it does.** A generic Linear MCP workflow: set up the MCP via `codex mcp add` (:22-38), clarify scope, pick a workflow, run read-then-write tool batches, and summarize (:40-53). It lists the tool names (:55-61) and gives example workflows such as sprint planning and triage (:63-73).
- **Strong parts to keep:** "Read first … Create or update next … For bulk operations, explain the grouping logic before applying changes" (:47-50).
- **Weaknesses:** it is not research-specific and its setup is Codex-specific. This environment already exposes Linear MCP tools directly.
- **Overlap.** Locally research-docs-linear-lifecycle. No upstream equivalent.
- **License:** **(a) Apache-2.0** (`LICENSE.txt`; copyright holder line unfilled; origin not named in any file).
- **Verdict:** **RETIRE from the library.** It can stay installed as a general tool.
  - Reason: Linear is optional in the plan, and this skill contains no research-records logic.

### aris-auto-research

- **Path:** `~/.claude/skills/aris-auto-research/`.
- **Size:** SKILL.md 64 lines. 1 reference (`references/general-aris-loop.md`, 40 lines). Plus `agents/openai.yaml`.
- **What it does.** An entry point to an external "ARIS" repo at `/Users/yitwah/Projects/Auto-claude-code-research-in-sleep` (:10-12, :20, :49). That repo is **not present on this machine**.
  - For academic tasks it routes to the repo's skills (`research-pipeline`, `auto-review-loop`, `research-lit`, :25-34).
  - For general research it runs a five-step loop: plan → gather → draft → adversarial review → persist, with five artifacts (`RESEARCH_BRIEF.md`, `EVIDENCE_TABLE.md`, `DRAFT_FINDINGS.md`, `ADVERSARIAL_REVIEW.md`, `FINAL_REPORT.md`) (:54-62; reference :5-40).
  - It mandates "BrowserOS only" for browser automation (:23).
- **Strong parts to keep:** "Use fresh adversarial review for acceptance decisions. The executor should not mark its own result as final" (:40); claim labels confirmed / likely / speculative / unresolved (reference :11-12); "write … a short update log so the next run can resume" (reference :15-16).
- **Weaknesses:** it depends on an absent repo, a foreign path, and a tool constraint (BrowserOS) that may not apply.
- **Overlap.** Upstream **deep-research** (freeze the brief, adversarial search, quality gates; a much fuller version) and vibe-research-workflow. Locally se-paper-reviewer (adversarial review).
- **License:** **(c)/(d).** An external project is named ("ARIS", "Auto-claude-code-research-in-sleep"), but there is no URL or license and the repo is absent.
- **Verdict:** **RETIRE** (REFERENCE-ONLY note in deep-research: "artifact-per-phase + fresh-reviewer acceptance").
  - Reason: upstream deep-research covers it with more rigor, and the pointer target is not on this machine.

### takenotes

- **Path:** `~/.claude/skills/takenotes/`.
- **Size:** SKILL.md 389 lines. A previous version, `SKILL.md.fancy-backup-20260531` (353 lines). 2 scripts: `publish_note.py` (487), `strict_mintlify_check.py` (123). Plus `agents/openai.yaml`.
- **What it does.** Turns pasted material into a Mintlify MDX blog post in `/Users/yitwah/projects/blog`.
  - Nine post types with intake prompts (:36-131), required frontmatter and JSX metadata cards (:152-228), and per-type body sections (:230-243).
  - Navigation grouping by month and topic (:331-344).
  - It then automatically validates (`mint validate`, broken links, a11y), commits, **pushes, and deploys to Vercel** (:346-370).
- **Strong parts to keep:** the `decision` and `experiment` note templates (:119-131, :241-243) as optional `docs/notes` shapes, and "If the raw material contains wrong attempts, put them under failure modes … do not present them as recommended steps" (:285).
- **Weaknesses:** it is a personal blog publisher with side effects (push and deploy) and hard-coded foreign paths. It has nothing to do with papers.
- **Overlap.** Locally ADR (`decision` type) and research-docs-linear-lifecycle (`docs/notes`). No upstream overlap.
- **License:** **(d).**
- **Verdict:** **RETIRE from the library.**
  - Reason: out of scope, and auto-publishing conflicts with "records outside the paper, private by default". At most, borrow the `experiment`/`decision` headings for `docs/notes` templates.

---

## 7. Writing craft

### writing-shape

- **Path:** `~/.claude/skills/writing-shape/`.
- **Size:** SKILL.md 79 lines. Plus `agents/openai.yaml` (implicit invocation off).
- **What it does.** An "exploit" session that turns a raw-material file into an article.
  - Read the pile, fix the reader's prerequisites, offer 2–3 candidate openings each implying a different thesis, then grow the article paragraph by paragraph, arguing about each block's format (:19-26).
  - Track a "grounded concepts" list: a block may lean only on concepts that are already grounded (:28-39).
  - Push-back prompts (:45-51), "name the gap" when the pile lacks material (:57), and format trade-offs (:59-67).
- **Strong parts to keep:** **Grounding** (:28-39), the cleanest statement in the set of "define before use" at the *concept* level; "If the pile lacks something … name the gap explicitly" (:57); and "What does this paragraph do for the reader that the previous one didn't?" (:47).
- **Weaknesses:** it is aimed at articles and blogs and is interactive by design (the user picks openings). It has no evidence or citation handling.
- **Overlap.** Upstream intro-drafter (flowchart planning) and tech-paper-template (skeleton). Locally writing-beats (the same grounding text), se-paper-refinement 3h (motivate before operation), and lecture "first sentence is the point".
- **License:** **(d).** No author, license, or URL in the files.
- **Verdict:** **REFERENCE-ONLY.** Lift "Grounding" into `core/` as a reader-logic rule used by paper-writer and intro-drafter.
  - Reason: the concept-grounding discipline is general and valuable; the interactive article workflow is not a research-paper procedure.

### writing-beats

- **Path:** `~/.claude/skills/writing-beats/`.
- **Size:** SKILL.md 67 lines. Plus `agents/openai.yaml`.
- **What it does.** A choose-your-own-adventure "exploit" variant. Settle prerequisites, offer 2–3 starting beats, write one beat at a time, and offer the next beats that are reachable from the grounded set (:13-19). It defines what a beat is (:40-50) and states that the article ends when the journey is complete, not when the pile is empty (:56-58).
- **Strong parts to keep:** "picking a beat that grounds concept X unlocks every beat that was waiting on X" (:36), and "If a 'beat' needs five paragraphs and three subheadings, it's … two beats glued together" (:50).
- **Weaknesses:** the same as writing-shape; essay-oriented and interactive.
- **Overlap.** writing-shape (the grounding section is near-identical) and writing-fragments.
- **License:** **(d).**
- **Verdict:** **RETIRE.** The grounding rule is captured via writing-shape.
  - Reason: redundant with writing-shape for the library's purposes.

### writing-fragments

- **Path:** `~/.claude/skills/writing-fragments/`.
- **Size:** SKILL.md 79 lines. Plus `agents/openai.yaml`.
- **What it does.** An "explore" interview that appends heterogeneous fragments to a single Markdown file separated by `---`. The model asks relentless questions, imposes no structure, and pushes the user to coin a "leading word" (:7-40, :42-69).
- **Strong parts to keep:** the "leading word" idea, one coined term the piece hangs on (:36-38), and "Never overwrite the file; only append" (:75).
- **Weaknesses:** it is essay or idea generation, not research writing.
- **Overlap.** Upstream idea-evaluator and vibe-research-workflow (loosely). Locally writing-shape and writing-beats.
- **License:** **(d).**
- **Verdict:** **RETIRE** (keep installed for personal essays if wanted).
  - Reason: out of scope for paper writing.

### storytelling

- **Path:** `~/.claude/skills/storytelling/`.
- **Size:** SKILL.md 165 lines. 3 references: `examples.md` (65), `workflows.md` (56), `shot-planning.md` (69).
- **What it does.** Plans multi-shot **image, video, and audio** generation with the `genmedia` CLI: shot tables, continuity anchors, routing to fal or Seedance endpoints, async runs and downloads (:9-165).
- **Strong parts to keep:** none relevant to paper writing.
- **Weaknesses:** a different domain. It depends on `model-routing`, `character-design`, and `commercial` (:18, workflows.md:37, :44).
- **Overlap.** None with upstream or the writing skills.
- **License:** **(d).**
- **Verdict:** **RETIRE from this library.**
  - Reason: it is a generative-media skill; the name collides with "writing craft" but the content is unrelated.

### paper

- **Path:** `~/.claude/skills/paper/`.
- **Size:** SKILL.md 95 lines. 1 script: `scripts/scaffold_paper.py`, 118 lines. Plus `agents/openai.yaml`.
- **What it does.** A general LaTeX paper workflow: identify the task type, inspect before editing, use `\(...\)`/`\[...\]` math, compile and fix from the log, and for proof audits separate whether the critique is correct, whether there is a serious gap, and how to repair it (:26-44).
  - The scaffold creates `main.tex` (article class with theorem environments), `references.bib`, `sections/`, `figures/`, `build/`, and `.gitignore`, and refuses to overwrite existing files (script:6-91).
  - It loads the user's style profile from `academic-author-team` (:18-22). That file exists locally at `~/.claude/skills/academic-author-team/references/style-profile.md`, but the skill points to a `/Users/yitwah/.codex/...` path.
- **Strong parts to keep:** "Avoid hiding proof obligations in phrases like 'clearly', 'standard', or 'it follows'" (:70-72); the three-way split for proof audits (:41-44); the "Before reporting success" verification options (:89-95); and the non-overwriting scaffold.
- **Weaknesses:** the scaffold's `main.tex` never `\input`s `sections/` (script:39-59), and it is math-oriented with no venue templates.
- **Overlap.** Upstream paper-writer (drafting), tech-paper-template, and pre-submission-reviewer (`latex-rules.md`). Locally academic-author-team (not audited here).
- **License:** **(d).**
- **Verdict:** **MERGE INTO paper-writer** (the proof-obligation rule goes to `fields/math.md`, the scaffold script goes to `scripts/`).
  - Reason: small, useful LaTeX and math hygiene that belongs in the math field profile and the drafting skill, not a separate entry point.

---

## 8. Archive-only skills (`03-skills/`)

### msr-tpa-rq-method-borrow

- **Path:** `/Users/wriseai/Projects/supervisor-skills-msr-tpa/03-skills/msr-tpa-rq-method-borrow/`.
- **Size:** SKILL.md 111 lines. 0 references (it points at `local-refs/related-work/_method_cards/*.md`, which are not in this folder).
- **What it does.** A companion to journal-adapt that extracts *analysis methods* rather than prose style from a related-work corpus. Hard rules: never edit `sections/*.tex` without a request, never import other papers' empirical claims, and use method cards only (:16-21).
  - **Phase A** maps each technique to an RQ with feasibility Now / Near / Future and a "Threat if misapplied" column (:43-55).
  - **Phase B** gives a ranked list of borrowings for this paper, e.g. "model–model agreement + confidence screening … report P/R/F1 + discarded rate" (:57-76).
  - **Phase C** is a gated implementation brief that includes a "Not doing" list (:78-92). **Phase D** hands off to journal-adapt. A subagent-per-card playbook follows (:101-107).
- **Strong parts to keep:** the method-card concept (journal-adapt rule 3 applied to methods); the feasibility labels with a "Threat if misapplied" column (:48-55); and the implementation brief with a "Not doing" list (:82-90).
- **Weaknesses:** entirely project-specific (MSR-TPA paper, specific papers and RQs).
- **Overlap.** Locally journal-adapt. Upstream idea-evaluator (feasibility) only loosely.
- **License:** **(d).** User-authored for the project.
- **Verdict:** **KEEP in the project repo.** Generalize the pattern into journal-adapt as a "method-card mode".
  - Reason: the pattern (borrow methods from a corpus without importing findings) is general, but this instance is not.

### adams-sail-issue-mining

- **Path:** `/Users/wriseai/Projects/supervisor-skills-msr-tpa/03-skills/adams-sail-issue-mining/`.
- **Size:** SKILL.md 247 lines. 1 reference: `references/six-papers.md`, 15 lines, listing six Adams/SAIL papers (MSR 2011/2012, EMSE 2012/2018/2022, WCRE 2010).
- **What it does.** A rhetoric reviewer for the "What Breaks in Proof Assistants" FSE/PACMSE manuscript. Its rules were generated from six journal-adapt style cards (:21).
  - Hard rules and a human gate (:10-15, :223-225).
  - A locked spine, a Keep list, and a Forbidden list (:23-27).
  - The P1–P5 stack (:43-69).
  - **17 consensus rules held by at least 4 of the 6 cards** (:73-93).
  - An "FSE resolutions" table for axes where the cards disagree (:97-106).
  - "P4 leaks" (CS-engineering sentences that do not belong in an issue-mining paper) (:110-114) and a NEVER-IMPORT list (:118-127).
  - Section rules with Do / Do not / 指出 (point out) / Emphasize (:131-213), a prescribed Threats order of 9 items (:195-207), Phase 2 red flags (:217-219), and three worked invocation examples (:229-247).
- **Strong parts to keep. This is the best SE-writing artifact in the inventory:**
  - "Consensus (general; ≥4 of 6 cards)" (:73). The rules are evidence-backed with a stated threshold.
  - "Status hygiene. `closed` ≠ resolved-family ≠ `fixed`" (:84) and "Calendar time ≠ labor" (:85).
  - "Residual / unknown / untraced is an arm" (:86) and "Mechanism stays 'possible explanation.' Nulls use the same grammar as positive contrasts" (:87).
  - "Related work is a they/we cut … 'We are the first' is never the only gap sentence" (:88).
  - "Threats are operational and ordered" (:89) together with the 9-item order (:197-205).
  - The "P4 leaks" test (:112).
  - "Current-draft tension (do not auto-edit until confirmed)" (:151).
- **Weaknesses:** it is manuscript-specific (numbers N=23671, κ, and the spine are hard-coded) and mixes Chinese labels (指出) into English rules.
- **Overlap.** Locally journal-adapt (it is that skill's output format), se-paper-writing and se-paper-refinement (it contradicts their numbered contribution bullets, se-paper-writing:204-214, with consensus rule 1 at :77), and deai-paper-writing (S3/S4).
- **License:** **(d).** User-generated through journal-adapt over six published papers. Rule 3 at :14 forbids paraphrasing them, and the file holds only structural rules.
- **Verdict:** **KEEP in the project repo, and use it as the template and exemplar for `fields/se.md` (MSR / issue-mining subsection) and for what journal-adapt should emit.**
  - Reason: it shows the desired output format (consensus threshold, conflict resolutions, leak tests, Do/Do not per section, red flags). Generalize by stripping project numbers and keeping the construct rules.

---

## 9. Summary table

| Skill | Verdict | Target | License class |
|---|---|---|---|
| journal-adapt | KEEP + STRENGTHEN | generator of `fields/` and `venues/` profiles | (a) MIT declared in REPO_README; no LICENSE file, holder, or URL |
| se-paper-writing | MERGE (retire standalone) | paper-writer + `fields/se.md` + `checklists/se-pre-submission.md` | (d) |
| se-paper-refinement | MERGE (§9 to project repo) | paper-polish + `core/claims-match-evidence` + `fields/se.md` | (d) user/advisor-authored, named people quoted |
| se-paper-reviewer | MERGE | pre-submission-reviewer (devil's-advocate pass) + SE challenges in `fields/se.md` | (d), with internal evidence of an unnamed external suite |
| avoid-ai-writing | MERGE | unified de-AI skill: general pattern catalog + editing contract | (a) MIT, Conor Bronsdon, github.com/conorbronsdon/avoid-ai-writing |
| deai-paper-writing | MERGE (as core) | unified de-AI skill: S1–S7, tasks A–E, guardrails | (d) |
| humanize-paper | MERGE | de-AI `core/` principles; inline-comment step to feedback-to-revision | (d), written for "Senior A" |
| parse-pdf-comments | KEEP as tool + STRENGTHEN | feedback-to-revision `scripts/` | (d), foreign path |
| collaborative-review-notes | MERGE | feedback-to-revision ledger format | (d) |
| lecture-paper-revision | REFERENCE-ONLY (paraphrase rules) | `fields/se.md` + `checklists/` with provenance | (c) lecture deck, no license |
| drawio-figure-replication | MERGE | drawio-reconstruction | (d) |
| drawio-architecture | RETIRE | (legend rule to figure-designer) | (a) Apache-2.0, holder blank |
| drawio-flowchart | RETIRE | none | (a) Apache-2.0, holder blank |
| nn-models-drawio-library | REFERENCE-ONLY | figure-designer `tools.md` pointer | (c) HuanPP library; absent, license unknown |
| scientific-illustration-ppt | REFERENCE-ONLY (outside library) | attribution pattern to figure-designer | (d) skill; indexed assets are third-party (BioIcons per-icon, Health Icons CC0) |
| tikz-diagram-review | MERGE | figure-designer render loop + script | (d) |
| anti-accretive-docs | KEEP | `core/` records | (c) brian-bell, durable-docs, ECC named; reference copies unlicensed |
| architecture-decision-records | KEEP | records | (c) affaan-m/ECC base, no license locally |
| research-docs-linear-lifecycle | MERGE | anti-accretive-docs lifecycle (Linear optional, `docs/STATUS.md` default) | (d) |
| linear | RETIRE (from library) | none | (a) Apache-2.0 |
| aris-auto-research | RETIRE | deep-research (note only) | (c)/(d) ARIS repo named, absent, no URL |
| takenotes | RETIRE | (note templates only) | (d) |
| writing-shape | REFERENCE-ONLY | "Grounding" rule to `core/` | (d) |
| writing-beats | RETIRE | none (covered by writing-shape) | (d) |
| writing-fragments | RETIRE | none | (d) |
| storytelling | RETIRE | none (genmedia video) | (d) |
| paper | MERGE | paper-writer + `fields/math.md` + scaffold script | (d) |
| msr-tpa-rq-method-borrow | KEEP in project | method-card mode in journal-adapt | (d) |
| adams-sail-issue-mining | KEEP in project + use as exemplar | `fields/se.md` (MSR / issue-mining) template | (d) |

**License blockers before vendoring verbatim text:**

1. journal-adapt: MIT is claimed, but there is no copyright holder or repository, so the MIT notice cannot be reproduced. Trace the upstream repo.
2. anti-accretive-docs: `references-brian-bell-*.md` are full third-party skill copies with no license.
3. architecture-decision-records: the ECC base has no license locally.
4. lecture-paper-revision: `reference.md` is a lecture transcription; paraphrase with credit only.
5. nn-models-drawio-library: the library is absent and its license unknown.
6. se-paper-reviewer: it was extracted from an unnamed external reviewer suite.
7. humanize-paper: it was written for a third party ("Senior A").
8. Privacy: se-paper-refinement quotes named advisors verbatim.

MIT (avoid-ai-writing) and Apache-2.0 (linear, drawio-architecture, drawio-flowchart) are fine with attribution. Keep avoid-ai-writing's own "adapted from" credits.

---

## 10. Overlap groups

### De-AI (avoid-ai-writing, deai-paper-writing, humanize-paper; upstream paper-polish `ai-tone-guardrails.md`, pre-submission-reviewer `forbidden-patterns.md`; local se-paper-refinement §1, journal-adapt P5)

Proposed shape of the single de-AI skill:

- **From deai-paper-writing (spine):**
  - The S1–S7 diagnosis vocabulary (kit:67-187).
  - The claim ledger (kit:226-233), the information-gain and asymmetry tests (kit:191-201), and "output longer than input = fail" (kit:47).
  - Tasks A–E as modes (diagnose / full / section / numbers / audit).
  - §8 guardrails (kit:533-556) and §7 author-only checklist (kit:508-529).
- **From avoid-ai-writing:**
  - The editing contract (candidate → finding → authorized edit; protected content; source fidelity) (SKILL.md:34-105).
  - "Never inject these" (SKILL.md:301-317).
  - The Tier 1A/1B split (patterns.md:37-45).
  - The Verification block (passes, checks, residuals, stop reason) (SKILL.md:236-242).
  - The context-profile mechanism. **Add an `academic` profile** in which em-dash and semicolon rules defer to venue style and LaTeX conventions.
- **From humanize-paper:** "hedge interpretations, never measured facts", "% TODO: verify" for unverifiable superlatives, "a paper defends; a review hedges", "preserve plainness", and minimal-diff LaTeX mechanics (SKILL.md:26-34).
- **From upstream:** deduplicate the word lists into one canonical list (paper-polish already marks its file as canonical with a sync script, `ai-tone-guardrails.md:1-2`).
- **Drop:** blanket bans on semicolons and colons (humanize-paper:27, se-paper-refinement:34, :375-376) as defaults. Keep them as venue or advisor profile options.

### SE writing (se-paper-writing, se-paper-refinement, se-paper-reviewer, lecture-paper-revision, adams-sail-issue-mining, msr-tpa-rq-method-borrow, journal-adapt `cs_engineering.md`)

`fields/se.md` should have short rules, each with one good/bad pair, field-neutral wording, and provenance tags:

- **Results:**
  - Finding-first paragraphs and the taxonomy-walk test (se-paper-writing:428-479).
  - The bold header as a sequential contract (refinement:131-149).
  - Number density (refinement:200-211).
  - No causes or implications in Results (refinement:213-239).
  - Evidence boundaries per RQ (se-paper-writing:717-731).
  - Comparison-word precision (se-paper-writing:566-578).
- **Constructs:**
  - Issue vs failure vs friction (se-paper-writing:733-750).
  - closed ≠ fixed and calendar time ≠ labor (adams:84-85).
  - Stable analysis units (refinement:107-116).
  - Metric definitions (refinement:264-280).
- **RQs:** related, not dependent (lecture reference.md:89-91); each RQ creates the need for the next (refinement:348-355).
- **Implications:** finding → characterization → SE research connection (refinement:241-258); audience-split but no unsolicited product advice (adams:92).
- **Threats:** construct/internal/external/reliability (se-paper-writing:293-312); operational and ordered (adams:89, :195-207); unfixable reviewer requests go to Threats (refinement:441-443).
- **Contributions:** document that SE sub-venues disagree. se-paper-writing:204-214 and `cs_engineering.md:31` say 2–4 numbered bullets; adams:77 says none (MSR / issue-mining). journal-adapt should decide per venue.
- **Reviewer lens:** the strongest counter-argument plus CRITICAL criteria (se-paper-reviewer:42-59, :157-158), plus SE criteria (se-paper-writing:908-928).
- **Process:** the methods-borrowing card (msr-tpa-rq-method-borrow:43-55) goes into journal-adapt.

### Comments → revision (parse-pdf-comments, collaborative-review-notes, humanize-paper inline comments, se-paper-refinement §8/§9i; upstream rebuttal-guidance)

The new **feedback-to-revision** skill:

- **Ingest:** PDF annotations via `extract_pdf_comments.py` (three-field records); inline TeX comments (humanize-paper:20-22); screenshots (collaborative-review-notes:25-35).
- **Ledger:** collaborative-review-notes entry schema (:74-101) plus states for resolved-by-diff and declined-with-reason.
- **Triage:** classify each item as wording / logic / evidence / new-work-needed. Do not adopt "do not argue" (refinement:389). Items that need new work narrow the claim and go to Threats (refinement:441-443). Reviewer-facing replies hand off to rebuttal-guidance.
- **Apply:** propagate a fix to every recurrence (humanize-paper:22; refinement:390-391); check that `\ref`/`\label` survive (refinement:307-309); keep the diff minimal.
- **Close:** a number check table (refinement:449) and acceptance criteria per entry.

### Figures (drawio-figure-replication, drawio-architecture, drawio-flowchart, nn-models-drawio-library, scientific-illustration-ppt, tikz-diagram-review; upstream figure-designer, drawio-reconstruction)

- **Into drawio-reconstruction:** the layout fingerprint, module-first build with module QA crops, and `SVG_ASSETS.md` provenance (drawio-figure-replication:24-39).
- **Into figure-designer:**
  - The TikZ render-and-inspect loop and script (tikz-diagram-review:10-95).
  - "color is not the only cue" (tikz:62).
  - "Do not change what a box or an arrow means between figures" and "overview component names = subsection headings" (lecture reference.md:32-33).
  - "Add a legend" (drawio-architecture:57).
  - Per-asset attribution records (scientific-illustration-ppt:19, :79-80).
  - A pointer to the NN block library.
- **Retire:** the generic GUI-oriented flowchart and architecture skills.

### Records (anti-accretive-docs, architecture-decision-records, research-docs-linear-lifecycle, linear, takenotes, aris-auto-research)

- **Keep:** anti-accretive-docs (replace-not-append, the "never saw old version" test, the history-allowed exceptions) and ADR (confirm-before-write, supersede chain, ≥2 real alternatives).
- **Fold in:** the lifecycle from research-docs-linear-lifecycle (scratch notes expire; never two CURRENT answers), using `docs/STATUS.md` as the default board and Linear as an optional adapter.
- **Borrow from elsewhere:** takenotes' `decision`/`experiment` headings as `docs/notes` templates, and the artifact-per-phase plus fresh-reviewer acceptance from aris (cite it in deep-research).
- **Retire:** linear (generic tool), takenotes (blog publishing), and aris (pointer to an absent repo).

### Writing craft (writing-shape, writing-beats, writing-fragments, storytelling, paper)

- **Into `core/`:** concept grounding (writing-shape:28-39): every concept is a prerequisite or introduced before a later block leans on it. It complements refinement 3h and the lecture's "first sentence is the point".
- **Into paper-writer and `fields/math.md`:** the proof-obligation rule and the scaffold script from `paper`.
- **Retire:** writing-beats and writing-fragments (essay workflows) and storytelling (video generation).

---

## 11. Diagnosis: why se-paper-* output felt weak

The user likes the SE-specific style and the writing → refinement → review structure, but generated output felt poor. The files themselves explain why.

1. **The skills contradict each other on core paragraph mechanics.** A model given both, or moving from writing to refinement, oscillates or averages the two.
   - *Order of numbers and claims.* se-paper-writing:686-693 is titled "Numbers First, Interpretation Second … Every claim must be numerically anchored". Its own "Bold Topic Sentences: Claim First" (:481-509) and refinement 3c "Explain before showing numbers" (:151-156) say the opposite.
   - *Implications inside Results.* se-paper-writing:646-684 closes results paragraphs with audience-targeted recommendations ("Harness developers should therefore prioritize…", :682), and :788 says "Every observation needs a 'so what' … implication". Refinement 4c says "No implications in results sections", which it calls the advisor's "#1 recurring complaint" (:228-235).
   - *Causal interpretation.* se-paper-writing's "good" examples are unmeasured interpretations ("reflecting that semantic similarity is valued but not yet trusted", :605; "LLM-as-judge has crossed a legitimacy threshold", :619). Refinement 4b and 4e (:213-226, :260-262), and se-paper-writing's own evidence-boundary rule (:717-731), forbid exactly that.
   - *Hedging.* se-paper-writing:381 says "Eliminate hedging: Remove 'may', 'might'…". Refinement:105 says interpretations should use "may", "is consistent with", "suggests".
   - *Abstract.* se-paper-writing:178-193 and :816 say "short and punchy", one sentence per RQ finding, and end with a practitioner implication. Refinement:471-480 says 150–250 words with most of the words on Methods and Results. Lecture-paper-revision:26 gives seven sentences in another order.
   - *Conclusion.* se-paper-writing:815 says "one sentence per RQ finding"; refinement:434 says "rather than writing one isolated sentence per RQ".
   - *Contributions.* se-paper-writing:204-214 says 2–4 bullets; adams-sail:77, evidence from 6 SE papers, says no numbered list.
   - *Figure pointers.* Lecture reference.md:97 says the second sentence should point at the figure; refinement:237 says cut pure pointer sentences.
2. **The rules are overfitted to two specific papers, and the model was never told which parts are local.**
   - The examples, labels, and audiences come from one LLM-evaluation-harness study: S0-A/S1-B codes, "harness developers", and the "ML developers" unification rule (se-paper-writing:446-470, :650-684).
   - Section 9 of refinement is literally "Project-Specific Rules (SWE-Bench 'Beyond the Leaderboard' paper)" (:397-480), including "Never merge Workflow and Reasoning" (:425-427). Both skills hard-code `experiment/RQ*_summary.txt` (se-paper-writing:766, refinement:403), and the "Gartner Hype Cycle" appears in a generic abstract rule (se-paper-writing:192).
   - On a new paper, a model either imports this vocabulary and these framings or cannot work out what the rule is.
3. **They are mostly reactive bans, not a generative procedure.**
   - Refinement is organized around one advisor's past complaints ("Wang is highly sensitive…", :27; dozens of verbatim quotes). That works for checking a draft but gives a generator no plan.
   - There are no positive templates for paragraph moves beyond sentence-level before/after snippets, and **no full exemplar paragraph sequence or section**.
   - Compare adams-sail-issue-mining, which derives rules from six papers with a stated "≥4 of 6" consensus threshold (:73), resolves disagreements explicitly (:97-106), and gives Do / Do not per section (:131-213).
4. **Mechanical punctuation and tense bans plus a tiny allowed-connector set produce monotone prose.**
   - The bans: no semicolons, no em dashes, no colons as consequence connectors, no "because" as a connector, and present tense only (se-paper-writing:191, :768-781; refinement:33-34, :375-376).
   - The approved replacements are ", so … / , meaning … / , with …" (se-paper-writing:414-419; refinement:376).
   - Under generation, a model satisfies the bans by chaining the same three connectors, which is a fresh templated texture. That is the failure avoid-ai-writing warns about ("Over-polishing", patterns.md:586; "uniformity itself is the strongest tell", humanize-paper:27).
   - The present-tense-only rule (se-paper-writing:770) also contradicts every journal-adapt base profile, which put findings in past tense (`general_academic.md:25`, `ml_cv_nlp.md:90`, `economics.md:23`).
5. **There is no evidence intake before drafting.**
   - se-paper-writing says "Be proactive … deliver a full draft" with `[TODO]` and `[CITATION NEEDED]` markers (:22, :114-119). "Workflow 0" is a few `find` and `grep` commands (:85-98).
   - Nothing builds a findings or claim list with numbers and scopes before prose is written: no claim ledger (deai kit:226-233) and no evidence phase like upstream paper-writer's Phase 2.
   - So the model writes fluent prose first and the numbers and scope rules are applied afterwards, if at all.
6. **The files are too long and lack progressive disclosure.**
   - se-paper-writing is 1017 lines and 55 KB; refinement is 41 KB in one file. Neither has a `references/` split.
   - Generic material (Gopen & Swan, Lipton & Steinhardt, venue tables, rejection reasons, replication packages; :352-384, :820-957) sits next to the SE-specific rules and dilutes attention. The undated venue table (:824-840) risks stale facts.
7. **The writing → refinement → review pipeline is not actually wired.**
   - All three have `disable-model-invocation: true` (writing:9, refinement:10, reviewer:10), and none hands off to another.
   - The "review" stage is a generic devil's advocate with no SE content. It references agents that do not exist (se-paper-reviewer:19-40, :63-72) and contradicts itself on stakeholders (:39 vs :124-129, :178-180).
8. **Some advice works against quality.**
   - "Cite generously: reviewers may have authored cited papers" (se-paper-writing:287).
   - "Avoid 'combine', 'modify', 'extend' (signals incremental). Use 'propose'…" (:384), which pushes toward overclaiming.
   - A scripted defence for benchmark contamination (:314).
   - "Do not argue — the comment's existence proves the text was unclear" (refinement:389).

**What to do about it** (feeds the merge plan):

1. Split the material into `core/` (field-neutral reader logic: refinement 2f/2g/3a/3b/3h/4a-4f) and `fields/se.md` (SE constructs, threats, implications), each rule with one short good/bad pair in neutral vocabulary.
2. Resolve every contradiction above once, in writing, in the profile (for example: claim-first bold; explanation before numbers; no implications in Results; hedge interpretations only). Make the remaining true divergences, such as contribution lists, venue-profile switches generated by journal-adapt.
3. Add an evidence-intake step (claim ledger with numbers and scope) to paper-writer before drafting.
4. Move punctuation bans into an optional "advisor style" overlay.
5. Move the project sections (refinement §9, deai SKILL.md:36-46, adams numbers) into the project repos.
6. Rebuild the review stage as pre-submission-reviewer plus the devil's-advocate pass plus SE checks.
