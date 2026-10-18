# Linear as an optional mirror

Decision: local files are the source of truth; Linear is an optional board.
[src: user:2026-10-13]

## Why not Linear first

| | Local first | Linear first |
|---|---|---|
| Agent access | plain files, always | needs the MCP and network |
| History | git, diffable | outside the repo |
| Survives archiving | yes | ticket ids remain in code, bodies are lost |
| Co-author visibility | needs repo access | good board and notifications |

In the evidence project, ticket ids appear in code and notes but their text
is not in the archive. [src: note:n08§4] (confirmed)

## Rules when `records.linear.enabled` is true

- One issue per TODO item or blocker that needs a board; not per note.
- Issue description holds three links: the living doc it owns, the ADR (or
  "none yet"), the active note (or "none"). [src: skill:research-docs-linear-lifecycle] (confirmed)
- Comments: one-line results and blockers. Never paste reports.
- Status flows from files to Linear. When an item closes in `docs/`, close
  the issue with a link to the evidence.
- Copy any decision made in a Linear thread into an ADR the same day.
- Use the Linear MCP tools when available; otherwise list the updates for
  the user to apply.
