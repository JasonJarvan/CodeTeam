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
  - [`methods/_comparison/lifecycle-workflow-comparison.zh-CN.md`](../../../../methods/_comparison/lifecycle-workflow-comparison.zh-CN.md)

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
