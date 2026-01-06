# Quick Start Guide

Get productive with Claude Code Playbook in 15 minutes.

## Prerequisites

Before starting, ensure you have:
- [x] Claude Code installed and configured
- [x] Python 3.8+ **OR** Node.js 18+ (depending on your project)
- [x] Git initialized in your project
- [x] Text editor (VS Code, nano, vim, etc.)

**Check Prerequisites:**
```bash
# Verify Claude Code
claude --version

# Verify Python or Node.js
python --version  # OR node --version

# Verify Git
git --version
```

---

## 15-Minute Setup

### Step 1: Clone the Playbook (1 minute)

```bash
# Clone to a temporary location
cd ~/temp  # or any temporary directory
git clone https://github.com/chokmah-me/claude-code-playbook.git
cd claude-code-playbook
```

### Step 2: Copy Templates to Your Project (3 minutes)

```bash
# Set your project path
PROJECT_PATH="/path/to/your/project"

# Copy core templates
cp templates/CLAUDE.md.template $PROJECT_PATH/CLAUDE.md
cp templates/.cursorrules.template $PROJECT_PATH/.cursorrules

# Copy Claude Code configuration
mkdir -p $PROJECT_PATH/.claude/commands
cp templates/.claude/settings.json.template $PROJECT_PATH/.claude/settings.json

# Copy MCP configuration (optional)
cp templates/.mcp.json.template $PROJECT_PATH/.mcp.json

# Copy gitignore additions
cat templates/.gitignore.claude >> $PROJECT_PATH/.gitignore

# Copy example slash commands
cp templates/.claude/commands/* $PROJECT_PATH/.claude/commands/
```

**For Windows (PowerShell):**
```powershell
$PROJECT_PATH = "C:\path\to\your\project"
Copy-Item templates\CLAUDE.md.template $PROJECT_PATH\CLAUDE.md
Copy-Item templates\.cursorrules.template $PROJECT_PATH\.cursorrules
New-Item -Path $PROJECT_PATH\.claude\commands -ItemType Directory -Force
Copy-Item templates\.claude\settings.json.template $PROJECT_PATH\.claude\settings.json
```

### Step 3: Customize CLAUDE.md (5 minutes)

Edit `CLAUDE.md` in your project:

```bash
cd $PROJECT_PATH
nano CLAUDE.md  # or: code CLAUDE.md, vim CLAUDE.md
```

**Update these sections:**

1. **Project Overview**
   ```markdown
   # Replace generic text with:
   **Name**: Your Project Name
   **Stack**: Python 3.10, NumPy, FastAPI (your actual stack)
   ```

2. **Validation Commands**
   ```markdown
   # Update with your actual commands:
   npm test          # OR: pytest tests/
   npm run lint      # OR: flake8 src/
   npm run type-check # OR: mypy src/
   ```

3. **Key File Locations**
   ```markdown
   # Add your project-specific paths:
   - Main logic: `src/core/`
   - API routes: `src/routes/`
   - Database: `src/database/`
   ```

**Quick Customization Checklist:**
- [ ] Project name updated
- [ ] Tech stack specified
- [ ] Validation commands correct
- [ ] Key paths documented
- [ ] Budget constraints reviewed

### Step 4: Configure Permissions (2 minutes)

Edit `.claude/settings.json`:

```bash
nano .claude/settings.json  # or: code .claude/settings.json
```

**Customize allowedCommands for your project:**

```json
{
  "allowedTools": ["Edit", "Write", "Bash"],
  "allowedCommands": [
    "git add",
    "git commit",
    "git status",
    "git diff",
    
    // Add your test commands
    "npm test",           // OR "pytest tests/"
    "npm run build",      // OR "python -m build"
    
    // Add your validation commands
    "npm run lint",       // OR "flake8 src/"
    "npm run type-check"  // OR "mypy src/"
  ]
}
```

### Step 5: Test the Setup (4 minutes)

```bash
# Navigate to your project
cd $PROJECT_PATH

# Test: Load context
/clear
claude skills refactoring qnew
```

**Expected Output:**
```
✅ Context loaded and understood!

I'm ready to help with refactoring. What would you like to work on today?

Suggestions based on project state:
1. Run `triage` to identify technical debt hotspots
2. Continue existing refactoring work (if in progress)
3. Extract a specific function or module
4. Modernize a specific file's patterns
5. Something else?
```

**If successful, continue:**

```bash
# Test: Analyze codebase
claude skills refactoring triage
```

**Expected:** Should scan your files and identify top 3 refactoring priorities.

```bash
# Test: Check token usage
/cost
```

**Expected:** Should show token consumption for the session.

---

## Verification Checklist

After setup, verify everything works:

