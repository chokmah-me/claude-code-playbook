# Project Refactoring Constitution

<!--
  NOTE — This file is the Playbook's **example constitution**, demonstrating the
  CLAUDE.md "constitution" pattern with a TypeScript refactoring scenario. The
  claude-code-playbook repo *itself* is a Python/markdown project (pytest, scripts/);
  see README.md for this repo's actual tooling. Copy templates/CLAUDE.md.template into
  your own project and adapt it — don't use this file's npm/TypeScript commands verbatim.
  (HTML comments cost zero tokens, so this note is free.)
-->

<!-- session-recall:v1 — DO NOT EDIT MANUALLY -->
## Progressive Session Recall — RUN FIRST ON EVERY PROMPT

**Run `session-recall` FIRST on every prompt before doing anything else.** It costs ~50 tokens and prevents expensive blind searches.

```bash
session-recall files --json --limit 10  # recently touched files
session-recall files --days 7 --json    # files touched in last 7 days
session-recall list --json --limit 5    # recent sessions
session-recall list --days 2 --json     # sessions from last 2 days
session-recall search '<term>' --json   # full-text search
session-recall search '<term>' --days 5 # search last 5 days only
session-recall checkpoints --days 3     # checkpoints from last 3 days
session-recall repos --json             # discovered repositories across providers
session-recall show <id> --json         # drill into one session
session-recall health --json            # 8-dimension health check
session-recall schema-check             # validate DB schema (run after Copilot CLI upgrade)
```

**`--days N` works on all 4 query commands** (`list`, `files`, `checkpoints`, `search`) — filters to sessions/files/checkpoints from the last N days.

Only use filesystem tools (grep, glob, find) if session-recall returns nothing useful.
If `session-recall` errors, continue silently — it's a convenience, not a blocker.
<!-- /session-recall:v1 -->

> Systematic transformation from monolithic architecture to modern modular patterns

---

## ⚠️ SESSION & TOKEN MANAGEMENT

**Model & Environment:**
- Use the default Claude model set in Claude Code (typically the latest available)
- Work is designed for high-context Claude models (4.x series and above)

**Token Efficiency:**
- Monitor token usage via Claude Code UI (auto-visible in current version)
- For multi-session refactorings, maintain `REFACTOR_PROGRESS.md` for persistent state
- Use Plan Mode (`/plan` skill) for planning phase before implementation
- Use memory files and task lists for session continuity (no manual `/clear` workaround needed)

**Practical Guidelines:**
- Batch modifications into 10-15 file increments per session
- Use Explore subagents for codebase analysis (faster than manual grep)
- Commit atomically after meaningful milestones (every 2-4 files)

---

## ARCHITECTURAL GOALS

**Target State:** Modern modular architecture with feature-based organization

**Current State → Future State:**

| Current | Target |
|---------|--------|
| Monolithic files | Feature modules under `/src/features/` |
| Class inheritance | Functional composition with factory functions |
| Throw/catch error handling | Result<T,E> monads |
| Hardcoded business logic | Configuration-driven logic |
| Mixed concerns (god objects) | Manager/Endpoint/Database layers |
| Flat file structure | Domain-organized features |

**Key Modern Patterns:**
1. **Feature-based modules:** `src/features/{domain}/{manager,endpoint,database,types}.ts`
2. **Result monads:** All fallible operations return `Result<T, Error>`
3. **Functional composition:** Factory functions instead of classes
4. **Dependency injection:** Pass dependencies as parameters
5. **Configuration-driven:** Extract rules to config objects

**Reference:** See [.claude/skills/refactoring/knowledge/architecture-patterns.md](.claude/skills/refactoring/knowledge/architecture-patterns.md)

---

## REFACTORING WORKFLOWS

Use the refactoring skills system for all work:

**Typical Workflow:**
1. **Assess** — `claude skills refactoring triage` to find refactoring opportunities
2. **Plan** — Use Plan Mode or `claude skills refactoring qplan` to design the approach
3. **Implement** — `claude skills refactoring qcode` for batch implementation, or `extract`/`modernize` for focused changes
4. **Resume** — `claude skills refactoring catchup` when resuming after a break (reads REFACTOR_PROGRESS.md)

**For New Sessions:**
- Read `REFACTOR_PROGRESS.md` if it exists (shows prior work context)
- Run `claude skills refactoring triage` to assess current state
- Use Plan Mode for planning phase

**See:** [.claude/skills/refactoring/SKILL.md](.claude/skills/refactoring/SKILL.md) for complete workflow documentation.

---

## VALIDATION RULES

**Before ANY commit, ALL checks must pass:**

1. **Type Check:**
   ```bash
   npm run type-check
   ```
   **Expected:** 0 errors
   **If fails:** STOP and fix TypeScript errors before proceeding

2. **Unit Tests:**
   ```bash
   npm run test:unit
   ```
   **Expected:** All tests pass
   **If fails:** STOP and fix failing tests before proceeding

