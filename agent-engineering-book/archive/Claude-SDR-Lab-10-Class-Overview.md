# Claude SDR Lab — 10-Class Overview

## Slide 1: Claude SDR Lab — Agent Engineering in 10 Days

- Objective: given a company name and our offering, produce an evidence-backed Account Brief — signals, stakeholders, pain/value hypotheses, draft outreach — with an independent reviewer checking every material claim
- Approach: learn Claude Code by building one real multi-agent system, not by studying isolated features
- One concept per class — Skills, subagents, tools, hooks, MCP, evals — each new class solves a problem the previous class exposed
- A hard rule for the whole course: human approval before any external action, every time

**Speaker notes:**

Frame the course before touching anything technical. The goal is NOT "replace an SDR" — it's a reliable, inspectable outbound intelligence system that researches accounts, detects buying signals, prepares personalized outreach, and improves through measured feedback. That distinction matters: it keeps scope honest and keeps a human approval gate in place while we're learning and collecting evaluation data.

Point out this is deliberately built as both a Claude learning lab and a reusable architecture — the same pattern generalizes to consulting discovery, proposal generation, and other enterprise research problems, not just SDR outbound.

Close the slide by previewing the shape of the course: 10 classes, each ships one working capability, one Claude concept, one evaluation dataset, and one visible improvement over the previous version. Nothing gets sent automatically, ever — that's non-negotiable and stays true through class 10.

---

## Slide 2: Class 1 — Project Foundation

- Set up the Claude Code project structure (config/, data/, outputs/, .claude/)
- Write CLAUDE.md — the business context and operating rules every future agent inherits
- Define the four business inputs agents can't work without: ICP, offering, voice, evidence policy
- No agents yet — this class is the scaffolding everything else builds on

**Speaker notes:**

This is deliberately the least "exciting" class and that's the point — we're building the deterministic foundation before anything reasons or acts. Emphasize CLAUDE.md as project-wide operating rules, not documentation: cite sources, separate fact from inference from speculation, never invent a stakeholder or event, no automated sending.

Walk through why the four config files exist before any agent does: the agents cannot work well without stable business context (ICP, offering, voice, evidence policy). Getting these right now saves rework in every later class.

Tie back to the course framing: no memory, no loops — every run this class enables will be stateless and independent until Class 4 introduces subagents and later classes introduce memory deliberately.

---

## Slide 3: Class 2 — Account Research Skill

- Author the first SKILL.md — .claude/skills/account-research/
- Define purpose, inputs, procedure, and output schema for company research
- Produce the first structured JSON company profile
- Learn the difference between a one-off prompt and a reusable Skill

**Speaker notes:**

This is the reference implementation for the whole course. Walk through the target output shape live: company, industry, size_estimate, business_model, recent_signals, likely_priorities, possible_pain_points, evidence, confidence.

The key teaching moment: a Skill is a reusable capability package Claude loads only when needed, not a permanent addition to context. Contrast this with just pasting instructions into a prompt each time — Skills can be tested, versioned, and reused across subagents.

Introduce basic evaluation here too: does the output match the schema, is confidence populated, are there any obviously fabricated fields? We're not doing citation-grade evidence checking yet — that's Class 3.

---

## Slide 4: Class 3 — Research Tools

- Give the Account Researcher real tools: web search, website fetch, file read/write
- Every factual claim must carry a source, source date, and retrieval date
- Classify each claim as directly supported or inferred — no blending fact and guesswork
- First evaluation pass: citation coverage and hallucination checks

**Speaker notes:**

This is where research stops being "the model just knows things" and becomes evidence-gathering. Connect directly to the evidence-policy.yaml scaffolded back in Class 1 — this is the class where it actually gets enforced.

Push on hallucination control specifically: an ungrounded claim about a company is worse than no claim at all, because it looks credible. The acceptance target for the whole MVP is 100% of factual claims carrying a source — this is the class where that habit gets built in.

Demo: run the researcher on one real company, show it retrying a search when the first source is stale or insufficient.

---

## Slide 5: Class 4 — Signal Hunter

- Split Account Research into two specialized subagents: Company Profiler and Signal Hunter
- Signal Hunter looks only for timely events — funding, leadership changes, hiring, M&A, layoffs, regulatory events
- Each subagent gets its own instructions, tool permissions, and one narrow responsibility
- Learn context isolation — a subagent doesn't inherit the manager's full conversation

**Speaker notes:**

This is the first real architectural decision of the course: when does a capability deserve its own subagent versus staying inside one Skill? The answer here is responsibility boundaries — Company Profiler answers "what is this company," Signal Hunter answers "what just changed." Different questions, different tools, different failure modes.

Claude Code subagents live under .claude/agents/ with their own instructions, tool permissions, and hooks — show the file structure, not just the concept.

Land the distinction the course keeps returning to: a prompt vs. a Skill vs. a subagent vs. an orchestrated workflow. This class is where subagent finally becomes concrete instead of theoretical.

---

## Slide 6: Class 5 — Research Orchestrator

- Build a Campaign Manager that delegates to Company Profiler and Signal Hunter, then aggregates their output
- First end-to-end workflow: Target Account → Company Profile → Trigger Events → draft Account Brief
- Learn delegation: the manager decides who does what, each worker returns structured output
- One subagent failing must not take down the whole run

**Speaker notes:**

