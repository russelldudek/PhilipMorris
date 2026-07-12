#!/usr/bin/env python3
"""Render and brand all PMI campaign PDFs from the committed document model."""
from pdf_documents import resume, cover_letter, brief, entry_plan, objection
from pdf_common import OUT
from stamp_pmi_brand import stamp_all

if __name__ == "__main__":
    resume()
    cover_letter()
    brief()
    entry_plan()
    objection()
    stamp_all()
    print(f"Rendered and PMI-branded campaign PDFs to {OUT}")
