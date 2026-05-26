# Recipe: openspec-superpowers-repomem-ecc

## Description

- Spec layer = OpenSpec, execution discipline = Superpowers, repository memory
  = RepoMem, harness enhancement = ECC(medium). No primary workflow framework.
  Primary workflow responsibility emerges from the OpenSpec change cycle plus
  Superpowers brainstorming and planning. ECC supplements with research-first
  context loading, session-state persistence, basic pre-commit verification
  loops, and dependency security scanning.
- This is a strict superset of `openspec-superpowers-repomem`. All invariants
  from that parent recipe carry over verbatim.

## Layer Assignments

- Primary Workflow Layer: none (emergent — see below)
- Spec Layer: OpenSpec
- Execution Discipline Layer: Superpowers
- Repository Memory Layer: RepoMem
- Harness Enhancement Layer: ECC(medium)

Emergent Ownership: OpenSpec change cycle (proposal → specs → tasks → archive)
plus Superpowers brainstorming and writing-plans jointly carry primary workflow
responsibility. ECC supplements with cross-task harness-level plumbing but does
not own primary workflow.

## End-to-End Pipeline

1. ECC.research-first — pull current library / API / pattern docs relevant to
   the task (Context7 or equivalent MCP)
2. RepoMem.read — load long-term architecture and memory as task context
3. Superpowers.brainstorming — clarify vague intent (consumes research-first
   output and RepoMem context)
4. OpenSpec.explore / propose — convert intent into a formal change with specs
5. RepoMem.capture — open task-level temporary docs (requirement, architecture)
6. Superpowers.writing-plans — consume OpenSpec specs and tasks to produce
   executable plan
7. Superpowers.using-git-worktrees + executing-plans + TDD — implement
8. RepoMem.capture (continuous) — record tacit knowledge into temporary memory
9. ECC.session-state.persist (continuous) — persist agent session state across
   restarts; harness-level, distinct from RepoMem
10. ECC.pre-commit-eval — fast mechanical gate (format, lint, smoke evals)
11. ECC.security-scan — run when dependencies change, and again pre-archive
12. Superpowers.verification-before-completion + OpenSpec.verify —
    dual-perspective behavior verification
13. Superpowers.requesting-code-review
14. Superpowers.finishing-a-development-branch
15. OpenSpec.archive — freeze change record (gated by ECC.security-scan when
    dependencies changed)
16. RepoMem.merge (HITL) — promote stable knowledge from temporary to long-term
17. RepoMem.prune / split — periodic hygiene, not per-task

## Cross-Layer Conflicts

| Overlap | Conflict | Resolution |
|---|---|---|
| Early-phase intent convergence | Superpowers.brainstorming vs OpenSpec.explore | brainstorming first when intent is vague; switch to OpenSpec once intent is formalizable as a change intent |
| Plan concept | Superpowers.writing-plans vs OpenSpec.tasks | OpenSpec.tasks defines WHAT contract; writing-plans defines HOW execution; the latter consumes the former |
| Verification | OpenSpec.verify vs Superpowers.verification-before-completion | run both — different lenses |
| Doc sedimentation | OpenSpec change docs vs RepoMem memory | OpenSpec is the authoritative source per change; RepoMem extracts durable lessons at archive time and never duplicates the change record |
| Context bootstrap | ECC.research-first vs Superpowers.brainstorming | research-first is read-only doc lookup; brainstorming consumes its output to shape intent. Run research-first first. |
| State persistence | ECC.session-state vs RepoMem.capture | ECC session-state is harness-level agent state (across restarts); RepoMem.capture is repo-level knowledge artifacts. Do not duplicate; agent runtime state never enters RepoMem. |
| Pre-commit checks | ECC.pre-commit-eval vs Superpowers.verification-before-completion | pre-commit-eval is a fast mechanical gate (format, lint, smoke); verification-before-completion is semantic (did we satisfy the change). Both run; the latter cannot be skipped just because the former passes. |

## Verification Topology

- ECC.pre-commit-eval — "do basic mechanical and smoke checks pass?" (fast)
- ECC.security-scan — "did any dependency / supply-chain risk regress?" (run
  on dependency change and pre-archive)
- OpenSpec.verify — "did we deliver what the spec promised?"
- Superpowers.verification-before-completion — "is the implemented behavior
  actually correct?"
- All four lenses are required for changes that touch dependencies; the first
  three are required for code-only changes.
- A change cannot enter `finishing-a-development-branch` unless OpenSpec.verify
  and Superpowers.verification-before-completion pass.
- A change cannot enter `OpenSpec.archive` unless ECC.security-scan passes when
  dependencies changed in this change.

## Merge Gates

- RepoMem.merge MUST run after OpenSpec.archive, never before.
- ECC.security-scan MUST pass before OpenSpec.archive whenever the change
  touches dependencies.
- RepoMem.merge is HITL — a human reviews promotion candidates before they
  enter the long-term layer.
- RepoMem.prune / split runs on a different cadence than per-task work.
- ECC.session-state persistence is continuous and is never gated by a merge.

