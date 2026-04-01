# 📊 Token Economics

**Complete guide to optimizing token usage and managing Claude Pro limits effectively.**

---

## 💰 Token Efficiency Strategy

### Modern Claude Models (2026+)
- **Capacity**: Extended context windows; no fixed 44K token ceiling
- **Cost model**: Usage-based pricing (exact limits depend on plan)
- **Best practice**: Monitor actual usage via Claude Code UI rather than preset budgets

### Practical Efficiency Targets
- **Healthy per-session usage**: 10-30K tokens (varies by task complexity)
- **Per-prompt guideline**: 1-3K tokens typical
- **Session planning**: Batch work logically; longer sessions are OK if on-track

**Token Efficiency Strategy:**
- Use Explore subagents for codebase analysis (more efficient than manual grepping)
- Use Plan Mode before major implementations
- Maintain `REFACTOR_PROGRESS.md` for multi-session context persistence
- Commit atomically to avoid re-explaining context

---

## ⚡ Workflow Costs (Relative Guide)

### Refactoring Workflows
| Workflow | Relative Cost | Use Case | When |
|----------|---------------|----------|------|
| `triage` | Low (~2K) | Initial codebase analysis | Start of project |
| `qnew` | Low (~2K) | Start new session | Session start |
| `qplan` | Medium (~3K) | Plan refactoring approach | Before major changes |
| `extract` | Medium (~5K) | Extract functions/modules | Targeted decomposition |
| `modernize` | Medium (~4K) | Update code patterns | Post-extraction |
| `qcode` | High (~8-12K) | Full implementation | Execute approved plan |
| `catchup` | Low (~1-2K) | Resume from progress file | Between sessions |

### Python Scientific Computing
| Workflow | Token Cost | Use Case |
|----------|------------|----------|
| Vectorization review | 3,000 tokens | Optimize array operations |
| Type hint analysis | 2,000 tokens | Add type annotations |
| Performance profiling | 4,000 tokens | Identify bottlenecks |
| Parallel processing | 5,000 tokens | Optimize for multiprocessing |

---

## 🔄 Session Protocol

### Multi-Session Continuity
Before stopping work:
1. Update `REFACTOR_PROGRESS.md` with completed tasks and next steps
2. Commit your work atomically with clear messages
3. On resumption: read `REFACTOR_PROGRESS.md`, then run `claude skills refactoring catchup`

**Why this works:**
- Persistent context across session breaks
- No manual context reset needed
- Clear handoff for resumption

### Example Session Flow
```
Session Goal: Extract 3 utility functions

1. triage         (~2K tokens)  - identify candidates
2. qplan          (~3K tokens)  - design extraction strategy
3. extract × 3    (~15K tokens) - implement extractions
4. commit + notes (~1K tokens)  - save progress

Total: ~21K tokens
```

---

## 📈 Token Usage Monitoring

### Real-time Monitoring
```bash
# Check current usage
/cost

# Check after major operations
claude skills refactoring qcode
/cost

# Check before context reset
/cost
/clear
```

### Daily Usage Tracking
```bash
# Start of day
Session 1: 22,000 tokens ✅
Session 2: 18,000 tokens ✅
Session 3: 25,000 tokens ⚠️ (close to limit)
Session 4: 15,000 tokens ✅
```

---

## 🎯 Optimization Strategies

### 1. Context Management
**Problem**: Growing context reduces available tokens  
**Solution**: Reset every 5-7 prompts
```bash
# Before: 35,000 tokens (dangerous)
# After reset: 8,000 tokens (safe)
```

### 2. Workflow Selection
**Problem**: Using expensive workflows for simple tasks  
**Solution**: Match workflow to task complexity
```bash
# For simple refactoring:
cctriage + ccextract  # 7,000 tokens total

# For complex refactoring:
cctriage + ccplan + cccode  # 17,000 tokens total
```

### 3. Prompt Efficiency
**Problem**: Long, rambling prompts waste tokens  
**Solution**: Concise, structured prompts
```bash
# Inefficient (500 tokens):
"Can you please help me understand what's wrong with my code, I've been trying to figure it out for hours..."

# Efficient (100 tokens):
"Analyze /src/main.py for performance issues. Focus on function complexity and database queries."
```

### 4. Response Filtering
**Problem**: Unnecessarily detailed responses  **Solution**: Specify output requirements
```bash
# Efficient request:
"List the top 3 performance issues in /src/main.py. Bullet points only, no explanations."
```

