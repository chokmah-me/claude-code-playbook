# 📊 Token Economics

**Complete guide to optimizing token usage and managing Claude Pro limits effectively.**

---

## 💰 Claude Pro Optimization

### Understanding Your Limits
- **Prompts**: 10-40 prompts per 5-hour window
- **Tokens**: ~44,000 tokens total capacity
- **Example Session**: 22K tokens (50% of budget)

**Token Budget Allocation:**
```
Total Capacity: 44,000 tokens
├── System Context: ~8,000 tokens (18%)
├── User Input: ~6,000 tokens (14%)
├── Assistant Response: ~12,000 tokens (27%)
└── Reserve: ~18,000 tokens (41%)
```

### Token Efficiency Targets
- **Target per session**: <25,000 tokens
- **Target per prompt**: <2,000 tokens
- **Context reset trigger**: >30,000 tokens

---

## ⚡ Workflow Costs

### Refactoring Workflows
| Workflow | Token Cost | Use Case | Frequency |
|----------|------------|----------|-----------|
| `triage` | 2,000 tokens | Initial codebase analysis | Once per session |
| `qnew` | 2,000 tokens | Start new refactoring | Once per session |
| `qplan` | 3,000 tokens | Create refactoring plan | 2-3 times per session |
| `extract` | 5,000 tokens | Extract functions/methods | 3-5 times per session |
| `modernize` | 4,000 tokens | Update code patterns | 2-3 times per session |
| `qcode` | 8-12,000 tokens | Generate refactored code | 1-2 times per session |
| `catchup` | 1-2,000 tokens | Restore context | Every 5-7 prompts |

### Python Scientific Computing
| Workflow | Token Cost | Use Case |
|----------|------------|----------|
| Vectorization review | 3,000 tokens | Optimize array operations |
| Type hint analysis | 2,000 tokens | Add type annotations |
| Performance profiling | 4,000 tokens | Identify bottlenecks |
| Parallel processing | 5,000 tokens | Optimize for multiprocessing |

---

## 🔄 Session Protocol

### Every 5-7 Prompts (Recommended)
```bash
/cost                              # Check current usage
/clear                             # Reset conversation context
claude skills refactoring catchup  # Restore essential context
```

**Why this protocol works:**
- Prevents context degradation
- Maintains token efficiency
- Preserves important project context
- Resets accumulated noise

### Session Budget Planning
```
Session Budget: 25,000 tokens
├── Setup (triage + qnew): 4,000 tokens (16%)
├── Planning (qplan × 2): 6,000 tokens (24%)
├── Implementation (qcode × 1): 10,000 tokens (40%)
├── Refinement (extract × 2): 4,000 tokens (16%)
└── Buffer: 1,000 tokens (4%)
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