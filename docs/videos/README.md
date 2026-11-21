# Demo videos

| Video | Length | What it shows |
|---|---|---|
| [intern-agent, explained](intern-agent-explained.mp4) | 1:31 | What the agent does end to end: finds startups, scores them, emails 200+ people a day on its own, follows up, applies, tracks replies, and stops the moment someone answers |
| [The job pipeline](job-pipeline-explained.mp4) | 1:31 | One email followed from the Toronto batch to an interview: address guessing, read-only inbox scans, the two follow-ups, matching and classifying the reply, the board and the funnels |
| [One day, 200+ emails](one-day-vertical.mp4) | 0:49 | Vertical (9:16) cut of a day on the server, from the 2 AM applications to the 9:30 PM scrape |
| [Dashboard walkthrough](dashboard-walkthrough.mp4) | 1:08 | The real dashboard with made-up demo data: home, job pipeline, a card's inbox timeline, all leads, a lead's fit and draft, Today and the calendar |

The three explainers are drawn by the motion engine of
[GitDiagram](https://github.com/ahmedkhaleel2004/gitdiagram) (MIT), the same one behind its
one-minute repository videos. The scripts and shots in `make/films/` were written by hand
against GitDiagram's own director and designer rules (twenty-odd beats, one subject per scene,
the product before the internals, verbatim code only under the hood), and the films carry
captions instead of a voice. On-screen code is copied from this repository. The funnel
numbers in "The job pipeline" are labelled sample data.

The walkthrough is a Playwright recording of the dashboard running on the data from
`make/seed_demo.py`: every company, person and address in it is invented (addresses use the
reserved `.example` domain).

## Making them again

The films (needs a local GitDiagram checkout, Node 22, Bun, ffmpeg and Chromium):

```bash
git clone https://github.com/ahmedkhaleel2004/gitdiagram && cd gitdiagram
git apply ../intern-agent/docs/videos/make/gitdiagram/engine-branding.patch   # github.com address, no GitDiagram logo
mkdir -p src/app/api/local-film
cp ../intern-agent/docs/videos/make/gitdiagram/local-film-route.ts src/app/api/local-film/route.ts
bun install && bun run build:mcp-app
# .env: VIDEO_EXPLAINER_ENABLED=1, NEXT_PUBLIC_VIDEO_EXPLAINER=1, VIDEO_STORE=local,
# VIDEO_RENDER_CHROME_PATH=<chromium>, plus Upstash/R2 values (any Redis behind an
# Upstash-style REST shim works; R2 values are unused with VIDEO_STORE=local)
node node_modules/next/dist/bin/next dev -p 3000

cd ../intern-agent/docs/videos/make/films
python make.py film_explainer landscape vertical     # -> out/film_explainer-*.mp4
```

No API keys are used: `local-film-route.ts` lays out the hand-written shots with GitDiagram's
own `normalizeShots`, times the captions at a natural reading pace over a silent track, and
stores the film so the normal MP4 renderer can draw it.

The walkthrough:

```bash
uv run python docs/videos/make/seed_demo.py /tmp/demo-data
DATA_DIR=/tmp/demo-data uv run internship-agent dashboard &
node docs/videos/make/record.js /tmp/demo-rec
python docs/videos/make/finish.py /tmp/demo-rec docs/videos/dashboard-walkthrough.mp4
```
