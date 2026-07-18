# How to Work a Class

The generic procedure for building any class (chapter) in this book, from
first fork through grading. Every class's own `README.md`/`BUILD.md` assumes
you've read this once.

## One-time setup

1. **Fork** this repo on GitHub into your own account.
2. **Clone your fork** locally and track the original as `upstream`:

   ```
   git clone <your-fork-url>
   cd agent_engineering
   git remote add upstream <original-repo-url>
   ```

3. **Install tools** per `book-1-foundations/SETUP.md` — Claude Code, Git,
   Python 3.11+. This happens once, before Class 01, precisely so Class 01
   isn't also an installation tutorial and Class 02 isn't a prerequisite for
   Class 01's own exercise.

## Per class-NN

4. **Sync your fork** before starting, in case earlier classes were fixed or
   new ones published:

   ```
   git fetch upstream
   git merge upstream/main
   git push origin main
   ```

5. **Copy the previous class**, not class-NN itself, into `my-work/` as your
   starting point:

   ```
   cp -r agent-engineering-book/book-1-foundations/class-(NN-1)-.../ \
         agent-engineering-book/my-work/book-1/class-NN/
   ```

   `class-NN-.../` in the repo is the finished reference solution — don't
   open it yet. (Class 02 has no predecessor; start from its own `BUILD.md`
   directly.)

6. **Read the manuscript chapter**
   (`manuscript/book-1-foundations/chNN-....md`) for the concept, then work
   through `class-NN-.../BUILD.md` — but building inside
   `my-work/book-1/class-NN/`, not the reference folder.

7. **Gate check — run the tests.** Copy `class-NN-.../tests/chNN/` (and any
   earlier `tests/chMM/` it depends on) into your working folder and run:

   ```
   cd agent-engineering-book/my-work/book-1/class-NN
   pip install -r requirements-dev.txt
   python3 -m pytest tests/ -v
   ```

   This is deterministic and binary: it checks the structural contract
   (files exist, schemas validate, required fields are present), not
   whether your solution is *good*. Don't skip it, but don't mistake it for
   step 9 either.

8. **Verify and fix** until every test passes.

9. **Now** open the gold solution
   (`book-1-foundations/class-NN-.../`) and diff against your own. Look at
   what you did differently, what you missed, and — just as importantly —
   where your approach is legitimately different but equally valid. The
   reference is one correct answer, not the only one.

10. **Quality check — LLM-as-judge.** Gate tests can't tell you whether your
    `CLAUDE.md` is well-written or your config is internally coherent. Follow
    `GRADING-RUBRIC-TEMPLATE.md` together with `class-NN-.../GRADING.md`
    (that class's specific criteria) to have Claude grade your submission
    against the gold solution on the things pytest can't check.

11. **Commit** your working folder to your fork. Optionally open a PR
    against your own fork's main branch just to keep a record — there's no
    requirement to push it anywhere else.

## The two-tier testing model

Every class distinguishes two different kinds of "is this done":

| | Gate check (step 7) | Quality check (step 10) |
|---|---|---|
| Tool | `pytest` | Claude, as an LLM judge |
| Nature | deterministic, offline | subjective, rubric-guided |
| Answers | "Did you meet the contract?" | "Is it actually good?" |
| Failure mode if skipped | broken structure ships silently | shallow, copy-of-the-reference work passes unnoticed |

Passing gate tests is necessary but not sufficient. A `CLAUDE.md` that
exists, references all four config files, and parses fine can still be a bad
`CLAUDE.md` — that's what step 10 is for.
