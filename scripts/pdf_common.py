#!/usr/bin/env python3
"""Deterministically render the PMI RoleForge printable artifact set."""
from __future__ import annotations

from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs"
OUT.mkdir(exist_ok=True)
PAGE_W, PAGE_H = A4
INK = colors.HexColor("#111826")
BLUE = colors.HexColor("#175BD8")
MUTED = colors.HexColor("#5D6676")
LINE = colors.HexColor("#D9DEE6")
LIGHT = colors.HexColor("#EEF3FA")
CYAN = colors.HexColor("#08A9C4")
GREEN = colors.HexColor("#0B8F6A")
AMBER = colors.HexColor("#B76B00")

BASE = getSampleStyleSheet()
styles = {
    "title": ParagraphStyle("title", parent=BASE["Title"], fontName="Helvetica-Bold", fontSize=27, leading=27, textColor=INK, spaceAfter=4),
    "identity": ParagraphStyle("identity", parent=BASE["Normal"], fontName="Helvetica-Bold", fontSize=11, leading=13, textColor=BLUE),
    "h2": ParagraphStyle("h2", parent=BASE["Heading2"], fontName="Helvetica-Bold", fontSize=10, leading=12, textColor=INK, spaceBefore=10, spaceAfter=5, uppercase=True),
    "h3": ParagraphStyle("h3", parent=BASE["Heading3"], fontName="Helvetica-Bold", fontSize=9.2, leading=11, textColor=BLUE, spaceAfter=3),
    "body": ParagraphStyle("body", parent=BASE["BodyText"], fontName="Helvetica", fontSize=8.4, leading=11.2, textColor=INK, spaceAfter=5),
    "small": ParagraphStyle("small", parent=BASE["BodyText"], fontName="Helvetica", fontSize=7.5, leading=9.5, textColor=MUTED),
    "summary": ParagraphStyle("summary", parent=BASE["BodyText"], fontName="Helvetica", fontSize=9.2, leading=12.5, textColor=colors.HexColor("#364052"), spaceAfter=6),
    "right": ParagraphStyle("right", parent=BASE["BodyText"], fontName="Helvetica", fontSize=8, leading=10.5, textColor=MUTED, alignment=TA_RIGHT),
    "letter": ParagraphStyle("letter", parent=BASE["BodyText"], fontName="Helvetica", fontSize=9.2, leading=13.7, textColor=INK, spaceAfter=8),
}


def P(text: str, style: str = "body") -> Paragraph:
    return Paragraph(text, styles[style])


def header(title: str, identity: str, right: str = "Russell Dudek<br/>Pittsburgh, Pennsylvania"):
    return Table([[P(title, "title"), P(right, "right")], [P(identity, "identity"), ""]], colWidths=[130*mm, 45*mm], style=TableStyle([
        ("VALIGN", (0,0), (-1,-1), "BOTTOM"), ("SPAN", (1,0), (1,1)),
        ("LINEBELOW", (0,1), (-1,1), .7, LINE), ("BOTTOMPADDING", (0,1), (-1,1), 6),
    ]))


def footer(canvas, doc, label: str):
    canvas.saveState(); canvas.setStrokeColor(LINE); canvas.line(15*mm, 10*mm, PAGE_W-15*mm, 10*mm)
    canvas.setFillColor(MUTED); canvas.setFont("Helvetica", 7)
    canvas.drawString(15*mm, 6*mm, label); canvas.drawRightString(PAGE_W-15*mm, 6*mm, f"Page {doc.page}")
    canvas.restoreState()


def build(path: str, story, label: str, margins=(15, 15, 13, 14)):
    l, r, t, b = [v*mm for v in margins]
    doc = BaseDocTemplate(str(OUT/path), pagesize=A4, leftMargin=l, rightMargin=r, topMargin=t, bottomMargin=b)
    frame = Frame(l, b, PAGE_W-l-r, PAGE_H-t-b, id="main")
    doc.addPageTemplates(PageTemplate(id="pmi", frames=frame, onPage=lambda c,d: footer(c,d,label)))
    doc.build(story)


def section(title: str):
    return [P(title.upper(), "h2"), HRFlowable(width="100%", thickness=.5, color=LINE, spaceAfter=5)]


def bullets(items):
    return [P("• " + x, "body") for x in items]


def grid(cards, cols=2):
    rows=[]
    for i in range(0,len(cards),cols):
        row=[]
        for title,text in cards[i:i+cols]:
            row.append([P(title,"h3"),P(text,"small")])
        while len(row)<cols: row.append("")
        rows.append(row)
    t=Table(rows, colWidths=[(180*mm)/cols]*cols, hAlign="LEFT")
    t.setStyle(TableStyle([("BOX",(0,0),(-1,-1),.5,LINE),("INNERGRID",(0,0),(-1,-1),.5,LINE),("BACKGROUND",(0,0),(-1,-1),colors.white),("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
    return t


def role(org,title,dates,items):
    head=Table([[P(f"<b>{org}</b> · {title}","h3"),P(dates,"right")]],colWidths=[140*mm,35*mm])
    head.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP")]))
    return KeepTogether([head]+bullets(items)+[Spacer(1,3)])