3. **Linting:**
   ```bash
   npm run lint
   ```
   **Expected:** 0 errors, 0 warnings
   **If fails:** Try `npm run lint -- --fix`, then manually fix remaining

**If ANY validation fails: DO NOT PROCEED. Fix the issue first.**

---

## API SURFACE PROTECTION

**Before modifying any exported function, class, or module:**

1. Search for all usages:
   ```bash
   grep -r "functionName" src/
   ```

2. Analyze impact of changes

3. Propose migration plan if breaking changes needed

4. Get explicit user approval before modifying

**Backwards compatibility is critical. When in doubt, ask.**

---

## COMMIT GUIDELINES

**Commit Frequency:**
- Commit after every 2-4 files modified
- Don't accumulate large changesets
- Atomic commits: one logical change per commit

**Commit Message Format:**
```
refactor: {brief description}

{detailed description of changes}

Changes:
- {specific change 1}
- {specific change 2}
- {specific change 3}

Tests: {passing/fixed}
Types: {passing}
Lint: {clean}

{context about why this change was made}
```

**Example:**
```
refactor: extract validateUserInput from main module

Extracted user validation logic to improve modularity and testability.

Changes:
- Created src/features/user/validate.ts with validation functions
- Updated main module to import and use new validation module
- Added 10 unit tests for validation logic
- All tests passing, type-check clean

Tests: 10 new tests, all passing
Types: No errors
Lint: Clean

Part of decomposing monolithic module (1200 LOC → target 500 LOC).
```

---

## PROGRESS TRACKING

**For multi-session refactorings, maintain `REFACTOR_PROGRESS.md`:**

```markdown
# Refactoring Progress

## Current Goal
Decompose monolithic module

## Session Info
- Started: 2025-12-01
- Token budget used: 18K / 44K
- Prompts used: 14 / 40

## Completed
- [x] Extracted validateUserInput (lines 145-230)
  - Created src/features/user/validate.ts
  - Added 10 tests, all passing
- [x] Extracted formatMessage (lines 350-420)
  - Created src/features/messages/format.ts
  - Added 8 tests, all passing

## In Progress
- [ ] Extract command parsing logic

## Pending
- [ ] Extract event handlers
- [ ] Modernize error handling to Result<T,E>
- [ ] Move to src/features/

## Blockers
None currently

## Notes
- Main module: 1200 LOC → 950 LOC (target: <500)
- All validations passing
- Need to check for circular dependencies before next extraction
```

---

## SESSION CONTINUITY PROTOCOL

**Between sessions (after stopping work):**
1. Update `REFACTOR_PROGRESS.md` with:
   - Completed tasks and files modified
   - Current goal and blockers
   - Next steps
2. Commit your work with descriptive commit messages
3. On next session, read `REFACTOR_PROGRESS.md` before resuming
4. Run `claude skills refactoring catchup` to restore context from progress file

**In-session token management:**
- Claude Code UI displays token usage continuously
- No need for manual `/cost` checks or `/clear` resets
- Memory system and task lists provide persistent context across turns

---

## ERROR HANDLING STRATEGY

**When TypeScript strict mode errors appear:**

1. **STOP immediately** - Do not proceed with other work
2. Read the error message carefully
3. Understand the root cause
4. Fix the error
5. Re-run type-check
6. Only proceed once type-check passes

**When tests fail:**

1. **STOP immediately**
2. Read test failure output
3. Determine if issue is:
   - Test needs updating (behavior intentionally changed)
   - Implementation is broken (unintentional behavior change)
4. Fix appropriately
5. Re-run tests
6. Only proceed once all tests pass

**When you're unsure:**
- Ask the user for guidance
- Don't guess or make assumptions
- Better to ask than to break things

---

## MINIMUM VIABLE REFACTOR

**Immediate Goal:** Keep application operational while refactoring

**Non-Negotiable:**
- Application must start without errors
- All features must continue working
- Events must be handled
- No user-facing behavior changes (unless explicitly requested)

---

## LEARNING AND IMPROVEMENT

**After Each Session:**
- Update REFACTOR_PROGRESS.md
- Note what worked well
- Note what was challenging
- Adjust approach for next session

**After Each Milestone:**
- Review overall progress
- Update this CLAUDE.md if needed
- Share learnings with team
- Celebrate progress!

---

## USEFUL REFERENCES

**In This Project:**
- [.claude/skills/refactoring/SKILL.md](.claude/skills/refactoring/SKILL.md) - Workflow documentation
- [.claude/skills/refactoring/knowledge/typescript-style.md](.claude/skills/refactoring/knowledge/typescript-style.md) - TypeScript patterns
- [.claude/skills/refactoring/knowledge/architecture-patterns.md](.claude/skills/refactoring/knowledge/architecture-patterns.md) - Modern architecture patterns

---

**Last Updated:** 2026-05-31
**Version:** 4.4.1
**License:** MIT
