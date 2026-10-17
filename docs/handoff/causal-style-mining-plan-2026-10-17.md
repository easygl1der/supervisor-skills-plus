# Pointer: causal style mining & monitor plan (2026-10-17)

- Plan: `docs/plans/2026-10-17-causal-style-mining-and-monitor.md`
- Investigation appendix: `docs/plans/2026-10-17-causal-style-mining-investigation.md`
- Claude paste prompt: `docs/plans/2026-10-17-causal-style-mining-and-monitor-CLAUDE.md`
- Intent: top-4 stats causal style vault + 刘汉中 author profile → style-mine; promote only with owner confirm.
- Intake: **bound (owner, 2026-10-17): skill-local APIs, not MCP.** `skills/style-mine/scripts/intake_search.py` calls Crossref + OpenAlex directly (Semantic Scholar only when `SEMANTIC_SCHOLAR_API_KEY` is set; `INTAKE_MAILTO` for the polite pools). Usage: `skills/style-mine/references/intake.md`. Full text, PDF cache and MinerU stay on the VPS Academic MCP / Lit Scout. No Apify.
- Liu corpus: `easygl1der/hanzhong-liu-research` `papers/publications.json` (do not invent lists; `catalog.json` is not the CV).
- Author profile: `skills/style-mine/references/author-profile.md` (author register, author/venue conflict table, vault path via `$STYLE_VAULT`). Vault: private repo `easygl1der/causal-style-vault` (owner, 2026-10-17); first author run there: 4 cards, draft profile, pending conflicts. ADR `docs/adr/0018-style-intake-and-author-profiles.md`.
- Routines not created; scheduled runs may only append to the queue; no auto-promote to research-core.
