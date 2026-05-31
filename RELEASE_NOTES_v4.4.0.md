# Release Notes — Claude Code Playbook v4.4.0

**Released:** 2026-05-31
**Tag:** `v4.4.0`
**License:** MIT

---

## What's in this release

v4.4.0 is a documentation and infrastructure release. Skill count and workflow count are unchanged (7 skills, 17 workflows). The additions are: a three-layer token optimization model, output compression integration, path-scoped rules as a new pattern, security hardening for the Mini Shai-Hulud supply chain threat class, and a `.claudeignore` template.

---

## Why this release exists

Three inputs landed close together in late May 2026:

1. **The Mini Shai-Hulud npm + PyPI worm** (Aikido Security, May 12 and 19 2026) explicitly targets `.claude/settings.json` for persistence and `~/.config/claude/claude_desktop_config.json` for credential theft. The playbook shipped a `.claude/settings.json.template` with no security guidance. That needed to change.

2. **Hamza Farooq's token optimization analysis** (The Production Gap, May 29 2026) benchmarked techniques the playbook hadn't documented: the 20K–30K session startup token floor, `.claudeignore` vs `permissions.deny` enforcement semantics, path-scoped `.claude/rules/` files (41% rule overhead reduction), and CLAUDE.md at under 500 tokens rather than under 50 lines.

3. **Headroom** (chopratejas/headroom, Apache 2.0, 2.5k+ stars) provides output compression for Claude Code sessions — 47–92% reduction in dynamic context from tool outputs, logs, and file reads. The `headroom wrap claude` pattern and `headroom learn` failure-mining automation were direct improvements to the playbook's session management story.

---

## New files

| File | Purpose |
|------|---------|
| `templates/.claudeignore` | Standard minimum context exclusions for any project |
| `templates/.claude/rules/global.md` | Example unscoped always-loaded rules |
| `templates/.claude/rules/api.md` | Example path-scoped API layer rules |

---

## Changed files

| File | Summary |
|------|---------|
| `docs/TOKEN_ECONOMICS.md` | Complete rewrite: three-layer model, session floor, Headroom, Layer 3 caching |
| `docs/CONFIGURATION.md` | Complete rewrite: six golden rules, `.claudeignore` vs `permissions.deny`, path-scoped rules, MCP warnings, security |
| `docs/AGENTIC_PATTERNS.md` | Patterns 8 (path-scoped rules) and 9 (Headroom compression) added; comparison table updated |
| `templates/CLAUDE.md.template` | Token target, HTML comment trick, import caveat, headroom learn note, security section |
| `templates/.claude/settings.json.template` | `permissions.deny` block, `_security_note` field |
| `scripts/check_config_health.sh` | v4.4.0: 9 sections; adds Headroom, path-scoped rules, `.claude/` security scan, `permissions.deny` count, token estimation |
| `README.md` | v4.4.0: three-layer optimization, Headroom quick start, security note, external resources |
| `CHANGELOG.md` | v4.4.0 entry |
| `CITATION.cff` | v4.4.0, added Headroom and token-optimizer references |
| `.zenodo.json` | v4.4.0 metadata, added related identifiers |

---

## Breaking changes

None. All additions are opt-in. Existing CLAUDE.md files, settings.json files, and workflow invocations continue to work without modification.

---

## Migration guide

**From v4.3.0 to v4.4.0:**

```bash
git pull origin main

# Add the new .claudeignore template to your projects
cp templates/.claudeignore /path/to/your/project/.claudeignore

# Update settings.json to add permissions.deny
# (see templates/.claude/settings.json.template for the deny block)

# Create .claude/rules/ for domain-specific rules
mkdir -p /path/to/your/project/.claude/rules
cp templates/.claude/rules/global.md /path/to/your/project/.claude/rules/

# Optional: install Headroom
pip install "headroom-ai[all]"
headroom wrap claude

# Run the updated health check
bash scripts/check_config_health.sh
```

---

## Security advisory

The Mini Shai-Hulud supply chain worm (npm wave May 12, PyPI wave May 19 2026, attributed to TeamPCP) writes persistence to `.claude/settings.json` and exfiltrates credentials from `~/.config/claude/claude_desktop_config.json`, `~/.cursor/mcp.json`, `~/.vscode/mcp.json`, and other AI coding assistant config files.

If you installed any of the following packages, treat the host as compromised until rotated:
- npm: `@tanstack/*`, `@mistralai/*`, `@uipath/*`, `@squawk/*` (affected versions, May 2026)
- PyPI: `durabletask==1.4.1`, `1.4.2`, `1.4.3`

Detection: check `~/.cache/.sys-update-check` (presence = worm ran), inspect `.claude/settings.json` for unexpected keys, search GitHub commits for `FIRESCALE` (dead-drop beacon string).

The updated `scripts/check_config_health.sh` (Section 4) checks `.claude/settings.json` for unexpected keys as part of the standard monthly health check.

---

## Acknowledgements

- [Headroom](https://github.com/chopratejas/headroom) by Tejas Chopra — Apache 2.0, directly integrated
- [token-optimizer](https://github.com/hamzafarooq/token-optimizer) by Hamza Farooq — benchmarks cited
- [Aikido Security](https://www.aikido.dev/blog) — Mini Shai-Hulud threat intelligence
- [The Production Gap newsletter](https://boringbot.substack.com/p/how-to-save-millions-in-claude-tokens) by Hamza Farooq — token optimization analysis

---

## Download

Download `ClaudePlaybook_v4.4.0.zip` from the [releases page](https://github.com/chokmah-me/claude-code-playbook/releases/tag/v4.4.0) and upload to your Claude Project, or clone and copy:

```bash
git clone --branch v4.4.0 https://github.com/chokmah-me/claude-code-playbook.git
```
