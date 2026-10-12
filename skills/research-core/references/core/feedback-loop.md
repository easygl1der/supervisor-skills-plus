# Feedback-to-revision principles

The procedure is in `feedback-to-revision`. These principles bind every
skill that acts on comments.

1. **Stable IDs.** Every comment gets an ID at intake (`FB-<origin>-<nn>`)
   with a pointer to where it was made and which version the commenter read.
   [src: note:n05§6.1] (confirmed)
2. **One change per comment.** The commit message starts with the ID. Do not
   mix comment fixes with sync merges or agent checkpoints; commit subjects in
   the evidence project often hid what a patch did.
   [src: note:n05§5.5; arc:msr:5262231; arc:msr:815305e] (confirmed)
3. **Verify the diff, not the report.** "Done" means the claimed change is in
   the diff. An agent change report in the evidence project claimed eleven
   fixes; none landed. [src: note:n05§5.5; arc:06-revision/REVISION-SUMMARY.md] (confirmed)
4. **Re-check after merges.** Stale-base pushes and sync bots reverted
   verified fixes. [src: note:n05§5.3; arc:ol:214cc0c] (confirmed)
5. **Never hide an unresolved note.** Do not delete, comment out or switch off
   the display of a reviewer's note that is not resolved. An agent may resolve
   only notes the project marks as agent-resolvable; for the rest it drafts a
   fix and appends a Done note (what changed, what remains).
   [src: arc:msr:9809b8c; arc:msr:815305e; arc:msr:ac172bd; arc:msr:5776349; note:n05§5.2] (confirmed)
6. **Conflicts are surfaced.** When two reviewers ask for opposite things,
   present both and a compromise, and record the decision with its owner.
   "Decided, tell the partners" in a checklist is not a confirmation.
   [src: note:n05§5.4] (confirmed)
7. **A repeated comment reopens the earlier one.** A re-raise means the
   earlier closure was wrong. [src: note:n05§6.9] (candidate)
8. **Guidance has actions and follow-up.** Expert guidance is recorded with
   scenario, interpretation, actions with owners and due dates, and a later
   status check. [src: user:2026-10-13; arc:@threats-pivot] (confirmed)