## Execution Policy

| # | Step | Policy | Skip Criteria (auto-judge only) | Notes |
|---|---|---|---|---|
| 1 | ECC.research-first | auto | — | Read-only doc fetch. Idempotent. |
| 2 | RepoMem.read | auto | — | Read-only context load. |
| 3 | Superpowers.brainstorming | auto-judge | Intent is already `clear` per task contract, or task is a trivial fix / pure refactor. | When skipped, OpenSpec.explore consumes the user prompt directly. |
| 4 | OpenSpec.explore / propose | auto-judge | Trivial fix / pure refactor / `<3h test` / declared spike with no spec impact. | Skipping #4 implies skipping #15 (archive) — log both together. |
| 5 | RepoMem.capture (open temp docs) | auto | — | Mechanical folder creation. |
| 6 | Superpowers.writing-plans | auto-judge | OpenSpec.tasks already lists atomic steps that map 1:1 to execution. | When skipped, agent executes OpenSpec.tasks directly. |
| 7 | using-git-worktrees + executing-plans + TDD | auto-judge | No isolation needed; small change with no parallel work. TDD scope follows plan. | Worktree decision is judged; TDD discipline is not. |
| 8 | RepoMem.capture (continuous) | auto | — | Passive tacit-knowledge recording. |
| 9 | ECC.session-state.persist (continuous) | auto | — | Harness-layer state persistence. Never gated. |
| 10 | ECC.pre-commit-eval | auto | — | Mechanical gate (format, lint, smoke). Tool-driven. |
| 11 | ECC.security-scan | ask-first | — | Findings require accept-vs-fix value judgment — present results, await direction. Skip when the change touches no dependencies (declare via `Recipe Invariant Exception`). |
| 12 | verification-before-completion + OpenSpec.verify | auto | — | Both lenses required. Read-only behavior + spec verification. |
| 13 | Superpowers.requesting-code-review | ask-first | — | External visibility: opens a review request to humans. Confirm before triggering. |
| 14 | Superpowers.finishing-a-development-branch | ask-first | — | Multi-step git state change. Confirm scope before executing. |
| 15 | OpenSpec.archive | ask-first | — | Half-irreversible: freezes change record. Gated by #11 when deps changed. Confirm completeness first. |
| 16 | RepoMem.merge | HITL | — | Contract-mandated human review. Never downgradable. |
| 17 | RepoMem.prune / split | auto | — | Periodic hygiene, not per-task. Runs on its own cadence. |

## Suitability Envelope

### Fits

- small-team (canonical) and lower end of large-team adopters
- long-lived repositories
- changes can be sliced into discrete change units
- risk medium to high
- shared context, lightweight pre-commit eval, or dependency security scan are
  valued enough to justify ECC overhead

### Does Not Fit

- pure spike or probe experiments — OpenSpec friction is too high
- short-lived repos — RepoMem overhead is unjustified
- solo, low-stakes — ECC(medium) overhead is disproportionate; prefer
  `openspec-superpowers-repomem` or `superpowers` instead
- multi-team large-scale coordination — still requires a heavier primary
  workflow above this combo

## Compatible Scenarios

- small-team × product × long-lived × governance=enabled — canonical default
  for the small-team scenario subtemplate
- small-team × platform × long-lived × governance=enabled

## Incompatible Scenarios

- any × any × short-lived × any
- solo × any × any × any — ECC(medium) overhead is disproportionate; use
  `openspec-superpowers-repomem` (no ECC) or `superpowers` (single method)
- large-team × any × any × any — large-team requires an active primary
  workflow layer; this recipe leaves Primary emergent

## Delivery Target Compatibility

### Suited For

- MVP, Alpha, Beta, MMP, RC, GA — these benefit from explicit change specs,
  HITL merge discipline, and ECC's pre-commit and security guardrails

### Not Suited For

- `<3h test` — OpenSpec proposal/specs/tasks overhead is disproportionate
- PoC, Demo — RepoMem long-term layer + ECC overhead is unjustified unless
  the PoC is expected to graduate

## Notes

- This recipe is the canonical default for
  `assets/templates/longterm/small-team.md`. The leaner variant without ECC is
  the parent recipe `openspec-superpowers-repomem.md`.
- ECC(medium) concretely includes: research-first via Context7 or equivalent
  MCP, cross-session memory persistence, team-shared skill discovery, basic
  pre-commit verification loops, and security scan on dependency changes. The
  authoritative definition will live in `references/ecc-intensity.md` (B6,
  pending). Until that file ships, this Notes section is the source of truth
  for the medium tier.
- Parent recipe in copy-on-write lineage: `openspec-superpowers-repomem.md`.
  All invariants there carry over verbatim; this recipe only adds.
- Add-only upgrade path from this recipe: when team scale crosses small-team,
  extend to `<primary>-openspec-superpowers-repomem-ecc.md` where `<primary>`
  is the chosen primary workflow (BMAD or GSD per the Session B init-by-scale
  rule).
