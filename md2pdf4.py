#!/usr/bin/env python3
"""
md_to_pdf.py — Markdown to PDF via CLI (supports --engine=weasyprint or pandoc)

Usage:
    $ python md_to_pdf.py --engine=weasyprint [input.md]
    (if no file, markdown 입력)
    Ctrl+D

    $ python md_to_pdf.py --engine=pandoc [input.md]

Font requirements for best Unicode/emoji/math support (install via Google Fonts or Homebrew):
    - Noto Sans
    - Noto Sans Math
    - Menlo (or another monospaced font)
"""

import sys
import os
import datetime
import subprocess

def read_markdown(filename=None) -> str:
    if filename:
        with open(filename, encoding="utf-8") as f:
            return f.read()
    print("Enter your Markdown. Press Ctrl+D to finish.")
    return sys.stdin.read()

def markdown_to_html(md_text: str) -> str:
    try:
        import markdown
        from markdown_katex import KatexExtension
    except ImportError:
        sys.exit("❌ Install: pip install markdown markdown-katex")

    return markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables", KatexExtension(no_inline_svg=True)]
    )

def html_to_pdf_weasyprint(html: str, out_path: str) -> None:
    try:
        from weasyprint import HTML
    except ImportError:
        sys.exit("❌ Install: pip install weasyprint")
    
    katex_css = """<link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.css\">"""
    full_html = f"<!DOCTYPE html><html><head>{katex_css}</head><body>{html}</body></html>"
    HTML(string=full_html).write_pdf(out_path)

def markdown_to_pdf_pandoc(md_text: str, out_path: str) -> None:
    with open("temp_input.md", "w", encoding="utf-8") as f:
        f.write(md_text)

    # Use lualatex for better Unicode/emoji support (may require further customization for color emoji)
    cmd = [
        "pandoc", "temp_input.md",
        "-o", out_path,
        "--pdf-engine=lualatex",
        "-V", "mainfont=Arial Unicode MS",
        "-V", "mathfont=Arial Unicode MS",
        "-V", "monofont=Arial Unicode MS"
    ]
    # To use Apple SD Gothic Neo instead, comment out the block above and uncomment below:
    # cmd = [
    #     "pandoc", "temp_input.md",
    #     "-o", out_path,
    #     "--pdf-engine=lualatex",
    #     "-V", "mainfont=Apple SD Gothic Neo",
    #     "-V", "mathfont=Apple SD Gothic Neo",
    #     "-V", "monofont=Apple SD Gothic Neo"
    # ]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        sys.exit("❌ Pandoc failed. Check if pandoc and lualatex are installed.")
    finally:
        os.remove("temp_input.md")

def write_in_cwd(filename: str) -> str:
    # Save output PDF in the current working directory
    return os.path.join(os.getcwd(), filename)

def main():
    engine = "pandoc"  # default
    if "--engine=pandoc" in sys.argv:
        engine = "pandoc"
    elif "--engine=weasyprint" in sys.argv:
        engine = "weasyprint"
    elif any(arg.startswith("--engine=") for arg in sys.argv):
        sys.exit("❌ --engine must be 'weasyprint' or 'pandoc'")

    # Find positional argument for filename (first non-flag argument)
    filename = None
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            filename = arg
            break

    md_text = read_markdown(filename)
    if not md_text.strip():
        sys.exit("❌ No markdown supplied.")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = write_in_cwd(f"md_output_{timestamp}.pdf")

    if engine == "weasyprint":
        html = markdown_to_html(md_text)
        html_to_pdf_weasyprint(html, out_path)
    else:
        markdown_to_pdf_pandoc(md_text, out_path)

    print(f"✅ PDF saved → {out_path}")

if __name__ == "__main__":
    main() 