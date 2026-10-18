# Checklist: venue-submission

Generic items for meeting a venue's formal rules and for the submission
itself. The venue profile adds the venue's own facts (limits, template,
required sections); this file checks that they were applied.

Run by: pre-submission-reviewer

## Contents
1. The official call
2. Format
3. Build hygiene
4. Submission form and upload

## 1. The official call

### VS-01 Venue facts from the official call
- [ ] Check: Page limit, template, anonymity rules, required sections and
  deadline were taken from the official call, saved to a dated file with its
  URL, and re-read in the final week; no deadline was taken from a meeting.
- Why: A remembered deadline in the evidence project differed from the call.
- Status: confirmed
- Scope: core
- Owner: pre-submission-reviewer, research-supervisor, research-records
- Src: arc:10-requirements/venue/fse-2027-requirements.md; arc:04-comms/20260920-msritp-meeting/README.md; note:n04§1.1; note:n08§5#32

### VS-02 Desk-reject causes checked one by one
- [ ] Check: Every desk-reject cause the call lists has a pass with evidence
  (command output, page number, file and line).
- Why: Desk rejects end the submission before review.
- Status: confirmed
- Scope: core
- Owner: pre-submission-reviewer
- Src: arc:10-requirements/venue/fse-2027-requirements.md

### VS-03 Required sections present
- [ ] Check: Every section the call requires (for example data availability,
  AI-use description in the method) is present at the place the call names.
- Why: A missing required section is a formatting failure.
- Status: confirmed
- Scope: core
- Owner: pre-submission-reviewer
- Src: arc:10-requirements/venue/fse-2027-requirements.md; arc:01-checklist/checklist.md G8; arc:01-checklist/checklist.md G9

## 2. Format

### VS-04 Page limit on the compiled PDF
- [ ] Check: The page count was measured on the compiled PDF, counting what
  the call counts (body, figures, appendix) and excluding only what it
  excludes (for example references).
- Why: Over-length is a desk reject; source line counts do not tell.
- Status: confirmed
- Scope: core
- Owner: pre-submission-reviewer
- Src: arc:10-requirements/venue/fse-2027-requirements.md; arc:CF-24@v2; arc:01-checklist/checklist.md G2

### VS-05 Template and fonts untouched
- [ ] Check: The official template and class options are used unchanged; no
  font substitution, margin change or local font or spacing shrinking; the
  check is repeated after every late edit.
- Why: Template deviations violate the formatting rules; a late edit
  reintroduced shrinking in the evidence project.
- Status: confirmed
- Scope: core
- Owner: pre-submission-reviewer, sv-write-polish
- Src: arc:10-requirements/venue/fse-2027-requirements.md; arc:chat:group@2026-10-01T09:20; arc:chat:group@2026-10-01T09:23; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md G3; note:n08§5#10

### VS-06 No appendix as padding
- [ ] Check: Where the page limit includes the appendix, content that does
  not need to be in the paper (long definitions, label tables) is in the
  replication package with a pointer and, if needed, a compact table.
- Why: Reviewers do not read padding appendices, and they cost pages.
- Status: confirmed
- Scope: core
- Owner: sv-write-polish, pre-submission-reviewer
- Src: arc:chat:group@2026-10-01T08:47; arc:chat:group@2026-10-01T08:48; arc:chat:group@2026-10-01T09:26; arc:msr:464168f; note:n08§5#11; user:2026-10-13 (promoted: failure had a clear bad outcome)

### VS-07 Figure descriptions match the layout
- [ ] Check: Where the template requires figure descriptions (alt text),
  every figure has one and it matches the actual layout.
- Why: A wrong description fails the accessibility check.
- Status: candidate
- Scope: core
- Owner: figure-designer, pre-submission-reviewer
- Src: arc:MF-22@v2; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H15; note:n07§A.8 FR18

## 3. Build hygiene

### VS-08 Clean compile log
- [ ] Check: The final compile log has no undefined references or citations
  and no overfull boxes.
- Why: Each is visible in the PDF as a question mark or overrun line.
- Status: candidate
- Scope: core
- Owner: pre-submission-reviewer, sv-write-polish
- Src: arc:01-checklist/checklist.md G5; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H16

## 4. Submission form and upload

### VS-09 Submission metadata a day early
- [ ] Check: Authors, conflicts of interest, topics and the corresponding
  author were entered in the submission system at least a day before the
  deadline; the co-author who knows the community entered the conflicts.
- Why: Form problems found in the last hours compete with paper fixes.
- Status: confirmed
- Scope: core
- Owner: pre-submission-reviewer, research-supervisor
- Src: arc:chat:group@2026-10-01T21:05; arc:chat:group@2026-10-03T17:28; note:n08§5#31; user:2026-10-13 (promoted: failure had a clear bad outcome)

### VS-10 Plain-text abstract in the form
- [ ] Check: The abstract pasted into the submission form is plain text with
  no macros, labels or markup.
- Why: Macros do not compile in the form and show as raw code.
- Status: confirmed
- Scope: core
- Owner: pre-submission-reviewer
- Src: arc:chat:group@2026-10-03T18:40; arc:chat:group@2026-10-03T18:43; note:n08§5#30; user:2026-10-13 (promoted: failure had a clear bad outcome)

### VS-11 Early complete upload
- [ ] Check: A complete PDF was uploaded well before the deadline and then
  replaced by later versions.
- Why: Editors and submission systems go down near deadlines.
- Status: confirmed
- Scope: core
- Owner: pre-submission-reviewer, research-supervisor
- Src: arc:chat:group@2026-10-03T19:45; arc:chat:group@2026-10-03T19:59; note:n08§5#4; user:2026-10-13 (promoted: failure had a clear bad outcome)
