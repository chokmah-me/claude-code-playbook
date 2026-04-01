# 🤖 Claude Code Playbook

**Version**: 4.2.1 | **Date**: April 1, 2026 | **License**: MIT | **Repository**: https://github.com/chokmah-me/claude-code-playbook

A token-efficient AI engineering system that reduces conversation turns through specialized workflows and agentic patterns.

Includes Plan Mode integration, Explore subagents, persistent memory, and 6 skill domains with 15 reusable workflows.

---

## 🚀 Quick Start

Get productive in **15 minutes**:

```bash
# 1. Clone
git clone https://github.com/chokmah-me/claude-code-playbook.git
cd claude-code-playbook

# 2. Copy templates to your project
cp templates/CLAUDE.md.template /path/to/your/project/CLAUDE.md
cp templates/.bash_aliases.template >> ~/.bashrc && source ~/.bashrc

# 3. Start working
cctriage  # Find refactoring opportunities
```

**Windows PowerShell:**
```powershell
# Quick setup
. scripts/powershell/setup_powershell_profile.ps1
ccnew  # Start session
```

**✅ Success indicators:**
- Workflows execute without errors
- Refactoring plan completes in 2-4 sessions
- REFACTOR_PROGRESS.md tracks multi-session work
- You're productive within 30 minutes

**📖 [Complete 15-Minute Setup Guide →](docs/GETTING_STARTED.md)**

---

## 🎯 What You Get

**Core Features:**
- **🖥️ Cross-Platform** - Windows (PowerShell), Mac, Linux
- **⚡ 20+ Aliases** - Save 8+ minutes/day (`ccnew`, `cctriage`, `cchealth`)
- **🧠 Agentic Patterns** - Plan Mode, Explore subagents, memory system, task tracking
- **📊 Token Efficient** - Modern high-context workflows (no manual /clear needed)
- **🎓 6 Skills, 15 Workflows** - refactoring, debugging, documentation, onboarding, skill-extractor, python-scientific

**In our testing:**
- Fewer conversation turns through structured workflows
- Test pass rates maintained across refactoring sessions
- 15-minute setup vs. 60+ minutes configuring from scratch

---

## 🛠️ Essential Commands

```bash
# Daily workflow
cctriage    # Find issues (~2K tokens)
ccplan      # Create plan + enter Plan Mode
cccode      # Implement with progress tracking
cchealth    # Check config health
```

**📋 Session continuity**: Automatic via REFACTOR_PROGRESS.md + memory files (no manual resets).

---

## 📚 Documentation

| Guide | What You'll Learn | Time |
|-------|-------------------|------|
| **[🚀 Getting Started](docs/GETTING_STARTED.md)** | Complete setup & first workflow | 5 min |
| **[🧠 Agentic Patterns](docs/AGENTIC_PATTERNS.md)** | Plan Mode, Explore agents, memory, tasks | 10 min |
| **[⚙️ Configuration](docs/CONFIGURATION.md)** | Best practices & optimization | 8 min |
| **[💡 Shell Aliases](docs/ALIASES.md)** | All 20+ shortcuts (Bash & PowerShell) | 6 min |
| **[📊 Token Economics](docs/TOKEN_ECONOMICS.md)** | Budget planning & efficiency | 7 min |
| **[🏆 Success Guide](docs/SUCCESS_GUIDE.md)** | Learning path & metrics | 10 min |

**Platform-Specific:**
- **[Windows PowerShell](docs/windows/WINDOWS_QUICKSTART.md)** - PowerShell setup guide
- **[Implementation Details](docs/PLAYBOOK_IMPLEMENTATION.md)** - Technical reference

---

## 📂 How Skills Work

Skills are markdown-based workflow definitions that Claude Code reads from `.claude/skills/`. Each skill has a `SKILL.md` router and a `workflows/` directory with step-by-step procedures. You invoke them by asking Claude to run a workflow (e.g., "run the diagnose workflow") or via shell aliases.

## 📂 Project Structure

```
├── 📁 .claude/skills/       # Skills loaded by Claude Code (canonical)
├── 📁 docs/                 # Complete documentation
├── 📁 scripts/              # Health checks & utilities
├── 📁 skills/               # Skills mirror (for browsing/reference)
│   ├── refactoring/         #   triage, extract, modernize, qnew, qplan, qcode, catchup
│   ├── debugging/           #   diagnose, trace
│   ├── documentation/       #   audit, generate
│   ├── onboarding/          #   orient, glossary
│   ├── skill-extractor/     #   extract, refine
│   └── python-scientific/   #   NumPy/SciPy patterns
├── 📁 templates/            # Ready-to-use configurations
└── 📄 README.md             # This file
```

**Templates include:** CLAUDE.md, .cursorrules, settings, aliases, and more.

---

## 🔧 Platform Support

### Linux/Mac
```bash
# Setup aliases
cat templates/.bash_aliases.template >> ~/.bashrc
source ~/.bashrc

# Use shortcuts
cctriage  # Analyze code
ccplan    # Create plan
cchealth  # Health check
```

### Windows (PowerShell)
```powershell
# Setup
. scripts/powershell/setup_powershell_profile.ps1

# Use shortcuts
cctriage  # Analyze code
ccplan    # Create plan
cchealth  # Health check
```

**Note**: May require: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Help needed:** Additional languages, templates, tutorials, translations.

---

## 📞 Support

- **📖 Documentation**: [Complete docs](docs/)
- **🐛 Issues**: [GitHub Issues](https://github.com/chokmah-me/claude-code-playbook/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/chokmah-me/claude-code-playbook/discussions)
- **📚 Claude Code Docs**: https://docs.anthropic.com/claude-code

---

*Ready? [Start here →](docs/GETTING_STARTED.md)*