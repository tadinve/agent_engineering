# Course Setup

Do this once, before Class 01. Class 01 is a concept exercise you work
through *with* Claude Code — it shouldn't have to double as an installation
guide, and Class 02 is about workspace/project structure, not tool
installation. Separating the two avoids a chicken-and-egg problem where
Class 01 needs a tool that Class 02 is what teaches you to set up.

## Install

1. **Claude Code** — install and authenticate per Anthropic's current
   instructions for your platform.
2. **Git** — any recent version.
3. **Python 3.11+** — confirm with `python3 --version`.

## Verify

```
claude --version
git --version
python3 --version
```

All three should print a version, not an error.

## Then

Start with `class-01-from-language-models-to-agents/README.md`. Its
`BUILD.md` is an exercise conducted through a live Claude Code (or
Claude.ai) conversation, not a code build — you need Claude available, not
a project workspace yet. The project workspace itself is what Class 02
builds.
