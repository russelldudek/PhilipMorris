"""Apply a restrained PMI identity layer to generated application PDFs."""
from io import BytesIO
from pathlib import Path
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import HexColor, white
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs"
HIRES = ROOT / "assets" / "brand" / "pmi-wordmark-hires.png"
FALLBACK = ROOT / "assets" / "brand" / "pmi-wordmark.png"
LOGO = HIRES if HIRES.exists() else FALLBACK
BLUE = HexColor("#0074C2")
DEEP = HexColor("#004A80")

def stamp_pdf(path: Path) -> None:
    reader = PdfReader(str(path))
    writer = PdfWriter()
    for page in reader.pages:
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        buffer = BytesIO()
        canvas = Canvas(buffer, pagesize=(width, height))
        canvas.setFillColor(BLUE)
        canvas.rect(0, height - 5, width, 5, stroke=0, fill=1)
        logo_width = 112
        logo_height = logo_width * (40 / 176)
        x = width - 43 - logo_width
        y = 12
        canvas.setFillColor(white)
        canvas.rect(x - 7, y - 5, logo_width + 14, logo_height + 10, stroke=0, fill=1)
        canvas.drawImage(ImageReader(str(LOGO)), x, y, width=logo_width, height=logo_height,
                         mask="auto", preserveAspectRatio=True)
        canvas.setFillColor(DEEP)
        canvas.setFont("Helvetica", 5.8)
        canvas.drawRightString(x - 10, y + logo_height / 2 - 2, "Independent candidate work")
        canvas.save()
        buffer.seek(0)
        page.merge_page(PdfReader(buffer).pages[0])
        writer.add_page(page)
    temporary = path.with_suffix(".branded.pdf")
    with temporary.open("wb") as handle:
        writer.write(handle)
    temporary.replace(path)

def stamp_all() -> None:
    for path in sorted(OUT.glob("*.pdf")):
        stamp_pdf(path)

if __name__ == "__main__":
    stamp_all()
