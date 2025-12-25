# Claude Code Configuration Health Check (PowerShell - Simple Version)
# Run monthly to ensure optimal configuration
# This version avoids complex syntax that may fail in restricted environments

Write-Host "=== Claude Code Configuration Health Check ===" -ForegroundColor Cyan
Write-Host ""

# Check 1: CLAUDE.md line count
Write-Host "1. Checking CLAUDE.md size..." -ForegroundColor Yellow
if (Test-Path "CLAUDE.md") {
    try {
        $content = Get-Content "CLAUDE.md" -ErrorAction Stop
        $lineCount = $content.Count
        if ($lineCount -le 50) {
            Write-Host "   SUCCESS: CLAUDE.md has $lineCount lines (target: less than 50)" -ForegroundColor Green
        } else {
            Write-Host "   WARNING: CLAUDE.md has $lineCount lines (should be less than 50)" -ForegroundColor Red
        }
    } catch {
        Write-Host "   ERROR: Could not read CLAUDE.md" -ForegroundColor Red
    }
} else {
    Write-Host "   ERROR: CLAUDE.md not found" -ForegroundColor Red
}
Write-Host ""

# Check 2: Settings file exists
Write-Host "2. Checking .claude/settings.json..." -ForegroundColor Yellow
if (Test-Path ".claude/settings.json") {
    Write-Host "   SUCCESS: settings.json exists" -ForegroundColor Green
    try {
        $size = (Get-Item ".claude/settings.json").Length
        if ($size -lt 3072) {
            Write-Host "   SUCCESS: Size is $size bytes (target: less than 3KB)" -ForegroundColor Green
        } else {
            Write-Host "   WARNING: Size is $size bytes (consider simplifying)" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "   ERROR: Could not read settings file size" -ForegroundColor Red
    }
} else {
    Write-Host "   ERROR: settings.json not found" -ForegroundColor Red
}
Write-Host ""

# Check 3: MCP configuration (simplified)
Write-Host "3. Checking .mcp.json..." -ForegroundColor Yellow
if (Test-Path ".mcp.json") {
    Write-Host "   SUCCESS: .mcp.json exists" -ForegroundColor Green
    try {
        $mcpContent = Get-Content ".mcp.json" -Raw
        # Simple count of enabled servers
        $enabledCount = 0
        if ($mcpContent -match '"disabled"\s*:\s*false') {
            $enabledCount = ([regex]::Matches($mcpContent, '"disabled"\s*:\s*false')).Count
        }
        Write-Host "   INFO: Found $enabledCount enabled MCP servers"
        if ($enabledCount -gt 3) {
            Write-Host "   WARNING: Consider disabling rarely-used servers (each adds 400-800 tokens)" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "   ERROR: Could not read MCP configuration" -ForegroundColor Red
    }
} else {
    Write-Host "   INFO: .mcp.json not found (optional)" -ForegroundColor Yellow
}
Write-Host ""

# Summary
Write-Host "=== Summary ===" -ForegroundColor Cyan
Write-Host "Run this check monthly to maintain optimal performance"
Write-Host "Target token usage: less than 25K per session"
Write-Host "Use '/cost' command to monitor token spending"
Write-Host ""

# Alternative for PowerShell-restricted environments
Write-Host "=== Alternative Commands ===" -ForegroundColor Cyan
Write-Host "If PowerShell scripts fail, try these alternatives:"
Write-Host "  Linux/Mac: bash scripts/check_config_health.sh"
Write-Host "  Windows: Use Git Bash or WSL to run bash scripts"
Write-Host "  Simple check: Count lines in CLAUDE.md manually"
Write-Host ""