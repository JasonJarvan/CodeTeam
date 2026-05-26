# Candidate Layer Extraction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Land the "candidate layer" as a first-class top-level directory `methods/`, populate it for the 7 currently-named methods (superpowers, repomem, openspec, ecc, bmad, gstack, gsd) plus 2 new candidates promoted from sendbox letters (sendbox, dashboard), and update the assembly layer (`harness-factory/`) so it explicitly reads candidate-layer profiles.

**Architecture:** Pure documentation/methodology refactor. No runtime code. Two-layer model already exists conceptually in `docs/RepoMem/persist/memory/factory-iteration-layers.md` (Research vs Inference). This plan makes that model physical and visible at repo top level: `methods/` (candidate, formerly anemic "Research Layer") + `harness-factory/` (assembly, unchanged Inference Layer). "Tests" are grep-based invariant checks and file-existence checks. Each task produces an atomic, independently committable change.

**Tech Stack:** Markdown, git, ripgrep (`rg`) for verification.

**Scope explicit non-goals:**
- Do NOT rename `harness-factory/` (deferred to a future v0.5 task).
- Do NOT mutate `docs/CN/` (frozen at v0.2 per existing convention).
- Do NOT add new recipes for sendbox/dashboard yet (recipe authoring is a separate downstream task; profiles unlock that work but don't require it).
- Do NOT burn the source letters at `../docs/sendbox/toHarnessFactory/from-{sendbox,dashboard}-embedding-playbook.md` in this plan — that is handled by sendbox-protocol's checkpoint sweep, not by this refactor.
- Do NOT backfill `Method References:` into existing recipe files (`superpowers.md`, `superpowers-repomem.md`, etc.) — only the recipe **template** gets the new field; existing recipes migrate lazily on next edit.

---

## Conventions (used by every task)

### A. Profile schema

Every `methods/<method>/profile.md` MUST follow this exact section order and headings. The schema is also written into `methods/README.md` in Task 1; this block is the authoritative copy for plan execution.

```markdown
# Profile — <method-name>

## Identity

- Upstream name: <canonical full name as used by the source community>
- Layer: <Primary Workflow | Spec | Execution Discipline | Repository Memory | Harness Enhancement>
- Status: <established | new candidate | research-only>
- Source location: <upstream repo URL OR local skill path>

## Lifecycle Coverage

Stage mapping uses the 8-stage scale from `methods/_comparison/lifecycle-workflow-comparison.zh-CN.md § 判断标准`.

| 目标定义 | 需求澄清 | 方案设计 | 任务规划 | 实现开发 | 测试验证 | 发布交付 | 运行反馈与迭代沉淀 |
|---|---|---|---|---|---|---|---|
| <主覆盖 / 辅助覆盖 / 基本不覆盖> | ... | ... | ... | ... | ... | ... | ... |

## Capabilities

- <bullet 1>
- <bullet 2>
- <bullet 3>

## Conflicts & Dependencies With Other Methods

- <overlap with method X — resolution rule>
- <dependency on method Y — direction>

## Embedding Mechanics

- Required? <yes | no>
- Playbook: <relative path to embedding-playbook.md | n/a>
- Activation cost: <none | symlink skill | edit target longterm.md | hook config | combination>

## Recipes That Use This Method

- <relative path to recipe file, one per line; "(none yet)" if no current recipe uses it>

## Source References

- <pointer to section in analysis doc, recipe file, or letter — relative path + heading anchor>
```

### B. Source mapping for the 7 established methods

For each method, the executor extracts the **Lifecycle Coverage** row verbatim from `methods/_comparison/lifecycle-workflow-comparison.zh-CN.md § 生命周期覆盖矩阵` (post-move, in Task 2; pre-move it lives at `docs/analysis-lifecycle-workflow-comparison.zh-CN.md` line 298-306) and the **Capabilities** + **Conclusion** from the per-system narrative section.

| Method | Per-system section heading | Lifecycle matrix row label | Layer assignment |
|---|---|---|---|
| superpowers | `### Superpowers` | `Superpowers` | Execution Discipline |
| repomem | `### RepoMem` | `RepoMem` | Repository Memory |
| openspec | `### OpenSpec` | `OpenSpec` | Spec |
| ecc | `### everythingclaudecode` | `everythingclaudecode` | Harness Enhancement |
| bmad | `### BMAD` | `BMAD` | Primary Workflow |
| gstack | `### gstack` | `gstack` | Primary Workflow |
| gsd | `### GSD` | `GSD` | Primary Workflow |

The `ecc/` directory uses the short form (matches `recipes/*.md` and `selection-criteria.md`); inside `profile.md`, `Identity § Upstream name` records `everythingclaudecode`.

### C. Commit message convention

All commits in this plan use prefix `methods:` for content under `methods/` and `assembly:` for changes under `harness-factory/`. RepoMem updates use `repomem:`. Examples:
- `methods: scaffold candidate layer (README + _comparison move)`
- `assembly: SKILL.md add Step 6.5 candidate-layer check`

---

## Task 1: Scaffold `methods/` and write candidate-layer README

**Files:**
- Create: `methods/README.md`

- [ ] **Step 1: Verify `methods/` does not yet exist**

Run: `test ! -e methods && echo OK || echo "methods/ already exists — abort"`
Expected: `OK`

- [ ] **Step 2: Create `methods/README.md` with full content**

Create `methods/README.md` with exactly this content:

````markdown
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
````

- [ ] **Step 3: Verify directory created and file readable**

Run: `ls methods/README.md && wc -l methods/README.md`
Expected: file exists, ~80-90 lines.

- [ ] **Step 4: Commit**

```bash
git add methods/README.md
git commit -m "methods: scaffold candidate layer with README and schema"
```

---

## Task 2: Move lifecycle-comparison doc and update references

**Files:**
- Move: `docs/analysis-lifecycle-workflow-comparison.zh-CN.md` → `methods/_comparison/lifecycle-workflow-comparison.zh-CN.md`
- Modify: `README.md` (top-level), `docs/RepoMem/persist/memory/factory-iteration-layers.md`, `harness-factory/SKILL.md` (only if it references the old path)

- [ ] **Step 1: Find every existing reference to the old path**

Run: `rg -n "analysis-lifecycle-workflow-comparison" --type md`
Expected: list of files that mention it. Note them — every one needs updating in Step 4.

- [ ] **Step 2: Create destination directory and move via git mv**

```bash
mkdir -p methods/_comparison
git mv docs/analysis-lifecycle-workflow-comparison.zh-CN.md \
       methods/_comparison/lifecycle-workflow-comparison.zh-CN.md
```

- [ ] **Step 3: Verify the move**

Run: `ls methods/_comparison/lifecycle-workflow-comparison.zh-CN.md && test ! -e docs/analysis-lifecycle-workflow-comparison.zh-CN.md && echo OK`
Expected: `OK`

- [ ] **Step 4: Rewrite each reference found in Step 1**

For each file from Step 1, replace the old path with the new path. Known references at plan-write time:

- `README.md` (top-level) — change the bullet under `## Iteration Layers (R3)` and the directory tree under `## Top-Level Layout` (the `docs/` block).
- `docs/RepoMem/persist/memory/factory-iteration-layers.md` — change the `当前归属此层的文件` bullet under `### 调研层 (Research Layer)`.
- `harness-factory/SKILL.md` — grep result will say whether it references the old path. If yes, update.

Replacement target: `methods/_comparison/lifecycle-workflow-comparison.zh-CN.md` (relative paths from each file's location, e.g., from `README.md` use `methods/_comparison/...`; from `factory-iteration-layers.md` use `../../../../methods/_comparison/...`).

Also update top-level `README.md § Top-Level Layout` directory tree to add `methods/` as a sibling of `harness-factory/`, `docs/`, and `output/`:

```
HarnessFactory/
├── README.md
├── methods/                     # candidate layer (per-method profiles + cross-method analysis)
├── harness-factory/             # assembly layer (factory source: skill + templates + references)
│   ...
├── docs/
│   ...                          # (remove the analysis-lifecycle-... line from this block)
└── output/                      # produced HarnessStack bundles, one per run
```

- [ ] **Step 5: Verify no stale references remain**

Run: `rg -n "docs/analysis-lifecycle-workflow-comparison" --type md`
Expected: no output (zero matches).

- [ ] **Step 6: Commit**

```bash
git add methods/_comparison/lifecycle-workflow-comparison.zh-CN.md README.md docs/RepoMem/persist/memory/factory-iteration-layers.md harness-factory/SKILL.md
git commit -m "methods: move lifecycle-workflow comparison to candidate layer"
```

(If `harness-factory/SKILL.md` was not touched, omit it from the `git add` line.)

---

## Task 3: Profiles for superpowers + repomem

**Files:**
- Create: `methods/superpowers/profile.md`
- Create: `methods/repomem/profile.md`

- [ ] **Step 1: Read source sections**

Open `methods/_comparison/lifecycle-workflow-comparison.zh-CN.md` and locate:
- `### Superpowers` (~line 149-176) — narrative
- `### RepoMem` (~line 211-269) — narrative
- `## 生命周期覆盖矩阵` (~line 296+) — matrix rows for both
- `### 第三组：Superpowers` and `### 第五组：RepoMem` (~line 594+ and ~line 627+) — overlap/boundary analysis

Open `harness-factory/assets/templates/recipes/superpowers-repomem.md § Cross-Layer Conflicts` for inter-method conflict text.

- [ ] **Step 2: Create `methods/superpowers/profile.md`**

```markdown
# Profile — superpowers

## Identity

- Upstream name: Superpowers
- Layer: Execution Discipline
- Status: established
- Source location: `~/.claude/skills/superpowers:*` (skill plugin set)

## Lifecycle Coverage

Stage mapping uses the 8-stage scale from `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 判断标准`.

| 目标定义 | 需求澄清 | 方案设计 | 任务规划 | 实现开发 | 测试验证 | 发布交付 | 运行反馈与迭代沉淀 |
|---|---|---|---|---|---|---|---|
| 辅助覆盖 | 辅助覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 辅助覆盖 |

## Capabilities

- Execution-discipline chain: `brainstorming → using-git-worktrees → writing-plans → executing-plans → TDD → requesting-code-review → finishing-a-development-branch`.
- Pre-implementation planning gates (writing-plans) and post-implementation verification gates (verification-before-completion).
- Subagent dispatch (subagent-driven-development) for parallel and isolated task execution.

## Conflicts & Dependencies With Other Methods

- vs RepoMem: writing-plans defines HOW; RepoMem temporary docs record WHY/context. Never duplicate plan steps into memory. (Source: `../../harness-factory/assets/templates/recipes/superpowers-repomem.md § Cross-Layer Conflicts`)
- vs OpenSpec: when both active, OpenSpec change cycle takes precedence for scope boundaries; Superpowers execution discipline runs inside an OpenSpec change.
- No dependency on any other layer to function; Superpowers is the canonical minimum execution-discipline layer.

## Embedding Mechanics

- Required? no — Superpowers is a skill set the user installs once; no per-target embedding action.
- Playbook: n/a
- Activation cost: none (the skill is already present in any Claude Code env that has the plugin installed)

## Recipes That Use This Method

- `../../harness-factory/assets/templates/recipes/superpowers.md`
- `../../harness-factory/assets/templates/recipes/superpowers-repomem.md`
- `../../harness-factory/assets/templates/recipes/openspec-superpowers-repomem.md`
- `../../harness-factory/assets/templates/recipes/openspec-superpowers-repomem-ecc.md`

## Source References

- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § Superpowers` (narrative)
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 生命周期覆盖矩阵` (matrix row)
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 第三组：Superpowers` (overlap/boundary)
```

- [ ] **Step 3: Create `methods/repomem/profile.md`**

```markdown
# Profile — repomem

## Identity

- Upstream name: RepoMem
- Layer: Repository Memory
- Status: established
- Source location: `~/.claude/skills/repo-mem`

## Lifecycle Coverage

Stage mapping uses the 8-stage scale from `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 判断标准`.

| 目标定义 | 需求澄清 | 方案设计 | 任务规划 | 实现开发 | 测试验证 | 发布交付 | 运行反馈与迭代沉淀 |
|---|---|---|---|---|---|---|---|
| 基本不覆盖 | 辅助覆盖 | 主覆盖 | 辅助覆盖 | 辅助覆盖 | 辅助覆盖 | 基本不覆盖 | 主覆盖 |

## Capabilities

- Persist-vs-temp split: long-term architecture / memory under `docs/RepoMem/persist/`, task-scoped docs under `docs/RepoMem/temp/<task>/`.
- HITL merge: `RepoMem.merge` promotes temp content to persist with a human review gate.
- Cross-task context load: `RepoMem.read` is the canonical task-entry context source.

## Conflicts & Dependencies With Other Methods

- vs Superpowers: see `methods/superpowers/profile.md § Conflicts`. Plan vs memory boundary.
- vs OpenSpec: OpenSpec design.md and RepoMem temporary architecture.md must not duplicate. (Source: v0.4 candidate in `docs/RepoMem/persist/version-plan.md § 未来考虑` — Task-Level Document Partition)
- Depends on: nothing structurally, but `RepoMem.merge` is positioned AFTER `Superpowers.finishing-a-development-branch` in recipes that bundle both.

## Embedding Mechanics

- Required? yes (lightweight) — target repo needs `docs/RepoMem/persist/` scaffolded on Day-One Init.
- Playbook: n/a — Day-One Init steps live in the bundle's `_toUser/README.md`, not in a separate playbook (RepoMem's embedding is mechanical enough to be inline).
- Activation cost: create `docs/RepoMem/persist/{architecture,memory}/` directories + optional `version-plan.md` per `_toUser/README.md § Tracking HarnessStack Evolution`.

## Recipes That Use This Method

- `../../harness-factory/assets/templates/recipes/superpowers-repomem.md`
- `../../harness-factory/assets/templates/recipes/openspec-superpowers-repomem.md`
- `../../harness-factory/assets/templates/recipes/openspec-superpowers-repomem-ecc.md`

## Source References

- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § RepoMem` (narrative)
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 生命周期覆盖矩阵` (matrix row)
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 第五组：RepoMem` (overlap/boundary)
```

- [ ] **Step 4: Verify both profiles match the schema**

Run: `for f in methods/superpowers/profile.md methods/repomem/profile.md; do echo "=== $f ==="; rg -n "^## " "$f"; done`
Expected: each file shows exactly these 7 headings in order: Identity, Lifecycle Coverage, Capabilities, Conflicts & Dependencies With Other Methods, Embedding Mechanics, Recipes That Use This Method, Source References.

- [ ] **Step 5: Commit**

```bash
git add methods/superpowers/profile.md methods/repomem/profile.md
git commit -m "methods: add superpowers and repomem profiles"
```

---

## Task 4: Profiles for openspec + ecc

**Files:**
- Create: `methods/openspec/profile.md`
- Create: `methods/ecc/profile.md`

- [ ] **Step 1: Read source sections**

Open `methods/_comparison/lifecycle-workflow-comparison.zh-CN.md`:
- `### OpenSpec` (~line 115-148)
- `### everythingclaudecode` (~line 177-210)
- `## 生命周期覆盖矩阵` (rows for OpenSpec, everythingclaudecode)
- `### 第二组：OpenSpec` (~line 572+) and `### 第四组：everythingclaudecode` (~line 613+)

Also check `harness-factory/assets/templates/recipes/openspec-superpowers-repomem-ecc.md` for ECC-specific Cross-Layer Conflicts and ECC strength variants (`ECC(light)`, `ECC(medium)`).

- [ ] **Step 2: Create `methods/openspec/profile.md`**

```markdown
# Profile — openspec

## Identity

- Upstream name: OpenSpec
- Layer: Spec
- Status: established
- Source location: upstream OpenSpec repository (referenced by recipes; no local skill path)

## Lifecycle Coverage

Stage mapping uses the 8-stage scale from `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 判断标准`.

| 目标定义 | 需求澄清 | 方案设计 | 任务规划 | 实现开发 | 测试验证 | 发布交付 | 运行反馈与迭代沉淀 |
|---|---|---|---|---|---|---|---|
| 辅助覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 辅助覆盖 | 主覆盖 |

## Capabilities

- Change-cycle spec contract: propose → design → tasks → implement → archive.
- Stable change boundaries — every spec change is auditable and reviewable as a discrete artifact.
- Supports custom schemas (TDD, rapid, etc.) per upstream OpenSpec docs.

## Conflicts & Dependencies With Other Methods

- vs RepoMem: see `methods/repomem/profile.md § Conflicts`. Design vs architecture boundary.
- vs Superpowers: OpenSpec change cycle takes scope precedence; Superpowers execution discipline runs inside the change.
- Spec root location is recipe-time decided: `./openspec/` (upstream default) or `docs/openspec/` (when co-located with other method-layer artifacts under `docs/`). See `../../harness-factory/assets/templates/longterm-template.md § OpenSpec Root`.

## Embedding Mechanics

- Required? yes — target repo creates `./openspec/` or `docs/openspec/` and adopts the change-cycle workflow.
- Playbook: n/a (mechanics are stated in `../../harness-factory/assets/templates/longterm-template.md § OpenSpec Root` and the upstream OpenSpec docs).
- Activation cost: create spec root + first change directory; ongoing cost = one change cycle per scoped change.

## Recipes That Use This Method

- `../../harness-factory/assets/templates/recipes/openspec-superpowers-repomem.md`
- `../../harness-factory/assets/templates/recipes/openspec-superpowers-repomem-ecc.md`

## Source References

- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § OpenSpec`
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 生命周期覆盖矩阵`
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 第二组：OpenSpec`
```

- [ ] **Step 3: Create `methods/ecc/profile.md`**

```markdown
# Profile — ecc

## Identity

- Upstream name: everythingclaudecode (commonly abbreviated ECC)
- Layer: Harness Enhancement
- Status: established
- Source location: upstream `everythingclaudecode` repository (referenced by recipes; no local skill path)

## Lifecycle Coverage

Stage mapping uses the 8-stage scale from `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 判断标准`.

| 目标定义 | 需求澄清 | 方案设计 | 任务规划 | 实现开发 | 测试验证 | 发布交付 | 运行反馈与迭代沉淀 |
|---|---|---|---|---|---|---|---|
| 基本不覆盖 | 辅助覆盖 | 辅助覆盖 | 辅助覆盖 | 主覆盖 | 主覆盖 | 辅助覆盖 | 主覆盖 |

## Capabilities

- Performance-optimization system for AI agent harnesses: skills + instincts + memory optimization + continuous learning.
- Hook-level injection points for memory / verification / context-quality enforcement.
- Strength tiers in recipes: `ECC(light)` (cheapest set of hooks), `ECC(medium)` (standard set). See `../../harness-factory/references/output-shapes.md § Run Directory Naming` for path encoding (`eccLight`, `eccMedium`).

## Conflicts & Dependencies With Other Methods

- Depends on: a memory layer (RepoMem) to attach memory-related hooks to. Without RepoMem, ECC's memory-side capabilities are unanchored.
- vs Superpowers: ECC hooks can wrap Superpowers steps but must not duplicate their gating (e.g., do not add a verification hook that competes with `verification-before-completion`).
- vs OpenSpec: ECC hooks run orthogonal to OpenSpec's change cycle; do not insert ECC hooks inside spec-time-only steps.

## Embedding Mechanics

- Required? yes — hook configs need to be authored in the target repo's `docs/HarnessStack/hooks/<hook>.md` style.
- Playbook: n/a (hook authoring patterns are stated in the upstream ECC docs and reflected in `../../harness-factory/assets/templates/recipes/openspec-superpowers-repomem-ecc.md`).
- Activation cost: per-hook config; strength tier sets the count.

## Recipes That Use This Method

- `../../harness-factory/assets/templates/recipes/openspec-superpowers-repomem-ecc.md`

## Source References

- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § everythingclaudecode`
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 生命周期覆盖矩阵`
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 第四组：everythingclaudecode`
```

- [ ] **Step 4: Verify schema**

Run: `for f in methods/openspec/profile.md methods/ecc/profile.md; do echo "=== $f ==="; rg -n "^## " "$f"; done`
Expected: each file shows the 7 schema headings in order.

- [ ] **Step 5: Commit**

```bash
git add methods/openspec/profile.md methods/ecc/profile.md
git commit -m "methods: add openspec and ecc profiles"
```

---

## Task 5: Profiles for bmad + gstack + gsd (research-only)

**Files:**
- Create: `methods/bmad/profile.md`
- Create: `methods/gstack/profile.md`
- Create: `methods/gsd/profile.md`

These three are listed in `selection-criteria.md` as "Default inactive" Primary Workflow upgrade options. Status = `research-only` (no current recipe uses them).

- [ ] **Step 1: Read source sections**

Open `methods/_comparison/lifecycle-workflow-comparison.zh-CN.md`:
- `### BMAD` (~line 42-65)
- `### gstack` (~line 66-89)
- `### GSD` (~line 90-114)
- `## 生命周期覆盖矩阵` (rows for BMAD, gstack, GSD)
- `### 第一组：BMAD、gstack、GSD` (~line 550+)

- [ ] **Step 2: Create `methods/bmad/profile.md`**

```markdown
# Profile — bmad

## Identity

- Upstream name: BMAD
- Layer: Primary Workflow
- Status: research-only
- Source location: upstream BMAD repository (not yet adopted by any recipe in this factory)

## Lifecycle Coverage

| 目标定义 | 需求澄清 | 方案设计 | 任务规划 | 实现开发 | 测试验证 | 发布交付 | 运行反馈与迭代沉淀 |
|---|---|---|---|---|---|---|---|
| 主覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 辅助覆盖 | 辅助覆盖 |

## Capabilities

- Full-stack methodology: covers from goal definition through verification.
- Roadmap-heavy delivery mode — fits projects whose work portfolio exceeds what execution discipline alone can carry.
- See `../_comparison/lifecycle-workflow-comparison.zh-CN.md § BMAD` for the canonical capabilities list.

## Conflicts & Dependencies With Other Methods

- vs gstack and GSD: all three are Primary Workflow candidates and mutually exclusive at activation time. Recipes pick one.
- vs Superpowers: Superpowers becomes the execution-discipline sublayer under BMAD; Superpowers' planning gates are bounded by BMAD's task-planning artifacts.
- vs OpenSpec: BMAD's design-stage artifacts may overlap with OpenSpec design.md; if both are active, recipe MUST state which owns scope boundaries.

## Embedding Mechanics

- Required? yes (heavyweight) — target repo adopts BMAD's full artifact set.
- Playbook: n/a (no playbook authored yet; document upstream mechanics in a future `embedding-playbook.md` when first recipe adopts it).
- Activation cost: high — full methodology onboarding.

## Recipes That Use This Method

- (none yet)

## Source References

- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § BMAD`
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 生命周期覆盖矩阵`
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 第一组：BMAD、gstack、GSD`
- `../../harness-factory/references/selection-criteria.md § Layer Defaults` (listed under "Default inactive" for Primary Workflow)
```

- [ ] **Step 3: Create `methods/gstack/profile.md`**

```markdown
# Profile — gstack

## Identity

- Upstream name: gstack
- Layer: Primary Workflow
- Status: research-only
- Source location: upstream gstack repository (not yet adopted by any recipe in this factory)

## Lifecycle Coverage

| 目标定义 | 需求澄清 | 方案设计 | 任务规划 | 实现开发 | 测试验证 | 发布交付 | 运行反馈与迭代沉淀 |
|---|---|---|---|---|---|---|---|
| 主覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 主覆盖 |

## Capabilities

- Most uniformly broad coverage of the 8-stage lifecycle among Primary Workflow candidates (every stage = 主覆盖).
- Stronger emphasis on release/delivery and post-release iteration than BMAD.
- See `../_comparison/lifecycle-workflow-comparison.zh-CN.md § gstack` for canonical capabilities list.

## Conflicts & Dependencies With Other Methods

- vs BMAD and GSD: see `methods/bmad/profile.md § Conflicts` — mutually exclusive Primary Workflow candidates.
- vs Superpowers: gstack's release-stage steps may overlap with `finishing-a-development-branch`; recipe MUST decide ownership.

## Embedding Mechanics

- Required? yes (heavyweight) — full methodology adoption.
- Playbook: n/a (author when first recipe adopts it).
- Activation cost: high.

## Recipes That Use This Method

- (none yet)

## Source References

- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § gstack`
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 生命周期覆盖矩阵`
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 第一组：BMAD、gstack、GSD`
- `../../harness-factory/references/selection-criteria.md § Layer Defaults`
```

- [ ] **Step 4: Create `methods/gsd/profile.md`**

```markdown
# Profile — gsd

## Identity

- Upstream name: GSD
- Layer: Primary Workflow
- Status: research-only
- Source location: upstream GSD repository (not yet adopted by any recipe in this factory)

## Lifecycle Coverage

| 目标定义 | 需求澄清 | 方案设计 | 任务规划 | 实现开发 | 测试验证 | 发布交付 | 运行反馈与迭代沉淀 |
|---|---|---|---|---|---|---|---|
| 主覆盖 | 主覆盖 | 辅助覆盖 | 主覆盖 | 主覆盖 | 辅助覆盖 | 辅助覆盖 | 主覆盖 |

## Capabilities

- "Get Stuff Done"-style lightweight methodology — strong on planning + execution + post-action sedimentation; lighter on design and verification compared to BMAD/gstack.
- Fits teams that need workflow structure without the full BMAD/gstack artifact set.
- See `../_comparison/lifecycle-workflow-comparison.zh-CN.md § GSD` for canonical capabilities.

## Conflicts & Dependencies With Other Methods

- vs BMAD and gstack: mutually exclusive Primary Workflow candidates.
- vs Superpowers: GSD's lighter design/verification coverage often pairs with Superpowers filling those gaps; recipe should make the pairing explicit.

## Embedding Mechanics

- Required? yes (moderate) — lighter than BMAD/gstack but still a methodology adoption.
- Playbook: n/a (author when first recipe adopts it).
- Activation cost: moderate.

## Recipes That Use This Method

- (none yet)

## Source References

- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § GSD`
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 生命周期覆盖矩阵`
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 第一组：BMAD、gstack、GSD`
- `../../harness-factory/references/selection-criteria.md § Layer Defaults`
```

- [ ] **Step 5: Verify schema for all three**

Run: `for f in methods/bmad/profile.md methods/gstack/profile.md methods/gsd/profile.md; do echo "=== $f ==="; rg -n "^## " "$f"; done`
Expected: each file shows the 7 schema headings in order.

- [ ] **Step 6: Commit**

```bash
git add methods/bmad/profile.md methods/gstack/profile.md methods/gsd/profile.md
git commit -m "methods: add bmad, gstack, gsd profiles (research-only)"
```

---

## Task 6: Promote sendbox candidate (profile + embedding-playbook)

**Files:**
- Create: `methods/sendbox/profile.md`
- Create: `methods/sendbox/embedding-playbook.md`

Source letter: `../../../CodeTeam/docs/sendbox/toHarnessFactory/from-sendbox-embedding-playbook.md` (subtree-mounted at `CodeTeam/docs/sendbox/toHarnessFactory/from-sendbox-embedding-playbook.md` from current repo root — verify path before reading).

**Path verification** (run before Step 2):

Run: `ls ../docs/sendbox/toHarnessFactory/from-sendbox-embedding-playbook.md 2>/dev/null || ls ../../docs/sendbox/toHarnessFactory/from-sendbox-embedding-playbook.md 2>/dev/null || find .. -name "from-sendbox-embedding-playbook.md" 2>/dev/null | head -3`

Expected: a path is printed. Use that path for reference; if no path, the letter is not reachable from this repo and the executor must read the playbook content from this plan only (see Step 3 — the plan contains the full content needed).

- [ ] **Step 1: Create `methods/sendbox/profile.md`**

```markdown
# Profile — sendbox

## Identity

- Upstream name: sendbox-protocol (cc-sendbox)
- Layer: Harness Enhancement
- Status: new candidate
- Source location: `~/.claude/skills/sendbox-protocol/SKILL.md` (skill); upstream repo: https://github.com/JasonJarvan/cc-sendbox

## Lifecycle Coverage

Sendbox is a cross-cutting communication protocol, not a lifecycle-stage workflow. The 8-stage matrix is not the most natural fit, but for consistency:

| 目标定义 | 需求澄清 | 方案设计 | 任务规划 | 实现开发 | 测试验证 | 发布交付 | 运行反馈与迭代沉淀 |
|---|---|---|---|---|---|---|---|
| 基本不覆盖 | 辅助覆盖 | 辅助覆盖 | 辅助覆盖 | 辅助覆盖 | 辅助覆盖 | 辅助覆盖 | 辅助覆盖 |

Sendbox is "辅助覆盖" across most stages because it is the *channel*, not the *content* — every multi-session lifecycle event may produce a letter, but no stage is owned by sendbox.

## Capabilities

- File-based asynchronous letters between agent sessions (under `docs/sendbox/to<Role>/`).
- Canonical letter types: `handoff`, `plan-ready`, `greenlight`, `blocker`, `decisions`, `milestone-done`, `archived`, `promote-to-durable`, `broadcast`.
- Lifecycle disposition: `burn` (default) / `archive` / `persist` (promoted-then-burned).
- A-12 stop-and-ask pattern for boundaries the agent cannot cross unilaterally.

## Conflicts & Dependencies With Other Methods

- Depends on: nothing structurally; runs alongside any other layer.
- Companion: cc-dashboard (`methods/dashboard/profile.md`) — dashboard projects out of the sendbox letter universe; without sendbox letters, dashboard has nothing to project.
- vs Superpowers: sendbox triggers overlay Superpowers steps (plan-ready, blocker, milestone-done, broadcast) without inserting new pipeline steps.
- vs RepoMem: `promote-to-durable` letters are the canonical bridge from sendbox transient knowledge to RepoMem long-term knowledge.

## Embedding Mechanics

- Required? yes
- Playbook: `embedding-playbook.md`
- Activation cost: symlink skill + one verbatim invariant paste into target `longterm.md § Cross-Method Invariants`. Do NOT pre-scaffold `docs/sendbox/` empty directories — it grows naturally as letters are written.

## Recipes That Use This Method

- (none yet; first recipe to adopt sendbox is expected to be a successor to `openspec-superpowers-repomem` for multi-implementer scenarios)

## Source References

- `embedding-playbook.md` (this directory)
- Upstream skill: `~/.claude/skills/sendbox-protocol/SKILL.md`
- Original letter (pre-promotion): `<sender-repo>/docs/sendbox/toHarnessFactory/from-sendbox-embedding-playbook.md`
```

- [ ] **Step 2: Create `methods/sendbox/embedding-playbook.md`**

This is the promoted, flat-markdown form of the original letter (frontmatter removed; `recipients/lifecycle/on_lifecycle_end/created/created_in` fields dropped since the playbook is now a durable reference, not a transient letter).

```markdown
# Embedding playbook — sendbox-protocol into a HarnessStack repo

> Promoted from `cc-sendbox/docs/sendbox/toHarnessFactory/from-sendbox-embedding-playbook.md` on 2026-05-26. The original letter is on the sendbox-protocol `persist → promoted-then-burned` lifecycle; this is the durable form.

This playbook tells a HarnessFactory agent (1) whether the target repo needs sendbox, and (2) exactly what to do to embed it. It is HS-specific.

## 1. Prerequisite

Required pre-read (≤3 min): upstream `sendbox-protocol` self-description (`~/.claude/skills/sendbox-protocol/SKILL.md`). Everything below assumes you know what sendbox is.

Authoritative skill source: `~/.claude/skills/sendbox-protocol/SKILL.md`.

## 2. Decision tree — embed or skip?

Embed sendbox into the target HS repo when **both** dimensions hold:

### 2.1 Recipe / scale dimension

| Target recipe | Embed sendbox? |
|---|---|
| `superpowers` (no RepoMem) | Skip by default — single-session execution discipline; sendbox adds ceremony |
| `superpowers-repomem` (solo, platform/library) | Embed iff §2.2 also says yes (most solo platform repos do NOT need it) |
| `openspec-superpowers-repomem` (small-team product) | Embed by default — multi-task work commonly spawns subagents |
| `openspec-superpowers-repomem-ecc` (small-team product, hardened) | Embed by default |
| Any recipe extending a primary-workflow layer (BMAD / gstack / GSD) | Embed by default |

### 2.2 Work-mode dimension

Embed if **any** of these is plausible in the target repo's near-term work:

- A task may be dispatched to a **subagent in a different cwd / worktree / repo**
- The repo will run **multi-worktree parallel work** (orchestrator + ≥1 implementer)
- The repo will produce **A-12 stop-and-ask boundaries** that need durable record
- The repo communicates with another HS repo via a **cross-repo handoff** mechanism

If none, skip the embed even if §2.1 says embed-by-default. Re-evaluate when work mode changes.

### 2.3 Skip outcome

If skipping: do NOT create `docs/sendbox/`, do NOT touch `longterm.md`. Record the decision in the target repo's `version-plan[.{lang}].md` "future considerations" / "未来考虑" so a future factory pass can reconsider.

## 3. Embedding checklist (when §2 says embed)

### 3.1 Install the skill

```sh
ln -s /home/<user>/Codes/cc-sendbox/skills/sendbox-protocol ~/.claude/skills/sendbox-protocol
```

Verify: Claude Code recognizes `sendbox-protocol` in the skill list at next session start.

### 3.2 Add one cross-method invariant to target `longterm.md`

Paste the §5 template **verbatim** into the target's `docs/HarnessStack/longterm.md § Cross-Method Invariants`. Do NOT inline the skill body. Do NOT paraphrase the wording — the wording is part of the contract.

### 3.3 Pipeline ↔ sendbox trigger reference

Do not insert new pipeline steps. Sendbox is triggered by *conditions* that overlay existing steps:

| HS pipeline step | Condition that triggers a letter | Canonical letter type |
|---|---|---|
| Step 2 brainstorming (multi-session work) | Spawning a fresh recipient session | `handoff.md` to `to<Role>/` |
| Step 5 worktree + executing-plans | Implementer awaits orchestrator greenlight | `from-<sender>-plan-ready.md` |
| Step 5 (during implementation) | A-12 stop-and-ask hit | `from-<sender>-blocker-<topic>.md` |
| Step 7 verification | Vertical-slice acceptance gate hit | `from-<sender>-<milestone>-done.md` |
| Step 8 requesting-code-review | Orchestrator owes N decisions to one recipient | `from-<orche>-<recipient>-decisions.md` (bundled) |
| Step 9 finishing-a-development-branch | Branch close-out summary | `from-<sender>-archived.md` |
| Step 10 RepoMem.merge HITL | Promotion candidates from temp → persist | `from-<sender>-repomem-merge-promotes.md` |
| Any time | New constraint applies to all active sessions | `toAllActiveSessions/from-<orche>.md` (broadcast) |

This map is *reference*, not enforcement. Only write a letter when the Minimal Sendbox rule says you should.

### 3.4 Verification (factory side, before declaring embed done)

- Target's `CLAUDE.md` (if it has one) does NOT override or weaken the sendbox hard rules.
- Target's `docs/sendbox/` is NOT scaffolded yet — it appears the first time a letter is actually written.
- `~/.claude/skills/sendbox-protocol` is reachable from the target user's Claude Code env.
- The invariant text in §3.2 is verbatim, not paraphrased.

## 4. Anti-patterns

1. **Do not inline the skill body** into the target's `longterm.md`. Reference; do not duplicate.
2. **Do not scaffold `docs/sendbox/`** with empty subdirectories. Let it grow as letters are written.
3. **Do not embed into a `superpowers`-only recipe** unless §2.2 explicitly says so.
4. **Do not modify the skill** in the target repo. File an upstream issue against `cc-sendbox` instead.
5. **Do not write the invariant in your own words.** §5 wording is contract wording.

## 5. Copy-paste invariant template

Paste this **verbatim** into the target's `docs/HarnessStack/longterm.md § Cross-Method Invariants`:

```markdown
- **Multi-session work uses sendbox-protocol.** When a task involves multiple
  sessions, dispatched subagents, or cross-worktree coordination, the
  `sendbox-protocol` skill (see `~/.claude/skills/sendbox-protocol/SKILL.md`)
  is the canonical asynchronous channel. The main agent's `docs/sendbox/` is
  the single source of truth, and subagents in side cwds write to it by
  relative or absolute path — never fan out under their own cwd. See
  `methods/sendbox/embedding-playbook.md` for the embedding playbook.
```

If the target repo bundles a vendored copy of cc-sendbox, adjust only the path in the parenthetical reference; leave the rest unchanged.

## 6. Pointers

- Generic self-desc: upstream `sendbox-protocol` SKILL.md
- Profile: `profile.md` (this directory)
- GitHub: https://github.com/JasonJarvan/cc-sendbox
```

- [ ] **Step 3: Verify both files**

Run: `rg -n "^## " methods/sendbox/profile.md methods/sendbox/embedding-playbook.md`
Expected: profile has the 7 schema headings; playbook has §1-§6 numbered sections.

Run: `rg -n "from-sendbox-embedding-playbook" methods/sendbox/`
Expected: zero matches in the playbook body (the source letter pointer is in `profile.md § Source References`, but the playbook content stands alone).

- [ ] **Step 4: Commit**

```bash
git add methods/sendbox/profile.md methods/sendbox/embedding-playbook.md
git commit -m "methods: add sendbox candidate (profile + promoted playbook)"
```

---

## Task 7: Promote dashboard candidate (profile + embedding-playbook)

**Files:**
- Create: `methods/dashboard/profile.md`
- Create: `methods/dashboard/embedding-playbook.md`

Source letter (same path discovery as Task 6): `from-dashboard-embedding-playbook.md`.

- [ ] **Step 1: Create `methods/dashboard/profile.md`**

```markdown
# Profile — dashboard

## Identity

- Upstream name: cc-dashboard
- Layer: Harness Enhancement
- Status: new candidate
- Source location: `~/.claude/skills/cc-dashboard/SKILL.md` (skill); upstream repo: cc-dashboard

## Lifecycle Coverage

Dashboard is a projection layer over sendbox letters, not a lifecycle-stage workflow. Stage matrix for consistency:

| 目标定义 | 需求澄清 | 方案设计 | 任务规划 | 实现开发 | 测试验证 | 发布交付 | 运行反馈与迭代沉淀 |
|---|---|---|---|---|---|---|---|
| 基本不覆盖 | 辅助覆盖 | 基本不覆盖 | 基本不覆盖 | 基本不覆盖 | 基本不覆盖 | 基本不覆盖 | 辅助覆盖 |

Dashboard is "辅助覆盖" only at `需求澄清` (surfaces pending user decisions) and `运行反馈与迭代沉淀` (records resolved actions in archive). Everything else is downstream of letter-creation events.

## Capabilities

- Single markdown file (`docs/Dashboard/index.md`) projecting every pending user-blocking action from sendbox letters, handoff briefs, and external trackers.
- Atomic granularity: one letter with three asks → three dashboard rows.
- Independent lifecycle from letters (`open → done → archived`); 14-day rolling archive.
- Six action types (decision / start / review / triage / destructive / ops).

## Conflicts & Dependencies With Other Methods

- **Hard dependency: sendbox** — dashboard projects out of the sendbox letter universe. Without sendbox embedded, dashboard has nothing to project. See `methods/sendbox/profile.md`.
- Dashboard rows MUST be user-action granularity, not L2 tracker issues — if external trackers exist (Linear, Multica, Jira), dashboard does NOT mirror their tickets at L2 granularity.
- vs Superpowers: dashboard is read-only by the user; it does not gate any Superpowers pipeline step.

## Embedding Mechanics

- Required? yes
- Playbook: `embedding-playbook.md`
- Activation cost: symlink skill + create `docs/HarnessStack/hooks/cc-dashboard.md` (hook config with repo-local Language Policy) + seed `docs/Dashboard/index.md` + add rows to `longterm.md § Hooks` and `CLAUDE.md` "Where to Look" table.

## Recipes That Use This Method

- (none yet; first recipe to adopt is the same downstream multi-implementer recipe expected to adopt sendbox)

## Source References

- `embedding-playbook.md` (this directory)
- Upstream skill: `~/.claude/skills/cc-dashboard/SKILL.md`
- Original letter (pre-promotion): `<sender-repo>/docs/sendbox/toHarnessFactory/from-dashboard-embedding-playbook.md`
- Companion profile: `../sendbox/profile.md`
```

- [ ] **Step 2: Create `methods/dashboard/embedding-playbook.md`**

```markdown
# Embedding playbook — cc-dashboard into a HarnessStack repo

> Promoted from `cc-dashboard/docs/sendbox/toHarnessFactory/from-dashboard-embedding-playbook.md` on 2026-05-26. The original letter is on the sendbox-protocol `persist → promoted-then-burned` lifecycle; this is the durable form.

This playbook tells a HarnessFactory agent (1) whether the target repo needs cc-dashboard, and (2) exactly what to do to embed it when needed.

## 1. Prerequisite

Authoritative skill source: `~/.claude/skills/cc-dashboard/SKILL.md`.

**One-paragraph overview**: cc-dashboard maintains a single markdown file (`docs/Dashboard/index.md`) listing every pending action the user owes — projected out of sendbox letters, handoff briefs, and external tracker tickets. Atomic granularity. Independent lifecycle from letters (`open → done → archived`). Written by any agent session at letter/handoff creation; read by the user; mark-done by anyone observing completion.

**Required companion**: `sendbox-protocol` skill must be embedded in the target repo first. Without sendbox letters, dashboard has nothing to project.

## 2. Decision tree — embed or skip?

Embed when **all three** dimensions hold:

### 2.1 sendbox-protocol prerequisite

| Target repo state | Embed cc-dashboard? |
|---|---|
| `sendbox-protocol` not embedded | Skip — defer until sendbox is embedded |
| `sendbox-protocol` embedded but `toUser/` rarely or never used | Skip — no user-action surface to project |
| `sendbox-protocol` embedded with active `toUser/` + multi-implementer flow | Continue to §2.2 |

### 2.2 Recipe / scale dimension

| Target recipe | Embed cc-dashboard? |
|---|---|
| `superpowers` (no RepoMem) | Skip |
| `superpowers-repomem` (solo, library) | Skip by default — re-evaluate if multi-implementer work emerges |
| `openspec-superpowers-repomem` (small-team product) | Embed iff §2.3 also says yes |
| `openspec-superpowers-repomem-ecc` (small-team product, hardened) | Embed by default if §2.3 says yes |
| Any recipe extending a primary-workflow layer (BMAD / gstack / GSD) | Embed by default |

### 2.3 User-action surface dimension

Embed if **any** of these is plausible:

- ≥3 active agent sessions accumulating user-blocking asks
- A single letter typically contains ≥2 atomic user decisions/actions with distinct completion timelines
- The user wears multiple roles (driver / courier / session-starter / reviewer) and switches frequently
- External trackers exist but hold L2 work units, not user-action granularity
- Reachability test fails: the user needs to open ≥4 surfaces to answer "what do I owe right now?"

If none, skip even if §2.1 + §2.2 say embed.

### 2.4 Skip outcome

If skipping: do NOT create `docs/Dashboard/`, do NOT add a hook config. Record the decision in the target repo's `version-plan[.{lang}].md` "future considerations" / "未来考虑".

## 3. Embedding checklist (when §2 says embed)

### 3.1 Skill registration

```sh
ln -s "$(realpath ${CC_DASHBOARD_REPO})/skills/cc-dashboard" ~/.claude/skills/cc-dashboard
```

### 3.2 Hook config

Create `<target>/docs/HarnessStack/hooks/cc-dashboard.md` with these required sections:

- Status / Scope / Skip-protocol / Authority frontmatter
- Purpose paragraph
- Data Location (path + versioning policy)
- **Language Policy** — declare the `Action`-column language for THIS repo
- Row Schema (copy from upstream SKILL.md)
- Action Types (A–F)
- Write Triggers (sendbox letter / handoff / external blocker)
- Mark-Done Protocol — pick one of (a)/(b)/(c)/(d) from upstream SKILL.md
- Archive Protocol (default 14-day rolling)
- Sendbox-protocol Coupling note (independent lifecycle, overlapping triggers)
- Hook Boundary (MUST NOT modify pipeline ordering / merge gates / verification topology)

### 3.3 Data file seed

Create `<target>/docs/Dashboard/index.md` from the template in upstream SKILL.md. Backfill by scanning:

- `docs/sendbox/toUser/` letters — each atomic ask becomes 1 row (Type A/C/D)
- Active `docs/sendbox/to<Implementer>/handoff.md` files — each becomes 1 Type-B row
- External tracker assignments to the user — MRs awaiting merge → Type-C, alerts needing triage → Type-D

Mark already-completed actions directly into `## Archive` — do NOT dump them into `## Active`.

### 3.4 Wire into the target's `longterm.md`

Add a row to the `## Hooks` table:

```markdown
| [`hooks/cc-dashboard.md`](hooks/cc-dashboard.md) | active | Maintain `docs/Dashboard/index.md` as SSOT for pending user actions; trigger on any session write to `docs/sendbox/` or identification of a new user-blocking action |
```

### 3.5 Wire into the target's `CLAUDE.md` / `AGENTS.md`

Add a row to the "Where to Look" table:

```markdown
| Know what the user owes now | `docs/Dashboard/index.md` (protocol: `docs/HarnessStack/hooks/cc-dashboard.md`) |
```

### 3.6 Acceptance checklist

- [ ] `docs/Dashboard/index.md` exists with seeded Active + Archive sections
- [ ] `docs/HarnessStack/hooks/cc-dashboard.md` exists with all required sections including repo-local Language Policy
- [ ] `longterm.md § Hooks` table contains the new row
- [ ] `CLAUDE.md` / `AGENTS.md` "Where to Look" references the dashboard path
- [ ] Skill discoverable via `Skill cc-dashboard` in a fresh CC session

## 4. Co-evolution with sendbox-protocol

cc-dashboard and sendbox-protocol move together:

- If `sendbox-protocol` is upgraded (new letter types, new lifecycle states), check whether new Action Types are needed — register them in the target repo's hook config (do not extend the portable skill without recurring justification).
- If `sendbox-protocol` is retired from the target repo, retire cc-dashboard too.
- If a target repo replaces sendbox-protocol with a different inter-session-comm convention, re-evaluate cc-dashboard's fit.

## 5. Anti-patterns

Surface in your post-run report if observed:

- Dashboard rows duplicating L2 tracker issues at L2 granularity
- Dashboard rows accumulating in `## Active` without being marked done for >14 days
- `## Archive` section growing unboundedly
- Letters being burned while their derived rows remain open without explanation
- Multiple dashboard files appearing under `docs/Dashboard/` without a clear split rationale

## 6. Versioning

This playbook tracks the cc-dashboard skill version. Current: **v0.1.0 (2026-05-26)**. v0.2.x (file-split / schema extension) updates §3.2 / §3.3 shape. v0.5.x (technology-stack change to web UI / structured data) requires a major revision of this playbook.
```

- [ ] **Step 3: Verify both files**

Run: `rg -n "^## " methods/dashboard/profile.md methods/dashboard/embedding-playbook.md`
Expected: profile has 7 schema headings; playbook has §1-§6 numbered sections.

- [ ] **Step 4: Commit**

```bash
git add methods/dashboard/profile.md methods/dashboard/embedding-playbook.md
git commit -m "methods: add dashboard candidate (profile + promoted playbook)"
```

---

## Task 8: Add Step 6.5 to assembly SKILL.md

**Files:**
- Modify: `harness-factory/SKILL.md` (Workflow section: insert new step 6.5 between current steps 6 and 7)
- Modify: `harness-factory/SKILL.md § Resources` (add a `candidates/` cross-reference)

- [ ] **Step 1: Read the current Workflow section**

Run: `rg -n "^[0-9]+\. " harness-factory/SKILL.md | head -20`
Expected: numbered steps 1-13 of the Workflow section.

- [ ] **Step 2: Insert Step 6.5 (renumber subsequent steps if any tooling depends on numbering — they do not, since the Workflow uses prose numbering only)**

Find the line that starts with `6. Read [references/output-shapes.md]` and ends at the start of step `7. Pick a recipe from`. Insert this new step between them. The new content:

```markdown
6.5. Read [methods/README.md](../methods/README.md) and verify every Method named in
   the chosen scenario × recipe combination has a `methods/<method>/profile.md`.
   For any Method that requires embedding mechanics (per its profile's
   `Embedding Mechanics § Required?` field), read its `embedding-playbook.md`
   before continuing to step 7. The assembly layer MUST NOT invent facts about
   a Method that the candidate layer does not state — if a profile is missing
   a fact you need, surface the gap (do not silently fill it in the recipe or
   long-term contract).
```

- [ ] **Step 3: Update `## Resources` section**

Find the `## Resources` heading. Add a new subsection at the top of Resources (before `### assets/templates/`):

```markdown
### Candidate Layer (read-only)

- `../methods/README.md`: the candidate-layer contract and per-method profile schema
- `../methods/<method>/profile.md`: per-method profile (one per supported Method)
- `../methods/<method>/embedding-playbook.md`: embedding playbook for Methods that need one
- `../methods/_comparison/lifecycle-workflow-comparison.zh-CN.md`: cross-method analysis

The assembly layer reads candidate-layer files; it MUST NOT write to them. See
`methods/README.md § Read-only contract with the assembly layer` for the full rule.
```

- [ ] **Step 4: Verify the edit**

Run: `rg -n "6.5|Candidate Layer \(read-only\)" harness-factory/SKILL.md`
Expected: at least 2 matches — Step 6.5 in Workflow and `### Candidate Layer (read-only)` in Resources.

- [ ] **Step 5: Commit**

```bash
git add harness-factory/SKILL.md
git commit -m "assembly: SKILL.md cite candidate layer (Step 6.5 + Resources)"
```

---

## Task 9: Add reverse links in selection-criteria.md

**Files:**
- Modify: `harness-factory/references/selection-criteria.md` (Layer Defaults section)

- [ ] **Step 1: Locate Layer Defaults section**

Run: `rg -n "^## Layer Defaults|^### solo|^### small-team|^### large-team" harness-factory/references/selection-criteria.md`
Expected: Layer Defaults at line ~58 (per plan-time inspection) + the three scenario subsections.

- [ ] **Step 2: For each Method named in any of the three scenario blocks, add an inline candidate-layer link**

In each scenario block, replace each bullet that names a Method with the same text **followed by** ` → \`methods/<method>/profile.md\``.

Replacements (perform via Edit tool one at a time to preserve formatting):

In `### solo`:
- `- Prefer \`Superpowers\`` → `- Prefer \`Superpowers\` → \`methods/superpowers/profile.md\``
- `- Add \`RepoMem\` when the repository is long-lived` → `- Add \`RepoMem\` when the repository is long-lived → \`methods/repomem/profile.md\``
- `- Add \`OpenSpec\` when changes need stable spec boundaries` → `- Add \`OpenSpec\` when changes need stable spec boundaries → \`methods/openspec/profile.md\``
- `- Enable \`ECC\` lightly when memory, hooks, or verification benefit the repository` → `- Enable \`ECC\` lightly when memory, hooks, or verification benefit the repository → \`methods/ecc/profile.md\``

In `### small-team`:
- `- Prefer \`Superpowers + RepoMem\`` → `- Prefer \`Superpowers + RepoMem\` → \`methods/superpowers/profile.md\`, \`methods/repomem/profile.md\``
- `- Add \`OpenSpec\` as the normal spec layer once collaboration cost rises` → `- Add \`OpenSpec\` as the normal spec layer once collaboration cost rises → \`methods/openspec/profile.md\``
- `- Add \`ECC\` at medium strength when shared context and guardrails matter` → `- Add \`ECC\` at medium strength when shared context and guardrails matter → \`methods/ecc/profile.md\``
- `- Add a stronger primary workflow only when simple execution discipline is no longer enough` → `- Add a stronger primary workflow only when simple execution discipline is no longer enough → \`methods/bmad/profile.md\`, \`methods/gstack/profile.md\`, \`methods/gsd/profile.md\``

In `### large-team`:
- `- Prefer \`OpenSpec + RepoMem + ECC\` as the default baseline` → `- Prefer \`OpenSpec + RepoMem + ECC\` as the default baseline → \`methods/openspec/profile.md\`, \`methods/repomem/profile.md\`, \`methods/ecc/profile.md\``
- `- Keep \`Superpowers\` as the execution discipline layer` → `- Keep \`Superpowers\` as the execution discipline layer → \`methods/superpowers/profile.md\``
- `- Upgrade the primary workflow to a heavier planning system when coordination cost is high` → `- Upgrade the primary workflow to a heavier planning system when coordination cost is high → \`methods/bmad/profile.md\`, \`methods/gstack/profile.md\`, \`methods/gsd/profile.md\``

- [ ] **Step 3: Verify all 9 Methods are reverse-linked**

Run: `rg -n "methods/(superpowers|repomem|openspec|ecc|bmad|gstack|gsd)/profile\.md" harness-factory/references/selection-criteria.md | wc -l`
Expected: ≥ 11 (counting multi-link bullets in small-team and large-team).

- [ ] **Step 4: Commit**

```bash
git add harness-factory/references/selection-criteria.md
git commit -m "assembly: selection-criteria.md reverse-link to candidate profiles"
```

---

## Task 10: Add `Method References:` field to recipe-template.md

**Files:**
- Modify: `harness-factory/assets/templates/recipes/recipe-template.md` (add new section between `## Layer Assignments` and `## End-to-End Pipeline`)

- [ ] **Step 1: Locate insertion point**

Run: `rg -n "^## Layer Assignments|^## End-to-End Pipeline" harness-factory/assets/templates/recipes/recipe-template.md`
Expected: Layer Assignments at ~line 32, End-to-End Pipeline at ~line 42.

- [ ] **Step 2: Insert new section between Layer Assignments and End-to-End Pipeline**

After the line `If a layer is intentionally inactive, write \`none\` and add an \`Emergent Ownership\` note under Primary if its responsibility is carried by other layers.` and before the line `## End-to-End Pipeline`, insert:

```markdown
## Method References

List the candidate-layer profile for each Method named under `Layer Assignments`.
One bullet per Method. The assembly layer reads these profiles to check
Lifecycle Coverage, Capabilities, and Conflicts before composing inter-layer
rules in this recipe. If a Method is named under Layer Assignments but has no
profile in `methods/`, that is a defect — pause and author the profile first.

- <method-name> → `methods/<method-name>/profile.md`

When a Method has an `embedding-playbook.md`, also link it:

- <method-name> → `methods/<method-name>/profile.md` (playbook: `methods/<method-name>/embedding-playbook.md`)
```

- [ ] **Step 3: Verify**

Run: `rg -n "^## Method References" harness-factory/assets/templates/recipes/recipe-template.md`
Expected: 1 match.

- [ ] **Step 4: Commit**

```bash
git add harness-factory/assets/templates/recipes/recipe-template.md
git commit -m "assembly: recipe-template.md add Method References field"
```

---

## Task 11: Sync RepoMem (factory-iteration-layers + version-plan)

**Files:**
- Modify: `docs/RepoMem/persist/memory/factory-iteration-layers.md`
- Modify: `docs/RepoMem/persist/version-plan.md`

- [ ] **Step 1: Update factory-iteration-layers.md**

In `docs/RepoMem/persist/memory/factory-iteration-layers.md`, find the `### 调研层 (Research Layer)` subsection and replace its body with this updated content (keep the heading):

```markdown
### 调研层 (Research Layer)

- 责任：维护每个 Harness Method（Superpowers / OpenSpec / RepoMem / ECC / BMAD / gstack / GSD / sendbox / dashboard / ...）
  的 profile（身份/生命周期覆盖/能力/冲突依赖/embedding）与跨方法对比。
- 维护方式：人 + agent 手工产出 profile；跨方法分析 (`_comparison/`) 同样手工维护；未来可考虑周期性 agent 维护。
- 物理目录（v0.4 落地于 2026-05-26）：`methods/`
  - `methods/README.md` — 候选层契约 + profile schema + 添加新候选的判据
  - `methods/<method>/profile.md` — per-method profile（schema 固定）
  - `methods/<method>/embedding-playbook.md` — embedding 机制非平凡的方法的落地手册
  - `methods/_comparison/lifecycle-workflow-comparison.zh-CN.md` — 跨方法生命周期对比（从 docs/ 搬过来）
```

Also update the `### 推断层 (Inference Layer)` subsection's third bullet to clarify the read-only contract — find the constraint section `## Constraints` and replace its first bullet with:

```markdown
- 推断层只读候选层产物，不直接读 Method 源仓库。候选层（`methods/`）是中间表。
  契约见 `../../../methods/README.md § Read-only contract with the assembly layer`。
```

- [ ] **Step 2: Add v0.4 section to version-plan.md**

In `docs/RepoMem/persist/version-plan.md`, find the `## 未来考虑` heading and insert a new `## v0.4 目标` + `## v0.4 决策与改动` pair BEFORE it (so the new v0.4 section goes between v0.3.2 and 未来考虑):

```markdown
## v0.4 目标

- 把已被 RepoMem 概念化但物理未落地的"调研层"显式化为顶层 `methods/` 目录
- 给每个已被 recipe 字面引用的方法（superpowers / repomem / openspec / ecc）补 profile
- 给在 selection-criteria 中作为"Default inactive"上调选项的方法（bmad / gstack / gsd）补 profile（status = research-only）
- 把外部 sendbox / dashboard 两个 playbook letter 晋升为候选层一级公民（profile + flat-markdown playbook）
- 让组装层（harness-factory/）显式 cite 候选层（SKILL.md Step 6.5 + selection-criteria 反链 + recipe-template 加 Method References 字段）

## v0.4 决策与改动

- 顶层新增 `methods/` 与 `harness-factory/`、`docs/`、`output/` 平级
- 不改 `harness-factory/` 名称（重命名为 `assembly/` 留作 v0.5 候选）
- 候选层维护 9 个 method 目录：superpowers, repomem, openspec, ecc, bmad, gstack, gsd, sendbox, dashboard
- 不动 `docs/CN/`（继续 freeze 在 v0.2）
- 不在本次为 sendbox / dashboard 增加新 recipe（recipe 编写是后续动作；profile 解锁但不要求）
- 源信 `from-{sendbox,dashboard}-embedding-playbook.md` 不在本任务里 burn，由 sendbox-protocol 的清扫机制处置
```

- [ ] **Step 3: Verify**

Run: `rg -n "methods/" docs/RepoMem/persist/memory/factory-iteration-layers.md`
Expected: at least 4 matches (the new path mentions).

Run: `rg -n "## v0.4" docs/RepoMem/persist/version-plan.md`
Expected: 2 matches (v0.4 目标 + v0.4 决策与改动).

- [ ] **Step 4: Commit**

```bash
git add docs/RepoMem/persist/memory/factory-iteration-layers.md docs/RepoMem/persist/version-plan.md
git commit -m "repomem: sync candidate-layer extraction (v0.4)"
```

---

## Task 12: Final cross-validation

No new files. This task is a sweep that asserts the whole refactor is internally consistent. If any check fails, stop and fix before declaring done.

- [ ] **Step 1: Every recipe-named Method has a profile**

Run:
```bash
for m in superpowers repomem openspec ecc bmad gstack gsd sendbox dashboard; do
  test -f "methods/$m/profile.md" || echo "MISSING: methods/$m/profile.md"
done
```
Expected: no output (every file exists).

- [ ] **Step 2: Every profile follows the schema**

Run:
```bash
for f in methods/*/profile.md; do
  count=$(rg -c "^## (Identity|Lifecycle Coverage|Capabilities|Conflicts & Dependencies With Other Methods|Embedding Mechanics|Recipes That Use This Method|Source References)$" "$f")
  test "$count" = "7" || echo "SCHEMA DEFECT: $f has $count of 7 required sections"
done
```
Expected: no output.

- [ ] **Step 3: Methods requiring embedding have a playbook**

Run:
```bash
for f in methods/*/profile.md; do
  if rg -q "^- Required\? yes" "$f" && ! rg -q "^- Playbook: \`embedding-playbook.md\`" "$f"; then
    dir=$(dirname "$f")
    if ! test -f "$dir/embedding-playbook.md"; then
      # legitimate "n/a" playbooks (repomem, openspec, ecc, bmad, gstack, gsd) are allowed
      if ! rg -q "^- Playbook: n/a" "$f"; then
        echo "MISSING PLAYBOOK: $f says Required? yes but no embedding-playbook.md or n/a"
      fi
    fi
  fi
done
```
Expected: no output (sendbox and dashboard have playbook files; others legitimately declare `n/a`).

- [ ] **Step 4: No stale references to the old comparison-doc path**

Run: `rg -n "docs/analysis-lifecycle-workflow-comparison" .`
Expected: no output.

- [ ] **Step 5: Assembly layer cites candidate layer**

Run:
```bash
rg -n "methods/" harness-factory/SKILL.md harness-factory/references/selection-criteria.md harness-factory/assets/templates/recipes/recipe-template.md | wc -l
```
Expected: ≥ 15 (citations across SKILL.md Step 6.5 + Resources, selection-criteria reverse links across 3 scenarios, recipe-template Method References section).

- [ ] **Step 6: Top-level README directory tree mentions `methods/`**

Run: `rg -n "^├── methods/" README.md`
Expected: 1 match.

- [ ] **Step 7: RepoMem reflects the new layer location**

Run: `rg -n "methods/" docs/RepoMem/persist/memory/factory-iteration-layers.md`
Expected: ≥ 4 matches.

- [ ] **Step 8: Branch is clean and commit history is sensible**

Run: `git status && git log --oneline -15`
Expected: clean working tree; ~11 commits with `methods:` / `assembly:` / `repomem:` prefixes.

- [ ] **Step 9: No commit required (verification-only task)**

If all checks above passed, the refactor is complete. If any failed, open the failing file, fix in place, and rerun the failed check before declaring done.

---

## Self-Review Notes (for the writing-plans skill — not for execution)

- **Spec coverage:** the user agreed to (1) `methods/` directory, (2) no rename of `harness-factory/`, (3) playbooks as flat markdown + original letters burned via sendbox-protocol (out of scope here), (4) SKILL.md Step 6.5 + selection-criteria reverse links + recipe-template Method References. Tasks 1-7 cover (1) and (3) (promotion); Tasks 8-10 cover (4); (2) is enforced by absence of any rename task. RepoMem sync (Task 11) was implied by the work but not asked explicitly — it preserves the repo's own contract about version-plan + factory-iteration-layers being authoritative.
- **Placeholder scan:** every step has either a complete file content block, an exact path edit instruction, or a verification command. No "TBD" / "fill in details".
- **Type consistency:** the 7 schema headings are quoted verbatim across Task 1 (README), Tasks 3-7 (profile creation), and Task 12 Step 2 (validation). `Required? yes` and `Required? no` and `Playbook: n/a` are quoted consistently across profiles and Task 12 Step 3.
