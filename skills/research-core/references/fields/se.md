# Field profile: Software engineering (empirical SE and MSR first)

Code: SE
Status: evidenced
Version: 0.1 (2026-10-13)
Scope: empirical SE and mining software repositories (MSR): RQ-driven
empirical papers and mining studies of issue trackers, commits and pull
requests. Technique and tool papers are covered only partially.

## Contents
Sources; Paper types; Typical structure; What reviewers and advisors care
about; Tone and phrasing; Citation norms; Figures and tables; Rigor and
threats; Checklist additions (SE-01 to SE-19); Known disagreements; Unknown;
Changelog.

Rules use the format of `references/core/precedence.md`. Core rules (claim
ledger, numbers, hedging, causal language, model-read qualifiers, agreement
numbers, term table, overview-figure numbering) are not repeated here.

## Sources
1. `lit:wohlin2012`: C. Wohlin, P. Runeson, M. Höst, M. C. Ohlsson,
   B. Regnell, A. Wesslén. *Experimentation in Software Engineering*.
   Springer, 2012. DOI 10.1007/978-3-642-29044-2. Record checked 2026-10-13;
   the four validity categories (conclusion, internal, construct, external)
   are attributed to it by the papers that apply it.
2. `lit:sigsoft-rm`: ACM SIGSOFT Empirical Standards, "Repository Mining"
   standard, fetched 2026-10-13 from
   https://raw.githubusercontent.com/acmsigsoft/EmpiricalStandards/master/docs/standards/RepositoryMining.md;
   summarized in P. Chatterjee, T. Sharma, P. Ralph, "Empirical Standards for
   Repository Mining", MSR 2022 tutorial, arXiv:2203.15950,
   DOI 10.1145/3524842.3528032.
3. Evidence project: one RQ-driven MSR study of a niche software
   ecosystem's issue trackers, submitted to the FSE research track. Cited as
   `arc:` ids and the evidence notes `note:n02`, `note:n05` to `note:n08`.
4. The owner's former skills `skill:se-paper-writing`,
   `skill:se-paper-refinement`, `skill:se-paper-reviewer` and
   `skill:lecture-paper-revision` (paraphrased lecture-deck rules). The
   owner's archived issue-mining rhetoric skill (rules shared by at least
   four of six SE exemplar style cards) is cited through its audit,
   `note:n02§8`, because its name carries personal names.
5. The FSE venue profile, `references/venues/fse.md`.

## Paper types
- **RQ-driven empirical study** (mining, survey, qualitative): numbered RQs,
  a data pipeline, results per RQ, implications by audience, threats.
  [src: note:n06§3; skill:se-paper-writing] (candidate)
- **Technique or tool paper**: approach, evaluation RQs against baselines,
  threats. Partial coverage only. [src: skill:se-paper-writing] (candidate)
- A mining paper characterizes (codebook, agreement, effect sizes); do not
  bolt on a prediction RQ. A sentence that could sit in a systems paper ("we
  design and build", product-style contribution bullets, predictor
  leaderboards) is a leak into the wrong type. [src: note:n02§8] (candidate)

## Typical structure
One exemplar's measured prose under an 18-page all-in limit; lengths are a
reference, not targets. [src: note:n06§3] (candidate)

| Section | Words (exemplar) | Floats |
|---|---:|---|
| Abstract | 190 to 270 | none |
| Introduction | ~1,100 | 1 phenomenon figure |
| Background and related work | ~1,150 | none |
| Methodology | ~1,850 | workflow figure, codebook table |
| Results, one subsection per RQ | 350 to 900 per RQ | 1 figure or table per RQ |
| Implications | ~900 | none |
| Threats to validity | ~700 | none |
| Conclusion | 150 to 200 | none |
| Data Availability | ~80 | none |

- **Abstract**: background, gap, "to fill this gap" with scope, method in one
  sentence, key findings, recommendation. [src: note:n06§3] (candidate)
- **Introduction**: context for a general SE reader; a figure showing the
  phenomenon; why the data source matters to SE (datasets, triage,
  benchmarks, validity of mining); the gap; RQ blocks (bold question, one
  "so we ask" sentence, two or three "we find" sentences); one-sentence
  method; contributions; roadmap. [src: note:n05§1.1 FB-A-09; note:n06§3] (candidate)
