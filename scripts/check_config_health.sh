#!/bin/bash

# Claude Code Configuration Health Check v4.4.0
# Run monthly to maintain optimal configuration

set -e

echo "╔══════════════════════════════════════════════════════╗"
echo "║   Claude Code Configuration Health Check  v4.4.0   ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""

ISSUES_FOUND=0
WARNINGS_FOUND=0

RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

error()   { echo -e "${RED}❌ $1${NC}";    ISSUES_FOUND=$((ISSUES_FOUND + 1)); }
warning() { echo -e "${YELLOW}⚠️  $1${NC}"; WARNINGS_FOUND=$((WARNINGS_FOUND + 1)); }
success() { echo -e "${GREEN}✅ $1${NC}"; }
info()    { echo -e "${BLUE}ℹ️  $1${NC}"; }
section() { echo ""; echo "═══════════════════════════════════════════════════════"; echo "  $1"; echo "═══════════════════════════════════════════════════════"; }

# ── 1. CLAUDE.md ────────────────────────────────────────────────
section "1. CLAUDE.md Token Budget"

if [ ! -f "CLAUDE.md" ]; then
    error "CLAUDE.md not found in current directory"
else
    lines=$(wc -l < CLAUDE.md)
    words=$(wc -w < CLAUDE.md)
    tokens=$(echo "$words * 1.3 / 1" | bc 2>/dev/null || echo "~$((words * 13 / 10))")
    echo "   Lines: $lines | Words: $words | Est. tokens: $tokens"

    if [ "$tokens" -lt 350 ] 2>/dev/null; then
        success "CLAUDE.md token count excellent (< 350 tokens)"
    elif [ "$tokens" -lt 500 ] 2>/dev/null; then
        success "CLAUDE.md token count good (< 500 tokens)"
    elif [ "$tokens" -lt 800 ] 2>/dev/null; then
        warning "CLAUDE.md large (~$tokens tokens). Target: under 500. Trim framework-obvious content."
    else
        error "CLAUDE.md too large (~$tokens tokens). Paid on every turn. Trim aggressively."
    fi

    if grep -qi "indentation\|spaces\|tabs\|semicolon" CLAUDE.md 2>/dev/null; then
        warning "CLAUDE.md contains style guide content — use .claude/rules/ or a linter instead"
    fi
    if grep -qi "write clean code\|follow best practices\|team roster\|contact info" CLAUDE.md 2>/dev/null; then
        warning "CLAUDE.md contains generic advice Claude already knows — remove it"
    fi
    if ! grep -qi "test\|lint\|type.check\|validation" CLAUDE.md 2>/dev/null; then
        warning "CLAUDE.md missing validation commands section"
    fi
fi

# ── 2. .claudeignore ────────────────────────────────────────────
section "2. .claudeignore Configuration"

if [ -f ".claudeignore" ]; then
    entries=$(grep -c "^[^#]" .claudeignore 2>/dev/null || echo "0")
    success ".claudeignore present ($entries entries)"
    for must_have in "node_modules" "dist" "__pycache__" "*.lock" "coverage"; do
        if ! grep -q "$must_have" .claudeignore 2>/dev/null; then
            warning ".claudeignore missing recommended entry: $must_have"
        fi
    done
else
    warning ".claudeignore not found — Claude will proactively read node_modules, dist, lock files"
    info "Copy templates/.claudeignore to project root"
fi

# ── 3. permissions.deny in settings.json ─────────────────────────
section "3. permissions.deny (Hard Exclusions)"

