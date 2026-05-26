# HarnessFactory Rename & Output Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Execute the v0.3 redesign — rename repository to HarnessFactory, rename factory source dir, restructure output to `./output/<run>/HarnessStack/`, add top-level distillation README, clean up stale docs, and sync supporting memory.

**Architecture:** Pure documentation/methodology refactor. No runtime code. "Tests" are grep-based invariant checks and file-existence checks. Each task produces an atomic, independently committable change. Source spec: `docs/superpowers/specs/2026-05-14-harness-factory-rename-and-output-redesign-design.md`.

**Tech Stack:** Markdown, YAML frontmatter, git, ripgrep for verification.

---

## Per-Occurrence Rewriting Rule (used by Tasks 3, 4, 8)

When editing any file, apply this rule per occurrence of `HarnessStack` or `harness-stack`:

| Pattern | Action |
|---|---|
| "HarnessStack 仓库" / "the HarnessStack repository" (= the method repo itself) | → `HarnessFactory` |
| "HarnessStack model" / "HarnessStack 模型" | → `HarnessFactory model that generates HarnessStacks` |
| "a HarnessStack" / "the HarnessStack" / "produces HarnessStacks" (= the artifact) | **keep unchanged** |
| `` `harness-stack/` `` path (factory source dir) | → `` `harness-factory/` `` |
| `` `docs/HarnessStack/` `` path (target activation dir) | **keep unchanged** |
| `name: harness-stack` (SKILL.md frontmatter) | → `name: harness-factory` |
| `display_name: "Harness Stack"` (agents/openai.yaml) | **keep** (display name reflects artifact) |
| "$harness-stack" / variable refs | → `$harness-factory` |

---

## Task 1: Cleanup stale documents

**Files:**
- Delete: `docs/handoff/3method-iteration-2026-05-07.md`
- Delete: `docs/examples/openspec-superpowers-repomem-longterm.md`
- Delete: `docs/examples/openspec-superpowers-repomem-longterm_v1.md`
- Delete (recursive): `docs/examples/openspec-superpowers-repomem-ecc-activation-kit/`
- Delete (empty dir after): `docs/handoff/`

- [ ] **Step 1: Verify no inbound references before deleting**

Run:
```bash
cd D:/Documents/Codes/Source_Jason/Tool_Dev/HarnessStack
rg -l "openspec-superpowers-repomem-longterm\.md|openspec-superpowers-repomem-longterm_v1|openspec-superpowers-repomem-ecc-activation-kit|3method-iteration-2026-05-07"
```
Expected: only matches inside the files being deleted themselves; no inbound references from `harness-stack/` or `docs/RepoMem/persist/`.

- [ ] **Step 2: Delete files**

```bash
rm "docs/handoff/3method-iteration-2026-05-07.md"
rm "docs/examples/openspec-superpowers-repomem-longterm.md"
rm "docs/examples/openspec-superpowers-repomem-longterm_v1.md"
rm -rf "docs/examples/openspec-superpowers-repomem-ecc-activation-kit"
rmdir "docs/handoff"
```

- [ ] **Step 3: Verify deletions and remaining example files**

```bash
ls docs/examples/
ls docs/ | grep -v handoff
```
Expected:
- `docs/examples/` contains exactly: `openspec-superpowers-repomem-longterm_orient.md`, `superpowers-only-longterm.md`
- `docs/` no longer lists `handoff`

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "$(cat <<'EOF'
chore(cleanup): remove stale handoff and example docs

Removes pre-v0.3 example outputs and the 2026-05-07 handoff snapshot.
Kept examples are the two referenced by recipes
(superpowers-only-longterm.md, openspec-superpowers-repomem-longterm_orient.md).
Empty docs/handoff/ directory removed.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 2: Rename factory source directory (pure rename, no content edits)

**Files:**
- Move: `harness-stack/` → `harness-factory/` (recursive, git-tracked)

- [ ] **Step 1: Pre-rename inventory**

```bash
ls harness-stack/
```
Expected: `SKILL.md  agents  assets  references`

- [ ] **Step 2: Git rename**

```bash
git mv harness-stack harness-factory
git status
```
Expected: all child files show as renamed (`R`) with no content changes.

- [ ] **Step 3: Verify new path works and old is gone**

```bash
ls harness-factory/
test ! -d harness-stack/ && echo "old dir removed OK"
```
Expected: `SKILL.md  agents  assets  references` and `old dir removed OK`.

- [ ] **Step 4: Commit the rename only**

