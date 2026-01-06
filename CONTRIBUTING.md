# Contributing to Claude Code Playbook

Thank you for your interest in contributing! This playbook is a community effort to democratize AI-assisted development.

---

## 🎯 Ways to Contribute

### 1. Share Your Experience
- Open an issue describing your success story
- Share metrics (token savings, time saved, etc.)
- Describe challenges you faced and how you solved them

### 2. Report Bugs
- Use GitHub Issues with the `bug` label
- Include steps to reproduce
- Share relevant context (OS, Claude version, workflow used)

### 3. Request Features
- Open an issue with the `enhancement` label
- Describe the use case
- Explain why it would help others

### 4. Improve Documentation
- Fix typos or unclear language
- Add examples or clarifications
- Translate to other languages

### 5. Add Workflows
- Create new workflow patterns for different use cases
- Follow the existing workflow structure
- Include token cost estimates

### 6. Contribute Patterns
- Add to `architecture-patterns.md` or `typescript-style.md`
- Include code examples
- Explain when to use the pattern

---

## 🔧 Development Setup

```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/claude-code-playbook.git
cd claude-code-playbook

# Create a branch for your changes
git checkout -b feature/your-feature-name

# Make your changes
# ...

# Test with Claude Code or claude.ai
# Upload .claude/ directory to a test project

# Commit and push
git add .
git commit -m "feat: add your feature description"
git push origin feature/your-feature-name
```

---

## 📝 Commit Message Convention

We follow conventional commits:

- `feat:` New feature or workflow
- `fix:` Bug fix
- `docs:` Documentation changes
- `refactor:` Code refactoring
- `test:` Adding tests
- `chore:` Maintenance tasks

Examples:
```
feat: add Python workflow variations
fix: correct token cost in qcode workflow
docs: improve quick start guide
refactor: simplify triage scoring algorithm
```

---

## 🎨 Workflow Structure

When adding new workflows, follow this structure:

```markdown
---
name: workflow-name
description: "Brief description of what this does"
---

# Workflow Title

## Purpose
Clear description of when to use this workflow

## Prerequisites
What needs to be in place before running

## Step 1: First Action
Detailed instructions...

## Step 2: Next Action
Detailed instructions...

## Budget Awareness
**Estimated token cost:** ~XK tokens

## Success Criteria
When is this workflow complete?
```

---

## 📊 Testing Guidelines

Before submitting a workflow:

1. **Test it yourself** on at least one real project
2. **Measure token costs** with `/cost` command
3. **Document edge cases** you discovered
4. **Include examples** of before/after

---

## 🔍 Code Review Process

1. **Submit PR** with clear description
2. **Maintainer reviews** within 1 week
3. **Address feedback** if any
4. **Merge** when approved

---

## 🌍 Multi-Language Support

If adding support for a new language:

1. Create `{language}-style.md` in `knowledge/`
2. Adapt workflows for language-specific patterns
3. Update main README with language support
4. Include examples in the new language

---

## 💡 Adding Patterns

When contributing to pattern libraries:

1. **Include code examples** (do's and don'ts)
2. **Explain the why** not just the what
3. **Show real-world usage** when possible
4. **Keep it concise** but complete

---

## 🚫 What NOT to Include

Please avoid:
- Proprietary or confidential patterns
- Company-specific workflows
- Personal file paths or credentials
- Workflows that encourage unsafe practices
- Overly complex or niche patterns

---

## 📋 Pull Request Checklist

Before submitting:

- [ ] Tested the changes yourself
- [ ] Updated relevant documentation
- [ ] Followed commit message convention
- [ ] Added examples if applicable
- [ ] Checked for typos and formatting
- [ ] Verified no proprietary content
- [ ] Token costs measured (for workflows)

---

## 🎓 Getting Help

Need help contributing?

- **Questions:** Use [GitHub Discussions](https://github.com/chokmah-me/claude-code-playbook/discussions)
- **Guidance:** Tag @dyb in your issue
- **Examples:** Look at merged PRs for reference

---

## 🏆 Recognition

Contributors will be:
- Listed in release notes
- Acknowledged in README
- Credited in relevant documentation

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## 🙏 Thank You

Every contribution, no matter how small, helps developers worldwide work more efficiently with AI. Thank you for being part of this community!

---

**Questions?** Open a [discussion](https://github.com/chokmah-me/claude-code-playbook/discussions) or issue.
