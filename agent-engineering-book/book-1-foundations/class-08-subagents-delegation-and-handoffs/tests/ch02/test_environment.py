"""Chapter 2 gate test: confirms the Claude Code workspace is set up correctly.

Deterministic and offline — no API key or network required. This is the
"simple verification task" Chapter 2.2 describes: the workspace has the
expected directory structure, .claude/settings.json is valid JSON, and the
Python version meets the book's stated minimum (3.11+).
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

EXPECTED_DIRS = ["config", "src", "data", "outputs", "tests", "evals", ".claude"]


def test_python_version_meets_minimum():
    assert sys.version_info >= (3, 11), (
        f"Python 3.11+ required, found {sys.version_info.major}.{sys.version_info.minor}"
    )


def test_expected_directories_exist():
    missing = [d for d in EXPECTED_DIRS if not (REPO_ROOT / d).is_dir()]
    assert not missing, f"Missing expected directories: {missing}"


def test_claude_settings_is_valid_json():
    settings_path = REPO_ROOT / ".claude" / "settings.json"
    assert settings_path.exists(), ".claude/settings.json is missing"
    json.loads(settings_path.read_text())


def test_claude_settings_denies_secret_reads():
    """.gitignore only controls what's committed — it does nothing to stop
    Claude reading a file during a session. permissions.deny is what
    actually blocks the read, and it needs to exist from Class 2 onward,
    before any real secret exists to accidentally expose."""
    settings = json.loads((REPO_ROOT / ".claude" / "settings.json").read_text())
    deny = settings.get("permissions", {}).get("deny", [])
    assert deny, ".claude/settings.json has no permissions.deny list"

    deny_text = " ".join(deny)
    for pattern in [".env", "secrets"]:
        assert pattern in deny_text, f"permissions.deny doesn't cover {pattern!r}"


def test_claude_md_exists():
    assert (REPO_ROOT / "CLAUDE.md").exists(), "CLAUDE.md is missing at repo root"


def test_can_write_to_outputs_directory():
    probe = REPO_ROOT / "outputs" / ".ch02_write_probe"
    probe.write_text("ok")
    assert probe.read_text() == "ok"
    probe.unlink()
