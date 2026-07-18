# Chapter 9 — Workflow Orchestration and Human Approval

A collection of Skills and subagents does not automatically become a coherent system. Orchestration determines the order of work, the flow of information, the handling of partial failure and the points at which human judgment is required. This chapter introduces sequential, parallel and conditional workflows, along with a Campaign Manager that coordinates the SDR agents. Readers also implement basic workflow state and a formal human-approval gate.

## 9.1 Sequential, Parallel and Conditional Workflows

Sequential workflows are appropriate when one stage depends on another. Parallel workflows reduce latency when tasks can be performed independently.

Conditional workflows choose different paths based on validated state or evidence. Readers will learn to represent these patterns explicitly rather than relying on an unrestricted model to decide every transition.

## 9.2 Manager–Worker Orchestration

The Campaign Manager receives the overall objective, delegates bounded tasks and combines the resulting artifacts. Worker agents remain responsible for specialized outputs rather than the entire business goal.

The manager should not repeat all worker reasoning. Its role is coordination, dependency management, validation and escalation.

## 9.3 Basic Workflow State

Workflow state records where a run currently stands: pending, active, complete, failed or awaiting approval. This is distinct from the conversational context visible to the model.

Readers will implement a run record containing identifiers, stage statuses, artifact references and errors. This allows the workflow to be inspected without rereading the entire conversation.

## 9.4 Partial Results and Failed Subagents

One failed research component should not necessarily invalidate every completed stage. The orchestrator should preserve valid partial results and identify what remains unavailable.

The system will return "insufficient evidence" rather than ask another component to invent missing content. More sophisticated recovery will be introduced in Book 3.

## 9.5 Human Approval Gates

External actions and material business claims require human judgment. The approval interface should present the proposed output, evidence, uncertainties and reviewer findings — not merely a generic confirmation button.

Readers will implement approve, edit and reject outcomes. The workflow will remain paused until one of these decisions is recorded.

## 9.6 Building the Campaign Manager

The Campaign Manager will coordinate profiling, signal research, stakeholder analysis, hypothesis development, message composition and review. It will preserve intermediate artifacts and produce a consolidated Account Brief.

The first version will use an explicit, bounded workflow. Greater planning discretion and adaptive loops will be introduced only after the deterministic baseline has been tested.
