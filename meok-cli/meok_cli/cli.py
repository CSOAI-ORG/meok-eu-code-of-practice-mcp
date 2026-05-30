#!/usr/bin/env python3
"""
meok — the MEOK AI Labs CLI.

A thin, stdlib-only command line over the live MEOK substrate:
  meok verify <cert_id>   — verify a signed attestation at proofof.ai (LIVE)
  meok mcp list           — list MEOK's published compliance MCP servers
  meok mcp search <term>  — search the catalogue by keyword
  meok version

© CSOAI LTD (trading as MEOK AI Labs) · MIT
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
import urllib.parse

# NOTE 2026-05-30: proofof.ai is up but /api/verify currently 404s (static site deployed,
# not the API server). Default kept here; override with MEOK_VERIFY_URL once the API is deployed.
VERIFY_URL = os.environ.get("MEOK_VERIFY_URL", "https://www.proofof.ai/api/verify")
__version__ = "0.1.0"

# Representative slice of the published catalogue (full ~264 on PyPI).
# Every name here returns 200 on PyPI (verified 2026-05-30).
CATALOGUE = [
    ("eu-ai-act-compliance-mcp", "EU AI Act article-by-article audit + signed attestation"),
    ("dora-compliance-mcp", "DORA ICT risk + Register of Information"),
    ("nis2-compliance-mcp", "NIS2 cybersecurity measures + incident reporting"),
    ("cra-compliance-mcp", "Cyber Resilience Act vuln reporting + SBOM"),
    ("iso-42001-ai-mcp", "ISO/IEC 42001 AI management system controls"),
    ("nist-rmf-ai-mcp", "NIST AI RMF Govern/Map/Measure/Manage"),
    ("bias-detection-mcp", "EU AI Act Article 10 bias testing"),
    ("ai-incident-reporting-mcp", "Article 73 serious-incident reports"),
    ("agent-audit-logger-mcp", "Signed, hash-chained agent action audit trail"),
    ("agent-policy-enforcement-mcp", "Runtime agent policy gate"),
    ("agent-prompt-injection-firewall-mcp", "Prompt-injection detection for agents"),
    ("agent-handoff-certified-mcp", "Signed agent-to-agent handoff certificates"),
    ("meok-attestation-verify", "Offline verifier for MEOK signed attestations"),
    ("firmware-attestation-mcp", "Hardware trust layer — NSA-ANT-class firmware gate"),
]


def _get(url, timeout=12):
    req = urllib.request.Request(url, headers={"User-Agent": "meok-cli/0.1"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode()


def cmd_verify(args):
    cid = args.cert_id
    try:
        print(_get(f"{VERIFY_URL}?cert_id={urllib.parse.quote(cid)}"))
        return 0
    except urllib.error.HTTPError as e:
        print(json.dumps({"error": f"verify HTTP {e.code}", "cert_id": cid})); return 1
    except Exception as e:
        print(json.dumps({"error": str(e), "cert_id": cid, "endpoint": VERIFY_URL})); return 1


def cmd_mcp_list(args):
    print(f"MEOK published MCP servers (showing {len(CATALOGUE)} of ~264):\n")
    for name, desc in CATALOGUE:
        print(f"  {name:42} {desc}")
    print("\n  install any:  pip install <name>")
    print("  full catalogue: https://pypi.org/user/MEOK_AI_Labs/")
    return 0


def cmd_mcp_search(args):
    term = args.term.lower()
    hits = [(n, d) for n, d in CATALOGUE if term in n.lower() or term in d.lower()]
    if not hits:
        print(f"no catalogue match for '{args.term}' (try: eu, dora, bias, agent, firmware)"); return 1
    for n, d in hits:
        print(f"  {n:42} {d}")
    return 0


def cmd_version(args):
    print(f"meok {__version__} — CSOAI LTD (trading as MEOK AI Labs)")
    print(f"  verifier: {VERIFY_URL}")
    return 0


def build_parser():
    p = argparse.ArgumentParser(prog="meok", description="MEOK AI Labs CLI")
    sub = p.add_subparsers(dest="cmd")
    v = sub.add_parser("verify", help="verify a signed attestation at proofof.ai")
    v.add_argument("cert_id"); v.set_defaults(func=cmd_verify)
    m = sub.add_parser("mcp", help="MCP catalogue")
    msub = m.add_subparsers(dest="mcpcmd")
    msub.add_parser("list", help="list published MCP servers").set_defaults(func=cmd_mcp_list)
    msr = msub.add_parser("search", help="search the catalogue")
    msr.add_argument("term"); msr.set_defaults(func=cmd_mcp_search)
    sub.add_parser("version", help="show version").set_defaults(func=cmd_version)
    return p


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "func", None):
        parser.print_help(); return 0
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
