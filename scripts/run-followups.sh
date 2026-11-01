#!/usr/bin/env bash
# Send the follow-ups that are due, at most FOLLOWUP_DAILY_LIMIT a run; the rest stay queued
# for the next run. Only with FOLLOWUPS_ENABLED=true, never after a reply or bounce.
set -euo pipefail
cd /home/aaravmodi/projects/intern-agent
flock -w 21600 /tmp/intern-agent-workflows.lock \
  docker compose exec -T dashboard /app/.venv/bin/internship-agent leads followups --send
