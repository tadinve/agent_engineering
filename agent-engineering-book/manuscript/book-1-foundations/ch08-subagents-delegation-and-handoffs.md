# Chapter 8 — Subagents, Delegation and Handoffs

As workflows grow, one agent can become overloaded with context, responsibilities and tools. This chapter introduces subagents as isolated specialists rather than simulated job titles. Readers define responsibility boundaries, tool permissions and structured handoff contracts before implementing separate research agents. The chapter explains when subagents add genuine value and when a Skill, function or workflow step would be simpler and more reliable.

## 8.1 When a Capability Deserves a Subagent

A subagent is justified when a task benefits from context isolation, parallel execution, specialized tools, restricted permissions or independent verification. Merely giving a task a professional title does not create a useful architectural boundary.

Readers will evaluate candidate subagents using explicit criteria. Unnecessary agents will be replaced by Skills or deterministic components.

## 8.2 Context Isolation

Subagents can operate with only the information required for their task. This reduces distraction, conflicting instructions and context-window consumption.

The Signal Hunter, for example, does not need every draft email or reviewer comment. Its context can remain focused on the target company, date range and acceptable signal categories.

## 8.3 Agent Roles and Responsibility Boundaries

Each subagent should own a defined output and avoid duplicating another component's work. Overlapping responsibilities create inconsistent conclusions and make failures difficult to attribute.

Readers will document each agent's purpose, exclusions and success criteria. These definitions become part of the system's architecture rather than informal prompt wording.

## 8.4 Tool and Permission Boundaries

Different subagents may require different toolsets. A research agent may search the web and read files, while a reviewer may only inspect supplied evidence and should not modify the original research.

Restricting permissions reduces accidental side effects and limits the consequences of prompt injection. Least privilege will be introduced here and expanded substantially in Book 3.

## 8.5 Handoff Contracts

A handoff should specify what information is transferred, the receiving agent's responsibility and the expected output schema. Passing a full conversational transcript is rarely an effective contract.

Readers will create compact handoff objects containing the target, completed work, supporting artifacts and unresolved questions. This supports reliable composition and later trajectory evaluation.

## 8.6 Creating the SDR Research Subagents

The Company Profiler and Signal Hunter will be implemented as separate subagents under `.claude/agents/`. Each will have independent instructions, permitted tools and validated output contracts.

The agents will be tested separately before orchestration. This allows readers to distinguish component quality from coordination quality.
