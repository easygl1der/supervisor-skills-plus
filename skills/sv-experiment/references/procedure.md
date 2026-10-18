<!-- Moved from skills/experiment-workflow/SKILL.md by ADR 0021 (2026-10-18); licence CC-BY-NC-SA-4.0. Section text unchanged; pointers updated. -->

# Experiment Workflow

## Contents

- Overview
- When to use this skill
- When NOT to use this skill
- Step 0: Load context
- Step 1: Freeze
- Step 2: Sample and gold
- Step 3: Model and prompt versions, acceptance bar
- Step 4: Disagreements become rules
- Step 5: Runs log
- Step 6: Numbers to paper
- Step 7: State files over dashboards
- Step 8: Data placement and backend
- Step 9: Replication artifact
- Step 10: Verified numbers go to STATUS first
- Checklist
- Outputs
- Hand-offs

## Overview

A paper's numbers are only as good as the trail behind them. This skill
keeps that trail: what data was frozen, what was fixed before results were
seen, which run produced which number with which code and data, where the
data lives, and how a reviewer can rerun it without learning who the
authors are.

Evidence base: one empirical SE study whose best practices (a recorded
corpus freeze, a prompt version log with rollbacks, a run script that
refused to start below the bar, an exact cell-by-cell table check) and worst
failures (a human-agreement value with no computation behind it, held-out
gold corrected after model output was seen, analysis code missing from the
package, an author-naming project page in the artifact) both came from this
stage (`note:n08` §2, §5 #15-#28, #39; `note:n04` §5 S1-S5; `note:n07` §A.1).

The steps are field-neutral. Gold sets, agreement and prompt versions apply
when people or models label data (common in SE/MSR and AI/ML); a
mathematics or theory project uses only the runs log, numbers file and
artifact steps, if any.

## When to use this skill

- Designing a study: corpus, sampling, gold set, codebook.
- Labelling with people or models; changing a prompt or model.
- Starting, finishing or failing a run.
- Putting numbers, tables or figures into the paper.
- Deciding where data lives; choosing local, Colab or a VPS.
- Building, anonymizing or refreshing the replication package.

## When NOT to use this skill

- Judging whether the study is worth doing: `sv-idea`.
- Writing the method or results prose: `sv-write-section` (it reads the claim
  ledger and the verified numbers this skill produces).
- Recording a decision or updating STATUS in general: `sv-supervisor-records`
  (this skill calls it for ADRs and STATUS rows).
- Full pre-submission review: `sv-review-once` (it reruns the
  `artifact`, `double-blind` and `integrity` checklists).

## Step 0: Load context

1. Load `research-core`: `references/core/integrity.md`,
   `references/core/records.md`, `references/core/claims-evidence.md`, the
   field profile named by `research.yaml` `field`, the venue profile, and the
   checklists `integrity.md`, `artifact.md` and `double-blind.md`.
2. Read `research.yaml`: `experiments` (backend, notebook, runs_log), `data`
   (location, manifest, lfs_patterns), `repos.research`, `repos.artifact`,
   `source_of_truth.numbers`, `review.double_blind`, `stage`.
3. If `research.yaml` is missing, offer `sv-supervisor-init`. If
   `docs/runs.md` is missing, copy `research-core`
   `assets/templates/runs-log.md`.

## Step 1: Freeze

Record the corpus snapshot id, time window and cutoff, population count and
how it was counted, and the selection criteria in an ADR (draft it, show it,
write it after approval, through `sv-supervisor-records`). Never extend the
corpus silently; an extension is a new ADR and every printed identifier is
updated in the same pass.

## Step 2: Sample and gold

1. Document the sampling design, strata, allocation, seed and draw script
   before drawing. Keep superseded runs, marked.
2. Write the codebook version and gold protocol before labelling.
3. Split off the held-out set with a recorded seed. **Freeze the held-out
   labels (commit and hash) before any model output on them is viewed.**
   Any later correction is logged item by item, results are reported before
   and after, and the correction is disclosed.
4. Record agreement only from raw, independent label sets kept in the repo,
   recomputed by a script that writes to the numbers file. No raw sets, no
   inter-rater value: describe what was done instead.
5. Name each agreement value by comparison (human with human, model with
   reference, run with run, the bar). A value seen in a sketch, a reference
   figure or a chat is not data.

## Step 3: Model and prompt versions, acceptance bar

1. Keep a version log: version, date, one-line change, model id and
   settings, held-out agreement per dimension and run, bar met, kept or
   rolled back with the reason. Rolled-back versions stay.
2. Lock the model and settings in an ADR; the method reports the same.
3. Write the acceptance bar (metric, threshold, runs, split) before the run.
   The run script enforces it and refuses to start the large run otherwise.
   A bar changed after results is a new ADR and is disclosed.

## Step 4: Disagreements become rules

Each annotation trap found in gold review becomes a numbered rule
(`L001`, `L002`, ...) in a tracked file such as
`rules/annotation-rules.md`, with the items that showed it and the prompt
version that added it. Never keep the rule file local-only.

See also `freeze-and-gold.md`

## Step 5: Runs log

Every run gets a row in `docs/runs.md` when it starts: run id, date,
purpose, command or notebook plus cells, code commit, data version, backend
and environment, status (`ran`, `failed`, `partial`, `superseded`),
outputs, notes. Failed runs are recorded, never deleted. Outputs go under
`outputs/<run id>/` and are never overwritten by a later run.

## Step 6: Numbers to paper

1. Scripts write `numbers.json` (path from `source_of_truth.numbers`) with
   `_meta.code_sha` and `_meta.data_sha`. No placeholders.
2. Tables, figures and the claim ledger read that file. Numbers inside
   figures follow the same rule.
3. Mark each printed number in the TeX with `%num:<key>` (or print through
   a key macro), then diff against the TeX before every hand-over and
   before submission:

```bash
python scripts/numbers_check.py analysis/numbers.json paper/ [--key-macro val] [--all-ints]
```

   `MISMATCH`, `UNKNOWN-KEY` and `NO-SHA` block; `NO-KEY` lists numbers in
   the TeX with no key, each to be traced or removed; `UNUSED` lists keys
   never printed (a dropped result or a missing marker).

## Step 7: State files over dashboards

The authoritative state of labels, queues and reviews is a diffable file
(database export, state JSON). A web UI is a view. Export after every
session, commit the export, cite the file and its hash in STATUS.

See also `runs-and-numbers.md`

## Step 8: Data placement and backend

1. Place files by kind: code and small tables (< 5 MB) in git; binaries
   over 5 MB in Git LFS; raw corpora, databases and model outputs on an
   external host; secrets nowhere. Every external file has a row in
   `data/MANIFEST.tsv` with bytes, sha256, source, licence and how to fetch.

```bash
python scripts/manifest.py build data/
python scripts/manifest.py verify --data-dir data/
```

2. Backend from `experiments.backend`:
   - `local`: clean tree, lock file hash, logs under the run id.
   - `colab`: no project evidence; use the owner's `colab-mcp-workflow`
     skill or a Colab CLI if one is installed, else ask the user to run the
     cells. The notebook clones the repo at a commit and runs committed
     scripts; record notebook URL, runtime and cells.
   - `vps`: ssh alias, repo at a commit, data by manifest, managed services
     for long jobs, keys never printed, outputs copied back.

See also `data-and-backends.md`

## Step 9: Replication artifact

1. Build the package from a manifest of paths, not by copying the research
   repo: code that regenerates every printed number, data or a download
   script with the manifest, codebook, rules, labels, prompts and outputs,
   and a README. Move analysis code in the day it is written.
2. Run it from a clean clone following the README alone; run
   `numbers_check.py` on the regenerated numbers file.
3. Anonymize (double-anonymous venues):

```bash
python scripts/anon_grep.py artifact/ --terms-file private/identity-terms.txt --allow "<mirror domain>" --git-log
```

   It reports names and terms, e-mails, home paths, account URLs, author
   fields in LICENSE, CITATION and package metadata, PDF metadata, rendered
   pages and git config. Check the hosting account name, repository
   description and image metadata by hand. Use a complete README, not a
   project page.
4. Publish through an anonymous mirror; link only the mirror. After every
   change, refresh the mirror and rerun the search on the mirrored copy.
5. The package holds code and data from the first day after the deadline.

See also `replication-artifact.md`

## Step 10: Verified numbers go to STATUS first

A number is verified when its script ran from a clean tree and its output
was checked. Write the row in `docs/STATUS.md` "Verified numbers" (claim id,
value, script, output file, code commit, data version, date) through
`sv-supervisor-records`. Only then does it go into the claim ledger and the
paper.

## Checklist

Run from `research-core`:

- `integrity`: IN-01 to IN-12 (traceable numbers, figure numbers, frozen
  identifiers, raw label sets, named agreement values, reporting rule,
  frozen reference, bars before the run, planned analyses, prompt log, rule
  file, AI-use disclosure).
- `artifact`: AR-01 to AR-09.
- `double-blind`: DB-03 to DB-08 when `review.double_blind` is true.
- `records`: RC-09 (dashboards are views).
- Field additions whose `Scope` matches (for example the AI/ML profile's
  repeated-runs items).

Report each item as `pass`, `fail`, `n/a` or `unknown` with evidence: the
script output, the commit, the file and line. A tick without evidence is
`unknown`.

## Outputs

- ADRs: freeze, sampling, gold protocol, model lock, acceptance bar,
  reporting rule.
- `docs/runs.md`; version log next to the prompts; numbered rule file.
- `analysis/numbers.json` with code and data SHAs; `numbers_check.py`
  report.
- `data/MANIFEST.tsv`; artifact repository and anonymous mirror;
  `anon_grep.py` report.
- Rows in `docs/STATUS.md` "Verified numbers" and "Runs".

## Hand-offs

- ADRs, STATUS and TODO updates: `sv-supervisor-records`.
- Method and results prose from verified numbers: `sv-write-section`.
- Figures from the numbers file: `sv-figure-design`.
- Design-time threats and data gaps: `sv-idea`; final threats,
  artifact and anonymity review: `sv-review-once`.
- Expert advice on an experiment: `sv-feedback-revise` guidance mode.
- After the project: `sv-supervisor-harvest`.
