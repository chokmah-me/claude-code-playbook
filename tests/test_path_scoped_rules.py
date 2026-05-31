"""
Tests for v4.4.0 Feature 2: Path-Scoped Rules.

Rules under .claude/rules/ with a `paths:` YAML frontmatter line load only
when the user edits a matching file.  Rules without `paths:` are "unscoped"
and load every session.  More than 3 unscoped rules triggers a warning.

The `count_unscoped_rules` helper in conftest.py mirrors the bash logic:
    scoped=$(grep -rl "^paths:" .claude/rules | wc -l)
    unscoped=$((total - scoped))
"""
import pytest

from conftest import (
    FIXTURES_DIR,
    bash_required,
    count_unscoped_rules,
    make_rule_file,
    run_health_check,
)


# ── Positive tests ─────────────────────────────────────────────────────────


class TestPathScopedRulesPositive:
    def test_all_rules_scoped_zero_unscoped(self, tmp_path):
        """Three rules, all with `paths:` → 0 unscoped."""
        rules_dir = tmp_path / ".claude" / "rules"
        for i in range(3):
            make_rule_file(rules_dir, f"rule{i}.md", with_paths=True)
        total, unscoped = count_unscoped_rules(rules_dir)
        assert total == 3
        assert unscoped == 0

    def test_one_global_rule_within_threshold(self, tmp_path):
        """1 unscoped global rule + 2 scoped rules → unscoped=1 (≤3 threshold, OK)."""
        rules_dir = tmp_path / ".claude" / "rules"
        make_rule_file(rules_dir, "global.md", with_paths=False)
        make_rule_file(rules_dir, "api.md", with_paths=True)
        make_rule_file(rules_dir, "db.md", with_paths=True)
        _, unscoped = count_unscoped_rules(rules_dir)
        assert unscoped == 1

    def test_three_unscoped_at_boundary(self, tmp_path):
        """Exactly 3 unscoped rules → unscoped=3 (equal to threshold, still OK)."""
        rules_dir = tmp_path / ".claude" / "rules"
        for i in range(3):
            make_rule_file(rules_dir, f"global{i}.md", with_paths=False)
        _, unscoped = count_unscoped_rules(rules_dir)
        assert unscoped == 3

    def test_valid_paths_frontmatter_counted_as_scoped(self, tmp_path):
        """Rule copied from the fixture has `paths:` at line start → scoped."""
        rules_dir = tmp_path / ".claude" / "rules"
        rules_dir.mkdir(parents=True)
        (rules_dir / "api.md").write_text(
            (FIXTURES_DIR / "rule_scoped.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        total, unscoped = count_unscoped_rules(rules_dir)
        assert total == 1
        assert unscoped == 0

    def test_global_fixture_counted_as_unscoped(self, tmp_path):
        """Rule from global fixture has no `paths:` line → unscoped."""
        rules_dir = tmp_path / ".claude" / "rules"
        rules_dir.mkdir(parents=True)
        (rules_dir / "global.md").write_text(
            (FIXTURES_DIR / "rule_global.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        _, unscoped = count_unscoped_rules(rules_dir)
        assert unscoped == 1


# ── Negative tests ─────────────────────────────────────────────────────────


class TestPathScopedRulesNegative:
    def test_four_unscoped_exceeds_threshold(self, tmp_path):
        """Four unscoped rules → unscoped=4 (exceeds the >3 warning threshold)."""
        rules_dir = tmp_path / ".claude" / "rules"
        for i in range(4):
            make_rule_file(rules_dir, f"unscoped{i}.md", with_paths=False)
        _, unscoped = count_unscoped_rules(rules_dir)
        assert unscoped > 3

    def test_rule_with_frontmatter_but_missing_paths_key_is_unscoped(self, tmp_path):
        """Frontmatter block without a `paths:` line → counted as unscoped."""
        rules_dir = tmp_path / ".claude" / "rules"
        rules_dir.mkdir(parents=True)
        # Has frontmatter delimiters but no paths: key
        (rules_dir / "no_paths.md").write_text(
            "---\ntitle: My Rule\ndescription: Important rule\n---\nDo the thing.\n",
            encoding="utf-8",
        )
        total, unscoped = count_unscoped_rules(rules_dir)
        assert unscoped == 1

    def test_broken_frontmatter_counted_as_unscoped(self, tmp_path):
        """Broken YAML frontmatter (no valid `paths:` line) → counted as unscoped."""
        rules_dir = tmp_path / ".claude" / "rules"
        make_rule_file(rules_dir, "broken.md", broken_frontmatter=True)
        _, unscoped = count_unscoped_rules(rules_dir)
        assert unscoped == 1

    def test_paths_in_body_not_at_line_start_is_unscoped(self, tmp_path):
        """'paths:' mid-sentence in rule body does not match '^paths:' → unscoped."""
        rules_dir = tmp_path / ".claude" / "rules"
        rules_dir.mkdir(parents=True)
        (rules_dir / "body_only.md").write_text(
            "---\n# no paths key\n---\nApply to all paths: src/ and lib/.\n",
            encoding="utf-8",
        )
        _, unscoped = count_unscoped_rules(rules_dir)
        assert unscoped == 1


# ── Bash integration tests ─────────────────────────────────────────────────


@bash_required
class TestPathScopedRulesBashIntegration:
    def test_no_rules_dir_is_info_not_error(self, git_project_dir):
        """Missing .claude/rules/ → health check emits the Section 5 info message.

        Note: we check content rather than returncode because bc is not available in
        all Git Bash installs — its absence triggers a false Section 1 error that
        makes returncode non-zero regardless of the rules-dir condition.
        """
        result = run_health_check(git_project_dir)
        # Section 5 emits an info message (path-scoped rules dir is optional)
        assert ".claude/rules/ not found" in result.stdout

    def test_all_scoped_rules_pass_health_check(self, git_project_dir):
        """All rules scoped → health check reports present, no unscoped warning."""
        rules_dir = git_project_dir / ".claude" / "rules"
        make_rule_file(rules_dir, "api.md", with_paths=True)
        make_rule_file(rules_dir, "db.md", with_paths=True)
        result = run_health_check(git_project_dir)
        assert ".claude/rules/ present" in result.stdout
        assert "unscoped rule files load every session" not in result.stdout

    def test_too_many_unscoped_warns_in_health_check(self, git_project_dir):
        """More than 3 unscoped rules → health check emits unscoped-rules warning."""
        rules_dir = git_project_dir / ".claude" / "rules"
        for i in range(4):
            make_rule_file(rules_dir, f"global{i}.md", with_paths=False)
        result = run_health_check(git_project_dir)
        assert "unscoped rule files load every session" in result.stdout
