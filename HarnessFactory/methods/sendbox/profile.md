# Profile — sendbox

## Identity

- Upstream name: sendbox-protocol (cc-sendbox)
- Layer: Harness Enhancement
- Status: new candidate
- Source location: `~/.claude/skills/sendbox-protocol/SKILL.md` (skill); upstream repo: https://github.com/JasonJarvan/cc-sendbox

## Lifecycle Coverage

Sendbox is a cross-cutting communication protocol, not a lifecycle-stage workflow. The 8-stage matrix is not the most natural fit, but for consistency:

| 目标定义 | 需求澄清 | 方案设计 | 任务规划 | 实现开发 | 测试验证 | 发布交付 | 运行反馈与迭代沉淀 |
|---|---|---|---|---|---|---|---|
| 基本不覆盖 | 辅助覆盖 | 辅助覆盖 | 辅助覆盖 | 辅助覆盖 | 辅助覆盖 | 辅助覆盖 | 辅助覆盖 |

Sendbox is "辅助覆盖" across most stages because it is the *channel*, not the *content* — every multi-session lifecycle event may produce a letter, but no stage is owned by sendbox.

## Capabilities

- File-based asynchronous letters between agent sessions (under `docs/sendbox/to<Role>/`).
- Canonical letter types: `handoff`, `plan-ready`, `greenlight`, `blocker`, `decisions`, `milestone-done`, `archived`, `promote-to-durable`, `broadcast`.
- Lifecycle disposition: `burn` (default) / `archive` / `persist` (promoted-then-burned).
- A-12 stop-and-ask pattern for boundaries the agent cannot cross unilaterally.

## Conflicts & Dependencies With Other Methods

- Depends on: nothing structurally; runs alongside any other layer.
- Companion: cc-dashboard (`methods/dashboard/profile.md`) — dashboard projects out of the sendbox letter universe; without sendbox letters, dashboard has nothing to project.
- vs Superpowers: sendbox triggers overlay Superpowers steps (plan-ready, blocker, milestone-done, broadcast) without inserting new pipeline steps.
- vs RepoMem: `promote-to-durable` letters are the canonical bridge from sendbox transient knowledge to RepoMem long-term knowledge.

## Embedding Mechanics

- Required? yes
- Playbook: `embedding-playbook.md`
- Activation cost: symlink skill + one verbatim invariant paste into target `longterm.md § Cross-Method Invariants`. Do NOT pre-scaffold `docs/sendbox/` empty directories — it grows naturally as letters are written.

## Recipes That Use This Method

- (none yet; first recipe to adopt sendbox is expected to be a successor to `openspec-superpowers-repomem` for multi-implementer scenarios)

## Source References

- `embedding-playbook.md` (this directory)
- Upstream skill: `~/.claude/skills/sendbox-protocol/SKILL.md`
- Original letter (pre-promotion): `<sender-repo>/docs/sendbox/toHarnessFactory/from-sendbox-embedding-playbook.md`
