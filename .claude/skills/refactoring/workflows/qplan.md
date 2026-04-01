---
name: qplan
description: "Plan refactoring approach using Plan Mode"
---

# Plan Refactoring Approach

Use Plan Mode to design a refactoring strategy before implementation. This ensures alignment and reduces wasted effort.

## Purpose

Use this workflow to:
- Design refactoring approach in Plan Mode
- Validate against architectural goals
- Identify risks and dependencies
- Get user approval before implementation

## Step 1: Enter Plan Mode

Invoke Plan Mode with context about the refactoring target:

```
/plan

Goal: Design refactoring approach for [target file/module]

Context:
- Current state: [description of what needs refactoring]
- Target state: [modern pattern goal]
- Constraints: [budget, dependencies, etc.]

Before proposing changes, explore:
1. Current implementation in detail
2. Existing tests and their coverage
3. Dependencies (what imports this file)
4. Similar implementations in the codebase

Then propose a step-by-step implementation plan with file modifications.
```

## Step 2: Explore Current Implementation

The Plan agent will explore:
- File structure and current patterns
- Test coverage
- Dependency graph
- Similar implementations elsewhere
- Breaking change risks

## Step 3: Propose Implementation Strategy

The agent will produce a plan like:

```markdown
## Plan: [Refactoring Target]

**Goal**: Transform [file] from [current pattern] to [modern pattern]

**Pre-requisites**:
- [ ] Read: [file paths to understand]
- [ ] Verify: existing test coverage
- [ ] Search: usages to identify impact

**Tasks**:
1. [ ] Extract [function1] to new module
2. [ ] Create [new module] with [pattern]
3. [ ] Update imports in [affected files]
4. [ ] Migrate tests
5. [ ] Validate with type-check and tests

**Risk**: [main blocker or concern]
**Est**: [effort estimate]
```

## Step 4: Review & Approve

Review the plan for:
- ✅ Clear step-by-step approach
- ✅ Identifies all affected files
- ✅ Considers test impact
- ✅ Realistic effort estimate
- ✅ No missed dependencies

Then approve in Plan Mode with `ExitPlanMode` command.

## Step 5: Implement from Plan

Once approved, use `qcode` or `extract` workflow to implement the plan file-by-file.

---

## When to Use

- **Before major refactorings** (extracting 3+ functions, pattern migration)
- **Before touching APIs** (exported functions, public interfaces)
- **When uncertain** about the approach
- **For team alignment** (share the plan before coding)

**Skip for:**
- Small targeted fixes (< 1 file)
- Obvious refactorings with clear precedent

---

## Token Cost

~3K tokens (includes exploration + planning)

## Success Criteria

Plan is ready when:
- ✅ Current implementation understood
- ✅ Step-by-step approach documented
- ✅ Files to modify identified
- ✅ Test strategy clear
- ✅ Risk assessment included
