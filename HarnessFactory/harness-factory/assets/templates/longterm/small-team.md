# longterm-small-team.md Template

## Document Meta

- Repository:
- Effective From:
- Source Template:
  - `harness-factory/assets/templates/longterm/small-team.md`
- Recipe Reference:
  - default small-team combo:
    `harness-factory/assets/templates/recipes/openspec-superpowers-repomem-ecc.md`
  - leaner variant without ECC:
    `harness-factory/assets/templates/recipes/openspec-superpowers-repomem.md`
- Last Updated Because:

## Current Long-Term Assessment

- Collaboration Scale:
  - `small-team`
- Repository Type:
  - `product | research | platform | other`
- Project Horizon:
  - `short-lived | long-lived`
- Long-Term Knowledge Governance:
  - `enabled`

## Current Active Long-Term Baseline

### 1. Primary Workflow Layer

- Default enabled:
  - none by default
- Emergent Ownership:
  - OpenSpec change cycle plus Superpowers brainstorming and writing-plans
    jointly carry primary workflow responsibility.
- Default inactive:
  - `BMAD`
- Upgrade trigger:
  - roadmap planning grows beyond lightweight coordination
  - cross-task coordination cost becomes persistently high

### 2. Spec Layer

- Default enabled:
  - `OpenSpec`
- Default inactive:
  - none by default
- Upgrade trigger:
  - enforce stronger use once collaboration drift appears

### 3. Execution Discipline Layer

- Default enabled:
  - `Superpowers`
- Default inactive:
  - none by default
- Upgrade trigger:
  - add stronger review, verification, and plan discipline for risky work

### 4. Repository Memory Layer

- Default enabled:
  - `RepoMem`
- Default inactive:
  - none by default
- Upgrade trigger:
  - split architecture and memory more aggressively as domains grow

### 5. Harness Enhancement Layer

- Default enabled:
  - `ECC(medium)`
- Default inactive:
  - none by default
- Upgrade trigger:
  - increase guardrails when shared context, safety, and repeatability become painful

> Note: The five cross-layer sections below (Pipeline, Cross-Layer Conflicts,
> Verification Topology, Merge Gates, Suitability Envelope) are rendered
> against the default recipe `openspec-superpowers-repomem-ecc`. If you switch
> `Recipe Reference` to a different recipe (e.g., the leaner variant without
> ECC), re-render these five sections from that recipe before using the
> document.

## Pipeline

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

## Suitability Envelope

### Fits

- 2 to 5 contributors (small-team scale)
- long-lived product or platform repositories
- changes can be sliced into discrete change units
- risk medium to high
- shared context, lightweight pre-commit eval, or dependency security scan are
  valued enough to justify ECC overhead

### Does Not Fit

- pure spike or probe experiments — OpenSpec friction is too high
- short-lived repos — RepoMem overhead is unjustified
- solo, low-stakes — switch scenario subtemplate to `solo.md` and consider
  recipes `openspec-superpowers-repomem` or `superpowers`
- multi-team large-scale coordination — switch to `large-team.md` with a
  primary workflow added (BMAD or GSD)

## Temporary Contractor Boundary Rules

### Temporary Contractor May Adjust

- choose lighter or heavier task-level flow based on clarity and delivery target
- reduce `OpenSpec` intensity for tiny low-risk tasks
- increase `Superpowers` and `ECC` intensity for risky work

### Temporary Contractor May Not Override

- the existence of `OpenSpec`, `RepoMem`, or `Superpowers` as the team baseline
- long-term collaboration and governance rules
- this document's collaboration-scale assumption without full rewrite

## Full Rewrite Conditions

- team shrinks to solo or grows into large-team conditions
- repository shifts into much heavier coordination mode
- default baseline needs permanent heavier planning workflow

## Related Documents

- `docs/HarnessStack/temporary-<task>.md`
- `docs/RepoMem/persist/version-plan.md`
