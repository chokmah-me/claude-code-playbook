---
name: refine
description: "Improve an existing skill based on real usage feedback and observed gaps"
---

# Refine Existing Skill

Improve a skill that works but has issues — wrong triggers, missing steps, too verbose, or poor token efficiency.

## Purpose

Use this workflow when:
- A skill produced wrong or incomplete results
- Steps were unclear and required manual intervention
- The skill is too verbose (>1000 tokens for simple tasks)
- Trigger conditions don't match real usage patterns
- A step was missing that you had to add manually

## Step 1: Diagnose the Issue

Read the skill files and identify what's wrong:

```
1. Read the SKILL.md router — is the overview accurate?
2. Read the relevant workflow file — walk through each step:
   - Is the trigger condition correct?
   - Are steps in the right order?
   - Are there missing steps you had to do manually?
   - Are there unnecessary steps that added no value?
   - Are tool calls specified correctly?
3. Check the last time the skill was used:
   - What went wrong or required manual override?
   - What went right and should be preserved?

Classify the issue:
- TRIGGER: skill invoked at wrong time or not invoked when needed
- MISSING_STEP: a necessary step isn't documented
- WRONG_ORDER: steps are in suboptimal sequence
- TOO_VERBOSE: skill has unnecessary content inflating token cost
- UNCLEAR: steps are ambiguous, leading to inconsistent execution
- STALE: references outdated tools, paths, or patterns
```

## Step 2: Plan the Fix

Based on the diagnosis:

```
For TRIGGER issues:
  → Rewrite "When to Use" with specific examples from real usage

For MISSING_STEP:
  → Add the step in the correct position
  → Verify it doesn't break the flow of subsequent steps

For WRONG_ORDER:
  → Reorder steps based on observed optimal sequence
  → Update any step references that depend on order

For TOO_VERBOSE:
  → Remove duplicate content across files
  → Consolidate overlapping sections
  → Cut examples to 1-2 (not 3-5)
  → Remove aspirational "future enhancements" sections

For UNCLEAR:
  → Add specific tool calls (Agent, Grep, Read, etc.)
  → Replace vague instructions with concrete actions
  → Add decision criteria for branching steps

For STALE:
  → Update tool names, file paths, patterns
  → Remove references to deprecated features
```

## Step 3: Apply Changes

```
1. Edit the affected files (SKILL.md and/or workflow files)
2. Preserve what works — don't rewrite sections that are fine
3. Keep changes minimal and focused on the diagnosed issue
4. Update token estimates if content size changed significantly
```

## Step 4: Verify

```
1. Re-read the updated skill end-to-end
2. Mentally walk through a scenario — do the steps make sense?
3. Check that the SKILL.md router still accurately describes workflows
4. If the skill is mirrored (e.g., .claude/skills/ and skills/), sync both copies
5. Commit: "fix(skills): improve [skill-name] — [what changed]"
```

## Output Format

```markdown
## Refined: [skill-name]

**Issue**: [1-line diagnosis]
**Fix**: [1-line summary of changes]
**Files changed**: [list]
**Token impact**: [+/- N tokens]
```

## Anti-Patterns

❌ Rewriting an entire skill when only one step needs fixing
❌ Adding content without removing equivalent bloat
❌ Refining based on hypothetical issues (refine from real usage only)

✅ Diagnose before changing anything
✅ Preserve working sections
✅ Sync mirrored copies after changes
