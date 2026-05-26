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

- 责任：维护每个 Harness Method（Superpowers / OpenSpec / RepoMem / ECC / BMAD / gstack / GSD / sendbox / dashboard / ...）
  的 profile（身份/生命周期覆盖/能力/冲突依赖/embedding）与跨方法对比。
- 维护方式：人 + agent 手工产出 profile；跨方法分析 (`_comparison/`) 同样手工维护；未来可考虑周期性 agent 维护。
- 物理目录（v0.4 落地于 2026-05-26）：`methods/`
  - `methods/README.md` — 候选层契约 + profile schema + 添加新候选的判据
  - `methods/<method>/profile.md` — per-method profile（schema 固定）
  - `methods/<method>/embedding-playbook.md` — embedding 机制非平凡的方法的落地手册
  - `methods/_comparison/lifecycle-workflow-comparison.zh-CN.md` — 跨方法生命周期对比（从 docs/ 搬过来）

### 推断层 (Inference Layer)

- 责任：基于用户引导（questionnaire）+ 调研层的方法定义，
  为目标仓库生成一份 `HarnessStack`（落到 `./output/<run>/HarnessStack/`）。
- 当前归属此层的实现：
  - `harness-factory/SKILL.md`（skill 主流程）
  - `harness-factory/references/{selection-criteria,question-flow,questionnaire,output-shapes}.md`
  - `harness-factory/assets/templates/{longterm,temporary,recipes,output-readme-template}.md`

## Constraints

- 推断层只读候选层产物，不直接读 Method 源仓库。候选层（`methods/`）是中间表。
  契约见 `../../../../methods/README.md § Read-only contract with the assembly layer`。
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
