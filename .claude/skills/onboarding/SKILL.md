# Skill: Onboarding & Repo Orientation
> "You can't improve what you don't understand."

## Overview
Workflows for getting oriented in an unfamiliar codebase. Different from `catchup` (which resumes prior work) — onboarding assumes no prior context.

**Primary Goal:** Build a mental model of a codebase's architecture, conventions, and gotchas in minimal time.

---

## Skill Structure

```
.claude/skills/onboarding/
├── SKILL.md              # This file - overview and router
└── workflows/
    ├── orient.md         # Guided codebase walkthrough
    └── glossary.md       # Extract domain terms and vocabulary
```

---

## Workflow Selection

| Situation | Workflow | Tokens |
|-----------|----------|--------|
| "I'm new to this repo" | `orient` | ~2K |
| "What do these terms mean?" | `glossary` | ~1K |

---

## Quick Reference

**orient** — Structured codebase walkthrough: architecture → key files → conventions → gotchas
```
Use when: first time in a repo, or returning after months away
Output: mental model summary with annotated file map
```

**glossary** — Extract domain-specific terms and project vocabulary
```
Use when: the codebase uses unfamiliar domain terms or custom naming
Output: term → definition table with file references
```

---

## Integration

- **Before refactoring**: Run `orient` on unfamiliar modules before changing them
- **New team member**: `orient` + `glossary` as first two steps
- **Cross-team work**: `glossary` to align on terminology