```bash
git commit -m "$(cat <<'EOF'
refactor: rename factory source dir harness-stack/ → harness-factory/

Pure path rename committed separately so the diff shows only renames.
Internal content rewrites follow in the next task.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 3: Rewrite internal references inside `harness-factory/`

**Files (edit in place):**
- `harness-factory/SKILL.md`
- `harness-factory/agents/openai.yaml`
- `harness-factory/references/selection-criteria.md`
- `harness-factory/references/question-flow.md`
- `harness-factory/references/questionnaire.md`
- `harness-factory/references/output-shapes.md`
- `harness-factory/assets/templates/longterm-template.md`
- `harness-factory/assets/templates/temporary-template.md`
- `harness-factory/assets/templates/longterm/solo.md`
- `harness-factory/assets/templates/longterm/small-team.md`
- `harness-factory/assets/templates/longterm/large-team.md`
- `harness-factory/assets/templates/temporary/clear.md`
- `harness-factory/assets/templates/temporary/partially-clear.md`
- `harness-factory/assets/templates/temporary/vague.md`
- `harness-factory/assets/templates/recipes/recipe-template.md`
- `harness-factory/assets/templates/recipes/superpowers.md`
- `harness-factory/assets/templates/recipes/superpowers-repomem.md`
- `harness-factory/assets/templates/recipes/openspec-superpowers-repomem.md`
- `harness-factory/assets/templates/recipes/openspec-superpowers-repomem-ecc.md`

- [ ] **Step 1: Apply per-occurrence rule to SKILL.md**

Edit `harness-factory/SKILL.md`:
- Frontmatter: `name: harness-stack` → `name: harness-factory`
- Frontmatter description: replace "HarnessStack model" → "HarnessFactory model that generates HarnessStacks"
- Body: `# Harness Stack` heading → `# Harness Factory`
- Body: every "harness-stack/" path → "harness-factory/"
- Body: keep every "docs/HarnessStack/" target-side path
- Body: keep "a HarnessStack" / "the HarnessStack" artifact references

- [ ] **Step 2: Apply per-occurrence rule to agents/openai.yaml**

