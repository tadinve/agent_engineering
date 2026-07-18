"""Chapter 3 gate test: CLAUDE.md and the four business-context config files
exist and are well-formed. Deterministic and offline.

This does not judge whether CLAUDE.md's *content* is good instruction
architecture — that's a human/reviewer judgment (Ch. 3.2). It only checks
the structural contract Chapter 3 requires: the file exists, references the
config files it depends on, and every config file it points to is valid YAML.
"""

import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = REPO_ROOT / "config"

REQUIRED_CONFIG_FILES = [
    "icp.yaml",
    "offering.yaml",
    "voice.yaml",
    "evidence-policy.yaml",
]


def test_claude_md_exists_and_is_nonempty():
    claude_md = REPO_ROOT / "CLAUDE.md"
    assert claude_md.exists(), "CLAUDE.md is missing"
    content = claude_md.read_text()
    assert len(content.strip()) > 200, "CLAUDE.md is still a placeholder"


def test_claude_md_references_all_config_files():
    content = (REPO_ROOT / "CLAUDE.md").read_text()
    missing = [f for f in REQUIRED_CONFIG_FILES if f not in content]
    assert not missing, f"CLAUDE.md does not reference: {missing}"


def test_all_config_files_exist():
    missing = [f for f in REQUIRED_CONFIG_FILES if not (CONFIG_DIR / f).exists()]
    assert not missing, f"Missing config files: {missing}"


def test_all_config_files_are_valid_yaml():
    for filename in REQUIRED_CONFIG_FILES:
        path = CONFIG_DIR / filename
        data = yaml.safe_load(path.read_text())
        assert isinstance(data, dict), f"{filename} did not parse to a mapping"


def test_evidence_policy_defines_required_fields():
    data = yaml.safe_load((CONFIG_DIR / "evidence-policy.yaml").read_text())
    assert "required_fields_per_claim" in data
    for field in ["source", "source_date", "retrieval_date", "confidence"]:
        assert field in data["required_fields_per_claim"]