This is the first class where students run something that feels like a real system rather than a single call. Walk the pipeline on the whiteboard before touching code: Target Account down to Evidence and Quality Review — we're only building the first half this class (through the draft brief), the rest arrives in Classes 6-8.

Emphasize reliability as a design constraint, not an afterthought: individual agent failure must not destroy the entire workflow, and failed research should produce "insufficient evidence," never invented content.

Reiterate the human-in-the-loop rule: the system produces an Account Brief, it does not send anything. That gate stays in place through the rest of the course.

---

## Slide 7: Class 6 — Stakeholder and Pain Agents

- Add a Stakeholder Mapper — identifies likely target roles first, names real people only with direct evidence
- Add pain and value hypothesis reasoning, chained: signal → business pressure → our capability → testable value hypothesis
- Every hypothesis is explicitly classified as verified fact, reasoned inference, or speculative hypothesis
- Define strict JSON schemas for each stage so outputs compose reliably

**Speaker notes:**

Multi-stage reasoning is the new skill this class, and schemas are what make it safe: each stage's output has to be structured enough that the next stage can trust it without re-deriving it.

Walk through a concrete hypothesis object live: hypothesis text, classification (fact / inference / hypothesis), supporting_evidence, confidence score. Stress that the classification field is not decoration — the reviewer in Class 8 will reject anything that blends inference into a factual claim.

Stakeholder Mapper is the first place fabrication risk gets personal — inventing a named decision-maker is a much worse failure than a generic pain hypothesis. Roles first, real people only with evidence, no exceptions.

---

## Slide 8: Class 7 — Outreach Composer

- Add a Message Composer: first-touch email, LinkedIn connection note, and meeting-opening question
- Enforce voice.yaml constraints — tone, banned phrases, word limits, no pitch in the first message
- Personalization must be grounded in evidence gathered earlier in the pipeline, not generic flattery
- Still nothing sends automatically — the composer produces drafts only

**Speaker notes:**

This is where the course starts to feel like the actual product, so it's worth slowing down on constraints rather than celebrating fluent copy. Pull up voice.yaml from Class 1 and show how each field maps directly to a generation rule: pitch_allowed: false, maximum_words: 90, avoid list.

The failure mode to watch for in this class is fabricated familiarity — language that implies prior contact or relationship with the recipient. That's called out explicitly as something the reviewer must catch next class, so make sure students see it happen at least once here.

Good personalization test: could this exact line be sent to any company in the ICP, or does it require the specific evidence gathered for this account? If the former, it's generic and should fail review.

---

## Slide 9: Class 8 — Reviewer and Hooks

- Formalize the Evidence Reviewer — rejects unsupported claims, flags generic personalization, detects fabricated familiarity
- Add pre-tool hooks: block automated sending, destructive commands, unapproved directory access
- Add post-tool hooks: citation presence, required fields, valid JSON, dated sources
- Add a final-output hook that runs the evaluation rubric before a brief is accepted

**Speaker notes:**

This is the class where the project becomes a real agent system rather than a chain of prompts — guardrails are what make autonomy safe to extend later.

Walk through all three hook types with a concrete trigger for each: pre-tool stops an action before it happens (e.g. blocking an email-send tool call outright), post-tool checks the shape of what just came back (e.g. rejecting a signal with no date), final-output is the last gate before a brief is considered "done" for this run.

Have students deliberately plant an error — an unsupported claim or a fabricated stakeholder — and confirm the reviewer catches it. That's one of the course's explicit success criteria, so make it a live demo, not a slide claim.

---

## Slide 10: Class 9 — MCP Integration

- Connect via MCP to real external systems — CRM, Google Sheets, research/enrichment services
- Replace the static accounts.csv with live, authenticated data sources
- Learn MCP as Claude Code's standard mechanism for external tools and data
- Guardrails still apply: read and enrich only — no CRM write-back, no automated sending

**Speaker notes:**

This is the class where the system stops being a closed sandbox and starts touching the real world — which is exactly why the Class 8 guardrails have to be solid before we get here.

Show at least one authenticated MCP connection end to end (e.g. Google Sheets or a CRM sandbox), and make explicit what's still out of scope even with real systems connected: no CRM write-back, no large-scale scraping, no autonomous campaign execution. Those are Phase 9-10 concepts, well past this course.

Good discussion prompt: now that we can reach a CRM, what's the actual argument for not letting the agent write back to it yet? Tie the answer back to the evaluation numbers we don't have yet — that's next class.

---

## Slide 11: Class 10 — Evaluation and Scaling

- Run the full pipeline across the whole 10-20 account list, not just one company
- Add prompt caching for the ICP, offering, and voice context reused on every account
- Add batch processing, concurrency, retries, and token/cost logging
- Score against the MVP acceptance targets: ≥90% verified accuracy, 0 fabricated people or events, ≥7/10 message quality, 100% human approval before send

**Speaker notes:**

This is the course's closing argument: everything built since Class 1 either holds up at scale or it doesn't, and this class is where we find out with numbers instead of vibes.

Prompt caching pays off specifically because ICP, offering, and voice are identical across every account in the run — point back at the Class 1 config files as the reused context. Batch processing is what makes running 20 accounts a class exercise instead of an afternoon of babysitting.

Close by reading the acceptance targets against whatever the class's own run actually produced. The course succeeds if students can point at their own numbers — factual accuracy, fabrication rate, reviewer verdicts — not just at a working demo. And the human approval gate from Class 1 is still there, unchanged, on every single account.
