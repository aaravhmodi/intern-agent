"""Store a hand-written film in the local GitDiagram, render it to MP4 and download it.

python make.py film_explainer [landscape|vertical ...] [--theme clay]

The theme (default lavender, GitDiagram's own) recolours the engine in the GitDiagram checkout
named by GITDIAGRAM_DIR (default: a "gitdiagram" folder beside this repository) before the
render; see ../gitdiagram/theme.py.
"""

import importlib
import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "http://127.0.0.1:3000"
REPO = Path(__file__).resolve().parents[4]  # the intern-agent checkout
OUT = Path(__file__).parent / "out"
GITDIAGRAM = Path(os.environ.get("GITDIAGRAM_DIR", REPO.parent / "gitdiagram"))
HEADERS = {"Content-Type": "application/json", "Origin": BASE}


def post(path: str, body: dict, timeout: float = 900) -> bytes:
    req = urllib.request.Request(BASE + path, data=json.dumps(body).encode(), headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as res:
        return res.read()


def main() -> None:
    args = sys.argv[1:]
    theme = "lavender"
    if "--theme" in args:
        at = args.index("--theme")
        theme = args[at + 1]
        del args[at : at + 2]
    name, formats = args[0], args[1:] or ["landscape"]
    sys.path.insert(0, str(Path(__file__).parent))
    sys.path.insert(0, str(Path(__file__).parents[1] / "gitdiagram"))
    import theme as themes

    themes.apply(GITDIAGRAM, theme)
    film = importlib.import_module(name).FILM
    paths = subprocess.run(
        ["git", "ls-files"], cwd=REPO, capture_output=True, text=True, check=True
    ).stdout.split()
    source = "\n".join((REPO / f).read_text() for f in film.get("code_files", []))
    words = sum(len(text.split()) for _, text in film["beats"])
    body = {
        "owner": "aaravhmodi",
        "repo": film["repo"],
        "description": film["description"],
        "language": "Python",
        "title": film["title"],
        "outro": film["outro"],
        "beats": [{"scene": scene, "narration": text} for scene, text in film["beats"]],
        "scenes": film["scenes"],
        "paths": paths,
        "sourceText": source,
        "wordsPerSecond": film.get("wps", 2.5),
    }
    stored = json.loads(post("/api/local-film", body))
    print(f"{name} ({theme}): {words} words, {len(film['beats'])} beats, {stored['duration']}s")
    for warning in stored["warnings"]:
        print("  warning:", warning)
    OUT.mkdir(exist_ok=True)
    for fmt in formats:
        events = post(
            "/api/video/render",
            {
                "username": "aaravhmodi",
                "repo": film["repo"],
                "format": fmt,
                "v": stored["createdAt"],
            },
        ).decode()
        last = [line for line in events.splitlines() if line.startswith("data:")][-1]
        print(f"  render {fmt}:", last[:200])
        query = urllib.parse.urlencode(
            {
                "username": "aaravhmodi",
                "repo": film["repo"],
                "format": fmt,
                "v": stored["createdAt"],
            }
        )
        url = f"{BASE}/api/video/file?{query}"
        with urllib.request.urlopen(
            urllib.request.Request(url, headers={"Origin": BASE}), timeout=120
        ) as res:
            target = OUT / f"{name}-{theme}-{fmt}.mp4"
            target.write_bytes(res.read())
        print(f"  saved {target} ({target.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
