# Design — HarnessFactory Rename & Output Redesign

- Status: Draft for user review
- Date: 2026-05-14
- Scope: v0.3 (follows v0.2 execution-policy/recipes/cross-method-invariants)

## 1. Motivation

The repository's role is **not** to be a HarnessStack; it is the **factory** that
produces HarnessStacks. Each run consumes a target-repository situation and
emits a layered workflow contract that the target repo activates locally.
Experience from operating that contract flows back here as iteration input.

The current name `HarnessStack` conflates the factory with its product. This
spec renames the repository to `HarnessFactory` and formalizes the
factory-produces-stacks relationship across naming, directory structure, output
layout, and supporting documentation.

## 2. Naming Model

Two layers only. No "Kit" or "Guide" tier.

| Role | Name | Lives At |
|---|---|---|
| Generator (this repo) | `HarnessFactory` | `<this repo>` |
| Single product instance | `a HarnessStack` | `./output/<run>/HarnessStack/` (factory side) and `<target-repo>/docs/HarnessStack/` (target side) |

Conceptual: **Factory produces Stacks**. Each Stack is one layered harness
configuration tailored to one target repository. The 5-layer baseline inside a
contract IS what makes it a "stack" — same word, same meaning.

### 2.1 Factory subdirectory rename

- `harness-stack/` → `harness-factory/`
- This is the factory's **source** directory (templates, recipes, references,
  SKILL.md). Naming it after its function (factory source) is more accurate
  than naming it after its output.

### 2.2 Skill identity

- `harness-factory/SKILL.md` frontmatter: `name: harness-factory`
- Description rewrites references like "the HarnessStack model" to
  "the HarnessFactory model that generates HarnessStacks".
- Output description: "produces `<output>/HarnessStack/` for deployment to
  `<target-repo>/docs/HarnessStack/`".

### 2.3 Target repo activation directory

- **Unchanged**: `<target-repo>/docs/HarnessStack/`
- Reason: this is literally "the HarnessStack active in this target repo".
  Renaming would invalidate ~35 internal references and break the name-on-both-
  sides symmetry that makes copy-deployment obvious.

## 3. Output Layout

Every factory run emits one bundle under `./output/`. The bundle's inner
directory is named `HarnessStack/` so it can be copied directly to
`<target-repo>/docs/HarnessStack/` without renaming.

```
./output/{YYYY-MM-DD-HHmm}-{scale}-{horizon}/HarnessStack/
├── README.md                    # AI distillation index (~60–80 lines)
├── longterm.md                  # core long-term contract (authoritative)
├── temporary-<task>.md          # task-level patch (optional)
└── _reference/
    ├── README.md                # full human-facing usage manual
    └── version-plan-skeleton.md # multi-version roadmap skeleton
```

### 3.1 Run directory naming

- Path format: `{YYYY-MM-DD-HHmm}-{scale}-{horizon}`
- Time precision: minute-level (`YYYY-MM-DD-HHmm`)
- Situation segment: `{scale}-{horizon}` only
  - `scale`: `solo` | `small-team` | `large-team` (canonical questionnaire values)
  - `horizon`: `short` | `long` — **abbreviated for path use only**. The
    canonical questionnaire values remain `short-lived` / `long-lived`; the
    skill maps them to the abbreviated form when constructing the directory
    name.
- Examples: `2026-05-14-1530-solo-long`, `2026-05-14-1612-small-team-long`

### 3.2 Why type is NOT in the directory name

- Investigation (see § 7) confirmed `repository type` is captured as metadata
  and acts as a **veto filter** in recipe `Compatible Scenarios`, but never as
  a positive selector in any Layer Defaults rule. Same `(scale, horizon)` with
  different `type` values produces byte-identical layer activation when the
  same recipe is chosen.
- Type **remains** as a user-input question because it filters which recipes
  are eligible. It just doesn't earn a slot in the directory name.

### 3.3 Recipe slug

- Not part of the path.
- Recorded inside the bundle: `longterm.md § Recipe Reference` and
  `README.md § Identity / Active Methods`.
- Rationale: keeping the path short and stable; recipe identity is bundle
  content, not bundle coordinate.

### 3.4 Inner directory name (`HarnessStack/`)

- Same name on factory side and target side.
- Deployment instruction is one sentence: "copy `./output/<run>/HarnessStack/`
  to `<target-repo>/docs/HarnessStack/`".

### 3.5 `_reference/` (renamed from `_kit-reference/`)

- "kit" is dropped because the artifact is now called a HarnessStack, not a
  kit.
- The `_` prefix is preserved. Per the existing convention, `_` marks the
  directory as **orthogonal to the active contract** — it can be deleted after
  activation without affecting the contract's correctness.

