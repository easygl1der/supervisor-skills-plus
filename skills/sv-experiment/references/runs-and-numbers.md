# Runs log, numbers file and state files

## Contents
1. Runs log
2. The numbers file
3. Checking the TeX against the numbers file
4. Verified numbers before the paper
5. State files over dashboards

## 1. Runs log

`docs/runs.md` (template: `research-core` `assets/templates/runs-log.md`).
One row per run, appended when the run starts and completed when it ends:

| Field | Content |
|---|---|
| Run id | `RUN-<YYYYMMDD>-<nn>` or the job name; used in commits and TODO links |
| Date | start date and time with timezone |
| Purpose | one line: which question, which version |
| Command / notebook | exact command line, or notebook URL plus cell range |
| Code commit | `git rev-parse --short HEAD` of the research repo; a dirty tree is recorded as `<sha>-dirty` and not used for printed numbers |
| Data version | snapshot id, manifest hash or split file hash |
| Backend | `local`, `colab`, `vps:<host alias>` and the environment (Python version, lock file hash, GPU type) |
| Status | `ran`, `failed`, `partial`, `superseded` |
| Outputs | output paths (under `outputs/<run id>/`) |
| Notes | why it failed, what it superseded, the ADR it belongs to |

Rules:
- Failed and partial runs are recorded, never deleted. A failure explains
  later choices and prevents re-running the same mistake.
- A row is written by the run script or the agent at start time, not
  reconstructed later.
- Each run writes its outputs under its own id; a later run never overwrites
  an earlier run's outputs.
[src: note:n08§2; note:n04§5] (candidate)

## 2. The numbers file

Every number printed in the paper comes from a script. The scripts write
one file, `analysis/numbers.json` (path from `research.yaml`
`source_of_truth.numbers`):

```json
{
  "_meta": {
    "code_sha": "3f2a91c",
    "data_sha": "sha256 of the frozen input or its manifest",
    "run_id": "RUN-20261001-03",
    "generated": "2026-10-01T14:02+08:00",
    "scripts": ["scripts/rq1.py", "scripts/agreement.py"]
  },
  "rq1_share_type_a": {"value": 0.4312, "scale": 100},
  "heldout_kappa_model_vs_gold_run1": 0.78,
  "n_corpus": 12345
}
```

- Keys name the comparison (`..._model_vs_gold_...`, `..._human_vs_human_...`)
  so agreement values cannot be merged by accident.
- `_meta.code_sha` and `_meta.data_sha` are real values. A placeholder such
  as "insert SHA here" left in a checklist was the gap in the evidence
  project's otherwise exact table check.
  [src: arc:01-checklist/CHECKLIST-UPDATE-SUMMARY.md; note:n08§5#17] (confirmed)
- Tables and figures read the same file. Numbers drawn inside figures follow
  the same rule. [src: note:n07§A.1] (confirmed)
- Put copyable numbers and tables into the manuscript before drafting prose
  around them. [src: arc:04-comms/20260920-msritp-meeting/README.md; note:n08§5#28] (candidate)

Optional: generate a macro file from the numbers file
(`\newcommand{\nCorpus}{12{,}345}`) and print numbers through macros; then a
mismatch can only be a stale build.

## 3. Checking the TeX against the numbers file

Mark each printed number in the TeX with a trailing comment:

```latex
Model and gold agree with $\kappa = 0.78$ on the held-out set. %num:heldout_kappa_model_vs_gold_run1
```

Run before every hand-over and before submission:

```bash
python scripts/numbers_check.py analysis/numbers.json paper/ [--key-macro val] [--all-ints]
```

Output kinds:

| Kind | Meaning | Blocks? |
|---|---|---|
| `MISMATCH` | marked number differs from the file | yes |
| `UNKNOWN-KEY` | marker or macro names a key that does not exist | yes |
| `NO-SHA` | `_meta` lacks a real code or data SHA | yes |
| `ROUNDED` | printed value is the stored value rounded | no |
| `UNMARKED` | number equals a key but has no marker; add one | warning |
| `NO-KEY` | decimal, percentage or separated number with no key | warning: trace it or remove it |
| `UNUSED` | key never marked | warning: a dropped result or a missing marker |

Record the run (command, commit, summary line) in `docs/log/` and the
result in STATUS. The evidence project's one exact table check (every cell
of a matrix against its script) is the model; its final audit found many
printed numbers not reproduced by the replication outputs.
[src: arc:01-checklist/CHECKLIST-UPDATE-SUMMARY.md; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md; note:n08§2] (confirmed)

## 4. Verified numbers before the paper

A number is verified when its script ran from a clean tree, the output was
checked, and the row is in `docs/STATUS.md` "Verified numbers" (claim id,
value, script, output file, code commit, data version, date). Only then does
it enter the paper or the claim ledger (`sv-write-section`). Update STATUS
through `sv-supervisor-records` (replace the row; never append a second value).
[src: note:n08§5#17] (confirmed)

## 5. State files over dashboards

The authoritative state of labels, reviews and queues is a file that can be
diffed: a database export, a state JSON, a TSV in git. A web UI or dashboard
is a view. In the evidence project the live annotation UI showed a far
smaller completed count than the local database and the state file, because
the server copy had never been re-imported; the resolution was to trust the
exported file. [src: arc:11-mining-github-issue-audit/tree/docs/notes/20260812-review-status-199-vs-582.md; note:n08§5#24] (confirmed)

- Export after every labelling session; commit the export.
- Importers stop on conflicting keys instead of overwriting.
  [src: arc:11-mining-github-issue-audit/tree/collaboration/README.md] (candidate)
- Back up databases before every import.
- STATUS cites the file and its hash, not the dashboard.