if [ -f ".claude/settings.json" ]; then
    if command -v python3 &>/dev/null; then
        deny_count=$(python3 -c "
import json, sys
try:
    with open('.claude/settings.json') as f:
        cfg = json.load(f)
    deny = cfg.get('permissions', {}).get('deny', [])
    print(len(deny))
except Exception as e:
    print(0)
" 2>/dev/null || echo "0")
        echo "   permissions.deny entries: $deny_count"
        if [ "$deny_count" -eq 0 ]; then
            warning "No permissions.deny entries — .claudeignore alone is advisory only"
            info "Add deny entries for node_modules, dist, lock files"
        elif [ "$deny_count" -lt 5 ]; then
            warning "Only $deny_count deny entries — consider adding node_modules/**, dist/**, *.lock"
        else
            success "permissions.deny configured ($deny_count entries)"
        fi
    fi
else
    warning ".claude/settings.json not found"
fi

# ── 4. Security: .claude/ file integrity ────────────────────────
section "4. Security: .claude/ File Integrity"

if [ -f ".claude/settings.json" ]; then
    # Check for suspicious keys that the Mini Shai-Hulud worm inserts
    if command -v python3 &>/dev/null; then
        suspicious=$(python3 -c "
import json
try:
    with open('.claude/settings.json') as f:
        cfg = json.load(f)
    # Look for unexpected top-level keys
    expected = {'allowedTools','allowedCommands','permissions','mcpServers',
                'contextManagement','_security_note','env','hooks'}
    found = set(cfg.keys()) - expected
    if found:
        print('UNEXPECTED: ' + ', '.join(found))
    else:
        print('OK')
except Exception as e:
    print('ERROR: ' + str(e))
" 2>/dev/null || echo "SKIP")
        if echo "$suspicious" | grep -q "UNEXPECTED"; then
            error "Unexpected keys in .claude/settings.json: $suspicious"
            error "Possible persistence mechanism from supply chain compromise. Inspect and rotate credentials."
        elif echo "$suspicious" | grep -q "OK"; then
            success ".claude/settings.json keys look clean"
        fi
    fi
fi

if [ -f ".claude/settings.local.json" ]; then
    info ".claude/settings.local.json exists — verify you created this file"
fi

# Check for unexpected entries in MCP claude config
if [ -f "$HOME/.config/claude/claude_desktop_config.json" ]; then
    info "~/.config/claude/claude_desktop_config.json present — named target of Mini Shai-Hulud worm"
    info "Ensure it contains only MCP servers you explicitly configured"
fi

# ── 5. Path-scoped rules ─────────────────────────────────────────
section "5. Path-Scoped Rules (.claude/rules/)"

if [ -d ".claude/rules" ]; then
    total=$(find .claude/rules -name "*.md" 2>/dev/null | wc -l)
    scoped=$(grep -rl "^paths:" .claude/rules 2>/dev/null | wc -l)
    unscoped=$((total - scoped))
    echo "   Total rule files: $total | Scoped: $scoped | Unscoped (loads every session): $unscoped"
    if [ "$total" -eq 0 ]; then
        info "No .claude/rules/ files — consider moving domain-specific CLAUDE.md content here"
    else
        success ".claude/rules/ present"
        if [ "$unscoped" -gt 3 ]; then
            warning "$unscoped unscoped rule files load every session — add paths: frontmatter to scope them"
        fi
    fi
else
    info ".claude/rules/ not found — consider adding for path-scoped domain rules (41% overhead reduction)"
fi

# ── 6. MCP Servers ───────────────────────────────────────────────
section "6. MCP Server Configuration"

if [ -f ".mcp.json" ]; then
    if command -v python3 &>/dev/null; then
        mcp_info=$(python3 -c "
import json
try:
    with open('.mcp.json') as f:
        cfg = json.load(f)
    servers = cfg.get('mcpServers', {})
    total = len(servers)
    enabled = [k for k,v in servers.items() if isinstance(v, dict) and v.get('enabled', False)]
    print(f'total={total} enabled={len(enabled)} names={\" \".join(enabled)}')
except Exception as e:
    print('error')
" 2>/dev/null || echo "error")
        if echo "$mcp_info" | grep -q "total="; then
            total=$(echo "$mcp_info" | grep -o 'total=[0-9]*' | cut -d= -f2)
            enabled_count=$(echo "$mcp_info" | grep -o 'enabled=[0-9]*' | cut -d= -f2)
            names=$(echo "$mcp_info" | sed 's/.*names=//')
            echo "   Total: $total | Enabled: $enabled_count | Active: $names"
            if [ "$enabled_count" -eq 0 ]; then
                info "No MCP servers enabled (fine if not needed)"
            elif [ "$enabled_count" -le 3 ]; then
                success "MCP server count reasonable ($enabled_count enabled, ~$((enabled_count * 600)) token overhead)"
            else
                warning "$enabled_count MCP servers enabled (~$((enabled_count * 600)) token overhead/session)"
                info "Use ENABLE_TOOL_SEARCH=true to defer schemas until needed"
            fi
        fi
    fi
else
    info "No .mcp.json found"
fi

# ── 7. Headroom ──────────────────────────────────────────────────
section "7. Headroom Output Compression"

if command -v headroom &>/dev/null; then
    version=$(headroom --version 2>/dev/null || echo "installed")
    success "Headroom installed ($version)"
    info "Run 'headroom wrap claude' to compress session tool output (47–92% reduction)"
    if command -v headroom &>/dev/null; then
        headroom stats 2>/dev/null | head -5 || true
    fi
else
    info "Headroom not installed — optional but recommended for long sessions"
    info "Install: pip install 'headroom-ai[all]' && headroom wrap claude"
    info "Benchmarks: code search 92%, SRE debugging 92%, issue triage 73% token reduction"
fi

# ── 8. Skills System ─────────────────────────────────────────────
section "8. Skills System"

if [ -d ".claude/skills" ]; then
    skill_count=$(find .claude/skills -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l)
    if [ "$skill_count" -eq 0 ]; then
        error ".claude/skills directory exists but contains no skills"
    else
        success "Skills system configured ($skill_count skills)"
        find .claude/skills -mindepth 1 -maxdepth 1 -type d | while read skill; do
            echo "      - $(basename "$skill")"
        done
    fi
else
    error ".claude/skills directory not found — workflows will not function"
fi

# ── 9. Git Repository ────────────────────────────────────────────
section "9. Git Repository Health"

if git rev-parse --git-dir > /dev/null 2>&1; then
    success "Git repository initialized"
    if git status --porcelain | grep -q "CLAUDE.md\|.claude/"; then
        warning "Uncommitted Claude configuration changes — commit to share with team"
    fi
else
    error "Not a git repository — Claude Code works best with version control"
fi

# ── Summary ──────────────────────────────────────────────────────
section "Health Check Summary"

echo ""
if [ $ISSUES_FOUND -eq 0 ] && [ $WARNINGS_FOUND -eq 0 ]; then
    echo -e "${GREEN}╔══════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║  🎉 EXCELLENT! Configuration is healthy             ║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════╝${NC}"
    exit 0
elif [ $ISSUES_FOUND -eq 0 ]; then
    echo -e "${YELLOW}╔══════════════════════════════════════════════════════╗${NC}"
    echo -e "${YELLOW}║  ⚠️  GOOD — Minor improvements recommended           ║${NC}"
    echo -e "${YELLOW}╚══════════════════════════════════════════════════════╝${NC}"
    echo "Warnings: $WARNINGS_FOUND"
    exit 0
else
    echo -e "${RED}╔══════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}║  ❌ ISSUES FOUND — Action required                   ║${NC}"
    echo -e "${RED}╚══════════════════════════════════════════════════════╝${NC}"
    echo "Critical: $ISSUES_FOUND | Warnings: $WARNINGS_FOUND"
    exit 1
fi
