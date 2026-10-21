#!/usr/bin/env bash
# One outreach batch, five a day: email up to 20 people never emailed (best-guess address
# format, sent from the outreach Gmail), topping up from startups' published shared inboxes
# when there are fewer than 20 founders left to try.
set -euo pipefail

batch=20
cd /home/aaravmodi/projects/intern-agent
run() {
  flock -w 3600 /tmp/intern-agent-workflows.lock \
    docker compose exec -T dashboard /app/.venv/bin/internship-agent leads "$@"
}

out=$(run guess-send --limit "$batch" --send | tee /dev/stderr)
sent=$(grep -oE '^[0-9]+ founder' <<<"$out" | tail -1 | grep -oE '^[0-9]+' || echo 0)
left=$((batch - sent))
if [ "$left" -gt 0 ]; then
  run inbox-send --limit "$left" --send
fi
