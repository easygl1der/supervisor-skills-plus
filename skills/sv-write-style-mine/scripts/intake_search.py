#!/usr/bin/env python3
"""Exemplar intake for sv-write-style-mine: find papers by journal or author via public APIs (no MCP).

Usage:
    python intake_search.py journal <slug|ISSN> [--since 2026-01-01] [--max 200] [--all] [--queue FILE]
    python intake_search.py author "<name>" [--openalex-id A...] [--s2-id N] [--since DATE] [--queue FILE]
    python intake_search.py exemplars <publications.json> --author "<name>" [--top4]
    python intake_search.py --selftest

Sources: Crossref (discovery by ISSN, works by ORCID) and OpenAlex (abstract,
OA status, author disambiguation) by default; Semantic Scholar is added only
when SEMANTIC_SCHOLAR_API_KEY is set (calls spaced 1.2 s apart). Set
INTAKE_MAILTO (an email) for the Crossref and OpenAlex polite pools. Keys come
from the environment only. On HTTP 429 or 5xx the script waits Retry-After, or
8, 15, 30 s, then gives up.

journal: lists articles since --since, marks each with the causal keywords it
hits (title or abstract) and prints hits only unless --all.
author: without an ID prints candidate authors and stops (a human picks one);
with --openalex-id or --s2-id prints that author's works.
exemplars: filters a local publication list (fields title, year, venue,
status, authors, doi, arxiv) into a Markdown table with the author's role.
--queue appends records whose key is new to a JSONL file (append-only; a
human later sets filter to human_keep or human_skip). No full text, PDF or
MinerU step happens here.
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# Top-4 statistics journals: Crossref filters take either ISSN (OR); pinning the
# ISSNs keeps out the old JRSS-B (Methodological) series and Annals of Applied Statistics.
VENUES = {
    "jasa": ("Journal of the American Statistical Association", ["1537-274X", "0162-1459"]),
    "jrssb": ("Journal of the Royal Statistical Society Series B: Statistical Methodology", ["1467-9868", "1369-7412"]),
    "aos": ("The Annals of Statistics", ["2168-8966", "0090-5364"]),
    "biometrika": ("Biometrika", ["1464-3510", "0006-3444"]),
}
TOP4_NAMES = {"JASA", "JRSS-B", "Annals of Statistics", "AoS", "Biometrika"}
# Unambiguous causal phrases only: "identif", "matching" and "randomiz" alone flagged mostly
# non-causal JASA papers in a 2026 test; use --all and the human screen for broader recall.
CAUSAL = ["causal", "treatment effect", "potential outcome", "instrumental variable",
          "regression discontinuity", "difference-in-difference", "difference in difference",
          "synthetic control", "propensity score", "rerandomization", "randomized experiment",
          "covariate adjustment", "interference", "counterfactual", "confound", "unmeasured"]
MAILTO = os.environ.get("INTAKE_MAILTO", "")
S2_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")


BACKOFF = (8, 15, 30)  # seconds after a 429 or 5xx when the server sends no Retry-After
S2_GAP = 1.2  # Semantic Scholar: at least 1 s between calls; 1.2 s leaves margin
_s2_last = 0.0


def wait_for(attempt: int, retry_after: str | None) -> float:
    return float(retry_after) if retry_after and retry_after.isdigit() else BACKOFF[attempt]


def get(url: str, headers: dict | None = None, body: bytes | None = None) -> dict:
    h = {"User-Agent": f"style-mine-intake/1.0 (mailto:{MAILTO or 'unset'})", **(headers or {})}
    for attempt in range(len(BACKOFF) + 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, body, h), timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < len(BACKOFF):
                s = wait_for(attempt, e.headers.get("Retry-After"))
                print(f"intake: HTTP {e.code}, retrying in {s:.0f} s", file=sys.stderr)
                time.sleep(s)
                continue
            raise SystemExit(f"intake: HTTP {e.code} from {url.split('?')[0]}")
    raise SystemExit("intake: unreachable")


def s2get(path: str, params: dict) -> dict:
    """Semantic Scholar call, spaced S2_GAP apart; only reached when SEMANTIC_SCHOLAR_API_KEY is set."""
    global _s2_last
    time.sleep(max(0.0, _s2_last + S2_GAP - time.monotonic()))
    try:
        return get(f"https://api.semanticscholar.org/graph/v1/{path}?" + q(params), {"x-api-key": S2_KEY})
    finally:
        _s2_last = time.monotonic()


def q(params: dict) -> str:
    return urllib.parse.urlencode({k: v for k, v in params.items() if v not in (None, "")})


def abstract_text(inv: dict | None) -> str:
    """OpenAlex stores abstracts as an inverted index {word: [positions]}."""
    if not inv:
        return ""
    pos = {i: w for w, idx in inv.items() for i in idx}
    return " ".join(pos[i] for i in sorted(pos))


def hits(text: str) -> list[str]:
    t = text.lower()
    return [k for k in CAUSAL if k in t]


def oa_fields(w: dict) -> tuple[str, str]:
    oa = w.get("open_access") or {}
    status, url = oa.get("oa_status") or "unknown", oa.get("oa_url") or ""
    # publisher "hybrid"/"bronze" links often need access; keep only green or repository copies
    if status not in ("green", "gold", "diamond") and "arxiv.org" not in url:
        url = ""
    return status, url


def record(doi, title, venue, issued, authors, source, abstract="", oa=("unknown", "")) -> dict:
    return {"key": (doi or "").lower() or title.lower()[:80], "doi": (doi or "").lower(), "title": title,
            "venue_slug": venue, "issued": issued, "authors": authors[:8], "source": [source],
            "keyword_hits": hits(title + " " + abstract), "oa_status": oa[0], "oa_url": oa[1],
            "filter": "", "status": "new"}


def merge(recs: list[dict]) -> list[dict]:
    out: dict[str, dict] = {}
    for r in recs:
        if r["key"] in out:
            o = out[r["key"]]
            o["source"] = sorted(set(o["source"] + r["source"]))
            o["keyword_hits"] = sorted(set(o["keyword_hits"] + r["keyword_hits"]))
            for f in ("oa_status", "oa_url", "issued"):
                if o[f] in ("", "unknown") and r[f]:
                    o[f] = r[f]
        else:
            out[r["key"]] = dict(r)
    return list(out.values())


def openalex_by_doi(dois: list[str]) -> dict[str, dict]:
    found = {}
    for i in range(0, len(dois), 50):
        chunk = "|".join(dois[i:i + 50])
        d = get("https://api.openalex.org/works?" + q({"filter": f"doi:{chunk}", "per-page": 50, "mailto": MAILTO}))
        for w in d.get("results", []):
            found[(w.get("doi") or "").replace("https://doi.org/", "").lower()] = w
    return found


def crossref_items(filt: str, n: int) -> list[dict]:
    d = get("https://api.crossref.org/works?" + q({"filter": filt, "rows": min(n, 1000), "sort": "published",
                                                    "order": "desc", "mailto": MAILTO,
                                                    "select": "DOI,title,author,issued,abstract,container-title"}))
    return d["message"]["items"]


def from_crossref(it: dict, venue: str) -> dict:
    parts = (it.get("issued") or {}).get("date-parts") or [[None]]
    issued = "-".join(f"{p:02d}" if i else str(p) for i, p in enumerate(parts[0]) if p)
    names = [f"{a.get('given', '')} {a.get('family', '')}".strip() for a in it.get("author", [])]
    return record(it.get("DOI"), (it.get("title") or [""])[0], venue, issued, names, "crossref", it.get("abstract", ""))


def journal(arg: str, since: str, n: int, show_all: bool) -> list[dict]:
    slug = arg.lower()
    name, issns = VENUES.get(slug, (arg, [arg]))
    filt = ",".join([f"issn:{s}" for s in issns] + [f"from-pub-date:{since}", "type:journal-article"])
    recs = [from_crossref(it, slug) for it in crossref_items(filt, n)]
    oa = openalex_by_doi([r["doi"] for r in recs if r["doi"]])
    for r in recs:  # OpenAlex enrichment: abstract for keyword hits, OA status
        w = oa.get(r["doi"])
        if w:
            r["source"].append("openalex")
            r["keyword_hits"] = sorted(set(r["keyword_hits"] + hits(abstract_text(w.get("abstract_inverted_index")))))
            r["oa_status"], r["oa_url"] = oa_fields(w)
    if S2_KEY:
        d = s2get("paper/search/bulk", {"query": "causal | treatment effect | identification", "venue": name,
                                        "year": f"{since[:4]}-", "fields": "title,externalIds,publicationDate,authors"})
        recs += [record((p.get("externalIds") or {}).get("DOI"), p.get("title") or "", slug, p.get("publicationDate") or "",
                        [a["name"] for a in p.get("authors", [])], "semanticscholar") for p in d.get("data", [])]
    recs = merge(recs)
    for r in recs:
        r["filter"] = "keyword_hit" if r["keyword_hits"] else "no_hit"
    return recs if show_all else [r for r in recs if r["keyword_hits"]]


def author(name: str, oa_id: str, s2_id: str, since: str) -> list[dict]:
    if not oa_id and not s2_id:  # disambiguation is a human decision
        d = get("https://api.openalex.org/authors?" + q({"search": name, "per-page": 10, "mailto": MAILTO}))
        for a in d.get("results", []):
            inst = ", ".join(i.get("display_name", "") for i in (a.get("last_known_institutions") or [])[:2])
            print(f"openalex {a['id'].rsplit('/', 1)[-1]}\t{a['display_name']}\tworks={a.get('works_count')}\t{inst}\torcid={a.get('orcid') or '-'}")
        if S2_KEY:
            d = s2get("author/search", {"query": name, "fields": "name,paperCount,affiliations"})
            for a in d.get("data", [])[:10]:
                print(f"s2 {a['authorId']}\t{a['name']}\tpapers={a.get('paperCount')}\t{', '.join(a.get('affiliations') or [])}")
        print("intake: pick one ID and rerun with --openalex-id or --s2-id", file=sys.stderr)
        return []
    recs = []
    if oa_id:
        a = get(f"https://api.openalex.org/authors/{oa_id}?" + q({"mailto": MAILTO}))
        d = get("https://api.openalex.org/works?" + q({"filter": f"author.id:{oa_id},from_publication_date:{since}",
                                                        "per-page": 200, "mailto": MAILTO}))
        for w in d.get("results", []):
            src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or ""
            recs.append(record((w.get("doi") or "").replace("https://doi.org/", ""), w.get("title") or "", src,
                               w.get("publication_date") or "", [x["author"]["display_name"] for x in w.get("authorships", [])],
                               "openalex", abstract_text(w.get("abstract_inverted_index")), oa_fields(w)))
        orcid = (a.get("orcid") or "").rsplit("/", 1)[-1]
        if orcid:  # Crossref only knows works whose deposits carry the ORCID
            recs += [from_crossref(it, (it.get("container-title") or [""])[0])
                     for it in crossref_items(f"orcid:{orcid},from-pub-date:{since}", 200)]
    if s2_id and S2_KEY:
        d = s2get(f"author/{s2_id}/papers", {"fields": "title,externalIds,venue,year,publicationDate,authors", "limit": 500})
        for p in d.get("data", []):
            issued = p.get("publicationDate") or str(p.get("year") or "")  # S2 often has a year but no date
            if issued and issued >= since[:len(issued)]:
                recs.append(record((p.get("externalIds") or {}).get("DOI"), p.get("title") or "", p.get("venue") or "",
                                   issued, [x["name"] for x in p.get("authors", [])], "semanticscholar"))
    elif s2_id:
        print("intake: --s2-id ignored, SEMANTIC_SCHOLAR_API_KEY is not set", file=sys.stderr)
    return merge(recs)


def role(authors: list[str], name: str) -> str:
    idx = [i for i, a in enumerate(authors) if name.lower() in a.lower()]
    if not idx:
        return "absent"
    i = idx[0]
    tags = (["first"] if i == 0 else []) + (["corresponding"] if authors[i].endswith("*") else []) + \
           (["last"] if i == len(authors) - 1 and i else [])
    return "+".join(tags) or "middle"


def exemplars(path: str, name: str, top4: bool) -> str:
    items = json.loads(Path(path).read_text())["items"]
    rows = ["| year | venue | status | role | title | id |", "|---|---|---|---|---|---|"]
    for it in sorted(items, key=lambda i: -(i.get("year") or 0)):
        if top4 and it.get("venue") not in TOP4_NAMES:
            continue
        ident = f"doi:{it['doi']}" if it.get("doi") else (f"arXiv:{it['arxiv']}" if it.get("arxiv") else "")
        rows.append(f"| {it.get('year', '')} | {it.get('venue', '')} | {it.get('status', '')} | "
                    f"{role(it.get('authors', []), name)} | {it.get('title', '')} | {ident} |")
    return "\n".join(rows)


def append_queue(path: str, recs: list[dict]) -> int:
    p = Path(path)
    seen = {json.loads(l)["key"] for l in p.read_text().splitlines() if l.strip()} if p.exists() else set()
    new = [r for r in recs if r["key"] not in seen]
    with p.open("a") as f:
        for r in new:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return len(new)


def opt(args: list[str], flag: str, default: str = "") -> str:
    return args[args.index(flag) + 1] if flag in args else default


def selftest() -> None:
    import tempfile
    assert abstract_text({"effect": [1], "Causal": [0]}) == "Causal effect"
    assert hits("Rerandomization and Covariate Adjustment") == ["rerandomization", "covariate adjustment"]
    assert hits("Distribution Matching to identify outliers in a randomized test") == []
    a = record("10.1/X", "Causal A", "jasa", "2026", [], "crossref")
    b = record("10.1/x", "Causal A", "jasa", "", [], "openalex", oa=("green", "https://arxiv.org/abs/1"))
    m = merge([a, b])
    assert len(m) == 1 and m[0]["source"] == ["crossref", "openalex"] and m[0]["oa_status"] == "green"
    assert oa_fields({"open_access": {"oa_status": "hybrid", "oa_url": "https://tandfonline.com/x"}}) == ("hybrid", "")
    assert role(["A B", "Ann Author*"], "Ann Author") == "corresponding+last"
    assert role(["Ann Author", "C D"], "Ann Author") == "first"
    with tempfile.TemporaryDirectory() as d:
        qf = str(Path(d) / "queue.jsonl")
        assert append_queue(qf, m) == 1 and append_queue(qf, m) == 0
        pub = Path(d) / "p.json"
        pub.write_text(json.dumps({"items": [{"title": "T", "year": 2026, "venue": "JRSS-B", "status": "published",
                                              "authors": ["Ann Author*"], "arxiv": "1"},
                                             {"title": "U", "venue": "arXiv", "authors": ["X"]}]}))
        t = exemplars(str(pub), "Ann Author", True)
        assert "first+corresponding" in t and "arXiv:1" in t and "| U |" not in t
    assert wait_for(0, "12") == 12 and [wait_for(i, None) for i in range(3)] == [8, 15, 30]
    global get, S2_KEY  # offline: stub the network and the clock
    calls, slept, real_get, real_sleep, real_key = [], [], get, time.sleep, S2_KEY
    get = lambda url, headers=None, body=None: calls.append(url) or {"data": [], "results": [], "message": {"items": []}}
    time.sleep = lambda s: slept.append(s)
    try:
        S2_KEY = ""
        journal("jasa", "2026-01-01", 5, True)
        assert not any("semanticscholar" in c for c in calls), "S2 must be skipped without a key"
        S2_KEY = "test"
        s2get("author/search", {}); s2get("author/search", {})
        assert slept[-1] > 1.0, "second S2 call must wait about S2_GAP"
    finally:
        get, time.sleep, S2_KEY = real_get, real_sleep, real_key
    print("intake_search selftest ok")


def main(argv: list[str]) -> None:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    if argv[0] == "--selftest":
        return selftest()
    cmd, rest = argv[0], argv[1:]
    if cmd == "exemplars":
        print(exemplars(rest[0], opt(rest, "--author"), "--top4" in rest))
        return
    if not MAILTO:
        print("intake: INTAKE_MAILTO is not set; Crossref may rate-limit (HTTP 429)", file=sys.stderr)
    since = opt(rest, "--since", f"{time.gmtime().tm_year}-01-01")
    if cmd == "journal":
        recs = journal(rest[0], since, int(opt(rest, "--max", "200")), "--all" in rest)
    elif cmd == "author":
        recs = author(rest[0], opt(rest, "--openalex-id"), opt(rest, "--s2-id"), since)
    else:
        raise SystemExit(f"intake: unknown command {cmd}; see --help")
    if "--queue" in rest:
        print(f"intake: {append_queue(opt(rest, '--queue'), recs)} new record(s) queued", file=sys.stderr)
    for r in recs:
        print(f"{r['issued']}\t{r['venue_slug']}\t{','.join(r['keyword_hits']) or '-'}\t{r['oa_status']}\t{r['doi'] or '-'}\t{r['title']}")


if __name__ == "__main__":
    main(sys.argv[1:])
