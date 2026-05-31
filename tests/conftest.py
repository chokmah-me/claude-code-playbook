"""Shared fixtures and helpers for v4.4.0 test suites."""
import json
import os
import re
import shutil
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
FIXTURES_DIR = Path(__file__).parent / "fixtures"

# Keys the v4.4.0 hardened settings.json template is allowed to have.
# Mirrors the whitelist in check_config_health.sh Section 4.
EXPECTED_SETTINGS_KEYS = {
    "allowedTools",
    "allowedCommands",
    "permissions",
    "mcpServers",
    "contextManagement",
    "_security_note",
    "env",
    "hooks",
}

_MINIMAL_CLAUDE_MD = """\
# Project Config

## Budget
Token target: keep CLAUDE.md under 500 tokens.

## Validation Commands
- Test: npm test
- Lint: npm run lint
- Type check: npm run type-check

## Key Commands
- Build: npm run build
- Dev: npm run dev
- Start: npm start

## Workflow
1. Check out a branch
2. Make changes
3. Run validation
4. Commit with descriptive message

## Error Handling
- Stop on TypeScript errors
- Fix failing tests before proceeding
- Ask for guidance if unsure

## Notes
- Keep atomic commits
- Document non-obvious decisions
- Review diffs before committing
"""

_MINIMAL_GITIGNORE = """\
node_modules/
dist/
.env
.claude/CLAUDE.local.md
REFACTOR_PROGRESS.md
"""

_MINIMAL_SKILL_MD = "# Refactoring Skill\nRoutes refactoring workflows.\n"


@pytest.fixture
def project_dir(tmp_path):
    """Minimal valid project directory — passes all validate_config.py checks with zero errors."""
    (tmp_path / "CLAUDE.md").write_text(_MINIMAL_CLAUDE_MD, encoding="utf-8")
    (tmp_path / ".gitignore").write_text(_MINIMAL_GITIGNORE, encoding="utf-8")
    skills = tmp_path / ".claude" / "skills" / "refactoring"
    skills.mkdir(parents=True)
    (skills / "SKILL.md").write_text(_MINIMAL_SKILL_MD, encoding="utf-8")
    return tmp_path


@contextmanager
def in_dir(path):
    """Temporarily change the working directory (ConfigValidator uses relative paths)."""
    old = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)


def make_settings(
    project_dir,
    *,
    extra_keys=None,
    deny=None,
    commands=None,
    no_permissions=False,
):
    """Write .claude/settings.json and return its Path."""
    claude_dir = Path(project_dir) / ".claude"
    claude_dir.mkdir(parents=True, exist_ok=True)
    cfg = {
        "allowedTools": ["Edit", "Write", "Bash"],
        "allowedCommands": (
            commands
            if commands is not None
            else ["git status", "npm test", "npm run lint"]
        ),
        "_security_note": "Inspect after supply chain incident.",
    }
    if not no_permissions:
        cfg["permissions"] = {
            "deny": (
                deny
                if deny is not None
                else [
                    "Read(node_modules/**)",
                    "Read(dist/**)",
                    "Read(build/**)",
                    "Read(.env)",
                    "Read(.env.*)",
                    "Read(*.lock)",
                    "Read(__pycache__/**)",
                    "Read(*.min.js)",
                    "Read(*.min.css)",
                    "Read(.next/**)",
                ]
            )
        }
    if extra_keys:
        cfg.update(extra_keys)
    path = claude_dir / "settings.json"
    path.write_text(json.dumps(cfg, indent=2), encoding="utf-8")
    return path


def make_rule_file(
    rules_dir,
    filename,
    *,
    with_paths=True,
    paths_value=None,
    broken_frontmatter=False,
):
    """Create a .claude/rules/*.md file with or without paths: frontmatter."""
    rules_dir = Path(rules_dir)
    rules_dir.mkdir(parents=True, exist_ok=True)
    if broken_frontmatter:
        content = "---\ninvalid: [yaml: content\n---\nRule body.\n"
    elif with_paths:
        paths = paths_value or ["src/api/**/*.ts"]
        paths_yaml = "\n".join(f'  - "{p}"' for p in paths)
        content = f"---\npaths:\n{paths_yaml}\n---\nRule body.\n"
    else:
        content = "---\n# global rule — no paths: frontmatter\n---\nRule body.\n"
    (rules_dir / filename).write_text(content, encoding="utf-8")


def check_settings_security(settings_path):
    """
    Return frozenset of unexpected top-level keys.

    Mirrors the inline Python snippet used by check_config_health.sh Section 4
    to detect Mini Shai-Hulud worm persistence entries.
    """
    with open(settings_path, encoding="utf-8") as f:
        cfg = json.load(f)
    return frozenset(cfg.keys()) - EXPECTED_SETTINGS_KEYS


def count_unscoped_rules(rules_dir):
    """
    Return (total_count, unscoped_count).

    Mirrors bash logic:
        scoped=$(grep -rl "^paths:" .claude/rules | wc -l)
        unscoped=$((total - scoped))
    """
    rules_dir = Path(rules_dir)
    rule_files = list(rules_dir.glob("*.md"))
    scoped = [
        f
        for f in rule_files
        if re.search(r"^paths:", f.read_text(encoding="utf-8"), re.MULTILINE)
    ]
    return len(rule_files), len(rule_files) - len(scoped)


def has_bash():
    return shutil.which("bash") is not None


bash_required = pytest.mark.skipif(
    sys.platform == "win32" and not has_bash(),
    reason="bash not available — bash integration tests skipped on this Windows system",
)


@pytest.fixture
def git_project_dir(project_dir):
    """project_dir with a git repo initialized.

    Required for bash integration tests: check_config_health.sh Section 9
    calls `git rev-parse --git-dir` and records an error if no repo is found,
    which would cause every bash test to exit non-zero.
    """
    subprocess.run(
        ["git", "init", "-q", str(project_dir)],
        check=True,
        capture_output=True,
    )
    return project_dir


def run_validate_config(project_dir):
    """Run validate_config.py in project_dir with UTF-8 I/O, return CompletedProcess."""
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "validate_config.py")],
        cwd=str(project_dir),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        env=env,
    )


def run_health_check(project_dir, *, extra_env=None):
    """Run check_config_health.sh in project_dir with UTF-8 I/O, return CompletedProcess.

    Skips the test if bash is not available on this system.

    On Windows, Git Bash inherits a PATH where Windows find.exe (System32) shadows
    GNU find, breaking the -mindepth/-maxdepth/-type d arguments used in the script.
    We prepend /usr/bin to PATH inside the bash -c invocation to fix this.
    """
    if shutil.which("bash") is None:
        pytest.skip("bash not available on this system")
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
    # Use forward-slash path so bash can resolve it on Windows and Unix alike
    script_posix = str(SCRIPTS_DIR / "check_config_health.sh").replace("\\", "/")
    return subprocess.run(
        ["bash", "-c", f"export PATH=/usr/bin:$PATH; bash '{script_posix}'"],
        cwd=str(project_dir),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        env=env,
    )
