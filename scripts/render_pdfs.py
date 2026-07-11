#!/usr/bin/env python3
"""Render all PMI campaign PDFs from the committed document model."""
from pdf_documents import resume, cover_letter, brief, entry_plan, objection
from pdf_common import OUT

if __name__ == "__main__":
    resume()
    cover_letter()
    brief()
    entry_plan()
    objection()
    print(f"Rendered PMI campaign PDFs to {OUT}")
