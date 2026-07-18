# Class 1 — Project Foundation

**Builds:** repository structure, CLAUDE.md, business context config
**Learns:** Claude Code project layout, CLAUDE.md as operating rules, how
agents will read stable business context in later classes

There are no agents, Skills, or scripts to run yet. Class 1 is the
foundation the rest of the course builds on: a real repository shape and
real business inputs, not placeholders.

## Prerequisites

- Claude Code
- Git
- Python 3.11+
- Node.js 20+ (recommended; needed once MCP servers arrive)

See the course requirements doc for full hardware/account details.

## Setup

1. Open this folder (`class-01-foundation/`) in Claude Code.
2. Read `CLAUDE.md` — it's the operating context every future class's
   agents will load.
3. Edit `config/icp.yaml`, `config/offering.yaml`, `config/voice.yaml`,
   `config/evidence-policy.yaml` to reflect your real target market and
   offering. The values checked in are a working example (ApexNeural /
   industrial-automation ICP), not your data.
4. Review `data/accounts.csv` — replace with your own 10-20 target
   companies if you have them, or keep the example list to start.

## Directory tour

| Path | Purpose |
|---|---|
| `CLAUDE.md` | Project-wide business context and operating rules |
| `.claude/settings.json` | Claude Code project settings (minimal for now) |
| `config/` | ICP, offering, voice, and evidence-policy inputs agents will read |
| `data/accounts.csv` | Seed list of target accounts |
| `data/examples/`, `data/evals/` | Empty — populated starting Class 2/3 |
| `outputs/` | Generated run output; gitignored |

## What's next

Class 2 adds the Account Research Skill (`.claude/skills/account-research/`)
and the first structured Account Brief output. Nothing in this class
performs research — it's the scaffolding that makes Class 2 possible.
