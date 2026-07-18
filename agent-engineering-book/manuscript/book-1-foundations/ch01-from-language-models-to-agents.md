# Chapter 1 — From Language Models to Agents

Large language models generate responses, but agents pursue goals through repeated decisions and actions. This chapter establishes the vocabulary used throughout the book and distinguishes prompts, assistants, workflows and autonomous agents. It introduces the autonomy spectrum and explains why an agent is not always the best solution. Readers examine how probabilistic reasoning can be combined with deterministic software and are introduced to the Claude SDR Lab, the continuous project through which the book's concepts will be implemented and evaluated.

## 1.1 What Makes a System an Agent?

An agent receives a goal, observes its environment, selects actions, evaluates results and decides what to do next. Unlike a conventional chatbot, it may use tools, maintain state and continue working without requiring a new instruction after every step.

Agency is therefore defined by decision-making and action, not merely by conversational fluency. A system that produces a sophisticated answer in one model call may still be an application rather than an agent.

## 1.2 Prompts, Assistants, Workflows and Agents

A prompt provides instructions for one model interaction. An assistant adds persistent instructions, conversational context or access to tools, but may still depend on the user to direct every action.

A workflow defines a sequence of steps created by the developer. An agent receives a goal and has some discretion over which steps, tools or strategies to use. Understanding these distinctions prevents ordinary automation from being mislabeled as autonomy.

## 1.3 The Autonomy Spectrum

Agentic systems range from tightly controlled suggestion generators to systems that plan and execute within defined boundaries. Most enterprise use cases should begin with limited autonomy and explicit approval points.

Readers will learn to think in levels: recommend, draft, act after approval, act within policy and manage exceptions. Autonomy should be increased only when testing demonstrates that the system is ready for additional responsibility.

## 1.4 Deterministic Software Versus Probabilistic Reasoning

Traditional code is appropriate when rules, calculations and transitions are known. Language models are useful when the task requires interpretation, semantic judgment, ambiguity resolution or adaptive planning.

A reliable agent combines both. The model decides where judgment is required, while deterministic code validates schemas, enforces policies, performs calculations and prevents prohibited actions.

## 1.5 When Not to Use an Agent

Agents introduce nondeterminism, cost, latency and operational risk. A simple function, query, rules engine or deterministic workflow may be safer and easier to maintain when the process is already understood.

Readers will learn to justify agent use based on task variability, uncertainty and required judgment. The goal is not to make every application agentic, but to use the least autonomous architecture that solves the problem reliably.

## 1.6 The Claude SDR Lab Case Study

The book's continuous case study begins with a clear objective: given a target company and a defined offering, produce an evidence-backed Account Brief. The brief will eventually include company research, current signals, stakeholder roles, pain hypotheses, value hypotheses and draft outreach.

The system will not send messages autonomously. Human approval remains mandatory, allowing the project to teach practical Agent Engineering without introducing unnecessary external-action risk.
