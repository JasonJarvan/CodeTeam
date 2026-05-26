# HarnessFactory

`HarnessFactory` is a methodology repository that produces a **HarnessStack** —
a layered workflow-contract bundle — tailored to a target development
repository's situation. Each factory run consumes questionnaire answers and
emits a deployable bundle under `./output/<run>/HarnessStack/`. The target
repository copies that bundle into its own `docs/HarnessStack/` and operates
from it. Experience accumulated while running the contract flows back into
this factory as iteration input.

## Two-Layer Naming

| Role | Name |
|---|---|
| Generator (this repo) | `HarnessFactory` |
| Single produced bundle | `a HarnessStack` |
| Factory-side output path | `./output/{YYYY-MM-DD-HHmm}-{stack}/HarnessStack/` |
| Target-side activation path | `<target-repo>/docs/HarnessStack/` |

The inner directory name is `HarnessStack/` on both sides so the bundle can
be copied directly without renaming.

## Top-Level Layout

```
HarnessFactory/
├── README.md
├── methods/                     # candidate layer (per-method profiles + cross-method analysis)
├── harness-factory/             # assembly layer (factory source: skill + templates + references)
│   ├── SKILL.md
│   ├── agents/
│   ├── assets/templates/
│   └── references/
├── docs/
│   ├── HarnessStack/             # this repo's own activated stack (dogfood)
│   ├── RepoMem/                  # long-term repository memory for the factory itself
│   ├── CN/                       # Chinese mirror of the factory surface
│   └── superpowers/specs+plans/  # v0.3 design + implementation plan
└── output/                       # produced HarnessStack bundles, one per run
```

## What A Produced HarnessStack Contains

```
./output/{run}/HarnessStack/
├── README.md                     # AI distillation index (~60–80 lines)
├── longterm.md                   # authoritative long-term contract
├── temporary-<task>.md           # task-level patch (when applicable)
└── _toUser/
    └── README.md                 # full human-facing usage manual
```

The top-level `README.md` inside the bundle is the **one-time AI distillation
source**: the target repo's AI reads it once and condenses sections 1–4 into
its `CLAUDE.md`. The authoritative full contract is `longterm.md`; the
human-facing manual lives in `_toUser/`.

## Quick Start (operating the factory)

1. Read `harness-factory/SKILL.md` to understand the question flow and output
   shapes.
2. Walk a target repository through the questionnaire
   (`harness-factory/references/questionnaire.md`).
3. Run the factory to produce
   `./output/<run>/HarnessStack/`.
4. Copy that directory to the target repository as `docs/HarnessStack/`.

## Quick Start (operating a produced HarnessStack)

1. Open `docs/HarnessStack/README.md` (the distillation index).
2. Condense sections 1–4 into your `CLAUDE.md`.
3. Use `docs/HarnessStack/longterm.md` for full details when needed.
4. For Day-One Init steps and per-task iteration, see
   `docs/HarnessStack/_toUser/README.md`.

## Iteration Layers (R3)

`HarnessFactory` internally distinguishes two iteration layers (see
`docs/RepoMem/persist/memory/factory-iteration-layers.md`):

- **Research Layer (调研层)** — maintains per-method definitions and
  cross-method comparisons. Current artifact:
  `methods/_comparison/lifecycle-workflow-comparison.zh-CN.md`.
- **Inference Layer (推断层)** — generates a HarnessStack from user
  guidance. Implemented today by `harness-factory/SKILL.md`.

## Status

- Current version: v0.3 — HarnessFactory rename & output redesign
- Design spec: `docs/superpowers/specs/2026-05-14-harness-factory-rename-and-output-redesign-design.md`
- Implementation plan: `docs/superpowers/plans/2026-05-14-harness-factory-rename-implementation.md`
