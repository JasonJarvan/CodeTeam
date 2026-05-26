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
