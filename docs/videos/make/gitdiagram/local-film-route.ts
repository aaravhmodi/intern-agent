// LOCAL ONLY (not part of GitDiagram): store a hand-written film so the normal
// player and MP4 renderer can show it. The script and shots are written by
// hand instead of by a model, and the narration is a silent track timed at a
// natural reading pace, so the captions carry the words.
import { execFileSync } from "node:child_process";
import { mkdtempSync, readFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

import type { VideoArtifact, VideoTiming } from "~/features/explainer/types";
import { normalizeShots } from "~/server/explainer/shots";
import { writeVideo } from "~/server/explainer/store";
import { normalizeWord } from "~/server/explainer/text";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

type Beat = { scene: string; narration: string; brief?: string };
type Body = {
  owner: string;
  repo: string;
  description: string;
  language: string;
  title: string;
  outro: string;
  beats: Beat[];
  /** One entry per scene: its layout and its shots (beat = global index). */
  scenes: Array<{ layout: unknown; shots: Array<Record<string, unknown>> }>;
  paths?: string[];
  sourceText?: string;
  wordsPerSecond?: number;
};

const LEAD_IN = 0.4;
const TAIL = 3.6;
const round = (n: number) => Math.round(n * 1000) / 1000;

function timeBeats(beats: Beat[], wps: number): VideoTiming {
  let t = LEAD_IN;
  const out: VideoTiming["beats"] = [];
  beats.forEach((beat, index) => {
    if (index > 0 && beats[index - 1]!.scene !== beat.scene) t += 0.7;
    const words = beat.narration.split(/\s+/).filter(Boolean);
    const timed = words.map((raw) => {
      // Longer words take longer to read; punctuation is where a reader breathes.
      const length = 0.55 + Math.min(raw.replace(/\W/g, "").length, 12) / 14;
      const s = t;
      const e = t + length / wps;
      t = e + 0.04;
      if (/[,;:—–]$/.test(raw)) t += 0.22;
      if (/[.!?…]$/.test(raw)) t += 0.42;
      return { w: normalizeWord(raw), s: round(s), e: round(e) };
    });
    out.push({ start: timed[0]?.s ?? t, end: timed.at(-1)?.e ?? t, words: timed });
  });
  const speechEnd = out.at(-1)?.end ?? 0;
  return {
    DURATION: Math.ceil((speechEnd + TAIL) * 10) / 10,
    SPEECH_END: round(speechEnd),
    beats: out,
  };
}

function silence(seconds: number): Buffer {
  const dir = mkdtempSync(join(tmpdir(), "film-"));
  const file = join(dir, "voice.mp3");
  execFileSync("ffmpeg", [
    "-v", "error", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
    "-t", String(seconds), "-q:a", "9", "-y", file,
  ]);
  return readFileSync(file);
}

export async function POST(request: Request): Promise<Response> {
  const host = new URL(request.url).hostname;
  if (host !== "127.0.0.1" && host !== "localhost")
    return Response.json({ error: "local only" }, { status: 403 });
  const body = (await request.json()) as Body;
  const designed = new Map<number, Record<string, unknown>>();
  for (const scene of body.scenes)
    for (const shot of scene.shots)
      designed.set(Number(shot.beat), { ...shot, layout: scene.layout });
  const script = { title: body.title, outro: body.outro, beats: body.beats.map((b) => ({ ...b, brief: b.brief ?? "" })) };
  const { plan, warnings } = normalizeShots(script, designed, {
    name: body.repo,
    paths: body.paths ?? [],
    sourceText: body.sourceText ?? "",
  });
  const timing = timeBeats(body.beats, body.wordsPerSecond ?? 2.5);
  const artifact: VideoArtifact = {
    version: 2,
    repository: `${body.owner}/${body.repo}`.toLowerCase(),
    createdAt: new Date().toISOString(),
    meta: {
      owner: body.owner,
      repo: body.repo,
      url: `https://github.com/${body.owner}/${body.repo}`,
      description: body.description,
      stars: 0,
      language: body.language,
    },
    plan,
    timing,
    voices: [{ start: LEAD_IN }],
    stats: {
      totalMs: 0, readMs: 0, planMs: 0, voiceMs: 0, planner: "api",
      model: "hand-written", plannerCostUsd: 0, inputTokens: 0, outputTokens: 0,
      ttsCharacters: 0, voiceCostUsd: 0, voice: "none", warnings,
    },
  };
  await writeVideo(artifact, [silence(timing.DURATION)]);
  return Response.json({ createdAt: artifact.createdAt, duration: timing.DURATION, warnings });
}
