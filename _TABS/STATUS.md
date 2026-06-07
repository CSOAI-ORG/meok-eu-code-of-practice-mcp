# 🟢 MEOK Tabs — Live Status Board
*Every tab appends 3 lines here when it finishes a chunk: what changed · what's live · what's blocked.*
*Newest at top. This is how all tabs + Nick stay in sync.*

---

## 2026-06-07 — main session: SIGIL trust-anchor fix + Six-Pillars lens + GitHub align
**main session** · `meok-attestation-api` repo `main` (pushed 97e40bb) + `_TABS/` (clawd-workspace)
- Changed: fixed the public `/verify` trust anchor — it crashed (`'dict' object has no attribute 'encode'`) on the documented object form `{payload:{...},signature}`; now re-canonicalises dict payloads so HMAC matches the signer. +regression test (both forms + tamper rejection, all pass). Added `_TABS/SIX_PILLARS.md` (architecture lens: SIGIL/LAW/MAP/COMPLIANCE/DOME/COUNCIL → real homes + CSOAI-engine wiring contract). Corrected DOME = MEOK World/constellation map (ours), NOT 3rd-party AIdome. Removed an orphan doc I'd wrongly left at `~/` (outside the repo).
- Live: fix pushed to `CSOAI-ORG/meok-attestation-api` main; NOT yet on prod — Vercel free-tier deploy cap hit (>100/day, resets ~24h). Code is safe + tested, lands on next deploy.
- Blocked / for Nick: (1) Vercel deploy of SIGIL fix waiting on 24h cap reset; (2) MAP vs DOME — I split them (MAP=terrain data, DOME=rendered map); confirm or collapse.

## 2026-06-07 — MEOK ONE tab claimed ownership + inventory honesty pass
**MEOK ONE** · branch `claude/meok-one` (this tab)
- Changed: this tab now OWNS the MEOK ONE consumer OS. Verified real homes for the 5 products Nick named + added them to the hub (Gaming=hud surface · Characters=server.py+characters.json · Characters **Factory**=engine path unverified, flagged · Guardian + Family OS=real in `meok/` + live MCP tools, no `/os` surface yet · **OLM=named-but-not-built, the genuine miss**).
- Live: nothing newly deployed — this was an inventory/ownership pass (no prod touch).
- Blocked / decisions for Nick: (1) `meok/` is assigned to NO tab — Guardian/Family/Characters source live there; (2) should MEOK ONE surface `/guardian`+`/family` tabs over the existing `meok/` MCP tools? (3) OLM needs a 1-page spec before it's a product.

## 2026-06-07 — characters leftovers CLOSED (LIVE, commit cc76dcb)
**MEOK ONE** · branch `claude/meok-one` (main session)
- Changed: faith-pack opt-in filter (default roster=24 wholesome; "faith pack on"→27; new `pack` field on list API + client filter); collectible-creature card styling; anime voice (brighter pitch/rate in Anime Mode).
- Live on VM: health 200, `/api/characters` exposes pack=faith, faith hidden by default, Voice Mode intact.
- NOTE: two tabs now touch meok-one (this + the new MEOK ONE tab) — clobber risk is live. This session's character work is DONE; next character chunk (avatar art, anime persona variants) is free for the other tab.

## 2026-06-07 — characters reframe + Anime Mode (LIVE)
**MEOK ONE** · branch `claude/meok-one` (pushed, commit 7cea5da)
- Changed: softened 9 adult/OTT personas (Marcus/Atlas/Titan/Vox/Rex/Cipher/Ember/Nyx/Dusk → warm/playful tagline+system_prompt); faith trio tagged `pack:faith`; added Anime Mode (opt-in vivid skin, "anime mode").
- Live on VM: softened taglines serving (`/api/character`), Anime Mode in /os, health 200, Voice Mode intact.
- Next (not done): default/opt-in roster filtering for the faith pack; cute avatar art (needs an artist/gen — no art assets in the stdlib app); anime persona variants.

## 2026-06-07 — main session (seed)
**MEOK ONE** · branch `claude/meok-one` (pushed)
- Changed: responsive pass (os/dome/law mobile), Voice Mode (orb+STT+TTS), Mac↔VM reconcile, LAW physical crosswalk.
- Live on VM: all of the above (`/os /law /dome` 200, Voice Mode + 28-framework LAW deployed).
- Blocked: `one.meok.ai` DNS (Namecheap A → 35.242.143.249) — owner-gated. Public exposure pending.

**CSOAI** · LAW physical-safety crosswalk
- Changed: +5 frameworks (ISO 13482/10218/45001 + EU/UK machinery), surfaced for humanoid/robotics entities.
- Live on VM: 23→28 crosswalks; humanoid@UK/EU returns physical law + obligations.
- Blocked: none.

**MCP Fleet** · branch `claude/meok-one` (marketplace is gitignored — local only)
- Changed: registry+GEO audit (`REGISTRY_GEO_AUDIT.md`), hub-backlink footer on 16 READMEs, 2 pkgs republished (meok-bs7121, meok-tacho-audit).
- Live: PyPI READMEs updated for the 2 republished; rest flow on next sweep.
- Blocked: 14 footer'd pkgs unpublished — publishing = new PyPI projects = re-trips cap. Hold.

**meok.ai (marketing/Next)** · separate repo CSOAI-ORG/meok-ai
- Changed: GEO moves 44–47 (Person schema, /constellation, 4 vertical-GEO pages, sitemap).
- Live: all 5 pages on meok.ai (200, JSON-LD valid).
- Blocked: none.
