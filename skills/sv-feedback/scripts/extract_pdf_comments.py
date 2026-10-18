#!/usr/bin/env python3
"""Extract PDF reviewer annotations as concise Markdown records."""

import sys
import pymupdf as fitz


def point_xy(point):
    """Return coordinates for PyMuPDF Point objects or tuple-style vertices."""
    if hasattr(point, "x"):
        return point.x, point.y
    return point[0], point[1]


def get_words_on_page(page):
    """Return list of (x0, y0, x1, y1, word) tuples for the page."""
    return [(w[0], w[1], w[2], w[3], w[4]) for w in page.get_text("words")]


def rects_overlap(r1, r2, threshold=0.3):
    """Check if two rects overlap by at least threshold of the smaller rect's area."""
    ix0 = max(r1[0], r2[0])
    iy0 = max(r1[1], r2[1])
    ix1 = min(r1[2], r2[2])
    iy1 = min(r1[3], r2[3])
    if ix1 <= ix0 or iy1 <= iy0:
        return False
    inter = (ix1 - ix0) * (iy1 - iy0)
    area1 = (r1[2] - r1[0]) * (r1[3] - r1[1])
    area2 = (r2[2] - r2[0]) * (r2[3] - r2[1])
    smaller = min(area1, area2)
    return smaller > 0 and (inter / smaller) >= threshold


def get_enclosed_text(page, annot, words):
    """Extract full enclosed text for highlight/underline/squiggly/strikeout."""
    # Try using annotation quads first
    try:
        quads = annot.vertices
    except Exception:
        quads = None

    selected_indices = set()

    if quads and len(quads) >= 4:
        # quads is a flat list of points; group into quads of 4 points
        quad_rects = []
        for i in range(0, len(quads), 4):
            pts = quads[i:i+4]
            if len(pts) == 4:
                coords = [point_xy(p) for p in pts]
                xs = [x for x, _ in coords]
                ys = [y for _, y in coords]
                quad_rects.append((min(xs), min(ys), max(xs), max(ys)))

        for qi, qr in enumerate(quad_rects):
            for wi, w in enumerate(words):
                if rects_overlap(qr, (w[0], w[1], w[2], w[3])):
                    selected_indices.add(wi)

    # Fallback: use annot rect
    if not selected_indices:
        r = annot.rect
        ar = (r.x0, r.y0, r.x1, r.y1)
        for wi, w in enumerate(words):
            if rects_overlap(ar, (w[0], w[1], w[2], w[3]), threshold=0.1):
                selected_indices.add(wi)

    if not selected_indices:
        # Last resort: extract text from rect directly
        r = annot.rect
        text = page.get_text("text", clip=r).strip()
        return text or "[unrecoverable]"

    # Sort selected words in reading order (by y then x)
    selected = sorted(selected_indices, key=lambda i: (round(words[i][1] / 5) * 5, words[i][0]))
    return " ".join(words[i][4] for i in selected)


def get_nearby_text(words, enclosed_indices, window=8):
    """Build nearby text window around enclosed words."""
    if not enclosed_indices:
        return "[no nearby]"

    all_sorted = sorted(range(len(words)), key=lambda i: (round(words[i][1] / 5) * 5, words[i][0]))
    pos_map = {wi: pos for pos, wi in enumerate(all_sorted)}

    min_pos = min(pos_map[i] for i in enclosed_indices if i in pos_map)
    max_pos = max(pos_map[i] for i in enclosed_indices if i in pos_map)

    before_indices = [all_sorted[p] for p in range(max(0, min_pos - window), min_pos)]
    after_indices = [all_sorted[p] for p in range(max_pos + 1, min(len(all_sorted), max_pos + 1 + window))]

    before = " ".join(words[i][4] for i in before_indices)
    after = " ".join(words[i][4] for i in after_indices)

    parts = []
    if before:
        parts.append(before)
    parts.append("[ENCLOSED]")
    if after:
        parts.append(after)
    return " ".join(parts)


def get_nearest_text(page, annot, words, window=8):
    """For sticky notes / free text: find nearest words around the annotation position."""
    r = annot.rect
    cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2

    def dist(w):
        wx, wy = (w[0] + w[2]) / 2, (w[1] + w[3]) / 2
        return ((wx - cx) ** 2 + (wy - cy) ** 2) ** 0.5

    sorted_words = sorted(range(len(words)), key=lambda i: dist(words[i]))
    nearest = sorted(sorted_words[:window], key=lambda i: (round(words[i][1] / 5) * 5, words[i][0]))
    return " ".join(words[i][4] for i in nearest)


