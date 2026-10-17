# style-mine intake scripts

Skill-local bibliography search for corpus building. **No Academic MCP.**

| Script | Role |
|---|---|
| `intake_search.py` | Journal search, author search, exemplars-from-list, queue append |

```bash
export INTAKE_MAILTO="you@example.org"   # Crossref / OpenAlex polite pool
# export SEMANTIC_SCHOLAR_API_KEY=...    # optional; calls spaced 1.2 s

python intake_search.py --selftest
python intake_search.py journal jasa --since 2026-06-01
python intake_search.py author "<author name>" --openalex-id A...
python intake_search.py exemplars /path/to/publications.json --author "..." --top4
```

Details: `../references/intake.md`. Author stacking: `../references/author-profile.md`.
Fulltext / MinerU / PDF batch: Lit Scout on the VPS, not these scripts.
