# De-AI contract (short form)

The full method, pattern catalog and modes are in the `sv-write-humanize-*` sub-commands (shared core: `sv-write/references/humanize/`).
This file holds the contract every skill follows when it edits prose.

1. Diagnose by intent, not by word list: ask what the sentence is trying to
   do and whether it does it with the fewest true words.
   [src: skill:deai-paper-writing] (confirmed)
2. Edit only what a finding justifies. Candidate pattern → confirmed finding
   → authorized edit. Protected content (numbers, citations, terms, quotes,
   LaTeX structure) is never changed by a style edit.
   [src: skill:avoid-ai-writing] (confirmed)
3. The output is not longer than the input unless the user asked for
   expansion. [src: skill:deai-paper-writing] (confirmed)
4. Uniformity is itself a tell. Do not replace one repeated pattern with
   another (for example, chaining the same two connectors everywhere).
   [src: skill:humanize-paper; skill:avoid-ai-writing; note:n02§11.4] (confirmed)
5. Preserve the author's plain voice; do not decorate.
   [src: skill:humanize-paper] (confirmed)
6. Punctuation bans (no semicolons, no em-dashes) are not core rules. Apply
   them only through an overlay or a venue profile.
   [src: user:2026-10-13; note:n02§11.4] (confirmed)
7. Figures can look AI-made too: detail lines under every box, gradient
   pastel frames, numbered badges. Treat them like prose tells.
   [src: note:n07§A.8 FR5; arc:msr:0f96193] (candidate)
