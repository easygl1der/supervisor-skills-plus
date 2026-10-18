#!/usr/bin/env python3
"""Index local icon libraries, search them, and record attribution.

Generalized from the owner's former local skill `scientific-illustration-ppt`
(index_assets.py, search_assets.py): any number of libraries, any field, no
hard-coded paths.

Libraries come from (merged in this order):
  1. --lib PATH or --lib NAME=PATH (repeatable)
  2. env ICON_LIBS: paths separated by os.pathsep (':' on macOS/Linux)
  3. research.yaml `figures.icon_libs` (--config, default ./research.yaml):
       figures:
         icon_libs:
           - ~/.cache/supervisor-skills/icons/tabler-icons          # plain path
           - {name: bioicons, path: ~/.cache/.../bioicons,
              license: per-icon, source: https://github.com/duerrsimon/bioicons,
              retrieved: 2026-10-13}

Commands:
  build      walk the libraries and write a JSON index
  search     keyword search with synonyms; prints path, licence, attribution
  attribute  append one row per used icon to <figure>_icons/ATTRIBUTION.tsv

Licences are read, never assumed: an explicit `license` in research.yaml
wins, then repository metadata (BioIcons licence folders, Health Icons
README terms), then the first lines of the library's LICENSE file. If none
is found the record says `unknown` and must not be used until checked.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

ASSET_EXT = {".svg", ".png", ".xml", ".drawio"}
SKIP_DIRS = {".git", "node_modules", ".github", "__pycache__", "dist", "build", "docs", "tests", "test"}
ATTR_HEADER = ["source", "path", "license", "author", "retrieved", "asset_id", "library", "note"]

SYNONYMS = {
    # general concepts
    "database": ["db", "storage", "data", "cylinder", "server"],
    "document": ["file", "doc", "paper", "page", "report"],
    "user": ["person", "people", "human", "annotator", "users"],
    "search": ["magnifier", "find", "query", "zoom"],
    "filter": ["funnel", "gate", "sieve"],
    "check": ["tick", "verify", "validation", "approved", "success"],
    "error": ["bug", "alert", "warning", "fail", "failure"],
    "settings": ["gear", "cog", "config", "configuration", "calibration"],
    "chart": ["graph", "plot", "bar", "analytics", "statistics"],
    "list": ["table", "rows", "items", "sample"],
    "cloud": ["server", "hosting"],
    # software engineering
    "code": ["source", "program", "brackets", "terminal", "script"],
    "bug": ["issue", "defect", "error", "insect"],
    "issue": ["bug", "ticket", "report"],
    "git": ["commit", "branch", "merge", "version", "repository"],
    "repository": ["repo", "git", "github", "gitlab"],
    "test": ["testing", "check", "flask", "beaker"],
    "ci": ["pipeline", "build", "workflow", "actions"],
    # AI / ML
    "robot": ["bot", "ai", "llm", "agent", "model"],
    "llm": ["robot", "ai", "chat", "language", "model", "transformer"],
    "neural": ["network", "nn", "neuron", "layer", "brain"],
    "brain": ["neural", "ai", "intelligence", "mind"],
    "attention": ["transformer", "self-attention", "head"],
    "convolution": ["conv", "cnn", "kernel"],
    "embedding": ["vector", "latent", "encoder"],
    # math / stats / causal
    "graph": ["network", "node", "edge", "dag"],
    "dag": ["graph", "causal", "bayesian", "network"],
    "distribution": ["histogram", "density", "probability", "gaussian", "normal"],
    "regression": ["line", "fit", "trend", "scatter"],
    "matrix": ["grid", "table", "heatmap"],
    # bio
    "cell": ["cells", "cell-types", "cell-culture"],
    "virus": ["viral", "viruses", "microbiology"],
    "dna": ["gene", "genetics", "nucleic", "helix"],
}
STOP = {"a", "an", "and", "or", "of", "the", "for", "in", "on", "to", "with", "icon", "icons"}

LICENSE_PATTERNS = [
    (r"\bCC0\b|Creative Commons Zero|CC0 1\.0", "CC0-1.0"),
    (r"Creative Commons Attribution[- ]ShareAlike 4\.0|CC BY-SA 4\.0", "CC-BY-SA-4.0"),
    (r"Creative Commons Attribution 4\.0|CC BY 4\.0", "CC-BY-4.0"),
    (r"Apache License,?\s+Version 2\.0", "Apache-2.0"),
    (r"\bISC License\b", "ISC"),
    (r"\bMIT License\b|The MIT License", "MIT"),
    (r"BSD 3-Clause|Redistributions of source code must retain", "BSD"),
    (r"SIL OPEN FONT LICENSE", "OFL-1.1"),
]


def today() -> str:
    return dt.date.today().isoformat()


def default_index() -> Path:
    base = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache"))
    return base / "supervisor-skills" / "icons" / "index.json"


def expand(p: str, base: Path | None = None) -> Path:
    path = Path(os.path.expandvars(os.path.expanduser(str(p))))
    if not path.is_absolute() and base is not None:
        path = base / path
    return path.resolve()


# ---------------------------------------------------------------- libraries

def load_config_libs(config: Path) -> list[dict]:
    if not config.exists():
        return []
    try:
        import yaml  # type: ignore
    except ImportError:
        print(f"warning: PyYAML not installed; {config} ignored (use --lib or ICON_LIBS)", file=sys.stderr)
        return []
    data = yaml.safe_load(config.read_text(encoding="utf-8")) or {}
    libs = ((data.get("figures") or {}).get("icon_libs")) or []
    out = []
    for entry in libs:
        if isinstance(entry, str):
            out.append({"path": str(expand(entry, config.parent))})
        elif isinstance(entry, dict) and entry.get("path"):
            e = dict(entry)
            e["path"] = str(expand(e["path"], config.parent))
            out.append(e)
    return out


def collect_libs(args) -> list[dict]:
    libs: list[dict] = []
    for spec in args.lib or []:
        name, sep, path = spec.partition("=")
        if not sep:
            name, path = "", spec
        libs.append({"name": name, "path": str(expand(path))})
    for part in filter(None, os.environ.get("ICON_LIBS", "").split(os.pathsep)):
        libs.append({"path": str(expand(part))})
    libs.extend(load_config_libs(Path(args.config)))
    seen, uniq = set(), []
    for lib in libs:
        if lib["path"] in seen:
            continue
        seen.add(lib["path"])
        lib.setdefault("name", Path(lib["path"]).name)
        if not lib["name"]:
            lib["name"] = Path(lib["path"]).name
        uniq.append(lib)
    return uniq


def detect_license(root: Path) -> str:
    for name in ("LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "COPYING"):
        f = root / name
        if f.exists():
            head = f.read_text(encoding="utf-8", errors="replace")[:4000]
            for pat, spdx in LICENSE_PATTERNS:
                if re.search(pat, head, re.I):
                    return spdx
            return "see " + name
    return "unknown"


def git_remote(root: Path) -> str:
    cfg = root / ".git" / "config"
    if cfg.exists():
        m = re.search(r"url\s*=\s*(\S+)", cfg.read_text(encoding="utf-8", errors="replace"))
        if m:
            return m.group(1)
    return ""


# ---------------------------------------------------------------- records

def tokens(text: str) -> list[str]:
    return [t for t in re.split(r"[^a-z0-9]+", text.lower()) if t]


def make_record(lib: dict, path: Path, root: Path, *, name: str = "", tags=None,
                license_: str = "", author: str = "", entry: str = "") -> dict:
    rel = path.relative_to(root).as_posix()
    nm = name or path.stem.replace("_", " ").replace("-", " ")
    lic = license_ or lib.get("license") or lib["_license"]
    auth = author or lib.get("author", "")
    src = lib.get("source") or lib["_remote"] or lib["path"]
    rid = f"{lib['name']}:{rel}" + (f"#{entry}" if entry else "")
    tag_list = sorted({t for t in (tags or []) + tokens(rel) if len(t) > 1})
    attribution = f"{nm}, {lib['name']}" + (f" by {auth}" if auth else "") + f", {lic}"
    return {
        "id": rid, "library": lib["name"], "name": nm, "tags": tag_list,
        "path": str(path) + (f"#{entry}" if entry else ""), "rel_path": rel,
        "format": path.suffix.lower().lstrip("."), "license": lic, "author": auth,
        "source": src, "retrieved": str(lib.get("retrieved", "")), "attribution": attribution,
        "note": lib.get("note", ""),
    }


def bioicons_records(lib: dict, root: Path):
    icons_root = root / "static" / "icons"
    meta = {}
    mj = icons_root / "icons.json"
    if mj.exists():
        for item in json.loads(mj.read_text(encoding="utf-8")):
            meta[(item.get("name", "").lower(), item.get("category", "").lower())] = item
    for svg in sorted(icons_root.rglob("*.svg")):
        parts = svg.relative_to(icons_root).parts
        if len(parts) < 4:
            continue
        lic, cat, author = parts[0], parts[1], parts[2]
        item = meta.get((svg.stem.lower(), cat.lower()), {})
        yield make_record(lib, svg, root, name=item.get("name", svg.stem),
                          tags=[cat.lower(), "bio"], license_=item.get("license") or lic,
                          author=item.get("author") or author.replace("_", " "))


def healthicons_records(lib: dict, root: Path):
    icons_root = root / "public" / "icons"
    meta = {}
    mj = icons_root / "meta-data.json"
    if mj.exists():
        for item in json.loads(mj.read_text(encoding="utf-8")):
            meta[item.get("id", "")] = item
    for svg in sorted((icons_root / "svg").rglob("*.svg")):
        item = meta.get(svg.stem, {})
        yield make_record(lib, svg, root, name=item.get("title", svg.stem),
                          tags=[t.lower() for t in item.get("tags", [])] + ["health"],
                          license_=lib.get("license") or "CC0-1.0 (icons, per README)",
                          author=lib.get("author") or "Health Icons contributors")


def mxlibrary_records(lib: dict, root: Path, xml: Path):
    text = xml.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"<mxlibrary>(.*)</mxlibrary>", text, re.S)
    if not m:
        return
    try:
        entries = json.loads(m.group(1))
    except json.JSONDecodeError:
        return
    for i, e in enumerate(entries):
        title = e.get("title") or f"entry {i}"
        yield make_record(lib, xml, root, name=title, tags=tokens(title) + ["drawio-library"],
                          entry=str(i))


def generic_records(lib: dict, root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in sorted(filenames):
            p = Path(dirpath) / fn
            ext = p.suffix.lower()
            if ext not in ASSET_EXT:
                continue
            if ext == ".xml":
                head = p.read_text(encoding="utf-8", errors="replace")[:200]
                if "<mxlibrary" in head:
                    yield from mxlibrary_records(lib, root, p)
                continue
            yield make_record(lib, p, root)


def index_library(lib: dict) -> list[dict]:
    root = Path(lib["path"])
    if not root.is_dir():
        print(f"warning: library not found: {root}", file=sys.stderr)
        return []
    lib["_license"] = detect_license(root)
    lib["_remote"] = git_remote(root)
    if (root / "static" / "icons" / "icons.json").exists():
        lib["_license"] = "per-icon (licence folder and icons.json)"
        recs = list(bioicons_records(lib, root))
    elif (root / "public" / "icons" / "meta-data.json").exists():
        lib["_license"] = "CC0-1.0 (icons, per README); code MIT"
        recs = list(healthicons_records(lib, root))
    else:
        recs = list(generic_records(lib, root))
    return recs


# ---------------------------------------------------------------- search

def variants(t: str) -> set[str]:
    v = {t}
    if t.endswith("ies") and len(t) > 4:
        v.add(t[:-3] + "y")
    if t.endswith("es") and len(t) > 4:
        v.add(t[:-2])
    if t.endswith("s") and len(t) > 3:
        v.add(t[:-1])
    return v


def expand_query(q: str) -> list[set[str]]:
    groups = []
    for t in tokens(q):
        if t in STOP:
            continue
        g = set(variants(t))
        for key, syns in SYNONYMS.items():
            syn_t = {x for syn in syns for x in tokens(syn)}
            if key in g or g & syn_t:
                g.add(key)
                g.update(syn_t)
        groups.append(g)
    return groups


def score(rec: dict, groups: list[set[str]], raw: list[str]) -> float:
    name_t = set(tokens(rec["name"]))
    tag_t = set(rec["tags"])
    s, hit_groups = 0.0, 0
    for g, word in zip(groups, raw):
        best = 0.0
        if variants(word) & name_t:
            best = 10
        elif g & name_t:
            best = 6
        elif variants(word) & tag_t:
            best = 4
        elif g & tag_t:
            best = 2
        if best:
            hit_groups += 1
        s += best
    if not hit_groups:
        return 0.0
    s *= hit_groups / len(groups)
    if rec["format"] == "svg":
        s += 0.5
    if rec["license"] in ("unknown",) or rec["license"].startswith("see "):
        s -= 1
    return s


def cmd_build(args) -> int:
    libs = collect_libs(args)
    if not libs:
        print("no libraries: pass --lib, set ICON_LIBS, or add figures.icon_libs to research.yaml", file=sys.stderr)
        return 1
    records = []
    summary = []
    for lib in libs:
        recs = index_library(lib)
        records.extend(recs)
        summary.append({"library": lib["name"], "path": lib["path"], "assets": len(recs),
                        "license": lib.get("license") or lib.get("_license", "unknown")})
    out = Path(args.out) if args.out else default_index()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"built": today(), "libraries": summary, "assets": records},
                              ensure_ascii=False, indent=1), encoding="utf-8")
    for row in summary:
        print(f"{row['library']}: {row['assets']} assets, licence {row['license']}")
    print(f"index: {out}")
    return 0


def load_index(path: str | None) -> dict:
    p = Path(path) if path else default_index()
    if not p.exists():
        raise SystemExit(f"index not found: {p} (run build first)")
    return json.loads(p.read_text(encoding="utf-8"))


def cmd_search(args) -> int:
    idx = load_index(args.index)
    raw = [t for t in tokens(args.query) if t not in STOP]
    groups = expand_query(args.query)
    allow = {a.strip().lower() for a in args.license.split(",")} if args.license else None
    hits = []
    for rec in idx["assets"]:
        if args.library and rec["library"] != args.library:
            continue
        if args.format and rec["format"] != args.format:
            continue
        if allow and not any(a in rec["license"].lower() for a in allow):
            continue
        sc = score(rec, groups, raw)
        if sc > 0:
            hits.append((sc, rec))
    hits.sort(key=lambda x: (-x[0], x[1]["id"]))
    hits = hits[: args.limit]
    if args.json:
        print(json.dumps([dict(r, score=round(s, 2)) for s, r in hits], ensure_ascii=False, indent=1))
    else:
        for s, r in hits:
            print(f"{s:5.1f}  {r['id']}\n       path: {r['path']}\n       licence: {r['license']}"
                  f"\n       attribution: {r['attribution']}")
    if not hits:
        print("no match", file=sys.stderr)
    return 0


def cmd_attribute(args) -> int:
    idx = load_index(args.index)
    by_id = {r["id"]: r for r in idx["assets"]}
    folder = Path(args.figure_dir)
    folder.mkdir(parents=True, exist_ok=True)
    tsv = folder / "ATTRIBUTION.tsv"
    new = not tsv.exists()
    existing = tsv.read_text(encoding="utf-8") if tsv.exists() else ""
    with tsv.open("a", encoding="utf-8") as f:
        if new:
            f.write("\t".join(ATTR_HEADER) + "\n")
        for aid in args.id:
            rec = by_id.get(aid)
            if rec is None:
                print(f"unknown id: {aid}", file=sys.stderr)
                continue
            if rec["license"] == "unknown":
                print(f"refusing {aid}: licence unknown; read the source licence first", file=sys.stderr)
                continue
            if f"\t{aid}\t" in existing:
                continue
            row = [rec["source"], rec["rel_path"], rec["license"], rec["author"],
                   rec["retrieved"] or args.retrieved or today(), aid, rec["library"], args.note or rec["note"]]
            f.write("\t".join(str(x).replace("\t", " ") for x in row) + "\n")
            print(f"recorded {aid}")
    print(f"attribution: {tsv}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("build", help="index the configured libraries")
    b.add_argument("--lib", action="append", help="PATH or NAME=PATH (repeatable)")
    b.add_argument("--config", default="research.yaml")
    b.add_argument("--out", help=f"index file (default {default_index()})")
    b.set_defaults(func=cmd_build)

    s = sub.add_parser("search", help="keyword search")
    s.add_argument("query")
    s.add_argument("--index")
    s.add_argument("--limit", type=int, default=12)
    s.add_argument("--library")
    s.add_argument("--format", choices=["svg", "png", "xml", "drawio"])
    s.add_argument("--license", help="comma list of allowed licence substrings, e.g. cc0,mit,apache")
    s.add_argument("--json", action="store_true")
    s.set_defaults(func=cmd_search)

    a = sub.add_parser("attribute", help="append rows to <figure>_icons/ATTRIBUTION.tsv")
    a.add_argument("--index")
    a.add_argument("--figure-dir", required=True, help="the <figure>_icons folder")
    a.add_argument("--id", action="append", required=True, help="asset id from search (repeatable)")
    a.add_argument("--retrieved", help="retrieval date if the library entry has none (YYYY-MM-DD)")
    a.add_argument("--note", default="", help="e.g. 'recoloured fill'")
    a.set_defaults(func=cmd_attribute)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
