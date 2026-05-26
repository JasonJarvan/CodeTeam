# RepoMem 版本计划

## Current Version

- 当前目标版本：`v2.1`
- 当前状态：规划中
- 当前重点：提升已有仓库分析质量、proposal 质量和长期维护体验

## Planned Versions

### v1.0

目标：

- 交付第一个可用的 `repo-mem` skill，并通过自举使用验证其基础能力

状态：

- 已通过自举演练验收

范围：

- 创建可发布的 `repo-mem` skill 包
- 提供 `SKILL.md`、`references/`、`scripts/`、`assets/templates/`
- 支持 `init`、`read`、`capture`、`merge`、`prune`、`split`
- 建立 `docs/RepoMem/` 作为 RepoMem 自举长期事实与临时文档库
- 建立主语言、长期层、临时层、多语言镜像层的基本规则
- 完成 `merge`、`prune`、`split` 的 HITL 基线
- 用 RepoMem 管理 RepoMem 自己的开发过程，作为 `v1.0` 的真实演练
- 已完成一次 `init -> proposal -> apply -> conflicts` 的自举演练闭环，证明 v1 基础结构可用

非范围：

- 既有仓库的自动分析式初始化
- runtime 经验自动提升为 skill 通用规则
- 全自动 `prune` 和 `split`

### v2.0

目标：

- 支持对已有仓库进行提案式初始化

状态：

- 已收敛并完成核心闭环

候选范围：

- 分析现有仓库，生成 `temp/<slug>/init-proposal.md`
- 识别已有文档和候选 domain
- 用户可直接修改并确认 `init-proposal.md`
- 基于 proposal 执行初始化 apply
- 创建不存在的长期文档
- 对已有长期文档只补全缺失内容
- 若发生冲突，生成 `temp/<slug>/init-conflicts.md`
- 以 `conflict_id` 为单位逐条处理冲突
- 当前已支持 `keep existing`、`replace with proposed`、`merge both`
- 冲突处理完成后展示 `git diff`

### v2.1

目标：

- 在已有仓库初始化主线之上，提高分析质量、审阅效率和规则提升能力

候选范围：

- 提升 `analyze-existing` 对 domain 和 migration suggestions 的自动生成质量
- 提升 `merge` 建议清单的可读性
- 增强 `read` 摘要与状态展示
- 改进 `prune` 和 `split` 的 proposal 结构与审阅流
- 定义 runtime 经验显式提升为 skill 规则的流程

### v2.2

目标：

- 在稳定分析能力之后，继续增强冲突处理与人工重写协作体验

候选范围：

- 为 `rewrite manually` 提供更强的协作支撑
- 细化 init/apply/conflict 过程中的差异展示和审阅体验
- 评估是否需要把 `init` 的分析与 apply 拆成更显式的子命令界面

## Backlog Candidates

- 是否需要任务级总览文件
- 是否需要副语言同步的更细粒度策略
- 是否需要更强的模板本地化能力
- 是否需要用于 skill 规则提升的显式 `promote` 动作

## Completed Versions Archive Policy

- 已完成版本移入归档，不挤占当前与未来版本计划
