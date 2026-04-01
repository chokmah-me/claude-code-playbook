# Agentic Patterns in Claude Code (2026)

Modern Claude Code workflows leverage native agentic capabilities for efficient multi-step tasks. This guide documents the patterns used in the Claude Code Playbook.

---

## Overview

As of April 2026, Claude Code includes:
- **Plan Mode** — Structured planning before implementation
- **Subagents** — Specialized agents (Explore, Plan, general-purpose)
- **Memory system** — Persistent session context
- **Task lists** — Tracked progress across turns
- **Background agents** — Parallel work execution

This playbook integrates all these patterns into refactoring workflows.

---

## Pattern 1: Plan Mode for Design

**When to use**: Before any multi-file refactoring or significant architectural change

**Workflow**:
1. User requests refactoring: "Add user authentication to the app"
2. Enter Plan Mode with `/plan` or via Plan skill
3. Claude explores current code, tests, dependencies
4. Claude designs step-by-step implementation plan
5. User reviews and approves plan
6. Exit with `ExitPlanMode` to begin implementation

**Example**:
```
/plan

Goal: Extract database layer from monolithic service.ts

Before proposing changes, explore:
1. Current service.ts structure and dependencies
2. Existing test coverage
3. What imports service.ts
4. Similar patterns in the codebase
```

**Result**: A detailed `.plan` file with clear steps, risk assessment, and file references.

---

## Pattern 2: Explore Subagent for Analysis

**When to use**: Fast, efficient codebase scanning without reading full files

**Typical task**:
```
Agent(subagent_type=Explore)

Task: Find all TypeScript files larger than 500 lines.
Return a table with:
- File path
- Line count
- Complexity indicators (any types, nested functions, etc.)
- Recommendation (extract, modernize, or leave)
```

**Why it works**:
- Explore agents use native file search tools (Glob, Grep)
- Faster than manual bash commands
- Structured output (tables, lists)
- Can analyze patterns across many files

**In refactoring context**:
- `triage` workflow launches Explore to identify debt hotspots
- Explore finds patterns, Claude prioritizes them
- Much faster than manual `find` + `wc -l` + `grep` chains

---

## Pattern 3: Task Lists for Progress Tracking

**When to use**: Multi-file changes, multi-session work, or complex operations

**Implementation**:
1. Create tasks at session start: `TaskCreate` for each major step
2. Mark as in-progress: `TaskUpdate(taskId, status: "in_progress")`
3. Complete and mark done: `TaskUpdate(taskId, status: "completed")`
4. Check progress anytime: `TaskList`

**Example task**:
```
TaskCreate({
  subject: "Extract validateUserInput to separate module",
  description: "Extract lines 145-230 from user.ts to user/validate.ts",
  activeForm: "Extracting user validation logic"
})
```

**Why it works**:
- Visible progress across many turns
- Survives context resets
- Helps estimate remaining work
- Clear next-step guidance

---

## Pattern 4: Memory System for Session Continuity

**When to use**: Multi-session projects, important decisions, project context

**Three types of memory**:

### User Memory
```markdown
---
name: user_role
type: user
---

User is a senior TypeScript engineer, first time touching Python backend.
Frame Python explanations in terms of TS analogues.
```

### Feedback Memory
```markdown
---
name: no_force_push_main
type: feedback
---

**Rule**: Never force-push to main branch
**Why**: Lost work in prior incident
**How to apply**: Use regular commits, request reviews before any rebase
```

### Project Memory
```markdown
---
name: mobile_release_freeze
type: project
---

**Fact**: Merge freeze begins 2026-04-10 for mobile v2.0 release
**Why**: Release cut, no breaking changes allowed
**How to apply**: Complete refactors before 2026-04-10
```

**Location**: `.claude/projects/{project-name}/memory/`
**Index**: `MEMORY.md` (auto-loaded each session)

---

## Pattern 5: Persistent Progress File (REFACTOR_PROGRESS.md)

**When to use**: Multi-session refactorings (the most reliable session continuity)

**Structure**:
```markdown
# Refactoring Progress

## Current Goal
Extract database layer from monolithic service

## Session Info
- Started: 2026-04-01
- Files to modify: [list]

## Completed
- [x] Extracted validateUserInput (lines 145-230)
  - Created user/validate.ts
  - Tests: 10 passing

## In Progress
- [ ] Extract formatMessage

## Pending
- [ ] Extract error handlers

## Blockers
None

## Notes
- Service.ts: 1200 LOC → 950 LOC (target: <500)
- All tests passing
```

