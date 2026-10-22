# AGENTS.md — claude-code-playbook

Token-efficient Claude Code playbook: templates, aliases, path-scoped rules, Headroom wrap. Copy templates into a target project. This repo is the kit.

## Commands

```powershell
Copy-Item templates\CLAUDE.md.template <project>\CLAUDE.md
Copy-Item templates\.claudeignore <project>\.claudeignore
. .\scripts\powershell\setup_powershell_profile.ps1
pip install "headroom-ai[all]"
pytest tests/ -q
```

Daily aliases after profile setup: `cctriage`, `ccplan`, `cccode`, `cchealth`.

## Work rules

- Keep a target project's `CLAUDE.md` small. `/context` should show it under ~500 tokens.
- Do not flatten path-scoped rules from `templates/.claude/rules/` into the root file.
- Tests here check playbook docs/scripts, not a user's downstream repo.

## Pointers

- `README.md` — 15-minute setup
- `docs/GETTING_STARTED.md`
- `templates/` — files to copy
- `CLAUDE.md` — Claude-only depth for this kit
