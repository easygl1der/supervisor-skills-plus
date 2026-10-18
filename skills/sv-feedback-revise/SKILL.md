---
name: sv-feedback-revise
description: >-
  Turns comments on a manuscript into tracked revisions: collects every
  comment from every channel, gives it an ID, triages it, applies one change
  per comment with the ID in the commit, keeps note markers until their owner
  closes them, verifies each claimed change against the actual diff, and
  fills the response table. Use when inline TeX notes, PDF annotations, chat
  requests or review reports arrive.
license: CC-BY-NC-SA-4.0
disable-model-invocation: true
---

# sv-feedback-revise

Mode A of the former `feedback-to-revision`. Load
`../sv-feedback/references/procedure.md`, follow its Step 0, then run
section "Mode A: Revision" (A1 to A6).

## Load by step

| Step | Load |
|---|---|
| A1 ingest, A2 triage | `intake-and-triage.md` |
| A3 apply, A5 verify | `apply-and-verify.md` |
| Examples of what goes wrong | `worked-examples.md` |

Scripts, run from the repository root:

- PDF annotations: `python skills/sv-feedback/scripts/extract_pdf_comments.py <pdf> <out_dir>`
- Inline notes and hidden markers: `python skills/sv-feedback/scripts/list_markers.py <paper_dir>`

See: ../sv-feedback/references/procedure.md
See: ../sv-feedback/references/intake-and-triage.md
See: ../sv-feedback/references/apply-and-verify.md
See: ../sv-feedback/references/worked-examples.md

## Rules that never bend

- One commit per comment ID, message starting with the ID.
- An unresolved note is never deleted, commented out or hidden.
- A report of a change is not the change: verify against the diff.

## Hand-offs

- Reviewer-facing text from the response table: `sv-feedback-rebuttal`.
- Re-check after the changes: `sv-review-loop`.
