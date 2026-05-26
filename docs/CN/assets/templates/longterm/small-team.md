# longterm-small-team.md 模板

## 文档元信息

- 仓库：
- 生效自：
- 来源模板：
  - `harness-stack/assets/templates/longterm/small-team.md`
- 上次更新原因：

## 当前长效评估

- 协作规模：
  - `small-team`
- 仓库类型：
  - `product | research | platform | other`
- 项目周期：
  - `short-lived | long-lived`
- 长效知识治理：
  - `enabled`

## 当前生效的长效基线

### 1. 主工作流层

- 默认启用：
  - 默认无
- 默认禁用：
  - `BMAD`
- 升级触发条件：
  - 路线图规划超出轻量协调
  - 跨任务协调成本持续偏高

### 2. 规格层

- 默认启用：
  - `OpenSpec`
- 默认禁用：
  - 默认无
- 升级触发条件：
  - 一旦出现协作漂移则加强使用

### 3. 执行纪律层

- 默认启用：
  - `Superpowers`
- 默认禁用：
  - 默认无
- 升级触发条件：
  - 对高风险工作加强评审、验证与计划纪律

### 4. 仓库记忆层

- 默认启用：
  - `RepoMem`
- 默认禁用：
  - 默认无
- 升级触发条件：
  - 领域增长时更激进地拆分架构与记忆

### 5. Harness 增强层

- 默认启用：
  - `ECC(medium)`
- 默认禁用：
  - 默认无
- 升级触发条件：
  - 当共享上下文、安全与可重复性成为痛点时加强护栏

## 临时契约边界规则

### 临时契约可以调整

- 按清晰度与交付目标选择更轻或更重的任务级流程
- 对很小且低风险的任务降低 `OpenSpec` 强度
- 对高风险工作提高 `Superpowers` 与 `ECC` 强度

### 临时契约不得覆盖

- `OpenSpec`、`RepoMem` 或 `Superpowers` 作为团队基线的存在性
- 长效协作与治理规则
- 未经完整重写，不得覆盖本文档的协作规模假设

## 完整重写条件

- 团队收缩为单人或扩张为大团队条件
- 仓库进入重得多的协调模式
- 默认基线需要永久更重的主工作流

## 相关文档

- `docs/HarnessStack/temporary-<task>.md`
- `docs/RepoMem/persist/version-plan.md`
