# Agent Engineering — From First Agent to Production-Grade Autonomous Systems

Source repo for the book by Venkatesh Tadinada.

- **[`manuscript/`](manuscript/)** — the book text: title page, front matter,
  and five books of ten chapters each.
- **[`book-1-foundations/`](book-1-foundations/)** — the reference
  implementation for Book 1, one self-sufficient folder per class. **This is
  the current focus.** Books 2–5 don't have code folders yet.
- **[`archive/`](archive/)** — superseded planning documents and an earlier,
  shorter build of the same underlying project, kept for reference.
- **[`HOW-TO-WORK-A-CLASS.md`](HOW-TO-WORK-A-CLASS.md)** — the generic
  workflow for building any class, fork through grading. Read this before
  starting Class 02.
- **[`GRADING-RUBRIC-TEMPLATE.md`](GRADING-RUBRIC-TEMPLATE.md)** — the
  generic LLM-as-judge template each class's `GRADING.md` plugs into.
- **`my-work/`** — gitignored personal workspace for your own attempts; see
  `my-work/README.md`.

## The five books

| Book | Chapters | Theme |
|---|---|---|
| 1 — Agent Engineering Foundations | 1–10 | Build the Claude SDR Lab MVP |
| 2 — Advanced Agent Architectures | 11–20 | Knowledge, memory, planning, collaboration |
| 3 — Reliable and Secure Agent Systems | 21–30 | Resilience, guardrails, safe autonomy |
| 4 — AgentOps and Production Engineering | 31–40 | Operating, evaluating, scaling |
| 5 — Frontier and Specialized Agent Systems | 41–50 | Multimodal, graph, model adaptation |

Each chapter file in `manuscript/` contains the full chapter text — intro
paragraph plus all `x.1`–`x.6` subsections — organized one file per chapter.

## How Book 1 is organized

Each class (chapter) gets its own folder under `book-1-foundations/`,
matching the manuscript filename:

```
book-1-foundations/
├── class-01-from-language-models-to-agents/    concept only, no code
├── class-02-setting-up-the-claude-code-workspace/
│   ├── README.md        what's in this snapshot
│   ├── BUILD.md         how to build it yourself, using Claude
│   └── ...              the completed code for this class
├── class-03-instruction-architecture-and-claude-md/
│   └── ...               same pattern, one class further along
├── class-04-... through class-10-...           not yet built
```

Every class folder from 02 onward is **self-sufficient**: it's the complete,
cumulative project state through that chapter, not just that chapter's diff.
Open `class-05/` on its own and you have a fully working project through
Chapter 5 — you don't need to have built classes 2–4 first. This trades
some duplication across folders for the ability to jump to any checkpoint
directly.

Each class folder has (or will have) three documents:

- **`README.md`** — what's in this snapshot, what's new since the last class.
- **`BUILD.md`** — a practical, step-by-step walkthrough for building this
  class's deliverable yourself using Claude Code, ending in a `pytest` gate
  check against the reference solution already in the folder.
- **`GRADING.md`** — the quality-check criteria for this specific class, for
  use with `GRADING-RUBRIC-TEMPLATE.md`'s LLM-as-judge step. Gate tests
  check the structural contract; grading checks whether the work is
  actually good.

Full procedure, fork through grading: `HOW-TO-WORK-A-CLASS.md`.

## History — how this became one project

This project went through two earlier, separate planning efforts before
landing here:

1. **A 10-day / 10-class course outline** (a Word doc), which produced a
   `claude-sdr-lab/class-01-foundation/` build — real `CLAUDE.md`,
   `config/*.yaml`, and `data/accounts.csv` for its Class 1 — plus a
   matching slide deck (`.pptx`/`.md`) covering all 10 classes.
2. **This 50-chapter book** (a separate, much larger planning document),
   describing the same underlying Claude SDR Lab project in far more depth,
   organized as 5 books of 10 chapters instead of one 10-class course.

Both described the same project at different scales and had drifted apart
structurally (e.g. the course's "Class 8: Reviewer and Hooks" has no single
equivalent in the book, which spreads guardrails and human control across
several chapters in Book 3 instead).

**Reconciliation**: the book is now the canonical version. The real content
already written for the old course's Class 1 (`config/*.yaml`,
`data/accounts.csv`) was migrated into `class-03-instruction-architecture-and-claude-md/`
and adapted to this book's Chapter 3 framing (instruction precedence,
policy/procedure/reference separation) rather than rewritten from scratch.
`CLAUDE.md` was then written for real using that migrated content,
completing Chapter 3. The project was later restructured a second time —
from one continuously-evolving `sdr-lab/` folder into the current per-class
self-sufficient folders described above, so each class is independently
buildable and each has its own Claude-driven build guide. The original
course build, its source doc, and its slide deck remain preserved under
`archive/` — nothing was deleted, only consolidated.

## Next step

Build Class 04 (Skills and Reusable Capabilities): author
`.claude/skills/account-research/SKILL.md` and produce the first structured
JSON company profile, starting from a copy of
`class-03-instruction-architecture-and-claude-md/`.
