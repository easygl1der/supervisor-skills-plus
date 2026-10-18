# Speaker notes

Write notes from the final rendered pages, not from the outline. Put them
in `\note{}` on each frame and export Markdown with `scripts/export_notes.py`.

## Per page

- The main point (one sentence).
- Each symbol and what the formula does; how it connects to the slides
  before and after.
- Each figure: modules, arrows, colours, curves, axes, legend, takeaway.
- Why this page exists; what the audience is likeliest to misunderstand.
- A spoken transition to the next page.

## Voice

Conversational. Keep the presenter's own judgment. Do not restock selling
points that already sit on the slide. Audit notes with `sv-write-humanize-slides`
`academic`, not `slides`.

## Delivery (short)

Encourage questions; paraphrase a question before answering; defer
philosophical ones. Do not read the slide aloud.

## Export

`# Slide N` headings, matching frame order (including duplicates used
instead of overlays). Sidecar: `docs/meetings/<date>/notes.md`.
