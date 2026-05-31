# 🤖 Claude Code Playbook

**Version**: 4.4.0 | **Date**: May 31, 2026 | **License**: MIT | **Repository**: https://github.com/chokmah-me/claude-code-playbook

A token-efficient AI engineering system that reduces conversation turns through specialized workflows, agentic patterns, and three-layer context optimization.

Includes Plan Mode integration, Explore subagents, persistent memory, path-scoped rules, output compression via Headroom, and 7 skill domains with 17 reusable workflows.

---

## 🚀 Quick Start

Get productive in **15 minutes**:

```bash
# 1. Clone
git clone https://github.com/chokmah-me/claude-code-playbook.git
cd claude-code-playbook

# 2. Copy templates to your project
cp templates/CLAUDE.md.template /path/to/your/project/CLAUDE.md
cp templates/.claudeignore /path/to/your/project/.claudeignore
cp templates/.bash_aliases.template >> ~/.bashrc && source ~/.bashrc

# 3. Optional — output compression (recommended for long sessions)
pip install "headroom-ai[all]"
headroom wrap claude

# 4. Start working
cctriage  # Find refactoring opportunities
```

**✅ Success indicators:**
- Workflows execute without errors
- `/context` shows CLAUDE.md under 500 tokens
- Tool output is visibly compressed in long sessions
- REFACTOR_PROGRESS.md tracks multi-session work

**📖 [Complete 15-Minute Setup Guide →](docs/GETTING_STARTED.md)**

---

## 🎯 What You Get

**Core Features:**
- **🖥️ Cross-Platform** — Windows (PowerShell), Mac, Linux
- **⚡ 20+ Aliases** — Save 8+ minutes/day (`ccnew`, `cctriage`, `cchealth`)
- **🧠 Agentic Patterns** — Plan Mode, Explore subagents, memory, path-scoped rules, output compression
- **📊 Three-Layer Token Optimization** — Don't load it · Compress it · Cache it
- **🔒 Security Hardening** — Supply chain threat guidance, `.claude/` integrity checks
- **🎓 7 Skills, 17 Workflows** — refactoring, debugging, documentation, onboarding, skill-extractor, skill-creator, python-scientific

**Measured results:**
- 91.9% context reduction from CLAUDE.md optimization
- 47–92% dynamic context reduction via Headroom output compression
- 41% rule overhead reduction from path-scoped `.claude/rules/`
- 67% fewer conversation turns through structured workflows

---

## 🛠️ Essential Commands

```bash
# Daily workflow
cctriage    # Find issues (~2K tokens)
ccplan      # Create plan + enter Plan Mode
cccode      # Implement with progress tracking
cchealth    # Check config health

# Token optimization
headroom wrap claude    # Compress session tool output
headroom stats          # See savings so far
headroom learn          # Mine failed sessions → CLAUDE.md corrections
```

**Session continuity**: Automatic via REFACTOR_PROGRESS.md + memory files. No manual resets needed.

---

## 📚 Documentation

| Guide | What You'll Learn | Time |
|-------|-------------------|------|
| **[🚀 Getting Started](docs/GETTING_STARTED.md)** | Complete setup & first workflow | 5 min |
| **[🧠 Agentic Patterns](docs/AGENTIC_PATTERNS.md)** | Plan Mode, Explore, path-scoped rules, Headroom | 10 min |
| **[⚙️ Configuration](docs/CONFIGURATION.md)** | CLAUDE.md, .claudeignore, rules, MCP, security | 8 min |
| **[📊 Token Economics](docs/TOKEN_ECONOMICS.md)** | Three-layer optimization: don't load · compress · cache | 8 min |
| **[💡 Shell Aliases](docs/ALIASES.md)** | All 20+ shortcuts (Bash & PowerShell) | 6 min |
| **[🏆 Success Guide](docs/SUCCESS_GUIDE.md)** | Learning path & metrics | 10 min |

**Platform-Specific:**
- **[Windows PowerShell](docs/windows/WINDOWS_QUICKSTART.md)** — PowerShell setup guide

---

## 📂 How Skills Work

Skills are markdown-based workflow definitions in `.claude/skills/`. Each skill has a `SKILL.md` router and a `workflows/` directory. Invoke by asking Claude to run a workflow or via shell aliases.

**New in v4.4.0:** `.claude/rules/` path-scoped rules load only when Claude touches matching files — zero cost until triggered. See [Agentic Patterns](docs/AGENTIC_PATTERNS.md#pattern-8-path-scoped-rules-for-zero-cost-context).

## 📂 Project Structure

```
├── 📁 .claude/
│   ├── skills/              # Skills loaded by Claude Code
│   └── rules/               # Path-scoped rules (new in v4.4.0)
├── 📁 docs/                 # Complete documentation
├── 📁 scripts/              # Health checks & utilities
├── 📁 skills/               # Skills mirror (for browsing/reference)
├── 📁 templates/            # Ready-to-use configurations
│   ├── CLAUDE.md.template   # Token-optimized project constitution
│   ├── .claudeignore        # Standard context exclusions (new in v4.4.0)
│   ├── .claude/rules/       # Example path-scoped rules (new in v4.4.0)
│   └── .claude/settings.json.template  # Permissions with deny rules
└── 📄 README.md
```

---

## 🔒 Security Note

The Mini Shai-Hulud supply chain worm (May 2026, npm + PyPI) explicitly targets:
- `.claude/settings.json` — writes persistence entries
- `~/.config/claude/claude_desktop_config.json` — exfiltrates MCP tokens

After any supply chain incident (unexpected CI behavior, suspicious package output):
1. Inspect `.claude/settings.json` for entries you didn't add
2. Rotate API keys stored in MCP config files
3. Run `bash scripts/check_config_health.sh` — section 4 checks for unexpected entries

See [Configuration Guide](docs/CONFIGURATION.md) for full hardening guidance.

---

## 🔧 Platform Support

### Linux/Mac
```bash
cp templates/.claudeignore /path/to/project/.claudeignore
cat templates/.bash_aliases.template >> ~/.bashrc && source ~/.bashrc
cctriage
```

### Windows (PowerShell)
```powershell
. scripts/powershell/setup_powershell_profile.ps1
cctriage
```

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Issues: [GitHub Issues](https://github.com/chokmah-me/claude-code-playbook/issues).

---

## 🔗 External Resources

- **[Headroom](https://github.com/chopratejas/headroom)** — output compression for Claude Code (60–95% token reduction)
- **[token-optimizer](https://github.com/hamzafarooq/token-optimizer)** — CLAUDE.md benchmark and audit tool
- **[The Production Gap — Token Optimization](https://boringbot.substack.com/p/how-to-save-millions-in-claude-tokens)** — Boringbot analysis of CLAUDE.md trim, .claudeignore, path-scoped rules
- **[Claude Code Documentation](https://docs.anthropic.com/claude-code)**

---

*Ready? [Start here →](docs/GETTING_STARTED.md)*
