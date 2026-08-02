#!/usr/bin/env bash
set -euo pipefail

# Usage: ./scripts/set_discord_secret.sh [WEBHOOK_URL]
# Requires: GitHub CLI `gh` authenticated (gh auth login)

if ! command -v gh >/dev/null 2>&1; then
  echo "Error: GitHub CLI 'gh' not found. Install from https://cli.github.com/ and run 'gh auth login'."
  exit 2
fi

WEBHOOK_URL="${1:-}" 
if [ -z "$WEBHOOK_URL" ]; then
  read -r -p "Paste Discord webhook URL: " WEBHOOK_URL
fi
if [ -z "$WEBHOOK_URL" ]; then
  echo "No webhook URL provided. Aborting."
  exit 3
fi

# Determine repo (owner/repo) from git remote if possible
REPO_OVERRIDE="${2:-}"
if [ -n "$REPO_OVERRIDE" ]; then
  REPO="$REPO_OVERRIDE"
else
  ORIGIN_URL=$(git config --get remote.origin.url || true)
  if [ -n "$ORIGIN_URL" ]; then
    # extract owner/repo
    REPO=$(echo "$ORIGIN_URL" | sed -E 's#.*[:/](.+/[^/.]+)(.git)?#\1#')
  else
    echo "Could not determine repo from git remote. Provide repo as second arg (owner/repo)."
    exit 4
  fi
fi

echo "Setting secret DISCORD_WEBHOOK_URL on repository: $REPO"
printf "%s" "$WEBHOOK_URL" | gh secret set DISCORD_WEBHOOK_URL --repo "$REPO"
echo "Secret set successfully."
