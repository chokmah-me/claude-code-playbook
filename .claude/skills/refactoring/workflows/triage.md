---
name: triage
description: "Analyze codebase to find top 3 technical debt hotspots"
---

# Codebase Triage for Refactoring

This workflow analyzes your codebase to identify the top 3 files with the most significant technical debt using modern analysis tools.

## Purpose

Use this workflow to:
- Identify where to start refactoring
- Find "god objects" and monolithic files
- Prioritize refactoring efforts
- Understand codebase complexity

## Step 1: Launch Explore Agent for Initial Scan

Use an Explore agent to efficiently discover the codebase structure:

**Agent Task:**
```
Launch: Agent(subagent_type=Explore)

Task: Scan the codebase and identify:
1. Total count of source files (TypeScript, Python, or primary language)
2. Files larger than 500 lines (show paths and line counts)
3. Files with multiple concerns (mixing DB, API, business logic)
4. Files with code smells (any types, console logs, TODO comments)
5. Dependency counts for top 10 most-imported files

Use Glob to find source files and Grep to count patterns efficiently.
Return a table with file paths, LOC, complexity indicators, and debt scores.
```

## Step 2: Analyze Results

The Explore agent will return a scored analysis. Review the table and identify patterns:

- **High LOC** (>500 lines) = complexity risk
- **Multiple concerns** (DB + API + business logic) = extraction candidates
- **High dependency count** (>20 imports) = tight coupling
- **Code smells** (any types, debugging artifacts) = quality debt

## Step 3: Present Top 3 Candidates

Create a prioritized list:

```markdown
## Top 3 Refactoring Candidates

### 1. [filename] (Debt Score: X/100)
- **LOC**: X lines
- **Complexity**: X indicators
- **Dependencies**: X imports
- **Issues**: [list specific concerns]
- **Recommended Action**: [extract, modernize, or decompose]

### 2. [filename] (Debt Score: X/100)
...
```

**Scoring Guide:**
- Lines of Code: 200-500 (10pts), 500-1000 (30pts), 1000+ (60pts)
- Cyclomatic Complexity: 10-20 (10pts), 20-40 (30pts), 40+ (50pts)
- Dependencies: 10-20 (5pts), 20-30 (15pts), 30+ (30pts)
- Mixed Concerns: 2+ types (30pts)
- Code Smells: 2 pts per `any`, 1 pt per console/TODO
- Each console.log: +1 point
- Each TODO: +1 point

### Total Debt Score

**Debt Score = LOC score + Complexity score + Dependency score + God Object points + Code Smell points**

## Step 3: Rank Files

Sort all files by debt score (highest first).

Create a summary table:

```markdown
### Technical Debt Analysis

| Rank | File | LOC | Complexity | Dependencies | Debt Score |
|------|------|-----|------------|--------------|------------|
| 1 | file1.ts | 1500 | High | 25 | 145 |
| 2 | file2.ts | 1200 | Medium | 32 | 128 |
| 3 | file3.ts | 800 | High | 18 | 95 |
...
```

## Step 4: Generate Triage Report

Create the final report:

```markdown
### Codebase Triage Report

## Step 4: Suggest Refactoring Approach

For the top 3 candidates, recommend actions:

```markdown
## Refactoring Plan

### Priority 1: [filename] (Quick win)
- **Action**: Extract [specific functions] to separate module
- **Effort**: 1-2 hours
- **Benefit**: Reduce to <300 LOC, break tight coupling
- **Next**: Run `extract` workflow

### Priority 2: [filename] (Medium effort)
- **Action**: Decompose mixed concerns (DB/API/Logic)
- **Effort**: 3-4 hours
- **Benefit**: Enable independent testing and evolution
- **Next**: Run `qplan`, then `extract`

### Priority 3: [filename] (Long-term)
- **Action**: Modernize error handling to Result<T,E>
- **Effort**: 4-6 hours
- **Benefit**: Type-safe error propagation
- **Next**: Run `modernize` workflow
```

## Step 5: Generate Debt Report

Provide a summary for team visibility:

```markdown
## Technical Debt Summary

**Codebase Health Score**: [X]/100

| File | LOC | Complexity | Issues | Action |
|------|-----|-----------|--------|--------|
| {file1} | {X} | {Y} | {Z} | Extract |
| {file2} | {X} | {Y} | {Z} | Modernize |
| {file3} | {X} | {Y} | {Z} | Decompose |

**Key Issues**:
- {count} files over 500 LOC
- {count} files with mixed concerns
- {count} instances of code smells

**Recommended Focus**: Start with Priority 1 (highest ROI per effort)
```

---

## Budget Awareness

**Estimated token cost:** ~2,000 tokens

**Recommendations:**
- Run this once at the start of a refactoring project
- Re-run after major changes to track progress
- Don't run this every session (expensive)
- Save the report for reference

---

## Success Criteria

Triage is successful when:
- ✅ All .ts files analyzed
- ✅ Debt scores calculated for each file
- ✅ Top 3 priorities identified with specific issues
- ✅ Next actions recommended
- ✅ Effort estimates provided

---

## Next Steps

After triage:
1. Review top 3 files identified
2. Pick the #1 priority (or user's preference)
3. Run `qplan` to design refactoring approach
4. Use `extract` or `modernize` workflows to execute
5. Track progress in REFACTOR_PROGRESS.md
