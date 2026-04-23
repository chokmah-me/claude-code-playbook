---
name: audit
description: "Validate a skill against quality standards"
---

# Audit an Existing Skill

Assess whether a skill meets playbook quality standards. Use after creating a new skill or to evaluate existing ones.

## Purpose

Use this workflow when:
- You just created a skill and want to verify it passes standards
- A skill is under-performing and you want to diagnose issues
- You're reviewing skills before a release or contribution
- Checking whether a skill is ready to add to the playbook

## Step 1: Read the Skill Files

Use Bash to list the target skill's files:
```bash
ls -la .claude/skills/[skill-name]/
ls -la .claude/skills/[skill-name]/workflows/
```

Use Read to open and review each file:
1. `.claude/skills/[skill-name]/SKILL.md` — Full router
2. Each `.claude/skills/[skill-name]/workflows/[name].md` — All workflows

Note the file sizes (approximate token count):
```bash
wc -w .claude/skills/[skill-name]/SKILL.md .claude/skills/[skill-name]/workflows/*.md
```

## Step 2: Score Against Standards

Reference `knowledge/quality-standards.md` and evaluate each criterion:

### Structure Checks

Does SKILL.md have all 7 sections?
- ☐ Philosophy motto (tagline)
- ☐ Overview (2-3 sentences)
- ☐ Primary Goal (1 sentence)
- ☐ Skill Structure (directory tree)
- ☐ Workflow Selection (table)
- ☐ Quick Reference (per-workflow blocks)
- ☐ Integration (2-3 bullets)

Does each workflow have all 5 sections?
- ☐ Frontmatter (name, description)
- ☐ Purpose (3-4 bullets)
- ☐ Numbered steps (4-8 steps)
- ☐ Output format (markdown block)
- ☐ Anti-patterns section (3+ ❌/✅ pairs)

**Scoring:** Count missing sections. If 0 missing → ✅ PASS (STRUCTURE). If 1+ missing → ❌ FAIL (STRUCTURE).

### Actionability Checks (STEPS)

Read each workflow's steps. For every step, verify:
- Does it name a **specific tool**? (Read, Grep, Bash, Edit, Write, Agent, etc.)
  - ✅ "Use Grep to find the function definition"
  - ❌ "Look for the function"
- Does it specify **inputs and outputs**?
  - ✅ "Input: file path | Output: list of usages"
  - ❌ "Search for usages"
- Is it **independently executable**?
  - ✅ "Read .claude/skills/*/SKILL.md and extract each overview"
  - ❌ "Review the skills"

**Scoring:** Count steps that fail any criterion. If 0 fail → ✅ PASS (STEPS). If 1+ fail → ❌ FAIL (STEPS), list the bad steps.

### Trigger Precision (TRIGGER)

For each workflow, find its trigger phrase (usually in Purpose section).

Evaluate:
- Is it **concrete and specific**? Not "when needed", "might be useful", "sometimes"
- Would a user **actually say this phrase**?
- Does it **match a real use case**?

Examples:
- ✅ "create a skill for X domain" (specific)
- ✅ "I keep doing Y" (recognizable pattern)
- ❌ "when appropriate" (vague)
- ❌ "might help with Z" (hypothetical)

**Scoring:** If all workflows have concrete triggers → ✅ PASS (TRIGGER). If any are vague → ❌ FAIL (TRIGGER), list them.

### Anti-Patterns (ANTI_PATTERNS)

For each workflow, find the "Anti-Patterns" section. Count pairs:
- ❌ [Wrong approach]
- ✅ [Right approach]

**Scoring:** Count pairs per workflow. If all have 3+ pairs → ✅ PASS (ANTI_PATTERNS). If any have <3 → ❌ FAIL (ANTI_PATTERNS), list them.

### Token Cost (TOKEN_COST)

Use the word counts from Step 1:

```bash
wc -w .claude/skills/[skill-name]/SKILL.md
wc -w .claude/skills/[skill-name]/workflows/*.md
```

Convert to approximate tokens (1.3 tokens/word):
- SKILL.md target: < 600 tokens
- Each workflow target: < 1000 tokens
- Total skill target: < 3000 tokens

