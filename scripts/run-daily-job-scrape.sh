#!/usr/bin/env bash
set -euo pipefail

cd /home/aaravmodi/projects/intern-agent
exec flock -w 3600 /tmp/intern-agent-workflows.lock \
  docker compose exec -T dashboard /app/.venv/bin/internship-agent leads scrape-jobs
