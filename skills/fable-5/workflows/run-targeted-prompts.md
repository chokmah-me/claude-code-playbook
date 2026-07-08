---
name: run-targeted-prompts
description: "Run the best published Fable 5-specific prompts (official Anthropic, Every library, Ken Huang, and community) with proper scaffolding."
---

# Run Best Fable 5 Targeted Prompts

## Purpose

Use this workflow when:
- You have Fable 5 access and want to apply the highest-leverage prompts specifically designed or tested for it.
- You want to run meta prompts, one-shot ambitious work, harness audits, or memory setups optimized for Fable 5's strengths.
- You need the prompts adapted to your current Claude Code harness (CLAUDE.md, skills, memory).

## Step 1: Select Category

Present the main categories of best Fable 5 prompts and let the user choose or combine:

**A. Official Anthropic Scaffolding (from Prompting Claude Fable 5 guide)**
- Effort-aware instructions
- Memory system setup
- Boundaries and "act when ready"
- Grounded progress reporting
- Subagent delegation

**B. Every.to Fable 5 Prompt Library (13 templates)**
- Delegate overnight
- Fix broken agent workflow
- Build from product spec
- Go-to-market strategy from data
- Turn feedback into batched changes
- Build loops
- Etc.

**C. Ken Huang Day-One Blocks**
- Intent + "because" framing
- Grounded progress audit
- Autonomy rules for long runs
- Plain-English output for users

**D. Community / Practical Fable 5 Prompts**
- Pre-window catch-up audits (review code written while Fable was away)
- Full UX path audits with browser control
- One-shot ambitious creative + code tasks
- Extracted claude-design system prompt for front-end

**E. Meta / Harness Level (Fable-optimized Miessler-style)**
- Harness goal orientation
- Memory that compounds
- Loop audit for Fable
- Self-model / project-model audit
- "What 10x and what dies" for your work

Ask which category or specific prompt(s) they want to run now.

## Step 2: Load Context

- Read relevant parts of user's CLAUDE.md, AGENTS.md, loop-engineering references, and any existing memory.
- Identify what files/tools/skills the prompt should have access to.
- Ask for any specific project or task context to inject.

## Step 3: Adapt and Output the Prompt

For the chosen prompt(s):
- Inject the "because" intent and current state if not already present.
- Add Fable 5 best-practice wrappers (effort note, memory reference, verification instruction).
- Make it Claude Code native (mention skills, subagents, worktrees, /goal if appropriate).
- Output in a clean, copy-paste ready block.
- Also provide a short "how to use" note (e.g., "Paste at the start of a new Fable 5 session at high effort").

If multiple, present them as a sequence the user can run in one long session or across /goal turns.

## Step 4: Post-Run Capture

After the user runs the prompt(s), remind them:
- Use `setup-memory` to capture lessons.
- Consider running `prepare-session` next time for better scaffolding.
- Note any surprising strengths or weaknesses of Fable 5 on this task.

## Output Format

```markdown
## Selected Fable 5 Prompts

**Category**: [e.g. Official Anthropic + Every Library]

### Prompt 1: [Name]
[Full adapted prompt]

**Usage**: Start a Fable 5 session at [effort]. Paste this first.

### Prompt 2: ...
...

## Recommended Session Settings
- Effort: high / xhigh
- Memory: reference [your memory path]
- Enable subagents: yes
- Suggested length: [single turn / /goal / overnight]

## After the Run
Run `fable-5 setup-memory` with the results to make knowledge compound.
```

## Anti-Patterns

❌ Running raw prompts without adding intent ("because") and current state
❌ Using low effort on meta/harness prompts (waste of Fable 5)
❌ Forgetting to tell Fable 5 about your existing skills and memory files
❌ Treating every prompt the same — match ambition to the model's strengths (long horizon, verification, one-shot complex work)

✅ Always wrap with outcome + why + constraints
✅ Reference memory explicitly
✅ Use subagents for parallel parts of the prompt
✅ Capture lessons afterward so future Fable runs (or weaker models) benefit