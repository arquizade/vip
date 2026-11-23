#!/usr/bin/env bash
# Create a project folder from the template and a matching workspace card.
# Usage: scripts/new-project.sh <kebab-case-name>
set -euo pipefail

slug="${1:-}"
if [[ ! "$slug" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "Usage: scripts/new-project.sh <kebab-case-name>" >&2
  echo "Example: scripts/new-project.sh webhook-service" >&2
  exit 1
fi

root="$(cd "$(dirname "$0")/.." && pwd)"
template_dir="$root/vault/main/01-projects/_template"
dest="$root/vault/main/01-projects/$slug"
card="$root/workspace/projects/$slug-card.md"
today="$(date +%F)"
name="$(echo "$slug" | tr '-' ' ' | awk '{for(i=1;i<=NF;i++)$i=toupper(substr($i,1,1)) substr($i,2)}1')"

if [[ -e "$dest" || -e "$card" ]]; then
  echo "Already exists: $dest or $card" >&2
  exit 1
fi

cp -r "$template_dir" "$dest"
rm -f "$dest/.gitkeep"

# Fill the placeholders that the script can know
find "$dest" -type f -name '*.md' -exec sed -i.bak \
  -e "s|{{PROJECT_SLUG}}|$slug|g" \
  -e "s|{{PROJECT_NAME}}|$name|g" \
  -e "s|{{YYYY-MM-DD}}|$today|g" {} +
find "$dest" -name '*.bak' -delete

sed -e "s|{{PROJECT_SLUG}}|$slug|g" \
    -e "s|{{PROJECT_NAME}}|$name|g" \
    -e "s|{{YYYY-MM-DD}}|$today|g" \
    "$root/workspace/_templates/project-card-template.md" > "$card"

echo "Created:"
echo "  $dest"
echo "  $card"
echo "Next: fill the {{...}} placeholders in the README and the card."
