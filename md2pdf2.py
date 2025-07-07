#!/usr/bin/env python3
"""
md_to_pdf.py – Markdown → PDF (WeasyPrint) CLI tool

Usage:
    $ python md_to_pdf.py
    (start typing markdown…)  
    Ctrl+D  # finish input

Dependencies:
    pip install markdown weasyprint markdown-katex
    brew install cairo pango gdk-pixbuf libffi (on macOS for weasyprint)

Output:
    ~/Desktop/md_output_YYYYMMDD_HHMMSS.pdf
"""

import sys
import os
import datetime


def read_markdown() -> str:
    """Read Markdown text from STDIN until EOF (Ctrl+D)."""
    print("Enter your Markdown. Press Ctrl+D to finish.")
    return sys.stdin.read()


def markdown_to_html(md_text: str) -> str:
    """Convert Markdown to HTML with math (LaTeX) support."""
    try:
        import markdown
        from markdown_katex import KatexExtension
    except ImportError:
        sys.exit("❌  Install dependencies: pip install markdown markdown-katex")
    
    return markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables", KatexExtension(no_inline_svg=True)]
    )


def html_to_pdf(html: str, out_path: str) -> None:
    """Render HTML to PDF using WeasyPrint."""
    try:
        from weasyprint import HTML
    except ImportError:
        sys.exit("❌  Install weasyprint: pip install weasyprint")

    # inject minimal KaTeX CSS for LaTeX rendering
    katex_css = """
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.css">
    """
    html = f"<!DOCTYPE html><html><head>{katex_css}</head><body>{html}</body></html>"

    HTML(string=html).write_pdf(out_path)


def write_on_desktop(filename: str) -> str:
    """Return path to save *filename* on Desktop (fallback: cwd)."""
    home = os.path.expanduser("~")
    desktop = os.path.join(home, "Desktop")
    return os.path.join(desktop if os.path.isdir(desktop) else os.getcwd(), filename)


def main() -> None:
    md_text = read_markdown()
    if not md_text.strip():
        sys.exit("No Markdown supplied. Exiting.")

    html = markdown_to_html(md_text)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out_file = write_on_desktop(f"md_output_{timestamp}.pdf")

    html_to_pdf(html, out_file)
    print(f"✅  Saved PDF → {out_file}")


if __name__ == "__main__":
    main()
