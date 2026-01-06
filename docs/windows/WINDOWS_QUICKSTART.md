# Windows 10 PowerShell Quick Start Guide
**Claude Code Playbook v4.1.0**

## Prerequisites
- ✓ Windows 10
- ✓ PowerShell 5.1+ (built-in) or PowerShell 7+ (recommended)
- ✓ Claude Code CLI installed

## 15-Minute Setup

### Step 1: Check PowerShell Version
```powershell
$PSVersionTable.PSVersion
# Should show 5.1 or higher
```

### Step 2: Run Automated Setup Script
```powershell
cd ~/.local/bin/scripts
.\setup_powershell_profile.ps1
```

This script will:
- Set execution policy to RemoteSigned
- Create profile directory if needed
- Backup existing profile

### Step 3: Verify Profile Is Loaded
```powershell
# Reload PowerShell (close and reopen terminal)
# OR run:
. $PROFILE

# You should see:
# "Claude Code profile loaded! (26 aliases)"
```

### Step 4: Verify Setup
```powershell
# Run health check
cchealth

# Check available aliases
Get-Alias | Where-Object { $_.Name -like 'cc*' }

# Test core commands
cccost
```

### Step 5: Start Using Workflows
```powershell
# Example workflows
cc "your task here"
ccnew
cctriage
cchealth
```

## Available Commands (26 Aliases)

### Core Commands (4)
- `cc` - Claude CLI
- `cchelp` - Display Claude help
- `cccost` - Check token usage
- `ccclear` - Clear context

### Workflow Shortcuts (9)
- `cctriage` - Run triage workflow
- `ccnew` - Start new feature workflow
- `ccextract` - Extract code to separate module
- `ccplan` - Create implementation plan
- `cccode` - Implement planned changes
- `ccreview` - Review recent code changes
- `ccfix` - Fix identified issue
- `ccmodernize` - Modernize code patterns
- `cccatchup` - Catch up on recent changes

### Git + Claude Integration (2)
- `cccommit` - Smart git commit (runs status + diff + Claude)
- `ccpr` - Create pull request

### Health & Configuration (6)
- `cchealth` - Run PowerShell health check
- `cchealthbash` - Run Bash health check (if Git Bash installed)
- `ccconfig` - View CLAUDE.md
- `ccsettings` - View settings.json (formatted)
- `ccmcp` - View .mcp.json (formatted)

### Navigation (2)
- `cdclaude` - Navigate to ~/.local/bin
- `cdbsi` - Navigate to G:\bsi-vortrag

### Testing (4)
- `cctest` - Run pytest with verbose output
- `cctype` - Run mypy type checking
- `cclint` - Run flake8 linting
- `cccheck` - Run all checks (type + lint + test)

## Daily Workflow

1. **Start PowerShell** - Profile auto-loads
2. **Check token budget** - `cccost`
3. **Work with Claude** - `cc "your task"`
4. **Monitor usage** - `cccost` every 3 prompts
5. **Reset context** - `ccclear` every 5-7 prompts
6. **Monthly health check** - `cchealth`

## Configuration Files

All configuration files are in `C:\Users\danie\.local\bin\`:

```
.local\bin\
├── CLAUDE.md                      (49 lines - project context)
├── .claude\
│   └── settings.json              (allowlists & permissions)
├── .mcp.json                      (MCP server config)
├── scripts\
│   ├── check_config_health.ps1    (PowerShell health check)
│   ├── check_config_health.sh     (Bash health check)
│   └── setup_powershell_profile.ps1
└── PLAYBOOK_IMPLEMENTATION.md     (full documentation)
```

PowerShell profile location:
```
C:\Users\danie\Documents\PowerShell\claude-code-profile.ps1
```

## Troubleshooting

### "Scripts are disabled on this system"
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Profile not loading
```powershell
# Reload manually
. $PROFILE

# Check if claude-code-profile.ps1 exists
Test-Path "$HOME\Documents\PowerShell\claude-code-profile.ps1"

# View profile location
$PROFILE
```

### Aliases not found after reload
```powershell
# Verify alias exists
Get-Alias cchelp

# If missing, reload profile
. $PROFILE

# Check for errors in profile loading
$Error[0]
```

### cchealth returns errors
```powershell
# Run with verbose output
& "$HOME\.local\bin\scripts\check_config_health.ps1"

# Verify config files exist
Test-Path "$HOME\.local\bin\CLAUDE.md"
Test-Path "$HOME\.local\bin\.claude\settings.json"
Test-Path "$HOME\.local\bin\.mcp.json"
```

### G:\bsi-vortrag not found
```powershell
# Check if drive exists
Test-Path "G:\bsi-vortrag"

# Navigate manually
cd G:\bsi-vortrag
```

## Token Budget Management

**Target:** <25K tokens per session (Claude Pro: 44K in 5 hours)

**Strategy:**
- Check `/cost` every 3 prompts
- Clear `/clear` every 5-7 prompts
- Use catchup workflow to restore context efficiently
- Run `cchealth` monthly to optimize configuration

**Workflow Costs:**
- Quick tasks (triage, qnew): ~2K tokens
- Planning (qplan): ~3K tokens
- Extraction: ~5K tokens
- Complex refactoring: 8-12K tokens
- Context restoration (catchup): 1-2K tokens

## Expected Performance Benefits

Based on playbook v4.1.0 metrics:

- **Setup time reduction:** 75% faster (15 min vs 60+ min)
- **Configuration errors:** 80% reduction
- **Token efficiency:** 15-20% improvement
- **Permission interruptions:** ~90% reduction

## Next Steps

- [x] Setup complete ✓
- [x] Profile loaded ✓
- [ ] Start using workflows
- [ ] Monitor token usage with `cccost`
- [ ] Run `cchealth` monthly
- [ ] Explore playbook documentation in PLAYBOOK_IMPLEMENTATION.md

## Additional Resources

- **Playbook Repository:** https://github.com/chokmah-me/claude-code-playbook
- **Full Implementation:** See `PLAYBOOK_IMPLEMENTATION.md`
- **Project Context:** See `CLAUDE.md`
- **Health Check:** Run `cchealth`

## Git Bash Compatibility

If you also use Git Bash:
- `.bash_aliases` file available for Bash shell
- `check_config_health.sh` for Bash health checks
- Both environments share same configuration files
- Use `cchealthbash` from PowerShell to run Bash health check

---

**Last Updated:** 2025-12-25
**Version:** 4.1.0
**Profile Location:** `C:\Users\danie\Documents\PowerShell\claude-code-profile.ps1`
