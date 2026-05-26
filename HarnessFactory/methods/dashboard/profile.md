# Profile — dashboard

## Identity

- Upstream name: cc-dashboard
- Layer: Harness Enhancement
- Status: new candidate
- Source location: `~/.claude/skills/cc-dashboard/SKILL.md` (skill); upstream repo: cc-dashboard

## Lifecycle Coverage

Dashboard is a projection layer over sendbox letters, not a lifecycle-stage workflow. Stage matrix for consistency:

| 目标定义 | 需求澄清 | 方案设计 | 任务规划 | 实现开发 | 测试验证 | 发布交付 | 运行反馈与迭代沉淀 |
|---|---|---|---|---|---|---|---|
| 基本不覆盖 | 辅助覆盖 | 基本不覆盖 | 基本不覆盖 | 基本不覆盖 | 基本不覆盖 | 基本不覆盖 | 辅助覆盖 |

Dashboard is "辅助覆盖" only at `需求澄清` (surfaces pending user decisions) and `运行反馈与迭代沉淀` (records resolved actions in archive). Everything else is downstream of letter-creation events.

## Capabilities

- Single markdown file (`docs/Dashboard/index.md`) projecting every pending user-blocking action from sendbox letters, handoff briefs, and external trackers.
- Atomic granularity: one letter with three asks → three dashboard rows.
- Independent lifecycle from letters (`open → done → archived`); 14-day rolling archive.
- Six action types (decision / start / review / triage / destructive / ops).

## Conflicts & Dependencies With Other Methods

- **Hard dependency: sendbox** — dashboard projects out of the sendbox letter universe. Without sendbox embedded, dashboard has nothing to project. See `methods/sendbox/profile.md`.
- Dashboard rows MUST be user-action granularity, not L2 tracker issues — if external trackers exist (Linear, Multica, Jira), dashboard does NOT mirror their tickets at L2 granularity.
- vs Superpowers: dashboard is read-only by the user; it does not gate any Superpowers pipeline step.

## Embedding Mechanics

- Required? yes
- Playbook: `embedding-playbook.md`
- Activation cost: symlink skill + create `docs/HarnessStack/hooks/cc-dashboard.md` (hook config with repo-local Language Policy) + seed `docs/Dashboard/index.md` + add rows to `longterm.md § Hooks` and `CLAUDE.md` "Where to Look" table.

## Recipes That Use This Method

- (none yet; first recipe to adopt is the same downstream multi-implementer recipe expected to adopt sendbox)

## Source References

- `embedding-playbook.md` (this directory)
- Upstream skill: `~/.claude/skills/cc-dashboard/SKILL.md`
- Original letter (pre-promotion): `<sender-repo>/docs/sendbox/toHarnessFactory/from-dashboard-embedding-playbook.md`
- Companion profile: `../sendbox/profile.md`
