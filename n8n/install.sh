#!/usr/bin/env bash
# Run on the server after the workflow files change: give n8n read-only Gmail access, then
# load the workflows and switch them on.
#   bash ~/projects/intern-agent/n8n/install.sh
# Only these workflows are touched; anything you made in the n8n editor is left alone.
set -euo pipefail
here=$(cd "$(dirname "$0")" && pwd)
cd ~/homelab/n8n

# n8n reads the inbox with the same Gmail app password this app sends with (GMAIL_ADDRESS
# and GMAIL_APP_PASSWORD in ../.env). It goes into a private temporary file in the
# container, n8n imports and encrypts it, and the file is deleted; nothing is printed.
python3 - "$here/../.env" << 'PY' | docker compose exec -T n8n sh -c 'umask 077; cat > /tmp/gmail.json'
import json, sys

env = {}
for line in open(sys.argv[1], encoding="utf-8"):
    key, sep, value = line.strip().partition("=")
    if sep and not key.startswith("#"):
        env[key] = value.strip().strip("\"'")
print(json.dumps([{
    "id": "gmailimapreadonly", "name": "Gmail (read-only)", "type": "imap",
    "data": {"user": env["GMAIL_ADDRESS"], "password": env["GMAIL_APP_PASSWORD"].replace(" ", ""),
             "host": "imap.gmail.com", "port": 993, "secure": True,
             "allowUnauthorizedCerts": False},
}]))
PY
docker compose exec -T n8n sh -c 'n8n import:credentials --input=/tmp/gmail.json; rm -f /tmp/gmail.json'

docker compose exec -T n8n n8n import:workflow --separate --input=/workflows-internship
for file in "$here"/workflows/*.json; do
  id=$(python3 -c 'import json, sys; print(json.load(open(sys.argv[1]))["id"])' "$file")
  docker compose exec -T n8n n8n publish:workflow --id="$id"
done
# n8n starts published workflows when it starts.
docker compose restart n8n