- **Related work**: per cited study its method, scale and result; per strand
  what it misses; a they/we cut on the dependent construct. "We are the
  first" is never the only gap sentence. [src: arc:msr:9c69675; note:n02§8] (candidate)
- **Methodology**: overview paragraph, then one bold "Step n" run-in per
  workflow box (purpose, procedure, number produced). Labeling and gold are
  method objects described before any distribution or duration result.
  [src: arc:msr:b5c0045; note:n06§2.5; note:n02§8] (candidate)
- **RQs**: three or four, related but not dependent; none answerable by yes
  or no; you know which figure answers each.
  [src: skill:lecture-paper-revision; skill:se-paper-refinement] (candidate)
- **Results**: one subsection per RQ, no sub-subsections. Finding paragraph:
  (1) bold finding in words, scoped ("pooled over ecosystems"), at most one
  number; (2) a sentence citing the figure, table or column with one or two
  exact numbers, never a bare pointer; (3) one to three sentences of
  breakdown, exception, robustness or needed definition. Merge paragraphs
  that add nothing; order by importance.
  [src: arc:msr:0f96193; arc:msr:9809b8c; note:n06§2.4; skill:lecture-paper-revision] (candidate)
- **Summary box** at the end of each RQ, titled "RQn Summary": two to four
  sentences, pooled claim then its exception, one or two exact numbers, the
  body's hedges, no recommendations. [src: arc:msr:9809b8c; note:n06§3] (candidate)
- **Implications**: one sentence naming the audiences, one subsection per
  audience (maintainers, tool builders, researchers). Item: bold imperative;
  "RQx shows that ..."; consequence or a labelled untested explanation;
  optional worked example; "<audience> should ...". Operational and tied to
  an RQ; no unsolicited product advice.
  [src: arc:msr:f141169; arc:msr:393f596; note:n06§1.8; note:n02§8] (candidate)
- **Threats**: an opening sentence naming the four categories with a
  citation, one subsection each; every threat written as threat, check or
  mitigation, residual. [src: lit:wohlin2012; arc:msr:d0d4c03; note:n06§1.9] (confirmed)
- **Conclusion**: one paragraph: what was done, findings in RQ order, a
  conditional implication ("suggest ... when ..."), one future-work
  direction tied to the main limitation. [src: note:n06§1.10] (candidate)
- **Data Availability**: unnumbered, after the conclusion; the anonymous
  package link and one inventory sentence whose scope matches what the
  package recomputes. [src: arc:msr:5776349; arc:msr:24d8c65; note:n06§1.12] (candidate)

## What reviewers and advisors care about
1. Honest threats and an available replication package.
   [src: skill:se-paper-writing; lit:sigsoft-rm] (confirmed)
2. SE framing: motivate through maintenance and evolution uses, not domain
   importance alone. [src: note:n05§1.1 FB-A-09; arc:CF-02@v2] (candidate)
3. Codebook provenance per dimension (built, borrowed, model-proposed).
   [src: arc:CF-26@v2; note:n05§1.5] (candidate)
4. A baseline from another domain; whether group differences are expected
   or surprising. [src: arc:CF-28@v2; note:n05§1.5] (candidate)
5. Related work covering likely program-committee work, with the closest
   paper positioned exactly. [src: arc:RW-01@v2; arc:RW-02@v2] (candidate)
6. Effect sizes beside p-values; recent baselines; real-world data.
   [src: skill:se-paper-writing] (candidate)
7. The strongest counter-argument, answered before a reviewer raises it.
   [src: skill:se-paper-reviewer] (candidate)
8. No appendix as padding under an all-in page limit; a compact codebook
   table in the body, definitions in the package.
   [src: arc:chat:group@2026-10-01T08:56; arc:chat:group@2026-10-02T01:51; arc:msr:464168f] (candidate)

## Tone and phrasing
- Active "we" for design choices and claims; almost no causal verbs.
  [src: note:n02§8] (candidate)
- Name what was measured: "issue" for reported problems, "failure" only for
  measured failures. [src: skill:se-paper-writing] (candidate)
- "Consistent with" needs one matching pair; "proportional to" needs a ratio
  across pairs. [src: skill:se-paper-writing] (candidate)
- Evidence boundaries per RQ: an RQ showing where problems concentrate does
  not say why unless a later RQ measures it. [src: skill:se-paper-writing] (candidate)
