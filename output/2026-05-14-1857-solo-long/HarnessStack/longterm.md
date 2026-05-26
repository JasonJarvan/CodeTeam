# longterm.md

## Document Meta

- Repository: HarnessFactory
- Effective From: 2026-05-13
- Source Template: `harness-factory/assets/templates/longterm/solo.md`
- Recipe Reference: `harness-factory/assets/templates/recipes/superpowers-repomem.md`
- Last Updated Because: initial long-term contract; solo + long-lived methodology repo needs cross-task memory but no spec layer; renamed repository identity to HarnessFactory per v0.3 redesign (2026-05-14)

## Current Long-Term Assessment

- Collaboration Scale: `solo`
- Repository Type: `research`
- Project Horizon: `long-lived`
- Long-Term Knowledge Governance: `enabled`

## Current Active Long-Term Baseline

### 1. Primary Workflow Layer

- Default enabled: none
- Emergent Ownership: Superpowers brainstorming and writing-plans carry primary workflow responsibility.
- Default inactive: `BMAD`, `gstack`, `GSD`
- Upgrade trigger:
  - repository acquires a roadmap-heavy delivery mode
  - task portfolio grows past what execution discipline alone can carry

### 2. Spec Layer

- Default enabled: none
- Default inactive: `OpenSpec`
- Upgrade trigger:
  - a task requires stable change boundaries
  - delivery target reaches `MVP` or above
  - task risk or scope makes chat-only agreement unsafe

### 3. Execution Discipline Layer

- Default enabled: `Superpowers`
- Default inactive: none
- Upgrade trigger:
  - raise verification and review intensity when risk rises

### 4. Repository Memory Layer

- Default enabled: `RepoMem`
- Default inactive: none
- Upgrade trigger:
  - long-term memory pressure requires `RepoMem.prune / split`
  - memory governance needs harden into `ECC` hooks

### 5. Harness Enhancement Layer

- Default enabled: none
- Default inactive: `ECC`, `ECC(light)`
- Upgrade trigger:
  - agent context quality, safety, or repeatability becomes a recurring problem
  - memory or verification loops would benefit from harness-level hooks

## Pipeline

1. RepoMem.read — load long-term architecture and memory as task context
2. Superpowers.brainstorming — clarify vague intent
3. RepoMem.capture — open task-level temporary docs (requirement, architecture)
4. Superpowers.writing-plans — produce executable plan
5. Superpowers.using-git-worktrees + executing-plans + TDD — implement
6. RepoMem.capture (continuous) — record tacit knowledge into temporary memory
7. Superpowers.verification-before-completion — verify behavior
8. Superpowers.requesting-code-review
9. Superpowers.finishing-a-development-branch
10. RepoMem.merge (HITL) — promote stable knowledge from temporary to long-term
11. RepoMem.prune / split — periodic hygiene, not per-task

## Cross-Layer Conflicts

| Overlap | Conflict | Resolution |
|---|---|---|
| Plan vs memory | Superpowers.writing-plans vs RepoMem temporary requirement doc | writing-plans defines HOW; RepoMem temporary doc records WHY/context; never duplicate plan steps into memory |
| Verification vs memory | Superpowers.verification-before-completion vs RepoMem.merge | verification gates branch completion; RepoMem.merge runs after branch finishing, never as part of verification |
| Doc sedimentation | task-level temporary memory vs long-term memory | temporary memory is authoritative during the task; long-term memory only accepts content via the HITL merge step |

## Verification Topology

- Superpowers.verification-before-completion is the single verification entry before requesting-code-review.
- RepoMem has no verification role — it does not gate completion.

## Merge Gates

- RepoMem.merge MUST run after Superpowers.finishing-a-development-branch, never before.
- RepoMem.merge is HITL — review promotion candidates before they enter the long-term layer.
- RepoMem.prune / split runs on a different cadence than per-task work.

## Suitability Envelope

### Fits

- one active contributor
- long-lived methodology / research repository where decisions accumulate
- changes that do not need formal spec boundaries

### Does Not Fit

- multi-contributor coordination
- tasks that require durable change specs — extend to `openspec-superpowers-repomem`
- short-lived spikes — drop to `superpowers` for that task via the temporary contract

## Temporary Contractor Boundary Rules

### Temporary Contractor May Adjust

- add `OpenSpec` for a single task
- raise or lower `Superpowers` intensity
- enable lightweight `ECC` for a task
- skip `RepoMem.capture` for trivial `<3h test` tasks (still must read long-term memory)

### Temporary Contractor May Not Override

- the existence of long-term repository memory
- long-term governance and safety constraints
- pipeline ordering, merge gates, and verification topology — recipe invariants;
  exceptions require a declared `Recipe Invariant Exceptions` section with reason and compensating action
- this document's collaboration-scale assumption without full rewrite

## Full Rewrite Conditions

- repository moves from solo to team collaboration
- repository horizon flips to short-lived
- default primary workflow needs to become permanently heavier

(Note: switching from `superpowers-repomem` to a superset recipe such as `openspec-superpowers-repomem` is an extension under add-only — update `Recipe Reference` in place; not a full rewrite.)

## Related Documents

- `docs/HarnessStack/temporary-<task>.md`
- `docs/RepoMem/persist/version-plan.md`
