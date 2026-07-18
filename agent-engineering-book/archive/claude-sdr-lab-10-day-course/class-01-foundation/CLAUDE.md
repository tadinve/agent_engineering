# Claude SDR Lab — Class 1: Foundation

## What this project is

Given a company name and our offering, produce an evidence-backed Account
Brief containing current signals, likely stakeholders, pain and value
hypotheses, and draft outreach — with an independent reviewer checking every
material claim.

This is a learning project: we're building a small, inspectable outbound
intelligence system one Claude Code concept at a time (Skills, subagents,
tool use, hooks, MCP, evaluation). Class 1 sets up the project foundation
only — no Skills or subagents exist yet. See README.md for the class-by-class
plan.

## Business context

Read these before doing any research or writing any output:

- `config/icp.yaml` — who we target
- `config/offering.yaml` — what we sell, and what we may not claim
- `config/voice.yaml` — tone and outreach constraints
- `config/evidence-policy.yaml` — what counts as valid evidence for a claim

## Non-negotiable operating rules

- Never state a fact about a company or person without a source, source
  date, and retrieval date. See `config/evidence-policy.yaml`.
- Distinguish verified fact, reasoned inference, and speculative hypothesis
  explicitly — never blend them.
- Never invent a stakeholder, event, or signal. If evidence is insufficient,
  say "insufficient evidence" rather than filling the gap.
- Never claim prior contact, familiarity, or relationship with a target
  company or person unless it is directly evidenced.
- No automated sending of email or LinkedIn messages. Every external action
  requires explicit human approval. (Nothing in this project sends anything
  yet — sending is explicitly out of scope for the MVP.)
- Never commit secrets. API keys live in environment variables only; see
  `.gitignore` at the repo root.

## Directory layout (Class 1)

```
class-01-foundation/
├── CLAUDE.md          this file
├── README.md          setup and orientation
├── .claude/
│   └── settings.json  intentionally minimal — hooks/permissions arrive Class 8
├── config/            business inputs agents will read starting Class 2
├── data/
│   ├── accounts.csv   10-20 seed target accounts
│   ├── examples/      worked agent output (empty until Class 2)
│   └── evals/         gold-standard eval set (empty until Class 3)
└── outputs/           generated run output, gitignored
```

`.claude/skills/`, `.claude/agents/`, `schemas/`, and `scripts/` are not
created yet — they show up as later classes introduce the concepts that need
them (Skills in Class 2, subagents in Class 4, schemas/validation earlier
than that as research output needs structure).
