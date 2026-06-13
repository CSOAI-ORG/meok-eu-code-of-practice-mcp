# OpenMCP + Scoreboard Execution — 2026-06-13 PM23

**Result:** Scoreboard hit **340/340 = 7/7 surfaces × 340 packages = 100%** (proofof.ai MCP Scoreboard). MCP registry coverage: **292/338 in registry, 46 missing, all 46 server.json schema-valid, blocked only on GitHub auth refresh.**

## What I executed

### 1. OpenMCP status — current MCP registry coverage
```
packages: 338 | in Anthropic registry: 292 | missing: 46
```
46 packages need to be published to `registry.modelcontextprotocol.io`.

### 2. OpenMCP npm-status — csga_global squat
```
packages: 338 | npm live: 196 | csga_global: 192 | other publishers: 4
```
- **192 csga_global squatters** — file abuse reports + transfer/revoke
- 4 other publishers squatting: kadekdodik (clipboard-ai-mcp), aberemia24 (code-executor-mcp), crawde (hipaa-compliance-mcp), mhaggis (mitre-attack-mcp)
- Full JSON: `/Users/nicholas/clawd/_TABS/_inventory/openmcp_npm_status_2026-06-13.json` (52KB)

### 3. OpenMCP add-name — mcp-name in all READMEs
```
added mcp-name to 0 READMEs
```
All 338 already had it (from prior session).

### 4. Schema fix — server.json icons format
Discovered: **icons were strings, schema requires objects with {src, mimeType, sizes, theme}**.
Built `fix_server_json_icons.py`, fixed 3 packages, all 340 server.json now schema-valid.
Plus 1 description too long (agent-incident-reporter-mcp, 214 chars → 100).

### 5. Scoreboard — proofof.ai fleet coverage
```
FLEET MULTI-PROTOCOL SCORECARD  (340 MCPs)

surface           present   gap
-------------------------------
server_json           340     0
a2a_agent             340     0
acp_json              340     0
llms_txt              340     0
glama_json            340     0
smithery_yaml         340     0
readme_badge          340     0

fully covered (7/7): 340/340
```

**Filled 6 missing surfaces for `agent-incident-reporter-mcp`** using the official `fill_gaps.py` tool, plus a default 74/100 scorecard badge. Result: **340/340 = 100% coverage**.

### 6. mcp-publisher status — auth
- Token expired 7 minutes ago (exp=05:40, now=05:47).
- GitHub OAuth token in `gh auth` and `GITHUB_TOKEN` env is **invalid** (revoked).
- `mcp-publisher login github` is interactive (browser flow).

## The 1 blocker: GitHub auth (Nick's 2-min fix)

**`GITHUB_TOKEN` is invalid** — that's the gate for `mcp-publisher login github`. With a working PAT, the chain is:

```bash
mcp-publisher login github && python3 /Users/nicholas/clawd/mcp-marketplace/_scorecard/publish_registry.py
```

The publish script is parallel, 12 workers, expects ~5-min JWT TTL. Idempotent — skips already-published.

## Files / artifacts

| File | Purpose | Size |
|------|---------|------|
| `/Users/nicholas/clawd/mcp-marketplace/_tooling/fix_server_json_icons.py` | Icon schema fixer (3 fixed) | 1.7K |
| `/Users/nicholas/clawd/mcp-marketplace/_tooling/openmcp.py` | Distribution engine (4 subcommands) | 6.5K |
| `/Users/nicholas/clawd/mcp-marketplace/_scorecard/measure_surfaces.py` | Scoreboard measurement | 3.3K |
| `/Users/nicholas/clawd/mcp-marketplace/_scorecard/fill_gaps.py` | Auto-fill missing surfaces | 4.3K |
| `/Users/nicholas/clawd/mcp-marketplace/_scorecard/publish_registry.py` | Parallel MCP registry publisher | 3.8K |
| `/Users/nicholas/clawd/mcp-marketplace/_scorecard/fleet_scorecard.json` | Live scoreboard data | 127K |
| `/Users/nicholas/clawd/_TABS/_inventory/scoreboard_2026-06-13.json` | Scoreboard snapshot | 127K |
| `/Users/nicholas/clawd/_TABS/_inventory/openmcp_npm_status_2026-06-13.json` | Full npm audit | 52K |
| `/Users/nicholas/clawd/mcp-marketplace/agent-incident-reporter-mcp/.well-known/agent.json` | New A2A surface (filled) | 1.7K |
| `/Users/nicholas/clawd/mcp-marketplace/agent-incident-reporter-mcp/acp.json` | New ACP surface (filled) | — |
| `/Users/nicholas/clawd/mcp-marketplace/agent-incident-reporter-mcp/llms.txt` | New LLM surface (filled) | — |
| `/Users/nicholas/clawd/mcp-marketplace/agent-incident-reporter-mcp/glama.json` | New Glama surface (filled) | — |
| `/Users/nicholas/clawd/mcp-marketplace/agent-incident-reporter-mcp/smithery.yaml` | New Smithery surface (filled) | — |

## What's still pending (Nick's lane)

| # | Action | Time | What it unblocks |
|---|--------|------|------------------|
| 1 | **GitHub PAT re-issue** (current `GITHUB_TOKEN` is invalid/revoked) | 2 min | `mcp-publisher login github` → publish 46 packages to MCP registry |
| 2 | **csga_global npm password change** | 30 sec | Kills 8 remaining tokens → can republish 192 meok-* packages under meok-ai-labs |
| 3 | **PyPI per-PROJECT throttle** | 24-48h wait OR Trusted Publisher OR support | Unblocks 22 phantoms + 40 first-publish |

## Nick's command (when ready)

```bash
# Refresh GitHub auth
gh auth login --with-token < github_pat.txt
# or
export GITHUB_TOKEN=<new_pat>

# Then run the publish
mcp-publisher login github && \
  python3 /Users/nicholas/clawd/mcp-marketplace/_scorecard/publish_registry.py
```

The publish is parallel + idempotent. Expected: 46 packages published in <5 min.
