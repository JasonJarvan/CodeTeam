---
last_reviewed_at: 2026-05-15
---

# 版本计划

## 当前定位

当前仓库是 `HarnessFactory` —— 多工作流契约体系的**工厂仓库**，按用户引导
为每个目标仓库产出一份 `HarnessStack`（分层的 harness 配置）。仓库本身不
是任何具体业务仓库的工作根目录。

当前已确认：

- 仓库名 `HarnessFactory`，产出物名 `a HarnessStack`（每次产出 = 一份 HarnessStack）
- 方法仓库的主要顶层目录采用 `docs/`、`harness-factory/`、`output/`
- 产出物落到 `./output/{YYYY-MM-DD-HHmm}-{stack}/HarnessStack/`（v0.3.1：`{stack}` 编码 active 层组成，如 `superpowers-repomem`、`openspec-superpowers-repomem-eccMedium`）
- 目标开发仓库中的 `docs/HarnessStack/` 目录只保存当前激活结果
- contractor 第一阶段采用纯 Markdown；若 agent 读取稳定性不足，再升级为 `Markdown + 极简机器可读清单`

## v0.2 目标

- 固化 `HarnessFactory` 的仓库定位
- 将长期 contractor 与临时 contractor 的设计收敛为正式文档模板
- 在 `README.md` 中加入速查表与判断标准
- 在 `SKILL.md` 中加入问答式工作流选择逻辑
- 在 `harness-factory/` 中建立长期 contractor 与临时 contractor 的正式目录结构

## v0.2 待办

- 定义长期 contractor 的标准结构
- 定义临时 contractor 的标准结构
- 定义长期 contractor 与临时 contractor 的冲突优先级
- 定义 skill 的问答输入项与输出格式
- 定义 README 速查表的最短路径
- 将 `README.md` 改成真正的仓库首页说明

## v0.3 目标

- 完成 `HarnessStack` → `HarnessFactory` 仓库改名
- 完成 `harness-stack/` → `harness-factory/` 工厂源目录改名
- 引入产物结构 `./output/{run}/HarnessStack/`，固化目录与文件契约
- 引入产物顶层 README（AI 蒸馏入口），定义"压缩 Pipeline 不可成为权威"等防漂移约束
- `_kit-reference/` → `_reference/`，配套术语统一
- 清理 v0.2 之前的过期 examples 与 handoff 文档
- 在 RepoMem 中正式引入"调研层 / 推断层"工厂迭代分层概念
- 同步用户 auto-memory

## v0.3 待办

- 在真实目标仓库中跑一次产出流程，验证 `./output/<run>/HarnessStack/` 直接 copy 到 `docs/HarnessStack/` 可用
- 验证压缩 Pipeline 与 `longterm.md § Pipeline` 由同一 recipe source 渲染（不漂移）
- 验证 AI 在读完顶层 README 之后能正确蒸馏出 CLAUDE.md 内容
- 评估"调研层"是否需要专门 skill（v0.4 题）
- `harness-factory/SKILL.md § Output Rules` 增补一句：长期契约产物总是落在 `output/<run>/HarnessStack/longterm.md`（bundle 形式），与 README 同位；`docs/HarnessStack/` 仅在 dogfood 场景使用（2026-05-14 dogfood 测试中发现 Step 10 仅点名 README，未点名 longterm，落地依据只在 `references/output-shapes.md`）
- ~~`_reference/README.md` 二选一并落定~~ → **v0.3.1 已落定**（见下方 v0.3.1 段）

## v0.3.1 目标

- 解决 v0.3 暴露的 `_reference/` 缺口与目录命名问题
- 推进 dogfood 校验（本仓库直接产出到 `docs/HarnessStack/`）

## v0.3.1 决策与改动

- `_reference/README.md` 落点：**方案 ε + 改名 `_toUser/`**——`_reference/` → `_toUser/`，bundle 只保留 `_toUser/README.md` 一份人读手册；`version-plan-skeleton.md` 不进 bundle，在 `_toUser/README.md § Tracking HarnessStack Evolution` 中建议目标仓库自维护（推荐用 RepoMem skill 落到 `docs/RepoMem/persist/version-plan.md`）
- 产物路径段：`{scale}-{horizon}` → `{stack}`，编码 active 层组成（如 `superpowers-repomem`、`openspec-superpowers-repomem-eccMedium`）。理由：scale/horizon 已在 contract metadata 里、给定 stack 不影响层激活；新路径自描述
- 新增模板 `harness-factory/assets/templates/to-user-readme-template.md`
- `harness-factory/SKILL.md` Workflow 增 Step 11 渲染 `_toUser/README.md`；Resources 列表同步
- `harness-factory/references/output-shapes.md` 改 bundle 图、改路径定义、改"为什么 X 不进路径"那段（从"type 不进"改为"scale/horizon/type 都不进"）
- 顶层 `README.md` 同步：bundle 图、Quick Start 指针、Two-Layer Naming 表
- 不动：`docs/superpowers/specs|plans/2026-05-14-*`（历史时间戳记录）、`docs/CN/`（按指示 freeze 在 v0.2）

