# 📚 Claude Code Playbook Documentation

**Complete documentation index for the Claude Code Playbook.**

---

## 🚀 Quick Links

**New Users Start Here:**
- **[Getting Started](GETTING_STARTED.md)** - Complete 15-minute setup guide
- **[Windows Quick Start](windows/WINDOWS_QUICKSTART.md)** - PowerShell-specific setup

**Reference Guides:**
- **[Configuration Guide](CONFIGURATION.md)** - Best practices and optimization
- **[Shell Aliases](ALIASES.md)** - Productivity shortcuts for all platforms
- **[Token Economics](TOKEN_ECONOMICS.md)** - Optimize token usage and costs
- **[Success Guide](SUCCESS_GUIDE.md)** - Learning paths and success metrics

**Implementation Details:**
- **[Playbook Implementation](PLAYBOOK_IMPLEMENTATION.md)** - Technical implementation details
- **[Workflow Guide](WORKFLOW_GUIDE.md)** - Detailed workflow documentation

---

## 📖 Documentation Overview

### Getting Started Guides (15 min total)
| Guide | Description | When to Use |
|-------|-------------|-------------|
| [🚀 Getting Started](GETTING_STARTED.md) | Complete setup for all platforms | First time setup |
| [🪟 Windows Quick Start](windows/WINDOWS_QUICKSTART.md) | PowerShell-specific instructions | Windows users |
| [⚙️ Configuration](CONFIGURATION.md) | Best practices and optimization | After basic setup |

### Reference Guides (Use as needed)
| Guide | Description | When to Use |
|-------|-------------|-------------|
| [💡 Shell Aliases](ALIASES.md) | Complete alias reference | Daily productivity |
| [📊 Token Economics](TOKEN_ECONOMICS.md) | Token optimization strategies | When hitting limits |
| [🏆 Success Guide](SUCCESS_GUIDE.md) | Learning paths and metrics | Skill development |

### Advanced Guides (Optional)
| Guide | Description | When to Use |
|-------|-------------|-------------|
| [🔧 Implementation](PLAYBOOK_IMPLEMENTATION.md) | Technical details | Custom development |
| [🔄 Workflows](WORKFLOW_GUIDE.md) | Workflow deep-dive | Advanced usage |

---

## 🎯 Learning Path

### Beginner (Week 1)
1. **[Getting Started](GETTING_STARTED.md)** (5 min) - Complete setup
2. **[Windows Quick Start](windows/WINDOWS_QUICKSTART.md)** (3 min) - If on Windows
3. **[Configuration](CONFIGURATION.md)** (8 min) - Basic optimization
4. **Practice**: Use `cctriage`, `ccnew`, `ccclear`

### Intermediate (Week 2-3)
1. **[Shell Aliases](ALIASES.md)** (6 min) - Master productivity shortcuts
2. **[Token Economics](TOKEN_ECONOMICS.md)** (7 min) - Optimize usage
3. **Practice**: All 7 refactoring workflows

### Advanced (Month 2+)
1. **[Success Guide](SUCCESS_GUIDE.md)** (10 min) - Success strategies
2. **[Implementation](PLAYBOOK_IMPLEMENTATION.md)** (15 min) - Technical details
3. **Practice**: Complex refactorings, custom workflows

---

## 🔧 Platform-Specific Guides

### Linux/Mac Users
- **[Getting Started](GETTING_STARTED.md)** - Bash/Zsh setup
- **[Shell Aliases](ALIASES.md)** - Bash/Zsh shortcuts
- **Commands**: Use `bash scripts/check_config_health.sh`

### Windows Users
- **[Windows Quick Start](windows/WINDOWS_QUICKSTART.md)** - PowerShell setup
- **[Shell Aliases](ALIASES.md)** - PowerShell shortcuts
- **Commands**: Use simplified PowerShell commands (see notes below)

---

## ⚠️ Important Notes

### PowerShell Limitations
Some PowerShell examples in the documentation may require modification due to:
- Execution policy restrictions
- Profile loading issues
- Module availability

**Workaround for simple commands:**
```powershell
# Instead of complex scripts, use simple commands
powershell -NoProfile -Command "Get-Content 'CLAUDE.md' | Measure-Object -Line"

# For health checks, use the bash script via WSL or Git Bash
bash scripts/check_config_health.sh
```

### Token Limits
- **Claude Pro**: 10-40 prompts per 5-hour window
- **Target**: <25,000 tokens per session
- **Check**: Use `/cost` command regularly
- **Reset**: Use `/clear` + `catchup` every 5-7 prompts

---

## 📊 Success Tracking

### Daily Metrics
- Token usage per session (target: <25K)
- Commands used (target: 3+ different workflows)
- Time saved with aliases (target: 8+ minutes)

### Weekly Review
- Configuration health check
- Workflow adoption progress
- Learning path advancement

### Monthly Assessment
- Complete success metrics review
- Documentation updates needed
- Skill level progression

---

## 🆘 Common Issues

### Setup Issues
- **"Command not found"** → Check Claude Code installation
- **Permission errors** → Review `.claude/settings.json`
- **Template copy errors** → Verify paths and permissions

### Usage Issues
- **High token usage** → See [Token Economics](TOKEN_ECONOMICS.md)
- **Slow performance** → Check [Configuration](CONFIGURATION.md)
- **Workflow confusion** → Review [Success Guide](SUCCESS_GUIDE.md)

### Platform Issues
- **PowerShell problems** → Use [Windows Quick Start](windows/WINDOWS_QUICKSTART.md)
- **Alias not working** → Check [Shell Aliases](ALIASES.md)
- **Health check fails** → Use bash version or simplified commands

---

## 📞 Getting Help

**Documentation Issues**: Check this index first  
**Setup Problems**: Review [Getting Started](GETTING_STARTED.md)  
**Platform-Specific**: See platform guides above  
**General Questions**: [GitHub Discussions](https://github.com/chokmah-me/claude-code-playbook/discussions)  
**Bug Reports**: [GitHub Issues](https://github.com/chokmah-me/claude-code-playbook/issues)  

---

## 🔄 Documentation Updates

This documentation is updated with each release. Check the main README for:
- Version information
- New features
- Updated guides
- Platform support changes

**Last Updated**: April 1, 2026 (v4.2.0)