## 4. Top-Level README (the AI distillation index)

### 4.1 Role

The top-level `<output>/HarnessStack/README.md` is **not** a table of contents
and **not** the full manual. It is a **one-time distillation source** designed
for the target repo's AI agent to read once and condense into `CLAUDE.md`.

After CLAUDE.md is written, README is consulted only on recipe upgrade. The
authoritative full contract remains in `longterm.md`; the human-facing manual
remains in `_reference/README.md`.

### 4.2 Required sections (~60–80 lines total)

1. **Identity** — `"This repo runs HarnessStack at <scale>/<horizon>. Active recipe: <slug>."`
2. **Active Methods** — bullet list of methods activated by this stack
   (e.g. Superpowers, OpenSpec, RepoMem, ECC), each with a one-line
   responsibility.
3. **Per-Task Pipeline (Compressed)** — 7–10 step condensed version of
   `longterm.md § Pipeline`. Section heading MUST include the word
   `(Compressed)` and the section MUST end with a pointer:
   > "This is the compressed view. For the full step list, conflict rules, and
   > exception handling, see `longterm.md § Pipeline`."
   This labeling is required to prevent AI consumers from treating the
   compressed list as authoritative.
4. **Hard Invariants** — non-negotiable rules:
   - `<task>` = `change-id` = `<slug>`
   - Add-only: methods never deactivate, only extend
   - Dual-verification gate before finishing-a-development-branch
5. **Where to read more**
   - Full contract: `./longterm.md`
   - Usage manual: `./_reference/README.md`
   - Task-level patch (if present): `./temporary-<task>.md`
6. **For AI consumers** —
   > "Distill sections 1–4 into CLAUDE.md. Do not duplicate longterm.md
   > verbatim. Re-read this README only on recipe upgrade."

### 4.3 Anti-drift constraint

