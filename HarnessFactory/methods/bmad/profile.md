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
