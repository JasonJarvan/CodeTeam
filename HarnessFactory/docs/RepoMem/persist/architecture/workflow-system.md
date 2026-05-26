---
domain: workflow-system
last_reviewed_at: 2026-05-14
---

# workflow-system

## Purpose

记录 `CodingAgentHarnessSystem` 如何从多个工作流体系中抽取并组合出更精准的 contractor。

## Responsibilities

- 对比不同工作流的生命周期覆盖
- 判断哪些体系是主 workflow，哪些是规格层、执行层、记忆层、harness 层
- 为不同项目场景生成最小数量、最合适的 workflow contractor
- 为 `harness-factory/` 目录定义长期 contractor、临时 contractor 与 skill 内容的结构边界
- 为目标开发仓库中的 `HarnessStack/` 目录定义激活结果文档边界

## Key Structures Or Flows

- 先研究 `BMAD`、`gstack`、`GSD`、`OpenSpec`、`Superpowers`、`everythingclaudecode`
- 再把 `RepoMem` 加入为仓库记忆体层
- 最终基于场景与复杂度组合出 contractor
- 方法仓库中的 contractor 模板与 skill 内容放在 `harness-factory/`
- 目标开发仓库中的 `HarnessStack/` 只保存当前激活结果
- RepoMem 长期层负责保存 contractor 设计决策、版本计划和 GitHub 仓库定位

## Boundaries And Dependencies

- 该 domain 依赖对各工作流体系的分析文档
- 该 domain 不直接负责实现具体 skill，而是定义组合策略
- 当前 `CodingAgentHarnessSystem` 只是 contractor 体系的聚合仓库，不是目标开发仓库工作目录

## Related Memory

- 见 [workflow-system](../memory/workflow-system.md)
