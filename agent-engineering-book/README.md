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

## Development environment

- **Python**: 3.11+ (same minimum the book states in Chapter 2).
- **Claude Code**: current stable release — install per `book-1-foundations/SETUP.md`.
- **Setup and the one repository-wide quality gate:**

  ```
  cd agent-engineering-book
  python3 -m venv .venv && source .venv/bin/activate
  pip install -e ".[dev]"
  make verify
  ```

  `make verify` (`scripts/verify_repository.py`) checks everything in one
  command, locally and in CI identically: `manifest.yaml` validity and
  required artifacts per class, `tests_shared/` sync (no class's copy has
  drifted from canonical), no stray/secret files tracked by git, no broken
  relative links across the book's markdown, class folder names matching
  their manifest metadata, and the full pytest suite (schema validation,
  cross-file integrity, permission-deny rules, candidate-account fit,
  proof-point expiry). This is exactly what CI's `verify` job runs.

- **Individual class test command** (what a learner actually runs while
  working a class — see `HOW-TO-WORK-A-CLASS.md`):

  ```
  cd book-1-foundations/class-NN-.../
  pip install -r requirements-dev.txt
  pytest tests/ -v
  ```

  Per-class `requirements-dev.txt` files exist so a class folder copied out
  on its own is still self-sufficient; they're a subset of the root
  `pyproject.toml`'s `dev` extra, not an independent set — `pyproject.toml`
  is where a new dependency actually gets added first. CI's
  `per-class-self-sufficiency` job runs exactly this, per class, from a
  fresh checkout — proving self-sufficiency rather than assuming it.

- **`scripts/`** — `check_manifest.py`, `sync_shared_tests.py`,
  `create_class.py`, and `verify_repository.py`; see `scripts/README.md`.

## Current status

Precise, not aspirational, as of this writing:

- **Manuscript**: all 50 chapter blueprints drafted. Book 1's 10 chapters
  have since been expanded into full technical chapters (~23,700 words
  total, averaging ~2,370 words/chapter) — each goes beyond its original
  six `x.1`–`x.6` subsections with additional topics, worked examples and
  code excerpts drawn from the actual reference implementation, a Common
  Pitfalls section, and end-of-chapter exercises. Books 2–5 (chapters
  11–50, ~15,000 words) remain at original blueprint depth — see the
  depth caveat under "The five books" below.
- **Implementation**: Book 1, Classes 02 and 03 built and tested, plus CI.
  Class 02 has 6 gate tests; Class 03 is cumulative and has 114 (the same 6
  inherited from Class 02, unchanged, plus 108 new — not two independently-
  sized suites added together). Class 01 is a concept exercise (no code).
  Classes 04–10 are placeholder folders only.
- **Config as a real contract**: Class 03's five business-context files
  each have a formal JSON Schema (with tests proving the schemas actually
  reject bad input), a candidate-account dataset checked deterministically
  against the ICP, a proof-point lifecycle (approved/retired + expiry, not
  one ambiguous date), and cross-file integrity tests (e.g. CLAUDE.md's
  vocabulary vs. evidence-policy.yaml's, no unreferenced approved proof
  points). A manifest (`book-1-foundations/manifest.yaml`) is the single
  source of truth for which classes are implemented — CI validates every
  required artifact against it, not by scanning directories.
- **Process infrastructure**: `HOW-TO-WORK-A-CLASS.md`, the LLM-as-judge
  grading template, and CI are in place and apply to whatever's built.

The honest one-line summary: **a fully architected 50-chapter programme,
with Book 1 under active implementation and Classes 1–3 complete.** Not yet
a finished manuscript, and not yet a working Claude SDR Lab MVP — that
requires Classes 4–10.

## The five books

| Book | Chapters | Theme |
|---|---|---|
| 1 — Agent Engineering Foundations | 1–10 | Build the Claude SDR Lab MVP |
| 2 — Advanced Agent Architectures | 11–20 | Knowledge, memory, planning, collaboration |
| 3 — Reliable and Secure Agent Systems | 21–30 | Resilience, guardrails, safe autonomy |
| 4 — AgentOps and Production Engineering | 31–40 | Operating, evaluating, scaling |
| 5 — Frontier and Specialized Agent Systems | 41–50 | Multimodal, graph, model adaptation |

Every chapter file in `manuscript/` contains at least the intro paragraph and
the `x.1`–`x.6` subsections given in the original source outline — nothing
here is an empty stub. Depth varies by book, and it's worth being precise
about the difference:

- **Book 1** (chapters 1–10) has been expanded past blueprint stage into
  **full technical chapters**: each subsection is fleshed out with concrete
  detail, most chapters add several additional subsections beyond the
  original `x.6` (worked code and config excerpts pulled from the actual
  `book-1-foundations/` reference implementation, not invented examples), and
  every chapter closes with a Common Pitfalls section and end-of-chapter
  exercises. Average length is ~2,370 words, in the typical technical-book
  chapter range.
- **Books 2–5** (chapters 11–50, ~15,000 words) remain **chapter blueprints**
  — the full intended coverage, in outline-plus-paragraph form, at
  ~350–400 words per chapter — not yet expanded to the same depth. That
  expansion is separate, not-yet-started work, and would naturally follow
  each book's own reference implementation being built, the same way Book
  1's expansion followed Book 1's.

## How Book 1 is organized

Each class (chapter) gets its own folder under `book-1-foundations/`,
matching the manuscript filename:

```
book-1-foundations/
├── manifest.yaml         the single source of truth for "which classes are implemented"
├── tests_shared/         canonical foundational tests — edit here, not in a class folder
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

That duplication is managed, not manual: foundational tests live once in
`tests_shared/` and get copied into every applicable class by
`scripts/sync_shared_tests.py`. Fix a foundational test in `tests_shared/`,
re-run the sync script, and the fix reaches every class that carries that
chapter — `sync_shared_tests.py --check` (which CI runs) fails the build if
any class's copy has silently drifted from canonical instead.

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
