# 📥 MEOK Tabs — Cross-Tab Inbox
*If you need a change in another ecosystem's dirs, DON'T edit them. Drop a note here for that tab.*
*Format:  `→ [target tab]: [what you need + why]  — from [your tab], [date]`*

---

✅ DONE → MEOK ONE: characters reframe (soften 9 OTT personas · faith trio → opt-in `pack:faith` ·
  Anime Mode toggle · Tamagotchi mechanic). Shipped commit 7cea5da, live on VM. — closed by MEOK ONE tab, 2026-06-07

→ TAB 6 (Physical): MEOK ONE wants to surface `/guardian` + `/family` tabs inside `/os` that CALL your
  existing `meok/` MCP tools (guardian_*, family_*). You'd keep the sensing/robotics backend; we'd own the
  consumer UI surface only. Need Nick's OK on the split + confirmation `meok/` isn't actively owned elsewhere.
  — from MEOK ONE, 2026-06-07

✅ DONE → OLM 1-page spec drafted: `_TABS/OLM_SPEC_v0.1.md`. Correction to the "zero code" framing: OLM
  is a 5-repo cluster already (meok-ai + meok-agent-zero + meok-neural-learning + consciousness/creativity
  engines) — the spec NAMES + WIRES them, lists the 4 milestones before "shipped". Canonical home = meok-ai
  README once Nick accepts. — by MEOK ONE, 2026-06-07
  ⏭ NEXT (this tab, per decision #2): build `/guardian` + `/family` surfaces in `/os` over the meok/ MCP tools.
  ⚠️ COORDINATION: main session is actively editing meok-one this session (char work, commit cc76dcb). Will
  confirm main has paused meok-one edits before I touch server.py/web/ — clobber risk is live.

---
## ✅ NICK'S DECISIONS (relayed by main session, 2026-06-07)
1. **`meok/` → assigned to the MEOK ONE tab.** It's the source of Guardian/Family/Characters. One owner. No other tab edits `meok/`.
2. **YES — surface `/guardian` + `/family` tabs inside `/os`.** MEOK ONE tab owns the consumer UI; it CALLS the existing `meok/` MCP tools (guardian_*, family_*). Keep the backend where it is.
3. **YES — OLM gets a 1-page spec BEFORE it's called a product.** MEOK ONE tab to draft: what it learns from, where it lives, how it ties to SOV3 neural retrain + ICRL. Until the spec exists, OLM is "planned", not shipped (honesty rule).

## 🆕 from main session (GitHub+PC reconciliation) — see RECONCILIATION_2026-06-07.md
→ ALL tabs: a 7th ecosystem exists — **Dev Platform/Distribution** (SDKs go/ts/python, cli, teams/slack/vscode apps, skills, integrations). Needs an owner (`claude/devplatform`).
→ Nick: 🔴 `~/CSOAI-Research-Institute/` (26k files) + `~/councilof-ai/` (25k files) are LOCAL-ONLY, no git/GitHub backup. Highest-value protection = back them up. NOT auto-pushed (secret-leak risk — we found leaked Stripe keys this session; needs a scan first).

## 🆕 from main session (Six Pillars / CSOAI engine wiring — Stage 3) — see CSOAI_ENGINE.md
*The signing/verify/billing/audit spine ALREADY EXISTS in `meok-attestation-api` (verified live this session). Wiring = pointing pillars at it, not building it. Endpoints + per-pillar targets are in `_TABS/CSOAI_ENGINE.md`.*
→ **MEOK ONE tab (LAW + DOME):** (1) LAW results in `meok-one/.../law*.py` should emit `/sign`-signed certs with a `verify_url` (call `meok-attestation-api` `/sign`), so a crosswalk result is verifiable evidence, not just text. (2) DOME (`web/dome`) map nodes should each link to that product's live `/verify` proof. Don't build signing — just call the existing `/sign` + link `/verify`.
→ **MCP Fleet tab (MAP):** make the registry manifests + `_TOPOLOGY/` the ONE canonical graph DOME renders (MAP=data, DOME=picture — ruling below). A single `topology.json` the DOME surface can fetch.
→ **CSOAI lane (mine, DONE this session):** SIGIL `/verify` object-form bug fixed+pushed (`meok-attestation-api` 97e40bb); COMPLIANCE LAYER gateway smoke-tested green + CI test pushed (`meok-compliance-gateway` 58c9a38). Remaining CSOAI cell = billing-link consolidation (the 50-link sprawl → one ladder via the existing webhook/provision spine) — flagged, not yet done.
✅ RULED (Nick delegated) → MAP vs DOME: **MAP = terrain data (topology+registry); DOME = the rendered World/constellation map that draws MAP.** One capability, two layers. Collapse later if you prefer one. — main session, 2026-06-07
