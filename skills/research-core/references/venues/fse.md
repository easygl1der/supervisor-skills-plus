# Venue profile: FSE (ACM International Conference on the Foundations of Software Engineering), research track, recurring

Status: draft
Call URL: https://conf.researchr.org/track/fse-2027/fse-2027-papers (the
2027 call; the URL changes every year)
Fetched: 2026-10-01, by WebFetch, which returns a model-written extraction,
not a raw copy. Re-fetch before every submission and for every new year.
Field: SE

## Contents
Dates; Format; Review model; Required sections and statements; Desk-reject
causes; Submission system; Style from exemplars; Checklist additions
(FS-01 to FS-14); Changelog.

Quotes and close paraphrases below come from the dated extraction
[src: arc:10-requirements/venue/fse-2027-requirements.md]. Items the
extraction left unclear are marked CONFIRM. Dates hold for one cycle only:
re-fetch them from the new call each year; never reuse a date heard in a
meeting [src: note:n04§1.1; note:n08§5].

## Dates
| Item | Value | Source |
|---|---|---|
| Paper submission (FSE 2027 cycle) | Fri 2 Oct 2026, AoE (UTC-12) | arc:10-requirements/venue/fse-2027-requirements.md |
| Abstract registration, notification, revision dates | Not in the extraction. CONFIRM | none |
| Next cycle | Unknown until the new call is fetched | none |

In the evidence project a meeting gave a wrong deadline; the dated fetch
settled it. The submission site went down near the deadline and reopened
later, which the organizers announced. [src: note:n08§3]

## Format
- ACM template, single column:
  `\documentclass[acmsmall,screen,review,anonymous]{acmart}`, from
  `sample-acmsmall-conf.tex`. Numeric or author-year citations are both
  allowed. [src: arc:10-requirements/venue/fse-2027-requirements.md] (confirmed)
- Initial submission: at most 18 pages for all text and figures, plus 4
  pages for references. Major revision: 20 plus 4.
  [src: arc:10-requirements/venue/fse-2027-requirements.md] (confirmed)
- Appendices count toward the 18 pages: a co-author quoted the call as
  covering "all text, figures, and appendices". The model extraction omits
  appendices. CONFIRM on the live page.
  [src: arc:chat:1on1@2026-09-22T05:02; arc:CF-24@v2]
- Do not change template fonts, margins or spacing, and do not shrink
  fonts locally (`\footnotesize` in tables, small `\tabcolsep`); senior
  co-authors treated this as a format violation and so a desk-reject risk.
  [src: arc:chat:group@2026-10-01T09:23; note:n08§3] (candidate)
- Every figure carries `\Description{}` matching its actual layout (ACM).
  [src: note:n07§A.8 FR18] (candidate)
- Supplementary material: the replication package, linked through an
  anonymous mirror, not an appendix. [src: note:n08§3] (candidate)

## Review model
- Double-anonymous. Remove author names and affiliations; write
  self-citations in the third person; anonymize URLs to author-revealing
  sites (tools, datasets) and organization names that reveal affiliation;
  acknowledgements are discouraged at submission.
  [src: arc:10-requirements/venue/fse-2027-requirements.md] (confirmed)
- Preprints are allowed but must not state the FSE submission.
  [src: arc:10-requirements/venue/fse-2027-requirements.md] (confirmed)
- Everything a reviewer can open counts: the anonymous artifact's README,
  licence, rendered project page, repository description and PDF metadata.
  A complete README is safer than a rendered project page.
  [src: arc:chat:group@2026-10-06T05:09; arc:chat:group@2026-10-02T00:45; note:n08§3] (candidate)

## Required sections and statements
- **Data Availability**: a section with this title after the Conclusion,
  saying whether a replication package is available, or why not. It does
  not count toward the page limit. CONFIRM whether it must be anonymized at
  submission: the extraction called it "non-anonymous".
  [src: arc:10-requirements/venue/fse-2027-requirements.md] (confirmed)
- **AI use**: AI help with writing needs no disclosure. AI that assisted
  methodology, data generation, coding or analysis the conclusions rely on
  is described in detail in the methods section.
  [src: arc:10-requirements/venue/fse-2027-requirements.md] (confirmed)
