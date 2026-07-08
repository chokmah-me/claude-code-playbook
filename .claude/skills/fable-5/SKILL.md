# Skill: Fable 5
> "Maximize Fable 5 with its targeted prompts and scaffolding."

## Overview
Specialized skill for getting the most out of Claude Fable 5 (and Mythos-class models). Provides the best published Fable 5-specific prompts, official scaffolding patterns, memory systems, effort guidance, and harness audits. Designed for ambitious, long-horizon work in Claude Code.

Fable 5 benefits from smaller intent-focused prompts, explicit "why", strong verification, memory files, and subagent delegation — this skill encodes exactly those patterns.

**Primary Goal:** Turn Fable 5 access into reliably higher-quality, more autonomous results on complex tasks by using the right prompts and harness setup.

---

## Skill Structure

```
.claude/skills/fable-5/
├── SKILL.md
└── workflows/
    ├── prepare-session.md
    ├── run-targeted-prompts.md
    └── setup-memory.md
```

---

## Workflow Selection

| Situation | Workflow | Tokens |
|-----------|----------|--------|
| Starting a Fable 5 session or big task | `prepare-session` | ~800 |
| Want to run the actual best Fable 5 prompts | `run-targeted-prompts` | ~1.2K |
| Need memory or compounding knowledge for Fable | `setup-memory` | ~900 |

---

## Quick Reference

**prepare-session** — Prepare intent + scaffolding for Fable 5
Use when starting any significant Fable 5 work. Outputs a ready-to-paste session brief with official patterns.

**run-targeted-prompts** — Execute the best published Fable 5 prompts
Use when you want to apply the highest-leverage official + community prompts (Anthropic guide, Every library, Ken Huang blocks, etc.).

**setup-memory** — Create and maintain Fable-optimized memory system
Use to build persistent lesson files, cross-session state, and reflection loops that Fable 5 uses exceptionally well.

---

## Integration

- Complements `loop-engineering`, `skill-creator`, and your existing CLAUDE.md / AGENTS.md.
- Use before or during Fable 5 runs in Claude Code.
- Pair with `/goal` or long `/loop` sessions.
- After runs, feed results back into `setup-memory`.
- For harness-wide upgrades, combine with the meta prompts from the fable-5-meta-prompts collection.

**When Fable 5 is available:** Prioritize this skill for the hardest unsolved problems.
**When falling back to Opus:** The scaffolding still helps, but reduce ambition and effort expectations.