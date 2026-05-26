# longterm-large-team.md 模板

## 文档元信息

- 仓库：
- 生效自：
- 来源模板：
  - `harness-stack/assets/templates/longterm/large-team.md`
- 上次更新原因：

## 当前长效评估

- 协作规模：
  - `large-team`
- 仓库类型：
  - `product | research | platform | other`
- 项目周期：
  - `short-lived | long-lived`
- 长效知识治理：
  - `enabled`

## 当前生效的长效基线

### 1. 主工作流层

- 默认启用：
  - `GSD` 或 `BMAD`
- 默认禁用：
  - 默认无
- 升级触发条件：
  - 协调开销需要更强的路线图与规划结构

### 2. 规格层

- 默认启用：
  - `OpenSpec`
- 默认禁用：
  - 默认无
- 升级触发条件：
  - 多个并发变更相互影响时需要更严的执行

### 3. 执行纪律层

- 默认启用：
  - `Superpowers`
- 默认禁用：
  - 默认无
- 升级触发条件：
  - 在贡献者间加强计划执行、评审与验证

### 4. 仓库记忆层

- 默认启用：
  - `RepoMem`
- 默认禁用：
  - 默认无
- 升级触发条件：
  - 随着仓库领域增多，扩展架构与记忆分解

### 5. Harness 增强层

- 默认启用：
  - `ECC(strong)`
- 默认禁用：
  - 默认无
- 升级触发条件：
  - 高风险交付时提高安全、评测与编排严谨度

## 临时契约边界规则

### 临时契约可以调整

- 在已激活栈内提高或降低任务级强度
- 按清晰度与交付目标选择不同临时流程
- 为当前任务收窄或放宽验证强度

### 临时契约不得覆盖

- `OpenSpec`、`RepoMem`、`Superpowers` 或 `ECC` 作为基线的存在性
- 长效治理、审计与安全期望
- 未经完整重写，不得覆盖本文档的协作规模假设

## 完整重写条件

- 协作规模实质下降
- 主工作流需要在更重规划体系间永久切换
- 全仓库治理强度发生实质变化

## 相关文档

- `docs/HarnessStack/temporary-<task>.md`
- `docs/RepoMem/persist/version-plan.md`
