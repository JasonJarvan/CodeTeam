---
domain: workflow-system
last_reviewed_at: 2026-05-14
---

# template-evolution

## Constraints

- The longterm contract template originally treated five layers as independent
  toggles. That shape lost inter-layer pipeline, conflict, verification, and
  merge-gate semantics, especially for combinations like
  `OpenSpec + Superpowers + RepoMem` where Primary is `none`.
- Scenario subtemplates (`solo`, `small-team`, `large-team`) embed implicit
  layer combos. Without an explicit recipe abstraction, the same combo at
  different scales produces different contracts even when the user wants the
  combo to be the invariant.

## Decisions

- Long-term contract template extended with five cross-layer slots:
  - `Pipeline`
  - `Cross-Layer Conflicts`
  - `Verification Topology`
  - `Merge Gates`
  - `Suitability Envelope`
- New `Recipe Reference` field added to `Document Meta`.
- Primary Workflow Layer gains an `Emergent Ownership` field for cases where
  Primary is `none` but the responsibility is jointly carried by Spec and
  Execution layers.
- Recipe abstraction introduced under
  `harness-factory/assets/templates/recipes/`. A recipe captures layer combo +
  inter-layer rules. Final activation = scenario × recipe.
- Question flow gains a `Layer-First` entry mode for users who pre-fix layer
  choices. Default remains `Scenario-First`.
- Add-only principle adopted (project_decisions.md item 7): once a method is
  activated for a project, it never deactivates. Implications applied:
  - Vocabulary: `Default disabled` renamed to `Default inactive`
    (binary `Active` / `Inactive`, no permanent-exclusion state).
  - Recipe lifecycle: copy-on-write. Recipes are immutable once published;
    extending a recipe means creating a new superset recipe file. Old recipe
    files are preserved forever; references stay valid.
  - Recipe naming: layer-canonical-order
    (Primary → Spec → Execution → Memory → Harness), lowercase
    hyphen-separated. Example: `bmad-openspec-superpowers-repomem-ecc.md`.
  - Recipe upgrade does NOT trigger long-term rewrite review; the
    `Full Rewrite Conditions` line "the recipe is replaced" was removed.
- Break-glass mechanism for recipe invariants: temporary contractor MAY skip
  Pipeline ordering, Merge Gates, or Verification Topology, but only by
  declaring the exception in its `Recipe Invariant Exceptions` section with
  reason and compensating action. Default is deny.
- Composition rule documented in `references/selection-criteria.md`:
  scenario × recipe = `union`; recipe is authoritative on layer/cross-layer
  rules; scenario is authoritative on scale defaults.
- `Layer-First` ambiguity resolved: skill always asks scale unless the
  recipe's Compatible Scenarios fix the axis to a single value.
- First single-layer recipe published: `recipes/superpowers.md`.
- `Delivery Target Compatibility` section added to recipe template; existing
  recipes updated.

## Rationale

- Sample run on `OpenSpec + Superpowers + RepoMem` produced a near-duplicate
  of `small-team.md` minus `ECC(medium)`. The 1-line delta exposed that
  "combination" had no first-class home and that scenario subtemplates were
  silently encoding implicit recipes.
- Adding cross-layer slots without a recipe abstraction would have made
  scenario subtemplates duplicate the same rules. Extracting recipes once
  removes the duplication and makes layer-first questions answerable.

## Pitfalls

- Scenario subtemplates currently still embed implicit recipes. Until each
  scale gets an explicit default recipe, scenario subtemplates and recipes can
  drift. Treat any change to inter-layer rules in a scenario subtemplate as a
  signal to extract or update a recipe.
- ECC-bearing recipe for the small-team default scenario has not been
  published yet. `small-team.md` references it as the default but the file
  does not exist. Build it before users adopt small-team baseline.
- The Chinese mirror under `docs/CN/` has not been updated to match this
  template evolution. Defer until the recipe abstraction stabilizes.
- `Emergent Ownership` is free-form text by design. If we ever want
  tooling-level validation (e.g., "Primary=none must declare Emergent
  Ownership"), introduce a controlled vocabulary later — not now.

## Related Memory

- See [workflow-system](./workflow-system.md)
- See [contractor-output](./contractor-output.md)
- First concrete recipe: `harness-factory/assets/templates/recipes/openspec-superpowers-repomem.md`
