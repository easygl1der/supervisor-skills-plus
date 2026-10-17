# Claude prompt: refine style-mine skill-local intake

Paste into Claude Code in `~/Projects/supervisor-skills-plus` on `main`
(normal `git push`, no force). Intake already exists — **do not rebuild from
scratch or route through Academic MCP.**

## Already on main (use these)

- `skills/style-mine/scripts/intake_search.py` — Crossref + OpenAlex (+ optional S2)
- `skills/style-mine/references/intake.md` — how to run journal / author / exemplars / queue
- `skills/style-mine/references/author-profile.md` — author profile stacked with venue
- `skills/style-mine/SKILL.md` — section **Intake and author profiles**

## Owner intent (2026-10-17)

1. Intake must be **usable inside the skill** (Claude Code / Cursor / Codex
   run `python skills/style-mine/scripts/intake_search.py ...`).
2. **No Academic MCP** for search or metadata. No supervising through the
   HK VPS MCP for this path.
3. Fulltext resolve, PDF cache and MinerU stay with Lit Scout / VPS.
4. Keys only in env: `INTAKE_MAILTO`, optional `SEMANTIC_SCHOLAR_API_KEY`
   (never commit).
5. S2 spacing ≥ **1.0 s** (prefer ~1.2 s); on 429 back off (Retry-After or
   8 → 15 → 30 s).
6. Human gate: queue/cards may accumulate; rules enter `research-core` /
   skill files only via `lessons-harvest` after owner confirm.
7. English only in this repo. Direct commits on `main`, no force-push.

## Please refine

1. Run `python skills/style-mine/scripts/intake_search.py --selftest` and fix
   any failures.
2. Live smoke (when network + `INTAKE_MAILTO` are set):
   `journal jasa --since 2026-01-01` should return rows; author search
   without an ID must **stop** after printing candidates (no silent pick).
3. Confirm S2 is skipped cleanly when the key is unset, and rate-limited
   when set.
4. Tighten docs if the CLI flags in `intake.md` / `SKILL.md` drift from the
   script's `--help`.
5. Optional: add a one-line pointer in the skill README if missing.
6. Short English note in `PROGRESS.md`.
7. Commit and `git push` origin main (no force).

## Non-goals

- Do not add Academic MCP / Apify dependencies for intake.
- Do not rewrite research-bridge or proposal-writer.
- Do not invent OpenAlex author IDs for 刘汉中; keep placeholders or use
  the owner's curated `publications.json` path.
- Do not auto-promote rules into research-core.

## Done when

- `--selftest` passes offline.
- Docs match the real CLI.
- Owner can run journal/author intake from the skill alone, without MCP.
