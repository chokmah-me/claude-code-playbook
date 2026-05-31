# Agentic Patterns in Claude Code (2026)

Modern Claude Code workflows use native agentic capabilities alongside external tooling for efficient multi-step tasks. This guide documents the patterns used in the Claude Code Playbook.

---

## Overview

As of mid-2026, Claude Code includes:
- **Plan Mode** — structured planning before implementation
- **Subagents** — Explore, Plan, and general-purpose agents
- **Memory system** — persistent session context
- **Task lists** — tracked progress across turns
- **Background agents** — parallel work execution

This playbook also integrates:
- **Path-scoped rules** — context that loads only when relevant files are touched
- **Output compression** — Headroom, for compressing tool outputs before they re-enter context
- **`headroom learn`** — failure mining that writes corrections back to CLAUDE.md

---

## Pattern 1: Plan Mode for Design

**When to use**: Before any multi-file refactoring or significant architectural change.

Enter Plan Mode with `/plan`. Claude explores current code, tests, dependencies, and produces a step-by-step implementation plan. Review and approve before execution.

```
/plan

Goal: Extract database layer from monolithic service.ts

Before proposing changes, explore:
1. Current service.ts structure and dependencies
2. Existing test coverage
3. What imports service.ts
4. Similar patterns in the codebase
```

---

## Pattern 2: Explore Subagent for Analysis

**When to use**: Fast, efficient codebase scanning without reading full files.

```
Agent(subagent_type=Explore)

Task: Find all TypeScript files larger than 500 lines.
Return a table with file path, line count, complexity indicators,
and a recommendation (extract, modernize, or leave).
```

Explore agents use native file search tools (Glob, Grep) and return structured output. Faster than manual bash chains.

---

## Pattern 3: Task Lists for Progress Tracking

**When to use**: Multi-file changes, multi-session work, complex operations.

```
TaskCreate({
  subject: "Extract validateUserInput to separate module",
  description: "Extract lines 145-230 from user.ts to user/validate.ts"
})
```

Tasks persist across turns and survive context resets. Check `TaskList` at any time for current state.

---

## Pattern 4: Memory System for Session Continuity

**When to use**: Multi-session projects, important decisions, project context.

Three memory types in `.claude/projects/{project}/memory/`:

**User memory** — communication preferences, role context.
**Feedback memory** — rules from past mistakes ("never force-push to main").
**Project memory** — time-bounded facts ("merge freeze begins 2026-04-10").

Claude reads `MEMORY.md` (the index) at session start. Keep individual memory entries short.

---

## Pattern 5: REFACTOR_PROGRESS.md for Multi-Session Work

**When to use**: Any refactoring spanning more than one session.

```markdown
# Refactoring Progress

## Current Goal
Extract database layer from monolithic service

## Completed
- [x] Extracted validateUserInput (lines 145-230)
  - Created user/validate.ts, 10 tests passing

## In Progress
- [ ] Extract formatMessage

## Pending
- [ ] Extract error handlers

## Blockers
None
```

Plain text in the repo root. Claude reads it via `catchup`. Commit it before ending a session so the next session can resume cleanly.

If you run `headroom learn` (Pattern 8), it may append corrections derived from failed sessions. Review those entries; they are machine-written and need trimming for token budget before commit.

---

## Pattern 6: Background Agents for Parallel Work

**When to use**: Long-running tasks that don't block other work.

```
Agent(run_in_background=true)

Task: Run full test suite on refactored code.
Commands: npm run test:unit, npm run type-check, npm run lint
Return results when done.
```

Start tests while implementing the next file. Reduces idle time waiting for slow commands.

---

## Pattern 7: Atomic Commits as Structured Logs

**When to use**: After every 2–4 files modified.

```
refactor: extract database layer from service

Changes:
- Created src/database/connection.ts (new)
- Updated service.ts:lines 20-100 to import database module
- Updated tests/service.test.ts imports

Tests: 45 passing
Types: No errors
Lint: Clean
```

Atomic commits make `git blame` useful for future maintainers and enable clean rollback. Commit message body is the session log.

---

## Pattern 8: Path-Scoped Rules for Zero-Cost Context

**When to use**: Domain-specific rules that only matter when touching specific files.

Rules in `.claude/rules/` with `paths:` frontmatter cost zero tokens until Claude touches a matching file. Without the frontmatter they load unconditionally like CLAUDE.md.

```yaml
---
paths:
  - "src/api/**/*.ts"
---
All endpoints must validate input with Zod schemas.
Response errors must use the shared ApiError class.
Never return raw Prisma errors to the client.
```

Structure your rules directory:

```
.claude/rules/
├── global.md       # No paths: — loads every session, keep tiny
├── api.md          # paths: src/api/**
├── database.md     # paths: src/database/**
└── tests.md        # paths: tests/**
```

Move anything domain-specific out of CLAUDE.md and into scoped rules. One team documented a 41% reduction in always-loaded rule overhead this way.

---

## Pattern 9: Output Compression with Headroom

**When to use**: Any session where tool outputs, logs, or file reads are large — which is most sessions.

