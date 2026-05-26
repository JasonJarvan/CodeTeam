# longterm.md Template

## Document Meta

- Repository:
- Effective From:
- Source Template:
- Recipe Reference:
  - Single value. The active recipe path only. Fallback / downgrade options
    (e.g., leaner variant when tooling is incomplete) belong in the recipe's
    own Notes or the activation kit README, not in this field.
- OpenSpec Root:
  - Default: `./openspec/`. Recommended when the repo follows OpenSpec's
    upstream convention.
  - Alternative: `docs/openspec/`. Recommended when other method-layer
    artifacts (RepoMem, HarnessStack) already live under `docs/`, so
    method-layer co-location is preferred over OpenSpec's upstream default.
  - Leave blank if the Spec Layer is not OpenSpec.
- Last Updated Because:

## Current Long-Term Assessment

- Collaboration Scale:
  - `solo | small-team | large-team`
- Repository Type:
  - `product | research | platform | other`
- Project Horizon:
  - `short-lived | long-lived`
- Long-Term Knowledge Governance:
  - `enabled | disabled`

## Current Active Long-Term Baseline

### 1. Primary Workflow Layer

- Default enabled:
- Emergent Ownership:
  - Use this field when Primary is `none` but the responsibility is jointly
    carried by other layers (for example, OpenSpec change cycle plus
    Superpowers brainstorming/writing-plans). Otherwise leave blank.
- Default inactive:
- Upgrade trigger:

### 2. Spec Layer

- Default enabled:
- Default inactive:
- Upgrade trigger:

### 3. Execution Discipline Layer

- Default enabled:
- Default inactive:
- Upgrade trigger:

### 4. Repository Memory Layer

- Default enabled:
- Default inactive:
- Upgrade trigger:

### 5. Harness Enhancement Layer

- Default enabled:
- Default inactive:
- Upgrade trigger:

## Pipeline

Numbered ordered steps describing how the active layers chain end-to-end. Pull
from the `End-to-End Pipeline` of the chosen recipe. If no recipe is chosen,
state explicitly that the contract is incomplete.

1.

## Cross-Layer Conflicts

Pull from the chosen recipe. Lists overlap points and the resolution rule.

| Overlap | Conflict | Resolution |
|---|---|---|

## Verification Topology

State which verification fires from which layer and what each one answers.
Pull from the chosen recipe.

-

## Merge Gates

Cross-layer sequencing rules and HITL points. Pull from the chosen recipe.

-

## Execution Policy

Per-step runtime mode (`auto | auto-judge | ask-first | HITL`). Copy verbatim
from the chosen recipe's `Execution Policy` table — do not invent values here.

| # | Step | Policy | Skip Criteria (auto-judge only) | Notes |
|---|---|---|---|---|

Semantics:

- `auto` — agent runs the step directly, no announcement, no wait.
- `auto-judge` — agent decides at runtime whether to run or skip. **Does not
  interrupt the user.** Skip decisions are logged in
  `temporary-<task>.md § Auto-Skip Log` (one line per skip).
- `ask-first` — agent announces (1–2 lines) and waits for user confirmation
  before executing. Use for externally visible or hard-to-reverse side effects.
- `HITL` — contract-level mandatory human review. Not downgradable by any
  task-level setting.

Skipping `auto` or `ask-first` steps requires a heavyweight
`Recipe Invariant Exception` in the task contract. Skipping `auto-judge` steps
requires only a lightweight `Auto-Skip Log` line. See
`temporary-<task>.md § Mechanism Selection`.

## Suitability Envelope

### Fits

-

### Does Not Fit

-

## Temporary Contractor Boundary Rules

### Temporary Contractor May Adjust

- Task-level workflow composition
- Task-level intensity of spec, review, and verification
- Task-level temporary additions or skips inside the allowed baseline

### Temporary Contractor May Not Override

- Long-term repository memory existence
- Long-term quality and safety hard constraints
- Long-term default governance decisions unless this document is fully rewritten
- Pipeline ordering, Merge Gates, and Verification Topology are recipe-level
  invariants. The temporary contractor MAY skip one of them only by declaring
  the exception in its `Recipe Invariant Exceptions` section, with reason and
  compensating action. Default is deny — silent skips are forbidden.

## Full Rewrite Conditions

- Collaboration scale changes materially
- Repository type changes materially
- The repository moves into a new long-term delivery mode
- The default workflow stack changes at the long-term level

(Note: under the add-only principle, switching from one recipe to a superset
recipe is an extension, not a rewrite. Update `Recipe Reference` in place; do
not trigger a full rewrite review.)

## Related Documents

- `docs/HarnessStack/temporary-<task>.md`
- `docs/RepoMem/persist/version-plan.md`
- Related RepoMem architecture and memory docs

## Cross-Method Invariants

These rules bind HarnessStack to its companion methods. They are not part of
any single layer and therefore live here at the long-term contract level.

- **Single task identifier.** When the active recipe includes both OpenSpec
  (Spec Layer) and RepoMem (Repository Memory Layer), the OpenSpec `change-id`,
  the RepoMem `<slug>`, and the HarnessStack `<task>` MUST be the same string:
  `<task>` = `change-id` = `<slug>`. Diverging on naming defeats per-task
  cross-referencing across the three method layers.
- **No content duplication across per-task document sets.** OpenSpec change
  docs (`openspec/changes/<id>/`), RepoMem temp docs
  (`docs/RepoMem/temp/<slug>/`), and the HarnessStack per-task contract
  (`docs/HarnessStack/temporary-<task>.md`) each answer a distinct question
  and MUST NOT restate each other's content. The reviewer at `RepoMem.merge`
  rejects (deletes, does not merge) any temp content that duplicates the
  archived OpenSpec record.
- Divergence from either rule requires a `Recipe Invariant Exception` in the
  task contract with reason and compensating action.
