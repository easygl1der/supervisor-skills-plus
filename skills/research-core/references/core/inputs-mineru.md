# Document input: MinerU only

Every PDF (paper, textbook chapter, exemplar, scanned notes) is converted to
Markdown plus images with MinerU before any skill reads it. No other PDF text
extractor is used: not pdf-parse, PyMuPDF, pypdf, pdfplumber, pdftotext or a
model reading the PDF directly. [src: user:2026-10-16] (confirmed)

Why: generic extractors drop equations, tables and reading order, and merge
two-column layouts, so theory and statistics papers become unreadable and
numbers get misread. MinerU keeps section headings, LaTeX equations, tables
and figures. [src: up:docs/handoff/claude-paper-deepdive-2026-10-16.md]

## Routes, in order

All three run the MinerU engine; use the first one available in the current
environment.

| # | Route | How | Limits and privacy |
|---|---|---|---|
| 1 | MinerU MCP | tool `mineru_parse_documents_smart` (local PDF path or URL) | the owner's wrapper server; splits long PDFs past upstream page and size limits; `model='pipeline'` default, `model='vlm'` for hard layouts |
| 2 | MinerU official CLI | `mineru-open-api flash-extract <pdf> -o <dir>` (no token); `mineru-open-api extract` with a token for long files | flash: 20 pages and 10 MB per call; uploads the file to mineru.net, so ask before sending an unpublished manuscript |
| 3 | Local MinerU | `mineru -p <pdf> -o <dir>` | needs a local install |

Splitting a long PDF into page ranges before route 2 is allowed (page
splitting does not read text). Record the page range in the output's
metadata.

## On failure: stop

If no route works, stop and say so plainly: which routes were tried, the
error of each, and what the user can do (start the MCP server, add a token,
install MinerU, or supply Markdown or LaTeX they converted themselves). Do
not fall back to another extractor and do not summarize from the abstract
page or from memory.

## Other inputs

- Markdown, plain text or LaTeX supplied by the user: read directly.
- arXiv TeX source: only as corroboration (to check an equation or a number
  that MinerU rendered badly), never as the primary text, and only when the
  user agrees to download it.
- Web pages: `mineru-open-api crawl <url>` or the user's own copy.

## Readability gate

After conversion check: headings present and in order, equations intact
(spot-check three), tables not flattened, figure files saved. Report pages
converted, route used and any damaged regions before using the text.
Quote page, section, table, figure and equation labels from the original,
not MinerU's internal numbering.
