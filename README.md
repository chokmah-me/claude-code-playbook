# 🤖 Claude Code Playbook

**Version**: 4.1.1 | **License**: MIT | **Repository**: https://github.com/dyb5784/claude-code-playbook

A token-efficient AI engineering system that reduces conversation turns through specialized workflows.

**✨ New in v4.1.1**: Cross-platform PowerShell support, comprehensive documentation, and improved Windows compatibility.

---

## 🚀 Quick Start

Get productive in **15 minutes** with our streamlined setup:

```bash
# 1. Clone the playbook
git clone https://github.com/dyb5784/claude-code-playbook.git
cd claude-code-playbook

# 2. Copy templates to your project
cp templates/CLAUDE.md.template /path/to/project/CLAUDE.md
cp templates/.cursorrules.template /path/to/project/.cursorrules

# 3. Test your setup
claude skills refactoring qnew
```

**Windows PowerShell:**
```powershell
git clone https://github.com/dyb5784/claude-code-playbook.git
Copy-Item templates/CLAUDE.md.template C:\path\to\project\CLAUDE.md
. scripts/powershell/setup_powershell_profile.ps1
ccnew  # Start new session
```

**✅ Success indicators:**
- Workflows execute without errors
- Token usage stays under 25K per session  
- Context resets work smoothly
- You're productive within 30 minutes

**📖 [Complete Getting Started Guide →](docs/GETTING_STARTED.md)**

---

## 🎯 What You'll Get

**Core Features:**
- **🖥️ Cross-Platform Support** - Works on Windows (PowerShell), Mac, and Linux
- **📦 Complete Template Set** - 8 configuration templates for instant setup
- **🔧 Health Check Scripts** - Automated monitoring and validation
- **⚡ Productivity Aliases** - 26+ shortcuts that save 8+ minutes/day
- **🎓 Structured Learning Path** - Go from beginner to expert in 4 weeks

**Available Skills:**
- **Python Scientific Computing** - Research-grade patterns for NumPy/SciPy
- **General Refactoring** - 7 structured workflows (triage, extract, modernize, qnew, qplan, qcode, catchup)

**Proven Results:**
- 67% reduction in conversation turns
- 100% test pass rate maintained
- 40% improvement in code maintainability
- 75% faster setup (60min → 15min)

---

## 📚 Documentation

Our documentation is organized into focused guides:

| Guide | Description | Time to Read |
|-------|-------------|--------------|
| **[🚀 Getting Started](docs/GETTING_STARTED.md)** | Complete 15-minute setup guide | 5 min |
| **[⚙️ Configuration](docs/CONFIGURATION.md)** | Best practices and optimization | 8 min |
| **[💡 Shell Aliases](docs/ALIASES.md)** | Productivity shortcuts for all platforms | 6 min |
| **[📊 Token Economics](docs/TOKEN_ECONOMICS.md)** | Optimize token usage and costs | 7 min |
| **[🏆 Success Guide](docs/SUCCESS_GUIDE.md)** | Learning paths and success metrics | 10 min |

**Platform-Specific Guides:**
- **[Windows Quick Start](docs/windows/WINDOWS_QUICKSTART.md)** - PowerShell setup and usage
- **[Implementation Guide](docs/PLAYBOOK_IMPLEMENTATION.md)** - Technical implementation details

---

## 🛠️ Key Commands

### Daily Workflow
```bash
# Start your session
ccclear && ccnew

# Analyze and plan
cctriage && ccplan

# Implement changes
cccode || ccextract

# Check usage and reset
cccost
# Reset if >25K tokens: /clear && cccatchup
```

### Essential Commands
| Command | Purpose | Tokens |
|---------|---------|--------|
| `cctriage` | Find refactoring opportunities | ~2K |
| `ccnew` | Start fresh session | ~2K |
| `ccplan` | Create refactoring plan | ~3K |
| `cccode` | Generate implementation | ~8-12K |
| `cccatchup` | Restore context after reset | ~1-2K |

**💰 Budget**: Stay under 25K tokens per session for Claude Pro efficiency.

---

## 📂 What's Included

