---
name: generate
description: "Generate markdown documentation from code signatures and comments"
---

# Documentation Generator

Create accurate documentation directly from source code.

## Purpose

Use this workflow when:
- A new module needs documentation
- Existing docs are blank or completely stale
- You want docs that reflect the actual code, not aspirational design

## Step 1: Identify Scope

**Actions:**
```
1. Determine what to document:
   - Single file: "Generate docs for src/auth/middleware.ts"
   - Module/directory: "Generate docs for src/features/user/"
   - Public API: "Generate docs for all exported functions"

2. Identify the audience:
   - API consumers (focus on inputs/outputs/examples)
   - Contributors (focus on internals/patterns/gotchas)
   - End users (focus on behavior/configuration)
```

## Step 2: Extract Code Surface

**Actions:**
```
Launch: Agent(subagent_type=Explore)

Task: For [target files], extract:
1. All exported functions/classes/types with their signatures
2. JSDoc/docstring comments (if any)
3. Parameter types and return types
4. Default values and configuration options
5. Error conditions (what throws/returns errors)
6. Dependencies (what it imports)

Return as structured data, NOT prose.
```

## Step 3: Generate Documentation

Using the extracted surface, generate markdown:

```markdown
# [Module Name]

[1-2 sentence description derived from file header comment or inferred from exports]

## Functions

### `functionName(param1: Type, param2: Type): ReturnType`

[Description from docstring, or inferred from function body]

**Parameters:**
- `param1` (`Type`) — [description]
- `param2` (`Type`, optional, default: `value`) — [description]

**Returns:** `ReturnType` — [description]

**Throws:** `ErrorType` — [when condition]

**Example:**
```ts
const result = functionName("input", { option: true });
```

## Types

### `TypeName`
[Fields and description]

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| ... | ... | ... | ... |
```

## Step 4: Validate

```
1. Every function in the doc exists in the code (Grep to verify)
2. Every parameter type matches the code signature
3. No undocumented public exports remain
4. Examples are syntactically valid
```

## Guidelines

- **Document what IS, not what SHOULD BE** — no aspirational features
- **Derive from code** — if the code doesn't have a comment, infer from the implementation
- **Skip internals** — don't document private/unexported functions unless audience is contributors
- **Include examples** — one minimal example per public function
- **Note gotchas** — anything surprising or non-obvious about behavior
