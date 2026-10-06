"""Hard character limits for messages, enforced deterministically."""

import re

# LinkedIn caps invitation notes at 200 characters on free accounts.
LINKEDIN_NOTE_LIMIT = 200


def fit_to_limit(text: str, limit: int) -> str:
    """Shorten text to at most `limit` characters without cutting mid-word.

    Prefers ending at the last complete sentence that fits; otherwise cuts at a word
    boundary and adds an ellipsis.
    """
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    window = text[:limit]
    sentence_end = max(window.rfind(". "), window.rfind("? "), window.rfind("! "))
    if window.endswith((".", "?", "!")):
        sentence_end = len(window) - 1
    if sentence_end >= 40:  # a complete sentence beats a mid-sentence cut
        return window[: sentence_end + 1]
    cut = text[: limit - 1].rsplit(" ", 1)[0].rstrip(",;:-—")
    return cut + "…"
