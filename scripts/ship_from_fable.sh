#!/bin/bash
# ship_from_fable.sh — deploy davidbieber.com from the fable-personal box.
#
# Does exactly the documented ship (David's Jul 11 grant: "ssh + deploy + other
# ops"): pull the GitHub-Actions-built `deploy` branch on the www box and copy
# the built site into the served dir (Tornado serves default/ live, no restart).
# Scoped narrowly so it can carry a Claude Code allow-rule:
#   Bash(/root/code/github/dbieber/davidbieber.com/scripts/ship_from_fable.sh:*)
set -euo pipefail

HOST="david810@35.184.59.12"
KEY="/root/.ssh/id_ed25519"

echo "== shipping deploy branch to davidbieber.com =="
ssh -i "$KEY" -o StrictHostKeyChecking=no -o ConnectTimeout=15 "$HOST" \
  'cd /home/dbieber/davidbieber.com && sudo git pull origin deploy && sudo cp -r hugo/public/* default/ && echo "shipped: $(git log --format=%h -1 origin/deploy 2>/dev/null || git log --format=%h -1)"'

echo "== verifying live =="
curl -sS -m 15 https://davidbieber.com/now/ | grep -oE "Last updated on [0-9-]+" | head -1
