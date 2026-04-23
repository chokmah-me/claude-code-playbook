# Skill: Skill Creator
> "Design first, then build; formalize intent into systems."

## Overview
Create new skills from pure intent — describe what you need, and this skill generates a complete, production-ready skill with all files, validation, and mirroring. Complements the reactive `skill-extractor` (which mines existing sessions) by enabling proactive skill design driven by domain goals.

**Primary Goal:** Generate a well-formed skill in <2K tokens that passes quality standards and is immediately usable in the playbook.

---

## Skill Structure

```
.claude/skills/skill-creator/
├── SKILL.md              # This file - overview and router
├── knowledge/
│   └── quality-standards.md   # Token budgets, required sections, validation checklist
└── workflows/
    ├── create.md         # Design and generate a complete skill from intent
    └── audit.md          # Validate an existing skill against quality standards
```

---

## Workflow Selection

| Situation | Workflow | Tokens |
|-----------|----------|--------|
| "I need a skill that does X" | `create` | ~2K |
| "Does this skill meet our standards?" | `audit` | ~1K |

---

## Quick Reference

**create** — Design and generate a complete skill from intent
```
Use when: You have a domain/need and want a full skill (SKILL.md + workflows)
Output: 2 new skill directories (skills/ and .claude/skills/), README entry, validation report
```

**audit** — Validate a skill against quality standards
```
Use when: After creating a skill, or to assess an existing skill for compliance
Output: Pass/fail report by category (STRUCTURE, STEPS, TRIGGER, TOKEN_COST, MIRROR, REGISTRATION)
```

---

## Integration

- **Before creating**: Run `audit` on an existing skill to learn the standard
- **After creating**: Run `audit` against your new skill to confirm it passes
- **When refining**: Use `skill-extractor/refine` to fix issues identified by `audit`
- **Design reference**: See `knowledge/quality-standards.md` for all validation criteria

---

**Last Updated:** 2026-04-22
**Version:** 1.0
