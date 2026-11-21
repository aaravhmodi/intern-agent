"""Turn the raw walkthrough into the final MP4: title card, captions, end card.

python finish.py <recdir> <out.mp4>
"""

import json
import subprocess
import sys
from pathlib import Path

REC, OUT = Path(sys.argv[1]), Path(sys.argv[2])
W, H = 1280, 800

CARD = """<!doctype html><html><head><style>
body{{margin:0;width:{w}px;height:{h}px;background:#0b0d12;color:#f4f4f6;
  display:flex;flex-direction:column;justify-content:center;padding:0 120px;
  box-sizing:border-box;font-family:Georgia,'Times New Roman',serif}}
.k{{font:600 18px/1 sans-serif;letter-spacing:.22em;color:#c9a227;margin-bottom:28px}}
.t{{font-size:84px;line-height:1.05;letter-spacing:-.02em}}
.s{{font:400 26px/1.5 sans-serif;color:#9aa0ae;margin-top:26px;max-width:980px}}
.u{{font:500 20px/1 monospace;color:#a5b4fc;margin-top:48px}}
</style></head><body>
<div class="k">{kicker}</div><div class="t">{title}</div><div class="s">{sub}</div>
<div class="u">github.com/aaravhmodi/intern-agent</div>
</body></html>"""


def card(name: str, kicker: str, title: str, sub: str) -> Path:
    html = REC / f"{name}.html"
    png = REC / f"{name}.png"
    html.write_text(CARD.format(w=W, h=H, kicker=kicker, title=title, sub=sub))
    script = (
        "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
        f"const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});"
        f"await p.goto('file://{html}');await p.screenshot({{path:'{png}'}});await b.close();}})();"
    )
    subprocess.run(["node", "-e", script], check=True)
    return png


def ass_time(t: float) -> str:
    h, rem = divmod(max(t, 0), 3600)
    m, s = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def subtitles(lead: float) -> Path:
    caps = json.loads((REC / "captions.json").read_text())
    lines = [
        "[Script Info]",
        "ScriptType: v4.00+",
        f"PlayResX: {W}",
        f"PlayResY: {H}",
        "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour,"
        " BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle,"
        " BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
        # BorderStyle 3: an opaque box behind the text, like a modern caption pill.
        "Style: Cap,DejaVu Sans,30,&H00FFFFFF,&H00FFFFFF,&H28140F0B,&H28140F0B,"
        "1,0,0,0,100,100,0,0,3,14,0,2,160,160,46,1",
        "",
        "[Events]",
        "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
    ]
    for c in caps:
        start, end = ass_time(c["start"] + lead), ass_time(c["end"] + lead - 0.05)
        lines.append(f"Dialogue: 0,{start},{end},Cap,,0,0,0,,{{\\fad(180,120)}}{c['text']}")
    path = REC / "captions.ass"
    path.write_text("\n".join(lines) + "\n")
    return path


intro = card(
    "intro",
    "WINTER 2027 · DEMO",
    "intern-agent",
    "Finds internships, emails the people behind them, follows up, and tracks every reply.",
)
outro = card(
    "outro",
    "MADE UP DATA · REAL DASHBOARD",
    "200+ emails a day.<br>Replies are yours.",
    "Sends and follows up on its own. From the first reply on, it's all you.",
)
INTRO, OUTRO = 3.0, 3.5
ass = subtitles(0)
subprocess.run(
    [
        "ffmpeg",
        "-v",
        "error",
        "-y",
        "-loop",
        "1",
        "-t",
        str(INTRO),
        "-i",
        str(intro),
        "-i",
        str(REC / "walkthrough-raw.webm"),
        "-loop",
        "1",
        "-t",
        str(OUTRO),
        "-i",
        str(outro),
        "-f",
        "lavfi",
        "-t",
        "1",
        "-i",
        "anullsrc=r=48000:cl=stereo",
        "-filter_complex",
        f"[0:v]fps=30,format=yuv420p,fade=t=out:st={INTRO - 0.4}:d=0.4[a];"
        f"[1:v]fps=30,format=yuv420p,subtitles={ass}[b];"
        f"[2:v]fps=30,format=yuv420p,fade=t=in:st=0:d=0.4[c];"
        "[a][b][c]concat=n=3:v=1:a=0,scale=1280:-2:flags=lanczos[v]",
        "-map",
        "[v]",
        "-c:v",
        "libx264",
        "-preset",
        "slow",
        "-crf",
        "24",
        "-pix_fmt",
        "yuv420p",
        "-movflags",
        "+faststart",
        str(OUT),
    ],
    check=True,
)
print("wrote", OUT, OUT.stat().st_size // 1024, "KB")
