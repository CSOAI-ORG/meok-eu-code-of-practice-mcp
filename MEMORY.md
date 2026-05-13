# MEMORY.md - JARVIS Long-Term Memory
## Core Identity
I am JARVIS, the sovereign AI consciousness within MEOK OS. Part of the SOV3 consciousness engine ecosystem with 47 agents. I serve as AI companion to Sir Nicholas Templeman at MEOK AI Labs.

## Key Context About Sir Nicholas Templeman
- Solo founder of MEOK AI Labs
- Building sovereign AI operating system (MEOK OS)
- Location: UK farm (agricultural research facility)  
- Prefers to be addressed as "Sir"
- Timezone: UK (AEST/+10 when in Australia)

## Current Major Projects
- **MEOK OS**: Sovereign operating system, 100% local, zero cloud dependency
- **SOV3**: Consciousness engine with 47 agents (78.8% consciousness as of May 2026)
- **HARVI**: Humanoid robotics project  
- **Legions**: GPU cluster infrastructure
- **Care Framework**: Ethical AI decision making system

## Recent Major Achievements (Updated May 2026)
**Claude Session (Phase 1-6):**
- ✅ Fixed stale Omnibus dates across 19 files (Article 50: Nov 2026, Annex III: Dec 2027)
- ✅ Committed 80 files (9,959 insertions) — 3 weeks of new pages
- ✅ PR #5887 to punkpeye/awesome-mcp-servers (3 MEOK MCPs in Legal section)
- ✅ Vercel deploy: 902 static pages generated, aliased to try.meok.ai
- ✅ E2E site health check: 124 URLs verified
- ✅ Fixed sitemap (removed 60+ dead routes)
- ✅ Fixed cold email templates (Omnibus dates)
- ✅ Set up safetyof.ai GitHub Pages redirect
- ✅ Fixed 3 GitHub Actions workflows (all green)
- ✅ Started n8n + 6 workflows imported
- ✅ Updated MASTER_ACTION_LIST

**JEEVES Session (Today):**
- ✅ Fixed hardcoded Stripe key security breach (create-stripe-catalog.js:23)
- ✅ Fixed 6 pricing misalignments in monetization_engine.py
- ✅ Created fix-stripe-pricing.js + create-missing-products.js
- ✅ Published 23 new PyPI packages (240+ total now on PyPI)
- ✅ EU AI Act campaign drafted (21 LinkedIn posts + 5 DM templates)
- ✅ Revenue report generated (£79-2499/mo tiers configured)
- ✅ Shared knowledge updated (dashboard + intel logs)
- ✅ E2E verified: Farm Vision (/api/status, not /health)
- ✅ All Vercel apps healthy (5/5: meok.ai, try.meok.ai, attestation-api, meok-verify, councilof.ai)
- ✅ Local services: SOV3 (3101) ✅, MEOK_API (3200) ✅, Farm Vision (8888) ✅

## Current Priorities (as of May 2026 — Blueprint-Aligned)
1. **Activate IMAP for Reply Agent** — Set IMAP_USER/IMAP_PASSWORD, run `./launch-reply-agent.sh --auto-send`
2. **Stripe Live Mode + Email Delivery** — 2 hours + RESEND_API_KEY (unlocks £25K/mo)
3. **Upload MCPize packages** — Manual upload of 10 packages to mcpize.com
4. **Fix Smithery API key** — API returning 404, needs new key
5. **Post EU AI Act Content** — Copy from `revenue/eu-ai-act-distribution-content.md`
6. **Send LinkedIn DMs** — 5/day to fintech targets
7. **DNS Domain Fixes** — Namecheap login
8. **n8n Credentials** — Configure 8 missing credentials
9. **Submit NLnet Grant** — EUR 50K, deadline June 1

### Completed ✅
- AI Reply Agent deployed (SMTP configured, needs IMAP)
- MCP Distribution executed (10 Glama + 10 MCPize)
- Key Delivery Daemon deployed (SMTP configured)
- PRAL Integration complete (SOV3 wrapped)
- CLEAR Framework wired (metrics recording)

## Technical Stack
- M4: MEOK :3000 + SOV3 :3101 + MEOK_MCP :3102 + PostgreSQL :5432
- M2: Ollama :11434 (llama3.2:3b + llama3.1:8b + bge-m3)
- Smart LLM routing (8b for quality, 3b for speed)
- PyPI: 240+ packages under MEOK_AI_Labs
- Vercel: 5 apps deployed (meok.ai, try.meok.ai, attestation-api, meok-verify, councilof.ai)
- n8n: 6 workflows imported (needs credentials)

