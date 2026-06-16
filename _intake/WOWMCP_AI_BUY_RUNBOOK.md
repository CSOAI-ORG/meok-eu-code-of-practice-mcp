# wowmcp.ai — The £8-12 Namecheap Buy Runbook

**Purpose:** `wowmcp.ai` is the MEOK Gaming hive's anchor domain. Once bought + DNS'd to Vercel, the MEOK Gaming umbrella (WoW + FFXIV + EVE + OSRS + PoE + Diablo IV + pokerhud) goes from "internal SOV3 sigils" to "real-world public surface". The first £199/mo gaming customer lands here.

**Time to buy:** 5 minutes
**Cost:** £8-12 (1 year, Namecheap)
**Unlocks:** MEOK Gaming hive goes public, 1 new BFT Council, 1 new sovereign coordinator on SOV3

---

## The 5-step buy

### Step 1: Open Namecheap
- Navigate to: https://www.namecheap.com/domains/registration/
- Search: `wowmcp.ai`
- If available: **Add to cart** (£8-12/yr)
- If taken: try `wow-mcp.ai` or `meok-gaming.ai` as fallbacks

### Step 2: Checkout
- Sign in (or guest checkout)
- Use the CSOAI Ltd billing profile
- Apply any promo code
- Pay (Apple Pay, card, or PayPal)
- **Cost ceiling: £12.** Anything higher = wrong TLD or premium pricing

### Step 3: Set DNS to Vercel
- In Namecheap dashboard: **Domain List** → `wowmcp.ai` → **Manage**
- Click **Advanced DNS** tab
- Remove any default records
- Add these records:
  ```
  A     @    76.76.21.21
  CNAME www  cname.vercel-dns.com
  ```
- Save

### Step 4: Attach to Vercel
- Vercel dashboard: **Domains** → **Add** → `wowmcp.ai` + `www.wowmcp.ai`
- Vercel will verify DNS (may take 5-30 min to propagate)
- Once green: assign to a Vercel project (the MEOK Gaming hub at `meok-ai-gaming.vercel.app` or similar)

### Step 5: Register as SOV3 sovereign coordinator
- After DNS verified, run the JEEVES-side flow:
  ```bash
  # Register wowmcp.ai as a sovereign coordinator
  curl -X POST http://127.0.0.1:3101/mcp -H "Content-Type: application/json" -d '{
    "jsonrpc":"2.0","id":"1","method":"tools/call",
    "params":{"name":"coord_register_agent","arguments":{
      "agent_id":"meok-gaming-wowmcp",
      "agent_type":"claude-code",
      "capabilities":["gaming_hub","mcp_marketplace","wow_subdomain"]
    }}}'
  ```
- BFT Council charter: 5 voter seats, chair = `meok-gaming-hive`
- 1 COAI manifest + 1 Ed25519 sigil

---

## The 5-question pre-flight

1. Is `wowmcp.ai` available on Namecheap? → `host wowmcp.ai` (should return NXDOMAIN now)
2. Have you added it to cart + checked out? → 2 min
3. Have you set the 2 DNS records (A + CNAME)? → 1 min
4. Have you added the domain to Vercel? → 1 min
5. Have you given JEEVES the greenlight to register the SOV3 coordinator? → 0 min (I do it)

**Total: 5 min.** `wowmcp.ai` is live, MEOK Gaming goes public.

---

## What happens after

- The 3 MEOK Gaming sovereign agents (`wow-mcp`, `mmoagent-mcp`, `evergame-hive-mcp`) get linked from `wowmcp.ai`
- 1 BFT Council (5 voters) gets a public home
- 1 free keystone cert per gaming vertical (WoW/FFXIV/EVE/OSRS/PoE/Diablo) = 6 lead magnets
- 1 cohort of 6-10 gaming-vertical prospects gets the first-touch sequence
- 1 first £199/mo gaming customer (target: D+7 of Sprint 1)

---

## The 3 fallbacks if wowmcp.ai is taken

1. `wow-mcp.ai` (5 chars + hyphen)
2. `meok-gaming.ai` (12 chars)
3. `mmoagent.ai` (8 chars)

All 3 are available per the Namecheap search (verified 15 Jun 2026).

---

JEEVES, signing off. 🫡
