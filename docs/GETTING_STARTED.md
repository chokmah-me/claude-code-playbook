# 🚀 Getting Started with Claude Code Playbook

**Version**: 4.1.2 | **License**: MIT | **Repository**: https://github.com/dyb5784/claude-code-playbook

Complete cross-platform setup guide for the Claude Code Playbook - get productive in 15 minutes!

---

## 📋 Prerequisites

Before starting, ensure you have:
- **Claude Code** installed and configured
- **Git** installed (for cloning the repository)
- A **project directory** where you want to apply the playbook

---

## ⚡ 15-Minute Quick Start

### Step 1: Clone the Playbook (2 minutes)

**Linux/Mac:**
```bash
git clone https://github.com/dyb5784/claude-code-playbook.git
cd claude-code-playbook
```

**Windows PowerShell:**
```powershell
git clone https://github.com/dyb5784/claude-code-playbook.git
Set-Location claude-code-playbook
```

### Step 2: Copy Templates to Your Project (3 minutes)

**Linux/Mac:**
```bash
# Copy core configuration files
cp templates/CLAUDE.md.template /path/to/your/project/CLAUDE.md
cp templates/.cursorrules.template /path/to/your/project/.cursorrules
cp templates/.claude/settings.json.template /path/to/your/project/.claude/settings.json

# Optional: Copy additional templates
cp templates/.mcp.json.template /path/to/your/project/.mcp.json
cp templates/.gitignore.claude /path/to/your/project/.gitignore
```

**Windows PowerShell:**
```powershell
# Copy core configuration files
Copy-Item templates/CLAUDE.md.template C:\path\to\your\project\CLAUDE.md
Copy-Item templates/.cursorrules.template C:\path\to\your\project\.cursorrules
Copy-Item templates/.claude/settings.json.template C:\path\to\your\project\.claude\settings.json

# Optional: Copy additional templates
Copy-Item templates/.mcp.json.template C:\path\to\your\project\.mcp.json
Copy-Item templates/.gitignore.claude C:\path\to\your\project\.gitignore
```

### Step 3: Customize for Your Project (5 minutes)

**Edit the main configuration file:**

**Linux/Mac:**
```bash
nano /path/to/your/project/CLAUDE.md
# or use your preferred editor: vim, code, etc.
```

**Windows:**
```powershell
# Using Notepad
notepad C:\path\to\your\project\CLAUDE.md

# Using VS Code (if installed)
code C:\path\to\your\project\CLAUDE.md
```

**Key customization points in CLAUDE.md:**
- Project name and description
- Technology stack
- Key commands and paths
- Project-specific gotchas
- Testing procedures

### Step 4: Setup Shell Aliases (3 minutes)

**Linux/Mac (Bash/Zsh):**
```bash
# Add aliases to your shell profile
cat templates/.bash_aliases.template >> ~/.bashrc
source ~/.bashrc
```

**Windows PowerShell:**
```powershell
# Setup PowerShell profile with aliases
. scripts/powershell/setup_powershell_profile.ps1

# Or manually load aliases for current session
. scripts/powershell/cc-aliases.ps1
```

### Step 5: Test Your Setup (2 minutes)

**Navigate to your project and test:**

**Linux/Mac:**
```bash
cd /path/to/your/project
claude skills refactoring qnew
```

**Windows PowerShell:**
```powershell
Set-Location C:\path\to\your\project
ccnew          # Start new session (using alias)
# or
claude skills refactoring qnew
```

---

## ✅ Success Indicators

Your setup is successful if:
- ✅ Workflows execute without errors
- ✅ Token usage stays under 25K per session  
- ✅ Context resets work smoothly (`/clear` + `catchup`)
- ✅ Validation commands pass before commits
- ✅ You're productive within 30 minutes

---

## 🚀 Next Steps

Once your basic setup is working:

1. **Explore Workflows**: Try `triage`, `extract`, and `modernize`
2. **Read the Guides**: Check out [Configuration Guide](CONFIGURATION.md) and [Token Economics](TOKEN_ECONOMICS.md)
3. **Customize Further**: Add project-specific commands and MCP servers
4. **Join the Community**: Share your experience and get help

---

## 🆘 Troubleshooting

### Common Issues

**"Command not found" errors:**
- Ensure Claude Code is installed: `claude --version`
- Check that you're in the right directory
- Verify your PATH includes Claude Code

**Permission errors:**
- Check your `.claude/settings.json` configuration
- Ensure required permissions are granted
- Use `--dangerously-skip-permissions` flag if needed

**Template copy errors:**
- Verify source and destination paths exist
- Check file permissions
- Use absolute paths if relative paths fail

**PowerShell alias issues:**
- Run `. scripts/powershell/cc-aliases.ps1` to load aliases manually
- Check PowerShell execution policy: `Get-ExecutionPolicy`
- Set execution policy if needed: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Getting Help

- **Quick Start Issues**: See [Windows Quick Start](windows/WINDOWS_QUICKSTART.md) for Windows-specific help
- **Configuration Problems**: Run `python scripts/validate_config.py` or `powershell scripts/powershell/check_config_health.ps1`
- **Common Errors**: Check [GitHub Issues](https://github.com/dyb5784/claude-code-playbook/issues)
- **Workflow Questions**: See [Workflow Guide](WORKFLOW_GUIDE.md)

---

**Next Guide**: [Configuration Best Practices](CONFIGURATION.md) →