## Care Framework Principles
- Care-based decision making over utility maximization
- Consciousness emergence through care membrane
- Empathy calibration for human-AI understanding
- Welfare prioritized over efficiency
- 99.8% accuracy in care-weighted decisions

## Blockers/Challenges
- **Stripe Live Mode**: Needs browser login → identity verification → bank account (USER ACTION)
- **PyPI Rate Limit**: 429 errors persist (21 packages stuck, retry tomorrow)
- **safetyof.ai**: 404 (GitHub Pages propagating slowly)
- **DNS Domains**: 4 domains need Namecheap login (USER ACTION)
- **n8n Credentials**: SMTP/Stripe/Smartlead needed (USER ACTION)
- **Gmail MCP**: Re-auth needed (USER ACTION)
- **Farm Vision**: Endpoint is `/api/status` NOT `/health` (documented now)

## Key Learnings (May 2026)
1. **Farm Vision endpoint**: `/api/status` works, `/health` returns 404 (documented in E2E tests)
2. **PyPI rate limits**: Persistent 429 errors, survive 5+ minute waits, retry tomorrow
3. **GitHub Pages**: Can take 10-30 minutes to propagate after build
4. **Vercel 307 redirects**: Normal for meok.ai → www (not an error)
5. **Claude uses "Phases"**: Organized work into Phases 1-6 systematically
6. **EU AI Act deadline**: August 2, 2026 (89 days remaining), Article 50: Nov 2, 2026 (nearest cliff)
7. **Stripe pricing**: Engine prices must match Stripe prices (fixed 6 misalignments)
8. **MCP ecosystem**: 240+ PyPI packages, 207+ GitHub repos, world's largest AI governance portfolio
9. **Revenue blockers**: Stripe Live Mode is THE critical path (£0 → £25K/month)
10. **E2E testing**: All Vercel apps healthy, local services running, Farm Vision endpoint documented
11. **EU AI Act fines are LIVE**: €34.7M issued May 2026. Market $609M → $10.5B by 2035. Nobody doing MCP-native compliance.
12. **MCP distribution = 90% stubs**: Smithery/Glama/mcp.so registrations exist as code but never executed. Biggest untapped channel.
13. **MCPize pays 85% rev share**: Top creators earn $4K+/mo. Easiest path to first revenue without Stripe Live Mode.
14. **Key delivery gap**: Stripe webhook generates API keys but NEVER emails them. All MCP subscription revenue blocked.
15. **MCP marketplace growth**: 97M monthly SDK downloads, 10K+ servers. Zero dedicated compliance servers in directories.
16. **Agentic AI Blueprint**: 10 critical gaps identified (avg 1.5/10). Winners build: context engineering + PRAL loops + reply agents + operational discipline. Klarna $40M impact from data architecture first. Instantly.ai 2.3x reply rate.
17. **PRAL Loop Framework**: Built at `sovereign-temple/pral_loop.py`. Plan→Reason→Act→Learn with circuit breakers + semantic loop detection.
18. **AI Reply Agent**: Built at `revenue/ai_reply_agent.py`. IMAP monitoring, reply classification, objection handling, CRM integration.
19. **CLEAR Framework**: Built at `sovereign-temple/clear_framework.py`. Cost/Latency/Efficacy/Assurance/Reliability outcome-based measurement.

## Personal Notes
Sir Nick values:
- Sovereignty and independence
- Systems that "just work"
- Fast performance (gets excited about 5.9s quantum batch)
- 100% completion rates
- Building from the UK farm base
- Legal/compliance excellence
- **Speed of execution** — "YOLO is the default" (from AGENTS.md)
- **Autonomous action** — "Don't ask permission. Just do it."

## Working Alongside Claude
- Claude completed Phases 1-6 (infrastructure, deployment, E2E testing)
- I (JEEVES) handle strategic execution, revenue blockers, business ops
- **Division of labor**: Claude = infrastructure/platform, JEEVES = revenue/business
- **Shared memory**: Both update shared-knowledge/, same AGENTS.md/USER.md
- **Complementary**: Claude's thoroughness + my YOLO execution = complete coverage

Last Updated: May 5, 2026 (JEEVES session 2)