## v0.3.1 待办

- ~~dogfood：把本仓库当作目标仓库跑一次产出，写入 `docs/HarnessStack/`~~ → **done**（见 `memory/harness-factory-v0.3.1-validation.md`；longterm.md type 改 platform、新增 README 与 _toUser/README.md）
- ~~验证压缩 Pipeline（顶层 README §3）与 `longterm.md § Pipeline` 同源不漂移~~ → **done**（步骤 1-10 全等，第 11 步 prune/split 按"periodic, not per-task"压缩省略，非漂移）
- ~~验证 AI 蒸馏：拿顶层 README 蒸馏出 `CLAUDE.md` 草稿，作为后续基准~~ → **done**（草稿存于 `memory/harness-factory-v0.3.1-validation.md § AI Distillation`；常规态足够，5 类非常规场景需回查 longterm.md）
- **未验证**：`{stack}` 路径段（dogfood 不走 output/；需要一次真实 output 运行覆盖 `eccMedium` 等强度后缀场景）
- v0.4 候选：questionnaire 是否引入 `skill` / `method` 作为 type 枚举值
- v0.4 候选：模板渲染半自动化（当前 `output-readme-template.md` / `to-user-readme-template.md` 手填 placeholder，无脚本）

## v0.3.2 决策与改动

- Add-Only Principle 分双 scope：
  - **Target-Repo Scope（严格）**：目标仓库激活后，方法不脱活、recipe 升级走 copy-on-write、`Recipe Reference` 单行替换；非可破例（保持目标仓库的稳定性承诺）
  - **Factory-Internal Scope（默认 + 显式破例）**：工厂内部对 recipe / 模板内容的修改/删除允许，条件是更干净的契约、既有决策确实有误，或可显式通知/迁移目标仓库；破例必须在 recipe 的 `Last Updated Because` + commit message + （触及 load-bearing 规则时）version-plan 中声明
- 动机：v0.3.1 设计 v0.4 时发现，纯 add-only 会迫使 v0.4 把 burn 判据塞进 Task-End Disposition 新章节再 cross-ref 回 Merge Gates，而不是直接精修 Merge Gates。降级后保留了对目标仓库的承诺，又给工厂内部留出迭代空间
- 与 `Break-Glass For Recipe Invariants` 同形态（默认 deny + 显式破例）
- 改动文件：`harness-factory/SKILL.md § Add-Only Principle` 整段重写

## v0.4 目标

- 把已被 RepoMem 概念化但物理未落地的"调研层"显式化为顶层 `methods/` 目录
- 给每个已被 recipe 字面引用的方法（superpowers / repomem / openspec / ecc）补 profile
- 给在 selection-criteria 中作为"Default inactive"上调选项的方法（bmad / gstack / gsd）补 profile（status = research-only）
- 把外部 sendbox / dashboard 两个 playbook letter 晋升为候选层一级公民（profile + flat-markdown playbook）
- 让组装层（harness-factory/）显式 cite 候选层（SKILL.md Step 6.5 + selection-criteria 反链 + recipe-template 加 Method References 字段）

## v0.4 决策与改动

- 顶层新增 `methods/` 与 `harness-factory/`、`docs/`、`output/` 平级
- 不改 `harness-factory/` 名称（重命名为 `assembly/` 留作 v0.5 候选）
- 候选层维护 9 个 method 目录：superpowers, repomem, openspec, ecc, bmad, gstack, gsd, sendbox, dashboard
- 不动 `docs/CN/`（继续 freeze 在 v0.2）
- 不在本次为 sendbox / dashboard 增加新 recipe（recipe 编写是后续动作；profile 解锁但不要求）
- 源信 `from-{sendbox,dashboard}-embedding-playbook.md` 不在本任务里 burn，由 sendbox-protocol 的清扫机制处置

## 未来考虑

- 调研层的周期性 agent 化（v0.4+）
- 产出物的多人协作版本（多 stack 共存仓库的策略）
- contractor 输出的英文实用文档版
- （v0.4 候选）在 `openspec-superpowers-repomem` recipe 中同时引入**任务级文档分区**与**任务末处置判据**两块新章节——两轴必须同时设计，分区不清楚则无法判处置，处置不清楚则分区只是装饰：
  - **Task-Level Document Partition**：把 OSR+ECC kit `longterm.md § Task Identifier and Document Boundary` 的"三件套不得互相重复"规则上抬到 recipe Cross-Layer Conflicts，明确 `OpenSpec design.md` / `RepoMem architecture.md` / `RepoMem requirement.md` / writing-plans plan 之间的内容归属
  - **Task-End Disposition**：给 archive / `RepoMem.merge` / burn 三类处置写出 reviewer 判据表与 HITL 检查清单——把 `RepoMem.merge` 从"排序约束"升级为"带判据的过滤器"，并首次把 "burn" 作为合法且应主动声明的处置（防止默认全部 merge 造成长期记忆膨胀）