**Scoring:** If all within targets → ✅ PASS (TOKEN_COST). If any exceed → ❌ FAIL (TOKEN_COST), list overages.

### Mirroring (MIRROR)

Verify the skill exists in both locations and is identical:

```bash
diff -r skills/[skill-name] .claude/skills/[skill-name]
```

Expected: No output (identical files).

If files are missing from either location:
```bash
ls -la skills/[skill-name]
ls -la .claude/skills/[skill-name]
```

**Scoring:** If diff is empty and both locations exist → ✅ PASS (MIRROR). If any diff or missing location → ❌ FAIL (MIRROR), show diff.

### Registration (REGISTRATION)

Use Bash to check if the skill appears in the README:

```bash
grep -i "[skill-name]" skills/README.md
```

Verify:
- ☐ Appears in "Skill Selection Guide" table
- ☐ Has a subsection in "Available Skills" section

**Scoring:** If present in both places → ✅ PASS (REGISTRATION). If missing → ❌ FAIL (REGISTRATION).

## Step 3: Compile Findings

Create a validation report by category:

```markdown
## Audit Report: [Skill Name]

**Date**: [YYYY-MM-DD]
**Auditor**: [Your name or automated]

### Results

| Category | Status | Issues |
|----------|--------|--------|
| STRUCTURE | ✅ PASS | [None] |
| STEPS | ❌ FAIL | Workflow "X" has vague step "Y" |
| TRIGGER | ✅ PASS | [None] |
| ANTI_PATTERNS | ⚠️ WARN | Workflow "Z" has only 2 pairs (need 3) |
| TOKEN_COST | ✅ PASS | SKILL.md: 580 tokens; avg workflow: 850 |
| MIRROR | ✅ PASS | Files identical in both locations |
| REGISTRATION | ✅ PASS | In README table and subsection |

### Summary

**Overall**: [✅ PASS / ⚠️ WARN / ❌ FAIL]

**Pass rate**: [X]% ([Y]/[Z] categories passing)

**Critical issues** (blocks use):
- [If any STRUCTURE or STEPS failures]

**Minor issues** (should fix):
- [If any TRIGGER, ANTI_PATTERNS, TOKEN_COST, MIRROR, REGISTRATION failures]

### Recommendations

[If PASS]: Skill is ready to use and meets all standards.

[If WARN or FAIL]:
1. Fix critical issues first (STRUCTURE, STEPS)
2. Address warnings (TRIGGER, ANTI_PATTERNS)
3. Optimize if needed (TOKEN_COST)
4. Sync mirrors if needed (MIRROR)
5. Re-register if needed (REGISTRATION)

Next: Run `skill-extractor/refine` to fix issues, then re-audit.
```

## Output Format

Present the audit findings:

```markdown
## Skill Audit: [Skill Name]

**Overall Status**: ✅ PASS / ⚠️ WARN / ❌ FAIL

**Detailed Report**:

**STRUCTURE**: ✅ All sections present
**STEPS**: ✅ All steps actionable and tool-specific
**TRIGGER**: ✅ All triggers concrete and specific
**ANTI_PATTERNS**: ⚠️ 2 workflows have only 2 pairs (need 3+)
**TOKEN_COST**: ✅ All under budget (SKILL.md: 580, avg workflow: 850)
**MIRROR**: ✅ Identical in skills/ and .claude/skills/
**REGISTRATION**: ✅ In README

**Issues** (if any):
- Workflow "validate" needs 1 more anti-pattern pair

**Action**: [Fix minor issues and re-audit, OR use skill as-is]
```

## Anti-Patterns

❌ Auditing only the SKILL.md and skipping workflow files — workflows have independent requirements
❌ Applying tool budgets inconsistently — use the standards document as source of truth
❌ Accepting vague trigger phrases like "when needed" — be strict on trigger precision
❌ Ignoring mirror mismatches — if files diverge, one location has stale content
❌ Stopping at FAIL without categorizing issues — users need to know what's critical vs. minor

✅ Audit all files systematically using the checklist
✅ Apply standards consistently across all skills
✅ Be specific about which step or section fails
✅ Verify mirror parity before declaring a skill complete
✅ Categorize issues so users know what to fix first
