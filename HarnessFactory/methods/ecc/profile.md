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
