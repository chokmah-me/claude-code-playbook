# Skill: Skill Extractor
> "If you did it twice, formalize it."

## Overview
Analyze Claude Code sessions to identify recurring workflows and extract them into reusable skill definitions. Transforms ad-hoc multi-step procedures into formalized skills that save tokens on future use.

**Primary Goal:** Detect repeated tool sequences and decision patterns in conversation history, then generate well-structured skill files.

---

## Skill Structure

```
.claude/skills/skill-extractor/
├── SKILL.md              # This file - overview and router
├── template.md           # Skill file template
└── workflows/
    ├── extract.md        # Detect patterns and create new skills
    └── refine.md         # Improve existing skills from usage feedback
```

---

## Workflow Selection

| Situation | Workflow | Tokens |
|-----------|----------|--------|
| "I keep doing the same thing" | `extract` | ~1.5K |
| "This skill needs improvement" | `refine` | ~1K |

---

## Quick Reference

**extract** — Detect repeated patterns in session history and generate a new skill
```
Use when: a workflow has been repeated 2+ times with 4+ steps
Output: new SKILL.md + workflow files following the standard pattern
```

**refine** — Improve an existing skill based on real usage feedback
```
Use when: a skill works but is too verbose, missing steps, or has wrong triggers
Output: updated skill files with improvements applied
```

---

## When to Extract vs. Not

**Good candidates:**
- Workflow repeated 2+ times in a session
- Multi-step procedure (4+ steps)
- Pattern with decision logic (if/else branches)
- Significant token savings (>200 tokens per use)
- Generalizable across projects

**Don't extract:**
- One-time operations
- Trivial 1-2 step tasks
- Highly context-specific workflows
- Patterns that duplicate existing skills

---

## Integration

- **After long sessions**: Run `extract` to capture patterns before they're lost
- **After skill usage**: Run `refine` when a skill didn't work as expected
- **With manifest-generator**: Update skill catalog after extraction
- **With skill-upgrader**: For deeper structural improvements beyond `refine`
