---
name: extract
description: "Detect repeated workflow patterns in session history and generate a new skill"
---

# Extract Skill from Session

Analyze the current conversation to find repeated patterns and create a reusable skill.

## Purpose

Use this workflow when:
- You've done the same multi-step procedure 2+ times in this session
- User says: "extract this workflow", "create a skill from this", "formalize this pattern"
- You notice yourself repeating a tool sequence (e.g., Grep → Read → Edit → Test)

## Step 1: Scan Session for Patterns

Review the conversation and identify candidates:

```
Look for:
1. Repeated tool sequences — same tools called in same order (2+ times)
2. Decision patterns — recurring if/else logic ("if test fails, do X")
3. Multi-step procedures — 4+ step workflows done manually
4. Domain procedures — "always check X before Y"

For each candidate, note:
- Times repeated: [N]
- Steps per occurrence: [N]
- Tools used: [list]
- Variation between occurrences: [low/medium/high]

Discard candidates with high variation — they're not patterns.
```

## Step 2: Select Best Candidate

If multiple patterns found, rank by:

```
Score = (repetitions × steps × consistency) - complexity

Pick the pattern with:
- Highest repetition count
- Most consistent structure (low variation)
- Clearest trigger condition
- Broadest reusability
```

Present to user for confirmation before proceeding.

## Step 3: Define the Workflow

Document the selected pattern:

```markdown
**Name**: [descriptive-kebab-case-name]
**Trigger**: [when to invoke — user phrase or situation]
**Steps**:
1. [Tool] — [purpose] ([input] → [output])
2. [Tool] — [purpose]
3. Decision: if [condition] → [branch A] else [branch B]
4. [Tool] — [purpose]
**Inputs**: [what the user provides]
**Outputs**: [what the skill produces]
```

## Step 4: Generate Skill Files

Create the skill following the standard structure:

```
1. Create directory: .claude/skills/[skill-name]/
   (or project-specific: skills/[skill-name]/)

2. Generate SKILL.md using template at ../template.md:
   - Purpose: 1-2 sentences
   - Skill Structure: directory tree
   - Workflow Selection: table with situations
   - Quick Reference: one block per workflow
   - Integration: how it connects to other skills

3. Generate workflows/[name].md:
   - Frontmatter: name, description
   - Purpose: when to use (3-4 bullet points)
   - Steps: numbered with tool calls and decision points
   - Output format: what the user sees
   - Anti-patterns: what NOT to do

4. Mirror to skills/ directory if in a playbook repo
```

## Step 5: Validate and Present

```
Before finalizing, verify:
- [ ] Steps are actionable without session context
- [ ] Trigger conditions are specific enough
- [ ] Token estimate is realistic
- [ ] Doesn't duplicate an existing skill
- [ ] Follows the SKILL.md router + workflows/ pattern

Present to user:

## Extracted Skill: [name]

**Purpose**: [1-line description]
**Pattern**: seen [N] times, [M] steps each
**Est. savings**: ~[X] tokens per future use
**Files created**: [list]
```

## Anti-Patterns

❌ Extracting after seeing a pattern only once
❌ Creating skills for trivial operations (grep + read)
❌ Including project-specific details in a general skill
❌ Generating bloated README + SKILL.md + separate doc (one router + workflows is enough)

✅ Wait for 2+ repetitions before extracting
✅ Parameterize project-specific values
✅ Follow the standard SKILL.md + workflows/ structure
✅ Keep each file focused on one concern
