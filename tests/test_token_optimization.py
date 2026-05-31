"""
Tests for v4.4.0 Feature 1: Three-Layer Token Optimization.

Covers Layer 1 (don't-load-it) behaviours:
  - CLAUDE.md line budget enforcement via validate_config.py
  - Anti-pattern detection (style guide, generic advice, missing sections)
  - permissions.deny hard-exclusion count via health check (bash integration)
  - .claudeignore required-entry validation via health check (bash integration)
"""
import pytest

from conftest import (
    FIXTURES_DIR,
    bash_required,
    in_dir,
    make_settings,
    run_health_check,
    run_validate_config,
)
from validate_config import ConfigValidator


# ── Positive tests ─────────────────────────────────────────────────────────


class TestClaudeMdPositive:
    def test_optimal_30_to_50_lines_no_error(self, project_dir):
        """CLAUDE.md with 30–50 lines → no errors from validate_claude_md."""
        with in_dir(project_dir):
            v = ConfigValidator()
            v.validate_claude_md()
        assert len(v.errors) == 0

    def test_has_validation_keywords_no_validation_warning(self, project_dir):
        """CLAUDE.md containing 'test' and 'lint' → no 'Missing validation' warning."""
        content = "\n".join(["# Config"] + ["description"] * 30 + ["Run: npm test", "Lint: npm run lint"])
        (project_dir / "CLAUDE.md").write_text(content, encoding="utf-8")
        with in_dir(project_dir):
            v = ConfigValidator()
            v.validate_claude_md()
        assert not any(
            "validation" in w.lower() and "missing" in w.lower() for w in v.warnings
        )

    def test_token_keyword_suppresses_budget_warning(self, project_dir):
        """CLAUDE.md containing 'token' → no 'Missing budget' warning."""
        lines = ["# Config", "Token target: <500 tokens."] + ["line"] * 29
        (project_dir / "CLAUDE.md").write_text("\n".join(lines), encoding="utf-8")
        with in_dir(project_dir):
            v = ConfigValidator()
            v.validate_claude_md()
        assert not any(
            "budget" in w.lower() and "missing" in w.lower() for w in v.warnings
        )

    def test_valid_project_validate_config_exits_0(self, project_dir):
        """Complete valid project → validate_config.py exits 0."""
        result = run_validate_config(project_dir)
        assert result.returncode == 0, result.stdout + result.stderr


# ── Negative tests ─────────────────────────────────────────────────────────


class TestClaudeMdNegative:
    def test_too_large_over_100_lines_triggers_error(self, project_dir):
        """CLAUDE.md with 150 lines → error 'too large'."""
        (project_dir / "CLAUDE.md").write_text("\n".join(["line"] * 150), encoding="utf-8")
        with in_dir(project_dir):
            v = ConfigValidator()
            v.validate_claude_md()
        assert any("too large" in e.lower() for e in v.errors)

    def test_too_large_claude_md_validate_config_exits_1(self, project_dir):
        """CLAUDE.md with 150 lines → validate_config.py exits 1."""
        (project_dir / "CLAUDE.md").write_text("\n".join(["line"] * 150), encoding="utf-8")
        result = run_validate_config(project_dir)
        assert result.returncode == 1

    def test_style_guide_indentation_warns(self, project_dir):
        """CLAUDE.md containing 'indentation' → style-guide warning."""
        lines = ["# Config"] + ["description"] * 30 + ["Use consistent indentation."]
        (project_dir / "CLAUDE.md").write_text("\n".join(lines), encoding="utf-8")
        with in_dir(project_dir):
            v = ConfigValidator()
            v.validate_claude_md()
        assert any("style guide" in w.lower() for w in v.warnings)

    def test_style_guide_semicolon_warns(self, project_dir):
        """CLAUDE.md containing 'semicolon' → style-guide warning."""
        lines = ["# Config"] + ["description"] * 30 + ["Always use semicolons."]
        (project_dir / "CLAUDE.md").write_text("\n".join(lines), encoding="utf-8")
        with in_dir(project_dir):
            v = ConfigValidator()
            v.validate_claude_md()
        assert any("style guide" in w.lower() for w in v.warnings)

    def test_generic_advice_write_clean_code_warns(self, project_dir):
        """CLAUDE.md containing 'write clean code' → generic-advice warning."""
        lines = ["# Config"] + ["description"] * 30 + ["Always write clean code."]
        (project_dir / "CLAUDE.md").write_text("\n".join(lines), encoding="utf-8")
        with in_dir(project_dir):
            v = ConfigValidator()
            v.validate_claude_md()
        assert any("generic" in w.lower() for w in v.warnings)

    def test_missing_validation_keywords_warns(self, project_dir):
        """CLAUDE.md with no 'test'/'lint'/'validation'/'check' → Missing validation warning."""
        lines = ["# Config", "Budget: token target under 500.", "Build: npm run build"] + ["line"] * 28
        (project_dir / "CLAUDE.md").write_text("\n".join(lines), encoding="utf-8")
        with in_dir(project_dir):
            v = ConfigValidator()
            v.validate_claude_md()
        assert any("validation" in w.lower() for w in v.warnings)


# ── Bash integration tests ─────────────────────────────────────────────────


@bash_required
class TestTokenOptimizationBashIntegration:
    def test_claudeignore_with_all_required_entries_passes(self, git_project_dir):
        """.claudeignore containing all required entries → health check reports present."""
        (git_project_dir / ".claudeignore").write_text(
            (FIXTURES_DIR / "valid_claudeignore.txt").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        result = run_health_check(git_project_dir)
        assert ".claudeignore present" in result.stdout

    def test_missing_claudeignore_warns(self, git_project_dir):
        """No .claudeignore → health check warns (Section 2 output present)."""
        result = run_health_check(git_project_dir)
        assert ".claudeignore not found" in result.stdout
        # Note: returncode may be non-zero on systems without bc (Section 1 bc fallback
        # produces "~N" which makes all numeric comparisons fail, triggering a false error).

    def test_permissions_deny_ten_entries_success(self, git_project_dir):
        """10 permissions.deny entries → health check reports configured."""
        make_settings(git_project_dir)
        result = run_health_check(git_project_dir)
        assert "permissions.deny configured" in result.stdout

    def test_permissions_deny_empty_warns(self, git_project_dir):
        """Empty permissions.deny → health check reports the expected warning text."""
        make_settings(git_project_dir, deny=[])
        result = run_health_check(git_project_dir)
        assert "No permissions.deny" in result.stdout