- No implications inside Results. [src: skill:se-paper-refinement] (candidate)
- Null and positive contrasts use the same grammar. [src: note:n02§8] (candidate)
- Define a non-standard metric (numerator, denominator, unit, direction,
  aggregation) before a finding uses it. [src: skill:se-paper-refinement] (candidate)

## Citation norms
- Check every bib entry against DBLP, or the publisher record when DBLP
  has none, and keep the audit output. Fabricated citations are a listed
  desk-reject cause. [src: arc:chat:group@2026-09-29T11:44; arc:10-requirements/venue/fse-2027-requirements.md] (confirmed)
- Flag arXiv-only entries; use the published version when one exists.
  [src: note:n08§3] (candidate)
- Never import another study's magnitudes, agreement values or taxonomy as
  facts about your corpus; note when a compared measure differs.
  [src: note:n02§8; note:n07§B.5] (candidate)
- Cite likely reviewers only when their work is relevant.
  [src: note:n02§2] (candidate)

## Figures and tables
- Category-by-group shares: one heatmap with a pooled and an equal-weight
  (balanced) column; the caption explains both and the colour scale.
  [src: arc:msr:9c69675; note:n07§A.8 FR12] (candidate)
- Put the compared items side by side (one bar per category with group
  shares inside, not one bar per repository). [src: note:n07§A.8 FR11] (candidate)
- In the workflow figure, gold data is validation only; it never feeds an
  RQ box. [src: note:n07§A.8 FR19] (candidate)
- The intro figure contrasts the failure modes studied; its caption scopes
  the architecture assumed. [src: note:n07§A.8 FR21] (candidate)
- One decimal place per table column. [src: skill:lecture-paper-revision] (candidate)

## Rigor and threats
- Mining essentials: why mining fits; units of analysis; justified data
  sources and repository selection; how inclusion and exclusion criteria
  were validated; sampling strategy; preprocessing; justified measures,
  validated or with construct validity assessed; external validity.
  [src: lit:sigsoft-rm] (confirmed)
- Closed is not fixed: report all-closed and fixed-only denominators,
  motivate both before results, name the denominator wherever cited.
  [src: note:n05§1.1 FB-A-05; arc:CF-30@v2; arc:TH-01@v2; note:n02§8] (candidate)
- Time-to-close is calendar time (tracker time, user wait), never effort or
  cost; an SE case of the core unmeasured-quantity rule.
  [src: arc:CF-29@v2; note:n02§8] (candidate)
- Open items are censored: state it or add a survival estimate before
  reading closed-item medians as typical. [src: arc:TH-06@v2; arc:msr:9c69675] (candidate)
- Tracker imports and migrations create artificial closing times; detect
  them, set them aside for durations, disclose. [src: arc:msr:9c69675; arc:TH-02@v2] (candidate)
- The residual class ("other", "unknown", untraced) is a result: its size
  and location go in Results. [src: note:n02§8; note:n07§B.5] (candidate)
- Repository labels are not study labels: a tracker's "bug" tag stays
  distinct from the coded type. [src: arc:AH-06@v2] (candidate)
- Tags, commit links, model outputs and author-built gold are readings, not
  ground truth. [src: note:n02§8; arc:TH-09@v2] (candidate)
- A strategy coded from issue text says nothing about code size; size claims
  need diff statistics. [src: arc:CF-13@v2; note:n07§B.5] (candidate)
- Stratify, then pool: per group first; an equal-weight view when one group
  dominates; cross-group disagreement is a result; state the analysed set
  per RQ and drop thin slices. [src: note:n02§8; arc:msr:9c69675; arc:CF-16@v2] (candidate)
- Check group effects against filing period; report by period when they
  are confounded. [src: note:n06§1.8; note:n06§1.9] (candidate)
- Threats use the four categories (conclusion, construct, internal,
  external). [src: lit:wohlin2012] (confirmed)
- Threats are operational and ordered, never "more projects are needed";
  robustness checks appear as mitigations with their numbers.
  [src: note:n02§8; arc:msr:9c69675; arc:msr:9c4567c] (candidate)
- A data gap more crawling cannot close, or a reviewer request a revision
  cannot meet, goes to Threats with its mechanism.
  [src: note:n08§5; skill:se-paper-refinement] (candidate)
- Examples quoted from one group are labelled illustrative.
  [src: arc:msr:b7a448b] (candidate)
- Discuss ethics of mining (personal data in issue text) where relevant.
  [src: lit:sigsoft-rm] (candidate)

