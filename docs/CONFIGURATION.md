# ⚙️ Configuration Best Practices

**Complete guide to configuring Claude Code Playbook for optimal performance, token efficiency, and security.**

---

## 🏆 The Golden Rules

### 1. Keep CLAUDE.md under 500 tokens (not just lines)

Every token in CLAUDE.md is paid on every single turn. A 3,847-token CLAUDE.md vs a 312-token version: 91.9% context reduction, no quality regression. Token count matters more than line count.

Estimate before and after:
```bash
python -c "
with open('CLAUDE.md') as f:
    words = len(f.read().split())
print(f'{words} words ≈ {int(words*1.3)} tokens (target: <500)')
"
```

HTML comments (`<!-- this note -->`) cost zero tokens — they're stripped before injection. Use them for teammate notes, rationale, and anything humans need that Claude doesn't.

`@path/to/file` imports are organizational only. All imported files still load at session start. Splitting CLAUDE.md across files saves no tokens.

### 2. Use .claudeignore and permissions.deny — they are different things

`.claudeignore` is advisory. Claude can still read ignored files if it decides they're necessary (documented in GitHub issues #36163, #51105). It handles the signal layer.

`permissions.deny` in `.claude/settings.json` is enforced. It blocks the Read tool for those paths entirely. Use both:

```json
{
  "permissions": {
    "deny": ["Read(node_modules/**)", "Read(dist/**)", "Read(*.lock)"]
  }
}
```

Minimum `.claudeignore` for any project:
```
node_modules/
dist/
build/
.next/
__pycache__/
*.pyc
*.lock
package-lock.json
yarn.lock
poetry.lock
coverage/
*.generated.*
*.min.js
*.min.css
```

Commit `.claudeignore` to version control. Every team member gets the same context discipline.

### 3. Use path-scoped rules in .claude/rules/

Rules files in `.claude/rules/` without `paths:` frontmatter load at session start like a second CLAUDE.md. Rules with `paths:` frontmatter load only when Claude touches a matching file — zero cost until triggered.

```yaml
---
paths:
  - "src/api/**/*.ts"
---
All endpoints must validate input with Zod schemas.
Response errors must use the shared ApiError class.
```

Move domain-specific rules here instead of CLAUDE.md. One team reduced always-loaded rule overhead by 41% this way.

### 4. Enable only MCP servers you actually use

Each connected MCP server loads its tool schema into every request — 400–800 tokens each. Heavy setups add 10,000–20,000 tokens of silent per-session overhead.

`ENABLE_TOOL_SEARCH=true` in Claude Code settings defers schemas until needed, recovering 50,000–70,000 tokens in heavy setups.

**Do not connect or disconnect MCP servers mid-session.** Doing so wipes your entire prompt cache. Make changes at session boundaries only.

**Exception: Headroom's MCP server** (`headroom mcp install`) is worth adding even when disabling others, because it compresses the output of every other MCP tool, paying back its schema cost many times over.

### 5. Treat .claude/ files as credential material

The Mini Shai-Hulud supply chain worm (May 2026) writes persistence to `.claude/settings.json` and targets `~/.config/claude/claude_desktop_config.json` for credential theft. These are not just configuration files.

After any supply chain incident (unexpected package behavior, CI anomalies, suspicious npm/pip output):
- Inspect `.claude/settings.json` and `.claude/settings.local.json` for unexpected entries
- Check `~/.config/claude/claude_desktop_config.json` for unexpected MCP tokens or server entries
- Treat any API keys stored in MCP configs as potentially exfiltrated — rotate them

Do not store long-lived API keys or tokens in MCP config files in plaintext. Use environment variables or a secrets manager, and reference them by name.

### 6. Run health checks monthly

```bash
bash scripts/check_config_health.sh
```

---

## 📊 Configuration Files Overview