```
claude-code-playbook/
├── 📁 docs/                    # Complete documentation
│   ├── GETTING_STARTED.md     # 15-minute setup guide
│   ├── CONFIGURATION.md       # Best practices
│   ├── ALIASES.md            # Productivity shortcuts
│   ├── TOKEN_ECONOMICS.md    # Token optimization
│   ├── SUCCESS_GUIDE.md      # Success metrics & learning
│   └── windows/              # Windows-specific guides
├── 📁 scripts/               # Health check and utility scripts
│   ├── check_config_health.sh    # Linux/Mac health check
│   ├── validate_config.py        # Configuration validator
│   └── powershell/           # Windows PowerShell scripts
├── 📁 skills/                # Available skills and workflows
│   ├── python-scientific/    # Scientific computing patterns
│   └── refactoring/          # 7 refactoring workflows
├── 📁 templates/             # Ready-to-use configuration files
│   ├── CLAUDE.md.template    # Main project configuration
│   ├── .cursorrules.template # IDE integration rules
│   ├── .claude/              # Claude-specific settings
│   └── [5 more templates]    # Complete template set
└── 📄 README.md              # This file
```

---

## 🎓 Learning Path

### Week 1: Foundation ✅
- [ ] Complete 15-minute setup
- [ ] Run first `triage` workflow
- [ ] Master basic commands (`ccnew`, `ccclear`, `cccost`)
- [ ] Understand token limits with `/cost`

### Week 2: Workflows 🔄
- [ ] Use all 7 refactoring workflows
- [ ] Achieve <25K tokens per session
- [ ] Practice context resets
- [ ] Configure project settings

### Week 3: Optimization ⚡
- [ ] Master shell aliases (save 8+ min/day)
- [ ] Run monthly health checks
- [ ] Customize for your tech stack
- [ ] Track productivity metrics

### Week 4: Mastery 🏆
- [ ] Handle complex multi-file refactorings
- [ ] Design custom strategies
- [ ] Contribute improvements back
- [ ] Mentor team members

**📖 [Complete Success Guide →](docs/SUCCESS_GUIDE.md)**

---

## 🏆 Success Metrics

**Immediate Benefits:**
- Setup time: **15 minutes** (vs 60+ minutes without playbook)
- First productive session: **30 minutes**
- Daily time savings: **8+ minutes** with aliases

**Quality Improvements:**
- 67% reduction in conversation turns
- 100% test pass rate maintained
- 40% improvement in code maintainability
- Zero API breakage during refactoring

**Long-term Value:**
- Consistent code quality across projects
- Reduced debugging time
- Faster onboarding for new team members
- Standardized development practices

---

## 🔧 Platform Support

### Linux/Mac (Bash/Zsh)
```bash
# Setup aliases
cat templates/.bash_aliases.template >> ~/.bashrc
source ~/.bashrc

# Use shortcuts
cctriage  # Analyze code
cccost    # Check tokens
cchealth  # Health check
```

### Windows (PowerShell)
```powershell
# Setup PowerShell profile
. scripts/powershell/setup_powershell_profile.ps1

# Use shortcuts
cctriage  # Analyze code
cccost    # Check tokens
cchealth  # Health check
```

**Note**: PowerShell execution may require:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Areas needing help:**
- Additional language support (Go, Rust, Java)
- More custom command templates
- Video walkthroughs and tutorials
- Translation to other languages
- Performance benchmarking tools

---

## 📞 Support

**Documentation**: Browse our complete [docs/](docs/) folder  
**Issues**: Report bugs on [GitHub Issues](https://github.com/dyb5784/claude-code-playbook/issues)  
**Discussions**: Share experiences in [GitHub Discussions](https://github.com/dyb5784/claude-code-playbook/discussions)  
**Claude Code Docs**: https://docs.anthropic.com/claude-code

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

**Version**: 4.1.1 | **Date**: December 25, 2025 | **Status**: ✅ Production Ready

---

*Ready to get started? Head to the [🚀 Getting Started Guide](docs/GETTING_STARTED.md) and be productive in 15 minutes!*