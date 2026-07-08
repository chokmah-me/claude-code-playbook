---
name: prepare-session
description: "Prepare intent, scaffolding, memory, and effort settings for a high-leverage Fable 5 session in Claude Code."
---

# Prepare Fable 5 Session

## Purpose

Use this workflow when:
- You are about to start a significant task with Fable 5 (Claude Code or direct).
- You want to apply official Anthropic Fable 5 prompting patterns and community best practices from the start.
- You need to set up proper boundaries, memory references, subagent delegation, and effort levels before the run begins.

## Step 1: Gather Context

Ask the user for or load:
- The larger project or goal
- Why this matters ("because..." intent)
- Current state (attach relevant CLAUDE.md, files, previous session notes)
- Hard constraints (what must not change, scope, approvals needed)
- Available tools/MCPs/skills in the environment

Use Read or Grep on the user's CLAUDE.md, AGENTS.md, and any memory files if provided.

## Step 2: Choose Effort and Mode

Recommend effort level:
- Routine or interactive: medium or high
- Complex, long-horizon, or one-shot ambitious work: high or xhigh
- Maximum capability (expensive, slower): max

Confirm if they want:
- Single long turn vs /goal vs scheduled /loop
- Heavy use of parallel subagents
- Dynamic workflows

## Step 3: Build the Session Brief

Generate a ready-to-paste opening prompt that includes:

1. **Intent framing**
   ```
   I'm working on [larger project] for [audience], because [what the outcome enables].
   ```

2. **Current state + constraints**

3. **Official Fable 5 scaffolding blocks** (from Anthropic guide):
   - "When you have enough information to act, act."
   - Ground progress claims against tool results.
   - "Lead with the outcome."
   - Memory instructions (reference any existing memory files).
   - Boundaries (pause only for destructive actions or user-only info).
   - Delegation encouragement for subagents.

4. **Fable-specific memory note**
   ```
   Store lessons in [path-to-memory]. One lesson per file. Reference it in future turns.
   ```

5. **Verification plan**
   - What "done" looks like
   - How to audit claims
   - Human checkpoints

Output the full prepared brief in a clean code block.

## Step 4: Memory & Harness Check

Quickly check:
- Does a memory system exist? (Suggest creating one with `setup-memory` if not.)
- Are there any contradictions in current CLAUDE.md / skills that Fable 5 might exploit?
- Any previous Fable runs that should be reviewed first?

## Output Format

Return:

```markdown
## Fable 5 Session Brief (ready to paste)

[Full prompt here]

## Recommended Settings
- Effort: high / xhigh
- Memory file: [path]
- Expected checkpoints: [list]
- Suggested first sub-task delegation: [optional]

## Next Steps
1. Paste the brief
2. (Optional) Run `fable-5 run-targeted-prompts` for specific powerful prompts to layer in
3. After the run, use `setup-memory` to capture lessons
```

## Anti-Patterns

❌ Starting with a vague "do this big thing" without "because" intent or constraints
❌ Using long prescriptive step-by-step lists (Fable 5 prefers outcome + boundaries)
❌ Forgetting to set up memory references before a long run
❌ Setting effort to max for every task (wasteful on routine work)
❌ Not telling Fable 5 about available skills/MCPs upfront

✅ Lead with outcome + why
✅ Include explicit "audit claims against tool results"
✅ Reference or create memory early
✅ Match effort to task complexity
✅ Explicitly encourage subagent delegation for parallel work