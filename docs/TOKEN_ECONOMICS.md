# 📊 Token Economics

**Three complementary layers: don't load it, compress it, cache it.**

---

## The Token Floor Problem

Before you type a single character, Claude Code has already consumed **20,000–30,000 tokens**. A GitHub issue (#52979 in the Claude Code repo) confirmed a simple "hi" prompt consumed ~31,000 tokens. That floor is what loads at session start:

- System prompt and Claude Code internals
- `CLAUDE.md` and any imported files (loaded in full, every turn)
- `.claude/rules/` files without `paths:` frontmatter (also in full, every turn)
- MCP server tool schemas — 400–800 tokens per connected server; heavy setups add 10,000–20,000 tokens
- Memory files and skill descriptions

This is your highest-leverage optimization surface. Every token you cut here is cut on every single turn, not just once.

Run `/context` at any point in a session for a live breakdown by category. Run `/memory` to see exactly which files loaded at startup.

---

## Three Layers, Three Different Problems

Token optimization has three independent levers. They address different stages of the request lifecycle and don't sum into one number.

| Layer | Technique | Measured reduction |
|-------|-----------|-------------------|
| **1. Don't load it** | Trim CLAUDE.md, `.claudeignore`, path-scoped rules | 41–92% of session startup overhead |
| **2. Compress before send** | Headroom (tool outputs, logs, RAG, files) | 47–92% of dynamic context |
| **3. Cache what's stable** | CacheAligner / prompt caching (API track) | 70–90% of repeated content cost |

CLI subscription users pay with response quality, not money; bloated context dilutes Claude's attention and produces generic answers. API users pay per token. Both audiences benefit from all three layers.

---

## Layer 1: Don't Load It

### CLAUDE.md — under 500 tokens

Every Claude Code session loads `CLAUDE.md` into **every request**. It is the most expensive single file you control, paid on every turn, forever. Benchmarks comparing a 3,847-token CLAUDE.md with a 312-token version stripped to only what Claude cannot infer from the code found **91.9% context reduction** with no quality regression (source: token-optimizer benchmark, hamzafarooq/token-optimizer).

Target: under 500 tokens. Anthropic's official guidance is under 200 lines. Some teams run at 60.

**Cut anything Claude already knows from training:** framework routing conventions, standard syntax, generic best-practice advice, team rosters, meeting schedules, FAQs Claude can't act on. A useful test: would this genuinely surprise an experienced developer new to the repo? If not, remove it.

**Keep:** non-obvious build and test commands, architecture decisions that go against framework defaults, project-specific constraints and gotchas.

Three things most people don't know:

- HTML comments (`<!-- internal note -->`) are stripped before injection. They cost zero tokens. Use them for notes to teammates, rationale, anything humans need that Claude doesn't.
- `@path/to/file` imports are organizational only. All imported files still load at session start. Splitting CLAUDE.md across files saves no tokens.
- Edits to CLAUDE.md during a session don't apply until the next restart or `/compact`. Claude reads it once at startup.

If you run `headroom learn` (see Layer 2), it may auto-append corrections to CLAUDE.md from failed sessions. Review those entries before committing.

### .claudeignore vs permissions.deny — use both

`.claudeignore` is **advisory**. It signals to Claude that certain files are not relevant. Claude can still read ignored files if it decides they are necessary (documented in GitHub issues #36163, #51105).

`permissions.deny` in `.claude/settings.json` is **enforced**. It blocks the Read tool for those paths entirely. Claude cannot read them regardless of what it decides.

```json
{
  "permissions": {
    "deny": ["Read(node_modules/**)", "Read(dist/**)", "Read(*.lock)"]
  }
}
```

The 85.5% context reduction benchmark for `.claudeignore` was measured on the signal layer. Teams with strict context discipline add `permissions.deny` on top.

Minimum `.claudeignore` for any project:

```
node_modules/
dist/
build/
.next/
__pycache__/
*.pyc
*.lock
package-lock.json
yarn.lock
poetry.lock
coverage/
*.generated.*
*.min.js
*.min.css
```

Commit this to version control. Every team member gets the same context discipline automatically.

### Path-scoped rules in .claude/rules/

`.claude/rules/` lets you place rules files that load selectively. Rules **without** `paths:` frontmatter in the file header load at session start like a second CLAUDE.md with no savings. Rules **with** `paths:` frontmatter load only when Claude first touches a file matching that pattern, at zero cost until triggered.

```yaml
---
paths:
  - "src/api/**/*.ts"
---
# API Layer Rules
All endpoints must validate input with Zod schemas.
Response errors must use the shared ApiError class.
Never return raw Prisma errors to the client.
```

This rule costs nothing during frontend work, database work, or test writing. It enters context only when Claude touches a file in `src/api/`. Path-scoped rules are invisible until needed.

One documented case (Zenn, 2025) reduced always-loaded rule overhead from 1,358 lines to 807 lines (**41% reduction**) by converting procedure-heavy rule files into Skills and scoping domain-specific rules to their directories.

### MCP server overhead

Each connected MCP server loads its tool schema into every request by default. Heavy setups can add 10,000–20,000 tokens of silent per-session overhead.

`ENABLE_TOOL_SEARCH=true` in Claude Code settings defers MCP tool schemas until actually needed, recovering 50,000–70,000 tokens in heavy multi-server setups.

**Do not connect or disconnect MCP servers mid-session.** Doing so wipes your entire prompt cache. Make changes at session boundaries.

---

## Layer 2: Compress Before Send

Even after optimizing startup load, dynamic context accumulates fast: tool outputs, test logs, file reads, search results. A single failing test suite can dump 10,000 lines into context. A grep over a large codebase can return thousands of matches. This content enters the window before Claude processes it.

**[Headroom](https://github.com/chopratejas/headroom)** (Apache 2.0, 2.5k+ stars) compresses tool outputs, logs, RAG chunks, and files before they reach the LLM. It runs entirely locally; your data never leaves. Benchmarks on real agent workloads:

| Workload | Before | After | Reduction |
|----------|--------|-------|-----------|
| Code search (100 results) | 17,765 | 1,408 | **92%** |
| SRE incident debugging | 65,694 | 5,118 | **92%** |
| GitHub issue triage | 54,174 | 14,761 | **73%** |
| Codebase exploration | 78,502 | 41,254 | **47%** |

Accuracy is preserved: GSM8K ±0.000 delta, BFCL tool calls 97% at 32% compression.

**For Claude Code users, one command wraps the entire session:**

```bash
pip install "headroom-ai[all]"
headroom wrap claude
```

All tool outputs are compressed before re-entering context. No code changes required.

**headroom learn** mines failed sessions and writes corrections to your CLAUDE.md, automating part of the `catchup` workflow:

```bash
headroom learn
```

Review generated entries before committing; they are machine-written and may need token trimming.

**Headroom as an MCP server** exposes `headroom_compress`, `headroom_retrieve`, and `headroom_stats` to any MCP client:

```bash
headroom mcp install
```

This is the one MCP server worth adding even when disabling others, because it reduces the token cost of every other MCP tool's output. It also integrates CacheAligner for Layer 3 benefits.

**Six compression algorithms applied by content type:**

- **SmartCrusher** — JSON arrays, nested objects, tool call results
- **CodeCompressor** — AST-aware for Python, JS, Go, Rust, Java, C++
- **Kompress-base** — HuggingFace prose model trained on agentic traces
- **CacheAligner** — stabilizes prefixes so provider KV caches hit (Layer 3 synergy)
- **IntelligentContext** — score-based context fitting with learned importance
- **CCR (reversible)** — originals stored locally; LLM retrieves on demand via `headroom_retrieve`

**Compared to alternatives:**

| Tool | Scope | Local | Reversible |
|------|-------|-------|------------|
| Headroom | All context: tools, logs, RAG, files, history | Yes | Yes |
| RTK | CLI command outputs only | Yes | No |
| lean-ctx | CLI, MCP tools, editor rules | Yes | No |

Headroom ships RTK as an included binary for shell-output rewriting; both tools compose cleanly.

---

## Layer 3: Cache What's Stable (API Users)

For teams using Claude via the API, prompt caching cuts the cost of repeated content by 90%: cache reads cost $0.30/M vs $3.00/M for standard Sonnet 4 input tokens. A team burning 5M input tokens/day: ~$15,000 at standard rates vs ~$3,500 with 80% cache hit rate (~$4M annualized difference).

Most teams enable caching and still see 5–15% savings instead of 70–90%. The gap is structural. Caching only works when prompts are built in a specific way:

- Stable content (system prompt, CLAUDE.md) must appear before dynamic content
- Cache boundaries must be placed deliberately
- Any change to content before a cache boundary invalidates everything after it

Headroom's **CacheAligner** handles prefix stabilization automatically so provider KV caches hit at the rates Anthropic advertises.

For Claude Code CLI users on subscription: prompt caching is handled internally. Layers 1 and 2 are the primary levers.

---

## Workflow Cost Reference

These assume CLAUDE.md is under 500 tokens and `.claudeignore` is in place. Without Layer 1 optimization, every cost increases by your unoptimized startup overhead.

| Workflow | Relative cost | Best use |
|----------|--------------|---------|
| triage | Low (~2K) | Initial analysis, run once |
| qnew | Low (~2K) | Session start |
| qplan | Medium (~3K) | Design phase |
| extract | Medium (~5K) | Single function |
| modernize | Medium (~4K) | Pattern updates |
| qcode | High (~8–12K) | Batch implementation |
| catchup | Low (~1–2K) | Resume from progress file |

---

## Monthly Maintenance

```bash
# Estimate CLAUDE.md token count
python -c "
with open('CLAUDE.md') as f:
    words = len(f.read().split())
print(f'{words} words ≈ {int(words*1.3)} tokens (target: <500)')
"

# Full health check
bash scripts/check_config_health.sh

# If running Headroom
headroom stats
```

---

## Related Documentation

- [Getting Started](GETTING_STARTED.md) — setup
- [Configuration](CONFIGURATION.md) — CLAUDE.md, .claudeignore, rules, MCP, security
- [Agentic Patterns](AGENTIC_PATTERNS.md) — compression, hooks, memory, cross-agent patterns
- [Success Guide](SUCCESS_GUIDE.md) — metrics and learning path
