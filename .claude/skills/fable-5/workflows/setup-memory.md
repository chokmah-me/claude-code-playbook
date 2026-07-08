---
name: setup-memory
description: "Create and maintain a memory system optimized for Fable 5's strengths in long-horizon work and compounding knowledge."
---

# Setup Fable 5 Memory System

## Purpose

Use this workflow when:
- You are using Fable 5 for multi-session or long-running work.
- You want lessons, corrections, and patterns to survive across turns and future Fable (or weaker model) sessions.
- You need to bootstrap or improve a memory system that Fable 5 actually uses well.

Fable 5 performs significantly better when it can reference persistent, structured lessons instead of re-deriving everything every time.

## Step 1: Assess Current Memory State

Check for existing memory:
- Any `memory/`, `lessons/`, `notes.md`, or similar files referenced in CLAUDE.md?
- Previous session summaries or reflection files?
- Loop state files or progress trackers?

Use Grep or list relevant directories if the user provides paths.

Report:
- What memory exists
- How well it is structured for Fable 5 (one lesson per file is ideal)
- Gaps (no reflection, no cross-session lookup, too verbose, etc.)

## Step 2: Design the Memory Structure

Recommend the Fable-optimized pattern (from Anthropic guidance + community):

```
memory/
├── lessons/
│   ├── 2026-07-07-refactor-pattern.md
│   ├── 2026-07-06-verification-anti-pattern.md
│   └── ...
├── reflections/
│   └── [date]-session-reflection.md
└── INDEX.md          # One-line summaries + when to reference
```

Rules to enforce:
- One lesson per file
- Top line: one-sentence summary
- Include "why it mattered" and "when to apply"
- Update in place rather than duplicate
- Delete or mark obsolete lessons

## Step 3: Bootstrap or Improve

If no memory system:
- Create the directory structure
- Generate initial lessons by reflecting on recent work (use subagents if a lot of history)
- Create INDEX.md

If system exists:
- Audit for duplication, bloat, or missing "why"
- Extract new lessons from the current conversation or last Fable run
- Improve INDEX.md for fast lookup

Always ask the user to review and approve before writing files.

## Step 4: Add Usage Instructions

Generate a small block the user can add to CLAUDE.md or a skill:

```markdown
## Memory for Fable 5
When working on long or recurring tasks, read relevant files from `memory/lessons/` and `memory/INDEX.md`.
After meaningful work, store one lesson per file in `memory/lessons/`.
Reference memory explicitly in future prompts.
```

## Output Format

```markdown
## Fable 5 Memory System

**Structure created/updated:**
- memory/lessons/
- memory/INDEX.md

**New lessons added:**
- [list]

**CLAUDE.md addition (copy this):**
[block]

**How to use going forward:**
- In every major Fable 5 session, include: "Reference memory/lessons/ and INDEX.md as needed."
- After the run: "Extract 1-3 lessons and write them to memory/lessons/ following the one-file rule."

Next time you use Fable 5, run `fable-5 prepare-session` and it will automatically weave in memory references.
```

## Anti-Patterns

❌ Dumping entire chat history into one giant memory file (Fable 5 prefers targeted lookup)
❌ Never referencing memory in prompts (the model won't magically use it)
❌ Writing vague lessons without "why it mattered" or "when to use"
❌ Letting memory grow without periodic cleanup

✅ One focused lesson per file
✅ Top-line summary for fast scanning
✅ Explicit instruction to the model to read memory
✅ Combine with verifier subagents for better quality lessons