#!/usr/bin/env python3
"""Generate conversion-page static sites for Construction + Agriculture hives."""
from pathlib import Path

ROOT = Path("/Users/nicholas/clawd")

ACCENT = "#c9a84c"

DOMAINS = {
    "grabhire": {
        "domain": "grabhire.ai",
        "name": "GrabHire",
        "sector": "construction",
        "hero": "Hire verified labour & grab lorries in minutes, not days.",
        "sub": "From one-off grabs to full-site labour dispatch — instant quotes, compliant operatives, and same-day booking.",
        "features": [
            ("⚡ Instant quote", "Tell us the job size and get a fixed quote in under 60 seconds."),
            ("🛡 Verified operatives", "Every driver and labourer is CSCS/CPCS checked and insured."),
            ("📍 Same-day dispatch", "Local fleet matching means you can book for today or schedule ahead."),
            ("📑 Invoice & compliance", "Waste transfer notes, insurance certs and POs handled automatically."),
        ],
        "tiers": [
            ("Day Rate", "£250", "per day", ["1 operative + grab lorry", "8hr shift", "Digital dockets"], "Hire now"),
            ("Site Team", "£895", "per day", ["3 operatives + 2 vehicles", "Priority dispatch", "Account manager"], "Book a team"),
            ("Enterprise", "Custom", "POA", ["Dedicated fleet", "24/7 operations", "API / MCP access"], "Talk to sales"),
        ],
        "partner": {
            "title": "Partner with GrabHire",
            "blurb": "Plant-hire brokers, groundworkers and construction resellers earn recurring commission by referring jobs.",
            "benefits": [
                "10–15% commission on referred hires",
                "Co-branded booking portal",
                "Real-time job tracking dashboard",
                "Monthly BACS payouts",
            ],
        },
        "enterprise": {
            "title": "GrabHire for Enterprise",
            "blurb": "National contractors and housebuilders manage labour, plant and waste through one procurement layer.",
            "benefits": [
                "Multi-site fleet allocation",
                "Purchase-order and cost-code billing",
                "HSE-ready compliance pack",
                "SSO and dedicated support",
            ],
        },
        "mcps": [
            ("muckaway-ai-mcp.quote_job", "Get instant spoil-removal quotes from any construction workflow."),
            ("planthire-ai-mcp.book_equipment", "Book excavators, dumpers and plant directly through MCP."),
        ],
    },
    "muckaway": {
        "domain": "muckaway.ai",
        "name": "MuckAway",
        "sector": "construction",
        "hero": "Instant muckaway quotes. Zero phone calls.",
        "sub": "Enter your spoil type, access and volume. We match you to the nearest licensed tipper or grab lorry — and quote in seconds.",
        "features": [
            ("🧱 Any spoil type", "Clay, hardcore, green waste, asbestos-soil — matched to the right carrier."),
            ("🚛 Real-time fleet", "See available tippers and grabs near your postcode."),
            ("♻ Eco routing", "Choose landfill diversion or recycling yard routing with CO2 estimates."),
            ("📄 Digital waste notes", "Legally compliant waste transfer notes stored in your account."),
        ],
        "tiers": [
            ("Load", "£195", "per load", ["6-wheel tipper", "Up to 8 tonnes", "Digital docket"], "Book a load"),
            ("Grab", "£395", "per load", ["8-wheel grab lorry", "Self-loading arm", "Remote site access"], "Book a grab"),
            ("Site Account", "Custom", "POA", ["Multiple daily loads", "Waste audits", "API / MCP access"], "Talk to sales"),
        ],
        "partner": {
            "title": "MuckAway Partner Program",
            "blurb": "Groundworkers, demolition firms and skip brokers add muckaway to their service stack without owning wagons.",
            "benefits": [
                "10% recurring commission per load",
                "White-label quote widget",
                "Lead attribution dashboard",
                "Priority carrier allocation",
            ],
        },
        "enterprise": {
            "title": "MuckAway for Enterprise",
            "blurb": "Major civils and infrastructure projects move spoil at scale with guaranteed capacity and audit trails.",
            "benefits": [
                "Daily multi-load scheduling",
                "Waste carrier licence verification",
                "Environmental reporting pack",
                "Custom cost centres and PO matching",
            ],
        },
        "mcps": [
            ("muckaway-ai-mcp.quote_job", "Embed instant muckaway quotes in CRMs, spreadsheets or AI agents."),
        ],
    },
    "planthire": {
        "domain": "planthire.ai",
        "name": "PlantHire",
        "sector": "construction",
        "hero": "Book plant equipment on demand.",
        "sub": "Excavators, dumpers, rollers and telehandlers — live availability, operator hire, and delivery to site.",
        "features": [
            ("🔧 Live fleet", "See which machines are available now near your postcode."),
            ("👷 Operator included", "Add a CPCS operator with any machine in two clicks."),
            ("🚚 Delivery & collection", "Tracked transport to site, timed to your programme."),
            ("✅ Maintenance certs", "All LOLER / PUWERS documentation attached automatically."),
        ],
        "tiers": [
            ("Mini Digger", "£145", "per day", ["1.5 tonne micro digger", "Delivery extra", "Ideal for gardens"], "Book mini"),
            ("360 Excavator", "£295", "per day", ["13 tonne excavator", "Operator optional", "Large groundwork"], "Book excavator"),
            ("Enterprise", "Custom", "POA", ["Multi-machine account", "Cross-hire rates", "API / MCP access"], "Talk to sales"),
        ],
        "partner": {
            "title": "PlantHire Partner Program",
            "blurb": "Independent hire yards, brokers and plant resellers join our network to fill idle machines.",
            "benefits": [
                "15% commission on bookings",
                "Shared availability calendar",
                "Co-branded customer portal",
                "Fleet utilisation reports",
            ],
        },
        "enterprise": {
            "title": "PlantHire for Enterprise",
            "blurb": " Contractors and developers source plant across multiple sites with one account and consolidated billing.",
            "benefits": [
                "National machine allocation",
                "Programme-level scheduling",
                "Hire-vs-buy analytics",
                "SSO, approvals and reporting",
            ],
        },
        "mcps": [
            ("planthire-ai-mcp.book_equipment", "Reserve plant directly from project-management tools or AI agents."),
        ],
    },
    "fishkeeper": {
        "domain": "fishkeeper.ai",
        "name": "FishKeeper",
        "sector": "agriculture",
        "hero": "AI health checks for every tank and pond.",
        "sub": "Upload a photo, get an instant disease diagnosis, treatment guide and water-quality action plan.",
        "features": [
            ("📸 Photo diagnosis", "fishkeeper-ai-mcp.diagnose_disease identifies symptoms and suggests treatment."),
            ("🧪 Water tracking", "Log ammonia, nitrite, nitrate and pH to spot trends before fish suffer."),
            ("💊 Treatment planner", "Step-by-step medication, dosage and quarantine guidance."),
            ("🌐 Community data", "Anonymised pond-health benchmarking across the UK."),
        ],
        "tiers": [
            ("Hobby", "£9", "per month", ["Up to 3 tanks/ponds", "5 diagnoses / month", "Email support"], "Start free trial"),
            ("Pro", "£39", "per month", ["Unlimited ponds", "Unlimited diagnoses", "WhatsApp support"], "Start free trial"),
            ("Enterprise", "Custom", "POA", ["Multi-pond farms", "Sensor integrations", "Vet referrals"], "Talk to sales"),
        ],
        "partner": {
            "title": "FishKeeper Partner Program",
            "blurb": "Aquatic retailers, vets and pond-builders recommend FishKeeper and earn recurring revenue.",
            "benefits": [
                "20% recurring commission",
                "Branded diagnosis landing page",
                "Customer referral dashboard",
                "Co-marketing support",
            ],
        },
        "enterprise": {
            "title": "FishKeeper for Enterprise",
            "blurb": "Fish farms, aquaculture research centres and public aquariums monitor health at scale.",
            "benefits": [
                "Multi-pond health dashboards",
                "IoT sensor integrations",
                "Vet-issued treatment records",
                "Compliance and welfare reports",
            ],
        },
        "mcps": [
            ("fishkeeper-ai-mcp.diagnose_disease", "Run AI disease diagnosis from any aquarium app or workflow."),
        ],
    },
    "koikeeper": {
        "domain": "koikeeper.ai",
        "name": "KoiKeeper",
        "sector": "agriculture",
        "hero": "Premium water quality & care for koi ponds.",
        "sub": "Continuous water-quality monitoring, AI disease diagnosis and seasonal care calendars for serious koi keepers.",
        "features": [
            ("💧 Live water quality", "meok-koikeeper-ai-mcp.water_quality tracks pH, KH, ammonia and temperature."),
            ("🔬 Disease scanner", "Upload photos of lesions or behaviour for AI-assisted diagnosis."),
            ("📅 Care calendar", "Seasonal feeding, filter maintenance and treatment reminders."),
            ("🚨 Smart alerts", "Get notified the moment parameters drift outside safe koi ranges."),
        ],
        "tiers": [
            ("Starter", "£12", "per month", ["1 pond", "Manual water logs", "Email alerts"], "Start free trial"),
            ("Koi Pro", "£49", "per month", ["Unlimited ponds", "IoT sensor sync", "Priority chat"], "Start free trial"),
            ("Estate", "Custom", "POA", ["Multiple estates", "On-site support", "Vet network"], "Talk to sales"),
        ],
        "partner": {
            "title": "KoiKeeper Partner Program",
            "blurb": "Koi dealers, pond builders and aquatic vets offer clients premium water monitoring and care.",
            "benefits": [
                "20% recurring commission",
                "White-label pond reports",
                "Partner badge and listings",
                "Customer success playbooks",
            ],
        },
        "enterprise": {
            "title": "KoiKeeper for Enterprise",
            "blurb": "Koi farms, estates and show venues maintain water quality across dozens of ponds with SLAs.",
            "benefits": [
                "Multi-pond SLA monitoring",
                "Sensor gateway integrations",
                "Show-ready health certificates",
                "Dedicated account manager",
            ],
        },
        "mcps": [
            ("meok-koikeeper-ai-mcp.water_quality", "Pull live water-quality telemetry into dashboards or automations."),
        ],
    },
}


