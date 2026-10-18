# Rewriting docs without accretion

Accretion: corrections stacked on old text ("X, but no longer since Y"),
so the doc only makes sense as a diff against a version the reader never saw.

## Passes

1. **Accuracy.** Check each claim in the living doc against its source of
   truth (code and config for tools; STATUS, ADRs and the numbers file for
   research facts). Fix false claims; delete docs that are plainly obsolete;
   move historical material to `docs/log/`, ADRs or an archive folder.
   Do not invent behavior you did not verify.
2. **One job per doc.** README for first use; STATUS for current state; ADRs
   for why; notes for scratch; logs for history. Merge duplicates into one
   home; delete filler and empty sections.
3. **Prose check.** Remove editing narration ("recently", "now", "no longer",
   "after further investigation", "initially ... but"). For each changed
   sentence ask whether a reader who never saw the old version would notice a
   gap. Keep load-bearing commands, safety constraints and unique facts.
4. **Decision hygiene.** If the doc changed because a decision was reversed,
   write a superseding ADR instead of an apology in the doc.

History is allowed in ADRs, logs, the changelog, the methods section of a
paper and archive folders; that is their job.

Sources: the owner's former skills `anti-accretive-docs` and
`research-docs-linear-lifecycle`, which build on published guidance about
replace-not-append documentation; restated here in this library's words.
[src: skill:anti-accretive-docs; skill:research-docs-linear-lifecycle] (confirmed)

The same rule governs the paper body (`research-core`
`references/core/body-text.md`).
