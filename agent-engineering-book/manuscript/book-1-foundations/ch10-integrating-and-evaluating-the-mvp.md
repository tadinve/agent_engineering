# Chapter 10 — Integrating and Evaluating the MVP

The final chapter of Book 1 assembles the individual components into the first complete Claude SDR Lab. Readers run the workflow across a small account dataset, examine component and end-to-end behaviour and establish the initial evaluation baseline. The objective is not to claim production readiness, but to demonstrate that the system works coherently, produces inspectable evidence and respects the human-approval boundary. The completed version becomes the starting point for the advanced capabilities introduced in Book 2.

## 10.1 The End-to-End SDR Workflow

The integrated workflow begins with a target company and offering configuration. It produces a company profile, relevant signals, stakeholder roles, business hypotheses, draft outreach and an independent review.

Every stage writes a structured artifact. The final Account Brief links these artifacts together without concealing uncertainty or failed stages.

## 10.2 Stakeholder and Pain Hypothesis Generation

The Stakeholder Mapper will identify relevant roles before attempting to name individuals. A real person may be included only when direct, current evidence is available.

Pain hypotheses will connect observed signals to possible business pressure. They will remain explicitly classified as inferences or hypotheses until validated with the prospect.

## 10.3 Evidence-Grounded Outreach Composition

The Message Composer will use only approved facts, hypotheses and internal offering information. Personalization must depend on account-specific evidence rather than generic compliments.

Voice rules will control length, tone, claims and calls to action. The composer will create drafts but will have no permission to send them.

## 10.4 Independent Review

The reviewer will inspect factual support, evidence classification, stakeholder verification, message specificity and policy compliance. It will return structured findings rather than simply rewriting the draft.

The reviewer remains independent of the composer's internal reasoning. This creates a meaningful verification boundary rather than a cosmetic self-critique step.

## 10.5 Building a Beginner Evaluation Dataset

Readers will create a small golden dataset containing expected company facts, known signals, prohibited claims and message-quality examples. Deterministic checks will be combined with a human-readable rubric.

The same test cases will be run against the reader's implementation and the supplied reference solution. Differences will become inputs for analysis rather than merely pass-or-fail judgments.

## 10.6 Demonstrating the Claude SDR Lab MVP

The completed system will be run across several accounts and committed as the Book 1 release. Readers will inspect the generated briefs, validation results and approval records.

The deployment remains local and bounded, but it represents a genuine end-to-end agentic system. Book 2 begins from this tested baseline rather than introducing advanced concepts into an unstable foundation.
