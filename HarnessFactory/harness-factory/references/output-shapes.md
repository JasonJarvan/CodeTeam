# HarnessStack Output Shapes

## Purpose

Use this reference to keep outputs consistent after the question flow is complete.

## Output Destination

Every factory run emits one bundle under `./output/`. The bundle's inner
directory is named `HarnessStack/` so it can be copied directly to
`<target-repo>/docs/HarnessStack/` without renaming.

```
./output/{YYYY-MM-DD-HHmm}-{stack}/HarnessStack/
├── README.md                    # AI distillation index (rendered from output-readme-template.md)
├── longterm.md                  # core long-term contract
├── temporary-<task>.md          # task-level patch (when there is a current task)
└── _toUser/
    └── README.md                # full human-facing usage manual (rendered from to-user-readme-template.md)
```

### Why version-plan Is NOT In The Bundle

Per v0.3.1 decision: a HarnessStack contract and a RepoMem-style version
plan are orthogonal layers. Bundling a version-plan skeleton inside the
HarnessStack output would force target repositories to adopt RepoMem-like
conventions whether or not they use RepoMem. Target repositories that want
to track their stack's evolution maintain a version-plan in whatever memory
area fits them (see the bundle's `_toUser/README.md § Tracking HarnessStack
Evolution` for placement guidance).

### Why The Directory Is `_toUser/`

The `_` prefix preserves the convention that an underscore-prefixed
directory is auxiliary, not part of the active contract surface. `toUser`
names the audience: the human operator of the target repository. This
contrasts with `README.md` (audience: AI distillation) and `longterm.md`
(audience: authoritative contract, read by both).

### Run Directory Naming

- Time precision: `YYYY-MM-DD-HHmm` (minute-level).
- Stack segment: `{stack}` — the active layer composition, hyphen-joined in
  layer order (Primary → Spec → Execution → Memory → Harness). Inactive
  layers are omitted.
  - Base form equals the recipe slug (e.g., `superpowers-repomem`,
    `openspec-superpowers-repomem`).
  - Layer-level strength qualifiers are encoded by replacing the layer name
    with `<layer><Strength>` in camelCase. Example: a stack using
    `ECC(medium)` renders as `eccMedium`; `ECC(light)` renders as `eccLight`.
- Examples:
  - `2026-05-15-1530-superpowers-repomem`
  - `2026-05-15-1612-openspec-superpowers-repomem-eccMedium`

### Why Scale / Horizon / Type Are NOT In The Path

Scale and horizon are captured in the contract metadata
(`longterm.md § Current Long-Term Assessment`) and act as scenario
constraints. Given a chosen `{stack}`, they do not alter layer activation —
two runs with the same `{stack}` but different scale/horizon produce
byte-identical layer activation. Repository type is a recipe veto filter
and similarly does not positively select layers (see
`selection-criteria.md § Layer Defaults`). Putting the stack composition
in the path instead makes each bundle directory immediately
self-describing: the path tells you what is inside.

## Output Modes

> Modes below describe the **logical contracts** that get produced. Their
> physical files land first under `./output/<run>/HarnessStack/` (see
> § Output Destination), then are copied to `<target-repo>/docs/HarnessStack/`
> on deployment. The paths shown below use the target-side form for
> readability; the factory-side path is the same filename under
> `./output/<run>/HarnessStack/`.

### Mode A: Temporary Contract Only

Use when:

- `docs/HarnessStack/longterm.md` already exists, and
- no long-term rewrite condition is triggered

Required outputs:

- one complete `docs/HarnessStack/temporary-<task>.md`

### Mode B: Long-Term Contract And Temporary Contract

Use when:

- `docs/HarnessStack/longterm.md` does not exist, or
- long-term rewrite conditions are clearly triggered

Required outputs:

- one complete `docs/HarnessStack/longterm.md`
- one complete `docs/HarnessStack/temporary-<task>.md` when there is a current task

### Mode C: Long-Term Rewrite Suggestion

Use when:

- current evidence suggests the long-term baseline may be wrong, but
- the information is not strong enough to rewrite it safely

Required outputs:

- a recommendation in conversation
- optionally a temporary contract for the current task

Do not silently rewrite `longterm.md` in this mode.

## Long-Term Output Shape

The generated `longterm.md` must contain:

1. source template and update metadata
2. long-term repository assessment
3. full active five-layer baseline
4. temporary contractor boundary rules
5. full rewrite conditions

Field-level rules:

- `Recipe Reference` MUST be exactly one path — the currently active recipe.
  Downgrade or fallback options live in the recipe's own Notes or the
  activation kit README, never here. Switching recipes is a single-line edit
  plus a `Last Updated Because` entry, not a multi-value field.

### Single-File vs Index-Plus-Hooks

Pick output form based on the rendered length of the long-term contract:

| Form | When to use | Layout |
|---|---|---|
| Single file | Total rendered length ≤ ~400 lines | One `docs/HarnessStack/longterm.md` containing every section in full. |
| Index + hooks | Total rendered length > ~400 lines | `docs/HarnessStack/longterm.md` is an index (TOC + 1-2 line summary per section + pointer); detailed sections live under `docs/HarnessStack/longterm/<section>.md`. |

Threshold rationale: ~400 lines is the boundary where a single Markdown file
stops being scannable in one view. Below the threshold, splitting adds
navigation cost without payoff; above it, progressive disclosure (the
skill-creator pattern) reduces cognitive load.

When using index + hooks:

- The index file MUST contain `Document Meta`, `Current Long-Term Assessment`,
  and `Cross-Method Invariants` in full — these are read on every task.
- Sections that may exceed ~80 lines (Pipeline, Cross-Layer Conflicts,
  Verification Topology, Merge Gates, Execution Policy, Suitability Envelope,
  Temporary Contractor Boundary Rules, Full Rewrite Conditions) are
  candidates for extraction. Extract only those that actually do exceed the
  threshold; leave shorter ones inline.
- Each extracted section becomes `docs/HarnessStack/longterm/<section>.md`,
  with the index showing a 1-2 line summary and a relative link.
- The target repo owns synchronization between index and hooks; the factory's
  job is to emit a consistent initial state. The target repo MAY feed back
  drift discoveries to the factory.

Choose form deterministically: render full content first, count lines, then
decide. Do not pre-commit to either form before seeing the output.

## Temporary Output Shape

The generated `temporary-<task>.md` must contain:

1. task metadata
2. task assessment
3. adjustments relative to long-term baseline
4. final active five-layer stack
5. execution rules
6. conflict rules against long-term baseline
7. exit and merge rules

## Completeness Rules

- Write complete active documents, not pointers.
- Do not output only “use template X”.
- Do not leave key workflow layers implicit.
- If a layer is intentionally inactive, state that explicitly.