**Why it works**:
- Plain text (readable by humans and LLMs)
- Persists in git (no `.gitignore`)
- Claude reads it automatically on `catchup`
- Tracks what changed between sessions
- No setup required (just a file in the repo root)

---

## Pattern 6: Background Agents for Parallel Work

**When to use**: Long-running tasks that don't block other work

**Example**:
```
Agent(run_in_background=true)

Task: Run full test suite on the refactored code.
Commands:
- npm run test:unit
- npm run type-check
- npm run lint

Return results when done.
```

**Workflow**:
1. Start background task
2. Continue with other work (reading files, planning next steps)
3. Claude notifies when task completes
4. Review results and proceed

**In refactoring**:
- Start tests while implementing next file
- Check linting while writing new modules
- Reduces idle time waiting for slow commands

---

## Pattern 7: Atomic Commits with Clear Messages

**When to use**: After every 2-4 file modifications

**Format**:
```
refactor: extract database layer from service

Decomposed monolithic service.ts into separate database module for:
- Improved testability
- Reduced coupling
- Clearer separation of concerns

Changes:
- Created src/database/connection.ts (new)
- Created src/database/queries.ts (new)
- Updated service.ts:lines 20-100 to import database module
- Updated tests/service.test.ts imports

Tests: 45 passing (unchanged)
Types: No errors
Lint: Clean

Reduces service.ts from 1200 to 950 LOC. On track for <500 target.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

**Why it works**:
- Clear history of what changed and why
- `git blame` shows context for future maintainers
- Enables easy rollback if needed
- Atomic (each commit = independent change)

---

## Integrated Workflow: From Plan to Commit

Here's how all patterns work together:

```
Session Start
    ↓
1. Read REFACTOR_PROGRESS.md (continuity)
2. Read MEMORY.md (context)
    ↓
3. /plan → Design phase
    ↓
4. ExitPlanMode (approve plan)
    ↓
5. TaskCreate for major steps
    ↓
6. For each file:
   - Read related code (Explore if large codebase)
   - Implement change
   - Update task: TaskUpdate(status: "in_progress")
   - Validate (type-check, tests, lint)
   - Commit atomically
   - Mark task done: TaskUpdate(status: "completed")
    ↓
7. Update REFACTOR_PROGRESS.md
    ↓
8. Session end:
   - Final validation
   - Commit progress file
   - Save snapshot (optional)
```

---

## Comparison: 2025 vs 2026 Patterns

| Task | 2025 | 2026 |
|------|------|------|
| **Session continuity** | `/clear` + `catchup` every 5 prompts | REFACTOR_PROGRESS.md + memory files |
| **Budget awareness** | Manual `/cost` checks | Claude Code UI (automatic) |
| **Code analysis** | Manual bash: `find`, `wc -l`, `grep` | Explore subagent (Glob/Grep tools) |
| **Planning** | Text prompts, hope for clarity | Plan Mode (structured, reviewable) |
| **Progress tracking** | `catchup` workflow | TaskList + REFACTOR_PROGRESS.md |
| **Model version** | Hardcoded "Sonnet 4.5" | Use current default Claude model |
| **Context resets** | Every 5-7 prompts | Rarely needed (persistent memory) |

---

## Best Practices

### ✅ DO

- Use Plan Mode before major refactorings
- Maintain REFACTOR_PROGRESS.md throughout multi-session work
- Run Explore subagent for large codebase analysis
- Commit after every 2-4 files
- Update task status as you progress
- Save important decisions in memory files
- Trust Claude Code UI for token visibility

### ❌ DON'T

- Manual `/clear` resets (unnecessary)
- Hardcode model names in documentation
- Manually grep/find large codebases (use Explore)
- Accumulate 20+ file changes before committing
- Rely on verbal memory (write to memory files)
- Preset token budgets (use actual Claude capabilities)
- Skip validation (tests, types, lint) between files

---

## Resources

- [CLAUDE.md](../CLAUDE.md) — Constitution template for new projects
- [TOKEN_ECONOMICS.md](TOKEN_ECONOMICS.md) — Budget planning
- [Refactoring Skill](../skills/refactoring/SKILL.md) — Refactoring workflows
- [Session Snapshot Skill](../skills/session-snapshot/README.md) — Crash recovery

---

**Last Updated**: 2026-04-01
**Version**: 4.2.0
