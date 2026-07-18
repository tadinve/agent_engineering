# Chapter 5 — Structured Outputs and Data Contracts

Natural-language outputs are useful for people but unreliable as interfaces between software components. This chapter introduces structured outputs and data contracts as the foundation of agent orchestration. Readers define JSON schemas, validation rules, confidence semantics and explicit error objects. They then design the Account Brief schema that will connect research, reasoning, composition and review stages. The central lesson is that agents should communicate through contracts rather than loosely interpreted prose.

## 5.1 Why Natural-Language Outputs Are Not Enough

A prose response may omit important information, change field names or blend facts with assumptions. Downstream software then has to infer the structure, creating silent errors.

Structured outputs make required information explicit and machine-checkable. Narrative explanations may still be included, but the workflow should depend on validated fields rather than prose interpretation.

## 5.2 JSON Schemas and Typed Objects

JSON Schema or equivalent typed models define fields, data types, nested objects and permitted values. The schema becomes the contract between an agent and the next component in the workflow.

Readers will build schemas that are strict enough to validate but flexible enough to represent partial research. They will also generate typed application models from these definitions where appropriate.

## 5.3 Required, Optional and Enumerated Fields

Required fields represent information without which the output cannot be used. Optional fields represent information that may legitimately be unavailable.

Enumerations constrain fields such as evidence classification, workflow status and confidence level. They reduce ambiguous variations such as "probably," "likely" and "medium confidence" appearing without consistent meaning.

## 5.4 Confidence, Status and Error Objects

A useful output should communicate whether the task succeeded, partially succeeded or failed. It should also distinguish model confidence from evidence strength.

Error objects will identify the failing stage, error type, attempted action and recoverability. This prepares the workflow for later retry and recovery mechanisms.

## 5.5 Schema Validation and Repair

Every structured output should be validated before it is passed downstream. Invalid output may be rejected, repaired deterministically or returned to the agent with precise validation feedback.

Readers will compare uncontrolled regeneration with targeted repair. They will also establish limits so that repeated schema failures do not create endless correction loops.

## 5.6 Designing the Account Brief Schema

The Account Brief will contain company profile, signals, stakeholder roles, hypotheses, evidence, outreach drafts, reviewer findings and approval status. Each section will have its own schema and version identifier.

The schema will evolve throughout the book. Versioning from the beginning will make later additions — such as memory references and production lineage — manageable.
