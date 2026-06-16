# 🐉 Sprint 1 Audit: Day 1 (15 Jun 2026)
**Audit time:** 15 Jun 2026, 14:15 UK
**Sprint window:** 15-19 Jun 2026 (5 days, 30 moves)
**Sprint goal:** Close the 6-action env gate → first £199/mo customer

---

## 6-Action Gate Status (verified, not claimed)

| # | Action | Status | Evidence |
|---|--------|--------|----------|
| 1 | **SMTP env in `~/.hermes/.env`** | ✅ **SET** | `EMAIL_ADDRESS=***`, `EMAIL_PASSWORD=***`, `EMAIL_IMAP_HOST=***` all present |
| 2 | **IndexNow on 4 domains** | ⚠️ **CRON REGISTERED, IDLE** | `com.csoai.weekly-indexnow` + `com.meok.weekly-indexnow` loaded with PID `-`; no script executed this week |
| 3 | **MEOK_MASTER_API_KEY** | ❌ **NOT SET** | Not in `~/.hermes/.env`; not in `~/clawd/sovereign-temple/.env`; should be Vercel env var (per Day 4 discovery) |
| 4 | **1 outbound ready** | ⚠️ **PARTIAL** | `hive-mailer/queue.jsonl` has 44 rows BUT all 44 are `status: sent` from 14 Jun; **0 actually pending** |
| 5 | **launchctl load (autostart)** | ⚠️ **PARTIAL** | `com.csoai.mcp-monetization-api` (PID 9542) running; keystone tests work; most other plists PID `-` (idle, not running) |
| 6 | **wowmcp.ai domain bought** | ❌ **NXDOMAIN** | `host wowmcp.ai` returns 3(NXDOMAIN); user must buy at Namecheap |

**Score: 0/6 fully green, 1/6 set, 3/6 partial, 2/6 missing.**

## The 3 User-Gated Actions

The user must do:
- **A:** Buy wowmcp.ai at Namecheap (5 min, ~£10)
- **B:** Set MEOK_MASTER_API_KEY in Vercel env (5 min, 1 keystroke)
- **C:** Verify `mail.meok.ai` in Resend dashboard (5 min, 1 click)

The 3 partials can be closed by autonomous actions:
- **D:** Trigger the 2 IndexNow crons (1 keystroke: `launchctl kickstart -k`)
- **E:** Re-stage 95 new prospect emails (5 min, mcp_bridge_call)
- **F:** Run `launchctl load` on the 6 idle plists (2 min, 6 commands)

**Net user work: 15 min for A+B+C → first £199/mo customer unlocked.**

## Sprint 1 Plan (30 moves, 5 days)

### Day 1 (15 Jun — TODAY) — Audit + Plan (DONE this session)
- ✅ M1: Sovereign-temple Python 3.9 → 3.11 venv rebuild (DONE)
- ✅ M2: mcp + ddgs + weaviate v3 install (DONE)
- ✅ M3: mcp_bridge_call verified end-to-end (a2a-governance-bridge-mcp.get_trust_registry)
- ✅ M4: openpatent-hive docker compose rebuilt (13/13 containers healthy)
- ✅ M5: 2 plists env-injected (hermes gateway + sovereign gunicorn)
- ✅ M6: 19-day plan written (`~/clawd/_intake/19_DAY_PLAN_TO_4JUL2026.md`)
- ✅ M7: Sprint 1 audit written (this file)

### Day 2 (16 Jun) — IndexNow + Outbound re-stage (6 moves)
- M8: `launchctl kickstart -k gui/$(id -u)/com.csoai.weekly-indexnow`
- M9: Same for `com.meok.weekly-indexnow`
- M10: Verify both ran (check logs + IndexNow API)
- M11: Re-stage 95 emails via mcp_bridge_call (25 EU + 20 GRC + 25 care + 25 enterprise)
- M12: Wire 5-touch autoresponder sequence (Day 0, D+3, D+7, D+14, D+30)
- M13: 5 EU prospects with day-1 keystone certs as lead magnet

### Day 3 (17 Jun) — MEOK_MASTER_API_KEY path (6 moves)
- M14: Document the 2 keystrokes (Vercel dashboard env + the 32-char hex mint)
- M15: Probe `POST /provision` endpoint to confirm master-key auth path
- M16: Probe `meok-claim` :3102 to confirm customer key auth path
- M17: Build the customer-mint script (no real Stripe, just staging)
- M18: Add 5 row to MEOK_MASTER_API_KEY docs
- M19: Verify SOV3 sigil for "master-key path ratified"

### Day 4 (18 Jun) — wowmcp.ai + first keystone certs (6 moves)
- M20: Document the 1 keystroke (Namecheap search → buy → DNS to Vercel)
- M21: Stage 3 meok-gaming-hive manifest files in iCloud staging
- M22: Issue 25 free keystone certs across 20 verticals (one warm intro per prospect)
- M23: Build 25 prospect emails with cert URLs
- M24: Stage 25 follow-ups (D+3, D+7, D+14, D+30)
- M25: SOV3 sigil: "25 keystone certs minted, 0 £199 customer"

### Day 5 (19 Jun) — Sprint 1 seal (6 moves)
- M26: First outbound send (25 EU prospects, with keystone cert lead magnets)
- M27: 5-touch autoresponder armed (Day 0/3/7/14/30)
- M28: SOV3 sigil: "Day 5 sprint 1 complete, 25 outbound sent, £0 MRR (waiting on responses)"
- M29: Sprint 2 handoff doc (`~/clawd/_intake/SPRINT_2_HANDOFF.md`)
- M30: Final seal (the 4-section shape)

**Sprint 1 success criteria (per the 6-action gate):**
- 6/6 actions green
- 25 first-touch emails sent
- 25 keystone certs issued
- £0 MRR → first £199 conversion in D+7-D+14 (after autoresponder + follow-ups)

**Sprint 1 red lines (held):**
- No real Stripe charges
- No real namecheap purchases
- No real social posts
- No real wallet spends
- All SMTP sends via `confirm=True` path
- No `~/.meok/` writes

---

**JEEVES, signing off Sprint 1 audit. 🫡**
**Next action: tomorrow (16 Jun) start with M8 — kickstart the 2 IndexNow crons.**
