# Chapter 2 — Setting Up the Claude Code Workspace

Agent behaviour is strongly influenced by the environment in which the model operates. This chapter introduces Claude Code as the implementation environment for the book and establishes a clean project structure for instructions, Skills, agents, data, tests and generated artifacts. Readers configure permissions, understand sessions and create the initial Git repository. The objective is to make every change inspectable and reproducible from the beginning rather than treating source control and project organization as later production concerns.

## 2.1 Claude Code Architecture

Claude Code operates inside a project workspace where it can inspect files, modify code, run permitted commands and use configured tools. Its behaviour depends on the instructions, permissions and resources available in that environment.

Readers will examine the relationship among the model, command-line interface, filesystem, tools and project instructions. This establishes a mental model for understanding what Claude can see, remember and execute during a session.

## 2.2 Installing and Configuring Claude Code

The development environment will be prepared with Claude Code, Git, Python, Node.js where required and an appropriate code editor. Authentication and basic configuration will be completed without embedding credentials in source files.

A simple verification task will confirm that Claude can inspect the repository, create a file and execute a permitted command. This becomes the baseline environment used throughout the book.

## 2.3 Project Directory Structure

The SDR Lab will separate configuration, source code, Skills, subagents, data, outputs, tests and operational artifacts. Clear separation makes the system easier to understand and prevents generated outputs from becoming confused with application logic.

The project will include directories such as `.claude/`, `config/`, `src/`, `data/`, `outputs/`, `tests/` and `evals/`. The structure will evolve, but its basic responsibilities will remain stable.

## 2.4 Sessions, Context and Working Directories

A Claude Code session has access to a particular working directory, active conversation and selected project instructions. Readers will learn what persists within a session and what disappears when a new session begins.

This distinction prepares the ground for later chapters on memory and durable state. At this stage, each run remains largely independent, making behaviour easier to observe and debug.

## 2.5 Permissions and Execution Modes

Access to files, shell commands, networks and external tools should be explicitly controlled. Convenience should not result in unrestricted authority, even in a learning environment.

Readers will configure sensible local permissions and observe how Claude requests approval for sensitive actions. These controls form the earliest version of the security model developed more fully in Book 3.

## 2.6 Creating the SDR Lab Repository

The initial Git repository will contain the project scaffold, README, dependency files, configuration templates and `.gitignore`. Secrets, generated caches and temporary artifacts will be excluded from source control.

Readers will create the first commit and run the supplied environment test. The repository will then serve as both the implementation workspace and the chronological record of the system's development.
