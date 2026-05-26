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
