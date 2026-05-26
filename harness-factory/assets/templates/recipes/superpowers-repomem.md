# Recipe: superpowers-repomem

## Description

- Execution discipline = Superpowers, repository memory = RepoMem. No spec
  layer, no harness enhancement, no primary workflow framework. Primary
  workflow responsibility emerges from Superpowers brainstorming and
  writing-plans; RepoMem provides cross-task persistence.
- Minimum recipe for long-lived solo repositories that need durable
  architecture and decision memory without paying OpenSpec change-cycle cost.

## Layer Assignments

- Primary Workflow Layer: none (emergent — see below)
- Spec Layer: none
- Execution Discipline Layer: Superpowers
- Repository Memory Layer: RepoMem
- Harness Enhancement Layer: none

Emergent Ownership: Superpowers brainstorming and writing-plans carry primary
workflow responsibility. RepoMem does not own workflow — it owns persistence
of context across tasks.

## End-to-End Pipeline

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

- Superpowers.verification-before-completion is the single verification entry
  before requesting-code-review.
- RepoMem has no verification role — it does not gate completion.

## Merge Gates

- RepoMem.merge MUST run after Superpowers.finishing-a-development-branch,
  never before.
- RepoMem.merge is HITL — a human reviews promotion candidates before they
  enter the long-term layer.
- RepoMem.prune / split runs on a different cadence than per-task work.

## Execution Policy

| # | Step | Policy | Skip Criteria (auto-judge only) | Notes |
|---|---|---|---|---|
| 1 | RepoMem.read | auto | — | Read-only context load. Idempotent. |
| 2 | Superpowers.brainstorming | auto-judge | Intent is already `clear` per task contract, or task is a trivial fix / pure refactor. | When skipped, writing-plans consumes the user prompt directly. |
| 3 | RepoMem.capture (open temp docs) | auto | — | Mechanical folder creation. |
| 4 | Superpowers.writing-plans | auto-judge | Single-step task with no branching, or `<3h test` delivery target. | When skipped, agent executes a 1-2 line ad-hoc plan. |
| 5 | using-git-worktrees + executing-plans + TDD | auto-judge | No isolation needed; small change with no parallel work. TDD scope follows plan. | Worktree decision is judged; TDD discipline is not. |
| 6 | RepoMem.capture (continuous) | auto | — | Passive tacit-knowledge recording. |
| 7 | Superpowers.verification-before-completion | auto | — | Behavior verification is non-negotiable. |
| 8 | Superpowers.requesting-code-review | ask-first | — | External visibility: opens a review request. Confirm before triggering. |
| 9 | Superpowers.finishing-a-development-branch | ask-first | — | Multi-step git state change. Confirm scope before executing. |
| 10 | RepoMem.merge | HITL | — | Contract-mandated human review. Never downgradable. |
| 11 | RepoMem.prune / split | auto | — | Periodic hygiene, not per-task. Runs on its own cadence. |

## Suitability Envelope

### Fits

- solo or small-team
- long-lived repositories where architecture and decisions accumulate
- changes that do not need explicit spec boundaries
- risk low to medium

### Does Not Fit

- short-lived or disposable repositories — RepoMem overhead unjustified;
  use `superpowers` instead
- changes that need durable spec boundaries — extend to
  `openspec-superpowers-repomem` instead
- multi-team large-scale coordination — needs a heavier primary workflow

## Compatible Scenarios

- solo × any × long-lived × any
- small-team × any × long-lived × governance=disabled — only when the team
  has explicitly rejected OpenSpec; default small-team scenario enables it

## Incompatible Scenarios

- any × any × short-lived × any
- large-team × any × any × any — large-team requires an active primary
  workflow layer; this recipe leaves Primary emergent

## Delivery Target Compatibility

### Suited For

- PoC, Demo, MVP, Alpha, Beta — minimum-process targets that still benefit
  from cross-task memory

### Not Suited For

- `<3h test` — RepoMem capture overhead is disproportionate; use `superpowers`
- MMP, RC, GA — extend to a recipe with explicit spec layer (e.g.,
  `openspec-superpowers-repomem`) before reaching late delivery targets

## Notes

- This recipe is the canonical add-only step between `superpowers` and
  `openspec-superpowers-repomem`. Typical progression:
  `superpowers` → `superpowers-repomem` → `openspec-superpowers-repomem` →
  further extensions with harness enhancement and primary workflow.
- Default recipe for the solo scenario when the repository is long-lived.
