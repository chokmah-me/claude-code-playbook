# CLAUDE.md - ACP Simulation Development Guide

## Project Overview

**ACP Simulation v3.1** - Research-grade Python simulation for Asymmetric Cognitive Projection (ACP) cybersecurity defense strategy validation. This is a scientific computing project focused on statistical validation, reproducibility, and performance optimization.

**Key Technologies:**
- Python 3.8+ (NumPy, SciPy, NetworkX, Matplotlib)
- Multi-agent simulation with 1000+ episodes
- Statistical power analysis with bootstrap validation
- Parallel processing for scalability

## Budget Constraints & Session Management

### Token Budget
- **Limit**: ~44,000 tokens per session (Claude Pro)
- **Target**: 10-40 prompts per 5-hour session
- **Strategy**: Use compact, focused prompts; avoid verbose responses

### Session Management Protocol
1. **Check cost every 3 prompts**: `/cost` to monitor usage
2. **Clear context every 5-7 prompts**: `/clear` then `/catchup` with project summary
3. **Use skills proactively**: Reference `.claude/skills/` for best practices

### Cost-Effective Practices
- ✅ Read skills before asking questions
- ✅ Use compact code reviews (focus on key issues)
- ✅ Request specific file sections, not entire files
- ❌ Avoid repeated explanations of concepts
- ❌ Don't request verbose documentation in responses

## Development Standards

### Validation Requirements

**Before ANY commit, ALL of the following must pass:**

```bash
# 1. Type checking
mypy src/ --strict

# 2. Linting
flake8 src/ --max-line-length=100

# 3. Tests
pytest tests/ -v

# 4. Reproducibility check
python scripts/verify_reproducibility.py
```

**Commit only if ALL FOUR pass with no errors.**

### Python Best Practices

#### 1. Vectorization (Critical for Performance)
```python
# ❌ BAD - Loop over arrays
for i in range(len(agents)):
    rewards[i] = compute_reward(agents[i])

# ✅ GOOD - Vectorized operation
rewards = compute_rewards_vectorized(agent_states)
```

#### 2. Type Hints (Required for All Functions)
```python
from numpy.typing import NDArray
import numpy as np

def process_states(
    states: NDArray[np.float64],
    threshold: float
) -> NDArray[np.bool_]:
    """Process agent states with threshold."""
    return states > threshold
```

#### 3. Configuration Management
```python
from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True)
class SimulationConfig:
    num_episodes: int = 1000
    num_agents: int = 50
    random_seed: int = 42
    
    def save(self, path: str) -> None:
        with open(path, 'w') as f:
            json.dump(asdict(self), f, indent=2)
```

#### 4. Reproducibility (Non-Negotiable)
```python
# Every simulation function MUST accept seed parameter
def run_simulation(config: SimulationConfig, seed: int = 42) -> dict:
    rng = np.random.default_rng(seed)
    # Use rng for all random operations
    noise = rng.standard_normal(100)
    return results
```

### Code Organization Principles

1. **Separate concerns**: Keep simulation logic, analysis, and visualization in different modules
2. **Immutable configs**: Use `frozen=True` on dataclasses
3. **Pure functions**: Minimize side effects, maximize testability
4. **Vectorized operations**: Use NumPy operations instead of Python loops
5. **Explicit dependencies**: Import specific functions, not entire modules

## Claude Skills Integration

### Available Skills

#### 1. Python Scientific Computing (`.claude/skills/python-scientific/`)
**When to use:** Any work on simulation code, numerical analysis, or statistical validation

**Key patterns:**
- Vectorization over loops
- Reproducible random seeds
- Type hints with `numpy.typing`
- Configuration with dataclasses
- NumPy-style docstrings

**Usage:**
```bash
# Start session reading the skill
/clear
view .claude/skills/python-scientific/SKILL.md
```

#### 2. General Refactoring (`.claude/skills/refactoring/`)
**When to use:** Architectural changes, code organization, modernization