Edit `harness-factory/agents/openai.yaml`:
- `default_prompt: "Use $harness-stack ..."` → `default_prompt: "Use $harness-factory ..."`
- `display_name: "Harness Stack"` → keep (this is the artifact's display name shown to users)
- `short_description` → no change

- [ ] **Step 3: Apply per-occurrence rule to every file in `references/` and `assets/templates/`**

For each file listed above, scan for the patterns in the per-occurrence rule table and apply.

Critical patterns to watch:
- `Source Template:` field values that point at template paths use `harness-factory/...`
- `Recipe Reference:` field values that point at recipe paths use `harness-factory/...`
- Examples in templates referring to "在 HarnessStack 仓库中" → "在 HarnessFactory 仓库中"
- "HarnessStack 长期 contractor" / "HarnessStack 临时 contractor" → keep these (HarnessStack here is the model name applied to its components, kept per artifact-vs-repo distinction)
- All "docs/HarnessStack/" paths → unchanged

- [ ] **Step 4: Verify expected residuals (artifact-side mentions only)**

```bash
rg -n "harness-stack" harness-factory/
```
Expected: no matches (factory source dir name fully replaced).

```bash
rg -n "HarnessStack" harness-factory/ | head -50
```
Expected: ONLY matches like `docs/HarnessStack/` (target path), `a HarnessStack` / `the HarnessStack` (artifact references), and "HarnessStack" as a model/concept name. No matches that mean "this method repository".

- [ ] **Step 5: Commit**

```bash
git add harness-factory/
git commit -m "$(cat <<'EOF'
refactor(factory): rewrite internal references for HarnessFactory naming

Updates SKILL.md frontmatter name, internal paths, recipe references,
and prose to reflect that this directory is the factory source. Keeps
'HarnessStack' wherever it refers to the produced artifact, and keeps
docs/HarnessStack/ target-side paths unchanged.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 4: Sync the Chinese mirror under `docs/CN/`

**Files:**
- `docs/CN/SKILL.md`
- `docs/CN/agents/openai.yaml`
- `docs/CN/references/selection-criteria.md`
- `docs/CN/references/question-flow.md`
- `docs/CN/references/questionnaire.md`
- `docs/CN/references/output-shapes.md`
- `docs/CN/assets/templates/longterm-template.md`
- `docs/CN/assets/templates/temporary-template.md`
- `docs/CN/assets/templates/longterm/{solo,small-team,large-team}.md`
- `docs/CN/assets/templates/temporary/{clear,partially-clear,vague}.md`

- [ ] **Step 1: Apply the same per-occurrence rule to each CN mirror file**

For each file, perform the same edits as Task 3 (SKILL.md frontmatter name → `harness-factory`, paths `harness-stack/` → `harness-factory/`, "HarnessStack 仓库" → "HarnessFactory 仓库", artifact mentions unchanged, target-side paths unchanged).

- [ ] **Step 2: Verify**

```bash
rg -n "harness-stack" docs/CN/
```
Expected: no matches.

```bash
rg -n "HarnessStack" docs/CN/ | head -30
```
Expected: only target paths and artifact references.

- [ ] **Step 3: Commit**

```bash
git add docs/CN/
git commit -m "$(cat <<'EOF'
refactor(cn-mirror): sync HarnessFactory naming in Chinese mirror

Same rewrites as harness-factory/ applied to docs/CN/ to keep the
bilingual surface consistent.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 5: Update `output-shapes.md` for new output structure (EN + CN)

**Files:**
- Modify: `harness-factory/references/output-shapes.md`
- Modify: `docs/CN/references/output-shapes.md`

- [ ] **Step 1: Replace the file paths in the three Output Modes (EN)**

Open `harness-factory/references/output-shapes.md`. Anywhere a path like
`docs/HarnessStack/longterm.md` describes **factory output destination**
(not target activation), replace with the new layout. Specifically, add a new
top-level section **before** the existing "Output Modes" section:

```markdown
## Output Destination

Every factory run emits one bundle under `./output/`. The bundle's inner
directory is named `HarnessStack/` so it can be copied directly to
`<target-repo>/docs/HarnessStack/` without renaming.

```
./output/{YYYY-MM-DD-HHmm}-{scale}-{horizon}/HarnessStack/
├── README.md                    # AI distillation index (rendered from output-readme-template.md)
├── longterm.md                  # core long-term contract
├── temporary-<task>.md          # task-level patch (when there is a current task)
└── _reference/
    ├── README.md                # full human-facing usage manual
    └── version-plan-skeleton.md # multi-version roadmap skeleton
```

### Run Directory Naming

- Time precision: `YYYY-MM-DD-HHmm` (minute-level).
- Situation segment: `{scale}-{horizon}` only.
  - `scale`: `solo` | `small-team` | `large-team`.
  - `horizon` (path-abbreviated): `short` | `long`. The canonical
    questionnaire values are `short-lived` and `long-lived`; the skill maps
    them to the abbreviated form when constructing the directory name.
- Examples: `2026-05-14-1530-solo-long`, `2026-05-14-1612-small-team-long`.

### Why `repository type` Is NOT In The Directory Name

Repository type is captured in the contract metadata and acts as a veto
filter in recipe `Compatible Scenarios`. It does not positively select any
layer — see `selection-criteria.md § Layer Defaults`. The same
`(scale, horizon)` with different `type` values produces a byte-identical
layer activation when the same recipe is chosen. Type stays as a
questionnaire input (for recipe filtering) but is excluded from the path.

### Recipe Slug

Not part of the path. Recorded inside the bundle in `longterm.md § Recipe
Reference` and in `README.md § Identity / Active Methods`.
```

- [ ] **Step 2: Update existing Output Modes language to reference factory-side path**

In the same file, the existing "Required outputs" lists currently say things
like `one complete docs/HarnessStack/temporary-<task>.md`. Those describe the
**target-side** destination, which remains the canonical form for documents
once deployed. Add a parenthetical clarification at the top of "## Output
Modes":

```markdown
## Output Modes

> Modes below describe the **logical contracts** that get produced. Their
> physical files land first under `./output/<run>/HarnessStack/` (see
> § Output Destination), then are copied to `<target-repo>/docs/HarnessStack/`
> on deployment. The paths shown below use the target-side form for
> readability; the factory-side path is the same filename under
> `./output/<run>/HarnessStack/`.
```

Leave the existing Mode A / B / C definitions as-is.

- [ ] **Step 3: Same edits in CN mirror**

Apply the equivalent edits to `docs/CN/references/output-shapes.md`,
translated into Chinese in the same prose style as the rest of that file.

- [ ] **Step 4: Verify**

```bash
rg -n "\./output/" harness-factory/references/output-shapes.md
rg -n "\./output/" docs/CN/references/output-shapes.md
```
Expected: matches found in both files showing the new run-directory pattern.

- [ ] **Step 5: Commit**

```bash
git add harness-factory/references/output-shapes.md docs/CN/references/output-shapes.md
git commit -m "$(cat <<'EOF'
feat(output-shape): add factory-side output destination structure

Defines ./output/{YYYY-MM-DD-HHmm}-{scale}-{horizon}/HarnessStack/ as the
canonical factory-side path. Documents why repository type is excluded
from the path. Adds clarification that existing Mode A/B/C target paths
remain target-side; their factory-side mirrors live under the run dir.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 6: Add the top-level output README template + rendering rule

**Files:**
- Create: `harness-factory/assets/templates/output-readme-template.md`
- Modify: `harness-factory/SKILL.md` (add a workflow step for rendering this)
- Modify: `docs/CN/SKILL.md` (mirror)

- [ ] **Step 1: Create the output-readme template (EN)**

Create file `harness-factory/assets/templates/output-readme-template.md`:

```markdown
# HarnessStack — {Repository} at {Scale}/{Horizon}

> One-time distillation source for an AI agent operating in the target
> repository. Read once, condense sections 1–4 into `CLAUDE.md`, then
> consult `longterm.md` for full detail. Re-read this file only on recipe
> upgrade.

## 1. Identity

This repository runs HarnessStack at `{scale}` scale, horizon `{horizon}`.

- **Active recipe:** `{recipe-slug}`
- **Source template:** `{source-template-path}`
- **Effective from:** {effective-from-date}

## 2. Active Methods

{render one bullet per active method from the recipe's layer set, with a one-line responsibility, e.g.:}

- `Superpowers` — execution discipline (TDD, brainstorming, writing-plans, verification, finishing-a-development-branch).
- `OpenSpec` — spec layer; one task uses one `change-id`.
- `RepoMem` — long-term repository memory (persist + temp split).
- `ECC(medium)` — harness enhancement (pre-commit hooks, session-state, security scan).

## 3. Per-Task Pipeline (Compressed)

> This is the compressed view. **It is not authoritative.** For the full
> step list, conflict rules, and exception handling, see
> `longterm.md § Pipeline`.

{render 7–10 condensed steps from the active recipe's Pipeline, e.g.:}

1. `RepoMem.read` — load relevant persist memory.
2. `brainstorming` — establish design and approval gate.
3. `OpenSpec.explore` + `OpenSpec.propose` — produce change set.
4. `writing-plans` — produce implementation plan.
5. Execute (TDD; `ECC.session-state.persist` continuous; `RepoMem.capture` continuous).
6. `pre-commit-eval` and `security-scan` (if dependencies changed).
7. Dual verification: `OpenSpec.verify` + `Superpowers.verification-before-completion`.
8. `requesting-code-review`.
9. `finishing-a-development-branch`.
10. `OpenSpec.archive` + `RepoMem.merge` (HITL).

## 4. Hard Invariants

- `<task>` = `change-id` = `<slug>` — one identifier across OpenSpec, RepoMem, and HarnessStack docs.
- **Add-only**: a method that has been activated never deactivates; upgrades are extensions, never replacements.
- **Dual-verification gate**: both `OpenSpec.verify` and `Superpowers.verification-before-completion` MUST pass before `finishing-a-development-branch`.
- Task-level documents do not duplicate content (see `longterm.md § Cross-Method Invariants`).

## 5. Where To Read More

- Full long-term contract: `./longterm.md`
- Full usage manual (Day-One Init, per-task iteration, long-term iteration): `./_reference/README.md`
- Task-level patch (if a task is in progress): `./temporary-<task>.md`

## 6. For AI Consumers

Distill sections 1–4 into `CLAUDE.md` (or the equivalent always-loaded
instruction file in your harness). Do not duplicate `longterm.md` verbatim;
the contract remains the authoritative source for details. Re-read this
README only on recipe upgrade or full rewrite events.
```

- [ ] **Step 2: Add a workflow step to SKILL.md for rendering README**

Open `harness-factory/SKILL.md`. In the "Workflow" section, after the step
that fills `longterm-template.md`, add a new numbered step:

```markdown
N. Render the top-level output README from
   `assets/templates/output-readme-template.md`, populating Identity,
   Active Methods, and the Compressed Pipeline from the same recipe used
   to fill `longterm.md`. The Compressed Pipeline (§3) MUST be derived from
   the recipe's Pipeline definition in one pass — do not author it
   independently of `longterm.md § Pipeline`. Place the rendered file at
   `<output>/HarnessStack/README.md`.
```

Renumber subsequent steps accordingly.

- [ ] **Step 3: Mirror in CN SKILL.md**

Apply the equivalent edit to `docs/CN/SKILL.md` in Chinese.

- [ ] **Step 4: Verify**

```bash
test -f harness-factory/assets/templates/output-readme-template.md && echo "EN template exists"
rg -n "output-readme-template" harness-factory/SKILL.md docs/CN/SKILL.md
```
Expected: `EN template exists` and at least one match in each SKILL.md.

- [ ] **Step 5: Commit**

```bash
git add harness-factory/assets/templates/output-readme-template.md harness-factory/SKILL.md docs/CN/SKILL.md
git commit -m "$(cat <<'EOF'
feat(template): add top-level output README template

Adds the AI-distillation README that lives at <output>/HarnessStack/README.md.
Sections 1–4 are intended for the target repo's AI to condense into CLAUDE.md.
Section 3 (Compressed Pipeline) is labeled non-authoritative and must be
rendered from the same recipe source as longterm.md § Pipeline to prevent
drift. SKILL.md gains a workflow step that renders this template alongside
longterm.md.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 7: Rename `_kit-reference` → `_reference` references throughout factory

**Files:**
- Modify any file in `harness-factory/`, `docs/CN/`, or top-level docs that mentions `_kit-reference`.

- [ ] **Step 1: Survey current usage**

```bash
rg -n "_kit-reference" harness-factory/ docs/CN/ docs/RepoMem/
```
Expected: matches in `output-shapes.md`, SKILL.md, possibly elsewhere. (Note: any matches inside `docs/superpowers/specs/` may stay as historical references; the cleanup task already removed the example kit folder that physically used `_kit-reference/`.)

- [ ] **Step 2: Replace `_kit-reference` → `_reference` in each matching file**

For every file from the survey (except `docs/superpowers/specs/`), update
`_kit-reference` to `_reference`. Where the prose says "the `_kit-reference/`
directory" rewrite to "the `_reference/` directory".

- [ ] **Step 3: Verify**

```bash
rg -n "_kit-reference" harness-factory/ docs/CN/ docs/RepoMem/
```
Expected: no matches.

```bash
rg -n "_reference/" harness-factory/ docs/CN/ | head
```
Expected: at least one match per file that previously referenced `_kit-reference`.

- [ ] **Step 4: Commit**

```bash
git add harness-factory/ docs/CN/ docs/RepoMem/
git commit -m "$(cat <<'EOF'
refactor(template): _kit-reference/ → _reference/ in factory templates

Drops the 'kit' word now that the artifact is named HarnessStack rather than
'a kit'. Preserves the leading underscore which marks the directory as
orthogonal to the active contract (deletable post-activation).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 8: Update RepoMem persist memory

**Files:**
- `docs/RepoMem/persist/memory/workflow-system.md`
- `docs/RepoMem/persist/memory/contractor-output.md`
- `docs/RepoMem/persist/memory/github-repo-design.md`
- `docs/RepoMem/persist/memory/cross-method-invariants.md`
- `docs/RepoMem/persist/memory/execution-policy.md`
- `docs/RepoMem/persist/memory/template-evolution.md`
- `docs/RepoMem/persist/architecture/workflow-system.md`

- [ ] **Step 1: Apply per-occurrence rule to each file**

For each file, apply the rule. Specific high-frequency rewrites:

- "多工作流契约体系的 GitHub 仓库名确定为 `HarnessStack`" → "多工作流契约体系的 GitHub 仓库名确定为 `HarnessFactory`；每次产出物称为 `a HarnessStack`"
- "方法仓库 `HarnessStack`" → "方法仓库 `HarnessFactory`"
- "`harness-stack/`" → "`harness-factory/`"
- "`docs/HarnessStack/`" → keep unchanged
- "目标开发仓库中的 `HarnessStack/` 目录" → keep unchanged

Also update `last_reviewed_at:` frontmatter to `2026-05-14` on every file edited.

- [ ] **Step 2: Update cross-method-invariants.md's parenthetical**

In `cross-method-invariants.md` Pitfalls section, the line:
`该规则不约束方法仓库自身（HarnessStack），只约束目标开发仓库；`
→ rewrite to:
`该规则不约束方法仓库自身（HarnessFactory），只约束目标开发仓库；`

- [ ] **Step 3: Verify**

```bash
rg -n "HarnessStack 仓库|harness-stack/" docs/RepoMem/persist/
```
Expected: no matches (every "method repo" reference uses HarnessFactory now; every `harness-stack/` factory path uses `harness-factory/`).

```bash
rg -n "HarnessFactory" docs/RepoMem/persist/ | head
```
Expected: multiple matches across the updated files.

- [ ] **Step 4: Commit**

```bash
git add docs/RepoMem/persist/
git commit -m "$(cat <<'EOF'
docs(repo-mem): rewrite persist memory for HarnessFactory naming

Updates persist architecture and memory files so the method-repo identity
is HarnessFactory and the artifact identity is 'a HarnessStack'. Target-side
docs/HarnessStack/ paths are preserved. Refreshes last_reviewed_at on touched
files.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 9: Update RepoMem `version-plan.md` with v0.3 entry

**Files:**
- Modify: `docs/RepoMem/persist/version-plan.md`

- [ ] **Step 1: Rewrite the "当前定位" and v0.3 sections**

Open `docs/RepoMem/persist/version-plan.md`. Replace the "当前定位" block and the v0.3 sections with:

```markdown
## 当前定位

当前仓库是 `HarnessFactory` —— 多工作流契约体系的**工厂仓库**，按用户引导
为每个目标仓库产出一份 `HarnessStack`（分层的 harness 配置）。仓库本身不
是任何具体业务仓库的工作根目录。

当前已确认：

- 仓库名 `HarnessFactory`，产出物名 `a HarnessStack`（每次产出 = 一份 HarnessStack）
- 方法仓库的主要顶层目录采用 `docs/`、`harness-factory/`、`output/`
- 产出物落到 `./output/{YYYY-MM-DD-HHmm}-{scale}-{horizon}/HarnessStack/`
- 目标开发仓库中的 `docs/HarnessStack/` 目录只保存当前激活结果
- contractor 第一阶段采用纯 Markdown；若 agent 读取稳定性不足，再升级为 `Markdown + 极简机器可读清单`

## v0.3 目标

- 完成 `HarnessStack` → `HarnessFactory` 仓库改名
- 完成 `harness-stack/` → `harness-factory/` 工厂源目录改名
- 引入产物结构 `./output/{run}/HarnessStack/`，固化目录与文件契约
- 引入产物顶层 README（AI 蒸馏入口），定义"压缩 Pipeline 不可成为权威"等防漂移约束
- `_kit-reference/` → `_reference/`，配套术语统一
- 清理 v0.2 之前的过期 examples 与 handoff 文档
- 在 RepoMem 中正式引入"调研层 / 推断层"工厂迭代分层概念
- 同步用户 auto-memory

## v0.3 待办

- 在真实目标仓库中跑一次产出流程，验证 `./output/<run>/HarnessStack/` 直接 copy 到 `docs/HarnessStack/` 可用
- 验证压缩 Pipeline 与 `longterm.md § Pipeline` 由同一 recipe source 渲染（不漂移）
- 验证 AI 在读完顶层 README 之后能正确蒸馏出 CLAUDE.md 内容
- 评估"调研层"是否需要专门 skill（v0.4 题）

## 未来考虑

- 调研层的周期性 agent 化（v0.4+）
- 产出物的多人协作版本（多 stack 共存仓库的策略）
- contractor 输出的英文实用文档版
```

Also bump frontmatter `last_reviewed_at: 2026-05-14`.

- [ ] **Step 2: Verify**

```bash
rg -n "HarnessFactory" docs/RepoMem/persist/version-plan.md
rg -n "v0\.3 目标" docs/RepoMem/persist/version-plan.md
```
Expected: matches in both.

- [ ] **Step 3: Commit**

```bash
git add docs/RepoMem/persist/version-plan.md
git commit -m "$(cat <<'EOF'
docs(repo-mem): version-plan v0.3 — HarnessFactory rename & output redesign

Replaces 当前定位 with the HarnessFactory framing and records the v0.3
deliverables (rename, output structure, distillation README, _reference
rename, cleanup, and the調研/推斷 layer concept).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 10: Create the R3 RepoMem entry — factory iteration layers

**Files:**
- Create: `docs/RepoMem/persist/memory/factory-iteration-layers.md`

- [ ] **Step 1: Create the new memory file**

Write `docs/RepoMem/persist/memory/factory-iteration-layers.md`:

```markdown
---
domain: harness-factory-iteration
last_reviewed_at: 2026-05-14
---

# factory-iteration-layers

## Purpose

记录 `HarnessFactory` 内部迭代的两个概念层级，作为 v0.4+ 设计的术语锚点。
当前 SKILL 只实现"推断层"；"调研层"目前为人工维护，未来可考虑自动化。

## Layers

### 调研层 (Research Layer)

- 责任：维护每个 Harness Method（Superpowers / OpenSpec / RepoMem / ECC / BMAD / gstack / ...）
  的层级定义、生命周期覆盖与对比分析。
- 维护方式：当前由人 + agent 手工产出研究文档；未来可考虑由周期性 agent 维护。
- 当前归属此层的文件：
  - [`docs/analysis-lifecycle-workflow-comparison.zh-CN.md`](../../../analysis-lifecycle-workflow-comparison.zh-CN.md)

### 推断层 (Inference Layer)

- 责任：基于用户引导（questionnaire）+ 调研层的方法定义，
  为目标仓库生成一份 `HarnessStack`（落到 `./output/<run>/HarnessStack/`）。
- 当前归属此层的实现：
  - `harness-factory/SKILL.md`（skill 主流程）
  - `harness-factory/references/{selection-criteria,question-flow,questionnaire,output-shapes}.md`
  - `harness-factory/assets/templates/{longterm,temporary,recipes,output-readme-template}.md`

## Constraints

- 推断层只读调研层产物，不直接读 Method 源仓库。调研层是中间表。
- 调研层文档变化触发 recipe 评审，但不自动改 recipe；recipe 改动仍走 v0.3 的
  add-only 与 cross-method invariants 流程。
- 两层之间的契约是"方法的能力与边界"。当一个 Method 的能力扩展时，应先在调研层
  记录证据，再在 recipe 中体现。

## Future

- v0.4 评估：是否把调研层升级为单独 skill（如 `method-survey`），周期触发。
- v0.4+：调研层是否纳入版本治理（versioned method definitions）。

## Related

- 见 [workflow-system 架构](../architecture/workflow-system.md)
- 见 [contractor-output 决策](./contractor-output.md)
- 见 [template-evolution 历史](./template-evolution.md)
```

- [ ] **Step 2: Verify**

```bash
test -f docs/RepoMem/persist/memory/factory-iteration-layers.md && echo "exists"
rg -n "analysis-lifecycle-workflow-comparison" docs/RepoMem/persist/memory/factory-iteration-layers.md
```
Expected: `exists` and a match for the linked Research-Layer artifact.

- [ ] **Step 3: Commit**

```bash
git add docs/RepoMem/persist/memory/factory-iteration-layers.md
git commit -m "$(cat <<'EOF'
docs(repo-mem): add factory-iteration-layers memory (R3)

Codifies the Research Layer / Inference Layer split inside HarnessFactory.
Anchors analysis-lifecycle-workflow-comparison.zh-CN.md as the first
Research-Layer artifact. Notes that the調研層 may become a periodic agent
in v0.4+.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 11: Update dogfood activation file

**Files:**
- Modify: `docs/HarnessStack/longterm.md`

- [ ] **Step 1: Update the Repository field**

Open `docs/HarnessStack/longterm.md`. In the `Document Meta` block:
- `- Repository: HarnessStack` → `- Repository: HarnessFactory`

If a `Last Updated Because` field exists, append a short note:
`; renamed repository identity to HarnessFactory per v0.3 redesign (2026-05-14)`.

Do **not** rename the file path. `docs/HarnessStack/` is the target-side
activation directory and stays.

- [ ] **Step 2: Verify**

```bash
rg -n "^- Repository:" docs/HarnessStack/longterm.md
```
Expected: `- Repository: HarnessFactory`.

- [ ] **Step 3: Commit**

```bash
git add docs/HarnessStack/longterm.md
git commit -m "$(cat <<'EOF'
docs(dogfood): update self-applied contract Repository field

This repository dogfoods HarnessFactory's own output. The factory-side
identity changed; the activation dir docs/HarnessStack/ is unchanged
(it represents the activated stack inside this repo).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 12: Rewrite the top-level repository README

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Replace the README with the new framing**

Open the top-level `README.md` and replace its entire contents with:

```markdown
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
| Factory-side output path | `./output/{YYYY-MM-DD-HHmm}-{scale}-{horizon}/HarnessStack/` |
| Target-side activation path | `<target-repo>/docs/HarnessStack/` |

The inner directory name is `HarnessStack/` on both sides so the bundle can
be copied directly without renaming.

## Top-Level Layout

```
HarnessFactory/
├── README.md                     # this file
├── harness-factory/              # factory source (skill + templates + references)
│   ├── SKILL.md
│   ├── agents/
│   ├── assets/templates/
│   └── references/
├── docs/
│   ├── HarnessStack/             # this repo's own activated stack (dogfood)
│   ├── RepoMem/                  # long-term repository memory for the factory itself
│   ├── CN/                       # Chinese mirror of the factory surface
│   ├── examples/                 # worked examples referenced by recipes
│   ├── superpowers/specs+plans/  # v0.3 design + implementation plan
│   └── analysis-lifecycle-workflow-comparison.zh-CN.md   # Research-Layer artifact
└── output/                       # produced HarnessStack bundles, one per run
```

## What A Produced HarnessStack Contains

```
./output/{run}/HarnessStack/
├── README.md                     # AI distillation index (~60–80 lines)
├── longterm.md                   # authoritative long-term contract
├── temporary-<task>.md           # task-level patch (when applicable)
└── _reference/
    ├── README.md                 # full human-facing usage manual
    └── version-plan-skeleton.md  # multi-version roadmap skeleton
```

The top-level `README.md` inside the bundle is the **one-time AI distillation
source**: the target repo's AI reads it once and condenses sections 1–4 into
its `CLAUDE.md`. The authoritative full contract is `longterm.md`; the
human-facing manual lives in `_reference/`.

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
   `docs/HarnessStack/_reference/README.md`.

## Iteration Layers (R3)

`HarnessFactory` internally distinguishes two iteration layers (see
`docs/RepoMem/persist/memory/factory-iteration-layers.md`):

- **Research Layer (调研层)** — maintains per-method definitions and
  cross-method comparisons. Current artifact:
  `docs/analysis-lifecycle-workflow-comparison.zh-CN.md`.
- **Inference Layer (推断层)** — generates a HarnessStack from user
  guidance. Implemented today by `harness-factory/SKILL.md`.

## Status

- Current version: v0.3 — HarnessFactory rename & output redesign
- Design spec: `docs/superpowers/specs/2026-05-14-harness-factory-rename-and-output-redesign-design.md`
- Implementation plan: `docs/superpowers/plans/2026-05-14-harness-factory-rename-implementation.md`
```

- [ ] **Step 2: Verify**

```bash
rg -n "^# HarnessFactory" README.md
rg -n "harness-stack/" README.md
```
Expected: heading match found; no `harness-stack/` matches.

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "$(cat <<'EOF'
docs: rewrite top-level README for HarnessFactory framing

Repositions this repo as the factory that produces HarnessStack bundles,
documents the two-layer naming, the produced bundle layout, the
factory-side output path, and the Research / Inference iteration layers.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 13: Update user auto-memory

**Files (user's machine-local auto-memory; ABSOLUTE paths):**
- `C:\Users\sheng.zhao\.claude\projects\D--Documents-Codes-Source-Jason-Tool-Dev-HarnessStack\memory\MEMORY.md`
- `C:\Users\sheng.zhao\.claude\projects\D--Documents-Codes-Source-Jason-Tool-Dev-HarnessStack\memory\project_overview.md`
- `C:\Users\sheng.zhao\.claude\projects\D--Documents-Codes-Source-Jason-Tool-Dev-HarnessStack\memory\project_structure.md`
- `C:\Users\sheng.zhao\.claude\projects\D--Documents-Codes-Source-Jason-Tool-Dev-HarnessStack\memory\project_decisions.md`
- `C:\Users\sheng.zhao\.claude\projects\D--Documents-Codes-Source-Jason-Tool-Dev-HarnessStack\memory\project_version_plan.md`
- `C:\Users\sheng.zhao\.claude\projects\D--Documents-Codes-Source-Jason-Tool-Dev-HarnessStack\memory\kit_osr_ecc_invariants.md` (verify only)

- [ ] **Step 1: Read each memory file to confirm current content**

```bash
cat "C:/Users/sheng.zhao/.claude/projects/D--Documents-Codes-Source-Jason-Tool-Dev-HarnessStack/memory/MEMORY.md"
```
And the other four. (These files are NOT inside the git repo; they live in the user's Claude Code project memory.)

- [ ] **Step 2: Rewrite `project_overview.md`**

Update the body to describe the repository as `HarnessFactory` (the factory that produces HarnessStacks). Keep "HarnessStack" mentioned as the **produced artifact name**. Make explicit:

> 当前仓库（`HarnessFactory`）是工厂仓库，每次运行根据用户引导产出一份 `HarnessStack`。
> 产出物落到 `./output/<run>/HarnessStack/`，用户拷贝到目标仓库 `docs/HarnessStack/`。

Update the `description:` frontmatter to match.

- [ ] **Step 3: Rewrite `project_structure.md`**

Update the top-level directory listing:

- `harness-stack/` → `harness-factory/` (description: factory source — skill, templates, references)
- Add: `output/` (description: produced HarnessStack bundles, one per run)
- Keep `docs/HarnessStack/` (description: this repo's own dogfooded activated stack)
- Keep `docs/CN/` (description: Chinese mirror)

Update the `description:` frontmatter to match.

- [ ] **Step 4: Rewrite `project_decisions.md`**

Replace the "仓库名 HarnessStack" decision line with:

> **仓库名 `HarnessFactory`；产出物 `a HarnessStack`**（每次产出 = 一份完整的 HarnessStack；目标仓库激活目录仍叫 `docs/HarnessStack/`）。

Add a new decision line:

> **工厂源目录 `harness-factory/`**（从 v0.3 起；v0.2 之前叫 `harness-stack/`）。

Add a new decision line:

> **产物落点 `./output/{YYYY-MM-DD-HHmm}-{scale}-{horizon}/HarnessStack/`**（v0.3 起；type 留在 questionnaire 中作 recipe 过滤器，不入目录名）。

- [ ] **Step 5: Rewrite `project_version_plan.md`**

Replace the body with:

> 当前位于 **v0.3** 阶段。v0.3 完成 `HarnessFactory` 改名、`harness-factory/` 工厂源目录改名、`./output/<run>/HarnessStack/` 产物结构、顶层 README 蒸馏入口、`_reference/` 改名、过期文档清理与 RepoMem 同步。设计 spec：`docs/superpowers/specs/2026-05-14-harness-factory-rename-and-output-redesign-design.md`。

- [ ] **Step 6: Verify `kit_osr_ecc_invariants.md` references**

Read the file. If any path references `harness-stack/`, rewrite to `harness-factory/`. The OSR+ECC kit invariant rule itself is content-stable; only paths may need updating.

- [ ] **Step 7: Update `MEMORY.md` (the index)**

Open `MEMORY.md`. Update each one-line hook to reflect:

- `project_overview.md` — `HarnessFactory 是工厂仓库，产出 HarnessStack`
- `project_structure.md` — `顶层目录：docs/、harness-factory/、output/；docs/CN/ 中文镜像`
- `project_decisions.md` — `仓库名 HarnessFactory；产物 HarnessStack；五层基线；纯 Markdown`
- `project_version_plan.md` — `当前位于 v0.3 阶段：HarnessFactory 改名与产出结构定型`
- `kit_osr_ecc_invariants.md` — keep (verify path refs match harness-factory/ if needed)

Add a new index entry:

- `factory_iteration_layers.md` — pointer to the in-repo memory at `docs/RepoMem/persist/memory/factory-iteration-layers.md`

- [ ] **Step 8: Verify**

```bash
rg -n "HarnessFactory" "C:/Users/sheng.zhao/.claude/projects/D--Documents-Codes-Source-Jason-Tool-Dev-HarnessStack/memory/"
rg -n "harness-stack" "C:/Users/sheng.zhao/.claude/projects/D--Documents-Codes-Source-Jason-Tool-Dev-HarnessStack/memory/"
```
Expected: multiple `HarnessFactory` matches; no `harness-stack` matches (path form).

- [ ] **Step 9: No commit**

Auto-memory is outside the git repo; do not attempt to commit it. Confirm by:
```bash
cd D:/Documents/Codes/Source_Jason/Tool_Dev/HarnessStack
git status
```
Expected: clean working tree.

---

## Task 14: Final verification against acceptance criteria

**Files:** none modified. This task only verifies.

- [ ] **Step 1: Acceptance § 10.1 — Top-level README**

```bash
rg -n "^# HarnessFactory" README.md
rg -n "Factory.{0,5}Stack" README.md
```
Expected: heading match; at least one mention of the Factory→Stack relationship.

- [ ] **Step 2: Acceptance § 10.2 — Factory source dir**

```bash
test -d harness-factory && echo "harness-factory exists"
test ! -d harness-stack && echo "harness-stack gone"
ls harness-factory/
```
Expected: both echoes print; directory contains SKILL.md, agents/, assets/, references/.

- [ ] **Step 3: Acceptance § 10.3 — CN mirror sync**

```bash
rg -n "harness-stack" docs/CN/
```
Expected: no matches.

- [ ] **Step 4: Acceptance § 10.4 — Output structure described**

```bash
rg -n "\./output/\{YYYY-MM-DD-HHmm\}-\{scale\}-\{horizon\}/HarnessStack/" harness-factory/references/output-shapes.md docs/CN/references/output-shapes.md
```
Expected: match in both files.

- [ ] **Step 5: Acceptance § 10.5 — Compressed Pipeline label**

```bash
rg -n "Per-Task Pipeline \(Compressed\)" harness-factory/assets/templates/output-readme-template.md
rg -n "not authoritative|longterm\.md § Pipeline" harness-factory/assets/templates/output-readme-template.md
```
Expected: both matches found.

- [ ] **Step 6: Acceptance § 10.6 — RepoMem updated + R3 entry**

```bash
test -f docs/RepoMem/persist/memory/factory-iteration-layers.md && echo "R3 exists"
rg -n "HarnessFactory" docs/RepoMem/persist/ | head
rg -n "HarnessStack 仓库|harness-stack/" docs/RepoMem/persist/
```
Expected: `R3 exists`; multiple HarnessFactory matches; **no** matches for the third query.

- [ ] **Step 7: Acceptance § 10.7 — Cleanup committed**

```bash
test ! -f docs/handoff/3method-iteration-2026-05-07.md && echo "handoff gone"
test ! -d docs/examples/openspec-superpowers-repomem-ecc-activation-kit && echo "ecc kit gone"
test ! -f docs/examples/openspec-superpowers-repomem-longterm.md && echo "longterm sample gone"
test ! -f docs/examples/openspec-superpowers-repomem-longterm_v1.md && echo "v1 gone"
ls docs/examples/
```
Expected: four `gone` echoes; remaining files in `docs/examples/` are exactly `openspec-superpowers-repomem-longterm_orient.md` and `superpowers-only-longterm.md`.

- [ ] **Step 8: Acceptance § 10.8 — Auto-memory updated**

```bash
rg -n "HarnessFactory" "C:/Users/sheng.zhao/.claude/projects/D--Documents-Codes-Source-Jason-Tool-Dev-HarnessStack/memory/" | head
```
Expected: matches across MEMORY.md, project_overview.md, project_structure.md, project_decisions.md, project_version_plan.md.

- [ ] **Step 9: Acceptance § 10.9 — Dogfood Repository field**

```bash
rg -n "^- Repository: HarnessFactory" docs/HarnessStack/longterm.md
```
Expected: one match.

- [ ] **Step 10: Final-state grep sweep**

```bash
rg -n "harness-stack" .
```
Expected: matches **only** in (a) `docs/superpowers/specs/` (the design doc retains historical context), (b) git history (not file contents), (c) any deliberately preserved historical example. Specifically, **no** matches in `harness-factory/`, `docs/CN/`, `docs/RepoMem/persist/`, or top-level `README.md`.

- [ ] **Step 11: Final git log inspection**

```bash
git log --oneline -15
```
Expected: ~13 new commits with clear progression from cleanup → rename → content rewrites → output structure → README template → RepoMem updates → dogfood → top-level README → (auto-memory was uncommitted).

- [ ] **Step 12: Report completion**

Summarize to the user:
- Commit count.
- Acceptance items satisfied.
- Auto-memory state (updated, not committed — confirm with user whether to leave as-is).