## Checklist additions

### SE-01 Motivation in SE terms
- [ ] Check: The introduction says why the data source matters to SE (datasets, triage, benchmarks, validity of mining).
- Why: Advisors asked for maintenance-and-evolution framing.
- Status: candidate
- Scope: field:se
- Owner: intro-drafter, paper-writer
- Src: note:n05§1.1 FB-A-09; arc:CF-02@v2

### SE-02 Mining method essentials
- [ ] Check: Methods define units of analysis, justify sources and repository selection, state how inclusion criteria were validated, explain sampling and preprocessing.
- Why: Essential attributes of the published repository-mining standard.
- Status: confirmed
- Scope: field:se
- Owner: experiment-workflow, paper-writer, pre-submission-reviewer
- Src: lit:sigsoft-rm

### SE-03 Dual denominators
- [ ] Check: Shares and durations are given for all-closed and fixed-only items, both motivated, each cited share naming its denominator.
- Why: Closed is not fixed.
- Status: candidate
- Scope: field:se
- Owner: paper-writer, check-loop
- Src: note:n05§1.1 FB-A-05; arc:CF-30@v2; arc:TH-01@v2

### SE-04 Calendar time is not effort
- [ ] Check: No sentence reads time-to-close as effort, labour, cost or difficulty.
- Why: Only tracker time was measured.
- Status: candidate
- Scope: field:se
- Owner: paper-polish, check-loop
- Src: arc:CF-29@v2; note:n02§8

### SE-05 Durations: censoring and import artifacts
- [ ] Check: Open items are handled by a survival estimate or an explicit statement, and items closed by a tracker import or migration are excluded from durations and disclosed.
- Why: Closed-item medians hide long-open work; imports create artificial closing times.
- Status: candidate
- Scope: field:se
- Owner: experiment-workflow, research-records, pre-submission-reviewer
- Src: arc:TH-06@v2; arc:TH-02@v2; arc:msr:9c69675

### SE-06 Residual class reported
- [ ] Check: Size and location of the "other" or untraced class appear in Results.
- Why: The residual is a finding.
- Status: candidate
- Scope: field:se
- Owner: paper-writer, check-loop
- Src: note:n02§8; note:n07§B.5

### SE-07 Repository labels kept apart
- [ ] Check: Tracker tags are never used as, or named like, the coded categories.
- Why: Readers confuse them and the counts differ.
- Status: candidate
- Scope: field:se
- Owner: paper-polish, check-loop
- Src: arc:AH-06@v2

### SE-08 Codebook provenance
- [ ] Check: Each codebook dimension says whether it was built, borrowed (cited) or model-proposed.
- Why: An advisor asked where the taxonomies came from.
- Status: candidate
- Scope: field:se
- Owner: experiment-workflow, paper-writer
- Src: arc:CF-26@v2; note:n05§1.5

### SE-09 Cross-domain baseline
- [ ] Check: Findings are compared with another domain, and group differences are called expected or surprising with a reason.
- Why: Without a reference point readers cannot judge the numbers.
- Status: candidate
- Scope: field:se
- Owner: idea-evaluator, paper-writer
- Src: arc:CF-28@v2; note:n05§1.5

### SE-10 Text-coded strategy and code size
- [ ] Check: Claims about change size rest on diff statistics, not on text-coded strategy labels.
- Why: Text-derived strategy says nothing about code size.
- Status: candidate
- Scope: field:se
- Owner: check-loop, pre-submission-reviewer
- Src: arc:CF-13@v2; note:n07§B.5

### SE-11 Stratify before pooling
- [ ] Check: Every pooled result is checked per group; a dominant group gets an equal-weight view; exceptions are named in the same sentence.
- Why: A pooled share can be one repository's share.
- Status: candidate
- Scope: field:se
- Owner: experiment-workflow, paper-writer, check-loop
- Src: note:n02§8; arc:msr:9c69675; arc:CF-16@v2

### SE-12 Finding paragraph shape
- [ ] Check: Each results paragraph opens with a bold scoped finding, then a figure or table sentence with its numbers, then detail; no bare pointers.
- Why: Readers come for results; the senior co-author asked for this layout.
- Status: candidate
- Scope: field:se
- Owner: paper-writer, paper-polish, check-loop
- Src: arc:msr:0f96193; note:n06§2.4; skill:lecture-paper-revision

