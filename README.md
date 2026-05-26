<div align="center">

# RepoMem

### Make repositories remember.

**A persistent memory layer for code repositories and coding agents.**

**Compatible with GSD, ECC, OpenSpec, Superpowers, BMAD, gstack, and similar workflows.**

[English](./README.md) / [中文](./README_CN.md)

![AI Agents](https://img.shields.io/badge/AI%20Agents-Repo%20Memory%20Layer-111111?style=flat-square)
![HITL](https://img.shields.io/badge/HITL-Review%20Before%20Long--term%20Writes-0A7B83?style=flat-square)
![Memory Model](https://img.shields.io/badge/Temp-%3E%20Merge%20%3E%20Persist-8A5CF6?style=flat-square)
![Repo-native](https://img.shields.io/badge/Repo--native-Durable%20Memory-2D6A4F?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-black?style=flat-square)
![Stars](https://img.shields.io/github/stars/JasonJarvan/RepoMem?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/JasonJarvan/RepoMem?style=flat-square)

![RepoMem Social Preview](./assets/repomem_social_preview.png)

</div>

RepoMem gives your repository a durable, reviewable place to store:

- architecture knowledge
- long-lived engineering memory
- version planning
- task-scoped working memory

Instead of letting important context live only in chats, agent sessions, or scattered docs, RepoMem keeps that knowledge **inside the repository**, with **HITL review** before long-term updates land.

RepoMem is **not** a full delivery workflow orchestrator.
It is the memory layer you can use on its own or embed into other workflows.

## Workflow Compatibility

RepoMem is natively compatible with GSD, ECC, OpenSpec, Superpowers, BMAD, gstack, and similar workflows.

For the best integrated developer experience, use it with [HarnessStack](https://github.com/JasonJarvan/HarnessStack).

## Why RepoMem

AI coding agents are fast, but repository knowledge decays fast too.

Common failure modes:

- the agent solves the task but forgets the architectural reason
- hard-won debugging lessons stay trapped in chat history
- a repo has docs, but no clear separation between temporary notes and durable truth
- "memory" becomes stale because no one knows what should be promoted or reviewed

RepoMem is designed to solve that gap:

- `persist/architecture/` stores how the repo is structured
- `persist/memory/` stores durable constraints, pitfalls, and rationale
- `persist/version-plan.md` stores future-facing planning
- `temp/<slug>/` stores task-scoped working memory before anything is promoted
- `merge` turns task memory into reviewed long-term knowledge

The result is simple:

**your repository stops depending on fragile conversational memory.**

## What Makes It Different

Most repo documentation systems answer "where do we write things?"

RepoMem answers a harder question:

**what should stay temporary, what should become long-term memory, and how should that promotion happen safely?**

Its core design principles:

- **Repo-native**: knowledge lives in the repository, not in a hidden external memory service
- **Agent-friendly**: optimized for AI-assisted task execution and recovery
- **HITL-first**: long-term writes are reviewed before they become repository truth
- **Separation of memory types**: architecture, memory, plan, and task notes are not mixed together
- **Workflow-agnostic**: works alone or underneath larger delivery systems

## How It Works

### 1. Initialize repo memory

Use `repo-mem init` to create the standard memory structure.

For a new repository, RepoMem initializes the persistent skeleton directly.

For an existing repository, RepoMem uses a proposal-first flow:

1. analyze the repository
2. generate `temp/<slug>/init-proposal.md`
3. let the user review and edit the proposal
4. apply the confirmed proposal
5. if conflicts appear, generate `temp/<slug>/init-conflicts.md`
6. resolve conflicts by `conflict_id`
7. review the resulting `git diff`

### 2. Recover context at task start

Use `repo-mem read <slug>` when starting or resuming work.

RepoMem reads:

- persistent docs
- relevant domain docs
- existing temp docs for the same task slug

It then produces a focused context summary for the active task.

### 3. Capture task-scoped memory during execution

Use `repo-mem capture <slug>` while the work is in progress.

RepoMem updates task docs such as:

- `requirements.md`
- `architecture.md`
- `memory.md`

`capture` writes only to `temp/`.
It does **not** write long-term repository truth directly.

### 4. Promote durable knowledge with review

Use `repo-mem merge <slug>` only after the task reaches closure.

RepoMem:

1. generates structured merge suggestions
2. waits for HITL confirmation
3. writes the confirmed long-term updates
4. updates temp status
5. shows post-write `git diff`

Current merge categories:

- `to architecture`
- `to memory`
- `do not merge`

### 5. Maintain long-term memory without reckless cleanup

Use:

- `repo-mem prune [domain]`
- `repo-mem split [domain]`

These are maintenance actions, not blind destructive commands.
RepoMem generates proposals first, then the human decides what to apply.

## Standard Repository Layout

```text
docs/RepoMem/
├── persist/
│   ├── config.md
│   ├── version-plan.md
│   ├── architecture/
│   │   ├── index.md
│   │   └── <domain>.md
│   └── memory/
│       ├── index.md
│       └── <domain>.md
├── temp/
│   ├── <slug>/
│   │   ├── requirements.md
│   │   ├── architecture.md
│   │   ├── memory.md
│   │   ├── init-proposal.md
│   │   └── init-conflicts.md
│   └── <maintenance-slug>/
│       └── proposal.md
└── multi-lang/
    └── <language>/
```

Use `init-proposal.md` and `init-conflicts.md` only for existing-repository initialization.
They are not part of the normal task-memory trio.

## The Memory Model

### Persistent docs

Long-term repository knowledge:

- `persist/architecture/`
  structure, boundaries, domain map, cross-domain relationships
- `persist/memory/`
  constraints, pitfalls, decision rationale, long-lived implicit knowledge
- `persist/version-plan.md`
  future version planning only

### Temp docs

Task-scoped working memory:

- `requirements.md`
- `architecture.md`
- `memory.md`

This separation is the heart of RepoMem.
Temporary work stays temporary until a human-reviewed merge promotes what actually deserves to persist.

## Language Policy

RepoMem uses **one primary repository language**.

That language governs:

- persistent docs
- temp docs
- merge suggestions
- maintenance proposals
- HITL review items

Secondary languages are mirrors only.
Store them under `multi-lang/<language>/`.
Do not use them as the primary fact source.

## Where RepoMem Fits

RepoMem is best used as a memory layer around other workflows.

Typical integration points:

- before planning: `repo-mem read <slug>`
- during execution: `repo-mem capture <slug>`
- at task closure: `repo-mem merge <slug>`
- during maintenance: `repo-mem prune` / `repo-mem split`

It pairs naturally with agent-heavy workflows because it gives them a durable, auditable memory system instead of relying on chat context alone.

## What RepoMem Is Not

RepoMem is not:

- a vector database
- a chat memory product
- a general knowledge base for everything
- a replacement for your delivery workflow
- a fully automatic long-term write system

It is a **repository-native memory discipline** for AI-assisted software work.

## Current Status

RepoMem currently supports:

- reusable skill packaging
- template-based repository initialization
- self-hosted runtime docs under `docs/RepoMem/`
- task temp docs
- HITL merge flow
- proposal-first initialization for existing repositories
- conflict generation and conflict resolution by decision

Ongoing work is tracked in:

- [docs/RepoMem/persist/version-plan.md](/home/shenzhou/Codes/CodingAgentHarnessSystem/RepoMem/docs/RepoMem/persist/version-plan.md)

## Repository Structure

This repository contains three distinct areas:

```text
repo-mem/
  reusable skill package

repo-mem/assets/templates/
  templates used to initialize other repositories

docs/RepoMem/
  RepoMem managing RepoMem itself
```

## License

RepoMem is licensed under the **MIT License**.

That means you can use, modify, and commercialize it, as long as you keep the copyright notice and license text.

See:

- [LICENSE](/home/shenzhou/Codes/CodingAgentHarnessSystem/RepoMem/LICENSE)

## One-Line Pitch

If AI agents are becoming your new contributors, RepoMem gives your repository something they usually lack:

**durable memory with structure, review, and promotion rules.**
