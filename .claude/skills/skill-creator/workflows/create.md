---
name: create
description: "Design and generate a complete skill from intent in 7 steps"
---

# Create a New Skill

Turn a domain need into a production-ready skill with quality standards baked in.

## Purpose

Use this workflow when:
- You have a clear domain (e.g., "API testing", "data validation", "performance profiling")
- You want a full skill (SKILL.md + 2-4 workflows + knowledge base)
- You need it to integrate with the playbook architecture
- You want token-efficient workflows that pass quality standards

## Step 1: Intake & Scope

Ask the user: **"Describe the skill domain in 1-3 sentences. What workflows should it have?"**

Extract and document:
- Skill name candidate (kebab-case, e.g., `api-tester`, `data-validator`)
- Domain/purpose (1-2 sentences)
- List of 2-4 proposed workflows (e.g., "test endpoints", "validate schemas")

**Output:** Skill intake summary (name, purpose, workflows proposed)

## Step 2: Gap Check

Use Bash to list all existing skills:
```bash
ls .claude/skills/*/SKILL.md
```

For each one, read the **Overview** section only (first 50 lines). Scan for overlap:
- Is there already a skill doing this domain?
- Do any workflow names conflict?
- Is this skill genuinely new?

Present findings:
```markdown
## Gap Analysis

**Proposed skill**: [name]
**Existing similar skills**: [list or "None"]
**Verdict**: ✅ No overlap / ⚠️ Partial overlap (see note) / ❌ Duplicate
```

Ask user: **"Proceed with this new skill?"** If ❌, stop here.

## Step 3: Design Workflows

For **each** proposed workflow, design it on paper (or in conversation):

1. **Trigger phrase** — Exact words user would say (e.g., "validate this API response")
2. **Purpose bullets** — 3-4 concrete use cases
3. **Steps** — 4-8 numbered steps, each naming a specific tool (Read, Grep, Bash, Edit, Write, Agent)
4. **Decision branches** — "if X, do Y; else do Z"
5. **Output format** — Markdown block showing what user sees at end

Document the design in a table:

```markdown
| Workflow | Trigger | Steps | Output |
|----------|---------|-------|--------|
| [name] | [phrase] | [count] | [type] |
```

## Step 4: Generate SKILL.md

Using `skills/skill-extractor/template.md` as reference, create the router:

```markdown
# Skill: [Name]
> "[Philosophy motto, <10 words]"

## Overview
[2-3 sentences about what it does]

**Primary Goal:** [1 sentence outcome]

---

## Skill Structure

[Directory tree showing file layout]

---

## Workflow Selection

| Situation | Workflow | Tokens |
|-----------|----------|--------|
| [when to use 1] | `workflow-1` | ~[N]K |
| [when to use 2] | `workflow-2` | ~[N]K |

---

## Quick Reference

**workflow-1** — [action verb]
[Use when / Output blocks]

**workflow-2** — [action verb]
[Use when / Output blocks]

---

## Integration

- [Relationship to other skills]
- [When to use this vs. related skills]
```

Validate: SKILL.md < 600 tokens. If over, trim sections.

**Write to both locations:**
- `skills/skill-creator/SKILL.md`
- `.claude/skills/skill-creator/SKILL.md`

## Step 5: Generate Workflow Files

For each workflow, create a .md file with exact structure:

```markdown
---
name: workflow-name
description: "One-line description"
---

# [Workflow Title]

## Purpose

Use this workflow when:
- [Bullet 1]
- [Bullet 2]
- [Bullet 3]

## Step 1: [Action]

[Description of step, inputs, outputs]

## Step 2: [Action]

...

## Output Format

[Markdown block showing user-facing result]

## Anti-Patterns

❌ [Wrong approach 1]
❌ [Wrong approach 2]
❌ [Wrong approach 3]

✅ [Right approach 1]
✅ [Right approach 2]
✅ [Right approach 3]
```

Validate: Each workflow < 1000 tokens. If over, reduce examples or consolidate steps.

**Write to both locations:**
- `skills/skill-name/workflows/[name].md`
- `.claude/skills/skill-name/workflows/[name].md`

## Step 6: Update Registration

Edit `skills/README.md`. Find the "Skill Selection Guide" table. Add a new row:

```markdown
| [Skill Name] | [One-line purpose] | [Workflows] | Notes |
```

Example:
```markdown
| Skill Creator | Generate production-ready skills | create, audit | Design-first approach; complements skill-extractor |
```

Also add a subsection in the "Available Skills" section:

```markdown
### N. Skill Name

**Location**: `.claude/skills/skill-name/SKILL.md`

**Purpose**: [1-2 sentence description]

**Available Workflows**: [list]

**When to Use**: [bullets]

**Quick Start**: [code block or link to SKILL.md]
```

## Step 7: Validate Against Standards

Use Bash to measure token count (approximate):
```bash
wc -w skills/skill-name/SKILL.md
wc -w skills/skill-name/workflows/*.md
```

Run the quality checklist from `knowledge/quality-standards.md`:

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

Verify mirror parity:
```bash
diff -r skills/skill-name .claude/skills/skill-name
```

Present report:

```markdown
## Validation Report: [Skill Name]

**Overall**: ✅ PASS / ❌ FAIL

**Issues by category**:
- STRUCTURE: ✅ PASS
- STEPS: ✅ PASS
- TRIGGER: ⚠️ FAIL — Workflow "X" has vague trigger
- ANTI_PATTERNS: ✅ PASS
- TOKEN_COST: ✅ PASS (SKILL.md: 580 tokens, workflows: 850 avg)
- MIRROR: ✅ PASS (identical)
- REGISTRATION: ✅ PASS (in README)

**Next steps**: [If PASS: "Skill ready to use!" / If FAIL: "Fix issues, re-run audit"]
```

## Output Format

Present the complete skill creation result:

```markdown
## Skill Created: [Skill Name]

**Domain**: [Description]
**Workflows**: [List]
**Files created**:
- skills/skill-name/SKILL.md
- skills/skill-name/workflows/[name].md (x[N])
- .claude/skills/skill-name/ (mirrored)

**Validation**: ✅ PASS

**Next**: Use the skill in your projects or run `audit` to validate further.
```

## Anti-Patterns

❌ Creating a skill with only 1 workflow — too narrow, won't generalize
❌ Skipping the gap check — might duplicate existing skills
❌ Generating workflows without concrete trigger phrases — users won't know when to invoke
❌ Forgetting to mirror to `.claude/skills/` — Claude Code won't find the skill
❌ Skipping validation — might fail quality checks when used
❌ Writing vague step descriptions like "check if X works" instead of "use Grep to find X"

✅ Propose 2-4 workflows per skill
✅ Always check for overlap with existing skills
✅ Make trigger phrases specific and exact
✅ Mirror to both locations immediately
✅ Run validation checklist before declaring done
✅ Name tools explicitly: "Use Read to open file.ts"
