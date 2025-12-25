# 💡 Shell Productivity Aliases

**Complete guide to shell shortcuts that save 8+ minutes per day.**

---

## 🚀 Overview

The Claude Code Playbook includes productivity aliases for both **Bash/Zsh** (Linux/Mac) and **PowerShell** (Windows). These shortcuts reduce typing and speed up common workflows.

**Time Savings**: 10 seconds per command × 50 commands/day = **8+ minutes/day**

---

## 🐧 Linux/Mac (Bash/Zsh)

### Setup
```bash
# Add aliases to your shell profile
cat templates/.bash_aliases.template >> ~/.bashrc

# Reload your shell configuration
source ~/.bashrc

# Or add to ~/.zshrc if using Zsh
cat templates/.bash_aliases.template >> ~/.zshrc
source ~/.zshrc
```

### Available Aliases

#### Core Commands
| Alias | Full Command | Description |
|-------|--------------|-------------|
| `cc` | `claude --dangerously-skip-permissions` | Claude with skip permissions |
| `cchelp` | `claude help` | Show Claude help |
| `cccost` | `claude cost` | Check current token usage |
| `ccclear` | `claude clear` | Clear conversation context |

#### Refactoring Workflows
| Alias | Full Command | Description |
|-------|--------------|-------------|
| `cctriage` | `claude skills refactoring triage` | Analyze codebase issues |
| `ccnew` | `claude skills refactoring qnew` | Start new refactoring session |
| `ccplan` | `claude skills refactoring qplan` | Create refactoring plan |
| `cccode` | `claude skills refactoring qcode` | Generate refactored code |
| `cccatchup` | `claude skills refactoring catchup` | Restore context after reset |
| `ccextract` | `claude skills refactoring extract` | Extract functions/methods |
| `ccmodernize` | `claude skills refactoring modernize` | Modernize code patterns |

#### Git Integration
| Alias | Full Command | Description |
|-------|--------------|-------------|
| `cccommit` | `claude skills refactoring commit` | Generate commit message |
| `ccpr` | `claude skills refactoring pr` | Create pull request description |

#### Health & Validation
| Alias | Full Command | Description |
|-------|--------------|-------------|
| `cchealth` | `bash scripts/check_config_health.sh` | Run health check |
| `cctest` | `claude test` | Run project tests |
| `cctype` | `claude type-check` | Run type checking |
| `cclint` | `claude lint` | Run linting |
| `cccheck` | `claude validate` | Validate configuration |

#### Utility Commands
| Alias | Full Command | Description |
|-------|--------------|-------------|
| `ccskills` | `claude skills` | List available skills |
| `cccontext` | `claude context` | Show current context |
| `ccreset` | `claude reset` | Reset to initial state |

---

## 🪟 Windows (PowerShell)

### Setup
```powershell
# Method 1: Automated setup (recommended)
. scripts/powershell/setup_powershell_profile.ps1

# Method 2: Manual loading for current session
. scripts/powershell/cc-aliases.ps1

# Method 3: Add to your PowerShell profile manually
notepad $PROFILE
# Then add the contents of cc-aliases.ps1
```

### PowerShell Execution Policy
If you encounter execution policy errors:
```powershell
# Check current policy
Get-ExecutionPolicy

# Set policy for current user (if needed)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Available PowerShell Aliases

PowerShell includes all the Bash aliases above, plus Windows-specific ones:

#### Windows-Specific Commands
| Alias | Function | Description |
|-------|----------|-------------|
| `cchealth` | `Test-PlaybookHealth` | Run comprehensive health check |
| `ccconfig` | `Show-PlaybookConfig` | Display current configuration |
| `ccmcp` | `Show-MCPServers` | List configured MCP servers |
| `ccupdate` | `Update-Playbook` | Check for playbook updates |

#### PowerShell Functions
The PowerShell setup includes these custom functions:
- `Test-PlaybookHealth` - Comprehensive configuration check
- `Show-PlaybookConfig` - Display all configuration files
- `Show-MCPServers` - List enabled MCP servers
- `Update-Playbook` - Check for and apply updates

---

## 🎯 Usage Examples

### Daily Workflow (Linux/Mac)
```bash
# Start your day
ccclear          # Clear overnight context
cchealth         # Check system health
ccnew            # Start new session

