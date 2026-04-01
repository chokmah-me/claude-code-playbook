---
name: audit
description: "Scan for discrepancies between documentation claims and actual code"
---

# Documentation Audit

Systematically find where docs and code have drifted apart.

## Purpose

Use this workflow when:
- Preparing a release and need to verify docs are accurate
- After a major refactor that may have invalidated docs
- Periodic documentation hygiene (quarterly recommended)
- Before onboarding new team members

## Step 1: Inventory Documentation

**Actions:**
```
1. Find all documentation files:
   Glob("**/*.md") — filter to docs/, README.md, and any inline doc files

2. Categorize each doc file:
   - API reference (lists endpoints, functions, parameters)
   - Guide/tutorial (describes workflows or setup steps)
   - Configuration (lists settings, env vars, flags)
   - Architecture (describes structure, patterns, decisions)

3. Record the inventory as a checklist for Step 2
```

## Step 2: Cross-Reference Claims

For each documentation file, extract testable claims and verify them.

**Actions:**
```
Launch: Agent(subagent_type=Explore)

Task: Read [doc file] and extract every concrete claim:
- Function/class names mentioned → verify they exist (Grep)
- File paths referenced → verify they exist (Glob)
- CLI commands documented → verify they work or script exists
- Configuration options listed → verify they're read in code
- Feature descriptions → verify the feature is implemented

For each claim, report:
- VALID: claim matches code
- STALE: referenced item was renamed/moved
- MISSING: referenced item doesn't exist
- WRONG: claim contradicts actual behavior

Return as a table: [doc file:line] [claim] [status] [evidence]
```

## Step 3: Assess Severity

Classify each discrepancy:

```
🔴 CRITICAL — Doc promises a feature that doesn't exist
   (misleads users, causes support burden)

🟡 STALE — Doc references old name/path but feature exists
   (confusing but discoverable)

🟢 COSMETIC — Minor wording, formatting, or version number issues
   (low impact)
```

## Step 4: Generate Fix Plan

**Actions:**
```
For each discrepancy, produce a one-line fix:

| File:Line | Issue | Fix |
|-----------|-------|-----|
| docs/API.md:42 | `getUser()` renamed to `findUser()` | Update reference |
| README.md:15 | Claims WebSocket support | Remove or mark as planned |
| docs/CONFIG.md:8 | Lists `--verbose` flag | Flag was removed in v3 |

Sort by severity (🔴 first), then by file.
```

## Step 5: Apply Fixes

```
1. Fix all 🔴 CRITICAL items immediately
2. Fix 🟡 STALE items in a single commit
3. Log 🟢 COSMETIC items for later cleanup
4. Commit: "docs: fix [N] documentation discrepancies"
```

## Output Format

```markdown
## Documentation Audit Report

**Scanned**: [N] doc files, [M] testable claims
**Discrepancies**: [X] critical, [Y] stale, [Z] cosmetic

### Critical Issues
| File:Line | Claim | Reality |
|-----------|-------|---------|
| ... | ... | ... |

### Stale References
| File:Line | Old | Current |
|-----------|-----|---------|
| ... | ... | ... |

### Cosmetic
- [list]

### Recommendation
[1-2 sentences on overall doc health]
```
