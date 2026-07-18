# Chapter 7 — Evidence-Backed Agent Research

Research agents must do more than produce plausible summaries. They need to locate appropriate sources, extract supported claims, distinguish observations from interpretation and communicate uncertainty. This chapter turns the Account Research Skill into an evidence-backed research capability. Readers develop rules for source quality, dates, conflicting information and claim-level citations. The work is then divided into a Company Profiler and Signal Hunter, each optimized for a different type of research question.

## 7.1 Research as an Agent Workflow

Research involves forming questions, selecting sources, gathering evidence and synthesizing findings. Even in its initial form, the process should be visible rather than hidden inside a single undifferentiated prompt.

Readers will define research stages and the artifacts produced at each stage. This makes it possible to identify whether a weak result was caused by poor search, poor source selection or poor synthesis.

## 7.2 Source Selection and Source Quality

Official company sources, regulatory filings and authoritative publications generally carry more weight than anonymous posts or scraped aggregators. Source quality must nevertheless be evaluated in relation to the claim being made.

A company press release may accurately describe an announcement but not independently validate its success. The system will record source type and allow reviewers to assess the strength of the evidence.

## 7.3 Claim-Level Citations

A list of sources at the end of a report does not show which source supports which claim. Each material fact should be linked to the exact evidence used to derive it.

The research schema will therefore attach citations directly to claims. This makes unsupported statements detectable by deterministic checks and independent reviewers.

## 7.4 Facts, Inferences and Hypotheses

A fact is directly supported by evidence. An inference is a reasoned interpretation of one or more facts. A hypothesis is a proposition that requires validation.

These classifications will be explicit in every relevant output. For example, a hiring increase may be factual, the resulting operational pressure may be inferred and the relevance of the offering may remain a hypothesis.

## 7.5 Freshness, Dates and Conflicting Sources

Research about organizations changes over time. Every source and event should include publication or event dates where available, together with the retrieval date.

When sources disagree, the system should expose the conflict instead of silently choosing the most convenient version. Recent information is not automatically more authoritative, but its timing must be considered.

## 7.6 Building the Company Profiler and Signal Hunter

The Company Profiler will answer relatively stable questions about the organization's business, markets and operating model. The Signal Hunter will focus on timely developments such as leadership changes, funding, acquisitions, hiring and strategic initiatives.

Separating these responsibilities creates clearer evaluation criteria. It also prepares readers to understand when a capability should become a distinct subagent.