# Work on a feature
cctriage         # Analyze current issues
ccplan           # Plan your approach
cccode           # Generate implementation
cccommit         # Commit your changes

# End of session
cccost           # Check token usage
ccclear          # Clear sensitive context
```

### Daily Workflow (Windows)
```powershell
# Start your day
ccclear          # Clear overnight context
cchealth         # Check system health
ccnew            # Start new session

# Work on a feature
cctriage         # Analyze current issues
ccplan           # Plan your approach
cccode           # Generate implementation
cccommit         # Commit your changes

# End of session
cccost           # Check token usage
ccclear          # Clear sensitive context
```

### Quick Commands
```bash
# Check costs frequently
cccost

# Reset when things get messy
ccclear

# Get help
cchelp

# Quick health check
cchealth
```

---

## 🔧 Customization

### Adding Custom Aliases

**Linux/Mac:**
Add to your `~/.bashrc` or `~/.zshrc`:
```bash
# Custom Claude aliases
alias ccmine='claude skills refactoring myworkflow'
alias ccdebug='claude --debug'
```

**Windows PowerShell:**
Add to your PowerShell profile:
```powershell
# Custom Claude functions
function cc-mine { claude skills refactoring myworkflow }
function cc-debug { claude --debug }

# Custom aliases
Set-Alias ccmine cc-mine
Set-Alias ccdebug cc-debug
```

### Modifying Existing Aliases

**PowerShell users can customize functions:**
```powershell
# Edit the cc-aliases.ps1 file
notepad scripts/powershell/cc-aliases.ps1

# Or override specific functions in your profile
function cc-health {
    Write-Host "Running custom health check..."
    # Your custom implementation
}
```

---

## 📊 Productivity Metrics

**Time Savings Breakdown:**
- **Typing saved**: ~5 seconds per command
- **Command recall**: ~3 seconds (no need to remember full commands)
- **Error reduction**: ~2 seconds (fewer typos)
- **Total per command**: ~10 seconds

**Daily Impact:**
- 50 commands/day × 10 seconds = **8.3 minutes saved per day**
- 8.3 minutes × 5 days/week = **41.5 minutes saved per week**
- 41.5 minutes × 52 weeks/year = **36 hours saved per year**

**Learning Curve:**
- **Day 1**: Basic aliases (cc, ccclear, cccost)
- **Week 1**: Workflow aliases (cctriage, ccnew, cccatchup)
- **Month 1**: Advanced aliases (cchealth, cccommit, ccpr)

---

## 🚨 Troubleshooting

### Aliases Not Working (Linux/Mac)
```bash
# Check if aliases are loaded
alias | grep cc

# Reload your shell configuration
source ~/.bashrc  # or ~/.zshrc

# Check if alias file was appended
cat ~/.bashrc | grep -A 20 "Claude Code Aliases"
```

### PowerShell Aliases Not Working
```powershell
# Check if functions are loaded
Get-Command cc* -CommandType Function

# Reload aliases for current session
. scripts/powershell/cc-aliases.ps1

# Check execution policy
Get-ExecutionPolicy

# Check profile location
$PROFILE
```

### Commands Not Found
```bash
# Verify Claude Code installation
claude --version

# Check PATH
echo $PATH

# Test basic command
claude help
```

---

## 📚 Related Documentation

- **[Getting Started](GETTING_STARTED.md)** - Complete setup guide
- **[Configuration](CONFIGURATION.md)** - Best practices and settings
- **[Token Economics](TOKEN_ECONOMICS.md)** - Optimize token usage
- **[Success Guide](SUCCESS_GUIDE.md)** - Best practices and metrics

---

**Next Guide**: [Token Economics](TOKEN_ECONOMICS.md) →