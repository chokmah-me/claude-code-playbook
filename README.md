# 🤖 Claude Code Playbook

A comprehensive AI-assisted development toolkit for efficient, token-aware collaboration with Claude Code.

**Version**: 1.0.0  
**License**: MIT  
**Repository**: https://github.com/dyb5784/claude-code-playbook

---

## 🎯 What is Claude Code Playbook?

The Claude Code Playbook is a token-efficient AI engineering system that reduces conversation turns by 67% through specialized workflows and systematic development protocols.

### Key Benefits
- **67% reduction** in conversation turns for refactoring tasks
- **Predictable token costs** per operation type
- **Budget-aware development** optimized for Claude Pro limits
- **Reusable across projects** - Apply to any codebase
- **Proven workflows** - Field-tested patterns and practices

---

## 📂 Repository Structure

```
claude-code-playbook/
├── README.md                         # This file
├── LICENSE                           # MIT License
├── CONTRIBUTING.md                   # Contribution guidelines
├── docs/                             # Documentation
│   ├── GETTING_STARTED.md            # Quick start guide
│   ├── WORKFLOW_GUIDE.md             # Workflow usage guide
│   ├── CREATING_SKILLS.md            # Skill development guide
│   └── EXAMPLES.md                   # Usage examples
├── skills/                           # Core skills directory
│   ├── README.md                     # Skills overview
│   ├── python-scientific/            # Python scientific computing
│   │   ├── SKILL.md                  # Main skill file
│   │   └── examples/                 # Code examples
│   └── refactoring/                  # General refactoring
│       ├── SKILL.md                  # Skill overview
│       ├── workflows/                # Workflow definitions
│       │   ├── triage.md
│       │   ├── extract.md
│       │   ├── modernize.md
│       │   ├── qnew.md
│       │   ├── qplan.md
│       │   ├── qcode.md
│       │   └── catchup.md
│       ├── knowledge/                # Reference materials
│       │   ├── typescript-style.md
│       │   └── architecture-patterns.md
│       └── examples/                 # Refactoring examples
├── templates/                        # Project templates
│   ├── CLAUDE.md.template           # Project constitution template
│   ├── .cursorrules.template        # IDE rules template
│   └── python-project/              # Python project template
└── examples/                         # Example projects
    ├── python-scientific-example/   # Python scientific example
    └── refactoring-example/         # Refactoring example
```

---

## 🚀 Quick Start

### For Project Maintainers

1. **Clone the playbook:**
   ```bash
   git clone https://github.com/dyb5784/claude-code-playbook.git
   cd claude-code-playbook
   ```

2. **Copy templates to your project:**
   ```bash
   cp templates/CLAUDE.md.template /path/to/your/project/CLAUDE.md
   cp templates/.cursorrules.template /path/to/your/project/.cursorrules
   ```

3. **Customize the templates** for your project's specific needs

4. **Start using Claude Code** with your project!

### For Claude Code Users

```bash
# Start a session
/clear
claude skills refactoring qnew

# Analyze your codebase
claude skills refactoring triage

# Extract and modernize code
claude skills refactoring extract
claude skills refactoring modernize
```

---

## 📚 Available Skills

### 1. Python Scientific Computing

**Location**: `skills/python-scientific/SKILL.md`

Best practices for research-grade Python development with NumPy/SciPy:
- Vectorization over loops
- Random seed management for reproducibility
- Type hints with `numpy.typing`
- Configuration management with dataclasses
- Parallel processing patterns
- Performance profiling

**Use for**: Scientific simulations, numerical analysis, statistical validation

### 2. General Refactoring

**Location**: `skills/refactoring/SKILL.md`

Structured workflows for code quality improvement:
- **triage**: Identify technical debt hotspots
- **extract**: Extract reusable components
- **modernize**: Update to modern patterns
- **qnew**: Quick new feature development
- **qplan**: Quick planning session
- **qcode**: Full implementation with verification
- **catchup**: Resume after context clear

**Use for**: Architectural changes, code organization, modernization

---

## 📊 Token Economics

### Claude Pro Limits
- **10-40 prompts** per 5-hour window
- **~44,000 tokens** total capacity

### Example Session (Within Budget)
```
qnew:        2K tokens
triage:      2K tokens
qplan:       3K tokens
extract #1:  5K tokens
/clear + catchup: 1K tokens
extract #2:  5K tokens
modernize:   4K tokens
─────────────────────────
Total:      22K tokens (50% of budget)
```

### Session Management Protocol
**Every 5-7 prompts, execute:**
```bash
/cost                              # Check token usage
/clear                             # Reset context
claude skills refactoring catchup  # Restore context
```

---

## 🎓 Learning Path

### Beginner (Sessions 1-2)
1. Read `docs/GETTING_STARTED.md`
2. Run `claude skills refactoring qnew`
3. Use `triage` to understand your codebase
4. Extract 1 simple function with `extract`
5. Practice `/clear` + `catchup` protocol

### Intermediate (Sessions 3-10)
1. Use `qplan` before extractions
2. Extract 2-3 functions per session
3. Apply `modernize` to update patterns
4. Track progress in `REFACTOR_PROGRESS.md`

### Advanced (Sessions 10+)
1. Use `qcode` for batch operations (10-15 files)
2. Design custom extraction strategies
3. Contribute patterns back to knowledge base
4. Create new skills for your domain

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to Contribute
- Add new skills for different domains
- Improve existing workflows
- Add examples and use cases
- Report bugs and suggest features
- Improve documentation

---

## 📖 Documentation

- **[docs/GETTING_STARTED.md](docs/GETTING_STARTED.md)** - Quick start guide
- **[docs/WORKFLOW_GUIDE.md](docs/WORKFLOW_GUIDE.md)** - Detailed workflow usage
- **[docs/CREATING_SKILLS.md](docs/CREATING_SKILLS.md)** - How to create new skills
- **[docs/EXAMPLES.md](docs/EXAMPLES.md)** - Real-world usage examples

---

## 🏆 Success Stories

This playbook was originally developed for the [ACP Simulation](https://github.com/dyb5784/acp-simulation) project, where it achieved:
- **67% reduction** in conversation turns
- **100% test pass rate** maintained throughout refactoring
- **Zero API breakage** with systematic validation gates
- **40% improvement** in code maintainability

---

## 📞 Support

**For playbook issues:**
1. Check [docs/WORKFLOW_GUIDE.md](docs/WORKFLOW_GUIDE.md)
2. Review skill documentation in `skills/`
3. Open an issue on GitHub

**For Claude Code issues:**
- See [Claude Code Documentation](https://docs.claude.com/claude-code)

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

**Version**: 1.0.0  
**Date**: December 11, 2025  
**Status**: ✅ Production Ready
