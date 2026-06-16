# MEOK_MASTER_API_KEY — The 1-Keystroke Setup

**Purpose:** The `MEOK_MASTER_API_KEY` is the master key for the keystone's `POST /provision` endpoint. With this key set, you can mint customer-scoped API keys via the keystone's provisioning flow. The customer keys then unlock the 4 paywalled MCP tools: DORA audit, UK AI Bill sign, Annex IV docs, full audit report.

**Time to set:** 5 minutes
**Cost:** £0
**Unlocks:** 4 paywalled MCP tools (the £199/mo + £4,950 customer conversion path)

---

## The 5-step setup

### Step 1: Open the Vercel dashboard
- Navigate to: https://vercel.com/dashboard
- Find the project: `meok-attestation-api`
- Click: **Settings** → **Environment Variables**

### Step 2: Add the master key
- **Key:** `MEOK_MASTER_API_KEY`
- **Value:** 32-character hex string (mint your own — `openssl rand -hex 16` gives 32 chars, e.g. `a1b2c3d4e5f6...7890`)
- **Environment:** Production, Preview, Development (all 3)

### Step 3: Save + redeploy
- Click **Save**
- Vercel will auto-redeploy (or click **Deployments** → **Redeploy** on the latest)
- The keystone now reads `MEOK_MASTER_API_KEY` on every request

### Step 4: Verify the keystone accepts the key
- `curl -X POST https://meok-attestation-api.vercel.app/provision -H "X-Master-Key: <your-key-here>" -H "Content-Type: application/json" -d '{"email":"<test>@meok.ai","tier":"pro"}'`
- Expected: `{"customer_key":"<new-hex>","tier":"pro","valid_until":"2027-06-15"}`

### Step 5: Test the 4 paywalled MCP tools
- With the customer key, the 4 tools become available:
  - `dora-compliance-mcp.audit_all_pillars`
  - `meok-eu-ai-act-compliance-mcp.sign_uk_ai_bill`
  - `meok-eu-ai-act-compliance-mcp.generate_annex_iv_docs`
  - `meok-eu-ai-act-compliance-mcp.generate_full_audit_report`

---

## What changes when MEOK_MASTER_API_KEY is set

- **Before:** the 4 paywalled MCP tools return 402 Payment Required
- **After:** the 4 paywalled MCP tools become signed attestations, chargeable to the customer key

## The 3-arg signature

```bash
# Mint a customer key (one keystroke)
curl -X POST https://meok-attestation-api.vercel.app/provision \
  -H "X-Master-Key: $MEOK_MASTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email":"customer@co.com","tier":"pro"}'
# Returns: {"customer_key":"...","tier":"pro","valid_until":"..."}

# Use the customer key for a paywalled tool
curl -X POST https://meok-attestation-api.vercel.app/mcp \
  -H "X-Customer-Key: <customer_key>" \
  -H "Content-Type: application/json" \
  -d '{"tool":"dora-compliance-mcp.audit_all_pillars","arguments":{...}}'
# Returns: signed attestation with verify URL
```

---

## The 5-question pre-flight (per the morning-rundown skill)

1. Did you open the Vercel dashboard for `meok-attestation-api`? → 30 sec
2. Did you click Settings → Environment Variables? → 10 sec
3. Did you mint a 32-char hex (openssl rand -hex 16)? → 10 sec
4. Did you paste it as `MEOK_MASTER_API_KEY` in all 3 environments? → 30 sec
5. Did you click Save? → 10 sec
6. Did Vercel auto-redeploy? → wait 30 sec

**Total: 2 min.** The keystone's `POST /provision` endpoint is now armed.

---

JEEVES, signing off. 🫡
