# Skill Quality Standards

Reference checklist for designing and validating skills. Use during the `create` workflow (step 7 validation) and the `audit` workflow.

---

## Token Budgets

| Component | Hard Limit | Target | Rationale |
|-----------|-----------|--------|-----------|
| SKILL.md | 800 tokens | <600 tokens | Router must be scannable, not a textbook |
| Workflow .md | 1200 tokens | <1000 tokens | Step should fit one model context window |
| Complete skill | N/A | <3000 tokens | All files together for skill-in-use |

**Measurement:** Use token counter in Claude Code UI or count via `wc -w` and assume ~1.3 tokens/word.

---

## Required Sections (SKILL.md)

Every SKILL.md must contain:

- ✅ **Philosophy motto** (tagline, <10 words) — "The art of X is Y"
- ✅ **Overview** (2-3 sentences) — What it does, not how to use it
- ✅ **Primary Goal** (1 sentence) — The outcome users should expect
- ✅ **Skill Structure** (directory tree) — Where files live
- ✅ **Workflow Selection** (table) — When to use each workflow, token cost per row
- ✅ **Quick Reference** (one block per workflow) — Trigger, use case, output
- ✅ **Integration** (2-3 bullets) — Relationships to other skills

**Missing any?** Validation fails at "STRUCTURE" category.

---

## Required Sections (Workflow .md)

Every workflow file must contain:

- ✅ **Frontmatter** — `name:` and `description:`
- ✅ **Purpose** (3-4 bullets) — When and why to use this workflow
- ✅ **Numbered steps** (4-8 steps) — Exact sequence with tool calls
- ✅ **Output format** — Markdown block showing user-facing result
- ✅ **Anti-patterns section** — At least 3 ❌ (wrong) / ✅ (right) pairs

**Missing any?** Validation fails at "STRUCTURE" category.

---

## Actionability

Every step in a workflow must:

1. **Name a specific tool** — Not "search for X" but "use Grep to find X"
   - Valid: "Use Read to open `src/index.ts`"
   - Invalid: "Look for the main file"

2. **Define input & output** — What goes in, what comes out
   - Valid: "Grep for function `validateUser` → list of file paths"
   - Invalid: "Check if the function exists"

3. **Be independently executable** — Reader doesn't need external context
   - Valid: "Read `.claude/skills/*/SKILL.md` and extract the 'When to Use' section from each"
   - Invalid: "Review the skills and understand patterns"

**Scoring:** Every step gets a ✅ or ❌. If 1+ step fails, validation fails at "STEPS" category.

---

## Trigger Precision

Each workflow must have a **concrete trigger phrase** that users would actually say:

**Good triggers:**
- "create a skill for X" (specific domain)
- "I keep doing Y" (pattern recognition)
- "validate this skill" (direct action)

**Bad triggers:**
- "when needed" (too vague)
- "might be useful" (hypothetical)
- "sometimes" (ambiguous timing)

**Scoring:** If trigger is absent or vague, validation fails at "TRIGGER" category.

---

## Anti-Patterns Section

Each workflow .md must include a section showing what NOT to do:

```markdown
## Anti-Patterns

❌ [specific wrong approach]
❌ [specific wrong approach]
❌ [specific wrong approach]

✅ [recommended approach]
✅ [recommended approach]
✅ [recommended approach]
```

**Scoring:** Must have at least 3 pairs. If fewer, validation fails at "ANTI_PATTERNS" category.

---

## Mirroring

Skills must exist in **both** locations with **identical content**:

- `skills/skill-name/` ← Source of truth for version control
- `.claude/skills/skill-name/` ← Location Claude Code reads from

**Validation:**
```bash
diff -r skills/skill-name .claude/skills/skill-name
# Should output nothing (files identical)
```

**Scoring:** If diff is non-empty, validation fails at "MIRROR" category.

---

## Registration

The skill must be added to `skills/README.md` in the skill index table:

