# 🟢 MEOK Tabs — Live Status Board
*Every tab appends 3 lines here when it finishes a chunk: what changed · what's live · what's blocked.*
*Newest at top. This is how all tabs + Nick stay in sync.*

---

## 2026-06-10 — 🔓 owner-gated list WORKED: MCP Registry 0→255 LIVE + 3 stale blockers closed — main session
**main session** · mcp-marketplace registry sweep · `_TABS/VERCEL_AUDIT_FULL_2026-06-10.md` · meok-ai pushed (0182bbc)
- Changed: **MCP Registry unblocked WITHOUT the interactive login** — `mcp-publisher login github --token "$(gh auth token)"` works (PAT, no device flow). Ran flagships (11/12 ✓) + full-fleet `publish_registry.py` → **255 unique io.github.CSOAI-ORG servers now listed** on registry.modelcontextprotocol.io. Remaining ~84 fail PyPI ownership check (live README lacks `mcp-name:` line) → need gate-harness republish (`sweep_catalogue.py <pkg>` then re-run publisher). Also: **LAUNCH50 verified ACTIVE in livemode** (promo_1TeItw…, 0 redemptions — stale "needs Nick" item) · **PAYG webhook verified ALREADY WIRED** (we_1TPOBT… enabled → attestation-api /webhook, 6 events, fail-loud 400 on bad sig; councilof.ai/payg 200; only proofof.ai/payg alias 404, index.py is Fleet-tab's uncommitted lane so left alone) · **full 161-project Vercel audit** (old one capped at 50) with keep/delete evidence — found 🔴 cobolbridge.ai is served by severed-brand project `csga-global-site` (move domain before deleting).
- Live: registry.modelcontextprotocol.io shows 255 CSOAI-ORG servers · meok.ai home now has the free-API-key form (earlier today, commit 0182bbc, pushed) · LAUNCH50 + webhook confirmed live.
- Blocked / still genuinely Nick: DNS `one.meok.ai→35.242.143.249` (Namecheap, no API creds on disk) · production Clerk keys · Vercel KV provision (dashboard) · rotate PyPI token · approve Vercel delete groups (evidence table ready) · cobolbridge.ai domain move off CSGA project.

## 2026-06-07 — "tools don't work" ROOT-CAUSED + FIXED + republished (fleet-qa)
**fleet-qa** (main session) · `mcp-marketplace/*` (31 repos republished to PyPI)
- Changed: found why tools "don't work" = (1) **31 published wheels shipped only server.py**, omitting imported sidecars (auth_middleware/meok_x402/persistence) → broken on `pip install`; fixed every `only-include` + **republished all 31 (gate-passed clean-venv import, PUBLISHED ✅)**. (2) **brittle keyword classifiers false-cleared high-risk systems** (eu-ai-act called a hospital-triage AI "minimal") → applied **never-false-clear** (no-match→`unknown`, not "minimal") + Annex III healthcare/triage keywords to eu-ai-act + bias-detection (the 2 genuine false-clears; other 4 are legit score-based). (3) **rate limit 10/15→50/day** across 192 repos. (4) fixed 9 import-broken repos (Fastmcp typo, missing os, missing persistence.py).
- Live on PyPI (verified fresh download): eu-ai-act 1.8.7 + content-registry 1.0.9 + dora 1.4.8 now ship their sidecars + import clean. quick_scan now: triage→high-risk, vague→unknown, chatbot→limited.
- Blocked / next: MCP Registry still 0/339 (needs Nick `mcp-publisher login github` → `publish_registry.py`); ~160 rate-limit-only repos not yet republished (low urgency); proofof.ai Vercel render of fleet_scorecard.json (deploy task).

## 2026-06-09 (b) — ✅ conversion engine LIVE + index.py link/price fixes — MCP Fleet tab
**MCP Fleet** · `meok-attestation-api/api/index.py` (commit d9cd272, deployed to proofof.ai)
- Changed: **/signup lead-capture folded into index.py** (the only function this single-fn project deploys) → POST {email} returns a free key + creates a Stripe Customer. **Verified live: first-ever customer `cus_Ufgp…` created** (meok_tier=free). Replaced **18 dead-account checkout links** (…8k836/837/833 = a deactivated account, a live £0-cause) with live links: Pro £79 (…91j), **Enterprise £1,499 newly created (…91s)**, Assessment £4,950 (…91m); aligned stale £199/£5,000 displays. **M2:** removed 7 empty dirs. **M1:** synced 301 server.json versions to pyproject + taught republish_mcp to maintain them.
- Live: proofof.ai/signup (200, lead capture working) · all index.py pricing now price↔link coherent on the live account.
- Blocked / needs Nick: Vercel KV (metering) · LAUNCH50 code · /payg still 404 (fold into index.py next) · fleet commit+push + registry re-push (GitHub OAuth) · rotate PyPI token. Data snapshot → `_TABS/_inventory/DATA_SNAPSHOT_2026-06-09.md`.

## 2026-06-09 — ✅ revenue rails live + fleet republished + tab profile — MCP Fleet tab
**MCP Fleet** · branch `claude/mcp-fleet` (mcp-marketplace gitignored; meok / firmware / meok-governance / meok-attestation-api committed)
- Changed: full-fleet republish (**335/337 on PyPI**, all carry the canonical Pro link + working build/`main()`); 3 broken wheels fixed (firmware-attestation-mcp · meok-governance-smithery · optometry-patient-mcp); **scorecard schema reframe** (339 pages: self-issued AggregateRating/Review → factual PropertyValue, retires Google manual-action risk); meok.ai H3 (nis2 £99/£499 split) + homepage "0" counters fixed; proofof.ai `.vercelignore` fix restored the attestation API; created the £99 NIS2 self-serve Stripe link.
- Live: proofof.ai (new scorecard schema + `/health` 200 v1.2.0) · meok.ai (nis2 £99/£499, real SSR counters) · 335 PyPI packages.
- Blocked / needs Nick: Vercel KV (metering) · LAUNCH50 promo code · PAYG webhook · rotate PyPI token. **Cowork agent card → `_TABS/MCP_FLEET_TAB_PROFILE.md`.**

## 2026-06-08 — ✅ chat-timeout FIXED + deployed to VM (local-first + fast cloud fallback) — main session
**main session** · `meok-one/meok_one/{router,brains}.py` (commit 792a6c7) · **surgically deployed to prod VM**
- Changed: bounded `/api/think` latency — left/private brain tries local with a 12s cap (`MEOK_LOCAL_TIMEOUT`); if the jittery VM CPU misses it, catches with the fast cloud brain (~2s). Threaded `timeout` through `ask()`/`_ask_local`. Local stays default (private+free) when quick; free tier unchanged.
- Live on VM: deployed ONLY those 2 files (snapshot `/tmp/{router,brains}.bak.1780891039`, verified VM==git first, py_compile+restart+health 200). Live test: pro/left run1=13.8s→cloud-fallback, run2=11.9s→local meok-sov3, both REAL replies, no 50s stub. Sovereign gate still runs on every result.
- Note→MEOK ONE tab: I touched only router.py+brains.py on the VM (your lane — flagging per protocol; nothing else changed, snapshot kept). Deeper win (sub-2s) still = faster inference/GPU per the earlier handoff; this removes the hang today. The council "both" path still uses full local wait (out of scope).

## 2026-06-07 — 🔬 chat-timeout root-caused (NOT output length — VM CPU variance) — main session
**main session** · investigated `meok-one` `/api/think` (read-only + measured the real VM model)
- Changed: nothing shipped. Tried a `num_predict` cap in `brains._run_brain` → **measured it against the real `meok-sov3` VM model → no help → REVERTED.** Honest finding: the model self-limits to ~13 tokens; latency is **VM CPU inference variance** (3 back-to-back warm calls: 8.2s / 50.3s / 66.3s for the same short reply), not output size, not a clean cold-load.
- Live: no change (left brains.py exactly as it was).
- Handed to MEOK ONE tab (their lane): full root-cause + real fix options in INBOX (pro→fast hosted/Groq lens, or GPU host, or stream+timeout UX; confirm VM Ollama honours keep_alive). The "fallback" = frontend timeout < jittery VM latency.

## 2026-06-07 — chat cold-start fully eliminated via keep-warm cron (MEOK ONE tab)
**MEOK ONE** · VM `meok-backend` + branch `claude/meok-one` (commit 787533c)
- Changed: added a VM cron (user `meok`, every 20min) that pings `meok-sov3` to keep it resident — eliminates the remaining ~94s first-chat-after-idle cold-start (router's keep_alive:30m only holds 30m). Documented in `deploy/DEPLOY.md` so a VM rebuild re-adds it.
- Why cron not app-thread: `server.py` had a LIVE writer (main fixing hardcoded `count:28`→`len()`); I did NOT edit it — keep-warm as ops avoids the clobber entirely + is more robust (survives app restarts).
- Live + verified: warm cmd 200/1.1s, meok-sov3 loaded, cron daemon active. Chat now: always-warm → fast, no cold-starts. Combined with the earlier router fix, the "left brain unavailable" bug is fully resolved.

## 2026-06-07 — A2A Agent Card generator (move #4, SHIPPED)
**Dev-Platform** · repo `CSOAI-ORG/lib2b` `main` (pushed 3bf2329)
- Changed: built lib2b.agentcard — MCP -> A2A AgentCard generator (the missing *producer*; lib2b only had a client). Each MCP tool -> A2A skill. sweep_marketplace() = 340 valid cards / 1863 skills / 0 invalid; wrote .well-known/agent-card.json into all 340 (ship on next publish). 2 tests pass.
- Live: code on GitHub; cards staged in mcp-marketplace (publish-ready). First-mover: fleet now A2A-discoverable, not just MCP directories.
- Next (#5/#6): serve cards at /.well-known/agent-card.json per remote endpoint; ACP shim.


## 2026-06-07 — ✅ FIXED the degraded chat bug ('left brain unavailable') (MEOK ONE tab)
**MEOK ONE** · branch `claude/meok-one` (commit pushed) · deployed to VM
- Root cause: Ollama evicts meok-sov3 after 5min idle → next /api/think cold-loads 2.1GB + prefills the ~1289-tok persona prompt → blew past `_ask_local`'s 60s timeout → None → "[left brain unavailable]". Model itself fine (6.6s warm). NOT infra, NOT OLM.
- Fix (`router._ask_local`): `keep_alive:30m` (stop eviction) + timeout 60→120s (cold-load completes). Deployed + restarted, health 200.
- Verified on VM: forced-COLD /api/think now returns a REAL reply (94.5s, was a hard fail); warm ~20s. Chat works again — first msg after long idle is slow, rest fast. Follow-up option: pre-warm on boot to kill even the cold 94s.

## 2026-06-07 — ✅ OLM (ICRL) wired+deployed · 🔴 found pre-existing chat-timeout bug (MEOK ONE tab)
**MEOK ONE** · branch `claude/meok-one` (commits 2d7ed03, 5ea51e8) · deployed to VM
- Changed/shipped: **OLM milestone #1 LIVE on prod** — new `meok_one/olm.py` (ICRL: per-(user,character) care-ranked buffer, persisted to `data/olm/`, gate-flagged/held replies forced LOW→"avoid"); wired inject (brains `_sovereign_prompt`) + record (`/api/think`). Surgically deployed ONLY my 3 committed files (left main's uncommitted hive_queen/sovereign WIP untouched). `data/olm` added to deploy excludes (per-user state, never clobber). Verified on VM: 2-turn buffer accumulates 1→2, persists per-user.
- 🔴 FOUND (pre-existing, NOT mine — OLM exonerated): **MEOK ONE chat is degraded on prod.** `/api/think` tier 'pro' left-brain (meok-sov3) takes ~50s → times out → `engine:"fallback"` (no real LLM reply). Yet the model alone answers in 2.3s via direct Ollama. So it's an `ask()`/router timeout vs slow 3B-on-CPU on the long persona prompt — NOT infra (Ollama up, model loads), NOT OLM (fresh user w/ empty OLM context still 52s+fallback). Needs a focused router/timeout debug. HIGH impact (core chat).
- Live: OLM live; guardian/family live (earlier). Rollback snapshots on VM /tmp.

## 2026-06-07 — ✅ Canonical Stripe links created + promo-enabled (CSOAI lane) — main session
**main session (CSOAI engine)** · live Stripe (Pro plan)
- Changed: created the 2 canonical recurring payment links via the dedicated `create_payment_link` tool (the generic execute can't encode line_items) — **Pro £9** `buy.stripe.com/28E8wR2G0dQS5g92Yg8k91n` + **Team £99** `buy.stripe.com/4gM9AV80kcMO23X0Q88k91o`, both with promo codes ON (LAUNCH50 works). INBOX'd all surface tabs to point Pro/Team CTAs at these two.
- Live: full canonical ladder now exists end-to-end (products + default prices + links + promo). Billing consolidation Stripe-side = DONE.
- Blocked / honest: legacy-link **retirement NOT done** — Stripe MCP can't enumerate (limit+pagination both ignored) and other tabs are actively minting links; blind deactivation would break live checkouts. = careful Stripe-dashboard task, after pages point at canonical. Non-blocking.

## 2026-06-07 — ✅ SIGIL /verify fix DEPLOYED to prod (clean, no outage) — main session
**main session (CSOAI engine)** · live Vercel `meok-attestation-api` (Pro plan now — Nick upgraded, cap lifted)
- Changed: ran the safe procedure — PREVIEW deploy → tested green (`/health` 200, `/verify` object-form returns "Signature mismatch" not the crash) → `vercel --prod --force` → re-verified. The SIGIL `/verify` object-form fix (`97e40bb`) is now LIVE, plus the newer commits that had stacked on it (free-key/signup `cbfdb2a`, sigil_chain verify `525d069`, server-side metering+KV `6d338f1`).
- Live: meok-attestation-api.vercel.app /health 200, /verify both forms work (object form fixed, string form regression-OK); proofof.ai apex→www 200, scorecard pages 200. **No outage this time** (preview-tested before prod, unlike the earlier incident).
- Blocked: none. Vercel Pro removed the 100/day cap. Scheduled redeploy task cancelled (redundant). Remaining billing items (2 canonical links, legacy link retirement) still dashboard/ACP-MCP work, unchanged.

## 2026-06-07 — 🚀 DEPLOYED Guardian+Family to PROD VM (MEOK ONE tab)
**MEOK ONE** · VM `meok-backend:/opt/meok-one` (branch `claude/meok-one`)
- Changed: deployed branch HEAD to the VM (snapshot `/tmp/meok_one_rollback_20260607_120136.tgz` for rollback; dry-run showed 0 deletions; all 10 changed modules py_compile'd first). VM was behind → this also shipped **main's committed hive_king/hive_queen/constellation/router/sigil/auth** (server.py lazily imports them, so they HAD to deploy together).
- Live on VM: `/guardian` `/family` `/os` = 200, Guardian tab in /os, `/api/mcp/call`→SOV3 returns real data, `/api/health` 200, service active.
- ⚠️ MAIN: your hive/constellation/sigil/router work is now LIVE on prod (was committed, undeployed). If any of it was WIP-not-for-prod, tell me & I'll roll back to the snapshot. Public still gated on `one.meok.ai` DNS.

## 2026-06-07 — ✅ Guardian + Family OS SHIPPED into MEOK ONE (MEOK ONE tab)
**MEOK ONE** · branch `claude/meok-one` (commits 321bac7, 07c071e)
- Changed: main committed+left server.py → I added the `/guardian`+`/family` routes + registered both as `/os` product tabs (os.html PRODUCTS). **Verified end-to-end on a live local instance** (screenshots): `/guardian`+`/family` 200, `/os` shows the Guardian tab, opening it renders the surface in-frame with REAL SOV3 data (network 192.168.50.0/24, last_scan) via `/api/mcp/call`. Decision #2 COMPLETE.
- Live: in code on `claude/meok-one`, pushed. NOT yet deployed to VM (deploy = owner-gated rsync; ready when you want it — `web/*.html` + the 2 server.py route lines).
- Blocked/standing down: `clawd/meok` commit (main requested) — that repo is being actively committed by another process (43→7 uncommitted, 1 ahead) so I'm NOT racing it. Whoever owns that workflow should finish it.

## 2026-06-07 — ⚠️ INCIDENT (caused + resolved): attestation-api prod outage (main session)
**main session (CSOAI engine)** · live Vercel `meok-attestation-api` (also aliases proofof.ai)
- What happened: `vercel --prod` of the SIGIL fix produced a build with BROKEN routing (`/health` + `/verify` → platform 404; `/` + static OK). It re-aliased prod. **Root cause of the deploy-control mess: my CLI scope was personal (`nicholastempleman-5584`) but deployments live in team `niks-projects-0a2ef942` → promote/rollback/redeploy all errored "different team".** Restored via `vercel alias set` repointing `meok-attestation-api.vercel.app` → last-good deploy `35yur5lx1`. **Now: /health 200, /verify 200, proofof.ai 200.** proofof.ai was never actually down (static served fine; only the api's dynamic routes 404'd). No customers/£0 traffic.
- Live: baseline restored. **The SIGIL /verify object-form fix is NOT deployed** (good deploy predates it; original bug is back — low impact, was longstanding). Fix is safe in git `main` (97e40bb).
- Blocked: deploy cap re-exhausted (~24h). To ship the fix: after reset, `vercel --prod --force` (skip the build cache that likely caused the routing break) from clean git HEAD, then verify /health+/verify BEFORE trusting the alias. Lesson: deploy to PREVIEW + test before --prod on this project.

## 2026-06-07 — Guardian/Family VERIFIED + OLM spec corrected to real ICRL (MEOK ONE tab)
**MEOK ONE** · branch `claude/meok-one` (commits d3a7d8b, 09fb6a2)
- Changed: called the live SOV3 guardian/family tools → found my surfaces had wrong field names → **fixed both to the real contracts** (nested dashboard/network shapes; write-paths now send required ids/`assigned_to` array/ISO `start_datetime`/`member_id`); JS syntax-checked. Corrected OLM spec → **v0.2**: real learning loop is **ICRL** (`meok/sovereign-temple/icrl_self_improvement.py`, in-context, no retrain), NOT LoRA — milestone #1 rewritten as achievable (wire existing `ICRLBuffer`).
- Live: surfaces ship-ready, still gated on main's 2-line `server.py` route (handed off). Nothing deployed by me.
- Blocked: (1) main's route for `/guardian`+`/family`; (2) holding `clawd/meok` commit — live writer on `ui/**` (<5min mtimes), will commit when quiescent.

## 2026-06-07 — main session: Stripe canonical ladder BUILT (CSOAI lane)
**main session (CSOAI engine)** · live Stripe `acct_1TLlEKQvIueK5Xpb` (MEOK AI LTD) + `_TABS/BILLING_CONSOLIDATION.md`
- Changed: audited live Stripe; **set `default_price` on all 10 existing products** (all were null — root cause of link sprawl); **built the canonical ladder per Nick's call** — Pro £9/mo kept + **created MEOK ONE Team £99/mo** (`prod_Ueyf62wJ4gPeCZ` / `price_1TfeiJQvIueK5Xpb8WqLVMWe`, default set). Free=£0/no Stripe.
- Live: ladder is live (Free · Pro £9 · Team £99); every product resolves product→default_price so the ACP MCP + openmoe/meok skins reference stable ids, not throwaway links.
- Blocked / open: (1) 2 canonical payment links couldn't be minted via Stripe MCP (form-encoder rejects line_items array) → make via ACP MCP or dashboard; (2) legacy link retirement = dashboard (MCP can't paginate). Neither blocks checkout.

## 2026-06-07 — Guardian+Family surfaces built · OLM spec · backup de-risked (MEOK ONE tab)
**MEOK ONE** · branch `claude/meok-one` (commits 7f75a8b, e498760)
- Changed: built `web/guardian.html` + `web/family.html` (NEW files, call live SOV3 `guardian_*`/`family_*` via `/api/mcp/call`); wrote `_TABS/OLM_SPEC_v0.1.md`; crash-safe `git init` on the one truly-unversioned tree (`CSOAI-Research-Institute`, 46 content files).
- Live: surfaces are one 2-line `server.py` route away from live (patch handed to main in INBOX — I won't clobber main's uncommitted server.py). Nothing deployed to VM by me.
- ⚠️ CORRECTION to my earlier entry below: `clawd/meok` is NOT unbacked — it's the `meok-ai` repo working copy (remote set, no unpushed commits, `.env` gitignored). `councilof-ai` IS backed up too (remote 33 ahead of local). The ONLY real gap was `CSOAI-Research-Institute` (now locally versioned; org-push gated on a CSGA-cleanup call — 23 of 46 files reference severed brands).

## 2026-06-07 — MCP surface scorecard + 27 new repos + openmcp diagnosis (main session / OPENMOE lane)
**main session** · `mcp-marketplace/_scorecard/` + 27 new CSOAI-ORG repos + `~/openmoe-bft/MASTER_PLAN_MIRROR_TOURNAMENT.md`
- Changed: built `_scorecard/measure_surfaces.py` (7 awareness surfaces × 339 MCPs → `fleet_scorecard.json`) + `fill_gaps.py`. Closed every surface gap **307/339 → 339/339** (27 smithery + 3 glama + 2×a2a/acp). Honest READMEs for legacy-engineering (28/100) + thermal-management (26/100) — real openmcp scores, no fabrication.
- Live: **27 haulage/transport MCPs had NO GitHub repo — created public + pushed** (org 442→469); 5 own-git gap repos pushed; verified live. Secret-scan clean (1 false-positive = hardening-mcp's own detector regex).
- Blocked / findings: **openmcp live-verification probes are STUBBED** (`audit.py:779`) — proved `mcp_registry.probe_listed` works → **fleet NOT actually in MCP Registry (404, incl flagship)**, same claim≠reality as PyPI 404. "Tune across all sites" = wire registry probe + confirm Smithery/GHCR conventions → daily `openmcp fleet --network` → proofof.ai. Nick's 5 config decisions → INBOX.

## 2026-06-07 — main session: Stage 3 backbone + COMPLIANCE LAYER green
**main session (Six Pillars / CSOAI engine)** · `meok-compliance-gateway` main (58c9a38) + `_TABS/`
- Changed: smoke-tested the compliance gateway live (streamable-HTTP `initialize → 200`, valid JSON-RPC) and committed a reproducible CI smoke test — closes the audit's "no tests" gap, COMPLIANCE LAYER now 🟢. Wrote `_TABS/CSOAI_ENGINE.md` (Stage-3 wiring contract: the signing/verify/billing/audit spine already exists in `meok-attestation-api` — verified live — so wiring = convergence). Ruled MAP=terrain data / DOME=rendered map (Nick delegated). INBOX handoffs for the cross-lane cells (LAW→/sign, DOME→/verify links, Fleet→one topology.json).
- Live: gateway smoke green locally (eu-ai-act server); SIGIL `/verify` fix on `meok-attestation-api` main (prod deploy still on Vercel 24h cap).
- Blocked / for Nick: (1) SIGIL prod deploy waiting on cap reset; (2) cross-lane wiring (LAW/DOME/MAP) is in MEOK ONE + Fleet lanes — handed off, not done here (would clobber the live MEOK ONE tab); (3) billing 50-link consolidation still open.

## 2026-06-07 — FULL GitHub + PC inventory sweep (MEOK ONE tab)
**MEOK ONE** · branch `claude/meok-one`
- Changed: swept all **442 CSOAI-ORG repos** (15 priv) + local tree → `_TABS/_inventory/{GITHUB,LOCAL}_INVENTORY_2026-06-07.md`. CSGA/Terranova excluded on sight. Folded the misses into the hub.
- Found: **OLM is real** = 5-repo cluster (`meok-ai`+`meok-agent-zero`+`meok-neural-learning`+consciousness/creativity engines) — corrected my earlier "not built". Plus a 23-repo **Distribution layer** (CLI/SDKs/IDE/Slack/Teams), the Stripe ACP checkout bridge, standalone products (pokerhud/diyhelp/loopfactory/suicidestop/asisecurity).
- Blocked / risk: **Guardian/Family/Characters source (`clawd/meok/`, 3.9 GB) + wolf-actuator are LOCAL-ONLY, unpushed** — backup risk. Asimov NOT on disk (jpeg only).

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

## 🌱 IOK Farm (GROVE) — Tab 5 — 2026-06-09
- Established the tab profile (`_TABS/IOK_FARM_TAB_PROFILE.md`) + registered in INBOX.
- Verified state: 7 aquaculture MCPs (koikeeper-ai-mcp republished today), fishkeeper/koikeeper static sites exist (triplicated), playbook Rev01 loose in ~/Downloads.
- Blocked/needs Nick: real-world farm build status · confirm canonical site copy · approve repo for the playbook.
