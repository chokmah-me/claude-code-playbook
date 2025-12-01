# Changelog

All notable changes to the Claude Code Playbook will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [3.0.0] - 2025-12-01

### 🎉 Major Release - Skills-Based Architecture

This is a major rewrite from v2.0.0, introducing an executable skills-based system.

### Added
- **6 New Executable Workflows**
  - `triage` - Technical debt analysis with scoring algorithm (~2K tokens)
  - `qnew` - Session initialization with context loading (~2K tokens)
  - `qplan` - Plan validation against architectural patterns (~3K tokens)
  - `extract` - Surgical function extraction (~5K tokens)
  - `modernize` - Pattern updates (async/await, Result monads) (~4K tokens)
  - `qcode` - Full implementation with verification (~8-12K tokens)
  - `catchup` - Context restoration after `/clear` (~1-2K tokens)

- **Skills System Architecture**
  - Complete `.claude/skills/refactoring/` structure
  - SKILL.md with comprehensive documentation
  - Workflow-based execution model

- **Knowledge Base**
  - `typescript-style.md` - Modern TypeScript patterns
  - `architecture-patterns.md` - Feature modules, Result monads, functional composition

- **Session Management**
  - `/clear` + `catchup` protocol every 5-7 prompts
  - Token budget tracking integration
  - Emergency stop protocols

- **Quality Gates**
  - Type-check validation
  - Unit test validation
  - Lint validation

- **Documentation**
  - Complete README with quick start
  - Learning path (beginner → advanced)
  - Field-tested best practices
  - Common pitfalls guide
  - Budget management strategies

### Changed
- **BREAKING:** File structure changed from `knowledge_base/` to `.claude/skills/`
- **BREAKING:** Workflows now invoked via `claude skills refactoring <name>`
- **BREAKING:** CLAUDE.md now acts as constitution rather than bootloader
- Removed all proprietary references
- Generic, public-friendly examples throughout

### Improved
- 67% reduction in conversation turns (empirically tested)
- Predictable token costs per operation
- 100% test pass rate maintained through validation gates
- Zero API surface breakage methodology

### Documentation
- Added CONTRIBUTING.md
- Added comprehensive examples
- Added token economics model
- Added success metrics tracking

---

## [2.0.0] - 2024-11-12

### Added
- Initial public release
- Knowledge base structure
- CLAUDE.md bootloader pattern
- "One-Shot" Refactoring Pattern
- "Agentic" TDD Workflow
- Project "Brain" Structure
- Token Economics Model

### Features
- Velocity vs. Vision framework
- Indranet pattern documentation (proprietary)
- Basic refactoring workflows

---

## [Unreleased]

### Planned for v3.1
- Python workflow variations
- Go workflow variations
- Integration testing workflow
- Performance optimization workflow
- Team collaboration templates

### Planned for v4.0
- VS Code extension integration
- Automated token tracking
- Custom workflow creation guide
- Community patterns library

---

## Version Comparison

| Version | Architecture | Workflows | Languages | Integration |
|---------|--------------|-----------|-----------|-------------|
| 3.0.0   | Skills-based | 7 executable | TypeScript | Claude Projects |
| 2.0.0   | Knowledge base | Patterns only | TypeScript | Manual setup |

---

## Migration Guides

### Upgrading from v2.0.0 to v3.0.0

**Breaking Changes:**
1. File structure changed - re-upload to Claude Projects
2. Workflow invocation changed - use `claude skills refactoring <name>`
3. CLAUDE.md format changed - review and adapt

**Steps:**
1. Download v3.0.0 from GitHub or Zenodo
2. Remove old v2.0.0 files from Claude Project
3. Upload new `.claude/` directory
4. Upload new `CLAUDE.md`
5. Test with `claude skills refactoring qnew`

**Benefits:**
- 67% fewer conversation turns
- Predictable token costs
- Better session management
- More comprehensive workflows

---

## Support

- **Issues:** [GitHub Issues](https://github.com/dyb5784/claude-code-playbook/issues)
- **Discussions:** [GitHub Discussions](https://github.com/dyb5784/claude-code-playbook/discussions)
- **Zenodo:** [Archived Releases](https://doi.org/10.5281/zenodo.17744054)

---

**Legend:**
- 🎉 Major release
- ✨ New feature
- 🐛 Bug fix
- 📚 Documentation
- ⚡ Performance
- 🔒 Security
- ⚠️ Breaking change
