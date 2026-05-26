# temporary-<task>.md Template

## Document Meta

- Task:
- Effective Scope:
- Related Requirement / Issue / Change:
- Created At:
- Related Long-Term Baseline:
  - `docs/HarnessStack/longterm.md`
- Skip Bias: `conservative | aggressive`
  - `conservative` (default): when an `auto-judge` step's skip criteria are
    ambiguous, agent runs the step.
  - `aggressive`: when skip criteria are ambiguous, agent skips and logs.
  - Affects ONLY `auto-judge` steps. Has no effect on `auto`, `ask-first`,
    or `HITL`.

## Current Task Assessment

- Requirement Clarity:
  - `clear | partially-clear | vague`
- Delivery Target:
  - `<3h test | PoC | Demo | MVP | Alpha | Beta | MMP | RC | GA`
- Risk Level:
  - `low | medium | high`
- Long-Term Knowledge Impact:
  - `none | low | medium | high`

## Adjustments Relative To Long-Term Baseline

### Additions

- Add:

### Temporary Skips

- Skip:

### Strengthened Layers

- Strengthen:

### Weakened Layers

- Weaken:

## Current Final Active Stack

### 1. Primary Workflow Layer

- Active:

### 2. Spec Layer

- Active:

### 3. Execution Discipline Layer

- Active:

### 4. Repository Memory Layer

- Active:

### 5. Harness Enhancement Layer

- Active:

## Execution Rules

- Start with:
- Required intermediate outputs:
- Required completion conditions:

## Conflict Rules Against Long-Term Baseline

### Temporary Contractor Takes Priority On

- Task-level workflow composition
- Task-level execution intensity

### Long-Term Baseline Still Wins On

- Long-term governance rules
- Long-term memory existence
- Long-term quality and safety hard boundaries

## Auto-Skip Log

Lightweight record of `auto-judge` steps the agent skipped during this task,
along with the triggering skip criteria (copied verbatim from the recipe's
Execution Policy table).

Format: `- #<step-id> <step-name> — <triggered skip criteria>`

-

If this section is empty, no `auto-judge` steps were skipped.

## Recipe Invariant Exceptions

Heavyweight record of `auto` or `ask-first` invariants the task is breaking.
These are NOT skip-by-design steps; declaring an exception here is a contract
override.

By default, the active recipe's `Pipeline` ordering, `Merge Gates`,
`Verification Topology`, and `Execution Policy` (for `auto` / `ask-first` /
`HITL` rows) are invariants. Default is deny — silent skips are forbidden.

| Invariant Skipped | Reason | Compensating Action |
|---|---|---|

If this section is empty, no recipe invariants are broken.

## Mechanism Selection

Use this table to choose between the two skip-recording mechanisms above:

| Situation | Use | Why |
|---|---|---|
| Skipping an `auto-judge` step because its Skip Criteria triggered | `Auto-Skip Log` | Skip is by design; the recipe pre-authorized it. Lightweight log preserves the audit trail without ceremony. |
| Skipping any `auto`, `ask-first`, or `HITL` step | `Recipe Invariant Exceptions` | Step is an invariant in the active recipe. Override requires reason + compensating action. |
| Running an `auto-judge` step that the Skip Criteria would normally trigger | nothing to log | Running is the default branch; no record needed. |
| Skipping an `auto-judge` step whose Skip Criteria did NOT trigger | `Recipe Invariant Exceptions` | The skip is outside the recipe's authorized envelope — treat it as a recipe violation. |

Do not mix the two mechanisms. Using a lightweight log entry to bypass an
invariant defeats the audit purpose; using a heavyweight exception entry for
a by-design skip drowns real overrides in noise.

## Exit And Merge Rules

- Invalid when:
- Merge back to RepoMem:
- Trigger long-term baseline review:
