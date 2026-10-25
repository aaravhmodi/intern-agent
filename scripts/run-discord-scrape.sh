#!/usr/bin/env bash
set -euo pipefail

cd /home/aaravmodi/projects/intern-agent
# Writes leads, so it waits for any other workflow to finish first.
flock -w 21600 /tmp/intern-agent-workflows.lock \
  docker compose exec -T dashboard /app/.venv/bin/internship-agent leads scrape-discord --days 6
