---
name: glossary
description: "Extract domain-specific terms and project vocabulary from codebase"
---

# Domain Glossary Extraction

Build a vocabulary of project-specific terms from the code itself.

## Purpose

Use this workflow when:
- Domain terms are unfamiliar (finance, biotech, logistics, etc.)
- Codebase uses custom naming that isn't self-explanatory
- Team members use different terms for the same concept
- Onboarding someone from a different domain

## Step 1: Extract Candidate Terms

**Actions:**
```
Launch: Agent(subagent_type=Explore)

Task: Scan the codebase for domain-specific terminology:
1. Read type/interface/class definitions — extract names and field names
   that are domain-specific (not generic programming terms)
2. Read enum values — these often encode domain concepts
3. Check README and docs for capitalized terms or quoted phrases
4. Look at database table/column names if models exist
5. Check comments that explain "what" not "how" — these define terms

Return a raw list of candidate terms with the file where each appears.
Exclude generic programming terms (id, name, config, handler, etc.)
```

## Step 2: Define Terms

For each candidate term:

```
1. Read the code context where the term is used (2-3 usages)
2. Infer the definition from:
   - Type definition / interface fields
   - Comments or docstrings nearby
   - How it's used in business logic
3. Write a 1-sentence definition
4. Note aliases (if the same concept has multiple names)
```

## Step 3: Organize

**Actions:**
```
Group terms by domain area:
- Core domain (the business problem)
- Technical domain (project-specific patterns)
- Acronyms and abbreviations

Sort alphabetically within each group.
```

## Output Format

```markdown
## Glossary: [Project Name]

### Core Domain
| Term | Definition | Source |
|------|-----------|--------|
| Lattice | A graph-based entity relationship model | src/models/lattice.ts |
| Entity | A real-world object tracked in the system | src/types/entity.ts |
| ... | ... | ... |

### Technical Domain
| Term | Definition | Source |
|------|-----------|--------|
| Result monad | Error handling pattern returning Ok/Err | src/utils/result.ts |
| ... | ... | ... |

### Acronyms
| Acronym | Expansion | Context |
|---------|-----------|---------|
| ACP | Agent Communication Protocol | Network layer |
| ... | ... | ... |

### Aliases
| Preferred | Also Known As |
|-----------|---------------|
| Entity | Node, Object, Item |
| ... | ... |
```

## Guidelines

- **Define from code, not assumptions** — if you can't find a definition, mark it as "unclear"
- **Include source file** — so readers can see the term in context
- **Note when terms are overloaded** — same word, different meanings in different modules
- **Keep definitions to one sentence** — link to code for details
