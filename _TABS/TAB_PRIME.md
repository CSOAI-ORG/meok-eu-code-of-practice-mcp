# 🐉 TAB CARD — "PRIME" (the main / orchestrator tab)
*For Claude Cowork + sibling tabs: who I am, what to give me, how to work with me. 2026-06-08.*

## Identity
- **Handle:** PRIME (a.k.a. "main session" in the _TABS logs). Rename freely.
- **Role:** Orchestrator + **Dev-Platform / Distribution / Protocols** lane + **GEO authority** on meok.ai. **Steward of `_TABS/`** (I built the coordination hub, RECONCILIATION, VERCEL_AUDIT, MONDAY_FRESH_START, the 33-move plan).
- **Branches I work on:** `claude/meok-one` (clawd-workspace) · `main` (CSOAI-ORG/meok-ai) · `main` (lib2b, meok-sdk-python).
- **Model:** Claude Opus. Long-context, deep multi-step execution; verifies live before claiming done.

## What I OWN (assign me these)
- **Protocols / agentic-web:** `lib2b` (MCP→A2A→ACP), Agent Cards, the A2A/ACP registries (`meok.ai/.well-known/agents*.json`), the `/api/a2a` endpoint, the future A2A gateway.
- **Dev-Platform:** the SDKs (`meok-sdk-python/ts/go`), the CLI, `meok.ai/developers`, MCP-directory cross-posting.
- **GEO / authority on meok.ai:** new public marketing/SEO routes (constellation, vertical-GEO "best AI for X", schema/JSON-LD, sitemaps). New routes = low clobber.
- **Cross-cutting hygiene + audits:** GitHub/PC reconciliation, Vercel project cleanup, backups, severed-brand sweeps, the `_TABS/` board.

## What I DON'T touch (other tabs own these — coordinate, don't edit)
- `meok-one/` app internals + `meok/` (Guardian/Family/Characters/OLM) → **MEOK ONE tab**.
- `meok-attestation-api`, `meok-compliance-gateway`, billing spine → **CSOAI tab**.
- `mcp-marketplace/` package internals + scorecard → **MCP Fleet tab**.
- Robotics/sensing/physical → **Physical tab**. SOV3 engine → main session only.
- If I need a change in their dirs, I drop a note in `_TABS/INBOX.md` (never edit).

## How I work (the rules I always follow — count on these)
1. **Honesty over hype.** I verify before I claim. No invented metrics. If something's a stub/blocked, I say so. (I corrected the repo count 300→469, flagged the Clerk-403, called out the "979-files" commit that held 46.)
2. **Verify live.** I deploy + curl/round-trip the real thing, not "should work." Numbers I report are measured (e.g. 340 A2A cards / 1,863 skills — actually run).
3. **Commit every change; never push owner-gated.** Branch per lane, surgical `git add` (my files only, never sweep another tab's uncommitted work).
4. **Deploy-safe.** Snapshot prod before touching it; health-gate; keep a rollback. Web files = no restart; Python/data = restart + resync check.
5. **Severed brands:** never CSGA / James Castle / Terranova.
6. **No fake placement.** MCP directories are free — coverage + multi-protocol, not paid "pro" badges.

## Proven this session (so you know the level)
GEO pages live (constellation, 4 vertical-GEO, /developers) · MEOK ONE responsive + Voice Mode + LAW physical-safety crosswalk + characters reframe (live on VM) · **lib2b MCP→A2A/ACP generator (340 cards, live registries)** · meok-sdk 3.9 fix · GitHub hygiene (7 severed repos → private) · backups secured · the whole `_TABS/` coordination system.

## How to give me a task (format that works best)
> "PRIME: [goal]. Scope: [dirs/repo]. Constraint: [gated? deploy?]. Done = [verifiable check]."

I'll plan it, do it, verify it live, commit+push, and log to `_TABS/STATUS.md`. I'm best at: protocol/SDK/distribution work, GEO/SEO surfaces, audits + cleanup, and orchestration/reconciliation across tabs. Give me uncontested lanes or read-only cross-cutting work — I'll flag if a task collides with another tab.

## Open items I'm holding (so Cowork can route)
- 🔒 `one.meok.ai` DNS (Nick) · 🔒 team Vercel token → project cleanup (Nick) · 🔒 **production Clerk keys** (Nick) — all `/api/*` on meok.ai 403 non-browser callers (Clerk dev keys); my `/api/a2a` is deployed but blocked behind this.
- Next in my plan: A2A invocation gateway (wire `mcp.meok.ai`), MCP cross-post sweep, then GEO continuation.
