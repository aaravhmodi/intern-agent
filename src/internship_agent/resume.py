from pathlib import Path

from pypdf import PdfReader


def load_resume_text(pdf_path: Path, cache_path: Path) -> str:
    """Extract resume text once and cache it; re-extract when the PDF is newer."""
    if cache_path.exists() and cache_path.stat().st_mtime >= pdf_path.stat().st_mtime:
        return cache_path.read_text(encoding="utf-8")
    text = "\n".join(page.extract_text() or "" for page in PdfReader(pdf_path).pages).strip()
    if not text:
        raise ValueError(f"No text could be extracted from {pdf_path}")
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(text, encoding="utf-8")
    return text
