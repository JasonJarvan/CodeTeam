<div align="center">

# RepoMem

### 让仓库真正拥有记忆。

**一个面向代码仓库与 AI Coding Agent 的持久化记忆层。**

**支持与 GSD、ECC、OpenSpec、Superpowers、BMAD、gstack 等工作流兼容。**

[English](./README.md) / [中文](./README_CN.md)

![AI Agents](https://img.shields.io/badge/AI%20Agents-Repo%20Memory%20Layer-111111?style=flat-square)
![HITL](https://img.shields.io/badge/HITL-Review%20Before%20Long--term%20Writes-0A7B83?style=flat-square)
![Memory Model](https://img.shields.io/badge/Temp-%3E%20Merge%20%3E%20Persist-8A5CF6?style=flat-square)
![Repo-native](https://img.shields.io/badge/Repo--native-Durable%20Memory-2D6A4F?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-black?style=flat-square)
![Stars](https://img.shields.io/github/stars/JasonJarvan/RepoMem?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/JasonJarvan/RepoMem?style=flat-square)

![RepoMem Social Preview](./assets/repomem_social_preview.png)

</div>

RepoMem 为仓库提供一个可审阅、可持续、可沉淀的地方，用来存放：

- 架构知识
- 长期工程记忆
- 版本规划
- 任务范围内的工作记忆

很多关键信息现在只活在聊天记录、agent 会话或零散文档里。RepoMem 的目标，是把这些知识重新放回**仓库内部**，并且在长期知识写入前保留 **HITL 审阅**。

RepoMem **不是**完整的交付工作流编排器。
它更像是一个可独立使用、也可嵌入其他工作流的记忆层。

## 与其他工作流兼容

原生支持与 GSD、ECC、OpenSpec、Superpowers、BMAD、gstack 等工作流兼容。

推荐通过 [HarnessStack](https://github.com/JasonJarvan/HarnessStack) 获得最佳兼容开发体验。

## 为什么是 RepoMem

AI 写代码越来越快，但仓库知识衰减得也越来越快。

常见问题包括：

- agent 解决了任务，却没有留下架构层面的原因
- 调试中积累的经验被困在聊天上下文里
- 仓库里有文档，但没有区分“临时笔记”和“长期事实”
- 所谓 memory 会越来越脏，因为没人知道什么该沉淀、什么该审核

RepoMem 解决的是这个问题：

- `persist/architecture/` 保存仓库如何组织
- `persist/memory/` 保存长期约束、陷阱与决策依据
- `persist/version-plan.md` 保存未来版本规划
- `temp/<slug>/` 保存任务范围内的工作记忆
- `merge` 把任务记忆转成经过审阅的长期知识

最终效果很直接：

**你的仓库不再依赖脆弱的对话式记忆。**

## 它和普通文档系统有什么不同

多数仓库文档系统解决的是“文档写在哪里”。

RepoMem 解决的是更难的问题：

**哪些内容应该只是临时的，哪些应该成为长期记忆，以及这个提升过程怎样才安全。**

它的核心设计原则是：

- **Repo-native**：知识存在仓库里，而不是藏在外部黑盒记忆服务里
- **Agent-friendly**：针对 AI 辅助开发、任务恢复和上下文续接设计
- **HITL-first**：长期写入前必须经过人工审阅
- **记忆类型分层**：架构、记忆、版本计划、任务笔记不混在一起
- **Workflow-agnostic**：可独立使用，也可作为更大工作流的底层记忆层

## 它怎么工作

### 1. 初始化仓库记忆

使用 `repo-mem init` 初始化标准记忆结构。

对于新仓库，RepoMem 会直接创建持久化骨架。

对于已有仓库，RepoMem 使用“提案优先”的流程：

1. 分析仓库
2. 生成 `temp/<slug>/init-proposal.md`
3. 用户审阅并编辑提案
4. 应用已确认提案
5. 如果出现冲突，生成 `temp/<slug>/init-conflicts.md`
6. 通过 `conflict_id` 逐条解决
7. 审阅生成的 `git diff`

### 2. 在任务开始时恢复上下文

使用 `repo-mem read <slug>` 来开始任务或恢复任务。

RepoMem 会读取：

- 持久化文档
- 相关领域文档
- 同一任务 slug 下已有的临时文档

随后输出针对当前任务的上下文摘要。

### 3. 在执行过程中捕获任务记忆

使用 `repo-mem capture <slug>` 持续记录任务过程中的工作记忆。

RepoMem 会更新这些任务文档：

- `requirements.md`
- `architecture.md`
- `memory.md`

`capture` 只写入 `temp/`。
它**不会**直接写入长期事实层。

### 4. 用审阅机制沉淀长期知识

仅在任务闭环后使用 `repo-mem merge <slug>`。

RepoMem 会：

1. 生成结构化 merge 建议
2. 等待 HITL 确认
3. 写入确认后的长期更新
4. 更新 temp 状态
5. 展示写入后的 `git diff`

当前 merge 分类包括：

- `to architecture`
- `to memory`
- `do not merge`

### 5. 维护长期记忆，而不是粗暴清理

使用：

- `repo-mem prune [domain]`
- `repo-mem split [domain]`

它们是维护动作，不是盲目的破坏性命令。
RepoMem 会先生成 proposal，再由人决定如何应用。

## 标准仓库结构

```text
docs/RepoMem/
├── persist/
│   ├── config.md
│   ├── version-plan.md
│   ├── architecture/
│   │   ├── index.md
│   │   └── <domain>.md
│   └── memory/
│       ├── index.md
│       └── <domain>.md
├── temp/
│   ├── <slug>/
│   │   ├── requirements.md
│   │   ├── architecture.md
│   │   ├── memory.md
│   │   ├── init-proposal.md
│   │   └── init-conflicts.md
│   └── <maintenance-slug>/
│       └── proposal.md
└── multi-lang/
    └── <language>/
```

`init-proposal.md` 和 `init-conflicts.md` 只用于“已有仓库初始化”。
它们不是常规任务记忆三件套的一部分。

## RepoMem 的记忆模型

### 持久化文档

用于承载长期仓库知识：

- `persist/architecture/`
  结构、边界、领域映射、跨领域关系
- `persist/memory/`
  约束、陷阱、决策依据、长期隐性知识
- `persist/version-plan.md`
  仅用于未来版本规划

### 临时文档

用于承载任务范围内的工作记忆：

- `requirements.md`
- `architecture.md`
- `memory.md`

这层分离就是 RepoMem 的核心。
临时工作先保持临时，只有在人工审阅后，真正值得保留的部分才进入长期层。

## 语言策略

RepoMem 使用**一种主语言**作为仓库记忆的事实语言。

该语言用于：

- 持久化文档
- 临时文档
- merge 建议
- 维护提案
- HITL 审阅项

其他语言只作为镜像。
将其放在 `multi-lang/<language>/` 下。
不要把它当作主事实来源。

## RepoMem 适合放在哪一层

RepoMem 最适合作为其他工作流周围的一层“仓库记忆层”。

典型接入点：

- 规划前：`repo-mem read <slug>`
- 执行中：`repo-mem capture <slug>`
- 任务闭环时：`repo-mem merge <slug>`
- 长期维护时：`repo-mem prune` / `repo-mem split`

它非常适合 agent-heavy 的开发流程，因为它提供了一个可审计、可恢复、可沉淀的记忆系统，而不是继续依赖聊天上下文。

## RepoMem 不是什么

RepoMem 不是：

- 向量数据库
- 聊天记忆产品
- 什么都往里放的通用知识库
- 交付工作流的替代品
- 全自动的长期知识写入系统

它是一个面向 AI 辅助软件开发的**仓库原生记忆纪律**。

## 当前状态

RepoMem 当前支持：

- 可复用 skill 打包
- 基于模板的仓库初始化
- 位于 `docs/RepoMem/` 下的自托管运行态文档
- 任务临时文档
- HITL merge 流程
- 提案优先的已有仓库初始化
- 基于决策的冲突生成与冲突解决

持续工作记录见：

- [docs/RepoMem/persist/version-plan.md](/home/shenzhou/Codes/CodingAgentHarnessSystem/RepoMem/docs/RepoMem/persist/version-plan.md)

## 本仓库结构

这个仓库内部有三个清晰区域：

```text
repo-mem/
  可复用 skill 包

repo-mem/assets/templates/
  用于初始化其他仓库的模板

docs/RepoMem/
  RepoMem 对 RepoMem 自身的管理数据
```

## 许可证

RepoMem 使用 **MIT License**。

这意味着你可以使用、修改和商业化它，但需要保留版权声明与许可证文本。

见：

- [LICENSE](/home/shenzhou/Codes/CodingAgentHarnessSystem/RepoMem/LICENSE)

## 一句话介绍

如果 AI Agent 正在成为你仓库里的新贡献者，RepoMem 提供的是它们最缺的一层能力：

**带结构、带审阅、带提升规则的持久化仓库记忆。**