§3 (Compressed Pipeline) and `longterm.md § Pipeline` MUST be rendered from a
single source (the active recipe's pipeline definition). The skill renders the
full list to `longterm.md` and a condensed list to `README.md` in one pass; no
hand-edited duplication.

## 5. File-Level Change Scope

### 5.1 Mandatory rewrites

- Top-level `README.md` — full rewrite for HarnessFactory framing.
- All RepoMem persist memory:
  - `docs/RepoMem/persist/memory/workflow-system.md`
  - `docs/RepoMem/persist/memory/contractor-output.md`
  - `docs/RepoMem/persist/memory/github-repo-design.md`
  - `docs/RepoMem/persist/memory/cross-method-invariants.md`
  - `docs/RepoMem/persist/memory/execution-policy.md`
  - `docs/RepoMem/persist/memory/template-evolution.md`
  - `docs/RepoMem/persist/architecture/workflow-system.md`
  - `docs/RepoMem/persist/version-plan.md`
- Per-occurrence rewriting rule:
  - "HarnessStack 仓库 / the HarnessStack repository" (meaning the method repo)
    → `HarnessFactory`
  - "HarnessStack" used to mean **the artifact** (e.g. "produces a HarnessStack",
    "the HarnessStack at `docs/HarnessStack/`") → **unchanged**
  - "`harness-stack/`" (factory source dir) → "`harness-factory/`"
  - "`docs/HarnessStack/`" (target-repo activation dir) → **unchanged**

### 5.2 Factory source rename

- `harness-stack/` → `harness-factory/` (directory rename + all internal
  references)
- `harness-stack/SKILL.md` → `harness-factory/SKILL.md` with frontmatter
  `name: harness-factory`
- `harness-stack/agents/openai.yaml` — update any path or name fields
- `docs/CN/` mirror — sync all the above (SKILL.md, references/, assets/,
  agents/openai.yaml)

### 5.3 Existing dogfood activation

- `docs/HarnessStack/longterm.md` (this repo's self-applied stack) —
  **keep file path unchanged**; update only the `Repository:` field value
  from `HarnessStack` to `HarnessFactory`.

### 5.4 Out of scope (preserved as-is)

- Worked examples cited by recipes:
  - `docs/examples/superpowers-only-longterm.md`
  - `docs/examples/openspec-superpowers-repomem-longterm_orient.md`
- Historical mentions of "HarnessStack as repo name" inside frozen RepoMem temp
  docs (none currently exist; future temp memory will use HarnessFactory).

## 6. Cleanup (R2)

| Path | Action | Reason |
|---|---|---|
| `docs/handoff/3method-iteration-2026-05-07.md` | **delete** | No inbound refs; historical handoff snapshot |
| `docs/examples/openspec-superpowers-repomem-longterm.md` | **delete** | No inbound refs; superseded |
| `docs/examples/openspec-superpowers-repomem-longterm_v1.md` | **delete** | Explicit `_v1` historical version |
| `docs/examples/openspec-superpowers-repomem-ecc-activation-kit/` | **delete** (full directory) | No inbound refs; pre-redesign output sample |
| `docs/analysis-lifecycle-workflow-comparison.zh-CN.md` | **keep in place; record in RepoMem as Research-Layer artifact** | Belongs to "调研层" (see § 8). No file move; the new RepoMem entry lists it as a pointer. |

After deletions, also remove the empty `docs/handoff/` directory.

## 7. Repository Type Investigation Result

(Recorded here as design rationale; full evidence in conversation.)

Investigation conclusion: `repository type` is **not load-bearing for layer
selection**. Evidence:

- `harness-factory/references/selection-criteria.md § Layer Defaults` branches
  only on `collaboration scale`.
- Type appears only in recipe `Compatible Scenarios` as a veto filter — it can
  eliminate a recipe but never positively select a layer.
- All longterm scenario templates (`solo.md`, `small-team.md`,
  `large-team.md`) are scale-keyed; none branch on type.
- `Authority By Field` table (selection-criteria § Scenario × Recipe
  Composition) explicitly states "Current Active Long-Term Baseline:
  authoritative source = recipe; scenario contributes scale-level constraints"
  — type contributes nothing.

Consequence: type stays as a questionnaire input (because it filters recipes)
but is excluded from directory naming.

## 8. R3 — Factory Iteration Conceptual Layers (RepoMem entry)

A new RepoMem persist memory entry will be created describing the factory's
internal architecture in two conceptual layers (target: future v0.4+):

- **调研层 (Research Layer)** — maintains per-method layer definitions and
  lifecycle coverage analyses. Maintained periodically by an agent.
  `docs/analysis-lifecycle-workflow-comparison.zh-CN.md` is the first
  artifact assigned to this layer.
- **推断层 (Inference Layer)** — given user guidance (questionnaire answers),
  produces a HarnessStack. This is what the current SKILL implements.

This memory entry codifies the framing so future research/output additions
have a clear home. No implementation in this spec — design-only recording.

## 9. User Auto-Memory Updates (Q3d)

The user's auto-memory at
`C:\Users\sheng.zhao\.claude\projects\D--Documents-Codes-Source-Jason-Tool-Dev-HarnessStack\memory\`
will be updated:

- `project_overview.md` — rename repository name; preserve mention of
  HarnessStack as the produced artifact name.
- `project_structure.md` — update top-level directory list
  (`harness-stack/` → `harness-factory/`); add `output/` directory.
- `project_decisions.md` — replace fixed-decision "仓库名 HarnessStack" with
  "仓库名 HarnessFactory；产出物名 HarnessStack（每次产出 = 一份 HarnessStack）".
- `project_version_plan.md` — note v0.3 = factory rename and output redesign.
- `kit_osr_ecc_invariants.md` — unchanged content, but verify references to
  paths point to `harness-factory/` rather than `harness-stack/`.

## 10. Acceptance Criteria

This redesign is complete when:

1. Repo top-level README describes HarnessFactory and its Factory→Stack
   relationship.
2. `harness-factory/` directory exists with all former `harness-stack/`
   contents and updated internal cross-references. `harness-stack/` is gone.
3. `docs/CN/` mirror is in sync.
4. Skill output, when run, produces
   `./output/{YYYY-MM-DD-HHmm}-{scale}-{horizon}/HarnessStack/` containing
   `README.md`, `longterm.md`, optional `temporary-<task>.md`, and
   `_reference/` with the renamed contents.
5. The compressed Pipeline in `<output>/HarnessStack/README.md § 3` is
   labeled `(Compressed)` and points to `longterm.md § Pipeline` for the full
   version.
6. RepoMem persist memory is updated per § 5.1 and includes the new R3 entry.
7. Cleanup deletions per § 6 are committed.
8. User auto-memory entries per § 9 are updated.
9. The repository's own dogfood file `docs/HarnessStack/longterm.md` has
   `Repository: HarnessFactory`.

## 11. Non-Goals

- Replacing `docs/HarnessStack/` (target activation dir) with another name.
- Removing `repository type` from the questionnaire (it remains as recipe
  filter).
- Renaming RepoMem temp docs (cross-method invariants apply only to target
  repos, not the factory).
- Implementing the Research-Layer agent or any periodic maintenance
  automation (deferred to future version).
- Backward-compatibility shims for the old `harness-stack/` path.
