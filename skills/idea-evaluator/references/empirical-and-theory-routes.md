# Empirical-study and theory routes

## Contents
1. When each route applies
2. Empirical-study route
3. Worked example: a coverage gap foreseeable at design time
4. Theory route
5. Output blocks
6. Sources

## 1. When each route applies

The upstream five dimensions (Higher, Faster, Stronger, Cheaper, Broader)
score a method against baselines. They fit AI/ML and systems technique and
benchmark papers. Two common paper types need a different audit:

- **Empirical study**: the contribution is knowledge about a population
  (software repositories, developers, systems in the field) gained from
  mining, surveys, interviews, controlled experiments or observational
  data. `paper_type: empirical-study`.
- **Theory paper**: the contribution is a result together with its proof
  technique. `paper_type: theory`.

Both routes keep the upstream fatal-flaws gate, lifecycle matching,
feasibility check and verdicts. They replace the five dimensions with the
substitute dimensions below and add a design audit.

## 2. Empirical-study route

### 2.1 Research-question set

- Each question is answerable from the planned data, with a named unit of
  analysis and a named measure.
- Questions are related but not dependent: a failure in one does not void
  the others. Each question should create the need for the next.
  [src: note:n02§10] (candidate)
- Characterise; do not bolt on a prediction question to look like a
  technique paper. [src: note:n02§8] (candidate)
