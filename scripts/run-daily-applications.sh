#!/usr/bin/env bash
set -euo pipefail

# Every night at 2 AM: attempt every eligible open posting, lowest fit first.
# The target is just a ceiling above the number of open postings.
cd /home/aaravmodi/projects/intern-agent
exec flock -w 3600 /tmp/intern-agent-workflows.lock \
  docker compose exec -T dashboard /app/.venv/bin/internship-agent \
  leads application-campaign --target 1000 --lowest-first