Even with a trimmed CLAUDE.md and path-scoped rules, dynamic context accumulates fast. A failing test suite can dump 10,000 lines. A grep can return thousands of matches. All of this enters the context window before Claude processes it.

**[Headroom](https://github.com/chopratejas/headroom)** (Apache 2.0, 2.5k+ stars) compresses tool outputs, logs, RAG chunks, and files before they reach the LLM. It runs locally.

```bash
pip install "headroom-ai[all]"
headroom wrap claude          # wraps the entire Claude Code session
```

All tool outputs are compressed before re-entering context. No code changes.

Benchmarks on real agent workloads:

| Workload | Before | After | Reduction |
|----------|--------|-------|-----------|
| Code search (100 results) | 17,765 | 1,408 | **92%** |
| SRE incident debugging | 65,694 | 5,118 | **92%** |
| GitHub issue triage | 54,174 | 14,761 | **73%** |
| Codebase exploration | 78,502 | 41,254 | **47%** |

**Six compression algorithms** applied by content type: SmartCrusher (JSON), CodeCompressor (AST-aware), Kompress-base (prose ML model), CacheAligner (prefix stabilization for KV cache), IntelligentContext (score-based fitting), CCR (reversible — originals stored locally and retrievable on demand).

**headroom learn** mines failed sessions and writes corrections to CLAUDE.md:

```bash
headroom learn     # run after a failed or rough session
```

This automates part of what `catchup` does manually. Review generated entries before committing — trim for token budget.

**Headroom as MCP server** compresses output from all other MCP tools:

```bash
headroom mcp install
```

Add this even when disabling other MCP servers. Its schema cost is paid back on the first large tool output it compresses.

**Cross-agent memory** — if you work across Claude Code and other agents (Codex, Cursor), Headroom's SharedContext passes compressed context between them:

```python
from headroom import SharedContext
ctx = SharedContext()
ctx.put("session_goal", compressed_summary)  # from Claude Code session
# later, in a Codex session:
goal = ctx.get("session_goal")
```

---

## Integrated Workflow: From Plan to Commit

```
Session Start
    ↓
1. Read REFACTOR_PROGRESS.md (continuity)
2. Read MEMORY.md (context)
   [path-scoped rules load as files are touched — Pattern 8]
    ↓
3. /plan → Design phase (Plan Mode)
    ↓
4. ExitPlanMode (approve plan)
    ↓
5. TaskCreate for major steps
    ↓
6. For each file:
   - Read related code (Explore subagent if large codebase)
   - Implement change
   - Update task: in_progress → completed
   - Validate (type-check, tests, lint)
   - Commit atomically
   [Headroom compresses all tool output throughout — Pattern 9]
    ↓
7. Update REFACTOR_PROGRESS.md
    ↓
8. Session end:
   - Final validation
   - Commit progress file
   - headroom learn (optional, mines failures)
```

---

## Comparison: 2025 vs 2026 Patterns

| Task | 2025 | 2026 |
|------|------|------|
| Session continuity | `/clear` + `catchup` every 5 prompts | REFACTOR_PROGRESS.md + memory files |
| Budget awareness | Manual `/cost` checks | `/context` + `/memory` diagnostics |
| Code analysis | Manual bash: `find`, `wc`, `grep` | Explore subagent (Glob/Grep tools) |
| Planning | Text prompts | Plan Mode (structured, reviewable) |
| Domain rules | Everything in CLAUDE.md | Path-scoped `.claude/rules/` |
| Tool output size | Unmanaged, grows unchecked | Headroom compression (47–92% reduction) |
| CLAUDE.md corrections | Manual catchup notes | `headroom learn` auto-mining |
| Model version | Hardcoded "Sonnet 4.5" | Use current default Claude |

---

## Best Practices

### Do

- Use Plan Mode before major refactorings
- Maintain REFACTOR_PROGRESS.md throughout multi-session work
- Run Explore subagents for large codebase analysis
- Commit after every 2–4 files
- Move domain-specific rules to `.claude/rules/` with `paths:` frontmatter
- Run `headroom wrap claude` to compress session tool output
- Run `headroom learn` after rough sessions, review before committing results

### Don't

- Leave all rules in CLAUDE.md regardless of scope
- Let tool output accumulate uncompressed in long sessions
- Connect or disconnect MCP servers mid-session (wipes cache)
- Store API keys or MCP tokens in plaintext config files
- Inspect `.claude/settings.json` only on setup — check it after supply chain incidents

---

## Resources

- [CLAUDE.md](../CLAUDE.md) — project constitution template
- [TOKEN_ECONOMICS.md](TOKEN_ECONOMICS.md) — three-layer optimization model
- [CONFIGURATION.md](CONFIGURATION.md) — CLAUDE.md, rules, MCP, security
- [Headroom](https://github.com/chopratejas/headroom) — output compression tool
- [token-optimizer](https://github.com/hamzafarooq/token-optimizer) — CLAUDE.md benchmark and audit tool

---

**Last Updated**: May 2026
**Version**: 4.4.0
