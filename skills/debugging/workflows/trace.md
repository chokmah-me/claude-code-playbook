---
name: trace
description: "Trace execution path through codebase using Explore agents"
---

# Execution Trace

Follow data or control flow through the codebase to understand how something works.

## Purpose

Use this workflow when:
- You need to understand "how does X get from A to B?"
- Unfamiliar with a code path and need to map it
- Verifying that a change in one place propagates correctly

## Step 1: Define the Trace Target

**Actions:**
```
1. Identify the starting point:
   - An API endpoint, event handler, or user action
   - A specific function call or data value
2. Identify the end point:
   - Where the effect is observed (DB write, UI update, log output)
3. State the trace goal:
   "Trace how [input/event] at [entry point] reaches [effect] at [end point]"
```

## Step 2: Map the Call Chain

**Actions:**
```
Launch: Agent(subagent_type=Explore)

Task: Starting from [entry point file:function], trace the execution path
to [end point]. For each step in the chain, report:
1. File path and function name
2. What data is passed (parameter names and types)
3. Any transformations applied to the data
4. Branching conditions (if/switch) that affect the path

Return as a numbered list showing the complete call chain.
```

## Step 3: Annotate Key Points

Review the Explore agent's output and annotate:

```
1. [entry] src/routes/api.ts:handleRequest(req)
   → extracts req.body.userId (string)
2. [transform] src/services/user.ts:findUser(userId)
   → queries DB, returns User | null
3. [branch] if user === null → throws NotFoundError
4. [transform] src/services/auth.ts:checkPermissions(user)
   → returns boolean
5. [effect] src/db/audit.ts:logAccess(user.id, resource)
   → INSERT into audit_log table
```

## Step 4: Identify Risks

**Check for:**
```
- Missing null/error checks between steps
- Type narrowing gaps (any types, missing guards)
- Side effects that could fail silently
- Points where data could be stale or mutated unexpectedly
```

## Output Format

```markdown
## Trace: [goal]

### Call Chain
1. `file:function` — [what happens, data in/out]
2. `file:function` — [what happens, data in/out]
...

### Observations
- [risk or insight 1]
- [risk or insight 2]

### Recommendation
[action if any — or "path is clean"]
```

## When to Use vs. Diagnose

| Use `trace` | Use `diagnose` |
|-------------|----------------|
| "How does this work?" | "Why is this broken?" |
| No error, just understanding | Error or unexpected behavior |
| Proactive exploration | Reactive investigation |
