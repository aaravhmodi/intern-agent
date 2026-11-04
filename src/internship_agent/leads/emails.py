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
    "last": "{last}",
    "f.last": "{f}.{last}",
}


# Letters that don't break down into a plain letter plus an accent.
_SPELLED_OUT = str.maketrans({"ø": "o", "æ": "ae", "œ": "oe", "ß": "ss", "ł": "l", "đ": "d"})


def _clean(part: str) -> str:
    part = part.lower().translate(_SPELLED_OUT)
    ascii_part = unicodedata.normalize("NFKD", part).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z]", "", ascii_part.lower())


# Titles around a name that are not part of it ("Dr. Ali Haddad" was once sent to dr@).
_TITLES = frozenset({"dr", "mr", "mrs", "ms", "prof", "sir", "jr", "sr", "ii", "iii", "phd", "md"})


def name_words(full_name: str) -> list[str]:
    """The words of a person's name as written, without titles such as Dr. or PhD."""
    return [w for w in full_name.replace(",", " ").split() if _clean(w) not in _TITLES]


def guess_email(full_name: str, domain: str, pattern: str) -> str:
    """Build an address such as jane.doe@acme.ai. The result is always unverified."""
    if pattern not in PATTERNS:
        raise ValueError(f"unknown pattern {pattern!r}; expected one of {sorted(PATTERNS)}")
    names = [_clean(p) for p in name_words(full_name)]
    names = [n for n in names if n]
    if len(names) < 2:
        raise ValueError(f"need a first and last name, got {full_name!r}")
    first, last = names[0], names[-1]
    local = PATTERNS[pattern].format(first=first, last=last, f=first[0], l=last[0])
    return f"{local}@{domain.lower().removeprefix('www.')}"
