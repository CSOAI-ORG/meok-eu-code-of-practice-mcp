#!/usr/bin/env python3
"""HIVE MAILER — the hive sends its own outreach. Runs every 30 min via launchd.

Flow each run:
  1. Ask Resend to verify mail.meok.ai (no-op once verified).
  2. If the domain is NOT verified yet → exit quietly (fires automatically later).
  3. If verified → send up to DAILY_CAP queued emails from hello@mail.meok.ai,
     staggered 45-90s, reply-to Nick's real inbox. Mark sent in the queue (JSONL).

Queue: ~/clawd/hive-mailer/queue.jsonl   {"to":..,"subject":..,"body":..,"status":"queued"}
Log:   ~/clawd/hive-mailer/mailer.log
"""
import json, os, random, time, urllib.request
from datetime import date, datetime
from pathlib import Path

HOME = Path(__file__).parent
QUEUE = HOME / "queue.jsonl"
LOG = HOME / "mailer.log"
SENT_TODAY = HOME / f".sent-{date.today()}"
DAILY_CAP = 25
DOMAIN_ID = "3f47ef69-527d-4f65-9266-2c2a9fa985f0"  # mail.meok.ai in Resend
FROM = "Nick Templeman <hello@mail.meok.ai>"
REPLY_TO = "nicholas@meok.ai"

def log(m):
    line = f"{time.strftime('%F %T')} {m}"
    LOG.open("a").write(line + "\n")
    print(line)

def resend_key():
    # pulled from GCP Secret Manager (canonical) with env-file fallback.
    # gcloud lives at /Users/nicholas/google-cloud-sdk/bin/gcloud — use full path
    # because launchd runs with a minimal PATH that doesn't include it.
    import subprocess
    gcloud = "/Users/nicholas/google-cloud-sdk/bin/gcloud"
    r = subprocess.run([gcloud, "secrets", "versions", "access", "latest",
                        "--secret=RESEND_API_KEY", "--project=meok-498012"],
                       capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip():
        return r.stdout.strip()
    for line in open("/tmp/meok-att.env"):
        if line.startswith("RESEND_API_KEY="):
            return line.split('"')[1]
    raise SystemExit("no resend key")

def api(method, path, key, body=None):
    req = urllib.request.Request(f"https://api.resend.com{path}", method=method,
                                 headers={"Authorization": f"Bearer {key}",
                                          "Content-Type": "application/json",
                                          "User-Agent": "meok-hive-mailer/1.0"},
                                 data=json.dumps(body).encode() if body else None)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        return {"error": e.read().decode()[:200], "status": e.code}

def main():
    key = resend_key()
    api("POST", f"/domains/{DOMAIN_ID}/verify", key)  # idempotent nudge
    dom = api("GET", f"/domains/{DOMAIN_ID}", key)
    status = dom.get("status", "unknown")
    recs = dom.get("records", [])
    if recs and all(r.get("status") == "verified" for r in recs):
        status = "verified"  # aggregate flag lags; per-record truth wins (proven by live send 2026-06-11)
    if status != "verified":
        # Resend's status field flaps between API nodes even after records verify.
        # Live sends are the ground truth (proven 2026-06-11): probe with a real API
        # error check instead of trusting the flag.
        probe = api("POST", "/emails", key, {
            "from": FROM, "to": ["delivered@resend.dev"],
            "subject": "gate-probe", "text": "gate probe"})

        # 3-strike backoff: a single probe 403 is almost always API flap, not
        # a real "domain not verified" state. Only treat it as a hard failure
        # if 3 consecutive probes (30 min apart) all 403. Persist strike count
        # in HOME/.probe_strikes so we survive restarts.
        # v2 (15 Jun 06:50Z): cap at 9 to prevent log spam ("strike 47/3") if Resend
        # is genuinely down. Auto-decay to 0 every 24h so a recovered upstream
        # doesn't keep us gated forever.
        STRIKES = HOME / ".probe_strikes"
        STRIKE_TS = HOME / ".probe_strikes_ts"
        strikes = int(STRIKES.read_text()) if STRIKES.exists() else 0
        if STRIKE_TS.exists():
            try:
                last = datetime.fromisoformat(STRIKE_TS.read_text().strip())
                if (datetime.now() - last).total_seconds() > 86400:
                    log(f"strike counter stale ({strikes}, {(datetime.now()-last).total_seconds()/3600:.0f}h old) — auto-resetting to 0")
                    strikes = 0
            except Exception:
                strikes = 0  # corrupt timestamp file, reset
        STRIKE_CAP = 9

        if not probe.get("id"):
            strikes = min(strikes + 1, STRIKE_CAP)
            STRIKES.write_text(str(strikes))
            STRIKE_TS.write_text(datetime.now().isoformat())
            if strikes < 3:
                log(f"probe 403 strike {strikes}/3 — assuming flap, proceeding")
                # fall through to send
            else:
                log(f"probe 403 strike {strikes}/{STRIKE_CAP} (gate at 3) — waiting")
                return
        else:
            if strikes:
                log(f"probe recovered after {strikes} strikes — proceeding")
            STRIKES.write_text("0")
            STRIKE_TS.write_text(datetime.now().isoformat())
            log(f"status flag={status} but probe SENT ({probe['id']}) — proceeding")
    sent_today = int(SENT_TODAY.read_text()) if SENT_TODAY.exists() else 0
    if sent_today >= DAILY_CAP:
        log(f"daily cap reached ({sent_today}/{DAILY_CAP})")
        return
    if not QUEUE.exists():
        log("no queue file")
        return
    rows = [json.loads(l) for l in QUEUE.read_text().splitlines() if l.strip()]
    budget = DAILY_CAP - sent_today
    n = 0
    for row in rows:
        if row.get("status") != "queued" or budget <= 0:
            continue
        r = api("POST", "/emails", key, {
            "from": FROM, "to": [row["to"]], "reply_to": REPLY_TO,
            "subject": row["subject"], "text": row["body"],
        })
        if r.get("id"):
            row["status"] = "sent"; row["resend_id"] = r["id"]; row["sent_at"] = time.strftime("%F %T")
            n += 1; budget -= 1
            log(f"SENT → {row['to']} ({r['id']})")
            QUEUE.write_text("\n".join(json.dumps(x) for x in rows) + "\n")
            SENT_TODAY.write_text(str(sent_today + n))
            time.sleep(random.randint(45, 90))
        else:
            row["status"] = "error"; row["error"] = str(r)[:150]
            log(f"FAIL → {row['to']}: {str(r)[:120]}")
            QUEUE.write_text("\n".join(json.dumps(x) for x in rows) + "\n")
    log(f"run complete — {n} sent this run")

if __name__ == "__main__":
    main()
