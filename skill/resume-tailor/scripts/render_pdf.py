#!/usr/bin/env python3
"""Render a filled resume HTML to a one-page, text-based PDF and verify the page count.

Usage: python render_pdf.py <input.html> <output.pdf>

Tries HTML->PDF backends in order of layout fidelity, then verifies the page count.
The caller MUST see "PAGES: 1" (exit 0) before treating the PDF as done. If no backend is
available (exit 3), fall back to delivering the polished HTML and having the user
Print -> Save as PDF (Letter).

Exit codes:
  0  rendered AND verified exactly one page.
  2  rendered but one page NOT confirmed — more than one page, OR the page count could not
     be verified (pypdf missing). Do not treat as done; cut content or install pypdf.
  3  no PDF backend available -> fall back to HTML.
  1  usage error, or the input HTML file was not found, or another hard error.
"""
import os
import sys


def _render_weasyprint(html_path: str, pdf_path: str) -> bool:
    try:
        from weasyprint import HTML
    except Exception:
        return False
    HTML(filename=html_path).write_pdf(pdf_path)
    return True


def _render_xhtml2pdf(html_path: str, pdf_path: str) -> bool:
    # Pure-Python fallback (reportlab-based, no system libraries). Limited CSS support:
    # layout may degrade vs. weasyprint, but it produces a text-based PDF with no deps.
    try:
        from xhtml2pdf import pisa
    except Exception:
        return False
    with open(html_path, "r", encoding="utf-8") as src, open(pdf_path, "wb") as out:
        result = pisa.CreatePDF(src.read(), dest=out)
    return not result.err


def _reader(pdf_path):
    try:
        from pypdf import PdfReader
        return PdfReader(pdf_path)
    except Exception:
        pass
    try:
        from PyPDF2 import PdfReader  # older name
        return PdfReader(pdf_path)
    except Exception:
        return None


def _page_count(pdf_path):
    r = _reader(pdf_path)
    return None if r is None else len(r.pages)


def _text_len(pdf_path):
    r = _reader(pdf_path)
    if r is None:
        return None
    try:
        return sum(len((p.extract_text() or "")) for p in r.pages)
    except Exception:
        return None


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: python render_pdf.py <input.html> <output.pdf>", file=sys.stderr)
        return 1
    html_path, pdf_path = sys.argv[1], sys.argv[2]

    # Distinguish a bad input path from a missing backend (both used to look like exit 3).
    if not os.path.isfile(html_path):
        print(f"INPUT_NOT_FOUND: no such HTML file: {html_path}", file=sys.stderr)
        return 1

    backend = None
    for name, fn in (("weasyprint", _render_weasyprint), ("xhtml2pdf", _render_xhtml2pdf)):
        try:
            if fn(html_path, pdf_path):
                backend = name
                break
        except Exception as exc:  # backend present but failed on this input
            print(f"{name} failed: {exc}", file=sys.stderr)

    if backend is None:
        print("NO_PDF_BACKEND: install weasyprint or xhtml2pdf, or fall back to HTML.",
              file=sys.stderr)
        return 3

    pages = _page_count(pdf_path)
    if pages is None:
        # Rendered, but we cannot prove it's one page. Never report success unverified.
        print(f"RENDERED with {backend} but COULD NOT verify the page count (install pypdf). "
              "Treat as NOT confirmed one page.", file=sys.stderr)
        return 2

    text_len = _text_len(pdf_path)
    if text_len is not None and text_len < 40:
        print(f"WARNING: rendered PDF has almost no extractable text ({text_len} chars) — "
              "the input HTML may be empty or malformed.", file=sys.stderr)

    print(f"RENDERED with {backend}. PAGES: {pages}")
    return 0 if pages == 1 else 2


if __name__ == "__main__":
    raise SystemExit(main())