```markdown
| [Skill Name] | [1-line description] | [N] | [bullets on when to use] |
```

**Scoring:** If entry missing from table, validation fails at "REGISTRATION" category.

---

## Quick Validation Checklist

Run this before marking a skill "complete":

| Criterion | Pass? | Category |
|-----------|-------|----------|
| SKILL.md has all 7 sections | ☐ | STRUCTURE |
| Each workflow has all 5 sections | ☐ | STRUCTURE |
| Every step names a tool (Read, Grep, etc.) | ☐ | STEPS |
| Workflows have concrete trigger phrases | ☐ | TRIGGER |
| Each workflow has 3+ anti-pattern pairs | ☐ | ANTI_PATTERNS |
| Token count: SKILL.md < 600, workflows < 1000 | ☐ | TOKEN_COST |
| Mirror diff shows no differences | ☐ | MIRROR |
| Skill appears in skills/README.md table | ☐ | REGISTRATION |

**Result:** All checked = ✅ **PASS** | Any unchecked = ❌ **FAIL**

---

## Validation Categories (for audit workflow reporting)

When running `audit` or validating after `create`, report issues grouped by category:

- **STRUCTURE** — Missing required sections
- **STEPS** — Steps lack actionability or tool specificity
- **TRIGGER** — Workflow triggers are vague or missing
- **ANTI_PATTERNS** — Insufficient anti-pattern pairs
- **TOKEN_COST** — Exceeds budget limits
- **MIRROR** — Files missing or out of sync between locations
- **REGISTRATION** — Skill not in README table

---

## Example: Well-Formed Workflow

```markdown
---
name: validate-api-responses
description: "Check API response schemas against OpenAPI spec"
---

# Validate API Responses

## Purpose

Use this workflow when:
- Adding a new API endpoint and want to verify response matches spec
- Debugging API integration tests that fail on contract violations
- Before release to validate all endpoints against published OpenAPI schema

## Step 1: Read the OpenAPI Spec

Use Read to open the OpenAPI file (usually `docs/openapi.yaml` or `schema/api.schema.json`). Extract the endpoint path and response object shape.

**Input:** Project path
**Output:** Response schema object (properties, required fields, types)

## Step 2: Locate the Endpoint Handler

Use Grep to find the endpoint handler function. Pattern: search for the HTTP method + route path.

**Input:** Endpoint path from step 1 (e.g., `GET /api/users/:id`)
**Output:** File path + line number of handler

## Step 3: Extract Response Code

Use Read to open the handler file. Find the response object being returned. Copy the object structure.

**Input:** File path + line number from step 2
**Output:** Actual response object (code)

## Step 4: Compare

Manually inspect: Do the schema (step 1) and actual response (step 3) match?

**Decision:**
- ✅ All fields present, types match → Go to step 5
- ❌ Missing fields or type mismatch → Edit handler to match spec, then re-run steps 3-4

## Step 5: Update Tests

Use Grep to find tests for this endpoint. Use Edit to add assertions for the new fields.

**Input:** Handler file path
**Output:** Updated test file with assertions

## Output Format

```markdown
## Validation Result: [endpoint]

**Status**: ✅ PASS or ❌ FAIL

**Schema match**: [All fields present/Missing: field1, field2]
**Type match**: [All types correct/Mismatch in field1: expected string, got number]
**Test coverage**: [All fields tested/Missing assertions for field1]

**Action**: [No changes needed / Updated handler and tests]
```

## Anti-Patterns

❌ Comparing schema and code by eye without a clear checklist — easy to miss a field
❌ Updating tests without re-checking the actual response code — tests can pass with wrong code
❌ Assuming OpenAPI spec is always correct — verify against actual implementation first

✅ Extract spec → Extract code → Compare systematically
✅ Re-run the comparison after any handler changes
✅ When disagreement found, investigate which source is canonical (spec or code)
```

---

**Last Updated:** 2026-04-22
**Version:** 1.0
