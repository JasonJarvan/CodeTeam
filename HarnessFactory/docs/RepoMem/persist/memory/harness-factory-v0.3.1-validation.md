---
domain: harness-factory-v0.3.1-validation
last_reviewed_at: 2026-05-15
---

# harness-factory-v0.3.1-validation

## Purpose

记录 v0.3.1 dogfood 验证的实测结果，作为后续工厂改动（v0.4 起）的回归基准。
本次验证目标见 `version-plan.md § v0.3.1 待办`：bundle 结构、压缩 Pipeline
不漂移、AI 蒸馏可行性，以及 `{stack}` 路径段。

## What Was Validated

### 1. Bundle Structure（通过）

`docs/HarnessStack/` dogfood 实例当前包含：

```
docs/HarnessStack/
├── README.md                # AI distillation (~80 行)
├── longterm.md              # 权威契约
└── _toUser/
    └── README.md            # 人读手册
```

不含 `temporary-<task>.md`（dogfood 不是一次"任务"运行，是契约刷新），不含
`version-plan-skeleton.md`（按 v0.3.1 ε 决策移出 bundle）。与
`harness-factory/references/output-shapes.md § Output Destination`
描述一致。

### 2. Pipeline Non-Drift（通过）

`README.md § 3 Per-Task Pipeline (Compressed)` 与 `longterm.md § Pipeline`
**步骤命名、顺序、约束完全一致**（步骤 1-10）。压缩视图省略 `RepoMem.prune /
split`（步骤 11），因为该步骤是"periodic hygiene, not per-task"，不属于
单任务循环——这是预期的压缩，不是漂移。

`README.md § 3` 的 `(Compressed)` + `It is not authoritative` 声明保留，权威性
正确归位 `longterm.md`。

### 3. AI Distillation（通过）

模拟"目标仓库 AI 第一次读 README.md"场景，按 §6 For AI Consumers 指令将
§1-4 蒸馏为以下 ~25 行 CLAUDE.md 草稿（**作为后续回归基准**）：

```markdown
## Workflow Contract

This repository runs HarnessStack at `solo` / `long-lived` with recipe
`superpowers-repomem`. Active methods: Superpowers + RepoMem.

### Per-Task Flow (10 steps)

1. `RepoMem.read` → 2. `Superpowers.brainstorming` → 3. `RepoMem.capture`
→ 4. `Superpowers.writing-plans` → 5. `using-git-worktrees` +
`executing-plans` + TDD → 6. `RepoMem.capture` (continuous) →
7. `verification-before-completion` → 8. `requesting-code-review` →
9. `finishing-a-development-branch` → 10. `RepoMem.merge` (HITL)

### Invariants

- Add-only: methods never deactivate; upgrades extend, not replace.
- Verification gate: `verification-before-completion` MUST pass before
  `requesting-code-review`.
- Merge order: `RepoMem.merge` runs AFTER
  `finishing-a-development-branch`.
- Doc sedimentation: temporary memory authoritative during task;
  long-term only via HITL merge. Plan = HOW; memory = WHY. No duplication.

For full details, see `docs/HarnessStack/longterm.md`.
```

#### Distillation 之后仍需回查 longterm.md 的场景

- 处理任务级冲突时查 `Cross-Layer Conflicts` 表
- 判断本 stack 是否适合一类新任务时查 `Suitability Envelope`
- 决定是否开 `temporary-<task>.md` 时查 `Temporary Contractor Boundary Rules`
- 决定是否触发 full rewrite 时查 `Full Rewrite Conditions`
- 决定某一步是 `auto` / `ask-first` / `HITL` 时查 recipe 的 `Execution Policy`（dogfood longterm 未内联此表，由 recipe 提供）

结论：CLAUDE.md 草稿足够覆盖**日常路径**；非常规情况按上述映射回查
`longterm.md`。这正是 §6 "Re-read this README only on recipe upgrade"
的预期——常规态 CLAUDE.md 足矣。

### 4. `_toUser/README.md`（通过）

手册作为独立人读文档完整：Day-One Init / Per-Task Loop / Long-Term
Iteration / Tracking HarnessStack Evolution / Common Questions 五段全
落实。RepoMem skill 建议正确嵌入 § 5。

## What Was NOT Validated

### 5. `{stack}` 路径段（未验证）

dogfood 直接写入 `docs/HarnessStack/`，不走 `output/{time}-{stack}/` 路径。
路径段仅在 `harness-factory/references/output-shapes.md` 描述层验证——
**需要一次真实 output 运行**才能确认 `{stack}` 渲染（包括 `eccMedium` /
`eccLight` 等强度后缀）正确无误。

> 注：仓库 working tree 里存在 `output/2026-05-15-1711-superpowers-repomem/`，
> 是平行会话产物，未由本次验证生成。基础形态匹配（recipe slug 作 segment），
> 但未覆盖强度后缀场景。

### 6. "无边界" 语义（未澄清）

用户在 dogfood 启动时说"要求只有 superpowers+repomem，无边界"，三种可能解读
（无 Cross-Layer Conflicts / 无 Temporary Boundary Rules / 无 Suitability
Envelope）未明确。验证按"不动 recipe-mandated 内容"保守解读处理。**后续若
用户明确语义，可能需要回头调整 dogfood 或 recipe**。

## Issues Surfaced

1. **`type` 枚举不含 `skill`**：dogfood 类型实际是"HarnessFactory skill /
   methodology repository"，最接近的 `platform` 是 superset 而非精确。已在
   `longterm.md § Current Long-Term Assessment` 内联说明，v0.4 候选是加
   `skill` / `method` 枚举值（见 `version-plan.md § v0.3.1 待办`）。

2. **模板渲染仍是手工**：`output-readme-template.md` 与
   `to-user-readme-template.md` 都用 `{placeholder}` 语法，但没有渲染脚本，
   人/agent 按 SKILL.md Step 10/11 手填。v0.4+ 可考虑半自动化（如
   `harness-factory/SKILL.md` 加渲染辅助 sub-skill）。

3. **`output/` 与 dogfood 双轨**：本次确认了 `docs/HarnessStack/`（dogfood）
   与 `output/<run>/HarnessStack/`（factory product）是**两套独立产物**——
   dogfood 不走 output 路径，factory product 也不写入 docs。`SKILL.md §
   Output Rules` 新增一句"长期契约 landing 路径"明确了这点。

## Validation Outputs（本次生成的产物）

- 改动：`docs/HarnessStack/longterm.md`（type research → platform；
  `Last Updated Because` 增 v0.3.1 dogfood regeneration 一项；Related
  Documents 增 README + _toUser pointers）
- 新增：`docs/HarnessStack/README.md`（AI distillation 入口）
- 新增：`docs/HarnessStack/_toUser/README.md`（人读手册）

## Next Validation Cycle Triggers

下次 dogfood 应重新跑的触发条件：

- recipe `superpowers-repomem.md` 的 Pipeline / Cross-Layer Conflicts /
  Merge Gates / Execution Policy 任一变化（README §3 与 longterm §Pipeline
  需重渲染并复查不漂移）
- `to-user-readme-template.md` 或 `output-readme-template.md` 任一改动
- bundle 结构（`output-shapes.md § Output Destination`）变化
- v0.4 落地 `openspec-superpowers-repomem` 的 Task-Level Document
  Partition + Task-End Disposition 章节后（不直接影响本 dogfood，但需
  重新核对 add-only 路径）
