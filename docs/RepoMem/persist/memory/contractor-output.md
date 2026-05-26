---
domain: workflow-system
last_reviewed_at: 2026-05-14
---

# contractor-output

## Constraints

- “可写入仓库的契约结果”第一阶段采用纯 Markdown 文档。
- contractor 文档与 RepoMem 长期记忆分离；RepoMem 只负责引用与沉淀相关决策。
- 长期 contractor 是仓库默认基线；临时 contractor 是任务级 patch，而不是新的长期基线。
- 方法仓库与目标开发仓库必须区分“模板源”和“激活结果”。

## Decisions

- 在方法仓库 `HarnessFactory` 中，模板与 skill 内容统一放在 `harness-factory/`。
- 在目标开发仓库中，`HarnessStack/` 目录只用于保存当前激活结果。
- 当前至少区分三类文档：
  - 长期 contractor 备选文档
  - 临时 contractor 备选文档
  - 激活结果文档
- 每个真实开发仓库同一时刻只应激活一个长期 contractor。
- 临时 contractor 用于说明当前任务如何嵌入、增补、绕开或收缩当前长期 contractor。
- 如果 skill 判断长期 contractor 已不适用，应输出“替换建议”，而不是静默重写。

## Recommended Output Shape

- 长期 contractor
  - 写死默认启用哪些长期 workflow
  - 明确五层基线：
    - 主 workflow 层
    - 规格层
    - 执行纪律层
    - 仓库记忆体层
    - harness 增强层
- 临时 contractor
  - 写清当前需求适用条件
  - 写清相对长期 contractor 的新增项
  - 写清相对长期 contractor 的跳过项
  - 写清组合方式与优先级
- 激活结果文档
  - 在目标开发仓库的 `HarnessStack/` 下保存
  - 记录当前生效的长期 contractor
  - 记录当前生效的临时 contractor
  - 记录当前最终激活的 workflow 组合

## Future Upgrade Path

- 如果纯 Markdown 对 agent 读取不够稳定，再升级为：
  - Markdown contractor 文档
  - 外加一个极简机器可读清单文件
- 机器可读层不应先于文档层出现，避免前期过度设计。

## Related Memory

- 见 [workflow-system](./workflow-system.md)
- 见 [github-repo-design](./github-repo-design.md)
