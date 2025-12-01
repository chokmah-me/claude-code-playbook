# Claude Code Playbook

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17744054.svg)](https://doi.org/10.5281/zenodo.17744054)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/dyb5784/claude-code-playbook/releases)

> **Token-efficient AI engineering for everyone**  
> A public contribution to democratizing AI-assisted software development

---

## 🎯 What is This?

The Claude Code Playbook is a **skills-based system** that helps developers maximize value from Claude Pro subscriptions while maintaining code quality. It transforms traditional multi-turn AI conversations into efficient, predictable workflows.

### The Problem
- Claude Pro has hard token limits (10-40 prompts per 5 hours)
- Traditional chat workflows waste tokens on back-and-forth
- Simple refactoring tasks often require 5-10+ conversation turns
- No standardized approach to budget-aware AI collaboration

### The Solution
- **6 executable workflows** that compress common tasks
- **Empirical token costs** for predictable budget planning
- **67% reduction** in conversation turns
- **100% test pass rate** maintained through validation gates

---

## 🚀 Quick Start

### Installation

```bash
# Clone this repository
git clone https://github.com/dyb5784/claude-code-playbook.git
cd claude-code-playbook

# Upload to Claude Project
# 1. Open claude.ai
# 2. Create or open a Project
# 3. Upload the .claude/ directory to Project Knowledge
# 4. Upload CLAUDE.md to Project Knowledge
```

### Your First Session

```bash
# In Claude Code or claude.ai Project:

# Initialize session
/clear
claude skills refactoring qnew

# Analyze your codebase
claude skills refactoring triage

# Get your top 3 technical debt priorities!
```

---

## 📊 Available Workflows

| Workflow | Purpose | Cost | When to Use |
|----------|---------|------|-------------|
| **triage** | Find top 3 technical debt hotspots | ~2K tokens | Start of project |
| **qnew** | Initialize session with context | ~2K tokens | Start of work day |
| **qplan** | Validate refactoring plan | ~3K tokens | Before implementation |
| **extract** | Extract function to new module | ~5K tokens | Targeted decomposition |
| **modernize** | Update to modern patterns | ~4K tokens | Pattern upgrades |
| **qcode** | Full implementation (max 15 files) | ~8-12K tokens | Execute approved plan |
| **catchup** | Restore context after `/clear` | ~1-2K tokens | Every 5-7 prompts |

### Invoke Workflows

```bash
claude skills refactoring <workflow-name>

# Examples:
claude skills refactoring triage
claude skills refactoring extract
claude skills refactoring qcode
```

---

## 💡 Key Features

### Modern Architecture Patterns
- Feature-based module structure
- Result<T,E> monads for error handling
- Functional composition over classes
- Configuration-driven logic
- Dependency injection via factory functions

### Budget Management
- Session reset protocol (`/clear` + `catchup` every 5-7 prompts)
- Token usage checkpoints
- Predictable costs per operation
- Empirically tested on production codebases

### Quality Gates
Every change must pass:
- ✅ Type check (0 errors)
- ✅ Unit tests (all passing)
- ✅ Lint (0 warnings)

---

## 📂 Repository Structure

```
.claude/skills/refactoring/
├── SKILL.md                    # Complete overview
├── workflows/                  # 7 executable workflows
│   ├── triage.md              # Technical debt analysis
│   ├── extract.md             # Function extraction
│   ├── modernize.md           # Pattern updates
│   ├── qnew.md                # Session initialization
│   ├── qplan.md               # Plan validation
│   ├── qcode.md               # Full implementation
│   └── catchup.md             # Context restoration
└── knowledge/                  # Reference documentation
    ├── typescript-style.md    # Modern TS patterns
    └── architecture-patterns.md # Feature modules, Result monads
```

---

## 🎓 Learning Path

### Beginner (Sessions 1-2)
1. Run `qnew` to start
2. Use `triage` to understand your codebase
3. Extract 1 simple function with `extract`
4. Practice `/clear` + `catchup` protocol

### Intermediate (Sessions 3-10)
1. Use `qplan` before extractions
2. Extract 2-3 functions per session
3. Apply `modernize` to update patterns
4. Track progress in `REFACTOR_PROGRESS.md`

### Advanced (Sessions 10+)
1. Use `qcode` for batch operations (10-15 files)
2. Design custom extraction strategies
3. Contribute patterns back to knowledge base

---

## 📈 Empirical Results

Tested on real-world Discord bot refactoring:
- ✅ Decomposed 1200-line god objects into feature modules
- ✅ 67% reduction in conversation turns
- ✅ 100% test pass rate maintained
- ✅ Zero API surface breakage
- ✅ Predictable token costs per operation

---

## 🤝 Contributing

This is a public contribution to AI-assisted development. We welcome contributions!

### Ways to Contribute
1. **Share your experience** - Open issues with success stories or challenges
2. **Propose new workflows** - Submit PRs with additional workflow patterns
3. **Improve documentation** - Help make this more accessible
4. **Add patterns** - Contribute to `architecture-patterns.md` or `typescript-style.md`
5. **Report bugs** - Found an issue? Let us know

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📋 Roadmap

### v3.1 (Next Release)
- [ ] Python workflow variations
- [ ] Go workflow variations
- [ ] Integration testing workflow
- [ ] Performance optimization workflow
- [ ] Team collaboration templates

### v4.0 (Long-term)
- [ ] VS Code extension integration
- [ ] Automated token tracking
- [ ] Custom workflow creation guide
- [ ] Community patterns library

See [full roadmap](https://github.com/dyb5784/claude-code-playbook/issues) for details.

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

**Philosophy:** AI-assisted development should be accessible to all developers, not just those with expensive API budgets or large organizations.

---

## 🙏 Acknowledgments

- **Anthropic** for Claude Pro and Claude Code
- **TypeScript community** for modern patterns
- **All developers** who provided feedback during field testing
- **You** for using this playbook and contributing to its evolution

---

## 📚 Resources

- **[Documentation](/.claude/skills/refactoring/SKILL.md)** - Complete skill documentation
- **[Zenodo](https://doi.org/10.5281/zenodo.17744054)** - Archived releases
- **[Issues](https://github.com/dyb5784/claude-code-playbook/issues)** - Bug reports and feature requests
- **[Discussions](https://github.com/dyb5784/claude-code-playbook/discussions)** - Community Q&A

---

## 📖 Citation

If you use this playbook in research or professional work, please cite:

```bibtex
@software{claude_playbook_v3,
  author = {dyb5784},
  title = {Claude Code Playbook: Token-Efficient AI Engineering},
  year = {2025},
  version = {3.0.0},
  doi = {10.5281/zenodo.17744054},
  url = {https://github.com/dyb5784/claude-code-playbook}
}
```

---

## 💬 Support

- **Documentation:** Start with [SKILL.md](.claude/skills/refactoring/SKILL.md)
- **Issues:** [Report bugs or request features](https://github.com/dyb5784/claude-code-playbook/issues)
- **Discussions:** [Ask questions](https://github.com/dyb5784/claude-code-playbook/discussions)

---

## ⭐ Show Your Support

If this playbook helps you, please:
- Star this repository
- Share it with other developers
- Contribute improvements
- Cite it in your work

---

**Made with ❤️ for the developer community**

**Version:** 3.0.0  
**License:** MIT  
**Maintainer:** [@dyb5784](https://github.com/dyb5784)
