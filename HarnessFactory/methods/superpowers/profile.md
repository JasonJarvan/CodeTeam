# Profile — superpowers

## Identity

- Upstream name: Superpowers
- Layer: Execution Discipline
- Status: established
- Source location: `~/.claude/skills/superpowers:*` (skill plugin set)

## Lifecycle Coverage

Stage mapping uses the 8-stage scale from `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 判断标准`.

| 目标定义 | 需求澄清 | 方案设计 | 任务规划 | 实现开发 | 测试验证 | 发布交付 | 运行反馈与迭代沉淀 |
|---|---|---|---|---|---|---|---|
| 辅助覆盖 | 辅助覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 主覆盖 | 辅助覆盖 |

## Capabilities

- Execution-discipline chain: `brainstorming → using-git-worktrees → writing-plans → executing-plans → TDD → requesting-code-review → finishing-a-development-branch`.
- Pre-implementation planning gates (writing-plans) and post-implementation verification gates (verification-before-completion).
- Subagent dispatch (subagent-driven-development) for parallel and isolated task execution.

## Conflicts & Dependencies With Other Methods

- vs RepoMem: writing-plans defines HOW; RepoMem temporary docs record WHY/context. Never duplicate plan steps into memory. (Source: `../../harness-factory/assets/templates/recipes/superpowers-repomem.md § Cross-Layer Conflicts`)
- vs OpenSpec: when both active, OpenSpec change cycle takes precedence for scope boundaries; Superpowers execution discipline runs inside an OpenSpec change.
- No dependency on any other layer to function; Superpowers is the canonical minimum execution-discipline layer.

## Embedding Mechanics

- Required? no — Superpowers is a skill set the user installs once; no per-target embedding action.
- Playbook: n/a
- Activation cost: none (the skill is already present in any Claude Code env that has the plugin installed)

## Recipes That Use This Method

- `../../harness-factory/assets/templates/recipes/superpowers.md`
- `../../harness-factory/assets/templates/recipes/superpowers-repomem.md`
- `../../harness-factory/assets/templates/recipes/openspec-superpowers-repomem.md`
- `../../harness-factory/assets/templates/recipes/openspec-superpowers-repomem-ecc.md`

## Source References

- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § Superpowers` (narrative)
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 生命周期覆盖矩阵` (matrix row)
- `../_comparison/lifecycle-workflow-comparison.zh-CN.md § 第三组：Superpowers` (overlap/boundary)
