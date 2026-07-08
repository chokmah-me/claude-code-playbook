# Fable 5 Skill

Specialized skill for maximizing Claude Fable 5 (Mythos-class) using the best published targeted prompts and scaffolding.

## Workflows
- `prepare-session`: Prepare intent, scaffolding, effort, and memory references before a Fable 5 run.
- `run-targeted-prompts`: Execute the highest-leverage official and community Fable 5 prompts (Anthropic guide, Every library, Ken Huang blocks, harness meta, etc.).
- `setup-memory`: Build and maintain a persistent lesson-based memory system that Fable 5 uses exceptionally well.

## Installation / Activation
This skill is already placed in both the source and active locations.

In Claude Code, it should be discoverable as `fable-5`.

## Sources of Prompts
- Anthropic official "Prompting Claude Fable 5" guide
- Every.to Fable 5 Prompt Library (13 templates)
- Ken Huang Fable 5 day-one blocks
- Community patterns from Reddit and real usage when Fable 5 is available

## Recommended Pairings
- `loop-engineering` for long-running Fable work
- Your existing CLAUDE.md / AGENTS.md
- `skill-creator` if you want to turn recurring Fable patterns into new skills

Run `fable-5 prepare-session` at the start of important Fable 5 work.