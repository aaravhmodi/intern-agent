#!/usr/bin/env bash
# One outreach batch: email people never emailed (best-guess address format, sent from the
# outreach Gmail), topping up from startups' published shared inboxes when there are fewer
# founders left than the batch size.
#   run-email-batch.sh toronto|europe|new-york|sf   20 emails from that area, topped up
#                                                    from everywhere else when it runs out
#   run-email-batch.sh others                        20 emails spread across Europe, Canada, USA
set -euo pipefail

area=${1:?usage: run-email-batch.sh toronto|europe|new-york|sf|others}
batch=20
cd /home/aaravmodi/projects/intern-agent
run() {
  flock -w 21600 /tmp/intern-agent-workflows.lock \
    docker compose exec -T dashboard /app/.venv/bin/internship-agent leads "$@"
}

# Print with >&2, never by tee-ing to stderr's device path: under systemd stderr is the
# journal's socket, which can't be opened by path, so tee fails and pipefail ends the
# batch before the top-up below.
# --retries and --per-company 3: new founders alone no longer fill a batch of 20.
out=$(run guess-send --area "$area" --limit "$batch" --retries --per-company 3 --send)
printf '%s\n' "$out" >&2
sent=$(grep -oE '^[0-9]+ founder' <<<"$out" | tail -1 | grep -oE '^[0-9]+' || echo 0)
left=$((batch - sent))
if [ "$left" -gt 0 ]; then
  out=$(run inbox-send --area "$area" --limit "$left" --send)
  printf '%s\n' "$out" >&2
  sent=$(grep -oE '^[0-9]+ inbox' <<<"$out" | tail -1 | grep -oE '^[0-9]+' || echo 0)
  left=$((left - sent))
fi
# A city that has run out of people tops up from everywhere else, so the batch is still 20.
if [ "$left" -gt 0 ] && [ "$area" != others ]; then
  run guess-send --area others --limit "$left" --retries --per-company 3 --send
fi
