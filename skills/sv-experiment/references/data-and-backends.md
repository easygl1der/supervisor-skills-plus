# Data placement and compute backends

## Contents
1. Where each kind of file lives
2. The data manifest
3. Backends: local, Colab, VPS
4. What every backend records

## 1. Where each kind of file lives

| Kind | Place | Why |
|---|---|---|
| Code, configs, prompts, rule files, manifests | git (research repo) | diffable, small |
| Small derived tables (< 5 MB), split files, label files | git | needed to recompute numbers |
| Figure sources and final figure PDFs | git (paper repo) | built with the paper |
| Binaries > 5 MB that must travel with a repo | Git LFS (patterns in `research.yaml` `data.lfs_patterns`) | keeps clones fast |
| Raw corpora, databases, model outputs, crawled bodies | external host (data host, Hugging Face datasets, Zenodo, Figshare, object storage, a drive) listed in `data/MANIFEST.tsv` | code hosts reject or truncate large files |
| Secrets, tokens, local databases with credentials | nowhere in any repo; environment or a secret store | leaks with the artifact |
| Frozen data copies in the manuscript repo | never | copies drift from the frozen version |

The evidence project's research repository kept its multi-gigabyte data and
database out of git and listed them in a file manifest; the replication
bodies were too large for a code host and a senior co-author asked for a
data host instead. No Git LFS use is evidenced in its project repositories.
[src: arc:11-mining-github-issue-audit/README.md; arc:chat:group@2026-10-03T20:24; note:n08§5#39; note:n08§2] (candidate)

Make the private-material ignore rules on day one: chat exports, other
people's papers and personal notes never enter the shared repositories
(`sv-supervisor-records` Task 1). [src: note:n08§5#8] (confirmed)

## 2. The data manifest

`data/MANIFEST.tsv` (template: `research-core` `assets/templates/data-manifest.tsv`):

```
path	bytes	sha256	source	licence	how_to_fetch	notes
```

- `path` is relative to the repository root, also for files that live only
  on the external host.
- `source` says where the data came from (crawl id, dataset DOI, API);
  `licence` the terms it may be shared under; `how_to_fetch` a command or a
  download script name. A row with an empty `how_to_fetch` must be present
  locally.

Build and verify:

```bash
python scripts/manifest.py build data/            # hash files, keep filled columns, flag files > 5 MB
python scripts/manifest.py verify --data-dir data/ # sizes and hashes; unlisted files; external rows
```

Run `verify` before every run that produces printed numbers, and record the
manifest's own hash as the data version in the runs log. A partner bundle
with a sha256 manifest worked well for handing data to a co-author in the
evidence project. [src: arc:res:44b01cb] (candidate)

## 3. Backends: local, Colab, VPS

Set `research.yaml` `experiments.backend`. Each backend has the same job:
run the committed code on the manifest-listed data and write a runs-log row.

### local
- Run from a clean tree; record the lock file hash (`uv.lock`,
  `requirements.txt`, `environment.yml`).
- Long jobs: run under a process manager or `tmux`; write logs to
  `outputs/<run id>/log.txt`.

### Colab
**No project evidence.** The evidence project never used Colab; this adapter
is designed from the tools available on the owner's machine, not from a
lesson. [src: note:n08§2] (candidate)

1. Check for the owner's `colab-mcp-workflow` skill
   (`~/.claude/skills/colab-mcp-workflow` or the Codex or Cursor skill
   folders) and use it to connect to the notebook named in
   `research.yaml` `experiments.notebook`. If a Colab command-line tool is
   installed (check with `command -v`), it may be used instead. If neither
   is available, ask the user to run the cells and paste the output.
2. The notebook does not hold the code. Its first cell clones the research
   repo at a named commit and installs the locked environment; the next cell
   fetches data with the manifest's `how_to_fetch` commands and runs
   `manifest.py verify`.
3. Run the committed script from a cell (`!python scripts/rq1.py ...`), not
   code typed into cells. Code first written in a cell is moved to the repo
   and committed before its numbers count.
4. Copy outputs back (Drive or download), commit `numbers.json` and small
   outputs, list large ones in the manifest.
5. Record the notebook URL, the runtime type (CPU, GPU model) and the cell
   range in the runs log.
6. Stop before irreversible UI actions (sharing, deleting, paid runtime
   changes) and ask the user, as the Colab skill itself requires.

### VPS (ssh)
- Reach the host through an ssh alias; the runs log records the alias, not
  an address.
- Pull the research repo at a named commit; fetch data by the manifest.
- Long jobs run as managed services (systemd units or `tmux`) so the laptop
  can sleep; scripts never print API keys.
  [src: arc:11-mining-github-issue-audit/tree/scripts/vps-hk-llm-annotate.sh] (candidate)
- Re-import or export state after every session; the server's copy is not
  the source of truth (see the state-file rule in `runs-and-numbers.md`).
- Copy outputs back and commit `numbers.json` from the research repo, not
  from the server.

## 4. What every backend records

In `docs/runs.md`: command or notebook plus cells, code commit, data version
(manifest hash), backend and environment, status, outputs. A run that cannot
name its code commit and data version produces no printed number.
