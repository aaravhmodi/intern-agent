"""Deterministic email-address guesses from a company's known address format."""

import re
import unicodedata

PATTERNS = {
    "first": "{first}",
    "first.last": "{first}.{last}",
    "firstlast": "{first}{last}",
    "flast": "{f}{last}",
    "first_last": "{first}_{last}",
    "firstl": "{first}{l}",
}


def _clean(part: str) -> str:
    ascii_part = unicodedata.normalize("NFKD", part).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z]", "", ascii_part.lower())


def guess_email(full_name: str, domain: str, pattern: str) -> str:
    """Build an address such as jane.doe@acme.ai. The result is always unverified."""
    if pattern not in PATTERNS:
        raise ValueError(f"unknown pattern {pattern!r}; expected one of {sorted(PATTERNS)}")
    names = [_clean(p) for p in full_name.split()]
    names = [n for n in names if n]
    if len(names) < 2:
        raise ValueError(f"need a first and last name, got {full_name!r}")
    first, last = names[0], names[-1]
    local = PATTERNS[pattern].format(first=first, last=last, f=first[0], l=last[0])
    return f"{local}@{domain.lower().removeprefix('www.')}"
