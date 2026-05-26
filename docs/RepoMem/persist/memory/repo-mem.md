---
domain: repo-mem
last_reviewed_at: 2026-04-03
---

# repo-mem 记忆

## Constraints

- `repo-mem` 是仓库级长期知识治理 skill，不是全生命周期主 workflow。
- `merge` 永远需要 HITL 确认。
- `prune` 和 `split` 以建议驱动，人类可直接改文档，也可改建议后让智能体执行。
- `persist` 使用主语言；副语言只为 `persist` 提供可选镜像。
- 面向已有仓库的 `init` 必须先出 proposal，再进入 apply。

## Pitfalls

- 如果不把运行态与 skill 内容隔离，RepoMem 很容易被当前仓库特例污染。
- 如果把 `domains` 当作自由文本而不是 domain map 路由字段，`read` 和 `merge` 会不稳定。
- 如果让 `temp` 多语言化，会让主事实链路失真。
- 如果已有仓库初始化时直接覆盖长期文档，风险过高。

## Decision Rationale

- 使用 `RepoMem/repo-mem/` 存放 skill 包，使用 `RepoMem/docs/RepoMem/` 存放自举运行态事实与临时文档。
- 使用 `assets/templates/` 提供目标仓库初始化骨架。
- 保留 `domains` 字段，但由 AI 静默维护，不把元数据变化本身作为对用户的主要沟通内容。
- 后续 runtime 经验提升为 skill 通用规则，需要单独流程，暂不放入 `v1.0`。
- 既有仓库初始化使用 `temp/<slug>/init-proposal.md` 作为提案文档，而不是直接写长期层。
- `init apply` 时若遇到冲突，生成 `temp/<slug>/init-conflicts.md`，并按 `conflict_id` 逐条与用户对齐处理意见。
- 冲突解决完成后展示 `git diff`，与 `merge` 的 HITL 习惯保持一致。
- 所有等待用户回答的问题项都应使用编号或稳定 id，便于用户在对话中直接按项回复。
- 当前已实现的 init 冲突决策路径包括 `keep existing`、`replace with proposed` 和 `merge both`；`rewrite manually` 仍以人工处理为主。

## Related Architecture

- 见 [repo-mem](../architecture/repo-mem.md)
