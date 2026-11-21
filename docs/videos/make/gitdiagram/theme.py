"""Recolour GitDiagram's video engine in a local checkout, one theme at a time.

    python theme.py <gitdiagram-dir> lavender|clay|clay-dark|ocean

Every theme starts from the engine as committed plus engine-branding.patch, then swaps each
colour of GitDiagram's palette for its role in the theme, in the stylesheet and in the scene
code alike, so every element changes together. "lavender" is GitDiagram's own palette.
"""

import re
import subprocess
import sys
from pathlib import Path

PATCH = Path(__file__).with_name("engine-branding.patch")
FILES = ["engine.css", "kit.js", "shots.js", "stage.js", "camera.js", "reflow.js"]

# GitDiagram's palette, by role.
ROLES = {
    "paper": "#f2e8ff",
    "paper_2": "#e6d5ff",
    "card": "#fdfaff",
    "ink": "#17111f",
    "ink_2": "#4e4463",
    "ink_3": "#3a2f4a",
    "muted": "#b9a8d6",
    "accent": "#bd85fb",
    "accent_soft": "#dcc2ff",
    "accent_deep": "#7a2be0",
    "brand": "#9333ea",
    "green": "#0f7a48",
    "green_soft": "#cff2de",
    "red": "#b3263a",
    "red_soft": "#ffd9da",
    "code_string": "#7a4a14",
    "code_name": "#0d6e7a",
}

THEMES: dict[str, dict[str, str]] = {
    "lavender": {},
    # Warm ivory and terracotta, in the spirit of Claude's own look.
    "clay": {
        "paper": "#f0eee6",
        "paper_2": "#e6e1d3",
        "card": "#faf9f5",
        "ink": "#141413",
        "ink_2": "#5e5d59",
        "ink_3": "#3d3d3a",
        "muted": "#b7ad9f",
        "accent": "#d97757",
        "accent_soft": "#f1d6c9",
        "accent_deep": "#b8532f",
        "brand": "#c96442",
        "green": "#4a7c59",
        "green_soft": "#dceadf",
        "red": "#a8322b",
        "red_soft": "#f6d8d2",
    },
    # The same, after dark: charcoal, ivory text, a brighter clay.
    "clay-dark": {
        "paper": "#1f1e1d",
        "paper_2": "#2a2927",
        "card": "#30302e",
        "ink": "#f5f4ef",
        "ink_2": "#d3cec3",
        "ink_3": "#dedad0",
        "muted": "#6f6a62",
        "accent": "#d97757",
        "accent_soft": "#5a3a2e",
        "accent_deep": "#e8906f",
        "brand": "#e8906f",
        "green": "#7cc79a",
        "green_soft": "#22392c",
        "red": "#ef8a80",
        "red_soft": "#4a2724",
        "code_string": "#e6b98c",
        "code_name": "#86cbd2",
        "glow": "#30302e",
    },
    # Cool and clean: pale sky, ink navy, a strong blue.
    "ocean": {
        "paper": "#e8f1f8",
        "paper_2": "#d6e6f3",
        "card": "#fbfdff",
        "ink": "#0e1a2b",
        "ink_2": "#45566e",
        "ink_3": "#2b3a50",
        "muted": "#9fb3c8",
        "accent": "#4c8ef7",
        "accent_soft": "#c9dcfb",
        "accent_deep": "#1f5fd1",
        "brand": "#1f5fd1",
        "green": "#0f7a5a",
        "green_soft": "#cdeee2",
        "red": "#b3263a",
        "red_soft": "#ffd9da",
    },
}


def rgb(hex_colour: str) -> tuple[int, int, int]:
    h = hex_colour.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


# Colours GitDiagram writes as rgba() of a palette colour, mapped to their roles.
RGBA_ROLES = {
    (23, 17, 31): "ink",
    (242, 232, 255): "paper",
    (189, 133, 251): "accent",
    (78, 68, 99): "ink_2",
    (220, 194, 255): "accent_soft",
    (207, 242, 222): "green_soft",
    (255, 217, 218): "red_soft",
    (122, 43, 224): "accent_deep",
    (255, 255, 255): "glow",
}


def recolour(text: str, theme: dict[str, str]) -> str:
    for role, source in ROLES.items():
        if role in theme:
            text = re.sub(re.escape(source), theme[role], text, flags=re.IGNORECASE)
    for triple, role in RGBA_ROLES.items():
        if role in theme:
            r, g, b = rgb(theme[role])
            pattern = r"rgba\(\s*" + r",\s*".join(str(c) for c in triple) + r"\s*,"
            text = re.sub(pattern, f"rgba({r}, {g}, {b},", text)
    return text


def apply(checkout: Path, name: str) -> None:
    engine = checkout / "public" / "video-engine"
    subprocess.run(["git", "checkout", "--", "public/video-engine"], cwd=checkout, check=True)
    subprocess.run(["git", "apply", str(PATCH.resolve())], cwd=checkout, check=True)
    theme = THEMES[name]
    for file in FILES:
        path = engine / file
        path.write_text(recolour(path.read_text(), theme))


if __name__ == "__main__":
    apply(Path(sys.argv[1]), sys.argv[2])
    print("theme:", sys.argv[2])
