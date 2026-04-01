---
name: orient
description: "Guided codebase walkthrough: architecture, key files, conventions, gotchas"
---

# Codebase Orientation

Build a mental model of an unfamiliar codebase in a structured pass.

## Purpose

Use this workflow when:
- First time working in a repository
- Returning to a repo after months away
- Need to understand a module before modifying it
- Onboarding a new team member

## Step 1: Bird's-Eye View

Get the high-level shape of the project.

**Actions:**
```
1. Read README.md (first 100 lines) — what does this project DO?
2. Read package.json / pyproject.toml / Cargo.toml — dependencies and scripts
3. Check directory structure:
   Glob("*") for top-level, then Glob("src/**") or equivalent
4. Read CLAUDE.md / CONTRIBUTING.md if they exist — project conventions

Summarize in ≤5 lines:
- Purpose: [what it does]
- Language/framework: [stack]
- Structure: [monolith / modular / monorepo]
- Entry point: [main file or command]
- Test runner: [how to run tests]
```

## Step 2: Architecture Map

Identify how the pieces connect.

**Actions:**
```
Launch: Agent(subagent_type=Explore)

Task: Map the architecture of this codebase:
1. Identify the entry point(s) (main, index, app, server)
2. Find the top 5 most-imported files (dependency hubs)
3. Identify layers (routes/controllers → services → data/models)
4. Find configuration sources (env vars, config files, constants)
5. Identify external integrations (DB, APIs, queues, caches)

Return as a simple layer diagram using text:
  [Entry] → [Layer 1] → [Layer 2] → [External]
Plus a table of key files with 1-line descriptions.
```

## Step 3: Conventions Scan

Learn how this codebase does things.

**Actions:**
```
1. Check 2-3 recent commits (git log --oneline -5):
   - Commit message style
   - Typical change size

2. Read one "typical" file (medium size, recently modified):
   - Naming conventions (camelCase, snake_case)
   - Error handling pattern (throw, Result, error codes)
   - Import style (relative, absolute, barrel files)
   - Comment density and style

3. Check for linting/formatting config:
   Glob("*eslint*", "*prettier*", "*ruff*", "*.editorconfig")
```

## Step 4: Gotchas & Risks

Find things that would surprise a newcomer.

**Actions:**
```
1. Search for common red flags:
   Grep("TODO|FIXME|HACK|XXX|WORKAROUND") — count by file
   Grep("any") in TypeScript files — unsafe type usage
   Grep("eslint-disable|noqa|type: ignore") — suppressed warnings

2. Check for:
   - God files (>500 lines): find large files via Explore
   - Circular dependencies: look for mutual imports
   - Missing tests: compare src/ structure to test/ structure

3. Note environment requirements:
   - Required env vars (Grep for process.env or os.environ)
   - Required services (DB, Redis, etc.)
```

## Output Format

```markdown
## Orientation: [Project Name]

### What It Does
[2-3 sentences]

### Stack
- Language: [X]
- Framework: [X]
- Key deps: [X, Y, Z]

### Architecture
[Entry] → [Services] → [Data Layer] → [External]

### Key Files
| File | Role |
|------|------|
| src/index.ts | Entry point |
| src/services/auth.ts | Authentication logic |
| ... | ... |

### Conventions
- Naming: [style]
- Errors: [pattern]
- Commits: [format]

### Gotchas
- [gotcha 1]
- [gotcha 2]

### How to Start
1. [setup command]
2. [run command]
3. [test command]
```
