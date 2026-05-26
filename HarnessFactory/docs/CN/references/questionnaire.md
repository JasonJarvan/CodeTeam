# HarnessStack 问卷

## 用途

使用本问卷仅收集生成或更新以下文档所需信息：

- `docs/HarnessStack/longterm.md`
- `docs/HarnessStack/temporary-<task>.md`

只问确定正确输出所必需的**最少**问题。

## 长效问题

仅在以下情况询问：

- 不存在 `docs/HarnessStack/longterm.md`，或
- 有理由认为长效基线需要完整重写

### Q1. 协作规模

- 本仓库有多少活跃贡献者？

规范为：

- `solo`
- `small-team`
- `large-team`

### Q2. 仓库类型

- 本仓库主要是产品、研究还是平台类？

规范为：

- `product`
- `research`
- `platform`
- `other`

### Q3. 项目周期预期

- 本仓库预期短命还是长期维护？

规范为：

- `short-lived`
- `long-lived`

### Q4. 长效知识治理

- 本仓库是否需要持久的架构、记忆与版本计划治理？

规范为：

- `enabled`
- `disabled`

## 临时任务问题

针对当前任务询问。

### Q1. 任务名称

- 本任务最短且稳定的名称是什么？

用于命名 `temporary-<task>.md`。

### Q2. 需求清晰度

- 需求已经清晰、部分清晰，还是仍模糊？

规范为：

- `clear`
- `partially-clear`
- `vague`

### Q3. 交付目标

- 预期交付目标是什么？

规范为：

- `<3h test`
- `PoC`
- `Demo`
- `MVP`
- `Alpha`
- `Beta`
- `MMP`
- `RC`
- `GA`

### Q4. 风险等级

- 任务风险为低、中还是高？

规范为：

- `low`
- `medium`
- `high`

### Q5. 对长效知识的影响

- 本任务是否可能产生应在任务结束后仍保留的知识？

规范为：

- `none`
- `low`
- `medium`
- `high`

## 问题最少化规则

- 若仓库已有稳定的 `longterm.md`，除非触发重写条件，否则跳过长效问题。
- 若任务明显很小且低风险，不要过度追问。
- 若仓库上下文已能回答问题，不要重复询问。
- 优先规范为上述预定义取值。
