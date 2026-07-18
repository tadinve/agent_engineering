# Class 03 — Instruction Architecture and CLAUDE.md

Self-sufficient snapshot: this folder is the complete project state after
finishing Chapter 3. It includes everything from Class 02 plus this
chapter's additions — open it standalone, nothing outside this folder is
required.

## What's new since Class 02

- `CLAUDE.md` — written for real: project purpose, non-negotiable operating
  rules, instruction precedence, and pointers to the business-context files
  below.
- `config/icp.yaml`, `offering.yaml`, `voice.yaml`, `evidence-policy.yaml` —
  the four business-context files CLAUDE.md points to.
- `data/accounts.csv` — a seed list of 12 target accounts matching the ICP
  (this was migrated forward from an earlier build of this same project;
  see the repo-level README's "History" section).
- `tests/ch03/` — gate test confirming CLAUDE.md references all four config
  files and that they're valid, well-formed YAML.
- `BUILD.md` / `GRADING.md` — how to build this class and how to have Claude
  grade your attempt against this reference; see `../../HOW-TO-WORK-A-CLASS.md`.

## Run the tests

Requires Python 3.11+.

```
cd class-03-instruction-architecture-and-claude-md
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
python3 -m pytest tests/ -v
```

## Next

Class 04 (Skills and Reusable Capabilities) is not yet built. It will add
`.claude/skills/account-research/SKILL.md` and produce the first structured
JSON company profile.
