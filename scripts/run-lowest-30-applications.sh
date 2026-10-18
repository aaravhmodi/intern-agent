#!/usr/bin/env bash
set -euo pipefail

# One-off: apply to the 30 lowest-scored eligible postings; result goes to ntfy.
cd /home/aaravmodi/projects/intern-agent
exec flock -w 3600 /tmp/intern-agent-workflows.lock \
  docker compose exec -T dashboard /app/.venv/bin/internship-agent \
  leads application-campaign --target 30 --lowest-first
