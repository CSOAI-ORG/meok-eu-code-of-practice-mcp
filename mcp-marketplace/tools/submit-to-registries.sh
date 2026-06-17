#!/usr/bin/env bash
# submit-to-registries.sh
# Auto-generates PR-ready submission payloads for the major MCP registries from
# the live haulage.app/catalogue.json. Read REGISTRY_SUBMISSION_AUDIT_2026-06-07.md
# for context.
#
# Usage:
#   ./submit-to-registries.sh                 # write all four registry files into out/
#   ./submit-to-registries.sh --check         # just probe whether each MCP is already
#                                              # listed (no writes)
#
# Output:
#   out/wong2-awesome-mcp-PR.md       paste body for the awesome-mcp-servers PR
#   out/mcp-so-submissions.json       JSON array — feed to mcp.so submission form
#   out/modelcontextprotocol-registry-PRs/<slug>.yaml   one YAML per MCP for the
#                                                       modelcontextprotocol/registry PR
#   out/smithery-submissions.csv      CSV — feed Smithery batch importer
#   out/cline-marketplace-PR.md       Cline marketplace PR body
#   out/audit-already-listed.txt      what was already indexed (skipped)

set -euo pipefail

CATALOGUE_URL="${CATALOGUE_URL:-https://haulage.app/catalogue.json}"
OUT_DIR="${OUT_DIR:-out}"
PUBLISHER="MEOK AI Labs / CSOAI LTD"
GH_ORG="CSOAI-ORG"

CHECK_ONLY=0
if [ "${1:-}" = "--check" ]; then
  CHECK_ONLY=1
fi

command -v jq >/dev/null || { echo "ERROR: jq required (brew install jq)"; exit 2; }
command -v curl >/dev/null || { echo "ERROR: curl required"; exit 2; }

mkdir -p "$OUT_DIR" "$OUT_DIR/modelcontextprotocol-registry-PRs"

echo "[1/3] Fetching catalogue from $CATALOGUE_URL"
CATALOGUE_JSON="$(curl -fsSL "$CATALOGUE_URL")" || { echo "ERROR: failed to fetch catalogue"; exit 3; }

TOTAL=$(echo "$CATALOGUE_JSON" | jq '.mcps | length')
PUBLISHED=$(echo "$CATALOGUE_JSON" | jq '[.mcps[] | select(.published == true)] | length')
echo "  -> $TOTAL MCPs total, $PUBLISHED published"

# ---- audit-already-listed.txt --------------------------------------------
echo "[2/3] Auditing existing registry listings (HEAD requests)"
> "$OUT_DIR/audit-already-listed.txt"
echo "$CATALOGUE_JSON" | jq -r '.mcps[] | select(.published == true) | .name' | while read -r slug; do
  for reg in "mcp.so" "smithery.ai" "pulsemcp.com"; do
    code=$(curl -s -o /dev/null -w "%{http_code}" -L "https://${reg}/server/${slug}" 2>/dev/null || echo "000")
    if [ "$code" = "200" ]; then
      echo "ALREADY-INDEXED  ${slug}  on  ${reg}" >> "$OUT_DIR/audit-already-listed.txt"
    fi
  done
done
echo "  -> wrote $OUT_DIR/audit-already-listed.txt"

if [ "$CHECK_ONLY" = 1 ]; then
  cat "$OUT_DIR/audit-already-listed.txt"
  exit 0
fi

# ---- wong2-awesome-mcp-PR.md ---------------------------------------------
echo "[3/3] Building registry submission payloads"
{
  echo "# Add MEOK AI Labs trade-compliance MCP catalogue (32 servers)"
  echo
  echo "Adds the MEOK AI Labs trade-compliance MCP catalogue — currently $PUBLISHED published servers (of $TOTAL planned) across 9 trade verticals (UK road, EU rail, US logistics, air, sea, marine pollution, urban infrastructure, AI governance, lifting + materials handling)."
  echo
  echo "All MCPs are MIT-licensed, signed-by-default (HMAC-SHA256 attestation chain), and bridge to EU AI Act + UK AI Bill governance via meok-haulage-governance-bridge-mcp."
  echo
  echo "## Servers being added"
  echo
  echo "### Trade compliance"
  echo
  echo "$CATALOGUE_JSON" | jq -r '
    .mcps[]
    | select(.published == true)
    | "- **[\(.name)](https://pypi.org/project/\(.name))** — \(.tagline)"
  '
  echo
  echo "## Why this catalogue"
  echo
  echo "- Niche-specific: UK + EU trade regulation that horizontal MCPs do not cover (DVSA OCRS, Smart Tachograph 2, EU AI Act Annex III, BS 7121, LOLER, FORS, IATA DGR, MARPOL, NRSWA, NIS2 transport sector)."
  echo "- Signed attestations: every tool result is HMAC-SHA256 signed + verifiable publicly at meok-attestation-api.vercel.app/verify"
  echo "- Cross-platform: MCP Apps spec (SEP-1865) UI Resources rolling out so output renders in Claude / ChatGPT / VS Code Copilot / Goose."
  echo
  echo "Source for all servers: https://github.com/$GH_ORG"
  echo "Publisher: $PUBLISHER (Companies House 16939677)"
} > "$OUT_DIR/wong2-awesome-mcp-PR.md"
echo "  -> wrote $OUT_DIR/wong2-awesome-mcp-PR.md"

