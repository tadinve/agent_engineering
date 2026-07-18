# Chapter 4 — Skills and Reusable Capabilities

Repeatedly pasting task instructions into prompts does not create a maintainable agent system. This chapter introduces Skills as reusable, version-controlled capability packages that define how a task should be performed. Readers examine Skill structure, discovery, progressive disclosure and composition before implementing the Account Research Skill. The chapter emphasizes that Skills represent procedural knowledge: they describe a reliable method without necessarily creating a separate autonomous agent.

## 4.1 Prompts Versus Skills

A prompt is usually written for a particular interaction. A Skill packages instructions, procedures, examples and supporting resources so that a capability can be reused consistently.

Skills can be tested, reviewed and versioned like code. They reduce prompt duplication and make the agent's operating procedures visible to developers and instructors.

## 4.2 Anatomy of a SKILL.md

A well-designed Skill defines its purpose, activation conditions, expected inputs, procedure, output requirements and failure behaviour. It may also reference templates, scripts, examples or validation assets.

Readers will examine how much detail belongs in the main Skill file and what should be moved into supporting resources. The objective is to provide enough guidance without flooding the model's context.

## 4.3 Skill Discovery and Progressive Disclosure

Claude should load detailed instructions only when the corresponding capability is required. Progressive disclosure allows the system to know that a Skill exists without placing its entire contents into every interaction.

Readers will use clear names and descriptions so that the correct Skill can be selected. They will also examine ambiguous descriptions that cause the wrong procedure to be invoked.

## 4.4 Inputs, Procedures and Outputs

A Skill should define the information required before execution, the sequence of work and the form of the result. Missing inputs should produce an explicit request or error rather than implicit assumptions.

Procedures should provide useful constraints while leaving room for judgment. Outputs should be structured enough to support the next stage of the workflow.

## 4.5 Skill Composition and Reuse

Complex capabilities can be assembled from smaller Skills. Account research may invoke source assessment, claim extraction and evidence classification without embedding every procedure in one large instruction file.

Readers will learn to avoid Skills that are either too broad to test or so fragmented that orchestration becomes unnecessarily complicated. Good Skill boundaries reflect reusable business capabilities.

## 4.6 Building the Account Research Skill

The first Skill will accept a company name, website and research date, then produce a structured profile supported by evidence. It will identify the company's industry, business model, scale indicators and current strategic signals.

The Skill will initially operate without persistent memory or iterative planning. This controlled baseline allows its behaviour to be evaluated before more advanced capabilities are introduced.
