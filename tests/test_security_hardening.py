"""
Tests for v4.4.0 Feature 3: Security Hardening.

Covers two independent defences:

1. settings.json key whitelist — detects Mini Shai-Hulud worm persistence.
   The `check_settings_security` helper in conftest.py mirrors the inline
   Python snippet inside check_config_health.sh Section 4.

2. Dangerous-command detection — validate_config.py errors on allowedCommands
   entries that match known destructive patterns.
"""
import json

import pytest

from conftest import (
    FIXTURES_DIR,
    bash_required,
    check_settings_security,
    in_dir,
    make_settings,
    run_health_check,
)
from validate_config import ConfigValidator


# ── Positive tests: key-whitelist helper ───────────────────────────────────


class TestSettingsKeyWhitelistPositive:
    def test_clean_settings_no_unexpected_keys(self, tmp_path):
        """settings.json with only expected keys → empty unexpected-key set."""
        settings = tmp_path / "settings.json"
        settings.write_text(
            (FIXTURES_DIR / "valid_settings.json").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        assert check_settings_security(settings) == frozenset()

    def test_security_note_key_is_expected(self, tmp_path):
        """_security_note is in the allowed-key whitelist — must NOT be flagged."""
        settings = tmp_path / "settings.json"
        settings.write_text(
            json.dumps({"_security_note": "hardened config", "permissions": {"deny": []}}),
            encoding="utf-8",
        )
        assert "_security_note" not in check_settings_security(settings)

    def test_all_eight_expected_keys_accepted(self, tmp_path):
        """All eight whitelisted keys together → no unexpected flags."""
        cfg = {
            "allowedTools": [],
            "allowedCommands": [],
            "permissions": {"deny": []},
            "mcpServers": {},
            "contextManagement": {},
            "_security_note": "ok",
            "env": {},
            "hooks": {},
        }
        settings = tmp_path / "settings.json"
        settings.write_text(json.dumps(cfg), encoding="utf-8")
        assert check_settings_security(settings) == frozenset()


# ── Negative tests: key-whitelist helper ──────────────────────────────────


class TestSettingsKeyWhitelistNegative:
    def test_worm_persistence_key_detected(self, tmp_path):
        """settings.json with worm-inserted 'update_check' key → flagged as unexpected."""
        settings = tmp_path / "settings.json"
        settings.write_text(
            (FIXTURES_DIR / "compromised_settings.json").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        unexpected = check_settings_security(settings)
        assert "update_check" in unexpected

    def test_multiple_worm_keys_all_detected(self, tmp_path):
        """settings.json with three worm-inserted keys → all three flagged."""
        cfg = {
            "allowedTools": ["Edit"],
            "update_check": {"url": "https://c2.example.com"},
            "telemetry_endpoint": "https://c2.example.com/beacon",
            "auto_updater": {"enabled": True},
        }
        settings = tmp_path / "settings.json"
        settings.write_text(json.dumps(cfg), encoding="utf-8")
        unexpected = check_settings_security(settings)
        assert {"update_check", "telemetry_endpoint", "auto_updater"}.issubset(unexpected)

    def test_single_unexpected_key_not_worm_shaped(self, tmp_path):
        """Any key outside the whitelist is flagged, not just worm-shaped ones."""
        cfg = {"allowedTools": ["Edit"], "debug_mode": True}
        settings = tmp_path / "settings.json"
        settings.write_text(json.dumps(cfg), encoding="utf-8")
        assert "debug_mode" in check_settings_security(settings)


# ── Positive tests: ConfigValidator dangerous-command detection ────────────


class TestDangerousCommandsPositive:
    def test_safe_commands_no_error(self, project_dir):
        """allowedCommands with only safe entries → no errors."""
        make_settings(project_dir, commands=["git status", "npm test", "pytest"])
        with in_dir(project_dir):
            v = ConfigValidator()
            v.validate_settings_json()
        assert len(v.errors) == 0

    def test_invalid_json_raises_error(self, project_dir):
        """Malformed settings.json → ConfigValidator records an error."""
        (project_dir / ".claude").mkdir(exist_ok=True)
        (project_dir / ".claude" / "settings.json").write_text(
            "{broken json", encoding="utf-8"
        )
        with in_dir(project_dir):
            v = ConfigValidator()
            v.validate_settings_json()
        assert any("invalid json" in e.lower() for e in v.errors)


# ── Negative tests: ConfigValidator dangerous-command detection ────────────


class TestDangerousCommandsNegative:
    def test_rm_rf_in_allowed_commands_errors(self, project_dir):
        """allowedCommands containing 'rm -rf' → error 'Dangerous command'."""
        make_settings(project_dir, commands=["git status", "rm -rf /tmp/test"])
        with in_dir(project_dir):
            v = ConfigValidator()
            v.validate_settings_json()
        assert any("dangerous command" in e.lower() for e in v.errors)

    def test_sudo_in_allowed_commands_errors(self, project_dir):
        """allowedCommands containing 'sudo' → error 'Dangerous command'."""
        make_settings(project_dir, commands=["git status", "sudo systemctl stop app"])
        with in_dir(project_dir):
            v = ConfigValidator()
            v.validate_settings_json()
        assert any("dangerous command" in e.lower() for e in v.errors)

    def test_chmod_777_in_allowed_commands_errors(self, project_dir):
        """allowedCommands containing 'chmod 777' → error 'Dangerous command'."""
        make_settings(project_dir, commands=["git status", "chmod 777 /etc/passwd"])
        with in_dir(project_dir):
            v = ConfigValidator()
            v.validate_settings_json()
        assert any("dangerous command" in e.lower() for e in v.errors)

    def test_no_allowed_tools_warns(self, project_dir):
        """settings.json without 'allowedTools' key → warning."""
        (project_dir / ".claude").mkdir(exist_ok=True)
        (project_dir / ".claude" / "settings.json").write_text(
            json.dumps({"allowedCommands": ["git status"]}), encoding="utf-8"
        )
        with in_dir(project_dir):
            v = ConfigValidator()
            v.validate_settings_json()
        assert any("allowedtools" in w.lower() for w in v.warnings)


# ── Bash integration tests ─────────────────────────────────────────────────


@bash_required
class TestSecurityHardeningBashIntegration:
    def test_clean_settings_section4_passes(self, git_project_dir):
        """Clean settings.json → Section 4 reports keys look clean."""
        make_settings(git_project_dir)
        result = run_health_check(git_project_dir)
        assert "keys look clean" in result.stdout

    def test_worm_key_section4_errors(self, git_project_dir):
        """Worm-inserted key → Section 4 reports UNEXPECTED key and exits non-zero."""
        make_settings(git_project_dir, extra_keys={"auto_updater": {"enabled": True}})
        result = run_health_check(git_project_dir)
        assert "UNEXPECTED" in result.stdout
        assert result.returncode == 1

    def test_settings_local_json_shows_info(self, git_project_dir):
        """settings.local.json present → Section 4 emits an info message."""
        make_settings(git_project_dir)
        (git_project_dir / ".claude" / "settings.local.json").write_text(
            json.dumps({"allowedTools": ["Edit"]}), encoding="utf-8"
        )
        result = run_health_check(git_project_dir)
        assert "settings.local.json" in result.stdout

    def test_missing_permissions_deny_warns(self, git_project_dir):
        """settings.json without permissions.deny → Section 3 emits the expected warning text."""
        make_settings(git_project_dir, deny=[])
        result = run_health_check(git_project_dir)
        assert "No permissions.deny" in result.stdout
        # Note: returncode not checked — bc absence causes an unrelated Section 1
        # error that would make returncode == 1 regardless of the deny condition.
