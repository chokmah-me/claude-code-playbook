# Changelog

All notable changes to the Claude Code Playbook will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [4.4.1] - 2026-05-31

### Fixed

- **Root `CLAUDE.md`** — version/date stamp corrected from 4.2.0 / 2026-04-01 to 4.4.1 / 2026-05-31 (had drifted two releases behind the repo); added a labeled note clarifying the file is an *example* TypeScript refactoring constitution while this repo itself is Python/markdown.
- **`README.md`** — Quick Start used `cp templates/.bash_aliases.template >> ~/.bashrc`, which is invalid (`cp` cannot write to a redirect); changed to `cat`.
- **`AUDIT_REPORT.md`** — refreshed with a dated v4.4.1 verification section (7 skills / 17 workflows, three-layer optimization, path-scoped rules, security hardening, `pytest` 47 passed); the original v4.2.0 report is retained for history.

### Added

- **Test suite committed** — `pytest.ini` + `tests/` (47 passing) now tracked in git, covering token optimization, path-scoped rules, security hardening, and Headroom integration.

---

## [4.4.0] - 2026-05-31

### Added

**Token optimization — three-layer model**
- `docs/TOKEN_ECONOMICS.md` completely rewritten around three complementary layers: don't-load-it (Layer 1), compress-before-send (Layer 2), cache-what's-stable (Layer 3)
- Session startup token floor documented: 20,000–30,000 tokens before first keypress; `/context` and `/memory` diagnostic commands added
- **Layer 1:** `.claudeignore` vs `permissions.deny` distinction documented with enforcement semantics; minimum `.claudeignore` template; path-scoped `.claude/rules/` pattern documented with 41% overhead reduction benchmark
- **Layer 2:** [Headroom](https://github.com/chopratejas/headroom) integrated as recommended output compression tool — 47–92% dynamic context reduction; `headroom wrap claude`, `headroom learn`, `headroom mcp install` documented with benchmarks
- **Layer 3:** CacheAligner and prompt caching structure documented for API users; mid-session MCP connect/disconnect cache-wipe warning added
- `ENABLE_TOOL_SEARCH=true` documented as MCP schema deferral mechanism (recovers 50,000–70,000 tokens in heavy setups)
- CLAUDE.md token cost framing added: HTML comments cost zero tokens; `@path/to/file` imports do not save tokens

**Path-scoped rules (new pattern)**
- `docs/AGENTIC_PATTERNS.md` Pattern 8: path-scoped rules in `.claude/rules/` with `paths:` frontmatter
- `templates/.claude/rules/global.md` — example unscoped global rules
- `templates/.claude/rules/api.md` — example path-scoped API layer rules

**Headroom integration (new pattern)**
- `docs/AGENTIC_PATTERNS.md` Pattern 9: output compression with Headroom
- `headroom learn` documented as automation of REFACTOR_PROGRESS.md manual catchup
- Cross-agent SharedContext documented for multi-agent workflows

**Security hardening (Mini Shai-Hulud supply chain worm, May 2026)**
- `docs/CONFIGURATION.md` Golden Rule 5: treat `.claude/` files as credential material
- `templates/CLAUDE.md.template` security warning section added
- `scripts/check_config_health.sh` Section 4: `.claude/settings.json` unexpected-key detection
- `templates/.claude/settings.json.template` `_security_note` field added
- MCP config credential hygiene guidance throughout configuration docs

**New templates**
- `templates/.claudeignore` — standard minimum context exclusions for any project
- `templates/.claude/rules/global.md` — example always-loaded global rules
- `templates/.claude/rules/api.md` — example path-scoped API rules

**Documentation updates**
- `docs/AGENTIC_PATTERNS.md` 2025 vs 2026 comparison table updated with path-scoped rules and Headroom rows
- `docs/CONFIGURATION.md` fully restructured: five golden rules, `.claudeignore` vs `permissions.deny`, path-scoped rules, MCP overhead, security
- `README.md` updated to v4.4.0: three-layer optimization summary, Headroom quick start, security note, external resources section
- `scripts/check_config_health.sh` updated to v4.4.0: nine sections including Headroom check, path-scoped rules audit, `.claude/` security scan, `permissions.deny` count, token estimation

### Changed

- `docs/TOKEN_ECONOMICS.md` — complete rewrite (previous version covered workflow costs only; new version covers the session floor, three optimization layers, and Headroom)
- `docs/CONFIGURATION.md` — complete rewrite (previous version had five golden rules; new version has six, restructured around token efficiency + security)
- `docs/AGENTIC_PATTERNS.md` — Patterns 8 and 9 added; 2025/2026 comparison table extended; best practices updated
- `templates/CLAUDE.md.template` — added token target (500), HTML comment guidance, `@import` caveat, `headroom learn` note, security section, path-scoped rules reference
- `templates/.claude/settings.json.template` — added `permissions.deny` block with recommended exclusions, `_security_note` field
- `scripts/check_config_health.sh` — expanded from 5 sections to 9; added Headroom, path-scoped rules, security, permissions.deny, and token estimation checks
- `README.md` — v4.4.0, three-layer optimization in feature list, security note, external resources

### Version bump

- v4.3.0 → v4.4.0
- Skill count: 7 skills, 17 workflows (unchanged — this release is infrastructure and documentation)

---

## [4.3.0] - 2026-04-22

### Added

- **Skill Creator** — New design-first skill for generating production-ready skills from intent
  - `create` workflow: Design and generate complete skills (SKILL.md + workflows + validation)
  - `audit` workflow: Validate skills against quality standards (7-category checklist)
  - `knowledge/quality-standards.md`: Token budgets, required sections, actionability rules
  - Complements skill-extractor (reactive pattern mining) with proactive design approach
- Skill count: 6 → 7 skills, 15 → 17 workflows

---

## [4.2.0] - 2026-04-01

### Added

- Plan Mode integration across all workflows
- Explore subagent pattern for codebase analysis (replaces manual bash)
- `docs/AGENTIC_PATTERNS.md` — comprehensive April 2026 patterns guide
- REFACTOR_PROGRESS.md as primary session continuity mechanism

### Changed

- Removed `/clear` + `catchup` ritual — replaced with Plan Mode + persistent memory
- Removed hardcoded model version references
- Removed 44K token budget ceiling
- `qplan.md` and `qcode.md` expanded from stubs to full ~150-line documentation
- `triage.md` modernized: bash scoring → Explore subagent

---

## [4.1.3] - 2025-12-25

### Added

- Cross-platform PowerShell support with 26 aliases
- 5 comprehensive docs guides: GETTING_STARTED, CONFIGURATION, ALIASES, TOKEN_ECONOMICS, SUCCESS_GUIDE
- 2 health check scripts (bash + PowerShell)
- 8 configuration templates

---

## [4.0.0] - 2025-12-11

### Added

- Skills-based architecture: SKILL.md router + workflows/ + knowledge/
- Python Scientific Computing skill
- 7 refactoring workflows: triage, extract, modernize, qnew, qplan, qcode, catchup

### Changed

- Breaking: `knowledge_base/` → `.claude/skills/`
- Breaking: workflow invocation via `claude skills refactoring <name>`
- CLAUDE.md as constitution rather than bootloader

---

## [3.0.0] - 2025-12-01

### Added

- First public release with skills-based system
- Refactoring workflows
- CLAUDE.md constitution pattern
- Token economics model

---

## [2.0.0] - 2024-11-12

### Added

- Initial public release
- Knowledge base structure
- CLAUDE.md bootloader pattern

---

## Version Comparison

| Version | Architecture | Key Features | Setup Time |
|---------|--------------|--------------|------------|
| 4.4.0 | Skills + Rules + Compression | Three-layer token optimization, Headroom, path-scoped rules, security hardening | 15 min |
| 4.3.0 | Skills + Skill Creator | Skill generation and audit workflows | 15 min |
| 4.2.0 | Skills + Agentic | Plan Mode, Explore agents, persistent memory | 15 min |
| 4.1.0 | Skills + Quick Start | 8 templates, 2 scripts, cross-platform | 15 min |
| 4.0.0 | Skills-based | 7 workflows, Python scientific | 60 min |
| 3.0.0 | Skills-based | Initial workflows | 60 min |
| 2.0.0 | Knowledge base | Patterns only | 90+ min |