### SE-13 Results stay results
- [ ] Check: Results and the "RQn Summary" boxes (two to four sentences, pooled claim then exception) hold no recommendations; each recommendation sits in Implications and cites its RQ.
- Why: Resolves a contradiction between the former SE skills; keeps takeaways consistent.
- Status: candidate
- Scope: field:se
- Owner: paper-writer, paper-polish
- Src: skill:se-paper-refinement; note:n02§11; arc:msr:9809b8c; note:n06§3

### SE-14 Implications by audience
- [ ] Check: Implications are split by audience; each item has a bold imperative, RQ evidence and an operational action.
- Why: Advisors asked what each audience should do differently.
- Status: candidate
- Scope: field:se
- Owner: paper-writer, research-supervisor
- Src: arc:msr:f141169; note:n06§1.8; note:n05§1.1 FB-A-08

### SE-15 Four threat categories
- [ ] Check: Threats are grouped as conclusion, construct, internal and external validity, each written as threat, check, residual.
- Why: The standard SE validity classification.
- Status: confirmed
- Scope: field:se
- Owner: pre-submission-reviewer, paper-writer
- Src: lit:wohlin2012; note:n06§1.9

### SE-16 SE figure conventions
- [ ] Check: Gold data appears only on the validation path of the workflow figure, and category-by-group heatmaps have pooled and balanced columns explained in the caption with the colour scale.
- Why: Gold feeding RQ boxes misstates the method; one dominant group otherwise drives the pooled column.
- Status: candidate
- Scope: field:se
- Owner: figure-designer, drawio-reconstruction
- Src: note:n07§A.8 FR19; note:n07§A.8 FR12; arc:msr:9c69675

### SE-17 DBLP-checked bibliography
- [ ] Check: Every bib entry is checked against DBLP or the publisher, with the audit output kept.
- Why: Wrong or fabricated references are a desk-reject cause.
- Status: confirmed
- Scope: field:se
- Owner: paper-writer, pre-submission-reviewer
- Src: arc:chat:group@2026-09-29T11:44; arc:10-requirements/venue/fse-2027-requirements.md

### SE-18 No appendix as padding
- [ ] Check: Under an all-in page limit no appendix fills pages; a compact codebook table stays in the body, definitions go to the package.
- Why: Senior co-authors judged padding appendices a rejection risk.
- Status: candidate
- Scope: field:se
- Owner: journal-adapt, paper-polish, pre-submission-reviewer
- Src: arc:chat:group@2026-10-01T08:56; arc:chat:group@2026-10-02T01:51; arc:msr:464168f

### SE-19 Strongest counter-argument
- [ ] Check: A written strongest counter-argument to the main claim exists and the paper answers it.
- Why: Reviewers raise it otherwise.
- Status: candidate
- Scope: field:se
- Owner: pre-submission-reviewer, idea-evaluator
- Src: skill:se-paper-reviewer

## Known disagreements
The former SE skills contradicted each other; each point is decided once
here. [src: note:n02§11]
- **Claim or numbers first**: bold claim in words, then the figure sentence
  with numbers, then detail; explain before showing numbers.
- **Figure pointer**: the second sentence cites the figure and carries its
  numbers; bare pointers are cut.
- **Implications in Results**: none; this overrides the lecture rule that
  the takeaway box addresses developers.
- **Hedging**: hedge interpretations only (core rule).
- **Contribution list**: two former skills want two to four numbered
  bullets; six MSR and journal exemplars use none; the evidence paper
  itemized them. Decided per venue by `journal-adapt`.
- **Abstract length**: former rules say 150 to 200 or 150 to 250 words; the
  exemplar ran 190 to 270. The venue form limit decides.
- **Headline numbers**: senior co-authors trimmed and restored exact numbers
  in abstract and conclusion several times. One exact number per claim in
  headline positions; record the convention in an ADR. [src: note:n06§2.3]
- **Fourth threat category**: one former skill uses Reliability; the
  evidence paper tried it and folded it back. Use the four categories of
  `lit:wohlin2012` unless the venue's exemplars differ.

## Unknown
- Tense for findings (present or past): former rules conflict; no SE
  exemplar measured.
- Evaluation design for technique and tool papers.
- Section lengths at journals without an all-in page limit.
- Whether the six-exemplar consensus holds for survey and qualitative papers.

## Changelog
- 0.1 (2026-10-13): created from one evidence project, the owner's former
  SE skills and two published guides.
