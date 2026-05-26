# HarnessStack Selection Criteria

## Purpose

Use this reference to decide:

- whether a repository needs a long-term contractor update
- which temporary contractor shape best fits the current task
- which workflow layers should be active for the current task

## Primary Axes

### 1. Long-Term Repository Context

Use these for `docs/HarnessStack/longterm.md`.

- Collaboration scale
  - `solo`: 1 contributor
  - `small-team`: 2 to 5 contributors
  - `large-team`: 6 or more contributors
- Repository type
  - `product`
  - `research`
  - `platform`
  - `other`
- Project horizon
  - `short-lived`
  - `long-lived`

### 2. Temporary Task Context

Use these for `docs/HarnessStack/temporary-<task>.md`.

- Requirement clarity
  - `clear`
  - `partially-clear`
  - `vague`
- Delivery target
  - `<3h test`
  - `PoC`
  - `Demo`
  - `MVP`
  - `Alpha`
  - `Beta`
  - `MMP`
  - `RC`
  - `GA`
- Risk level
  - `low`
  - `medium`
  - `high`
- Long-term knowledge impact
  - `none`
  - `low`
  - `medium`
  - `high`

## Layer Defaults

Use these defaults before task-specific adjustments.

### solo

- Prefer `Superpowers`
- Add `RepoMem` when the repository is long-lived
- Add `OpenSpec` when changes need stable spec boundaries
- Enable `ECC` lightly when memory, hooks, or verification benefit the repository

### small-team

- Prefer `Superpowers + RepoMem`
- Add `OpenSpec` as the normal spec layer once collaboration cost rises
- Add `ECC` at medium strength when shared context and guardrails matter
- Add a stronger primary workflow only when simple execution discipline is no longer enough

### large-team

- Prefer `OpenSpec + RepoMem + ECC` as the default baseline
- Keep `Superpowers` as the execution discipline layer
- Upgrade the primary workflow to a heavier planning system when coordination cost is high

## Requirement Clarity Defaults

### clear

- Minimize workflow count
- Prefer execution-focused flow
- Add spec layer only when delivery target or risk justifies it

### partially-clear

- Add enough structure to stabilize scope before implementation
- Prefer adding `OpenSpec` when the repository does not already make scope explicit

### vague

- Prefer exploration-first flow
- Do not jump directly into implementation-heavy execution
- Upgrade planning and scope-definition layers first

## Delivery Target Modifiers

Use these to increase or decrease process intensity.

- `<3h test`
  - strongly prefer minimum viable process
- `PoC` or `Demo`
  - allow lighter specs and lighter long-term memory updates
- `MVP` or `Alpha`
  - raise the value of explicit scope and verification
- `Beta` or `MMP`
  - require stronger verification and more stable knowledge capture
- `RC` or `GA`
  - require strongest verification, completion, and guardrail intensity

## Scenario × Recipe Composition

Final long-term contract = scenario × recipe. The composition is `union`, not
override (per the add-only principle).

### Authority By Field

- `Document Meta`: filled at generation time by skill
- `Current Long-Term Assessment` (scale / type / horizon / governance):
  authoritative source = scenario
- `Current Active Long-Term Baseline` (per-layer Default enabled / Default
  inactive / Upgrade trigger / Emergent Ownership): authoritative source =
  recipe; scenario contributes scale-level constraints when recipe leaves a
  layer unspecified
- `Pipeline`, `Cross-Layer Conflicts`, `Verification Topology`, `Merge Gates`,
  `Suitability Envelope`: authoritative source = recipe (copy verbatim)
- `Temporary Contractor Boundary Rules`: union of scenario rules and recipe
  rules; on overlap, the stricter rule wins
- `Full Rewrite Conditions`: union of scenario rules and recipe rules

### Add-Only Constraint On Composition

- Composition never removes a layer that the recipe declares Active.
- Composition never removes an `Upgrade trigger` from any source.
- Composition never weakens an invariant from `Pipeline`, `Merge Gates`, or
  `Verification Topology`.

### When Recipe And Scenario Conflict

- If scenario and recipe disagree on whether a layer is Active, recipe wins
  and the conflict MUST be reported to the user. This usually signals that
  the recipe is incompatible with the scenario and a different recipe should
  be picked.
- If scenario implies a Primary framework but recipe leaves Primary as
  Emergent, recipe wins; record the scenario's expectation in the contract's
  `Upgrade trigger` so future progression remains explicit.

## Rewrite Conditions For Long-Term Baseline

Update `docs/HarnessStack/longterm.md` only when one or more of these are true:

- collaboration scale changed materially
- repository type changed materially
- repository horizon changed materially
- default long-term workflow stack changed materially

Otherwise generate only `temporary-<task>.md`.