- Prohibited: fabricated citations, hallucinated results, plagiarism, and
  prompt injection aimed at reviewers.
  [src: arc:10-requirements/venue/fse-2027-requirements.md] (confirmed)

## Desk-reject causes
- Not following the formatting rules.
- Fabricated or hallucinated citations.
- Breaking the anonymity rules.
[src: arc:10-requirements/venue/fse-2027-requirements.md] (confirmed)

## Submission system
- HotCRP form. Its abstract field takes plain text: no LaTeX macros or
  labels. [src: arc:chat:group@2026-10-03T18:37; arc:msr:4af1aff; note:n08§3] (candidate)
- Conflicts with program-committee members: the form forces an explicit
  choice; the co-author who knows the institutional ties enters them.
  Authors, conflicts, topics and corresponding author are done a day early.
  [src: arc:chat:group@2026-10-03T17:28; note:n08§3] (candidate)
- Topic choice: the evidence project picked the maintenance and evolution
  topic over a looser fit. [src: arc:chat:group@2026-10-01T21:05] (candidate)
- Upload a complete PDF well before the deadline, then replace it.
  [src: arc:chat:group@2026-10-03T19:45; note:n08§5] (candidate)

## Style from exemplars
Not yet filled by `sv-write-style-mine` from accepted FSE papers. Until it is, use
the SE field profile's typical structure, which was measured on one
submission to this track, not on accepted papers. Contribution-list format
at FSE: Unknown. [src: note:n06§3; note:n02§10]

## Checklist additions

### FS-01 Call re-fetched for this year
- [ ] Check: A dated copy of this year's call exists in the project, and every date in plans comes from it.
- Why: Calls and dates change every cycle; a meeting once gave a wrong deadline.
- Status: confirmed
- Scope: venue:fse
- Owner: sv-supervisor-brief, sv-supervisor-records, sv-review-once
- Src: arc:10-requirements/venue/fse-2027-requirements.md; note:n08§3

### FS-02 Page budget counted on the PDF
- [ ] Check: On the compiled PDF, all text, figures, tables and any appendix fit in 18 pages (20 for a major revision), references in 4 more; Data Availability excluded.
- Why: The limit is all-in; the evidence team lost track of it while cutting and refilling.
- Status: confirmed
- Scope: venue:fse
- Owner: sv-review-once, sv-write-polish
- Src: arc:10-requirements/venue/fse-2027-requirements.md; arc:chat:1on1@2026-09-22T05:02; note:n06§2.11

### FS-03 No appendix as padding
- [ ] Check: No appendix fills pages; useful content moves into the body, the rest into the replication package with a pointer.
- Why: Senior co-authors expected reviewers to skip it and read padding as a rejection signal.
- Status: confirmed
- Scope: venue:fse
- Owner: sv-write-polish, sv-write-style-apply, sv-review-once
- Src: arc:chat:group@2026-10-01T08:56; arc:chat:group@2026-10-02T01:51; arc:msr:464168f; user:2026-10-13 (promoted: failure had a clear bad outcome)

### FS-04 Page shortfall filled by priority
- [ ] Check: A short paper is filled by expanding thin results with explanation and examples, then method detail, then background gaps, then implications and threats.
- Why: Removing the appendix left the evidence paper a page short a day before the deadline.
- Status: candidate
- Scope: venue:fse
- Owner: sv-write-polish, sv-supervisor-brief
- Src: arc:chat:group@2026-10-02T22:44; arc:msr:d0d4c03; note:n06§2.11

### FS-05 Template untouched
- [ ] Check: The document class line is exactly `acmsmall,screen,review,anonymous`; no font, margin or local size changes appear anywhere, rechecked after the last edit.
- Why: Format violations are a desk-reject cause; a local shrink came back after it was removed once.
- Status: confirmed
- Scope: venue:fse
- Owner: sv-review-once, sv-write-polish
- Src: arc:10-requirements/venue/fse-2027-requirements.md; arc:chat:group@2026-10-01T09:23; note:n08§3

