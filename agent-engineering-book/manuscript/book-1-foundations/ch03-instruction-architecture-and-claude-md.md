# Chapter 3 — Instruction Architecture and CLAUDE.md

An agent cannot perform reliably when its operating expectations are scattered across ad hoc prompts. This chapter introduces instruction architecture: the deliberate separation of project-wide rules, task-specific procedures, business context and reference material. Readers create the first `CLAUDE.md` for the SDR Lab and define requirements for evidence, uncertainty, human approval and external actions. The chapter also explains instruction precedence and why excessively large instruction files can weaken rather than improve agent performance.

## 3.1 The Role of Project-Level Instructions

Project-level instructions establish rules that should apply across tasks and sessions. They define how the agent should behave whenever it operates inside the repository.

Examples include evidence requirements, coding conventions, output locations and approval policies. These rules reduce repeated prompting and create a consistent behavioural baseline for every Skill and subagent.

## 3.2 Designing an Effective CLAUDE.md

A useful `CLAUDE.md` is concise, explicit and operational. It tells Claude what the project is, how work should be performed, what must never happen and how completion should be verified.

Readers will avoid turning the file into a large knowledge dump. Stable rules belong here, while detailed procedures and domain documents will be placed in Skills, configuration files or retrieval sources.

## 3.3 Instruction Scope and Precedence

Agent behaviour may be influenced by system-level rules, project instructions, Skill instructions, subagent definitions, user requests and information found in external content. These sources do not have equal authority.

Readers will define a clear hierarchy in which trusted operating rules override instructions found in websites, documents or tool results. This becomes essential when later chapters introduce prompt injection and poisoned knowledge sources.

## 3.4 Business Context and Operating Rules

The SDR agent needs stable information about the intended customer, the company's offering, communication style and evidence standards. These will be represented through dedicated configuration files rather than repeatedly embedded in prompts.

The initial files will include `icp.yaml`, `offering.yaml`, `voice.yaml` and `evidence-policy.yaml`. Separating them allows the same agent architecture to be reused for different organizations and offerings.

## 3.5 Separating Policy, Procedure and Reference Material

Policies state what is permitted or required. Procedures explain how a task should be performed. Reference materials provide facts and domain knowledge that may be relevant to a task.

Mixing all three creates bloated context and unclear authority. Readers will learn to place policies in project instructions, procedures in Skills and changing knowledge in configuration or retrieval sources.

## 3.6 Defining the SDR Lab Evidence Policy

The evidence policy will specify acceptable sources, citation requirements, freshness expectations and the distinction among fact, inference and hypothesis. It will also prohibit invented companies, events and stakeholders.

Every material factual claim about a prospect must identify its source and date. When evidence is inadequate, the system must report uncertainty instead of completing the brief through fabrication.
