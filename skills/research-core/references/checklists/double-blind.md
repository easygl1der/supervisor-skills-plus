# Checklist: double-blind

Items that keep author identity out of everything a reviewer can open: the
PDF, the artifact, its mirror and its metadata. Items scoped
`venue:double-anonymous` apply when `research.yaml` sets double-anonymous review.

Run by: sv-review-once, sv-experiment

## Contents
1. The paper
2. Links and the artifact
3. Private material

## 1. The paper

### DB-01 No identity in the paper body
- [ ] Check: Author names, affiliations and organization names that reveal
  the affiliation are absent from the paper body; the template's anonymous
  mode is on.
- Why: Breaking anonymity is a desk-reject ground at double-anonymous venues.
- Status: confirmed
- Scope: venue:double-anonymous
- Owner: sv-review-once
- Src: arc:10-requirements/venue/fse-2027-requirements.md

### DB-02 Self-citations, acknowledgements and preprints
- [ ] Check: Self-citations are in the third person ("prior work of X", not
  "our prior work"); acknowledgements are left out at submission; any
  preprint does not state the submission to this venue.
- Why: Each of these reveals the authors indirectly.
- Status: confirmed
- Scope: venue:double-anonymous
- Owner: sv-review-once, sv-write-polish
- Src: arc:10-requirements/venue/fse-2027-requirements.md; arc:01-checklist/checklist.md AT3

## 2. Links and the artifact

### DB-03 Only the anonymous mirror is linked
- [ ] Check: The PDF links only the anonymous mirror of the artifact, never a
  personal page, author-named account, lab page or named repository.
- Why: A link to an author-revealing site breaks anonymity.
- Status: confirmed
- Scope: venue:double-anonymous
- Owner: sv-review-once, sv-experiment
- Src: arc:10-requirements/venue/fse-2027-requirements.md; arc:chat:group@2026-10-02T00:45; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md AT2

### DB-04 Identity search across everything a reviewer can open
- [ ] Check: Names, affiliations, personal domains and lab names were
  searched for, with the command output kept, in: paper source and PDF, PDF
  metadata, artifact repository, README, licence, project page, repository
  description, account name and image metadata.
- Why: In the evidence project a project web page in the artifact named all
  authors and was found only after the deadline.
- Status: confirmed
- Scope: venue:double-anonymous
- Owner: sv-review-once, sv-experiment
- Src: arc:10-requirements/venue/fse-2027-requirements.md; arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md B2; arc:chat:group@2026-10-06T05:09; note:n08§5#12

### DB-05 README rather than a rendered project page
- [ ] Check: The anonymous artifact presents itself through a complete README
  rather than a rendered project web page.
- Why: Web pages carry names in templates and metadata that are easy to miss.
- Status: confirmed
- Scope: venue:double-anonymous
- Owner: sv-experiment, sv-review-once
- Src: arc:chat:group@2026-10-06T05:09; note:n08§5#13; user:2026-10-13 (promoted: failure had a clear bad outcome)

### DB-06 Mirror refreshed and re-checked after every change
- [ ] Check: After every artifact change, including after the deadline and
  until reviews end, the anonymous mirror was refreshed and the identity
  search re-run on the mirrored copy.
- Why: A stale mirror can hide a leak in the source, and a refresh can
  publish one.
- Status: confirmed
- Scope: venue:double-anonymous
- Owner: sv-experiment, sv-review-once
- Src: arc:01-checklist/FINAL-CHECKLIST-2026-10-02.md H8; arc:01-checklist/checklist.md AT2; note:n08§2.7; unverified (co-author origin of the item); user:2026-10-13 (promoted: failure had a clear bad outcome)

### DB-07 Artifact name and citation are venue-neutral
- [ ] Check: The artifact's name and suggested citation do not name the venue
  and stay valid for a later preprint version.
- Why: A venue name in the artifact ties the preprint to the submission.
- Status: candidate
- Scope: venue:double-anonymous
- Owner: sv-experiment
- Src: arc:01-checklist/checklist.md AT4; unverified (chat source outside the archived exports)

## 3. Private material

### DB-08 Private material never tracked
- [ ] Check: Private chats, other people's papers, review notes and personal
  files are ignored in the manuscript and artifact repositories from day one,
  and none appear in their history.
- Why: Private material in a shared repository leaks identity and other
  people's work.
- Status: confirmed
- Scope: core
- Owner: sv-supervisor-records, sv-experiment, sv-review-once
- Src: arc:msr:f1c7df8; arc:msr:c8adb43; arc:01-checklist/checklist.md AT7; note:n08§5#8; user:2026-10-13 (promoted: failure had a clear bad outcome)
