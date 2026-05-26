---
name: harness-stack
description: 使用 HarnessStack 模型为仓库选择并生成长效与临时工作流契约文档。在 Codex 需要决定为项目或任务激活哪些工作流层级、创建 `docs/HarnessStack/longterm.md`、创建 `docs/HarnessStack/temporary-<task>.md`，或将任务工作流与仓库长效基线对齐时使用。
---

# Harness Stack

## 概述

使用本技能为仓库选择并生成工作流契约文档。
输出为仓库的**长效**基线，以及在需要时**不覆盖基线**、仅对其进行补丁式补充的**任务级临时**契约。

## 核心规则

- 将 `docs/HarnessStack/longterm.md` 视为仓库完整的长效生效契约。
- 将 `docs/HarnessStack/temporary-<task>.md` 视为当前任务完整临时生效契约。
- 不得让临时契约在无声中改写长效治理。
- 不得将整个方法库复制到目标仓库。
- 在目标仓库中，`docs/HarnessStack/` 只应包含**生效结果**文档。

## 工作流

1. 阅读仓库上下文；若有 RepoMem 事实则一并参考。
2. 判断仓库是需要更新长效基线，还是仅需临时任务契约。
3. 在选择工作流层级、阈值或重写条件之前，阅读 [references/selection-criteria.md](./references/selection-criteria.md)。
4. 在提问或决定是否同时产出长效与临时文档之前，阅读 [references/question-flow.md](./references/question-flow.md)。
5. 阅读 [references/questionnaire.md](./references/questionnaire.md)，以最少化并规范化实际提出的问题。
6. 在生成最终文档之前，阅读 [references/output-shapes.md](./references/output-shapes.md)。
7. 若生成长效契约，填写 `assets/templates/longterm-template.md` 模板。
8. 若生成临时契约，填写 `assets/templates/temporary-template.md` 模板。
9. 区分长效与临时职责：
   - 长效：稳定基线、边界、重写条件
   - 临时：任务评估、任务级调整、最终生效栈
10. 写出完整生效文档，而非模板占位符或残缺笔记。

## 输出规则

- 优先使用纯 Markdown 契约文档。
- 若仓库已有长效契约，仅在长效条件发生实质变化时更新。
- 否则保持长效契约稳定，仅生成临时契约。
- 当契约设计决策影响长效治理时，将决策记入 RepoMem 记忆。

## 资源

### assets/templates/

- `longterm-template.md`：仓库级长效生效契约模板
- `temporary-template.md`：任务级临时生效契约模板

### references/

- `selection-criteria.md`：长效与临时决策因素、阈值与层级默认
- `question-flow.md`：生成生效契约前的精简问题流与输出规则
- `questionnaire.md`：最少问题列表与规范化规则
- `output-shapes.md`：所需输出模式与完整性规则

将上述模板与参考作为生成契约文档的起点，填入仓库特定结果，而非复制方法库元数据。
