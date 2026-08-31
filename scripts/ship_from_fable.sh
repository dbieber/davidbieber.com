#!/bin/bash
# ship_from_fable.sh — deploy davidbieber.com from the fable-personal box.
#
# Does exactly the documented ship (David's Jul 11 grant: "ssh + deploy + other
# ops"): pull the GitHub-Actions-built `deploy` branch on the www box and mirror
# the built site into the served dir (Tornado serves default/ live, no restart).
# Since Aug 31 2026 default/ is a pure mirror of hugo/public: everything served
# (legacy games/, cv, robots.txt, the React apps, the manifest) is produced by
# the Hugo build from hugo/static, so stale build output gets pruned on ship.
# The www box (Debian 10) has no rsync, so the mirror is cp + prune; with rsync
# it would be a single `rsync -a --delete hugo/public/ default/`.
# Scoped narrowly so it can carry a Claude Code allow-rule:
#   Bash(/root/code/github/dbieber/davidbieber.com/scripts/ship_from_fable.sh:*)
set -euo pipefail

HOST="david810@35.184.59.12"
KEY="/root/.ssh/id_ed25519"

echo "== shipping deploy branch to davidbieber.com =="
ssh -i "$KEY" -o StrictHostKeyChecking=no -o ConnectTimeout=15 "$HOST" 'bash -s' <<'REMOTE'
set -euo pipefail
cd /home/dbieber/davidbieber.com
sudo git pull origin deploy
# Mirror hugo/public -> default/: copy the build, then prune files the build
# does not produce (and the directories that empties).
sudo cp -r hugo/public/. default/
deleted=0
while IFS= read -r -d '' f; do
  if [ ! -e "hugo/public/$f" ]; then
    sudo rm -f -- "default/$f"
    deleted=$((deleted + 1))
  fi
done < <(cd default && find . -type f -print0)
sudo find default -mindepth 1 -type d -empty -delete
echo "synced: $(find hugo/public -type f | wc -l) build files, $deleted stale files deleted"
echo "shipped: $(sudo git log --format=%h -1)"
REMOTE

echo "== verifying live =="
curl -sS -m 15 https://davidbieber.com/now/ | grep -oE "Last updated on [0-9-]+" | head -1