# ---- mcp-so-submissions.json ---------------------------------------------
echo "$CATALOGUE_JSON" | jq --arg pub "$PUBLISHER" --arg gh "$GH_ORG" '
  [.mcps[] | select(.published == true) | {
    name,
    description: .tagline,
    install: (.install // ("pip install " + .name)),
    repository: ("https://github.com/" + $gh),
    pypi: ("https://pypi.org/project/" + .name),
    license: "MIT",
    publisher: $pub,
    tags: (.tags // ["trade","compliance","mcp","attestation"])
  }]
' > "$OUT_DIR/mcp-so-submissions.json"
echo "  -> wrote $OUT_DIR/mcp-so-submissions.json"

# ---- modelcontextprotocol-registry-PRs/*.yaml ----------------------------
echo "$CATALOGUE_JSON" | jq -r '.mcps[] | select(.published == true) | .name' | while read -r slug; do
  tagline=$(echo "$CATALOGUE_JSON" | jq -r --arg n "$slug" '.mcps[] | select(.name == $n) | .tagline')
  install=$(echo "$CATALOGUE_JSON" | jq -r --arg n "$slug" '.mcps[] | select(.name == $n) | (.install // ("pip install " + .name))')
  cat > "$OUT_DIR/modelcontextprotocol-registry-PRs/${slug}.yaml" <<YAML
name: ${slug}
display_name: ${slug}
description: |
  ${tagline}
publisher: ${PUBLISHER}
homepage: https://haulage.app/mcps
repository: https://github.com/${GH_ORG}
license: MIT
install:
  command: ${install}
runtime: python
signed_attestations: true
signed_attestations_verifier: https://meok-attestation-api.vercel.app/verify
tags:
  - trade
  - compliance
  - haulage
  - attestation
  - eu-ai-act
  - uk-ai-bill
YAML
done
echo "  -> wrote $OUT_DIR/modelcontextprotocol-registry-PRs/ ($(ls $OUT_DIR/modelcontextprotocol-registry-PRs | wc -l | tr -d ' ') files)"

# ---- smithery-submissions.csv --------------------------------------------
{
  echo "name,description,install,repository,license,publisher"
  echo "$CATALOGUE_JSON" | jq -r --arg pub "$PUBLISHER" --arg gh "$GH_ORG" '
    .mcps[] | select(.published == true) |
    [.name, .tagline, (.install // ("pip install " + .name)), ("https://github.com/" + $gh), "MIT", $pub]
    | @csv
  '
} > "$OUT_DIR/smithery-submissions.csv"
echo "  -> wrote $OUT_DIR/smithery-submissions.csv"

# ---- cline-marketplace-PR.md ---------------------------------------------
{
  echo "# Add MEOK AI Labs trade-compliance MCPs to Cline marketplace"
  echo
  echo "$PUBLISHED published MCPs from the MEOK trade-compliance catalogue. All MIT-licensed, signed-by-default."
  echo
  echo "$CATALOGUE_JSON" | jq -r '
    .mcps[]
    | select(.published == true)
    | "## " + .name + "\n\n" + .tagline + "\n\nInstall: `" + ((.install) // ("pip install " + .name)) + "`\n\nRepo: https://github.com/CSOAI-ORG\n"
  '
} > "$OUT_DIR/cline-marketplace-PR.md"
echo "  -> wrote $OUT_DIR/cline-marketplace-PR.md"

echo
echo "Done. Next:"
echo "  1. Open PR with wong2-awesome-mcp-PR.md at https://github.com/wong2/awesome-mcp-servers"
echo "  2. Paste mcp-so-submissions.json items at https://mcp.so/submit"
echo "  3. Commit modelcontextprotocol-registry-PRs/*.yaml to a fork of modelcontextprotocol/registry"
echo "  4. Bulk-import smithery-submissions.csv at https://smithery.ai/"
echo "  5. Open PR with cline-marketplace-PR.md at https://github.com/cline/mcp-marketplace"
echo
echo "Already-indexed audit at $OUT_DIR/audit-already-listed.txt"
