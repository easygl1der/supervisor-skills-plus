# Freeze, sample, gold, versions and rule files

## Contents
1. Freeze the corpus
2. Sample
3. Build and freeze the gold set
4. Agreement values and their raw label sets
5. Model and prompt versioning
6. Acceptance bars in the run script
7. Disagreements become numbered rules
8. Labelling decisions that come from the research question

## 1. Freeze the corpus

Write an ADR (through `research-records`) before any analysis touches the
data. It records:

- snapshot identifier (crawl id, export file name, database dump hash);
- time window and cutoff timestamp with timezone;
- population count at the cutoff, and how it was counted (query or script);
- selection criteria for sources (which repositories, datasets, archives)
  and the date the selection was made, if different from the snapshot date;
- what is out of scope.

Never extend the corpus silently. A later addition is a new ADR that
supersedes the old one, and every printed identifier (snapshot date, version
id) is updated in the same pass. In the evidence project one frozen snapshot
with a recorded cutoff was the basis of every later number, and a
repository-selection date that differed from the snapshot date had to be
recorded as an accepted decision at the final check.
[src: note:n04§5; note:n08§2] (confirmed)

## 2. Sample

Document before drawing:

- the estimand and the sampling design (simple random, stratified,
  constrained allocation) with the alternatives rejected and why;
- strata, floors and the allocation table;
- the seed and the script that draws, and the output file name;
- inclusion probabilities if estimates are weighted.

Superseded sample runs stay in the repository marked `superseded`, for
audit. [src: arc:res:4c60e71; note:n04§5] (candidate)

## 3. Build and freeze the gold set

1. Write the codebook version and the gold protocol (who labels, blind to
   what, how disagreements are adjudicated) before labelling.
2. Split off the held-out set with a recorded seed and write the split file
   (ids only) to the repository.
3. **Freeze the held-out labels before any model output on them is viewed.**
   Commit the label file and record its hash in the ADR or STATUS.
4. A correction after model output was seen is allowed only as a logged
   event: which items, old and new label, who decided, what output was seen.
   Report results before and after the correction, and disclose it in the
   method. In the evidence project a batch of held-out gold cells was changed
   after viewing model-versus-gold pages, and the agreement bar was chosen in
   the same step; the decision was recorded, the disclosure was the open risk.
   [src: arc:11-mining-github-issue-audit/tree/docs/notes/gold-review/overlay-high14-review.md; note:n08§5#20] (confirmed)
5. If an agent proposes or writes gold labels, record which labels came from
   the agent and which a human confirmed one by one. Disclose AI help in
   building reference data. [src: arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md; note:n08§5#19] (confirmed)

## 4. Agreement values and their raw label sets

Layout that makes every agreement value recomputable:

```
labels/
  gold-v<k>/annotator-1.jsonl      raw independent labels, before adjudication
  gold-v<k>/annotator-2.jsonl
  gold-v<k>/adjudicated.jsonl
  model/<prompt-version>/run-<n>.jsonl
scripts/agreement.py               reads the files above, writes numbers.json keys
```

Rules:

- An inter-rater value exists only if the independent, pre-adjudication label
  sets exist. If they do not, describe what was done (single annotator plus
  review, agent proposal plus human check) and print no inter-rater value.
- Name each value by comparison: human with human, model with reference,
  run with run (self-consistency), and the reporting bar. Never one headline
  "agreement".
- The value enters the paper through `numbers.json`, never typed by hand.
- A value seen in a sketch, a reference figure or a chat is not data. In the
  evidence project a human-agreement value first appeared in a reference
  figure image, was copied into the replica figure and into the method text
  the same night, and no computation for it was ever found.
  [src: note:n07§A.1; arc:msr:393f596; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md] (confirmed)

## 5. Model and prompt versioning

Keep a version log next to the prompts (for example `prompts/<pack>/README.md`
or `docs/model-versions.md`):

| Version | Date | Change (one line) | Model, version, settings | Held-out agreement per dimension, run 1 / run 2 | Bar met? | Kept or rolled back (reason) |
|---|---|---|---|---|---|---|

- Every prompt or model change gets a new version id, even a one-word edit.
- Rolled-back versions stay in the log with the reason.
- Lock the model (provider, exact model id, temperature, output format) in an
  ADR; the method section reports the same values.
- Decisions that a script can enforce (gate order, existence checks,
  truncation caps, retries) are coded, not prompted.

The evidence project's prompt pack kept such a log with per-version held-out
agreement for two runs and three rolled-back versions.
[src: arc:11-mining-github-issue-audit/tree/prompts/llm-annotation-v1/README.md; note:n08§5#22] (confirmed)

## 6. Acceptance bars in the run script

Write the bar (metric, threshold, which runs, which split) in the ADR or the
version log **before** the run. The large run refuses to start unless the
bar is met. The evidence project's large audit run refused to start until an
explicit flag was set after held-out agreement passed on two runs.
[src: arc:11-mining-github-issue-audit/tree/scripts/vps-hk-llm-annotate.sh; note:n08§5#21] (confirmed)

Shell pattern:

```bash
# bar written in docs/adr/NNNN-acceptance-bar.md before the first run
: "${GOLD_BAR_OK:?refusing: held-out bar not confirmed; see docs/adr/NNNN}"
```

Stronger pattern, computed instead of declared:

```python
bar = 0.75                               # copied from the ADR, with its id
scores = json.load(open("out/heldout-agreement.json"))
failed = {d: s for d, s in scores.items() if min(s["run1"], s["run2"]) < bar}
if failed:
    sys.exit(f"bar {bar} (ADR NNNN) not met: {failed}")
```

A bar changed after results were seen is a new ADR that cites the results it
saw, and the change is disclosed.

## 7. Disagreements become numbered rules

Each annotation trap found during gold review becomes a numbered rule in a
file in the repository (for example `rules/annotation-rules.md`):

```
L007 A "closing, see above" comment is not evidence of a fix. (2026-..; items: id1, id2; prompt rule added in v<k>)
```

- One id per rule, never reused; superseded rules are marked, not deleted.
- The prompt version log names the rules each version added.
- Keep the file tracked. In the evidence project the machine-readable rule
  file was kept local-only and is lost; the readable changelog survived.
  [src: arc:11-mining-github-issue-audit/tree/docs/notes/gold-review/CHANGELOG.md; arc:res:7e4a35c; note:n08§5#23] (candidate)

## 8. Labelling decisions that come from the research question

- Decide between "unknown" and "out of scope" by what the label is for: a
  question about the problem only labels missing solution evidence as
  unknown; a question about problem and solution treats it as out of scope.
  Write that rule in the approach. [src: arc:@threats-pivot; note:n08§5#26] (candidate)
- Keep the method (prompt, agreement) apart from research-question
  numbering. A question that needs only statistics gets a script, not a
  model. [src: arc:04-comms/20260920-msritp-meeting/README.md; note:n08§5#27] (candidate)
- When a data gap cannot be closed by more collection, move it to threats
  with its mechanism and stop chasing it (`idea-evaluator`,
  `pre-submission-reviewer` threats items). [src: note:n08§5#25] (candidate)
