---
domain: repo-mem
last_reviewed_at: 2026-04-03
---

# repo-mem

## Purpose

记录 RepoMem 作为 skill 包、模板源和自举运行态实例时的总体结构。

## Responsibilities

- 提供 `repo-mem` skill 包
- 提供初始化目标仓库所需的模板与脚本
- 用 `docs/RepoMem/` 管理 RepoMem 自己的长期与临时文档

## Key Structures Or Flows

- `RepoMem/repo-mem/`：可发布 skill 包
- `RepoMem/repo-mem/assets/templates/`：初始化模板源
- `RepoMem/docs/RepoMem/`：RepoMem 自举长期事实层与临时工作区

## Boundaries And Dependencies

- `docs/RepoMem/` 是 RepoMem 自己的实例事实层，不是 skill 规则源
- runtime 经验不能自动进入 skill 内容
- skill 规则、模板和脚本必须与运行态文档隔离

## Related Memory

- 见 [repo-mem](../memory/repo-mem.md)
