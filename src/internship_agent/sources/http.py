"""Small HTTP helpers for public, no-auth job and news feeds."""

import json
import urllib.request
from typing import Any

USER_AGENT = "Mozilla/5.0 (compatible; internship-agent)"


def get_bytes(url: str, timeout: float = 15) -> bytes:
    if not url.startswith("https://"):
        raise ValueError(f"only https URLs are fetched: {url}")
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body: bytes = response.read()
    return body


def get_text(url: str, timeout: float = 15) -> str:
    return get_bytes(url, timeout).decode("utf-8", "ignore")


def get_json(url: str, timeout: float = 15) -> Any:
    return json.loads(get_bytes(url, timeout))
