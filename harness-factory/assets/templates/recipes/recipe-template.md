# Recipe: <recipe-name>

A `recipe` captures a specific layer combination together with the inter-layer
rules required to make it work. A recipe is orthogonal to scenario
subtemplates: scenarios encode scale defaults, recipes encode layer combos.

Final activation in a target repository = scenario × recipe.

## Naming Convention

- File name: lowercase, hyphen-separated method names.
- Methods listed in canonical layer order: Primary → Spec → Execution →
  Memory → Harness. Within a layer, use the canonical method name.
- Examples: `superpowers.md`, `openspec-superpowers.md`,
  `openspec-superpowers-repomem.md`,
  `bmad-openspec-superpowers-repomem-ecc.md`.

## Recipe Lifecycle (copy-on-write)

- Recipes are immutable once published. To extend a recipe (under the
  `add-only` principle), create a new recipe file whose layer set is a
  superset of the previous one. Do not mutate the published file.
- The previous recipe stays in place forever — references to it remain valid.
- Long-term contracts upgrade by changing their `Recipe Reference` to the new
  superset recipe; this is an extension event, not a rewrite event.

## Description

- One-line summary of the combination and what it is good for.

## Layer Assignments

- Primary Workflow Layer:
- Spec Layer:
- Execution Discipline Layer:
- Repository Memory Layer:
- Harness Enhancement Layer:

If a layer is intentionally inactive, write `none` and add an `Emergent
Ownership` note under Primary if its responsibility is carried by other layers.

## End-to-End Pipeline

Numbered ordered steps. State which layer drives each step and which artifacts
flow across layers.

1.

## Cross-Layer Conflicts

| Overlap | Conflict | Resolution |
|---|---|---|

## Verification Topology

- Which layer's verification fires when, and what each one answers.

## Merge Gates

- Cross-layer sequencing rules (e.g., RepoMem.merge runs only after
  OpenSpec.archive). State HITL points explicitly.

## Execution Policy

A per-step policy table. While `Pipeline` defines order and `Merge Gates`
define hard sequencing, `Execution Policy` defines **per-step runtime mode**:
does the agent run silently, judge whether to skip, announce-and-wait, or hand
off to a human?

Four policy values are defined:

| Policy | Behavior | Skip mechanism |
|---|---|---|
| `auto` | Agent runs the step directly, no announcement, no wait. | Cannot be skipped except via a heavyweight `Recipe Invariant Exception`. |
| `auto-judge` | Agent decides at runtime whether to run or skip. **Does not interrupt the user.** When skipping, agent appends a single line to `temporary-<task>.md § Auto-Skip Log`. | Skipping is by design; lightweight log entry only. |
| `ask-first` | Agent announces what it is about to do (1-2 lines, no body) and waits for user confirmation before executing. Use for steps with external visibility or hard-to-reverse side effects. | Skipping requires a `Recipe Invariant Exception`. |
| `HITL` | Contract-level mandatory human review. Cannot be downgraded by any task-level setting. | Cannot be skipped. |

Required columns:

| # | Step | Policy | Skip Criteria (auto-judge only) | Notes |
|---|---|---|---|---|

- `#`: matches the step number in `End-to-End Pipeline`.
- `Step`: the canonical step name.
- `Policy`: one of `auto | auto-judge | ask-first | HITL`.
- `Skip Criteria`: required when policy is `auto-judge`; states the condition
  under which skipping is legitimate. Leave blank for other policies.
- `Notes`: optional. Use to clarify what "ask-first" needs the user to decide,
  or why an `auto` step has no judgment space.

Recipe-level guidance:

- Default to `auto` for read-only / idempotent / mechanical steps.
- Use `auto-judge` only where the step is **legitimately skippable by design**
  (e.g., brainstorming when intent is already clear, OpenSpec.propose for a
  trivial fix). The Skip Criteria must be objective enough that an agent can
  decide without user input.
- Use `ask-first` for steps whose effects are externally visible (PR review,
  archived change records) or hard to reverse (branch finishing, dependency
  triage).
- Reserve `HITL` for contract-level merge gates already required by
  `Merge Gates`.

## Suitability Envelope

### Fits

-

### Does Not Fit

-

## Compatible Scenarios

List the (collaboration-scale × repository-type × project-horizon × governance)
combinations where this recipe is safe to activate.

-

## Incompatible Scenarios

Where this recipe MUST NOT be used, even if a user requests it.

-

## Delivery Target Compatibility

State which delivery targets this recipe is suited for. Use the same
normalized values as `references/questionnaire.md`:
`<3h test | PoC | Demo | MVP | Alpha | Beta | MMP | RC | GA`.

### Suited For

-

### Not Suited For

-

## Notes

- Implementation notes, known caveats, or links to related recipes.