- Keep the method (prompt, agreement study, model) separate from the
  question numbering; a question that needs only statistics gets a script.
  [src: note:n08§5#27] (candidate)
- Ask, for each question, which result would surprise the field and which
  would be expected; a set where every answer is expected is weak.

### 2.2 Population and sampling frame

- Name the target population and the frame actually crawled or recruited;
  claims are scoped to the frame (TH-01).
- Freeze the frame: one snapshot with a recorded cutoff, not a moving
  corpus. The study population is the snapshot. [src: note:n04§5] (candidate)
- Plan the sample from the estimand and the constraints: a probability
  sample with a recorded seed, inclusion probabilities, and floors for
  small groups when per-group results are planned. Record the rejected
  alternatives (for example simple random sampling that misses the
  floors). [src: note:n04§5] (candidate)
- Plan per-group analysis before pooling when groups differ in size
  (TH-02, SE-11).

### 2.3 Construct validity

- For every construct, write the operational definition and what it does
  not measure: closed is not fixed, calendar time is not effort, a
  repository label is not a study label (SE-03, SE-04, SE-07).
- Decide how units without the needed evidence are coded, by the purpose
  of the label (problem only: code as unknown; problem and solution: set
  aside and declare out of scope). [src: arc:@threats-pivot; note:n08§5#26] (candidate)
- Plan the agreement study now: which units get two independent
  annotators, which bar must be met before scale-up, and where the raw
  label sets will be kept (IN-04, IN-08). The evidence project had no
  designed second-annotator sample and could not later back its agreement
  value. [src: note:n04§5; note:n07§B.3] (candidate)
- Model-produced or author-built labels are readings, not ground truth
  (TH-05, TH-06).

### 2.4 Data availability

- The data is accessible now (API limits, licences, terms of service,
  personal data in issue text or survey answers and its ethics review).
- The fields each question needs exist in a usable share of units; measure
  that share on a pilot sample before committing (section 3).
- The data can be released in a replication package, or the paper can say
  why not (AR-06, AR-08).

### 2.5 Threats foreseeable at design time

Run these research-core items now and write each answer down:

- **TH-01** Which populations, sources or groups the claims will cover, and
  which major group the study will not cover.
- **TH-04** Which data gaps more collection cannot close. Each goes to the
  threats list with its mechanism today, and the team stops chasing it.
- **TH-08** Which alternative explanations the design cannot rule out.

Add the field profile's design items (for SE: SE-02 mining method
essentials, the four threat categories of SE-15) and record every answer in
the design-time threats list.

### 2.6 Substitute scoring dimensions

Score 1 to 10, start at 5, move only with grounds, as in the upstream
discipline. These dimensions restate the SE field profile's reviewer
concerns for an idea that has no data yet.

| Dimension | Question |
|---|---|
| Relevance | Does the question matter to the field's practitioners or researchers, in the field's own terms? |
| Novelty of question or data | Is the population, data source or question new, or the answer unknown? |
| Design rigor | Frame, sample, constructs and agreement plan as in 2.2 and 2.3 |
| Threat exposure | How many design-time threats are severe and unmitigable? (inverse score) |
| Actionability | Can each likely answer change what an audience does? |

## 3. Worked example: a coverage gap foreseeable at design time

A mining study of a niche software ecosystem's issue trackers planned a
question on how issues were resolved, coded from the linked fix. Weeks into
coding, a sizeable share of closed issues had no linked commit or pull
request, and matching commits by closing-time windows mostly failed as
well. The causes were structural: repository migrations, branches deleted
or never pushed, squashed commits.

Senior co-authors reframed it from a method problem to a validity problem:
state the mechanism in threats, code by the purpose of the label (unknown,
or set aside and declared out of scope in the approach), do not guess a
resolution, and move on to the question that does not depend on the links.
The record of that decision listed the rejected alternatives and a "do
not" list. [src: arc:@threats-pivot; note:n08§2.4; note:n08§5#25] (candidate)

Design-time question that would have flagged it: "In a pilot sample, what
share of units carry the link this question needs, and can any amount of
further crawling raise it?" If the share is low and the cause structural,
TH-04 applies before collection starts: scope the question to linked
units, or drop it, and write the threat now.

## 4. Theory route

### 4.1 Result and proof technique

State, in two sentences each:

- **The result**: the theorem in its strongest honest form, with every
  assumption in the statement (MT-01).
- **The proof technique**: the main idea that makes the proof work, and
  whether it is new, a new combination, or a known technique applied to a
  new object.

A theorem paper's contribution is the pair. A known technique giving an
expected result is weak; a new technique giving a modest result can be
strong if the technique is reusable. [src: note:n01§5.2] (candidate)

### 4.2 Theory checks

- Is the result already known, a special case of a known result, or an
  immediate corollary? Search for it (Step 2 retrieval), including under
  other names.
- Are the assumptions so strong that the result becomes trivial? Say what
  fails when each is dropped, where known. [src: skill:paper] (confirmed)
- Where is the key step of the proof, and is it done, sketched, or open?
  An open key step is the fatal-flaw candidate; record it as such.
- Which cited results does the proof depend on, and are they traced to
  sources (MT-07)?
- Proof status words: "no obvious issues found" after a review, never
  "verified"; "formally verified" only for proofs that compiled in a proof
  assistant (MT-08). [src: skill:proof-review-math; skill:formalize-lean4] (confirmed)
- The proofs are the evidence; never mark the idea thin because it has no
  experiments. [src: up:skills/pre-submission-reviewer/SKILL.md] (confirmed)

### 4.3 Substitute scoring dimensions

| Dimension | Question |
|---|---|
| Significance of the result | What does the field know afterwards that it did not know before? |
| Strength of the technique | Is the technique new and reusable beyond this result? |
| Generality | How weak can the assumptions be made? |
| Proof readiness | Key step done, sketched, or open |
| Feasibility | Can the open steps be closed in the lifecycle and with the author's background? |

## 5. Output blocks

Empirical-study route (section 5b of the evaluation):

```
| Item | Plan | Gap or risk | Checklist ID |
|---|---|---|---|
| RQ set | ... | ... | |
| Population and frame | ... | ... | TH-01 |
| Sampling | ... | ... | |
| Constructs | ... | ... | SE-03, SE-04 |
| Agreement plan | ... | ... | IN-04, IN-08 |
| Data availability | ... | ... | AR-08 |
| Design-time threats | mechanism per threat | ... | TH-04, TH-08 |
```

Theory route:

```
Result: <statement with assumptions>
Technique: <main idea; new / new combination / known>
| Check | Finding | Severity |
|---|---|---|
| Already known? | ... | |
| Assumption strength | ... | |
| Key step status | ... | |
| Cited dependencies | ... | MT-07 |
```

## 6. Sources

Rule sources are inline. Design rationale for both routes: the upstream
skill has no empirical-study, mathematics or statistics paradigm
[src: note:n01§3.5; note:n01§5.2] (confirmed); the routes follow the
approved design for this skill.
