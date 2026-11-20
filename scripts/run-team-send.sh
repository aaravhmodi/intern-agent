#!/usr/bin/env bash
# Daily: email a few drafted big tech people a coffee-chat note about their team, one company
# at a time (10 a day at most, from the outreach Gmail, each person once).
set -euo pipefail

cd /home/aaravmodi/projects/intern-agent
flock -w 21600 /tmp/intern-agent-workflows.lock \
  docker compose exec -T dashboard /app/.venv/bin/internship-agent leads team-send --limit 10 --send
