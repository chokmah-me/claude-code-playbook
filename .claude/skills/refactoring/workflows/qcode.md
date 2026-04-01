---
name: qcode
description: "Execute approved refactoring plan with validation"
---

# Execute Refactoring Plan

Implement a refactoring plan file-by-file with comprehensive validation after each change.

## Prerequisites

- ✅ Approved plan from `qplan` (or clear understanding of changes needed)
- ✅ REFACTOR_PROGRESS.md created (or will be during execution)
- ✅ All tests passing before starting

## Workflow Overview

```
1. Create/load REFACTOR_PROGRESS.md
2. For each file in plan:
   - Implement changes
   - Validate (type-check + tests + lint)
   - Commit atomically
   - Update progress file
3. Final verification suite
4. Mark session complete
```

## Step 1: Initialize Progress Tracking

Create or update `REFACTOR_PROGRESS.md`:

```markdown
# Refactoring Progress

## Current Goal
[Description of refactoring objective]

## Session Info
- Started: [date]
- Files to modify: [list]
- Target: [pattern or state]

## Completed
(none yet)

## In Progress
- [ ] [file 1]

## Pending
- [ ] [file 2]
- [ ] [file 3]

## Blockers
None currently
```

## Step 2: Implement File-by-File

For each file in the plan:

1. **Make changes** - Implement the refactoring
2. **Validate** - Run validation gates:
   ```bash
   npm run type-check  # No TypeScript errors
   npm run test:unit   # All tests pass
   npm run lint        # No linting issues
   ```
3. **Commit atomically** - One logical change per commit:
   ```bash
   git commit -m "refactor: [description]

   Changes:
   - [specific change 1]
   - [specific change 2]

   Tests: passing
   Types: clean
   Lint: clean"
   ```
4. **Update progress** - Mark file as completed

## Step 3: Track Progress

After each file, update `REFACTOR_PROGRESS.md`:

```markdown
## Completed
- [x] Extract validateInput to src/features/validation/validate.ts
  - Created new module with validation logic
  - Added 8 unit tests
  - Updated imports in [3 files]
  - All tests passing

## In Progress
- [ ] Extract formatOutput to src/features/output/format.ts
```

## Step 4: Hard Stops

**STOP immediately if:**
- ❌ TypeScript errors appear → Fix before proceeding
- ❌ Tests fail → Revert or fix implementation
- ❌ Linting fails → Fix before proceeding
- ❌ 15 files modified → Commit, save progress, stop session

## Step 5: Final Validation

When plan is complete:

```bash
# Full test suite
npm run test:unit

# Type check entire project
npm run type-check

# Lint entire project
npm run lint

# Check no regressions
npm run test:unit -- --coverage
```

## Step 6: Session Wrap-up

Update REFACTOR_PROGRESS.md final state:

```markdown
## Session Summary
- **Started**: [date/time]
- **Completed**: [X] of [Y] planned files
- **Commits**: [number]
- **Tests**: [count] passing
- **Coverage**: [if available]

## What's Next
[Next refactoring target or sign-off]
```

---

## Hard Limits

| Constraint | Value | Why |
|-----------|-------|-----|
| Max files per session | 15 | Token efficiency |
| Validation after each file | Required | Catch issues early |
| Atomic commits | Every 2-4 files | Clear history |
| TypeScript errors | STOP | Must fix before proceeding |
| Test failures | STOP | Must fix before proceeding |

## Token Cost

~8-12K tokens (varies by file count and complexity)

## When to Use

- ✅ After `qplan` approval
- ✅ For coordinated multi-file changes
- ✅ When you want tracked progress

**Alternative approaches:**
- Use `extract` workflow for single focused extraction
- Use `modernize` workflow for pattern updates
- Use manual editing + validation for small changes

## Success Criteria

Session is successful when:
- ✅ All planned files completed OR
- ✅ Clear blockers documented in REFACTOR_PROGRESS.md
- ✅ All validations passing
- ✅ REFACTOR_PROGRESS.md updated with next steps
- ✅ No uncommitted changes
