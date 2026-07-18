# LLM-as-Judge Grading — Generic Template

How to have Claude grade a class submission qualitatively, on top of the
deterministic `pytest` gate check every class already has. Used together
with a class-specific `GRADING.md` (see `class-NN-.../GRADING.md`), which
supplies the criteria this template leaves as placeholders.

## Why a separate step from pytest

Gate tests can only check what's mechanically checkable: does the file
exist, does it parse, does it mention the required fields. They cannot tell
you whether the *content* is good — whether `CLAUDE.md` is concise instead
of a knowledge dump, whether your ICP is internally coherent, whether your
evidence policy would actually catch a fabricated claim. That's a judgment
call, which is exactly the kind of task an LLM is suited to and a
pytest assertion is not.

## What to hand the judge

Four things, every time:

1. **Your submission** — the contents of your `my-work/book-N/class-NN/`.
2. **The gold reference solution** — `book-N-.../class-NN-.../`.
3. **This class's specific criteria** — `class-NN-.../GRADING.md`.
4. **The manuscript chapter** — for the concepts the criteria are checking
   understanding of.

## The judge prompt

Paste this into a fresh Claude Code session (fresh, so it isn't the same
session that helped you build the submission — some independence matters,
even if imperfect):

```
You are grading a student's submission for Class NN against a rubric. Be an
independent, skeptical reviewer — not the collaborator who helped build it.

Here is the class-specific rubric: [paste class-NN-.../GRADING.md]

Here is the manuscript chapter this class is built on:
[paste manuscript/book-N-.../chNN-....md]

Here is the gold reference solution: [paste or point to class-NN-.../]

Here is the student's submission: [paste or point to my-work/book-N/class-NN/]

For each criterion in the rubric:
1. State whether it is met, partially met, or not met.
2. Quote or point to the specific evidence in the submission that supports
   your judgment — don't just assert a verdict.
3. If the submission merely copies the gold reference's wording rather than
   demonstrating independent understanding, say so explicitly — that's a
   partial-met at best, regardless of test results.
4. If the submission takes a legitimately different but equally valid
   approach from the gold reference, say so — don't penalize divergence
   from the reference when the underlying requirement is still satisfied.

Finish with:
- A per-criterion table (met / partial / not met + one-line reason)
- An overall verdict: ready to move on, or needs revision — and if
  revision, the single most important thing to fix first.

Do not produce a single opaque numeric score. The table and verdict are the
output.
```

## Interpreting the result

- **"Ready to move on"** doesn't mean perfect — it means the submission
  demonstrates real understanding of this class's concepts, not just
  passing tests.
- **"Needs revision"** should come with one concrete, prioritized fix, not
  a list of everything imperfect. Fix that one thing, re-run the judge on
  just that criterion rather than the whole rubric again.
- Treat a judge verdict you disagree with as a signal to re-read the
  chapter section it's citing, not as automatically correct. LLM judges can
  be wrong, especially about legitimate alternative approaches — use
  judgment, don't defer blindly.

## Anti-gaming notes

- A submission that's structurally identical to the gold reference (same
  wording, same structure, no independent decisions) should not score well
  even if every gate test passes — that's copying, not building. Rubric
  criteria should explicitly probe for this (see the "independent
  understanding" criterion in each class's `GRADING.md`).
- Don't let the judge grade against its own aesthetic preferences where the
  rubric is silent. If a criterion isn't in `GRADING.md`, it shouldn't
  affect the verdict — extend the rubric instead of grading off-script.
