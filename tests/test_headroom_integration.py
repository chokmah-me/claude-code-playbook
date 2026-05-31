"""
Tests for v4.4.0 Feature 4: Headroom Output Compression integration.

Key contract: Headroom is *optional*.  Its absence must never cause
validate_config.py to fail or check_config_health.sh to exit non-zero.

Python tests confirm validate_config.py has no headroom gate.
Bash integration tests (skipped on Windows without bash) confirm the
health-check script emits info — not error — when headroom is absent,
and emits success when a headroom binary is present on PATH.
"""
import os
import stat

import pytest

from conftest import (
    SCRIPTS_DIR,
    bash_required,
    run_health_check,
    run_validate_config,
)


# ── Positive tests ─────────────────────────────────────────────────────────


class TestHeadroomPositive:
    def test_validate_config_never_checks_headroom(self):
        """validate_config.py source must not contain any headroom gate."""
        src = (SCRIPTS_DIR / "validate_config.py").read_text(encoding="utf-8")
        assert "headroom" not in src.lower()

    def test_validate_config_exits_0_without_headroom(self, project_dir):
        """validate_config.py exits 0 regardless of whether headroom is installed."""
        result = run_validate_config(project_dir)
        assert result.returncode == 0, result.stdout + result.stderr

    @bash_required
    def test_health_check_headroom_installed_shows_success(self, git_project_dir, tmp_path):
        """Fake headroom binary on PATH → Section 7 reports 'Headroom installed'."""
        bin_dir = tmp_path / "fake_bin"
        bin_dir.mkdir()
        fake_headroom = bin_dir / "headroom"
        fake_headroom.write_text(
            "#!/bin/bash\n"
            'if [ "$1" = "--version" ]; then echo "headroom-ai 0.9.1"; fi\n'
            "exit 0\n",
            encoding="utf-8",
        )
        # Make executable on POSIX; harmless on Windows (bash reads the shebang)
        fake_headroom.chmod(
            fake_headroom.stat().st_mode
            | stat.S_IEXEC
            | stat.S_IXGRP
            | stat.S_IXOTH
        )

        result = run_health_check(
            git_project_dir,
            extra_env={"PATH": f"{bin_dir}:{os.environ.get('PATH', '')}"},
        )
        assert "Headroom installed" in result.stdout


# ── Negative tests ─────────────────────────────────────────────────────────


class TestHeadroomNegative:
    @bash_required
    def test_health_check_headroom_absent_is_info_not_error(self, git_project_dir):
        """No headroom on PATH → Section 7 emits info (not an error line).

        We verify the Section 7 info text rather than returncode because bc may not
        be available, causing an unrelated Section 1 error that inflates returncode.
        The key contract is that headroom absence is reported as ℹ️ info, not ❌ error.
        """
        result = run_health_check(git_project_dir)
        assert "not installed" in result.stdout.lower()
        # "not installed" must NOT appear on an error line (❌ prefix)
        for line in result.stdout.splitlines():
            if "not installed" in line.lower():
                assert "❌" not in line, f"Headroom absence was flagged as error: {line}"

    @bash_required
    def test_health_check_headroom_absent_shows_install_hint(self, git_project_dir):
        """No headroom on PATH → health check output includes pip install hint."""
        result = run_health_check(git_project_dir)
        assert "headroom-ai" in result.stdout
