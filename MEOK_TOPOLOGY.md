# MEOK — Living Product Topology (the full stack, proven)

**DEFONEOS** = the whole private GitHub ecosystem (this monorepo = `CSOAI-ORG/clawd-workspace`,
**verified PRIVATE** ✅). Everything below is a product *inside* DEFONEOS.
**Proof discipline:** every product shows hard evidence (folder / package / domain / doc) found on
disk 2026-05-31, or is honestly marked **NAME-ONLY** (concept, not yet built).

Legend: 🟢 built+real · 🟡 partial/started · 🔵 name/concept only · ⭐ revenue-live

---

## THE SPINE (infrastructure — ties it all together)
| Product | What it is | Proof | State |
|---|---|---|---|
| **MEOK DEFONEOS** | The private GitHub ecosystem / master alignment (umbrella) | `MEOK_DEFONEOS_ALIGNMENT.md`, repo isPrivate=true | 🟢 |
| **MEOK SOVEREIGN** | SOV3 — the brain: memory, council, 110 MCP tools, neural nets | `sovereign-temple/` (6.6GB), `sovereign-temple-live/`, `meok-sovereign-api/` | 🟢 |
| **MEOK MCP** | The connective tissue — 264 PyPI MCPs + gateway that exposes every tool | `meok-api-gateway/`, `mcp-marketplace/`, `mcp-bridge/`, 264 published | 🟢⭐ |
| **MEOK SIGIL** | Wire format — 2.4× denser than JSON, HMAC-signed (agent comms) | `meok-sigil/` | 🟢 |
| **MEOK SYNC** *(new, spec'd)* | The A2A bus — agents talk over SYNC, SIGIL-encoded, COUNCIL-gated | `MEOK_BRIDGE_SPEC.md` + a2a/agentfacts/orchestrator MCPs | 🟡 |
| **MEOK MESH** | libp2p peer mesh (decentralised transport) | `meok-mesh/` | 🟡 |
| **MEOK EI3** | The safety substrate — care/ethics layer over everything | `csoai-org/`, `safetyof-ai/`, EI3 manifest | 🟢 |

## THE CONSUMER PRODUCTS (the experiences end-users touch)
| Product | What it is | Proof | State |
|---|---|---|---|
| **MEOK ONE** | The hatch→3D character→talk OS (your flagship; left/right/council brains) | `meok-one/` (renders, verified), `meok/ui/` (Next app) | 🟢 |
| **MEOK GAMING** | Emergence characters as playable game AI (Godot/Unity, north-star) | `scf-game-v1/`, `meok-3d-characters/`, gaming arch zip | 🟡🔵 |
| **MEOK CLAW** | The TUI / terminal sovereign (Go CLI, Homebrew tap) | `meokclaw-tui/`, `homebrew-meokclaw` | 🟢 |
| **MEOK GUARDIAN** | 24/7 family/child safety (game content, network, moderation) | `family-guardian-mcp/`, SOV3 guardian_* tools | 🟢 |
| **MEOK FAMILY** | Family OS — members, chores, events, shared care | `meok-family/`, SOV3 family_* tools | 🟡 |
| **MEOK SMB** | Small-business OS (the small-business skill suite) | `meok-smb/` | 🟡 |
| **MEOK WORK** | The work agents — Orion (tasks) / Riri (tools) / Hourman (sprints) | `sovereign-temple-live/agents/`, 70 docs | 🟢 |
| **MEOK ENTERPRISE** | Enterprise tier — 33-agent council, compliance, audit, £1,499/mo | `csoai-platform/`, Stripe Enterprise product live | 🟢⭐ |

## THE GOVERNANCE / COMPLIANCE SURFACE (the cash engine today)
| Product | What it is | Proof | State |
|---|---|---|---|
| **MEOK MAP** | Geospatial / compliance mapping (Gods-Eye, civilian) | `god-eye/`, gods-eye-geospatial-mcp, `start_dagon_maps.sh` | 🟡 |
| **MEOK DELBOY** | "Revenue mode" — the monetization engine/playbook (not a folder, a MODE) | 14 docs (LOOPFACTORY_Delboy_Mode etc.), `loopfactory-marketplace/` | 🟡⭐ |
| **MEOK BLACKSWAN** | x402 / machine-payment + frontier-tool research strand (a MODE/research) | 6 docs (BLACK SWAN x402/K2.6) | 🔵 |

## NAME-ONLY (concept, no build yet — honest flag)
| Product | Status |
|---|---|
| **MEOK DONE** | 🔵 0 files found. Pure name. Needs a definition before it's anything. (Task-completion product? "done" state?) |

---

## What this proves
- **17 of 18 named products have real evidence on disk.** Only **MEOK DONE** is purely a name.
- **DELBOY + BLACKSWAN are MODES/playbooks, not folders** — that's correct, they're how you *operate*
  the products (DELBOY = make money, BLACKSWAN = chase frontier edges), not products themselves.
- The portfolio splits cleanly into **3 layers**: Spine (infra) → Consumer products → Governance/cash.
- Everything is unified by **MEOK MCP** (every product exposes its tools as MCPs) + **MEOK SYNC**
  (every agent/brain talks over the same SIGIL bus) + **MEOK EI3** (every action passes the safety layer).

## The GitHub living-topology layout (where each maps in the monorepo)
```
clawd-workspace/  (= DEFONEOS, private)
  spine/
    sovereign/   (SOV3 — code in git, 6.6GB weights → GCS)
    mcp/         (gateway + the 264 MCP servers)
    sigil/  mesh/  sync/   ei3/
  products/
    one/  gaming/  claw/  guardian/  family/  smb/  work/  enterprise/
  governance/
    map/  delboy/ (revenue playbooks)  blackswan/ (research)
  research/      (all .md docs + inbox)
  COORDINATION.md  MEOK_TOPOLOGY.md (this file)
```

## Honest gaps before "fully aligned on GitHub"
1. **MEOK DONE** undefined — tell me what it is, or drop it.
2. Restructure into the layout above = a big, careful move (secrets stripped ✅, big files → GCS pending).
3. Several products are 🟡 partial — "improve inner features/tools/experience" (your ask) means
   picking which 🟡 to push to 🟢 first. My vote: MEOK ONE (flagship, already closest).
4. ~509 separate MCP repos exist outside this monorepo — decide: pull into `spine/mcp/` or keep as
   submodules/separate (they're independently published to PyPI).

## Decisions to lock the topology
1. Confirm the 3-layer grouping (spine / products / governance) is how you think of it.
2. **MEOK DONE** — define or drop?
3. Which 🟡 product to improve first? (I recommend MEOK ONE.)
4. Pull the 509 MCP repos in, or reference them?
