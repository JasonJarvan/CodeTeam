# Recipe: openspec-superpowers-repomem

## Description

- Spec layer = OpenSpec, execution discipline = Superpowers, repository memory
  = RepoMem. No primary workflow framework and no harness enhancement layer.
  Primary workflow responsibility emerges from the OpenSpec change cycle plus
  Superpowers brainstorming and planning.

## Layer Assignments

- Primary Workflow Layer: none (emergent — see below)
- Spec Layer: OpenSpec
- Execution Discipline Layer: Superpowers
- Repository Memory Layer: RepoMem
- Harness Enhancement Layer: none

Emergent Ownership: OpenSpec change cycle (proposal → specs → tasks → archive)
plus Superpowers brainstorming and writing-plans jointly carry primary workflow
responsibility.

## End-to-End Pipeline

1. RepoMem.read — load long-term architecture and memory as task context
2. Superpowers.brainstorming — clarify vague intent
3. OpenSpec.explore / propose — convert intent into a formal change with specs
4. RepoMem.capture — open task-level temporary docs (requirement, architecture)
5. Superpowers.writing-plans — consume OpenSpec specs and tasks to produce
   executable plan
6. Superpowers.using-git-worktrees + executing-plans + TDD — implement
7. RepoMem.capture (continuous) — record tacit knowledge into temporary memory
8. Superpowers.verification-before-completion + OpenSpec.verify — dual-perspective
   verification
9. Superpowers.requesting-code-review
10. Superpowers.finishing-a-development-branch
11. OpenSpec.archive — freeze change record
12. RepoMem.merge (HITL) — promote stable knowledge from temporary to long-term
13. RepoMem.prune / split — periodic hygiene, not per-task

## Cross-Layer Conflicts

| Overlap | Conflict | Resolution |
|---|---|---|
| Early-phase intent convergence | Superpowers.brainstorming vs OpenSpec.explore | brainstorming first when intent is vague; switch to OpenSpec once intent is formalizable as a change intent |
| Plan concept | Superpowers.writing-plans vs OpenSpec.tasks | OpenSpec.tasks defines WHAT contract; writing-plans defines HOW execution; the latter consumes the former |
| Verification | OpenSpec.verify vs Superpowers.verification-before-completion | run both — different lenses |
| Doc sedimentation | OpenSpec change docs vs RepoMem memory | OpenSpec is the authoritative source per change; RepoMem extracts durable lessons at archive time and never duplicates the change record |

## Verification Topology

- OpenSpec.verify — "did we deliver what the spec promised?"
- Superpowers.verification-before-completion — "is the implemented behavior
  actually correct?"
- Both run before requesting-code-review.
- A change cannot enter finishing-a-development-branch unless both pass.

## Merge Gates

- RepoMem.merge MUST run after OpenSpec.archive, never before.
- RepoMem.merge is HITL — a human reviews promotion candidates before they
  enter the long-term layer.
- RepoMem.prune / split runs on a different cadence than per-task work.

## Execution Policy

| # | Step | Policy | Skip Criteria (auto-judge only) | Notes |
|---|---|---|---|---|
| 1 | RepoMem.read | auto | — | Read-only context load. Idempotent. |
| 2 | Superpowers.brainstorming | auto-judge | Intent is already `clear` per task contract, or task is a trivial fix / pure refactor. | When skipped, OpenSpec.explore consumes the user prompt directly. |
| 3 | OpenSpec.explore / propose | auto-judge | Trivial fix / pure refactor / `<3h test` / declared spike with no spec impact. | Skipping #3 implies skipping #11 (archive) — log both together. |
| 4 | RepoMem.capture (open temp docs) | auto | — | Mechanical folder creation. |
| 5 | Superpowers.writing-plans | auto-judge | OpenSpec.tasks already lists atomic steps that map 1:1 to execution. | When skipped, agent executes OpenSpec.tasks directly. |
| 6 | using-git-worktrees + executing-plans + TDD | auto-judge | No isolation needed; small change with no parallel work. TDD scope follows plan. | Worktree decision is judged; TDD discipline is not. |
| 7 | RepoMem.capture (continuous) | auto | — | Passive tacit-knowledge recording. |
| 8 | verification-before-completion + OpenSpec.verify | auto | — | Both lenses required. Read-only behavior + spec verification. |
| 9 | Superpowers.requesting-code-review | ask-first | — | External visibility: opens a review request. Confirm before triggering. |
| 10 | Superpowers.finishing-a-development-branch | ask-first | — | Multi-step git state change. Confirm scope before executing. |
| 11 | OpenSpec.archive | ask-first | — | Half-irreversible: freezes the change record. Confirm completeness first. |
| 12 | RepoMem.merge | HITL | — | Contract-mandated human review. Never downgradable. |
| 13 | RepoMem.prune / split | auto | — | Periodic hygiene, not per-task. Runs on its own cadence. |

## Suitability Envelope

### Fits

- solo or small-team
- long-lived repositories
- changes can be sliced into discrete change units
- risk medium to high

### Does Not Fit

- pure spike or probe experiments — OpenSpec friction is too high
- short-lived repos — RepoMem overhead is unjustified
- multi-team large-scale coordination — needs a heavier primary workflow above
  this combo

## Compatible Scenarios

- small-team × product × long-lived × governance=enabled
- small-team × platform × long-lived × governance=enabled
- solo × product × long-lived × governance=enabled — only when the user
  explicitly opts into OpenSpec discipline; default solo scenario disables
  OpenSpec

## Incompatible Scenarios

- any × any × short-lived × any
- large-team × any × any × any — large-team requires an active primary
  workflow layer; this recipe leaves Primary emergent

## Delivery Target Compatibility

### Suited For

- MVP, Alpha, Beta, MMP, RC, GA — these benefit from explicit change specs
  and HITL merge discipline

### Not Suited For

- `<3h test` — OpenSpec proposal/specs/tasks overhead is disproportionate
- PoC, Demo — RepoMem long-term layer maintenance overhead is unjustified
  unless the PoC is expected to graduate

## Notes

- This recipe is the closest published cousin of `assets/templates/longterm/small-team.md`
  with `ECC(medium)` removed. Use this recipe when the team has rejected
  harness-level enhancement and prefers a leaner stack.
