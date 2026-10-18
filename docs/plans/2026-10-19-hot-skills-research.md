# Hot research skills: survey, test plan and what we adopt (2026-10-19)

Status: survey done; feature 1 implemented (`sv-experiment-prereg`); the rest
is a ranked backlog.

## 1. Questions

1. Which open-source agent skills for academic research are popular or rising
   now, and what concrete mechanisms do they have that we lack?
2. What do researchers praise and complain about in public discussion?
3. Which one feature is worth adopting first for this library and its owner
   (causal inference and statistics first, then SE and ML)?

## 2. Method

- **GitHub:** `gh search repos` by stars and by recent creation, then
  `gh api repos/<owner>/<repo>` for exact stars, last push and licence
  (2026-10-19). READMEs only; no SKILL.md bodies except the one adopted
  below.
- **Community:** Hacker News (Algolia API), Reddit (through the Arctic Shift
  mirror; reddit.com blocks fetches), Bilibili pages, Chinese media. X,
  Xiaohongshu, YouTube and Zhihu were not reachable. Engagement numbers are
  quoted only where visible.
- **Safety:** nothing was cloned; files were read through the GitHub API into
  a scratch folder; no downloaded code ran except where section 5 says so.

## 3. What is popular (stars are all-time, 2026-10-19)

| Repo | Stars | Licence | Distinctive mechanism |
|---|---|---|---|
| blader/humanizer | 58.1k | MIT | 26 patterns from Wikipedia "Signs of AI writing"; voice matching |
| Imbad0202/academic-research-skills (ARS) | 52.7k | none asserted | Blocking integrity gates; per-citation locator and claim-support audit; devil's advocate concedes only at score 4 of 5; reviewer calibration against a gold set |
| K-Dense-AI/scientific-agent-skills | 52.6k | MIT | 177 science skills; line-anchored full-text citations; power analysis |
| wanshuiyin/Auto-claude-code-research-in-sleep (ARIS) | 17.7k | MIT | Rebuttal hard gates (provenance, commitment, coverage) and a paste-ready file with exact character count; failed-idea ban list; assurance levels |
| Orchestra-Research/AI-Research-SKILLs | 13.7k | MIT | Session-end extractor of decisions and dead ends, tagged user or AI |
| Galaxy-Dawn/claude-scholar | 5.8k | MIT | Claim promotion gates; Zotero and Obsidian |
| Adkid-Zephyr/anti-defensive-writing-Skill | 3.4k (since 2026-08-11) | MIT | Every experiment must have an argumentative role |
| AIScientists-Dev/academic-humanizer | 2.2k | none asserted | "No verb stronger than the data"; grant mode |
| claesbackman/AI-research-feedback | 0.5k | MIT | Mechanical-only pre-submission pass; follows `\input{}` |
| TobiasLee/Rebuttal-Skill | 0.5k | none | Stage 0: rebuttal or resubmit; P0 to P3 experiment plan |
| fcakyon/phd-skills | 0.4k | MIT | Stop-hook peer check of conclusions against artifacts; DBLP BibTeX check |
| K-Dense-AI/science-superpowers | 0.4k | MIT | **Pre-registration lock with a git audit**; feasibility mode with kill criteria |
| wuliRothschild/scientific-review | small | Apache-2.0 | Evidence-level tags; abstract-only evidence cannot support a negative claim |
| jostelzer/grounded | small | MIT | Claims ledger before drafting; per-assertion receipts from a separate judge |

Sources: each repo's README fetched through `gh api` on 2026-10-19.

## 4. What researchers discuss (last 60 days)

- Floods of AI-written submissions and pushback: arXiv's two-per-day limit
  (HN 49926512, 152 points); TMLR asking authors to explain their own papers
  (HN 49734467, 234 points); ICLR reviewers complaining about generated text
  (r/MachineLearning, 142 upvotes).
- Autoresearch loops spreading beyond ML, with doubts about cost and about
  whether results are verified (HN 50047664; r/LocalLLaMA SoL-Pi, 313).
- AI peer review is divisive; simulated reviewers flip under pushback
  (r/MachineLearning ICLR thread, top comment 84).
- Humanizers are popular, detectors distrusted (r/PhD, 79 upvotes).
- Zotero as the hub of the literature stack; keep agent notes apart from
  your own (HN 49450898, 263 points).
- Privacy of research ideas in hosted chats (r/codex, 1,087 upvotes).

Common thread: **trust**. What is in demand is proof that a claim was
checked, decided in advance, or traceable, not more generation.

## 5. Test protocol for candidates

For each candidate feature:

1. Read its source (SKILL.md and scripts) through the API; record licence.
2. Map it onto our groups: which sub-command it extends, and whether we
   already have it (`sv-write-humanize-*` already covers most humanizer
   patterns, for example).
3. Score: relevance to the owner's fields (0 to 3), gap in our library
   (0 to 3), evidence of use (0 to 2), licence allows adaptation (0 or 1),
   effort (small 2, medium 1, large 0).
4. For the chosen feature: reimplement in our conventions, then test the
   mechanism end to end in a throwaway git repository, including every
   failure mode it claims to catch. Run the upstream script only in that
   throwaway repository, for comparison.

## 6. Scores

| Candidate | Rel. | Gap | Use | Lic. | Effort | Total |
|---|---|---|---|---|---|---|
| Pre-registration lock with git audit (science-superpowers) | 3 | 3 | 1 | 1 | 2 | **10** |
| Evidence-level tags; abstract-only cannot support negatives (scientific-review) | 2 | 2 | 1 | 1 | 2 | 8 |
| Concession threshold for critics (ARS) | 2 | 2 | 2 | 0 | 2 | 8 |
| Rebuttal hard gates and paste-ready file (ARIS) | 2 | 2 | 2 | 1 | 1 | 8 |
| Rebuttal or resubmit Stage 0 (Rebuttal-Skill) | 2 | 2 | 1 | 0 | 2 | 7 |
| Failed-idea ban list (ARIS) | 2 | 2 | 2 | 1 | 1 | 8 |
| Claim-support audit with receipts (ARS, grounded) | 3 | 2 | 2 | 1 | 0 | 8 |
| Anti-defensive writing check | 2 | 1 | 2 | 1 | 2 | 8 |
| Mechanical-only pre-submission pass | 1 | 1 | 1 | 1 | 2 | 6 |

"Lic." is 0 where no licence is asserted: the idea may be borrowed, the text
may not.

## 7. Decision

Adopt the pre-registration lock first, as a new sub-command
`sv-experiment-prereg`:

- It fills a real gap. `sv-experiment-freeze` freezes data, gold sets and
  prompt versions; nothing locks a confirmatory statistical analysis
  (hypotheses, decision rule, stopping, multiplicity) before outcomes are
  seen. That is the core risk in the owner's causal and statistics work.
- It answers the trust theme mechanically: a git audit proves the
  registration preceded every committed output and was never edited.
- The source is MIT; attribution goes in THIRD_PARTY.md.

## 8. Backlog (next, in order)

1. Evidence-level tags in `sv-litreview-survey` and `sv-quickread-card`
   (full text, abstract, inference; abstract-only cannot support a negative
   claim).
2. Rebuttal gates and a paste-ready output with exact character count in
   `sv-feedback-rebuttal`, plus a Stage 0 rebuttal-or-resubmit decision.
3. Failed-idea ban list in `sv-supervisor-records`, read first by
   `sv-idea-evaluate`.
4. Concession threshold and concession-rate log for `sv-review-loop` and
   `sv-idea-evaluate` critics.
5. Claim-support receipts: an independent check that each cited passage
   supports its sentence, as an optional layer of the verification ladder.
