---
domain: global
last_reviewed_at: 2026-04-03
---

# 记忆索引

## Purpose

这份文档是当前 `RepoMem` 子仓库长期记忆的全局导航层，记录跨 domain 的隐性知识、约束和维护规则。

## Global Constraints And Invariants

- `RepoMem` 既要能独立发布，也要能作为其他仓库的仓库记忆层使用。
- skill 包规则、模板源和运行态事实文档必须保持隔离。
- 主语言驱动整个 RepoMem 工作流输出；副语言只作为 `persist` 的镜像层。
- 长期层与临时层必须严格分离。

## Domain Memory Map

| Domain | Focus | Doc |
| --- | --- | --- |
| repo-mem | RepoMem 的边界、HITL 规则、多语言、init 闭环与迁移原则 | [repo-mem](./repo-mem.md) |

## Common Pitfalls And Decisions

- 不要把 skill 模板与 runtime 实例文档放在同一语义目录里。
- 不要让 `capture` 直接改长期层。
- `prune` 和 `split` 必须走 HITL 建议流程。
- `domains` 保留，但其值来自架构索引中的 domain map。

## Read Order

- 先读本文件，再读 [repo-mem](./repo-mem.md)。

## Prune And Split Guidance

- 失效记忆通过 `prune` 建议流程处理。
- 混合主题或过长文档通过 `split` 建议流程处理。
