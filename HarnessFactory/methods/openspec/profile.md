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
