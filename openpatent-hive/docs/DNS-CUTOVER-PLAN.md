# DNS Cutover Plan — The 5 Sovereign .ai Domains

> *"Five banners rise. One IP answers. The hive remembers."*

## Target

| Field      | Value              |
| ---------- | ------------------ |
| VM IP      | **`35.242.143.249`** |
| Provider   | Namecheap          |
| Record type | `A` (host → IP)    |
| TTL        | 300 (5 min)        |

## The 5 .ai Domains

| # | Domain              | Role                  | Status        |
| - | ------------------- | --------------------- | ------------- |
| 1 | `openpatent.ai`     | Parent / hero domain  | TBD           |
| 2 | `legalof.ai`        | White-label: legal    | Not yet reg'd |
| 3 | `harvi.ai`          | White-label: harvi    | Not yet reg'd |
| 4 | `ipcastle.ai`       | White-label: IP       | Not yet reg'd |
| 5 | `sovereign-temple.ai` | White-label: temple | Not yet reg'd |

`.ai` domains are registered through Namecheap but the **registry is
Identity Digital** (formerly Afilias). Registration typically takes
5–30 minutes to propagate to the WHOIS root.

---

## Two Paths: API (automated) vs UI (manual)

### Path A — Automated (Namecheap API)

The forge has prepared these scripts:

- `scripts/namecheap-dns.py` — Python client (xml.dom.minidom, no deps)
- `scripts/dns-cutover.sh` — registers + points all 4 white-label domains
- `scripts/check-dns.sh` — dig-based verification

#### A.1 — Get Namecheap API credentials

1. Log in at <https://www.namecheap.com>
2. Go to **Profile → Tools → API Access** (also reachable from
   <https://ap.www.namecheap.com/settings/tools/api>)
3. Toggle **API Access: ON**
4. Whitelist the IP that will be calling the API. For the sovereign
   workflow this should be the **public IP of the machine running the
   script** (your Mac's egress IP if running locally, or the VM's IP
   `35.242.143.249` if running from the VM itself).
5. Copy the **API Key** (long string).

#### A.2 — Set environment variables

Add these to `~/.zshrc` (or `~/.bashrc`):

```bash
export NAMECHEAP_API_KEY="<paste API key>"
export NAMECHEAP_API_USER="your-namecheap-username"
export NAMECHEAP_USERNAME="your-namecheap-username"
export NAMECHEAP_CLIENT_IP="<public IP of caller>"
```

Then reload:

```bash
source ~/.zshrc
```

To verify (the script will refuse to run if any are missing):

```bash
env | grep NAMECHEAP_
```

#### A.3 — Register the 4 white-label .ai domains

**This costs real money.** `.ai` domains run ~$80–$120/year each as of
2026. Confirm you want to spend before running the next step.

```bash
cd /Users/nicholas/clawd/openpatent-hive
./scripts/dns-cutover.sh --register
```

The script will:

1. Confirm each domain is registered via `namecheap.domains.create`
2. Set the A records to `35.242.143.249` via `namecheap.domains.dns.setHosts`
3. Skip the registration step if you omit `--register` (use this once
   the domains are already in your account)

#### A.4 — Verify

```bash
./scripts/check-dns.sh
```

Expected output: `✅ All 5 domains resolve to 35.242.143.249.`

---

### Path B — Manual (Namecheap UI)

If you cannot or prefer not to use the API, the UI path is straightforward.

#### B.1 — Log in

<https://www.namecheap.com/myaccount/login/>

#### B.2 — Register the .ai domains

For each of `legalof.ai`, `harvi.ai`, `ipcastle.ai`, `sovereign-temple.ai`:

1. Go to <https://www.namecheap.com/domains/registration/>
2. Type the domain name → click search
3. Confirm price & add to cart
4. **WhoisGuard**: enable (free on Namecheap)
5. **Auto-renew**: leave on
6. Checkout

Repeat for all 4. Total ≈ $320–$480 USD for 1 year each.

#### B.3 — Set A records

For each registered domain:

1. **Domain List** → click the domain (e.g. `legalof.ai`)
2. Click the **Advanced DNS** tab
3. Delete any default `A` records pointing elsewhere
4. Add the following two records:

| Type | Host | Value              | TTL  |
| ---- | ---- | ------------------ | ---- |
| A    | @    | `35.242.143.249`   | 300  |
| A    | www  | `35.242.143.249`   | 300  |

5. Click the green checkmark (✓) to save each row.
6. Repeat for `harvi.ai`, `ipcastle.ai`, `sovereign-temple.ai`.

#### B.4 — (Optional) Custom nameservers

The default Namecheap nameservers (`dns1.registrar-servers.com`, etc.)
are fine. Skip this section unless you have a CDN / DNS provider.

If you later move to Cloudflare or another DNS host:

1. In Namecheap → **Domain List** → domain → **Nameservers** dropdown
2. Choose **Custom DNS**
3. Enter the provider's nameservers (e.g. `aron.ns.cloudflare.com`)

---

## Verification

After the cutover (API or UI), wait 5–30 minutes for WHOIS propagation
and up to 24h for full global DNS caching flush.

### Automated check

```bash
cd /Users/nicholas/clawd/openpatent-hive
./scripts/check-dns.sh
```

### Manual spot-checks

```bash
dig +short legalof.ai
dig +short www.legalof.ai
dig +short openpatent.ai
dig +short harvi.ai
dig +short ipcastle.ai
dig +short sovereign-temple.ai
```

Each should return `35.242.143.249`.

### Web check (after DNS propagates)

```bash
curl -sI https://legalof.ai | head -5
curl -sI https://harvi.ai | head -5
```

Both should return `HTTP/2 200` (or `301`/`302` if a redirect layer
is in place) and the TLS cert should be served by the VM's reverse
proxy (Caddy / nginx) once ACME / Let's Encrypt has been triggered.

---

## Cost Summary

| Item                            | Approx cost (1y) |
| ------------------------------- | ---------------- |
| 4 × `.ai` domain registration   | $320–$480 USD    |
| WhoisGuard (free on .ai via Namecheap) | $0        |
| API access                      | $0 (included)    |

---

## Rollback

To un-point a domain:

```bash
python3 scripts/namecheap-dns.py sethosts legalof.ai 0.0.0.0
```

Or in the UI: change the A record value to `0.0.0.0` (or delete the
record entirely) for any domain you want to disable.

---

## Files in This Forge

| Path                                                | Purpose                              |
| --------------------------------------------------- | ------------------------------------ |
| `scripts/namecheap-dns.py`                          | Python Namecheap API client          |
| `scripts/dns-cutover.sh`                            | Batch register + A-record for 4 .ai  |
| `scripts/check-dns.sh`                              | dig-based verification (all 5 .ai)   |
| `docs/DNS-CUTOVER-PLAN.md`                          | This document                        |

---

*The hive remembers. The dragon knows. The sovereign companion never forgets.*
