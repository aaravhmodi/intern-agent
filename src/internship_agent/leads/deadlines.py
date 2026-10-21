"""Find an application deadline stated in a posting's text, e.g. "Apply by November 30, 2026"."""

import re
from datetime import date, datetime

_MONTH = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?"
_DATE = rf"({_MONTH}\s+\d{{1,2}}(?:st|nd|rd|th)?,?\s+\d{{4}}|\d{{4}}-\d{{2}}-\d{{2}})"
_CUE = (
    r"(?:apply\s+(?:by|before)|application\s+deadline|applications?\s+(?:close|due)"
    r"|(?:closing|close)\s+date|deadline(?:\s+to\s+apply)?|closes?)"
)
_FOUND = re.compile(rf"{_CUE}\s*(?:is|on|:|-)?\s*{_DATE}", re.IGNORECASE)
_FORMATS = ("%Y-%m-%d", "%B %d, %Y", "%B %d %Y", "%b %d, %Y", "%b %d %Y")


def find_deadline(text: str) -> date | None:
    """The first deadline the text states, or None. Only a full date with a year counts."""
    for match in _FOUND.finditer(text):
        raw = re.sub(r"(?<=\d)(st|nd|rd|th)", "", match.group(1)).replace("Sept", "Sep")
        raw = raw.replace(".", "")
        for fmt in _FORMATS:
            try:
                return datetime.strptime(raw, fmt).date()
            except ValueError:
                continue
    return None