### FS-06 Figure descriptions
- [ ] Check: Every figure has `\Description{}` that matches its layout.
- Why: ACM accessibility metadata; a stale description misstated a panel layout.
- Status: candidate
- Scope: venue:fse
- Owner: sv-figure-design, sv-review-once
- Src: note:n07§A.8 FR18

### FS-07 Data Availability section
- [ ] Check: A "Data Availability" section follows the Conclusion, links the package (anonymous mirror at submission, CONFIRM) and lists only what the package holds.
- Why: Required by the call; the evidence draft first overclaimed what the package recomputed.
- Status: confirmed
- Scope: venue:fse
- Owner: sv-experiment, sv-review-once
- Src: arc:10-requirements/venue/fse-2027-requirements.md; arc:msr:24d8c65

### FS-08 AI use in methods
- [ ] Check: Every AI use the conclusions rely on (labeling, gold construction, analysis code) is described in the methods section with model, version, settings and prompts.
- Why: Required by the call; undisclosed AI help in gold construction was an open risk in the evidence project.
- Status: confirmed
- Scope: venue:fse
- Owner: sv-experiment, sv-write-section, sv-review-once
- Src: arc:10-requirements/venue/fse-2027-requirements.md; note:n08§3

### FS-09 Anonymous artifact mirror
- [ ] Check: The PDF links only the anonymous mirror; the mirrored README, licence, description and metadata carry no names, labs or personal domains; the mirror is refreshed and re-checked after every artifact change.
- Why: Author-revealing URLs break the anonymity rules; a rendered project page nearly did after submission.
- Status: confirmed
- Scope: venue:fse
- Owner: sv-experiment, sv-review-once
- Src: arc:10-requirements/venue/fse-2027-requirements.md; arc:chat:group@2026-10-02T00:45; arc:chat:group@2026-10-06T05:09

### FS-10 Third-person self-citation and preprint wording
- [ ] Check: Self-citations are in the third person, no acknowledgements remain, and any preprint does not mention FSE.
- Why: Stated anonymity rules.
- Status: confirmed
- Scope: venue:fse
- Owner: sv-review-once
- Src: arc:10-requirements/venue/fse-2027-requirements.md

### FS-11 Plain-text abstract in the form
- [ ] Check: The abstract pasted into the submission form is plain text with no macros, labels or LaTeX commands.
- Why: Macros in the form abstract render as raw commands.
- Status: confirmed
- Scope: venue:fse
- Owner: sv-review-once
- Src: arc:chat:group@2026-10-03T18:37; arc:msr:4af1aff; user:2026-10-13 (promoted: failure had a clear bad outcome)

### FS-12 Form metadata a day early
- [ ] Check: Authors, conflicts, topics and corresponding author are entered at least a day before the deadline, conflicts by the co-author who knows the ties.
- Why: Conflict entry took hours on deadline day in the evidence project.
- Status: confirmed
- Scope: venue:fse
- Owner: sv-supervisor-brief, sv-review-once
- Src: arc:chat:group@2026-10-03T17:28; note:n08§5; user:2026-10-13 (promoted: failure had a clear bad outcome)

### FS-13 Upload early
- [ ] Check: A complete PDF is uploaded well before the deadline and replaced later if needed.
- Why: The editor and the submission site both failed near the deadline.
- Status: confirmed
- Scope: venue:fse
- Owner: sv-supervisor-brief, sv-review-once
- Src: arc:chat:group@2026-10-03T19:45; arc:chat:group@2026-10-03T23:18; note:n08§5; user:2026-10-13 (promoted: failure had a clear bad outcome)

### FS-14 Citations verified
- [ ] Check: Every reference is checked against DBLP or the publisher, with the audit kept.
- Why: Fabricated citations are a listed desk-reject cause.
- Status: confirmed
- Scope: venue:fse
- Owner: sv-write-section, sv-review-once
- Src: arc:10-requirements/venue/fse-2027-requirements.md; arc:chat:group@2026-09-29T11:44

## Changelog
- 2026-10-13: created from the dated 2026-10-01 extraction of the FSE 2027
  call and the evidence project's submission lessons.