---

## ⚠️ Warning Signs

### High Token Usage Indicators
- **Single prompt >3,000 tokens** ⚠️
- **Session >30,000 tokens** 🚨
- **Context >35,000 tokens** 🚨
- **Multiple sessions >25,000 tokens** ⚠️

### Performance Degradation Signs
- Slow response times
- Repetitive or circular suggestions
- Loss of project context
- Increasing token usage per prompt

---

## 💡 Advanced Optimization Techniques

### 1. Strategic Context Resetting
```bash
# Before complex operation
/cost
# If >20,000 tokens, reset
/clear
claude skills refactoring catchup
# Now you have fresh 8,000 token context
```

### 2. Workflow Chaining
```bash
# Efficient chaining:
cctriage && ccplan && cccode
# Total: 17,000 tokens in optimized context

# Inefficient chaining:
cctriage
# ... 10 prompts later ...
ccplan  
# ... 10 prompts later ...
cccode
# Total: 25,000+ tokens with degraded context
```

### 3. Selective Context Restoration
```bash
# After reset, only restore what's needed
claude skills refactoring catchup
# Focus on current task, not entire session history
```

---

## 📊 Token Economics by Use Case

### Code Review Session (15 minutes)
```bash
cctriage          # 2,000 tokens
ccreview          # 3,000 tokens
# 5 prompts       # 5,000 tokens
cccommit          # 2,000 tokens
Total: 12,000 tokens ✅
```

### Feature Implementation (30 minutes)
```bash
ccnew             # 2,000 tokens
ccplan            # 3,000 tokens
cccode            # 10,000 tokens
# 8 prompts       # 8,000 tokens
ccextract         # 5,000 tokens
cccommit          # 2,000 tokens
Total: 30,000 tokens ⚠️ (split into 2 sessions)
```

### Bug Fixing (20 minutes)
```bash
cctriage          # 2,000 tokens
ccfix             # 4,000 tokens
# 6 prompts       # 6,000 tokens
cccommit          # 2,000 tokens
Total: 14,000 tokens ✅
```

---

## 🎓 Learning Path for Token Efficiency

### Beginner Level (Week 1-2)
- ✅ Learn to check costs with `/cost`
- ✅ Reset context every 5-7 prompts
- ✅ Use efficient prompt structure
- **Target**: <30,000 tokens per session

### Intermediate Level (Week 3-4)
- ✅ Plan sessions with token budgets
- ✅ Choose appropriate workflows
- ✅ Optimize prompt length
- **Target**: <25,000 tokens per session

### Advanced Level (Month 2+)
- ✅ Strategic context management
- ✅ Workflow chaining optimization
- ✅ Selective context restoration
- **Target**: <20,000 tokens per session

---

## 🔧 Tools and Scripts

### Health Check Script
```bash
# Check token efficiency
bash scripts/check_config_health.sh

# Windows version
powershell scripts/powershell/check_config_health.ps1
```

**Checks:**
- Average tokens per session
- Context reset frequency
- Workflow efficiency
- Token usage trends

### Manual Tracking
```bash
# Create usage log
echo "$(date): $(claude cost)" >> ~/claude_usage.log

# Analyze patterns
grep "Session" ~/claude_usage.log | awk '{sum+=$3; count++} END {print sum/count}'
```

---

## 🚨 Common Token Waste Patterns

### 1. Context Bloat
**Problem**: Never resetting context  
**Cost**: 2x-3x token usage  
**Solution**: Reset every 5-7 prompts

### 2. Workflow Overkill
**Problem**: Using complex workflows for simple tasks  
**Cost**: 2x token usage  
**Solution**: Match workflow to task complexity

### 3. Prompt Rambling
**Problem**: Long, unfocused prompts  
**Cost**: 500+ tokens per prompt  
**Solution**: Structured, concise prompts

### 4. Response Overload
**Problem**: Requesting unnecessarily detailed responses  
**Cost**: 1,000+ tokens per response  
**Solution**: Specify output format and scope

---

## 📚 Related Documentation

- **[Getting Started](GETTING_STARTED.md)** - Complete setup guide
- **[Configuration](CONFIGURATION.md)** - Best practices and settings
- **[Aliases](ALIASES.md)** - Productivity shortcuts
- **[Success Guide](SUCCESS_GUIDE.md)** - Best practices and metrics

---

**Next Guide**: [Success Guide](SUCCESS_GUIDE.md) →