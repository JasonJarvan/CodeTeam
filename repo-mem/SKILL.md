---
name: repo-mem
description: Manage repository memory as persistent architecture, persistent memory, and version-plan documents plus task-scoped temporary docs. Use when initializing repo memory, handling task memory and merges, maintaining long-term knowledge with HITL review, or embedding a memory layer into other workflows.
---

# Repo Mem

## What This Skill Is For

Use this skill to manage repository memory as a long-term knowledge layer.
It governs persistent architecture docs, persistent memory docs, version-plan docs,
task-scoped temp docs, and the merge path between them.

This skill is not a full software-delivery workflow orchestrator.
Use it as a standalone repository-memory skill or embed it as the memory layer inside other workflows.

## When To Use

Use this skill when you need to:

- initialize RepoMem in a repository
- read persistent architecture, memory, and version-plan context for a task
- create or update task-scoped temp docs for requirements, architecture, or memory
- merge task knowledge into long-term docs with HITL review
- maintain long-term repository knowledge with `prune` or `split`
- keep repository-memory practices consistent across workflows

## Core Actions

- `repo-mem init`
  - input: repository root and language configuration
  - output: RepoMem persistent skeleton, config, and template docs
- `repo-mem read <slug>`
  - input: task slug
  - output: context summary from persistent docs and any existing temp docs
- `repo-mem read <slug> --scoped`
  - input: task slug plus a clearer task boundary
  - output: more focused context summary for the active task scope
- `repo-mem capture <slug>`
  - input: task slug and current task context
  - output: created or updated temp docs under `temp/<slug>/`
- `repo-mem capture requirements <slug>`
  - input: task slug and requirement context
  - output: updated `requirements.md`
- `repo-mem capture architecture <slug>`
  - input: task slug and architecture context
  - output: updated `architecture.md`
- `repo-mem capture memory <slug>`
  - input: task slug and memory context
  - output: updated `memory.md`
- `repo-mem merge <slug>`
  - input: task slug at task-closure time
  - output: structured merge suggestions, confirmed writes, updated temp status, and post-merge `git diff`
- `repo-mem merge architecture <slug>`
  - input: task slug
  - output: architecture-only merge suggestions and writes
- `repo-mem merge memory <slug>`
  - input: task slug
  - output: memory-only merge suggestions and writes
- `repo-mem prune [domain]`
  - input: optional domain
  - output: maintenance proposal with suggested removals, rewrites, or cleanup actions
- `repo-mem split [domain]`
  - input: optional domain
  - output: maintenance proposal for restructuring persistent docs

## Hard Rules

- Treat persistent docs as the source of long-term repository truth.
- Treat temp docs as task-scoped working memory only.
- Keep `capture` restricted to `temp/`; do not write long-term docs from `capture`.
- Run `merge` only when a requirement or bugfix task has reached closure.
- Always require HITL confirmation before every `merge`.
- After `merge`, show post-write `git diff` and remind the user they can edit docs directly.
- Keep `prune` and `split` HITL-first; produce proposals before large changes.
- Select `domains` from the repository domain map in persistent architecture docs.
- Let the agent update `domains` silently when task scope changes.
- Keep persistent docs in the repository primary language.
- Treat secondary-language docs as mirrors only; never as the primary fact source.
- Do not let runtime instance docs automatically become skill rules.
- Promote runtime experience into reusable skill rules only through an explicit future promote flow.

## File Layout

Read [references/file-layout.md](./references/file-layout.md) for:

- target-repository standard RepoMem layout
- this repository's self-hosted runtime layout
- the separation between skill package, templates, and runtime docs

## Read These References When Needed

- Read [references/frontmatter.md](./references/frontmatter.md) when creating or updating temp docs.
- Read [references/init-rules.md](./references/init-rules.md) when initializing an existing repository or applying an init proposal.
- Read [references/merge-rules.md](./references/merge-rules.md) when running `merge`, `prune`, or `split`.
- Read [references/workflow-integration.md](./references/workflow-integration.md) when embedding RepoMem into another workflow.
- Read [references/language-policy.md](./references/language-policy.md) when configuring or maintaining multilingual repository memory.
