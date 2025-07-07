#!/usr/bin/env python3
"""
md2pdf_tectonic.py — Markdown → PDF (via Pandoc + Tectonic)

Usage:
    $ python md2pdf_tectonic.py
    (입력 후 Ctrl+D로 종료)

Dependencies:
    brew install pandoc tectonic
"""

import sys
import os
import subprocess
import datetime

def read_markdown() -> str:
    print("Enter Markdown content. End with Ctrl+D.")
    return sys.stdin.read()

def write_temp_file(content: str, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def render_pdf_with_pandoc(md_path: str, out_path: str) -> None:
    cmd = [
        "pandoc", md_path,
        "-o", out_path,
        "--pdf-engine=tectonic",
        "-V", "mainfont=Apple SD Gothic Neo",
        "-V", "mathfont=Apple SD Gothic Neo",
        "-V", "monofont=Apple SD Gothic Neo"

    ]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        sys.exit("❌ Pandoc+Tectonic failed. Check installation.")

def write_on_desktop(filename: str) -> str:
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    return os.path.join(desktop if os.path.isdir(desktop) else os.getcwd(), filename)

def main():
    md = read_markdown()
    if not md.strip():
        sys.exit("❌ No markdown content.")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    temp_md = f"/tmp/md_{timestamp}.md"
    pdf_out = write_on_desktop(f"md_output_{timestamp}.pdf")

    write_temp_file(md, temp_md)
    render_pdf_with_pandoc(temp_md, pdf_out)

    print(f"✅ PDF created: {pdf_out}")

if __name__ == "__main__":
    main()
