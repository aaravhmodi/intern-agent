"""Links into the dashboard. Each view is a page (`/#/jobs`) and an item inside it is
`/#/picked/<key>`, so a push opens exactly what it's about, not the home page."""

from urllib.parse import quote


def page_url(base: str | None, view: str, key: str | None = None) -> str | None:
    """The dashboard page for a view, or for one lead or event in it. None without a base."""
    if not base:
        return None
    path = f"/#/{view}" + (f"/{quote(key, safe='')}" if key else "")
    return base.rstrip("/") + path
