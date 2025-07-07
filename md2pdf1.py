#!/usr/bin/env python3
"""
md_to_pdf.py – tiny CLI tool

Usage:
    $ python md_to_pdf.py
    (start typing markdown…)  
    ...  
    pppp   # <-- sentinel, finish input

The script keeps reading STDIN until it sees a line that is exactly
"pppp", then converts the collected Markdown to a PDF and drops it on
your Desktop.

Dependencies:
    pip install markdown weasyprint
    # weasyprint needs libffi/pango/cairo on Linux; on macOS install
    # via brew install pango cairo gdk-pixbuf libffi

Output:
    ~/Desktop/md_output_YYYYMMDD_HHMMSS.pdf
"""

import sys
import os
import datetime


def read_markdown(sentinel: str = "pppp") -> str:
    """Read multiline Markdown from STDIN until a line equals *sentinel*."""
    print("Enter your Markdown. Finish with a single line containing 'pppp'.")
    buf: list[str] = []
    for line in sys.stdin:
        if line.strip() == sentinel:
            break
        buf.append(line)
    return "".join(buf)


def markdown_to_html(md_text: str) -> str:
    """Convert Markdown text to HTML using *markdown* package."""
    try:
        import markdown  # local import so script still runs if missing
    except ImportError:
        sys.exit("❌  Install dependency first:  pip install markdown")
    return markdown.markdown(md_text, extensions=["fenced_code", "tables"])


def html_to_pdf(html: str, out_path: str) -> None:
    """Render HTML to PDF at *out_path* using weasyprint."""
    try:
        from weasyprint import HTML
    except ImportError:
        sys.exit("❌  Install dependency first:  pip install weasyprint")
    HTML(string=html).write_pdf(out_path)


def write_on_desktop(filename: str) -> str:
    """Return absolute path to *filename* placed on the user's Desktop.
    Falls back to cwd if Desktop cannot be resolved."""
    home = os.path.expanduser("~")
    desktop = os.path.join(home, "Desktop")
    if not os.path.isdir(desktop):
        desktop = os.getcwd()
    return os.path.join(desktop, filename)


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
