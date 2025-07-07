import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# JSON 로드
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# PDF 생성
pdf_file = 'output.pdf'
c = canvas.Canvas(pdf_file, pagesize=A4)
width, height = A4

# 기본 위치 설정
x = 50
y = height - 50
line_height = 15

# JSON 내용을 PDF에 기록
def draw_json(obj, indent=0):
    global y
    space = ' ' * (indent * 4)
    if isinstance(obj, dict):
        for key, value in obj.items():
            text = f"{space}{key}:"
            c.drawString(x, y, text)
            y -= line_height
            draw_json(value, indent + 1)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            c.drawString(x, y, f"{space}- [{i}]")
            y -= line_height
            draw_json(item, indent + 1)
    else:
        c.drawString(x, y, f"{space}{obj}")
        y -= line_height

draw_json(data)
c.save()