def shell(domain_key: str, page: str, title: str, description: str, body: str) -> str:
    cfg = DOMAINS[domain_key]
    domain = cfg["domain"]
    name = cfg["name"]
    nav_links = "".join(
        f'<a href="/{p}/" class="text-sm font-medium text-slate-300 hover:text-gold transition">{p.capitalize()}</a>'
        for p in ["pricing", "partner", "enterprise", "signup"]
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://{domain}/{page}">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            gold: '{ACCENT}',
            slate: {{
              950: '#0b0f19',
              900: '#0f172a',
              850: '#111827',
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    .text-gold {{ color: {ACCENT}; }}
    .bg-gold {{ background-color: {ACCENT}; }}
    .border-gold {{ border-color: {ACCENT}; }}
    .hover\:bg-gold-dark:hover {{ background-color: #b08d3d; }}
    .gradient-radial {{ background: radial-gradient(circle at 50% 0%, rgba(201,168,76,0.12), transparent 50%); }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 antialiased">
  <div class="gradient-radial">
    <nav class="border-b border-slate-800">
      <div class="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
        <a href="/" class="text-2xl font-extrabold tracking-tight">{name}<span class="text-gold">.ai</span></a>
        <div class="hidden md:flex items-center gap-6">
          {nav_links}
          <a href="/signup/" class="bg-gold text-slate-950 px-4 py-2 rounded-lg font-semibold hover:bg-gold-dark transition">Get started</a>
        </div>
        <a href="/signup/" class="md:hidden bg-gold text-slate-950 px-3 py-1.5 rounded-lg font-semibold text-sm">Start</a>
      </div>
    </nav>

    {body}

    <footer class="border-t border-slate-800 mt-20">
      <div class="max-w-6xl mx-auto px-6 py-10 grid md:grid-cols-3 gap-8 text-sm text-slate-400">
        <div>
          <p class="text-lg font-bold text-slate-100">{name}<span class="text-gold">.ai</span></p>
          <p class="mt-2">Part of MEOK AI Labs — CSOAI Ltd, UK 16939677.</p>
        </div>
        <div class="flex flex-col gap-2">
          <a href="/pricing/" class="hover:text-gold">Pricing</a>
          <a href="/partner/" class="hover:text-gold">Partners</a>
          <a href="/enterprise/" class="hover:text-gold">Enterprise</a>
          <a href="/signup/" class="hover:text-gold">Sign up</a>
        </div>
        <div>
          <p>hello@meok.ai</p>
          <p class="mt-2">100% Nick Templeman · Sovereign UK infrastructure.</p>
        </div>
      </div>
      <div class="max-w-6xl mx-auto px-6 pb-8 text-xs text-slate-500 flex flex-wrap gap-4">
        <a href="https://meok.ai/privacy" class="hover:text-gold">Privacy</a>
        <a href="https://meok.ai/terms" class="hover:text-gold">Terms</a>
        <a href="https://meok.ai/cookies" class="hover:text-gold">Cookies</a>
        <span>© 2026 {name}.ai</span>
      </div>
    </footer>
  </div>
</body>
</html>
"""


def cta_section(domain_key: str, primary_text: str = "Get started", secondary_text: str = "Talk to sales") -> str:
    cfg = DOMAINS[domain_key]
    return f"""
    <section class="max-w-4xl mx-auto px-6 py-16 text-center">
      <h2 class="text-3xl md:text-4xl font-bold">Ready to make {cfg['name']} work for you?</h2>
      <p class="mt-4 text-slate-400">Start a free trial, request a demo, or apply to become a partner.</p>
      <div class="mt-8 flex flex-col sm:flex-row gap-4 justify-center">
        <a href="/signup/" class="bg-gold text-slate-950 px-8 py-3 rounded-xl font-bold text-lg hover:bg-gold-dark transition">{primary_text}</a>
        <a href="/enterprise/" class="border border-slate-600 text-slate-100 px-8 py-3 rounded-xl font-semibold hover:border-gold hover:text-gold transition">{secondary_text}</a>
      </div>
    </section>
    """


def index_page(domain_key: str) -> str:
    cfg = DOMAINS[domain_key]
    features = "".join(
        f"""<div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 hover:border-gold/40 transition">
          <h3 class="text-xl font-bold text-gold">{f[0]}</h3>
          <p class="mt-3 text-slate-400">{f[1]}</p>
        </div>"""
        for f in cfg["features"]
    )
    mcp_cards = "".join(
        f"""<div class="bg-slate-900 border border-slate-800 rounded-2xl p-6">
          <code class="text-gold font-mono text-sm">{m[0]}</code>
          <p class="mt-2 text-slate-400">{m[1]}</p>
        </div>"""
        for m in cfg["mcps"]
    )
    body = f"""
    <section class="max-w-6xl mx-auto px-6 pt-16 pb-12 text-center">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-gold/30 bg-gold/10 text-gold text-xs font-semibold tracking-wide uppercase">
        AI-powered · MCP-ready · UK-built
      </div>
      <h1 class="mt-6 text-4xl md:text-6xl font-extrabold tracking-tight">{cfg['hero']}</h1>
      <p class="mt-6 text-lg md:text-xl text-slate-400 max-w-2xl mx-auto">{cfg['sub']}</p>
      <div class="mt-10 flex flex-col sm:flex-row gap-4 justify-center">
        <a href="/pricing/" class="bg-gold text-slate-950 px-8 py-4 rounded-xl font-bold text-lg hover:bg-gold-dark transition">See pricing</a>
        <a href="/signup/" class="border border-slate-600 text-slate-100 px-8 py-4 rounded-xl font-semibold hover:border-gold hover:text-gold transition">Start free trial</a>
      </div>
    </section>

    <section class="max-w-6xl mx-auto px-6 py-16">
      <h2 class="text-2xl md:text-3xl font-bold text-center mb-10">Built for speed, compliance and scale</h2>
      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
        {features}
      </div>
    </section>

    <section class="max-w-6xl mx-auto px-6 py-16">
      <div class="bg-slate-900 border border-slate-800 rounded-3xl p-8 md:p-12">
        <div class="md:flex md:items-center md:justify-between gap-8">
          <div class="md:w-2/3">
            <h2 class="text-2xl md:text-3xl font-bold">Connect via MCP</h2>
            <p class="mt-4 text-slate-400">{cfg['name']} exposes flagship tools as Model Context Protocol servers. Trigger quotes, bookings, diagnosis or water-quality checks from any MCP client.</p>
          </div>
          <div class="md:w-1/3 mt-6 md:mt-0">
            <a href="/enterprise/" class="block text-center bg-gold text-slate-950 px-6 py-3 rounded-xl font-bold hover:bg-gold-dark transition">Request MCP access</a>
          </div>
        </div>
        <div class="grid md:grid-cols-2 gap-6 mt-10">
          {mcp_cards}
        </div>
      </div>
    </section>

    {cta_section(domain_key)}
    """
    return shell(domain_key, "", f"{cfg['name']} — AI-powered {cfg['sector']} booking", cfg['sub'], body)


def pricing_page(domain_key: str) -> str:
    cfg = DOMAINS[domain_key]
    cards = "".join(
        f"""<div class="{'border-gold ring-1 ring-gold' if i==1 else 'border-slate-800'} bg-slate-900 border rounded-2xl p-8 flex flex-col">
          <p class="text-sm font-semibold text-gold uppercase tracking-wide">{t[0]}</p>
          <div class="mt-4 flex items-baseline gap-1">
            <span class="text-4xl font-extrabold">{t[1]}</span>
            <span class="text-slate-400">{t[2]}</span>
          </div>
          <ul class="mt-6 space-y-3 text-slate-300 flex-1">
            {''.join(f'<li class="flex gap-2"><span class="text-gold">✓</span><span>{item}</span></li>' for item in t[3])}
          </ul>
          <a href="/signup/" class="mt-8 block text-center bg-gold text-slate-950 px-6 py-3 rounded-xl font-bold hover:bg-gold-dark transition">{t[4]}</a>
        </div>"""
        for i, t in enumerate(cfg["tiers"])
    )
    body = f"""
    <section class="max-w-6xl mx-auto px-6 pt-16 pb-8 text-center">
      <h1 class="text-4xl md:text-5xl font-extrabold">Simple, transparent pricing</h1>
      <p class="mt-4 text-lg text-slate-400">Start small, scale as your operation grows.</p>
    </section>
    <section class="max-w-5xl mx-auto px-6 py-10">
      <div class="grid md:grid-cols-3 gap-6">
        {cards}
      </div>
      <p class="mt-8 text-center text-sm text-slate-500">All prices exclude VAT. Enterprise plans include dedicated onboarding and MCP access.</p>
    </section>
    {cta_section(domain_key, "Sign up now", "Become a partner")}
    """
    return shell(domain_key, "pricing", f"Pricing — {cfg['name']}", f"Transparent pricing for {cfg['name']}.ai. Instant quotes, flexible tiers and enterprise procurement.", body)


def form_html(action: str, fields: list, submit: str) -> str:
    inputs = ""
    for label, name, type_, placeholder in fields:
        if type_ == "select":
            opts = "".join(f'<option>{o}</option>' for o in placeholder)
            inputs += f"""<label class="block text-sm font-medium text-slate-300">{label}
              <select name="{name}" class="mt-1 block w-full rounded-lg bg-slate-950 border border-slate-700 px-4 py-3 focus:border-gold focus:ring-gold">
                {opts}
              </select>
            </label>"""
        else:
            inputs += f"""<label class="block text-sm font-medium text-slate-300">{label}
              <input type="{type_}" name="{name}" placeholder="{placeholder}" class="mt-1 block w-full rounded-lg bg-slate-950 border border-slate-700 px-4 py-3 focus:border-gold focus:ring-gold" required>
            </label>"""
    return f"""
    <form action="{action}" method="post" enctype="text/plain" class="space-y-5" onsubmit="this.action='mailto:hello@meok.ai?subject='+encodeURIComponent('New {submit} submission from '+this.email.value)+'&body='+encodeURIComponent(Array.from(new FormData(this)).map(([k,v])=>k+': '+v).join('\\n')); return true;">
      {inputs}
      <button type="submit" class="w-full bg-gold text-slate-950 px-6 py-3 rounded-xl font-bold hover:bg-gold-dark transition">{submit}</button>
      <p class="text-xs text-slate-500">We will reply within one business day. No spam, no real charges until the flow is tested.</p>
    </form>
    """


def signup_page(domain_key: str) -> str:
    cfg = DOMAINS[domain_key]
    body = f"""
    <section class="max-w-xl mx-auto px-6 pt-16 pb-8">
      <h1 class="text-3xl md:text-4xl font-extrabold text-center">Start your {cfg['name']} account</h1>
      <p class="mt-4 text-center text-slate-400">Enter your details and we will set up your trial or enterprise demo.</p>
      <div class="mt-10 bg-slate-900 border border-slate-800 rounded-2xl p-8">
        {form_html('#', [
            ('Full name', 'name', 'text', 'Your name'),
            ('Work email', 'email', 'email', 'you@company.com'),
            ('Company / site name', 'company', 'text', 'Acme Construction Ltd'),
            ('Phone', 'phone', 'tel', '+44 7700 000000'),
            ('Plan', 'plan', 'select', ['Starter / Day rate', 'Pro / Site team', 'Enterprise']),
        ], 'Create account')}
      </div>
    </section>
    """
    return shell(domain_key, "signup", f"Sign up — {cfg['name']}", f"Create a {cfg['name']}.ai account. Free trial, enterprise demo and partner applications.", body)


def partner_page(domain_key: str) -> str:
    cfg = DOMAINS[domain_key]
    benefits = "".join(f"<li class='flex gap-3'><span class='text-gold font-bold'>✓</span><span>{b}</span></li>" for b in cfg["partner"]["benefits"])
    body = f"""
    <section class="max-w-6xl mx-auto px-6 pt-16 pb-8 md:flex md:gap-12">
      <div class="md:w-1/2">
        <h1 class="text-4xl md:text-5xl font-extrabold">{cfg['partner']['title']}</h1>
        <p class="mt-6 text-lg text-slate-400">{cfg['partner']['blurb']}</p>
        <ul class="mt-8 space-y-4 text-slate-300">
          {benefits}
        </ul>
      </div>
      <div class="md:w-1/2 mt-10 md:mt-0">
        <div class="bg-slate-900 border border-slate-800 rounded-2xl p-8">
          <h2 class="text-2xl font-bold mb-6">Apply now</h2>
          {form_html('#', [
              ('Full name', 'name', 'text', 'Your name'),
              ('Work email', 'email', 'email', 'you@company.com'),
              ('Company', 'company', 'text', 'Your company'),
              ('Website', 'website', 'url', 'https://example.com'),
              ('Partner type', 'type', 'select', ['Referrer / Affiliate', 'Reseller', 'Integration partner', 'Hire yard / Supplier']),
          ], 'Apply to partner')}
        </div>
      </div>
    </section>
    {cta_section(domain_key, "Join partner program", "View pricing")}
    """
    return shell(domain_key, "partner", f"Partner program — {cfg['name']}", f"Become a {cfg['name']}.ai partner. Commissions, co-branding and referral dashboards.", body)


def enterprise_page(domain_key: str) -> str:
    cfg = DOMAINS[domain_key]
    benefits = "".join(f"<li class='flex gap-3'><span class='text-gold font-bold'>✓</span><span>{b}</span></li>" for b in cfg["enterprise"]["benefits"])
    body = f"""
    <section class="max-w-6xl mx-auto px-6 pt-16 pb-8 md:flex md:gap-12">
      <div class="md:w-1/2">
        <h1 class="text-4xl md:text-5xl font-extrabold">{cfg['enterprise']['title']}</h1>
        <p class="mt-6 text-lg text-slate-400">{cfg['enterprise']['blurb']}</p>
        <ul class="mt-8 space-y-4 text-slate-300">
          {benefits}
        </ul>
      </div>
      <div class="md:w-1/2 mt-10 md:mt-0">
        <div class="bg-slate-900 border border-slate-800 rounded-2xl p-8">
          <h2 class="text-2xl font-bold mb-6">Request a demo</h2>
          {form_html('#', [
              ('Full name', 'name', 'text', 'Your name'),
              ('Work email', 'email', 'email', 'you@company.com'),
              ('Company', 'company', 'text', 'Your company'),
              ('Number of sites / ponds', 'sites', 'text', 'e.g. 12'),
              ('What are you solving?', 'details', 'text', 'Tell us briefly'),
          ], 'Request demo')}
        </div>
      </div>
    </section>
    {cta_section(domain_key, "Get enterprise pricing", "View partner program")}
    """
    return shell(domain_key, "enterprise", f"Enterprise — {cfg['name']}", f"Enterprise procurement, fleet management and multi-site {cfg['name']}.ai deployment.", body)


VERCEL_JSON = """{
  "outputDirectory": ".",
  "cleanUrls": true,
  "trailingSlash": false,
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {"key": "X-Content-Type-Options", "value": "nosniff"},
        {"key": "X-Frame-Options", "value": "SAMEORIGIN"}
      ]
    }
  ]
}
"""

ROBOTS_TXT = "User-agent: *\nAllow: /\nSitemap: https://placeholder/sitemap.xml\n"


def write_site(key: str):
    cfg = DOMAINS[key]
    base = ROOT / f"{key}-deploy"
    base.mkdir(exist_ok=True)
    pages = {
        "index.html": index_page(key),
        "pricing/index.html": pricing_page(key),
        "signup/index.html": signup_page(key),
        "partner/index.html": partner_page(key),
        "enterprise/index.html": enterprise_page(key),
    }
    for path, html in pages.items():
        target = base / path
        target.parent.mkdir(exist_ok=True)
        target.write_text(html, encoding="utf-8")
    (base / "vercel.json").write_text(VERCEL_JSON, encoding="utf-8")
    robots = ROBOTS_TXT.replace("placeholder", cfg["domain"])
    (base / "robots.txt").write_text(robots, encoding="utf-8")
    print(f"Wrote {base} ({len(pages)} pages)")


if __name__ == "__main__":
    for key in DOMAINS:
        write_site(key)
    print("Done. Ready for deployment.")
