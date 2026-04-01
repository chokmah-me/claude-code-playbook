# Skill: Debugging & Root-Cause Analysis
> "Don't guess — trace, isolate, verify."

## Overview
Structured workflows for diagnosing failures instead of trial-and-error fixes. Complements the refactoring skill: refactoring builds, debugging diagnoses.

**Primary Goal:** Find the root cause of a bug or unexpected behavior systematically, not just suppress symptoms.

---

## Skill Structure

```
.claude/skills/debugging/
├── SKILL.md              # This file - overview and router
└── workflows/
    ├── diagnose.md       # Full root-cause analysis cycle
    └── trace.md          # Trace execution path through codebase
```

---

## Workflow Selection

| Situation | Workflow | Tokens |
|-----------|----------|--------|
| Bug report or test failure | `diagnose` | ~1.5K |
| "Where does X happen?" | `trace` | ~1K |

---

## Quick Reference

**diagnose** — Reproduce → Isolate → Hypothesize → Verify → Fix
```
Use when: a test fails, an error appears, behavior is wrong
Output: root cause identified, fix applied, regression test added
```

**trace** — Follow data/control flow through the codebase
```
Use when: you need to understand how a value propagates or where a function is called
Output: annotated call chain from entry point to effect
```

---

## Integration

- **Before refactoring**: Use `diagnose` to confirm a bug exists before changing code
- **After refactoring**: Use `diagnose` if tests fail post-change
- **During onboarding**: Use `trace` to understand unfamiliar code paths
