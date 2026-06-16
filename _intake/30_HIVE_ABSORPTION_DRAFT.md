# 🐉 30-Hive Absorption — 10 Master Hives Draft
**Goal:** Consolidate the MEOK/CSOAI 442-repo estate into 10 master hives, each with sovereign coordinator + COAI manifest + Ed25519 sigil + BFT Council. Staged out-of-tree (iCloud) per ralph-mode-overnight-sprint pitfall #3.

**Sigil:** to be emitted on each hive registration (10 sigils total)

---

## The 10 master hives

| # | Hive | Coordinator | Sub-hives | Domain |
|---|------|-------------|-----------|--------|
| 1 | **meok-keystone-hive** | `meok-keystone` | sovereign-coordinator, x402-billing, ed25519-signer, hmac-fallback | keystone substrate |
| 2 | **meok-governance-hive** | `meok-governance-engine` | csoai-attestation, csoai-council, csoai-crosswalk, csoai-watchdog | csoai.org |
| 3 | **meok-compliance-fleet** | `meok-compliance-gateway` | eu-ai-act, dora, nis2, cra, gdpr, iso-42001, iso-27001, soc2, pci-dss, hipaa, nist-rmf, care-membrane, proofof, llm-compliance | proofof.ai (compliance catalogue) |
| 4 | **meok-utility-fleet** | `meok-api-gateway` | document-comparison, healthcare-fhir, healthcare-governance, construction-iso-19650, care-home-scheduling, domiciliary-care, optical-care-home, llm-compliance-comparison | api.meok.ai |
| 5 | **meok-distribution-hive** | `meok-distribution` | PyPI publisher, npm @csgaglobal, mcp-marketplace, smithery-bridge, glama-bridge, punkpeye-bridge, apify-bridge | npm/PyPI/CDN |
| 6 | **meok-consumer-hive** | `meok-consumer` | meok-one, meok-os-v3, family-os, character-dashboard, mood-board, voice, vr, notifications, daily-ritual, habit-tracker, dome, council, gaming | meok.ai (consumer surface) |
| 7 | **meok-gaming-hive** | `meok-gaming-hive` | wow-mcp, ffxiv-mcp, eve-mcp, osrs-mcp, poe-mcp, diablo-iv-mcp, evergame-hive-mcp, mmoagent-mcp, pokerhud, gustfish | wowmcp.ai (MEOK Gaming) |
| 8 | **meok-verticals-hive** | `meok-verticals` | care-home-cqc, planthire-ai, muckaway-ai, diyhelp-ai, fishkeeper-ai, koikeeper-ai, landlaw-ai, socialmediamananger-ai, loopfactory-ai, optimobile-ai, suicidestop-ai, commercialvehicle-ai, grabhire-ai | 13 vertical .ai domains |
| 9 | **meok-aquaculture-hive** | `meok-aquaculture` | fishkeeper-ai, koikeeper-ai, aquaculture-water-quality, aquaculture-feed-optimizer | fishkeeper.ai + koikeeper.ai |
| 10 | **meok-research-hive** | `meok-research` | mavis-mcp-marketplace, oasf, openpatent-hive (api, patentmcp, drafting-fork, bft), openmoe-ai, sovereign-organic-brain | meok-research, openmoe.ai, openpatent.ai |

**Total: 10 master hives × ~3 sub-hives = ~40 sub-hives** (matches the marketing "30-hive mesh" claim).

---

## The 10-move absorption plan (Sprint 4 prep)

### M1: Register 10 hive coordinators on SOV3
```bash
for hive in keystone governance compliance-fleet utility-fleet distribution consumer gaming verticals aquaculture research; do
  curl -s -m 10 -X POST http://localhost:3101/mcp -H "Content-Type: application/json" -d '{
    "jsonrpc":"2.0","id":"1","method":"tools/call",
    "params":{"name":"coord_register_agent","arguments":{
      "agent_id":"meok-'"$hive"'",
      "agent_type":"claude-code",
      "capabilities":["hive_coordinator","sov3_sovereign","coai_certified","ed25519_signer"]
    }}}'
done
```

### M2: Build hive_triage.py (rule-based)
- 419 repos → 10 hive assignments
- Stdin: GITHUB_INVENTORY_2026-06-07.md
- Stdout: hive_assignment_2026-06-XX.json

### M3: Run triage → emit hive_assignment JSON

### M4: Update MCP_DEPLOYMENT_MANIFEST.json (419 entries with hive: field)
- 0 `hive: none` after

### M5: Write 10 COAI compliance manifests
- One per hive: canonical JSON, SHA-256 hash, COAI gates, banned features, BFT Council structure, monetization tiers

### M6: Submit 10 BFT Council charter proposals
- Each: 5 voter seats, chair = hive coordinator
- 2 → 12 proposals total

### M7: Emit 10 hive seal sigils on Ed25519
- One per hive, op code = `H`

### M8: Build 10-hive index doc
- `~/clawd/_TABS/_inventory/HIVES_2026-06-XX.md`

### M9: Update live /fleet hub to show 10 hives
- New section in meok.ai/fleet (when Vercel WAF clears)

### M10: Final seal sigil + absorption completion report
- `A|meok-keystone|30-hive-absorption-complete|...` with all 10 hive digests

---

## The 3 ratification questions (before execution)

1. **Coordinator names** — Want to rename any of the 10 coordinators?
2. **Sub-hive structure** — Keep flat (10 only) or expand to 10 × 4 = 40 sub-hives?
3. **Include the 23 extras?** — 419 in inventory, but ~23 duplicates. Include all or just the 419?

---

## Expected outcomes (per the skill)

- SOV3 agents: 184 → 194 (+10)
- SOV3 tasks completed: 54 → 64 (+10)
- SOV3 proposals open: 0 → 10 (+10)
- Ed25519 sigils on chain: +10
- MCP_DEPLOYMENT_MANIFEST `hive: none`: 202 → 0
- COAI compliance manifests: 11 → 21 (+10)
- BFT Councils active: 0 → 10 (each with 5 voter seats)
- /fleet hub: shows 10 hives

---

## Red lines (held)

- No new repos created (the 419 already exist)
- No destructive operations
- 4 severed (CSGA/Terranova) NEVER touched
- Additive only — every existing URL, history, LICENSE, README preserved
- Hive coordinators are added agents, not replacing existing ones
- MEOK Gaming hive preserved as-is (it was the only one with existing BFT charter)

---

JEEVES, signing off. 🫡
