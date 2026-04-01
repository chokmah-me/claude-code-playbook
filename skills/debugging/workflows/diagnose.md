---
name: diagnose
description: "Structured root-cause analysis: reproduce, isolate, hypothesize, verify, fix"
---

# Root-Cause Diagnosis

Systematic bug diagnosis that avoids guess-and-check loops.

## Purpose

Use this workflow when:
- A test fails and the cause isn't obvious
- Runtime error or unexpected behavior reported
- A fix attempt didn't work and you need to step back

## Step 1: Reproduce

Confirm the failure is real and repeatable.

**Actions:**
```
1. Run the failing test or reproduce the error:
   - npm run test:unit (or equivalent)
   - Note the EXACT error message, stack trace, and file:line
2. If no test exists, create a minimal reproduction:
   - Write a test that captures the expected vs actual behavior
   - Confirm it fails consistently
3. Record the reproduction command for later verification
```

**Output:** Exact error, file:line, reproduction command

## Step 2: Isolate

Narrow down where the bug lives.

**Actions:**
```
1. Read the stack trace bottom-up — find the FIRST frame in your code
2. Use Explore agent to trace the call chain:

   Agent(subagent_type=Explore):
   "Trace all callers of [function] in [file]. Show the call chain
    from entry point to the failing line. Include parameter types
    and any transformations applied to the data."

3. Check recent changes to the failing file:
   - git log --oneline -10 [file]
   - git diff HEAD~5 [file]

4. Identify the boundary: is the bug in YOUR code or a dependency?
```

**Output:** Specific function and line range where behavior diverges from expectation

## Step 3: Hypothesize

Form a testable theory about the cause.

**Actions:**
```
1. Read the isolated code section carefully (Read tool, specific lines)
2. Ask: What assumption does this code make that could be wrong?
   Common root causes:
   - Wrong type / null where unexpected
   - Off-by-one or boundary condition
   - Stale state / race condition
   - Missing error handling at a boundary
   - Dependency behavior changed
3. State your hypothesis in ONE sentence:
   "The bug occurs because [X] assumes [Y] but [Z] is actually true."
```

**Output:** One-sentence hypothesis

## Step 4: Verify

Prove or disprove the hypothesis before writing any fix.

**Actions:**
```
1. Add a targeted log/assertion at the suspected location
2. Re-run the reproduction command
3. Does the output confirm your hypothesis?
   - YES → proceed to Step 5
   - NO → return to Step 2 with new information, refine isolation
4. If stuck after 2 hypothesis cycles, expand scope:
   - Check if the bug is environmental (OS, Node version, config)
   - Check if it's a known issue: grep for the error message in issues/docs
```

**Output:** Confirmed root cause with evidence

## Step 5: Fix & Prevent

Apply the minimal fix and add a regression test.

**Actions:**
```
1. Write the SMALLEST change that fixes the root cause
   - Do not refactor surrounding code
   - Do not add unrelated improvements
2. Run the reproduction command — confirm it passes
3. Run the full test suite — confirm no regressions
4. If no regression test existed, add one:
   - Test should fail WITHOUT your fix (verify by reverting mentally)
   - Test should pass WITH your fix
5. Commit with clear message:
   "fix: [what was wrong] — [root cause]"
```

**Output:** Fix applied, tests green, regression test added

## Anti-Patterns

❌ Changing code before understanding the cause
❌ Adding try/catch to suppress errors instead of fixing them
❌ "Shotgun debugging" — changing multiple things at once
❌ Skipping reproduction ("I think I know what it is")

✅ Always reproduce first
✅ One hypothesis at a time
✅ Minimal fix, maximal understanding
