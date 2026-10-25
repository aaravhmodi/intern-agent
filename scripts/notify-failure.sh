#!/usr/bin/env bash
# Push a phone alert when a scheduled unit fails. Run by internship-failure@.service, which
# every unit names in OnFailure=. Talks to ntfy directly so it works with the dashboard down.
set -uo pipefail

unit=${1:?usage: notify-failure.sh UNIT}
cd /home/aaravmodi/projects/intern-agent
topic=$(grep -E '^NTFY_TOPIC=' .env | tail -1 | cut -d= -f2- | tr -d "\"'")
server=$(grep -E '^NTFY_SERVER=' .env | tail -1 | cut -d= -f2- | tr -d "\"'")
[ -n "$topic" ] || exit 0

tail=$(journalctl --user -u "$unit" -n 4 --no-pager -o cat 2>/dev/null)
curl -fsS -m 15 \
  -H "Title: Failed: ${unit%.service}" -H "Priority: 4" -H "Tags: warning" \
  -d "${tail:-No log lines.}" "${server:-https://ntfy.sh}/$topic" >/dev/null
