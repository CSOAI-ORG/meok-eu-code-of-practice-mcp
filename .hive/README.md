# CSOAI Hive — Autonomic Nervous System

The Hive is Phase 1 of the Living Ecosystem Blueprint: a self-organizing,
self-healing automation layer for the CSOAI/SOV3/MEOK ONE empire.

## What it does

| Agent | Responsibility | Cadence |
|---|---|---|
| **Sensor** (`hive_sensor.py`) | Scans TODO, blocker, quality, and ready-to-post files across the empire, classifies tasks by router and priority, and emits a living task queue. | Every 15 min |
| **Healer** (`service_healer.py`) | Probes critical service endpoints and restarts anything that is down, with strike/cooldown logic to avoid fighting launchd. | Every 5 min |
| **Quality Manager** (`quality_manager.py`) | Grades repo health per tree (dirty files, tests, placeholders/secrets) and writes a JSON report. | Hourly |
| **Publish Manager** (`publish_manager.py`) | Stages social posts from READY_TO_POST and SOCIAL_BLITZ, queues them, and publishes via Buffer API or Kimi WebBridge when enabled. | Every 30 min |
| **Notifier** (`hive_notify.py`) | Shared notification dispatcher used by all agents: email (SMTP), Discord, Slack, generic webhook, macOS alerts. | On demand |
| **Remediation Generator** (`remediation_generator.py`) | Converts quality, E2E, and domain audit findings into `.hive/tasks/TODO_remediation.md`. | Every 6 h |
| **Test Fleet Manager** (`test_fleet_manager.py`) | Runs configured test suites (E2E, pytest) and aggregates pass/fail into a JSON report. | Daily |
| **Secrets Inventory** (`secrets_inventory.py`) | Scans `.env*` files for placeholders and missing required secrets. | Every 6 h |
| **Dashboard** (`dashboard/index.html`) | Static web UI for service health, quality grades, task queue, test fleet, secrets, and publish queue. | http://localhost:3800/.hive/dashboard/ |

## Layout

```
.hive/
├── config.yaml              # Single source of truth for services, sensors, quality gates
├── scripts/
│   ├── generate_launchd.py  # Render launchd plists from config.yaml
│   ├── load_launchd.py      # Install and load agents
│   ├── hive_sensor.py       # Task/signal sensor
│   ├── service_healer.py    # Service health & restart
│   └── quality_manager.py   # Quality grading
├── launchd/
│   └── ai.csoai.*.plist     # launchd agent definitions
├── dashboard/
│   └── index.html           # Static Hive dashboard
├── logs/                    # Runtime logs (gitignored)
└── tasks/                   # Runtime task queues (gitignored)
    ├── publish_queue.jsonl  # Staged social posts
    └── TODO_remediation.md  # Auto-generated remediation tasks
```

## Quick start

```bash
cd ~/clawd

# Regenerate launchd plists after config changes
python3 .hive/scripts/generate_launchd.py

# Install and load all agents
python3 .hive/scripts/load_launchd.py

# Run agents manually
python3 .hive/scripts/hive_sensor.py
python3 .hive/scripts/service_healer.py
python3 .hive/scripts/quality_manager.py
python3 .hive/scripts/publish_manager.py
python3 .hive/scripts/remediation_generator.py
python3 .hive/scripts/test_fleet_manager.py
python3 .hive/scripts/secrets_inventory.py
python3 .hive/scripts/quorum_sensor.py
curl -X POST http://127.0.0.1:3900/emit -H "Content-Type: application/json" -d '{"channel":"mcp.queen.gold","agent_id":"sigil","payload":{}}'
python3 .hive/scripts/x402_mcp_server.py  # port 3950
python3 .hive/scripts/agent_card_generator.py
python3 .hive/scripts/env_readiness_report.py
python3 .hive/scripts/hive_notify.py "Test" "Hello from Hive"
```

## Configuration

Edit `.hive/config.yaml` to add services, sensor patterns, quality repos, or
notification channels. All scripts read from this file at runtime.

## Notifications

Edit `.hive/config.yaml` → `notifications:`

- `dry_run: true` logs what would be sent (default).
- Set `dry_run: false` and fill in channel creds to dispatch real alerts.
- Email uses env vars `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, `FROM_EMAIL` as fallbacks.

## Publish loop

Edit `.hive/config.yaml` → `publish_loop:`

- `dry_run: true` stages posts without publishing.
- Set `dry_run: false` and provide `BUFFER_ACCESS_TOKEN` or enable WebBridge to go live.
- Sources: `csoai-org/READY_TO_POST.txt`, `csoai-org/SOCIAL_BLITZ.md`.

## Dashboard

Serve the dashboard from the repo root, then open http://localhost:8080/.hive/dashboard/:

```bash
cd ~/clawd
python3 -m http.server 8080
```

## Monitoring

```bash
launchctl list | grep ai.csoai
tail -f .hive/logs/healer.log
tail -f .hive/logs/ai.csoai.service-healer.stderr.log
tail -f .hive/logs/notifier.log
tail -f .hive/logs/publish_manager.log
```

## Design principles

1. **Config-driven.** One YAML file drives Sensor, Healer, and Quality Manager.
2. **launchd-native.** macOS user agents keep the stack alive across reboots.
3. **Conservative healing.** Consecutive-failure strikes and restart cooldowns
   prevent the Healer from flapping against slow-starting services.
4. **No new sovereign AI.** The Hive automates the existing stack; it does not
   become another product.
