---
domain: harness-stack-execution-policy
last_reviewed_at: 2026-05-14
---

# cross-method-invariants

## Constraints

- 当 OpenSpec、RepoMem、HarnessStack 三套方法在同一目标仓库共存时，
  每套都有自己的"任务级文档"目录：
  - `openspec/changes/<change-id>/`
  - `docs/RepoMem/temp/<slug>/`
  - `docs/HarnessStack/temporary-<task>.md`
- 三处使用的任务标识符若各自独立，会出现 `<task>` ≠ `change-id` ≠
  `<slug>` 的情况，下游脚本和 reviewer 都无法把三处文档对应起来。
- 三处文档若各自完整复述需求 / 设计 / 决策，最终在 RepoMem.merge 阶段
  会出现大量重复内容，且修改一处而其他处不同步，造成长期失真。

## Decisions

- 单一任务标识符：硬规则 `<task>` = `change-id` = `<slug>`，三处同名，
  不允许通过任何字段映射或别名绕开。
- 任务级文档三件套不得互相重复内容：
  - `openspec/changes/<id>/` 负责 change set 的 spec delta 与 tasks
  - `docs/RepoMem/temp/<slug>/` 负责仓库记忆相关的临时上下文
  - `docs/HarnessStack/temporary-<task>.md` 负责相对长期 contractor
    的 patch（新增 / 跳过 / 组合）
  - 任一段内容只允许属于其中一处；reviewer 在 RepoMem.merge 时删除
    其他位置的重复段落
- 该规则在 `longterm-template.md` 落为 `Cross-Method Invariants` 节
  （硬规则，不可由 recipe 降级）。

## Rationale

- 该约束最早在 OSR+ECC kit 实战中被验证（详见 user-memory
  `kit_osr_ecc_invariants`），早期局限在单 kit 范围。
- v0.2 将其从单 kit 上提到长期 contractor 模板的跨方法层不变式，
  动机是：任何同时启用 OpenSpec + RepoMem + HarnessStack 的 recipe
  都会遇到同样的标识符与去重问题，应在工厂层一次性约束，避免每个
  recipe 重新发明。
- 把规则放在 longterm-template 而非 recipe-template，是因为它跨所有
  recipe 不变，且语义层级高于"层组合"。

## Pitfalls

- 早期 kit 示例把该节命名为 "Task Identifier and Document Boundary"，
  57 行教学版语境强，易被误读为单 kit 局部约束。v0.2 重命名为
  `Cross-Method Invariants` 以提示其跨 recipe 性质；旧名称在历史
  示例中仍保留，避免破坏 git history 索引。
- 该规则不约束方法仓库自身（HarnessFactory），只约束目标开发仓库；
  在方法仓库里讨论 v0.2 自身改动时不必触发去重检查。
- "不得重复"指内容层去重，不是路径层禁止——三处文件可以同时存在，
  也可以互相 link，只是各自承载的语义段不重叠。

## Related

- 工厂源文件：
  - `harness-factory/assets/templates/longterm-template.md` § Cross-Method Invariants
- 相邻记忆：
  - [execution-policy](./execution-policy.md)
  - [template-evolution](./template-evolution.md)
- user-memory：`kit_osr_ecc_invariants`（仍有效，作为 OSR+ECC kit
  级强化规则保留）
