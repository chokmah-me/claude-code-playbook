# Skill: Documentation
> "Docs that drift from code are worse than no docs."

## Overview
Workflows for keeping documentation accurate and generating docs from code. Addresses the gap between what code does and what docs claim.

**Primary Goal:** Detect and fix documentation drift, and generate documentation from source code rather than writing it from scratch.

---

## Skill Structure

```
.claude/skills/documentation/
├── SKILL.md              # This file - overview and router
└── workflows/
    ├── audit.md          # Scan for code/docs drift
    └── generate.md       # Generate docs from code
```

---

## Workflow Selection

| Situation | Workflow | Tokens |
|-----------|----------|--------|
| "Are our docs accurate?" | `audit` | ~1.5K |
| "Generate docs for this module" | `generate` | ~1K |

---

## Quick Reference

**audit** — Compare documentation claims against actual code
```
Use when: after major changes, before releases, periodic hygiene
Output: list of discrepancies with file:line references and suggested fixes
```

**generate** — Create documentation from code signatures and comments
```
Use when: new module needs docs, existing docs are blank/stale
Output: markdown documentation reflecting current code state
```

---

## Integration

- **Before release**: Run `audit` to catch capability overstatement
- **After refactoring**: Run `generate` to update docs for changed modules
- **During onboarding**: `audit` output shows where docs can't be trusted
