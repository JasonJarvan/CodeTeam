# HarnessStack 选择标准

## 用途

使用本参考决定：

- 仓库是否需要更新长效契约
- 哪种临时契约形态最适应当前任务
- 当前任务应启用哪些工作流层级

## 主轴

### 1. 长效仓库上下文

用于 `docs/HarnessStack/longterm.md`。

- 协作规模
  - `solo`：1 名贡献者
  - `small-team`：2～5 名贡献者
  - `large-team`：6 名及以上贡献者
- 仓库类型
  - `product`
  - `research`
  - `platform`
  - `other`
- 项目周期
  - `short-lived`
  - `long-lived`

### 2. 临时任务上下文

用于 `docs/HarnessStack/temporary-<task>.md`。

- 需求清晰度
  - `clear`
  - `partially-clear`
  - `vague`
- 交付目标
  - `<3h test`
  - `PoC`
  - `Demo`
  - `MVP`
  - `Alpha`
  - `Beta`
  - `MMP`
  - `RC`
  - `GA`
- 风险等级
  - `low`
  - `medium`
  - `high`
- 对长效知识的影响
  - `none`
  - `low`
  - `medium`
  - `high`

## 层级默认

在任务特定调整之前，使用以下默认。

### solo

- 优先 `Superpowers`
- 仓库为长期时增加 `RepoMem`
- 变更需要稳定规格边界时增加 `OpenSpec`
- 当记忆、钩子或验证对仓库有益时轻度启用 `ECC`

### small-team

- 优先 `Superpowers + RepoMem`
- 协作成本上升后将 `OpenSpec` 作为常规规格层
- 当共享上下文与护栏重要时以中等强度增加 `ECC`
- 仅当简单执行纪律不足时再加强主工作流

### large-team

- 默认基线优先 `OpenSpec + RepoMem + ECC`
- 将 `Superpowers` 作为执行纪律层
- 协调成本高时升级主工作流为更重的规划体系

## 需求清晰度默认

### clear

- 尽量少叠工作流
- 优先执行导向流程
- 仅在交付目标或风险需要时增加规格层

### partially-clear

- 在实现前增加足够结构以稳定范围
- 若仓库尚未明确范围，优先增加 `OpenSpec`

### vague

- 优先探索先行流程
- 不要直接进入重实现执行
- 先加强规划与范围定义层

## 交付目标调节

用于增减流程强度。

- `<3h test`
  - 强烈偏好最小可行流程
- `PoC` 或 `Demo`
  - 允许更轻的规格与更轻的长效记忆更新
- `MVP` 或 `Alpha`
  - 提高明确范围与验证的价值
- `Beta` 或 `MMP`
  - 需要更强验证与更稳定的知识沉淀
- `RC` 或 `GA`
  - 需要最强验证、收尾与护栏强度

## 长效基线重写条件

仅在以下至少一项为真时更新 `docs/HarnessStack/longterm.md`：

- 协作规模发生实质变化
- 仓库类型发生实质变化
- 仓库周期预期发生实质变化
- 默认长效工作流栈发生实质变化

否则仅生成 `temporary-<task>.md`。
