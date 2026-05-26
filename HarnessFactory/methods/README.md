# methods/ — Candidate Layer

This directory is the **candidate layer** (formerly "Research Layer" in
`docs/RepoMem/persist/memory/factory-iteration-layers.md`) of HarnessFactory.
It catalogs every workflow method known to this factory — what each method
covers, how it differs from peers, and (when applicable) the playbook for
embedding it into a target repository.

The candidate layer is the **only** input the assembly layer
(`harness-factory/`) reads when generating a HarnessStack. The assembly layer
MUST NOT read method source repositories directly; it reads `methods/<x>/profile.md`.

## Directory shape

```
methods/
├── README.md                   # this file
├── _comparison/                # cross-method analysis (not method-specific)
│   └── lifecycle-workflow-comparison.zh-CN.md
└── <method>/                   # one per candidate
    ├── profile.md              # required: identity + lifecycle + capabilities
    └── embedding-playbook.md   # optional: when embedding has non-trivial mechanics
```

The `_` prefix on `_comparison/` marks it as cross-method, not a method directory.

## Profile schema

Every `<method>/profile.md` MUST contain these sections in this order:

1. `## Identity` — upstream name, layer assignment, status, source location
2. `## Lifecycle Coverage` — 8-stage table (scale: 主覆盖 / 辅助覆盖 / 基本不覆盖); stage definitions in `_comparison/lifecycle-workflow-comparison.zh-CN.md § 判断标准`
3. `## Capabilities` — 1-3 bullets stating what the method actually does
4. `## Conflicts & Dependencies With Other Methods` — overlap and direction
5. `## Embedding Mechanics` — Required? / Playbook? / Activation cost
6. `## Recipes That Use This Method` — relative paths, `(none yet)` if unused
7. `## Source References` — pointers used to fill the profile

Missing sections are a profile defect.

## Layer mapping

Methods are assigned to one of five layers (matches `harness-factory/assets/templates/recipes/recipe-template.md § Layer Assignments`):

| Layer | Examples |
|---|---|
| Primary Workflow | BMAD, gstack, GSD |
| Spec | OpenSpec |
| Execution Discipline | Superpowers |
| Repository Memory | RepoMem |
| Harness Enhancement | ECC, sendbox, dashboard |

`sendbox` and `dashboard` are classified as Harness Enhancement because they
are cross-cutting hooks (inter-session-comm protocol, projection layer) rather
than execution or memory primitives. This classification is non-binding for
future recipes — the candidate layer records lifecycle facts; recipes decide
how to compose them.

## Adding a new candidate

A new method earns a `methods/<x>/` directory when **all three** hold:

1. It is **named** by at least one existing recipe, selection-criteria default,
   or active workflow plan — OR a maintainer has decided to evaluate it.
2. Its **lifecycle coverage** can be filled (the maintainer has read enough
   of the upstream method to fill the 8-stage row honestly, not by guess).
3. Its **layer assignment** is decidable. If a method straddles two layers,
   surface that ambiguity in `Conflicts & Dependencies` rather than splitting
   the directory.

The decision to add (or not add) a method belongs to the maintainer of the
candidate layer, not to the assembly layer. The assembly layer reads what
the candidate layer offers; it does not request additions.

## Status values

- `established` — used by at least one current recipe.
- `new candidate` — has a profile (and optionally a playbook) but no recipe
  references it yet.
- `research-only` — listed in `selection-criteria.md` upgrade triggers but
  has neither a recipe nor a confirmed adoption plan.

## Read-only contract with the assembly layer

The assembly layer (`harness-factory/`) MAY:
- read any file under `methods/`
- cite a method by directory name in recipes (`bmad`, `superpowers`, ...)
- declare `Method References:` in a recipe pointing at `methods/<x>/profile.md`

The assembly layer MUST NOT:
- write to `methods/`
- inline content from a method profile into a recipe (cite by path, do not duplicate)
- assume facts about a method that are not stated in its profile

If a recipe needs a fact the profile does not yet state, the fix is to
update the profile first, then update the recipe.
