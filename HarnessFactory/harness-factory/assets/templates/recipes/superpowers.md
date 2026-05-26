# Recipe: superpowers

## Description

- Execution discipline only. No spec layer, no repository memory, no harness
  enhancement, no primary workflow framework. Primary workflow responsibility
  emerges from Superpowers brainstorming and writing-plans.
- Smallest viable recipe. Recommended starting point for brand-new projects
  with vague requirements; under add-only progression, all richer recipes
  build on this one.

## Layer Assignments

- Primary Workflow Layer: none (emergent — see below)
- Spec Layer: none
- Execution Discipline Layer: Superpowers
- Repository Memory Layer: none
- Harness Enhancement Layer: none

Emergent Ownership: Superpowers brainstorming and writing-plans carry primary
workflow responsibility for new projects with vague intent.

## End-to-End Pipeline

1. Superpowers.brainstorming — clarify vague intent
2. Superpowers.writing-plans — produce executable plan
3. Superpowers.using-git-worktrees + executing-plans + TDD — implement
4. Superpowers.verification-before-completion — verify behavior
5. Superpowers.requesting-code-review
6. Superpowers.finishing-a-development-branch

## Cross-Layer Conflicts

- Single-layer recipe; no cross-layer conflicts apply.

## Verification Topology

- Superpowers.verification-before-completion is the single verification entry
  before requesting-code-review.

## Merge Gates

- No cross-layer merge gate. Branch finishing is the only completion event.

## Execution Policy

| # | Step | Policy | Skip Criteria (auto-judge only) | Notes |
|---|---|---|---|---|
| 1 | Superpowers.brainstorming | auto-judge | Intent is already `clear` per `temporary-<task>.md § Current Task Assessment`, or the task is a trivial fix / pure refactor. | When skipped, downstream writing-plans consumes the user prompt directly. |
| 2 | Superpowers.writing-plans | auto-judge | Single-step task with no branching, or `<3h test` delivery target. | When skipped, agent executes a 1-2 line ad-hoc plan in conversation. |
| 3 | using-git-worktrees + executing-plans + TDD | auto-judge | No isolation needed (small change, no parallel work) — may execute on current branch. TDD scope follows the plan. | Worktree decision is judged; TDD discipline is not. |
| 4 | Superpowers.verification-before-completion | auto | — | Behavior verification is non-negotiable in this recipe. |
| 5 | Superpowers.requesting-code-review | ask-first | — | External visibility: opens a review request to humans. Confirm before triggering. |
| 6 | Superpowers.finishing-a-development-branch | ask-first | — | Changes git state across multiple operations (merge, push, branch delete). Confirm scope before executing. |

## Suitability Envelope

### Fits

- brand-new projects with vague requirements
- solo or small-team
- short-lived or long-lived (RepoMem can be added later under add-only)
- exploration-first work where formal change specs would add friction

### Does Not Fit

- projects whose changes already need durable spec boundaries — extend to
  `openspec-superpowers` instead
- multi-team coordination — extend with a primary workflow layer

## Compatible Scenarios

- solo × any × any × any
- small-team × any × any × any
- (large-team is incompatible — large-team requires a primary workflow layer
  to be active)

## Incompatible Scenarios

- large-team × any × any × any

## Delivery Target Compatibility

### Suited For

- `<3h test`, PoC, Demo, MVP — minimum-process targets benefit most
- Alpha, Beta — still appropriate when changes do not need explicit specs

### Not Suited For

- MMP, RC, GA — extend to a recipe with explicit spec layer (e.g.,
  `openspec-superpowers`) before reaching late delivery targets

## Notes

- This recipe is the canonical add-only starting point. Typical progression:
  `superpowers` → `openspec-superpowers` → `openspec-superpowers-repomem` →
  further extensions with harness enhancement and primary workflow.
