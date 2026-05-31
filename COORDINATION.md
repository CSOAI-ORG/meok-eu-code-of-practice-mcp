# clawd-workspace — Multi-Agent Coordination Rules

**Why this exists:** Nick runs 4 AIs (Claude, Kimi, Gemini, DeepSeek) against ONE shared repo
(`github.com/CSOAI-ORG/clawd-workspace`) so work is backed up to GitHub, not trapped on the
MacBook. With 4 agents on one `main` branch under one identity, we were clobbering each other
("Kimi removed work") and the git log couldn't tell who did what. These rules fix that.

**Backup principle:** commit + PUSH often. The MacBook is NOT the source of truth — GitHub is.
If the Mac dies, anything pushed survives. Anything only-local is lost.

---

## RULE 1 — Each agent commits under its OWN identity (per-repo, local)
Run ONCE in `/Users/nicholas/clawd`:
```bash
# Claude:
git config --local user.name "Claude (Opus 4.8)" && git config --local user.email "noreply@anthropic.com"
# Kimi:
git config --local user.name "Kimi"    && git config --local user.email "kimi@meok.ai"
# Gemini:
git config --local user.name "Gemini"  && git config --local user.email "gemini@meok.ai"
# DeepSeek:
git config --local user.name "DeepSeek"&& git config --local user.email "deepseek@meok.ai"
```
(`--local` = this repo only; Nick's global `Nicholas` identity stays intact.)
⚠️ Only ONE local identity exists at a time. If agents run concurrently in the same checkout,
identity collides — see RULE 4.

## RULE 2 — Each agent works on its OWN branch, never commits straight to `main`
```
claude/*     e.g. claude/meok-one
kimi/*       e.g. kimi/mcps
gemini/*     e.g. gemini/<area>
deepseek/*   e.g. deepseek/<area>
```
Workflow per agent:
```bash
git checkout -b claude/meok-one        # or: git checkout claude/meok-one
# ... do work ...
git add <ONLY your own files>          # NEVER `git add -A` / `git add .`
git commit -m "..."
git push -u origin claude/meok-one
```
`main` is integration-only. Nick (or one designated merge step) merges agent branches → `main`.

## RULE 3 — Folder ownership (reduces cross-branch conflicts)
| Agent | Primary area |
|-------|--------------|
| Claude | `meok-one/` (the 3D character / MEOK ONE UX), strategy/alignment docs |
| Kimi | MCP servers (`*-mcp/`, `meok-api-gateway`, A2A substrate) |
| Gemini | (assign) |
| DeepSeek | (assign) |
Touch another agent's folder ONLY by agreement. Shared roots (`CLAUDE.md`, this file,
top-level strategy docs) → small commits, pull before push.

## RULE 4 — NEVER `git add -A`. Add only files you created/edited.
The repo always has dozens of dirty files from other agents mid-work. `git add -A` would
sweep their half-done work into YOUR commit under YOUR name. Always `git add path/to/specific/file`.

## RULE 5 — Pull before you push; rebase, don't clobber
```bash
git pull --rebase origin main      # before starting / before pushing
```
If you didn't make a commit, don't force-push over it. No `git push --force` to `main`, ever.

## RULE 6 — Verify before claiming "done"
Read the actual output / screenshot the actual result before saying it works. (Hard-won:
this repo has multiple `RETRACT … was FALSE` commits from claims made without verifying.)

---

## Current branches (keep updated)
- `main` — integration
- `claude/meok-one` — 3D VRM character window + MEOK ONE UX (Claude)
- (add yours here)

## Quick status check
```bash
git branch -a                      # all branches
git log --oneline -10 --format="%h %an %s"   # who did what
git status -sb                     # ahead/behind + dirty files
```
