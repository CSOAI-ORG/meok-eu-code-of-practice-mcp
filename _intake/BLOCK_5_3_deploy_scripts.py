#!/usr/bin/env python3
"""BLOCK 5.3: Deploy scripts (cp iCloud → meok-ai/ui for all 29 pages).
Also writes a deploy-run.sh script that does the actual cp once Vercel WAF clears.
"""
import os, json
from datetime import datetime

DEST_BASE = "/Users/nicholas/clawd/meok-ai/ui/src/app"
ICLOUD_BASE = "/Users/nicholas/Library/Mobile Documents/com~apple~CloudDocs/clawdbot-shared/mcp-staging"
NOW = datetime.now().isoformat()

# Map iCloud directories → app subpaths
DEPLOY_MAP = {
    # EU CoP main page (already exists)
    "eu-code-of-practice/page.tsx": "eu-code-of-practice/page.tsx",
    # 3 EU CoP sub-pages (Day 3)
    "eu-code-of-practice-subpages/article-50-marking/page.tsx": "eu-code-of-practice/article-50-marking/page.tsx",
    "eu-code-of-practice-subpages/code-of-practice-2nd-draft/page.tsx": "eu-code-of-practice/code-of-practice-2nd-draft/page.tsx",
    "eu-code-of-practice-subpages/article-50-deepfake/page.tsx": "eu-code-of-practice/article-50-deepfake/page.tsx",
    # 5 vertical industry pages (Day 3)
    "verticals-and-comparisons/vertical-fintech/page.tsx": "for-fintech/page.tsx",
    "verticals-and-comparisons/vertical-care-homes/page.tsx": "for-care-homes/page.tsx",
    "verticals-and-comparisons/vertical-edtech/page.tsx": "for-edtech/page.tsx",
    "verticals-and-comparisons/vertical-saas/page.tsx": "for-saas/page.tsx",
    "verticals-and-comparisons/vertical-healthcare/page.tsx": "for-healthcare/page.tsx",
    # 7 comparison pages (Day 3)
    "comparisons/vs-vanta/page.tsx": "vs/vanta/page.tsx",
    "comparisons/vs-drata/page.tsx": "vs/drata/page.tsx",
    "comparisons/vs-arthur-ai/page.tsx": "vs/arthur-ai/page.tsx",
    "comparisons/vs-credo-ai/page.tsx": "vs/credo-ai/page.tsx",
    "comparisons/vs-holistic-ai/page.tsx": "vs/holistic-ai/page.tsx",
    "comparisons/vs-nevermined/page.tsx": "vs/nevermined/page.tsx",
    "comparisons/vs-regen-network/page.tsx": "vs/regen-network/page.tsx",
    # 8 empire pages (Day 4)
    "4-surface-empire/empire/page.tsx": "empire/page.tsx",
    "4-surface-empire/csoai-org/page.tsx": "csoai-org/page.tsx",
    "4-surface-empire/openmoe-ai/page.tsx": "openmoe-ai/page.tsx",
    "4-surface-empire/openpatent-ai/page.tsx": "openpatent-ai/page.tsx",
    "4-surface-empire/by-numbers/page.tsx": "by-numbers/page.tsx",
    "4-surface-empire/manifesto/page.tsx": "manifesto/page.tsx",
    "4-surface-empire/nav/page.tsx": "nav/page.tsx",
    "4-surface-empire/press/page.tsx": "press/page.tsx",
    # 5 lead-magnet pages (Day 5)
    "lead-magnets/for-monzo/page.tsx": "for/monzo/page.tsx",
    "lead-magnets/for-cera-care/page.tsx": "for/cera-care/page.tsx",
    "lead-magnets/for-stitch/page.tsx": "for/stitch/page.tsx",
    "lead-magnets/for-verisure/page.tsx": "for/verisure/page.tsx",
    "lead-magnets/for-parsa/page.tsx": "for/parsa/page.tsx",
}

# Write the deploy script
script_lines = [
    "#!/usr/bin/env bash",
    f"# Deploy script — generated {NOW}",
    "# Run this after Vercel WAF cooldown clears (expected ~48h from 13 Jun 14:00 BST)",
    "# Usage: bash deploy-all.sh",
    "",
    f"DEST_BASE=\"{DEST_BASE}\"",
    f"ICLOUD_BASE=\"{ICLOUD_BASE}\"",
    "",
    "echo '=== DEPLOYING 29+ PAGES ==='",
    "total=0",
]

for src, dest in DEPLOY_MAP.items():
    src_path = f"$ICLOUD_BASE/{src}"
    dest_path = f"$DEST_BASE/{dest}"
    dir_part = dest.rsplit("/", 1)[0] if "/" in dest else ""
    if dir_part:
        script_lines.append(f"mkdir -p $DEST_BASE/{dir_part}")
    script_lines.append(f"cp {src_path} {dest_path}")
    script_lines.append(f"echo '  ✓ {src} → {dest}'")
    script_lines.append("total=$((total + 1))")

script_lines.append("")
script_lines.append("echo '=== ALL DONE ==='")
script_lines.append(f"echo 'Deployed $total pages'")

script_content = "\n".join(script_lines)
script_path = "/Users/nicholas/clawd/_intake/deploy-all.sh"
with open(script_path, "w") as f:
    f.write(script_content)
os.chmod(script_path, 0o755)

# Write the deployment manifest
manifest_path = "/Users/nicholas/clawd/_intake/DEPLOY_MANIFEST.json"
deploy_data = {
    "generated_at": NOW,
    "dest_base": DEST_BASE,
    "icloud_base": ICLOUD_BASE,
    "total_pages": len(DEPLOY_MAP),
    "status": "STAGED (awaiting Vercel WAF cooldown)",
    "waf_cooldown_since": "2026-06-13T14:00:00+01:00",
    "expected_clear_time": "2026-06-15T14:00:00+01:00",
    "pages": {k: v for k, v in DEPLOY_MAP.items()},
}
with open(manifest_path, "w") as f:
    json.dump(deploy_data, f, indent=2, sort_keys=True)

print(f"=== BLOCK 5.3: Deploy scripts ===")
print(f"  Script: {script_path}")
print(f"  Manifest: {manifest_path}")
print(f"  Total pages: {len(DEPLOY_MAP)}")
print(f"  Status: STAGED (awaiting Vercel WAF cooldown)")
