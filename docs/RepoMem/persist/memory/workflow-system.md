---
domain: workflow-system
last_reviewed_at: 2026-05-14
---

# workflow-system 记忆

## Constraints

- CAHS 的目标不是复刻某一个单独工作流，而是形成可组合的 contractor 体系。
- contractor 的设计必须以生命周期覆盖与项目情境为前提，而不是按工具名堆叠。
- 当前仓库只是聚合与设计仓库，不是最终承载 contractor 激活结果的真实开发仓库。
- 一个真实开发仓库同一时刻只应激活一个长期 contractor。
- 方法仓库中的模板源与目标开发仓库中的激活结果必须使用不同语义，不可混放。

## Pitfalls

- 直接把所有工作流并列看待，会丢失层次关系，导致组合设计失真。
- 没有先做生命周期映射，就很难判断重合和边界。
- 把长期 contractor 与临时 contractor 混写在一份大文档中，会迅速失去上下文优势。
- 如果把模板源与激活结果都放进目标开发仓库的同一 `HarnessStack/` 目录，会破坏“最小上下文”目标。

## Decision Rationale

- 先做软件工程生命周期覆盖对比，再判断哪些体系属于主 workflow、规格层、执行纪律层、仓库记忆体层和 harness 增强层。
- 将 `RepoMem` 加入比较，是为了补齐现有体系普遍缺失的仓库级长期记忆层。
- 长期 contractor 负责仓库默认基线，临时 contractor 负责任务级 patch。
- contractor 第一阶段只采用纯 Markdown；如果效果不好，再升级到 Markdown 加极简机器可读清单。
- 多工作流契约体系的 GitHub 仓库名确定为 `HarnessFactory`；每次产出物称为 `a HarnessStack`。
- 方法仓库的主要顶层目录采用 `docs/` 和 `harness-factory/`。
- 目标开发仓库中的 `HarnessStack/` 目录只保存当前激活结果，而不是备选模板库。

## Related Architecture

- 见 [workflow-system](../architecture/workflow-system.md)
