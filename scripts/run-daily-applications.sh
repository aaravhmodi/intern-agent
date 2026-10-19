#!/usr/bin/env bash
set -euo pipefail

# The dated campaign owns October 16. This recurring run starts October 17.
if [[ "$(TZ=America/Toronto date +%F)" < "2026-10-17" ]]; then
  exit 0
fi

args=(--target 20 --lowest-first)
# One-off for October 19: apply to every eligible posting that isn't a strong (green) fit.
if [[ "$(TZ=America/Toronto date +%F)" == "2026-10-19" ]]; then
  args=(--target 1000 --lowest-first --skip-strong)
fi

cd /home/aaravmodi/projects/intern-agent
exec flock -w 3600 /tmp/intern-agent-workflows.lock \
  docker compose exec -T dashboard /app/.venv/bin/internship-agent \
  leads application-campaign "${args[@]}"
