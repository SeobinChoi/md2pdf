#!/usr/bin/env python3
"""
md2pdf_typst.py — Markdown → Typst → PDF 변환기
입력은 STDIN, 종료는 Ctrl+D
"""

import sys
import os
import subprocess
from datetime import datetime

def read_markdown() -> str:
    print("Enter your Markdown. Finish with Ctrl+D.")
    return sys.stdin.read()

def convert_md_to_typst(md: str) -> str:
    # 기본 템플릿: 헤더 추가, 수식 $$ $$도 감쌈
    preamble = "#set page(width: 21cm, height: 29.7cm, margin: 2cm)\n\n"
    body = md.replace("$$", "$")  # Typst는 $ 수식만 지원
    return preamble + body

def write_typst_file(content: str, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def render_typst_to_pdf(src_path: str, out_path: str) -> None:
    try:
        subprocess.run(["typst", "compile", src_path, out_path], check=True)
    except subprocess.CalledProcessError:
        sys.exit("❌ Typst 컴파일 실패. typst가 설치되어 있는지 확인.")

def write_on_desktop(filename: str) -> str:
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    return os.path.join(desktop, filename)

def main():
    md = read_markdown()
    if not md.strip():
        sys.exit("❌ 입력 없음. 종료")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    typ_path = f"/tmp/md_{timestamp}.typ"
    pdf_path = write_on_desktop(f"md_typst_{timestamp}.pdf")

    typst_code = convert_md_to_typst(md)
    write_typst_file(typst_code, typ_path)
    render_typst_to_pdf(typ_path, pdf_path)

    print(f"✅ PDF 생성 완료 → {pdf_path}")

if __name__ == "__main__":
    main()