def extract_annotations(pdf_path):
    doc = fitz.open(pdf_path)
    records = []
    n = 0

    for page_num in range(len(doc)):
        page = doc[page_num]
        words = get_words_on_page(page)

        for annot in page.annots():
            n += 1
            info = annot.info
            annotator = info.get("title", "") or info.get("subject", "") or "Unknown"
            comment = info.get("content", "").strip() or "to be deleted"
            atype = annot.type[1]  # e.g. "Highlight", "Underline", "StrikeOut", "Text", "FreeText"

            if atype in ("Highlight", "Underline", "Squiggly", "StrikeOut"):
                # Get enclosed text and nearby window
                try:
                    quads = annot.vertices
                except Exception:
                    quads = None

                selected_indices = set()
                if quads and len(quads) >= 4:
                    quad_rects = []
                    for i in range(0, len(quads), 4):
                        pts = quads[i:i+4]
                        if len(pts) == 4:
                            coords = [point_xy(p) for p in pts]
                            xs = [x for x, _ in coords]
                            ys = [y for _, y in coords]
                            quad_rects.append((min(xs), min(ys), max(xs), max(ys)))
                    for qr in quad_rects:
                        for wi, w in enumerate(words):
                            if rects_overlap(qr, (w[0], w[1], w[2], w[3])):
                                selected_indices.add(wi)

                if not selected_indices:
                    r = annot.rect
                    ar = (r.x0, r.y0, r.x1, r.y1)
                    for wi, w in enumerate(words):
                        if rects_overlap(ar, (w[0], w[1], w[2], w[3]), threshold=0.1):
                            selected_indices.add(wi)

                if selected_indices:
                    all_sorted = sorted(range(len(words)), key=lambda i: (round(words[i][1] / 5) * 5, words[i][0]))
                    pos_map = {wi: pos for pos, wi in enumerate(all_sorted)}
                    sel_sorted = sorted(selected_indices, key=lambda i: (round(words[i][1] / 5) * 5, words[i][0]))
                    enclosed = " ".join(words[i][4] for i in sel_sorted)
                    nearby = get_nearby_text(words, selected_indices)
                else:
                    r = annot.rect
                    enclosed = page.get_text("text", clip=r).strip() or "[unrecoverable]"
                    nearby = "[no nearby context]"

            else:
                # Sticky note, FreeText, Ink, etc.
                enclosed = get_nearest_text(page, annot, words)
                nearby = "[sticky/freetext — nearest words shown as enclosed]"

            records.append({
                "n": n,
                "page": page_num + 1,
                "type": atype,
                "annotator": annotator,
                "nearby": nearby,
                "enclosed": enclosed,
                "comment": comment,
            })

    doc.close()
    return records


def write_page_markdown(records, page_num):
    lines = [f"# Page {page_num}\n"]
    for r in records:
        lines.append(f"## {r['n']}. {r['type']} - {r['annotator']}\n")
        lines.append(f"Nearby: `{r['nearby']}`\n")
        lines.append(f"Enclosed: `{r['enclosed']}`\n")
        lines.append(f"Comment: {r['comment']}\n")
        lines.append("")
    return "\n".join(lines)


def write_pages(records, output_dir):
    import os
    os.makedirs(output_dir, exist_ok=True)

    by_page = {}
    for r in records:
        by_page.setdefault(r["page"], []).append(r)

    created = []
    for page_num in sorted(by_page):
        filename = f"page_{page_num:03d}.md"
        filepath = os.path.join(output_dir, filename)
        content = write_page_markdown(by_page[page_num], page_num)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        created.append((page_num, filename, len(by_page[page_num])))

    index_lines = ["# Comments Index\n"]
    for page_num, filename, count in created:
        index_lines.append(f"- [Page {page_num}]({filename}) ({count} annotations)")
    with open(os.path.join(output_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines) + "\n")

    return created


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf_comments.py <input.pdf> [output_dir]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    if len(sys.argv) >= 3:
        output_dir = sys.argv[2]
    else:
        import os
        stem = os.path.splitext(pdf_path)[0]
        output_dir = stem + "_comments"

    records = extract_annotations(pdf_path)
    created = write_pages(records, output_dir)
    print(f"Extracted {len(records)} annotations across {len(created)} pages → {output_dir}/")
