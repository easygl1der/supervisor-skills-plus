#!/bin/sh
# Self-test for prereg.sh under this library's conventions (docs/prereg/,
# results under analysis/ or outputs/, the template in references/).
# Runs in a throwaway repository; prints "prereg selftest ok" or exits 1.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
PREREG="$HERE/prereg.sh"
TEMPLATE="$HERE/../references/template.md"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
export HOME="$TMP/home" GIT_CONFIG_NOSYSTEM=1
export GIT_AUTHOR_NAME=t GIT_AUTHOR_EMAIL=t@example.org GIT_COMMITTER_NAME=t GIT_COMMITTER_EMAIL=t@example.org
mkdir -p "$HOME"

setup() {  # $1 = case name; a repo with raw data and a filled-in registration
    d="$TMP/$1"; mkdir -p "$d/data" "$d/docs/prereg"; cd "$d"
    git init -q; echo x > data/raw.csv; git add .; git commit -qm base
    sed -n '/^```markdown/,/^```$/p' "$TEMPLATE" | sed '1d;$d' > docs/prereg/p.md
}
expect() {  # $1 = PASS|FAIL, $2 = label
    if sh "$PREREG" audit > out.txt 2>&1; then got=PASS; else got=FAIL; fi
    [ "$got" = "$1" ] || { echo "selftest: $2: expected $1, got $got"; cat out.txt; exit 1; }
}

setup clean;   sh "$PREREG" freeze docs/prereg/p.md data/raw.csv > /dev/null
grep -q '^\*\*Frozen at commit:\*\* [0-9a-f]\{40\}$' docs/prereg/p.md || { echo "selftest: stamp missing"; exit 1; }
mkdir analysis; echo 1 > analysis/numbers.json; git add .; git commit -qm run
expect PASS "clean run"

setup edited;  sh "$PREREG" freeze docs/prereg/p.md > /dev/null
echo "- H2: added later" >> docs/prereg/p.md; git commit -qam edit
expect FAIL "edited after freeze"

setup early;   mkdir outputs; echo 1 > outputs/r; git add outputs; git commit -qm peek
sh "$PREREG" freeze docs/prereg/p.md > /dev/null
expect FAIL "outputs before freeze"

setup data;    sh "$PREREG" freeze docs/prereg/p.md data/raw.csv > /dev/null
echo y > data/raw.csv; git commit -qam data
expect FAIL "raw data changed"

cd "$TMP/clean"
if sh "$PREREG" freeze docs/prereg/p.md > /dev/null 2>&1; then echo "selftest: refreeze accepted"; exit 1; fi
echo "prereg selftest ok"