| File | Purpose | Commit? | Size target |
|------|---------|---------|-------------|
| CLAUDE.md | Project guidelines | Yes | <500 tokens |
| .claude/settings.json | Permissions, tools, MCP | Yes | <3KB |
| .claude/rules/*.md | Path-scoped rules | Yes | Per-file, small |
| .mcp.json | MCP server config | Yes | <5KB |
| CLAUDE.local.md | Personal preferences | No (gitignored) | No limit |
| REFACTOR_PROGRESS.md | Session progress | No (temporary) | No limit |

---

## 🛠️ Detailed Configuration Guide

### CLAUDE.md Template

Cut these (Claude already knows them): framework routing, standard syntax, generic best practices, team contact info, FAQs.

Keep these: non-obvious build/test commands, architecture decisions against defaults, project-specific gotchas, validation command exact syntax.

### .claude/settings.json

```json
{
  "permissions": {
    "allow": [
      "Bash(git:*)",
      "Bash(npm:*)",
      "Bash(pytest:*)"
    ],
    "deny": [
      "Read(node_modules/**)",
      "Read(dist/**)",
      "Read(*.lock)"
    ]
  }
}
```

After any suspected supply chain compromise, inspect this file for entries you did not add. The Mini Shai-Hulud worm modifies it as a persistence mechanism.

### .claude/rules/ layout

```
.claude/rules/
├── global.md           # No paths: — loads every session (keep tiny)
├── api-rules.md        # paths: src/api/**
├── db-rules.md         # paths: src/database/**
└── test-rules.md       # paths: tests/**
```

Only `global.md` loads unconditionally. The others are free until touched.

### MCP configuration

```json
{
  "mcpServers": {
    "headroom": {
      "command": "headroom",
      "args": ["mcp", "serve"],
      "description": "Context compression — reduces all other tool output cost",
      "enabled": true
    },
    "github": {
      "enabled": false
    }
  }
}
```

Keep `ENABLE_TOOL_SEARCH=true` in your Claude Code settings when running multiple servers.

---

## 🔧 Monthly Maintenance

```bash
# 1. Health check
bash scripts/check_config_health.sh

# 2. Token audit
python -c "
with open('CLAUDE.md') as f:
    words = len(f.read().split())
print(f'CLAUDE.md: {words} words ≈ {int(words*1.3)} tokens')
"

# 3. MCP audit
cat .mcp.json | python -c "
import json, sys
cfg = json.load(sys.stdin)
servers = cfg.get('mcpServers', {})
enabled = [k for k,v in servers.items() if v.get('enabled', False)]
print(f'Enabled MCP servers ({len(enabled)}): {enabled}')
"

# 4. Security: check .claude/settings.json for unexpected entries
python -c "
import json
with open('.claude/settings.json') as f:
    cfg = json.load(f)
print(json.dumps(cfg, indent=2))
print('--- Review above for unexpected entries ---')
"

# 5. Update playbook
git pull origin main
```

---

## 🚨 Common Configuration Mistakes

**Overly detailed CLAUDE.md (most common)**
Problem: 100+ lines or 1000+ tokens of project history and generic advice.
Fix: Strip to commands, constraints, and genuine gotchas. Under 500 tokens.

**Using .claudeignore instead of permissions.deny for enforcement**
Problem: Ignored files still get read when Claude judges them necessary.
Fix: Add `permissions.deny` for paths that must never enter context.

**Never auditing MCP configs for credential leakage**
Problem: API keys accumulate in `~/.vscode/mcp.json`, `~/.cursor/mcp.json`, `.mcp.json`.
Fix: Use environment variable references, not plaintext keys. Rotate after any supply chain incident.

**Connecting MCP servers mid-session**
Problem: Wipes your entire prompt cache.
Fix: All MCP changes at session boundaries.

**Skipping path-scoped rules**
Problem: All rules load every session regardless of what you're working on.
Fix: Move domain-specific rules to `.claude/rules/` with `paths:` frontmatter.

---

## 📚 Related Documentation

- [Getting Started](GETTING_STARTED.md) — setup guide
- [Token Economics](TOKEN_ECONOMICS.md) — three-layer optimization model
- [Agentic Patterns](AGENTIC_PATTERNS.md) — compression, hooks, memory
- [Shell Aliases](ALIASES.md) — productivity shortcuts
