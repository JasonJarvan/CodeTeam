# Workflow Integration

Use RepoMem as a memory layer around other workflows, not as a replacement for their full delivery logic.

## Typical Integration Points

- Before task planning:
  - run `repo-mem read <slug>` to recover persistent and temp context
- During task execution:
  - run `repo-mem capture <slug>` to keep temp docs current
- At task closure:
  - run `repo-mem merge <slug>`
- During long-term maintenance:
  - run `repo-mem prune [domain]`
  - run `repo-mem split [domain]`

## Common Pairings

- With OpenSpec:
  - OpenSpec defines change scope and formal specs
  - RepoMem preserves long-term repository knowledge and task memory
- With Superpowers:
  - Superpowers enforces execution discipline
  - RepoMem preserves architecture and memory context before and after execution
- With GSD, BMAD, or gstack:
  - those workflows can orchestrate broader planning or delivery
  - RepoMem can remain the repository-memory layer underneath

## Boundary

- Do not treat RepoMem as the primary scope-definition system for a change.
- Do not let external workflows bypass RepoMem's HITL merge rules when writing long-term knowledge.
