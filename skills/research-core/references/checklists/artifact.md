# Checklist: artifact

Items for the replication package: that it holds what the paper promises,
builds from a clean clone, regenerates the printed numbers and is in place
when reviewers look.

Run by: experiment-workflow, pre-submission-reviewer

## Contents
1. Completeness
2. Build and reproduction
3. Hosting and timing
4. Statements about the artifact

## 1. Completeness

### AR-01 The package holds what the paper promises
- [ ] Check: Everything the paper says is released (data, codebook,
  reference labels, prompts, model outputs, scripts) is in the package; the
  paper does not say the package "recomputes every number" unless that was
  run and checked.
- Why: Reviewers open the package to test exactly these promises.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow, pre-submission-reviewer
- Src: arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H9; arc:01-checklist/checklist.md AT5; arc:chat:group@2026-10-03T20:20; user:2026-10-13 (promoted: failure had a clear bad outcome)

### AR-02 Analysis code moves to the package the same day
- [ ] Check: Every analysis script that produced a printed number is in the
  package; scripts written late for revised findings were moved the day they
  were written.
- Why: Late analysis code was the part missing from the package at the deadline.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow
- Src: arc:chat:group@2026-10-03T20:21; arc:chat:group@2026-10-03T20:22; note:n08§5#16; user:2026-10-13 (promoted: failure had a clear bad outcome)

### AR-03 No secrets or frozen copies in the wrong repository
- [ ] Check: No secrets, tokens, credentials or local databases are committed
  to any repository; frozen data is not copied into the manuscript repository.
- Why: Secrets leak with the artifact; data copies drift from the frozen version.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow, research-records
- Src: arc:RP-04@v2; arc:FP-04@v2; arc:FP-05@v2; arc:01-checklist/checklist.md AT7; user:2026-10-13 (promoted: failure had a clear bad outcome)

## 2. Build and reproduction

### AR-04 Clean build from a fresh clone
- [ ] Check: A fresh clone builds the paper and runs the analysis following
  the build document alone, and the build document lists the current figure set.
- Why: Hidden local state is found only by a fresh clone.
- Status: candidate
- Scope: core
- Owner: experiment-workflow, pre-submission-reviewer
- Src: arc:RP-05@v2; arc:RP-06@v2; arc:01-checklist/checklist.md G5

### AR-05 Script output matches the manuscript
- [ ] Check: Running the package scripts reproduces the numbers printed in
  the manuscript; the comparison (script output against text and tables) is
  recorded with zero unexplained mismatches.
- Why: A traceable number is only trusted once its script output was compared.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow, check-loop
- Src: note:n08§5#17; arc:01-checklist/CHECKLIST-UPDATE-SUMMARY.md RP-11

## 3. Hosting and timing

### AR-06 Large data on a data host with a manifest
- [ ] Check: Large raw data sits on a data host, not in a code repository,
  and a manifest lists each file with its location and checksum.
- Why: Code hosts reject or truncate large files; a manifest keeps them findable.
- Status: candidate
- Scope: core
- Owner: experiment-workflow
- Src: arc:chat:group@2026-10-03T20:24; note:n08§5#39

### AR-07 Package not empty after the deadline
- [ ] Check: The linked package is non-empty from the first day after the
  deadline; the README directory guide may follow, but code and data are there.
- Why: Reviewers may open the link as soon as they are assigned.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow, research-supervisor
- Src: arc:chat:group@2026-10-03T23:16; arc:chat:group@2026-10-02T06:36; note:n08§5#15; user:2026-10-13 (promoted: failure had a clear bad outcome)

## 4. Statements about the artifact

### AR-08 Data availability statement present and accurate
- [ ] Check: Where the venue asks for a data availability statement, it is
  present at the required place, says what is released and why anything is
  not, and follows the paper's reporting rule for numbers.
- Why: The venue requires it; an overclaiming statement is checked against
  the package.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow, pre-submission-reviewer
- Src: arc:10-requirements/venue/fse-2027-requirements.md; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md G8; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H1

### AR-09 Project page equals the paper
- [ ] Check: A project page, if any, matches the final paper (title, numbers,
  claims) and is updated in the same pass as the paper.
- Why: A stale page contradicts the paper reviewers are reading.
- Status: confirmed
- Scope: core
- Owner: experiment-workflow
- Src: arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H8; arc:01-checklist/checklist.md AT6; user:2026-10-13 (promoted: failure had a clear bad outcome)
