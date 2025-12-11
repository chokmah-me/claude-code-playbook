# 🤖 Claude Code Playbook

**Version**: 4.0.0

**License**: MIT

**DOI**: [10.5281/zenodo.17781760](https://doi.org/10.5281/zenodo.17781760)

**Repository**: https://github.com/dyb5784/claude-code-playbook

A token-efficient AI engineering system that reduces conversation turns by 67% through specialized workflows.

---

## 🎯 What is v4.0.0?

Complete AI-assisted development system with two specialized skills and seven production workflows.

**Key Features:**
- **Python Scientific Computing**: Research-grade patterns for NumPy/SciPy
- **General Refactoring**: 7 structured workflows (triage, extract, modernize, qnew, qplan, qcode, catchup)
- **Project Templates**: CLAUDE.md.template and .cursorrules.template
- **Token Optimization**: 67% reduction in conversation turns

---

## 📂 Quick Start

**1. Clone and setup:**
```bash
git clone https://github.com/dyb5784/claude-code-playbook.git
cd claude-code-playbook
cp templates/CLAUDE.md.template /path/to/your/project/CLAUDE.md
cp templates/.cursorrules.template /path/to/your/project/.cursorrules
```

**2. Start using:**
```bash
/clear
claude skills refactoring qnew
claude skills refactoring triage
```

---

## 📊 Token Economics

**Claude Pro Optimization:**
- 10-40 prompts per 5-hour window
- ~44,000 tokens total capacity
- Example session: 22K tokens (50% of budget)

**Workflow Costs:**
- triage: 2K | qnew: 2K | qplan: 3K | extract: 5K
- modernize: 4K | qcode: 8-12K | catchup: 1-2K

**Session Protocol (every 5-7 prompts):**
```bash
/cost                              # Check usage
/clear                             # Reset context
claude skills refactoring catchup  # Restore context
```

---

## 📚 Available Skills

### Python Scientific Computing
**Location**: `skills/python-scientific/SKILL.md`

Vectorization, reproducibility, type hints, configuration, parallel processing, performance profiling.

### General Refactoring
**Location**: `skills/refactoring/SKILL.md`

7 workflows: triage, extract, modernize, qnew, qplan, qcode, catchup.

---

## 📖 Documentation

- **[docs/GETTING_STARTED.md](docs/GETTING_STARTED.md)** - Step-by-step guide

- **[docs/WORKFLOW_GUIDE.md](docs/WORKFLOW_GUIDE.md)** - Detailed workflow usage

- **[skills/README.md](skills/README.md)** - Skill selection guide

---

## 🎓 Learning Path

**Beginner:** Read docs → Run qnew → Use triage → Extract 1 function

**Intermediate:** Use qplan → Extract 2-3 functions → Apply modernize

**Advanced:** Use qcode (10-15 files) → Design custom strategies → Contribute back

---

## 🏆 Success Metrics

Originally developed for [ACP Simulation](https://github.com/dyb5784/acp-simulation):
- 67% reduction in conversation turns
- 100% test pass rate maintained
- Zero API breakage
- 40% improvement in maintainability

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

## 📞 Support

**Issues:** Open on GitHub
**Claude Code Docs:** https://docs.claude.com/claude-code

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

**Version**: 4.0.0 | **Date**: December 11, 2025 | **Status**: ✅ Production Ready