**Workflows available:**
- `triage` - Identify issues in codebase
- `extract` - Extract reusable components
- `modernize` - Update to modern patterns
- `qnew`, `qplan`, `qcode` - Quick development workflows

**Usage:**
```bash
# Quick triage
claude skills refactoring triage

# Start new feature
claude skills refactoring qnew
```

### Skill Selection Guide

| Task | Primary Skill | Secondary Skill |
|------|---------------|-----------------|
| Optimize simulation loop | Python Scientific | - |
| Fix numerical stability | Python Scientific | - |
| Add configuration option | Python Scientific | - |
| Restructure modules | General Refactoring | - |
| Add new analysis | Python Scientific | General Refactoring |
| Performance profiling | Python Scientific | - |
| Type hint addition | Python Scientific | - |

## Research-Specific Guidelines

### Statistical Validation
- **Always** report confidence intervals (not just means)
- **Always** include effect sizes (Cohen's d)
- **Always** verify statistical power (target: ≥80%)
- **Always** use bootstrap validation for non-parametric tests

### Reproducibility Requirements
1. **Seed everything**: NumPy, random, any stochastic process
2. **Save configurations**: JSON files with all parameters
3. **Log versions**: Python, NumPy, SciPy, custom code
4. **Include timestamps**: ISO format for all runs
5. **Track git commits**: Include commit hash in results

### Performance Optimization Workflow
1. **Profile first**: Use cProfile to identify bottlenecks
2. **Measure baseline**: Record current performance
3. **Optimize**: Apply vectorization, algorithmic improvements
4. **Verify correctness**: Ensure results unchanged (use fixed seed)
5. **Measure improvement**: Quantify speedup
6. **Document**: Note optimization in commit message

## Commit Standards

### Commit Message Format
```
<type>(<scope>): <short description>

<detailed description>

Performance: <metrics if applicable>
Reproducibility: <verification if applicable>
Tests: <test coverage if applicable>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `perf`: Performance improvement
- `refactor`: Code restructure without behavior change
- `test`: Add or update tests
- `docs`: Documentation changes

**Example:**
```
perf(simulation): vectorize agent decision computation

Replaced loop-based decision logic with vectorized NumPy operations.
Reduces per-episode time from 3.2s to 0.8s (4x speedup).

Performance:
  - Before: 322 episodes/second
  - After: 1288 episodes/second
  
Reproducibility: Verified with seed=42, results identical
Tests: Added test_vectorized_decisions, all tests pass
```

## Development Workflows

### Starting a Session
```bash
# 1. Check current project state
/cost  # Check token budget
view CLAUDE.md  # Review guidelines

# 2. Load relevant skill
view .claude/skills/python-scientific/SKILL.md

# 3. Start work
<work on task>

# 4. Monitor usage
/cost  # After ~3 prompts
```

### Adding a Feature
```bash
# 1. Read skill
view .claude/skills/python-scientific/SKILL.md

# 2. Implement with patterns
- Use type hints
- Add docstrings (NumPy style)
- Include seed parameter
- Vectorize operations

# 3. Test
pytest tests/test_new_feature.py

# 4. Verify reproducibility
python scripts/verify_reproducibility.py

# 5. Commit
git add <files>
git commit -m "feat(module): add <feature>"
```

### Optimizing Performance
```bash
# 1. Profile
python -m cProfile -o profile.stats src/simulation.py

# 2. Analyze
view .claude/skills/python-scientific/SKILL.md
# Focus on "Performance Profiling" section

# 3. Identify bottlenecks
python -c "import pstats; p = pstats.Stats('profile.stats'); p.sort_stats('cumulative'); p.print_stats(20)"

# 4. Optimize (vectorization, algorithmic improvement)

# 5. Verify correctness
python tests/test_correctness.py --seed 42

# 6. Measure improvement
python benchmark.py
```

### Running Experiments
```bash
# 1. Create config
python scripts/create_config.py \
  --num-episodes 10000 \
  --num-agents 100 \
  --seed 42

# 2. Run simulation
python src/main.py --config configs/experiment_001.json

# 3. Verify reproducibility
python src/main.py --config configs/experiment_001.json
# Results should be identical

# 4. Analyze
python scripts/analyze_results.py outputs/experiment_001/
```

## Quick Reference

### Essential Commands
```bash
# Development
pytest tests/ -v                    # Run tests
mypy src/ --strict                  # Type check
flake8 src/ --max-line-length=100  # Lint

# Profiling
python -m cProfile -o profile.stats script.py
kernprof -l -v script.py           # Line profiling

# Reproducibility
python scripts/verify_reproducibility.py

# Session Management
/cost                              # Check token usage
/clear                             # Clear context
/catchup                           # Resume with summary
```

### File Structure
```
.
├── .claude/
│   └── skills/
│       ├── python-scientific/    # Scientific Python patterns
│       └── refactoring/          # Architecture patterns
├── src/                          # Source code
├── tests/                        # Test suite
├── scripts/                      # Utility scripts
├── configs/                      # Experiment configurations
├── outputs/                      # Results (git-ignored)
└── CLAUDE.md                     # This file
```

### Model Selection
- **Sonnet 4.5**: Default for all development (best performance/cost)
- **Opus 4**: Only for complex architectural decisions (use sparingly)

## Common Patterns

### Pattern: Reproducible Experiment
```python
from dataclasses import dataclass
import numpy as np
from pathlib import Path

@dataclass(frozen=True)
class ExperimentConfig:
    num_episodes: int = 1000
    random_seed: int = 42
    
    def save(self, path: Path) -> None:
        import json
        from dataclasses import asdict
        with open(path, 'w') as f:
            json.dump(asdict(self), f, indent=2)

def run_experiment(config: ExperimentConfig) -> dict:
    """Run experiment with full reproducibility."""
    # Save config
    output_dir = Path('outputs') / f'exp_{config.random_seed}'
    output_dir.mkdir(parents=True, exist_ok=True)
    config.save(output_dir / 'config.json')
    
    # Log versions
    import sys, scipy
    versions = {
        'python': sys.version,
        'numpy': np.__version__,
        'scipy': scipy.__version__
    }
    
    # Run with seed
    rng = np.random.default_rng(config.random_seed)
    # ... experiment code ...
    
    return {
        'results': results,
        'config': config,
        'versions': versions
    }
```

### Pattern: Vectorized Agent Updates
```python
def update_agents_vectorized(
    states: NDArray[np.float64],
    actions: NDArray[np.int64],
    rewards: NDArray[np.float64],
    learning_rate: float
) -> NDArray[np.float64]:
    """Update all agent states in one vectorized operation."""
    # Instead of: for i in range(len(states)): ...
    return states + learning_rate * rewards[:, np.newaxis]
```

## Thesis Defense Preparation

### Quality Checklist
- [ ] All experiments reproducible with fixed seeds
- [ ] Statistical power ≥80% for all claims
- [ ] Confidence intervals reported for all estimates
- [ ] Effect sizes (Cohen's d) reported
- [ ] Version information logged
- [ ] Configuration files saved
- [ ] Publication-quality figures (300 DPI)
- [ ] Code passes all validation checks

### Key Metrics to Report
1. **Performance**: Episodes per second, scaling factor
2. **Statistical**: p-values, confidence intervals, effect sizes, power
3. **Reproducibility**: Seed, versions, git commit
4. **Validation**: All tests pass, type checking clean

## Contact & Support

For questions or issues:
1. Check `.claude/skills/python-scientific/SKILL.md`
2. Review this file (CLAUDE.md)
3. Use `/cost` to check if context refresh needed
4. Use `/clear` + `/catchup` if approaching token limit

---

**Version**: 3.1.0  
**Last Updated**: 2025-12-11  
**Model**: Claude Sonnet 4.5  
**Focus**: Research-grade Python scientific computing
