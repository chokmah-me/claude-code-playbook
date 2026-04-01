# Claude Skills Directory

This directory contains skills for AI-assisted development with Claude Code.

## Directory Structure

```
.claude/skills/
├── README.md (this file)
├── python-scientific/         # Python scientific computing patterns
│   └── SKILL.md              # NumPy, reproducibility, performance
├── refactoring/              # General code refactoring
│   ├── SKILL.md              # Skill overview
│   ├── workflows/            # Development workflows
│   │   ├── triage.md
│   │   ├── extract.md
│   │   ├── modernize.md
│   │   ├── qnew.md
│   │   ├── qplan.md
│   │   ├── qcode.md
│   │   └── catchup.md
│   └── knowledge/            # Reference materials
│       ├── typescript-style.md
│       └── architecture-patterns.md
├── debugging/                # Bug diagnosis & root-cause analysis
│   ├── SKILL.md
│   └── workflows/
│       ├── diagnose.md       # Reproduce → isolate → hypothesize → verify → fix
│       └── trace.md          # Trace execution paths through codebase
├── documentation/            # Documentation accuracy & generation
│   ├── SKILL.md
│   └── workflows/
│       ├── audit.md          # Scan for code/docs drift
│       └── generate.md       # Generate docs from code
└── onboarding/               # Codebase orientation for newcomers
    ├── SKILL.md
    └── workflows/
        ├── orient.md         # Guided architecture walkthrough
        └── glossary.md       # Extract domain vocabulary
```

## Available Skills

### 1. Python Scientific Computing

**Location**: `skills/python-scientific/SKILL.md` (also mirrored to `.claude/skills/python-scientific/SKILL.md`)

**Purpose**: Best practices for research-grade Python development with NumPy/SciPy

**Key Topics**:
- Vectorization over loops
- Random seed management for reproducibility  
- Type hints with `numpy.typing`
- Configuration management with dataclasses
- Parallel processing patterns
- Testing numerical code
- Performance profiling
- Memory-efficient operations
- NumPy-style docstrings

**When to Use**:
- Working on simulation code
- Numerical analysis and statistical validation
- Performance optimization
- Ensuring reproducibility
- Writing research code for publication

**Quick Start**:
```bash
# Load skill at session start
view .claude/skills/python-scientific/SKILL.md

# Then work on your code with patterns in mind
```

### 2. General Refactoring

**Location**: `.claude/skills/refactoring/SKILL.md`

**Purpose**: Structured workflows for code quality improvement and architecture

**Available Workflows**:
- **triage**: Identify issues in codebase
- **extract**: Extract reusable components
- **modernize**: Update to modern patterns
- **qnew**: Quick new feature development
- **qplan**: Quick planning session
- **qcode**: Quick coding session  
- **catchup**: Resume after context clear

**When to Use**:
- Architectural decisions
- Code organization and structure
- Feature development
- Technical debt reduction

**Quick Start**:
```bash
# Use a specific workflow
claude skills refactoring triage
claude skills refactoring qnew
```

### 3. Debugging & Root-Cause Analysis

**Location**: `.claude/skills/debugging/SKILL.md`

**Purpose**: Structured bug diagnosis instead of guess-and-check

**Available Workflows**:
- **diagnose**: Full root-cause cycle (reproduce → isolate → hypothesize → verify → fix)
- **trace**: Map execution paths through unfamiliar code

**When to Use**:
- Test failures with non-obvious causes
- Runtime errors or unexpected behavior
- Understanding how data flows through the system

### 4. Documentation

**Location**: `.claude/skills/documentation/SKILL.md`

**Purpose**: Keep docs accurate and generate docs from code

**Available Workflows**:
- **audit**: Find discrepancies between docs and code
- **generate**: Create markdown docs from code signatures

**When to Use**:
- Before releases (verify doc accuracy)
- After major refactors (update affected docs)
- New modules that need documentation

### 5. Onboarding & Repo Orientation

**Location**: `.claude/skills/onboarding/SKILL.md`

**Purpose**: Build a mental model of an unfamiliar codebase quickly

**Available Workflows**:
- **orient**: Structured walkthrough (architecture → key files → conventions → gotchas)
- **glossary**: Extract domain terms and project vocabulary

**When to Use**:
- First time in a repository
- Onboarding new team members
- Cross-team work requiring shared vocabulary

## Skill Selection Guide

| Task Type | Primary Skill | Notes |
|-----------|---------------|-------|
| Optimize simulation | Python Scientific | Focus on vectorization |
| Add type hints | Python Scientific | Use numpy.typing |
| Fix numerical bug | Python Scientific | Check reproducibility |
| Restructure modules | Refactoring | Use extract workflow |
| Add new feature | Python Scientific + Refactoring | Combine both |
| Performance tuning | Python Scientific | Profile first |
| Code review | Refactoring | Check patterns |
| Debug test failure | Debugging | Use diagnose workflow |
| Trace data flow | Debugging | Use trace workflow |
| Verify docs accuracy | Documentation | Use audit workflow |
| Generate module docs | Documentation | Use generate workflow |
| New to a codebase | Onboarding | orient + glossary |
| Understand domain terms | Onboarding | Use glossary workflow |

## Usage Patterns

### Starting a Session

1. **Clear context** if needed: `/clear`
2. **Load appropriate skill**: `view .claude/skills/<skill>/SKILL.md`
3. **Work with patterns**: Apply skill guidelines to your code

### During Development

- **Check cost**: `/cost` every ~3 prompts
- **Reference skills**: View specific sections as needed
- **Follow patterns**: Use examples from SKILL.md files

### Before Committing

Verify your changes follow skill patterns:

```bash
# For Python scientific code
- [ ] Vectorized operations used
- [ ] Type hints added  
- [ ] Reproducibility verified
- [ ] NumPy-style docstrings
- [ ] Tests pass

# For refactoring work
- [ ] Code well-organized
- [ ] Modern patterns used
- [ ] Technical debt reduced
- [ ] Architecture improved
```

## Integration with CLAUDE.md

The skills in this directory support the development guidelines in `CLAUDE.md`:

- `CLAUDE.md` defines **project-level standards** and **validation requirements**
- Skills provide **implementation patterns** and **best practices**
- Together they ensure code quality and research reproducibility

## Adding New Skills

To add a new skill:

1. Create directory: `.claude/skills/<skill-name>/`
2. Add `SKILL.md` with:
   - Overview and purpose
   - When to use the skill
   - Key patterns with examples
   - Quick reference
3. Update this `README.md`
4. Reference in `CLAUDE.md` if needed

## Version History

- **v2.0** (2026-04-01): Added Debugging, Documentation, and Onboarding skills
- **v1.0** (2025-12-11): Initial skills directory with Python Scientific Computing
- **v0.9** (2025-12-10): General Refactoring skill added

## See Also

- `../../CLAUDE.md` - Project development guidelines
- `../../docs/AI_ASSISTED_DEVELOPMENT.md` - AI integration documentation
- `../../VERSION_CHANGELOG.md` - Project version history