- [ ] `claude skills refactoring qnew` loads without errors
- [ ] `claude skills refactoring triage` identifies files correctly
- [ ] `/cost` command shows token usage
- [ ] CLAUDE.md reflects your project specifics
- [ ] `.claude/settings.json` has your validation commands
- [ ] Custom slash commands exist in `.claude/commands/`

---

## Common Setup Issues

### Issue: "Workflow not found"

**Cause:** Claude can't find the skills directory

**Fix:**
```bash
# Verify you're in the project directory
pwd

# Check if skills were copied
ls .claude/skills/

# If missing, copy from playbook:
cp -r ~/temp/claude-code-playbook/.claude/skills .claude/
```

### Issue: "Permission denied" on commands

**Cause:** Commands not in allowlist

**Fix:**
```bash
# Edit settings.json
nano .claude/settings.json

# Add the failing command to allowedCommands
```

### Issue: CLAUDE.md validation fails

**Cause:** File too large or contains problematic content

**Fix:**
```bash
# Check size
wc -l CLAUDE.md

# If > 100 lines, trim to essentials
# Remove: style guides, obvious info, lengthy docs
```

---

## Next Steps

Now that setup is complete:

1. **Learn the Workflows**
   - Read: [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md)
   - Explore: [skills/README.md](../skills/README.md)

2. **Run Your First Session**
   ```bash
   /clear
   claude skills refactoring qnew
   claude skills refactoring triage
   # Pick a file and start refactoring
   ```

3. **Set Up Shell Aliases** (Optional but recommended)
   ```bash
   # Add to ~/.bashrc or ~/.zshrc
   cat templates/.bash_aliases.template >> ~/.bashrc
   source ~/.bashrc
   
   # Now use shortcuts:
   cc              # Claude with skip permissions
   cctriage        # Run triage workflow
   ccnew           # Start new session
   ```

4. **Configure MCP Servers** (If needed)
   - Read: [docs/MCP_SETUP.md](MCP_SETUP.md)
   - Enable: GitHub, Postgres, Sentry as needed

5. **Monthly Maintenance**
   ```bash
   # Run health check
   bash scripts/check_config_health.sh
   ```

---

## Project-Specific Guides

Choose based on your project type:

### Python Scientific Projects
- Primary Skill: `python-scientific`
- Template: `templates/CLAUDE.md.template` (already optimized)
- Key Patterns: Vectorization, reproducibility, type hints
- Read: [skills/python-scientific/SKILL.md](../skills/python-scientific/SKILL.md)

### TypeScript/JavaScript Projects
- Primary Skill: `refactoring`
- Focus: Modern patterns, Result monads, functional composition
- Read: [skills/refactoring/knowledge/typescript-style.md](../skills/refactoring/knowledge/typescript-style.md)

### General Projects
- Mix both skills as needed
- Decision tree: [skills/README.md](../skills/README.md)

---

## Getting Help

**Documentation:**
- [Workflow Guide](WORKFLOW_GUIDE.md) - Detailed workflow usage
- [Troubleshooting](TROUBLESHOOTING.md) - Common issues and fixes
- [MCP Setup](MCP_SETUP.md) - External tool integration
- [FAQ](FAQ.md) - Frequently asked questions

**Community:**
- GitHub Issues: Bug reports and feature requests
- GitHub Discussions: Questions and sharing experiences
- Success Stories: Share your wins!

**Official Resources:**
- [Claude Code Docs](https://docs.anthropic.com/claude-code)
- [Anthropic Blog](https://www.anthropic.com/blog)

---

## Success Indicators

You're set up correctly when:

1. ✅ Workflows execute without errors
2. ✅ Token usage stays under 25K per session
3. ✅ Context resets work smoothly (/clear + catchup)
4. ✅ Validation commands pass before commits
5. ✅ You're productive within 30 minutes of starting

---

## Quick Reference Card

**Essential Commands:**
```bash
# Session Management
/clear                              # Reset context
/cost                               # Check token usage
/context                            # See what's loaded

# Workflows
claude skills refactoring qnew      # Start session
claude skills refactoring triage    # Find issues
claude skills refactoring extract   # Extract code
claude skills refactoring catchup   # Resume after /clear

# Validation
npm test          # Run tests (adjust for your project)
npm run lint      # Lint code
npm run type-check # Type checking
```

**Session Protocol:**
```bash
# Every 5-7 prompts:
/cost
/clear
claude skills refactoring catchup
```

---

**Time Investment:** 15 minutes  
**Expected ROI:** 2+ hours saved per week  
**Support:** [Open an issue](https://github.com/chokmah-me/claude-code-playbook/issues) if you get stuck

**Ready to start? Run the first workflow:**
```bash
claude skills refactoring qnew
```
