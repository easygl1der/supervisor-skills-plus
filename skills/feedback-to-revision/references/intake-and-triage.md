# Intake and triage

## Contents
1. Channels and what each needs
2. ID scheme
3. Triage fields
4. Conflicts, duplicates, re-raises, stale versions
5. Intake table layout

## 1. Channels and what each needs

| Channel | How to ingest | Known problems (evidence) |
|---|---|---|
| Written comment file | One ID per actionable point; keep the file's line numbers | Broad themes make "done" a judgement; record the delivery date, often missing [src: note:n05§5.1] |
| Inline LaTeX notes | `scripts/list_markers.py`; ID per marker; record the commit that added it | A drop made on a stale base silently reverted others' work [src: arc:msr:9809b8c; note:n05§5.3] |
| Annotated PDF | `scripts/extract_pdf_comments.py`; key to caption or nearby text | Float numbers drift during a batch; flattened drawings are not extractable [src: note:n05§5.1] |
| Group or one-to-one chat | Copy the message text with timestamp; restate image-only requests in words | Requests mixed with process chat; "this one too?" on an image is unrecoverable later [src: note:n05§5.1] |
| `%TODO` comments by a co-author | Ask who they are for | The student had to ask whether they were meant for them [src: note:n05§5.1] |
| Relayed advice | Record the relay and the version the expert read | The advisor read an older version; one of seven points was already obsolete [src: note:n05§5.1] |
| Review report | One ID per weakness or question; keep reviewer numbering (R1.W2) | No evidence yet from this library's projects |
| Agent review or agent change report | Origin `AG`; never treat as a human request | A report claimed eleven fixes that were not in the diff [src: arc:06-revision/REVISION-SUMMARY.md; note:n05§5.5] |

## 2. ID scheme

`FB-<origin>[-<channel>]-<nn>`

- origin: `A`, `B`, `C` (co-authors by role), `ADV`, `R1`..`Rn`, `AG`, `SELF`
- channel (optional): `INL` inline, `P` PDF, `CH` chat, none for files
- numbering is per origin and channel, never reused, never renumbered

Process requests (sync, metadata, account access) get `PR-<nn>` and go to
`TODO.md`, not the response table.

## 3. Triage fields

| Field | Values |
|---|---|
| Type | structure, framing, terminology, claim-evidence, figure, table, formatting-venue, citation, anonymity, scope, page-budget, experiment |
| Size | S (sentence), M (paragraph or float), L (section or new analysis) |
| Needs author decision | yes when it changes a claim, scope, method, or contradicts another comment or an ADR |
| Duplicate of | earlier ID covering the same point |
| Conflicts with | ID asking for the opposite |
| Re-raise of | earlier ID the commenter repeats (reopen it) |
| Stale version | yes when the commenter read an older version than the current one |
| Image only | yes when the request refers to an image; restate in words |
| Page effect | estimated lines gained or lost |

## 4. Conflicts, duplicates, re-raises, stale versions

- **Conflicts.** Do not resolve silently. Present both positions with their
  sources and propose one option, often a compromise (in the evidence project
  an appendix dispute ended with a short table in the body and full
  definitions in the replication package). Record the decision, its owner and
  date; confirm with the person whose request lost. [src: note:n05§5.4] (confirmed)
- **Duplicates.** Link to the first ID; close together.
- **Re-raises.** Reopen the earlier ID and add the new pointer; a repeat means
  the earlier closure did not satisfy the commenter. [src: note:n05§6.9] (candidate)
- **Stale version.** Check whether the point still applies to the current
  text; if not, mark `superseded` with the reason and tell the commenter.
- **Cut versus fill.** Early comments that cut text and late comments that
  ask to fill pages must be reconciled against the page budget; track the
  page effect of each accepted change. [src: note:n05§6.8] (candidate)

## 5. Intake table layout

```
| ID | Origin | Channel | Date | Read version | Quote (short) | Pointer | Type | Size | Decide? | Links |
```

The response table (template in `research-core`) reuses the ID column and
adds decision, change, location, commit and verification.
