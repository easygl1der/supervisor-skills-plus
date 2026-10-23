#!/usr/bin/env bash
# Install this skill library by symlinking each skill into agent skill folders.
#
# Usage:
#   scripts/install.sh [--targets claude,codex,cursor] [--dry-run] [--no-backup-retired]
#   scripts/install.sh --uninstall [--targets ...]
#
# - One copy of the library (this repo) serves every tool: each skills/<name>
#   is symlinked into ~/.claude/skills, ~/.codex/skills and/or ~/.cursor/skills.
# - An existing non-symlink folder with the same name is moved to
#   <target>-backup/<date>/ before linking.
# - Old local skills that this library merged and retired are also moved to the
#   backup folder (unless --no-backup-retired), so only one version is active.
# - Links into this repo whose skill no longer exists (for example the names
#   retired by ADR 0021) are removed.
# - If ~/.claude/skills etc. are links into an agent-sync tree, use
#   scripts/sync_agent_links.py instead (see INSTALL.md).
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGETS="claude,codex,cursor"
DRY=0
UNINSTALL=0
BACKUP_RETIRED=1
STAMP="$(date +%Y%m%d-%H%M%S)"

RETIRED=(se-paper-writing se-paper-refinement se-paper-reviewer deai-paper-writing
  avoid-ai-writing humanize-paper parse-pdf-comments collaborative-review-notes
  drawio-figure-replication tikz-diagram-review anti-accretive-docs
  architecture-decision-records research-docs-linear-lifecycle paper)

while [[ $# -gt 0 ]]; do
  case "$1" in
    --targets) TARGETS="$2"; shift 2 ;;
    --dry-run) DRY=1; shift ;;
    --uninstall) UNINSTALL=1; shift ;;
    --no-backup-retired) BACKUP_RETIRED=0; shift ;;
    -h|--help) sed -n '2,19p' "$0"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done

run() { if [[ $DRY -eq 1 ]]; then echo "DRY: $*"; else "$@"; fi; }

target_dir() {
  case "$1" in
    claude) echo "$HOME/.claude/skills" ;;
    codex)  echo "$HOME/.codex/skills" ;;
    cursor) echo "$HOME/.cursor/skills" ;;
    *) echo "unknown target $1" >&2; exit 2 ;;
  esac
}

IFS=',' read -r -a TLIST <<< "$TARGETS"
for t in "${TLIST[@]}"; do
  dir="$(target_dir "$t")"
  backup="${dir}-backup/${STAMP}"
  echo "== $t: $dir"
  run mkdir -p "$dir"
  for skill_path in "$REPO"/skills/*/; do
    name="$(basename "$skill_path")"
    [[ -f "$skill_path/SKILL.md" ]] || continue
    dest="$dir/$name"
    if [[ $UNINSTALL -eq 1 ]]; then
      if [[ -L "$dest" && "$(readlink "$dest")" == "${skill_path%/}" ]]; then
        run rm "$dest"; echo "  removed link $name"
      fi
      continue
    fi
    if [[ -L "$dest" ]]; then
      run rm "$dest"
    elif [[ -e "$dest" ]]; then
      run mkdir -p "$backup"; run mv "$dest" "$backup/$name"; echo "  backed up existing $name"
    fi
    run ln -s "${skill_path%/}" "$dest"; echo "  linked $name"
  done
  for dest in "$dir"/*; do
    if [[ -L "$dest" && "$(readlink "$dest")" == "$REPO/skills/"* && ! -e "$dest" ]]; then
      run rm "$dest"; echo "  removed stale link $(basename "$dest")"
    fi
  done
  if [[ $UNINSTALL -eq 0 && $BACKUP_RETIRED -eq 1 ]]; then
    for name in "${RETIRED[@]}"; do
      if [[ -e "$dir/$name" && ! -L "$dir/$name" ]]; then
        run mkdir -p "$backup"; run mv "$dir/$name" "$backup/$name"; echo "  retired $name -> $backup/"
      fi
    done
  fi
done
echo "done. Restart the agent tools so they reload skills."
