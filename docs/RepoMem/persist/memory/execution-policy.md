---
domain: harness-stack-execution-policy
last_reviewed_at: 2026-05-14
---

# execution-policy

## Constraints

- 工厂在 v0.1 只有"是否需要 HITL"的二元位，下游 everclaw 激活后反馈
  `ask-first` 的语义在四个 recipe 间漂移：有的把它当"宣告即可"，有的
  当"等用户批准"，导致同名步骤在不同 recipe 里行为不一致。
- 实战中 auto-judge 类步骤（brainstorming / explore / writing-plans /
  worktrees）需要 agent 自主判断"跑还是跳"，但跳过必须留痕，否则
  reviewer 在 RepoMem.merge 时看不到决策路径。
- 留痕机制如果只有一档，会被同时用在"我按 Skip Criteria 跳了"和"我
  真的破坏了 recipe 不变式"两种场景，混在一起后 reviewer 无法区分
  真正需要人审的破例。
- OpenSpec 上游约定 change set 默认放 `./openspec/`，但在 RepoMem +
  HarnessStack 同居的方法层仓库中，把 OpenSpec 也收进 `docs/` 更
  一致；长期 contractor 模板必须能表达这种位置差异。
- longterm.md 在单文件形态下逼近 ~400 行后，agent 一次加载成本与
  reviewer 阅读成本同时上升；超阈值需要切多 hook。

## Decisions

- Execution Policy 升级为四档制：
  - `auto`：agent 直接执行，无需宣告
  - `auto-judge`：agent 自主判断跑或跳；跳时一行写入
    `temporary-<task>.md § Auto-Skip Log`，不打断用户
  - `ask-first`：agent 宣告后等用户显式批准，保留给外部可见或
    半不可逆的步骤
  - `HITL`：契约硬性人审，**仅 RepoMem.merge 一处使用，不可降级**
- 默认分类：
  - A 类（brainstorming / explore / writing-plans / worktrees）= `auto-judge`
  - B 类（security-scan / code-review / finishing-branch / archive）= `ask-first`
  - RepoMem.merge = `HITL`
- Mechanism Selection 双档：
  - `auto-judge` 步骤按 Skip Criteria 跳过 → `Auto-Skip Log`（轻量、
    一行、不打断）
  - 破坏 `auto` / `ask-first` / `HITL` 不变式，或跳过未触发
    Skip Criteria 的 `auto-judge` 步骤 → `Recipe Invariant Exceptions`
    （重量、需 reason + 补偿动作）
- OpenSpec Root 在 `longterm-template § Document Meta` 加可配字段：
  - 默认 `./openspec/`（与 OpenSpec 上游约定一致）
  - 推荐 `docs/openspec/`（与 RepoMem、HarnessStack 等方法层 `docs/`
    共置）
- longterm.md 输出 shape 自适应：
  - `≤ ~400 行` → 单文件
  - `> ~400 行` → 切 `Index + docs/HarnessStack/longterm/<section>.md`
    多 hook（progressive disclosure，对齐 skill-creator 模式）
- 影响落点：
  - `recipe-template.md` 加 Execution Policy 章节规范
  - 4 个 recipe（superpowers / superpowers-repomem /
    openspec-superpowers-repomem / openspec-superpowers-repomem-ecc）
    各填表
  - `longterm-template.md` 加 Execution Policy 段
  - `temporary-template.md` 加 Skip Bias 字段、Auto-Skip Log、
    Mechanism Selection 三处
  - `output-shapes.md` 落自适应阈值规则
  - `SKILL.md` 落 shape 切换说明

## Decision Path

- everclaw 下游激活后反馈 `ask-first` 语义在 recipe 之间不一致。
- 用户首选方案：三档制 `auto / auto-judge / HITL`，去掉 `ask-first`。
- 反对意见（采纳前提出）：去掉 `ask-first` 会让外部可见或半不可逆的
  步骤只能在"agent 自决"和"硬性人审"之间二选一，blast radius 失控；
  尤其 security-scan、PR push、归档这类步骤，缺一个显式的"宣告并等
  批准"档会丢掉用户在场感。
- 最终采纳：用户改采 everclaw 设计的四档制，`ask-first` 保留并使用
  语义清晰的命名，避免和 `auto-judge` 混淆。

## Open Questions

- A/B 类默认划分是基于当前 4 个 recipe 总结的，对于含 primary workflow
  的 recipe（BMAD、GSD 等），A/B 是否需要重新划线尚未验证。
- `Skip Bias` 目前只在任务级（`temporary-<task>.md`）声明，是否需要在
  recipe 级提供默认值（例如某 recipe 默认 `aggressive` / `conservative`）
  尚未决定。
- `Auto-Skip Log` 目前是单 session 的一行追加，未规定时间戳；跨 session
  同任务多次跳过时是否需要时间戳以便 reviewer 还原顺序，未决。

## Pitfalls

- 把 `Auto-Skip Log` 误用到"真正破坏 invariant"的场景：这是 Mechanism
  Selection 双档存在的根本原因；写入前必须先判断是否触发了 Skip Criteria。
- 用 `ask-first` 兜底所有外部可见步骤会反向稀释批准信号——只有真正
  blast radius 大的步骤应进 `ask-first`，否则用户会开始无脑批准。
- `HITL` 只授权给 RepoMem.merge 一处；任何 recipe 想给其他步骤升到
  `HITL` 都必须经过工厂层评审，不能在 recipe 内部静默升档。
- longterm.md shape 切换时，Index 与子文件之间的引用必须在同一次写入
  完成，否则 agent 加载 Index 后会找不到 hook 目标。

## Related

- 工厂源文件：
  - `harness-factory/assets/templates/recipes/recipe-template.md` § Execution Policy
  - `harness-factory/assets/templates/longterm-template.md` § Execution Policy
  - `harness-factory/assets/templates/temporary-template.md` § Skip Bias / Auto-Skip Log / Mechanism Selection
  - `harness-factory/references/output-shapes.md`
  - `harness-factory/SKILL.md`
- 相邻记忆：
  - [cross-method-invariants](./cross-method-invariants.md)
  - [template-evolution](./template-evolution.md)
