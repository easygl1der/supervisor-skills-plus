# Checklist: threats

Items for threats to validity and for the limits of what the study can
claim. Run at design time to flag threats early, and before submission to
check that threats and results agree.

Run by: sv-idea, sv-review-once

## Contents
1. Scope and generality
2. Measurement and reference data
3. Alternative explanations and selection
4. Threats agree with results

## 1. Scope and generality

### TH-01 General claims scoped in claims and in threats
- [ ] Check: Every general claim names what was covered (populations,
  sources, groups), and threats name the dominant contributor and any major
  group the study does not cover.
- Why: Reviewers test generality claims against what was sampled.
- Status: candidate
- Scope: core
- Owner: sv-idea, sv-review-once, sv-write-section
- Src: arc:CF-16@v2; arc:TH-02@v2; arc:TH-10@v2; arc:01-checklist/checklist.md C7; arc:@advisor-glimpse

### TH-02 Stratify before pooling
- [ ] Check: Pooled results were checked per group first; when the pooled
  result does not hold in every group, or groups differ in size so that
  pooling changes the direction, the text and threats say so.
- Why: Pooling across unequal groups can reverse a result.
- Status: candidate
- Scope: core
- Owner: sv-review-once, sv-experiment, sv-review-loop
- Src: arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H2; arc:01-checklist/checklist.md W5; arc:msr:24d8c65

### TH-03 Small counts disclosed where used
- [ ] Check: When a claim rests on a small held-out or rare-class count, the
  count is given next to the claim.
- Why: A share of a handful of cases reads as a strong result without its count.
- Status: candidate
- Scope: core
- Owner: sv-review-once, sv-write-section
- Src: arc:CF-15@v2; arc:TH-04@v2

### TH-04 Data gaps moved to threats early
- [ ] Check: A data gap that more collection cannot close is moved to threats
  with its mechanism at design time, and the team stops chasing it.
- Why: Chasing an unclosable gap cost weeks; stating its mechanism costs a paragraph.
- Status: candidate
- Scope: core
- Owner: sv-idea, sv-experiment, sv-supervisor-brief
- Src: arc:@threats-pivot; note:n08§5#25

## 2. Measurement and reference data

### TH-05 Low-agreement measures described as readings
- [ ] Check: Measures whose agreement is below the stated bar are described
  as the annotator's or model's reading, not as ground truth, wherever they
  are used.
- Why: Treating a weak measure as fact overstates every claim built on it.
- Status: confirmed
- Scope: core
- Owner: sv-review-once, sv-write-section, sv-review-loop
- Src: arc:CF-14@v2; arc:TH-05@v2; arc:01-checklist/checklist.md C3; arc:msr:643836a; note:n06§2.6; user:2026-10-13 (promoted: failure had a clear bad outcome)

### TH-06 Reference labels are not an oracle
- [ ] Check: Threats state that reference labels are a consensus of the study
  authors, not an oracle; any correction or metric that assumes a perfect
  reference says so.
- Why: Errors in the reference set bound every accuracy figure.
- Status: candidate
- Scope: core
- Owner: sv-review-once, sv-experiment
- Src: arc:TH-09@v2; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H13

### TH-07 Compared measures are comparable
- [ ] Check: Where the paper compares its numbers with prior work, it notes
  when the measures or populations differ.
- Why: Comparing unlike measures is a common reviewer objection.
- Status: candidate
- Scope: core
- Owner: sv-review-once, sv-write-section
- Src: arc:CF-19@v2

## 3. Alternative explanations and selection

### TH-08 Alternative explanations named
- [ ] Check: For each main finding, plausible alternative explanations the
  design cannot rule out are named in discussion or threats.
- Why: Reviewers supply alternatives the authors did not; naming them first
  shows the authors saw them.
- Status: candidate
- Scope: core
- Owner: sv-idea, sv-review-once
- Src: arc:TH-07@v2; arc:TH-08@v2; unverified (source of the original items)

### TH-09 Selection effects of filtered subsets
- [ ] Check: Where rates from a filtered subset are cited, the selection
  effect of the filter is stated in the same place.
- Why: A filter can create the pattern it seems to reveal.
- Status: candidate
- Scope: core
- Owner: sv-review-once, sv-experiment
- Src: arc:RS-16@v2; unverified (source of the original item)

### TH-10 Contradicting results kept
- [ ] Check: No result that contradicts the paper's framing was dropped; such
  results are reported and discussed.
- Why: Dropping inconvenient results is selective reporting.
- Status: confirmed
- Scope: core
- Owner: sv-review-once, sv-experiment, sv-review-loop
- Src: arc:CF-18@v2; user:2026-10-13 (promoted: failure had a clear bad outcome)

## 4. Threats agree with results

### TH-11 Threat statements are true of the paper
- [ ] Check: Every mitigation a threat paragraph claims (for example "we
  report per group before pooling") is actually done in the results.
- Why: A threat paragraph that promises an analysis the paper lacks is easy
  to catch.
- Status: confirmed
- Scope: core
- Owner: sv-review-once, sv-review-loop
- Src: arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H12; user:2026-10-13 (promoted: failure had a clear bad outcome)
