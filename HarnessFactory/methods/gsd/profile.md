# Profile — gsd

## Identity

- Upstream name: GSD
- Layer: Primary Workflow
- Status: research-only
- Source location: upstream GSD repository (not yet adopted by any recipe in this factory)

## Lifecycle Coverage

| 目标定義 | 需求澄清 | 方案設計 | 任務規劃 | 實現開發 | 測試驗證 | 發布交付 | 運行反饋與迭代沉澱 |
|---|---|---|---|---|---|---|---|
| 主覆蓋 | 主覆蓋 | 輔助覆蓋 | 主覆蓋 | 主覆蓋 | 輔助覆蓋 | 輔助覆蓋 | 主覆蓋 |

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
