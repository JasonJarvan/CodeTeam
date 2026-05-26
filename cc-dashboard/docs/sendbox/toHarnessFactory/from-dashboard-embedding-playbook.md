---
recipients:
  - role: HarnessFactory factory agent producing or upgrading a HarnessStack-managed repository, deciding whether and how to embed cc-dashboard
    purpose: drive the embed/skip decision and execute the embed correctly when needed
    lifecycle: persist (canonical embedding playbook; updates supersede in place)
on_lifecycle_end: persist
created: 2026-05-26
created_in: main agent in cc-dashboard repo, drafted during initial repo bootstrap
---

# Embedding playbook — `cc-dashboard` into a HarnessStack repo

This letter tells a HarnessFactory agent (1) whether the target repo needs cc-dashboard, and (2) exactly what to do to embed it when needed. It is HarnessStack-specific. Generic adopters should read [`../../skills/cc-dashboard/SKILL.md`](../../skills/cc-dashboard/SKILL.md) directly.

## 1. Audience + prerequisite

You are a HarnessFactory factory agent. You have just produced or are about to upgrade a target HS repo and must decide whether `cc-dashboard` belongs in it.

**Authoritative skill source**: [`../../skills/cc-dashboard/SKILL.md`](../../skills/cc-dashboard/SKILL.md) (or upstream `~/.claude/skills/cc-dashboard/SKILL.md` after install).

**One-paragraph overview**: cc-dashboard maintains a single markdown file (`docs/Dashboard/index.md`) listing every pending action the user owes — projected out of sendbox letters, handoff briefs, and external tracker tickets. Atomic granularity (a letter with three asks → three dashboard rows). Independent lifecycle from letters (`open → done → archived`). Written by any agent session at letter/handoff creation; read by the user; mark-done by anyone observing completion.

**Required companion**: `cc-sendbox`'s `sendbox-protocol` skill. cc-dashboard projects out of the sendbox letter universe; without sendbox-protocol it has nothing to project from. If the target repo doesn't (or won't) have sendbox-protocol embedded, do not embed cc-dashboard.

## 2. Decision tree — embed or skip?

Embed cc-dashboard into the target HS repo when **all three** dimensions below hold:

### 2.1 sendbox-protocol prerequisite

| Target repo state | Embed cc-dashboard? |
|---|---|
| `sendbox-protocol` not embedded | Skip — defer until sendbox is embedded |
| `sendbox-protocol` embedded but `toUser/` rarely or never used | Skip — no user-action surface to project |
| `sendbox-protocol` embedded with active `toUser/` + multi-implementer flow | Continue to §2.2 |

### 2.2 Recipe / scale dimension

| Target recipe | Embed cc-dashboard? |
|---|---|
| `superpowers` (no RepoMem) | Skip — single-session execution discipline; no dashboard surface |
| `superpowers-repomem` (solo, library) | Skip by default — re-evaluate if multi-implementer work emerges |
| `openspec-superpowers-repomem` (small-team product) | Embed iff §2.3 also says yes |
| `openspec-superpowers-repomem-ecc` (small-team product, hardened) | Embed by default if §2.3 says yes |
| Any recipe extending a primary-workflow layer (BMAD / gstack / GSD) | Embed by default |

### 2.3 User-action surface dimension

Embed if **any** of these is plausible in the target repo's near-term work:

- ≥3 active agent sessions (orchestrator + implementers + subagents) accumulating user-blocking asks
- A single letter typically contains ≥2 atomic user decisions/actions with distinct completion timelines
- The user wears multiple roles (driver / courier / session-starter / reviewer) and switches frequently
- External trackers exist (Linear / Multica / Jira) but they hold L2 work units, not user-action granularity
- Reachability test fails: the user needs to open ≥4 surfaces to answer "what do I owe right now?"

If none of these is plausible, skip even if §2.1 + §2.2 say embed. Re-evaluate when work mode changes.

### 2.4 Skip outcome

If skipping: do NOT create `docs/Dashboard/`, do NOT add a hook config. Record the decision in the target repo's `version-plan[.{lang}].md` "future considerations" / "未来考虑" section so a future factory pass can reconsider.

## 3. Embedding checklist (when §2 says embed)

### 3.1 Skill registration

Symlink (or copy) the skill into the user's CC skills directory:

```sh
ln -s "$(realpath ${CC_DASHBOARD_REPO})/skills/cc-dashboard" ~/.claude/skills/cc-dashboard
```

Verify CC discovers it at next session start (look for `cc-dashboard` in the available-skills list).

### 3.2 Hook config in the target repo

Create `<target>/docs/HarnessStack/hooks/cc-dashboard.md` following the same shape as the multica / sendbox hook files in the source repos. Required sections:

- Status / Scope / Skip-protocol / Authority frontmatter (bullet block)
- Purpose paragraph
- Data Location (path + versioning policy)
- **Language Policy** — declare the `Action`-column language for THIS repo (English / 中文 / etc.)
- Row Schema (copy from SKILL.md)
- Action Types (A–F; extend only if a recurring 7th category exists with a clear name)
- Write Triggers (sendbox letter / handoff / external blocker)
- Mark-Done Protocol — pick one of (a)/(b)/(c)/(d) from SKILL.md and codify it here
- Archive Protocol (default 14-day rolling)
- Sendbox-protocol Coupling note (independent lifecycle, overlapping triggers)
- Hook Boundary (MUST NOT modify pipeline ordering / merge gates / verification topology)

### 3.3 Data file seed

Create `<target>/docs/Dashboard/index.md` from the template in SKILL.md §"File template". Backfill by scanning:

- `docs/sendbox/toUser/` letters — each atomic ask becomes 1 row (Type A/C/D)
- Active `docs/sendbox/to<Implementer>/handoff.md` files — each becomes 1 Type-B row
- External tracker assignments to the user — MRs awaiting merge → Type-C, alerts needing triage → Type-D

Mark already-completed actions directly into `## Archive` — do NOT dump them into `## Active`.

### 3.4 Wire into the target's `longterm.md`

Add a row to the `## Hooks` table:

```markdown
| [`hooks/cc-dashboard.md`](hooks/cc-dashboard.md) | active | Maintain `docs/Dashboard/index.md` as SSOT for pending user actions; trigger on any session write to `docs/sendbox/` or identification of a new user-blocking action |
```

### 3.5 Wire into the target's `CLAUDE.md` / `AGENTS.md`

Add a row to the "Where to Look" table:

```markdown
| Know what the user owes now | `docs/Dashboard/index.md` (protocol: `docs/HarnessStack/hooks/cc-dashboard.md`) |
```

### 3.6 Acceptance checklist

- [ ] `docs/Dashboard/index.md` exists with seeded Active + Archive sections
- [ ] `docs/HarnessStack/hooks/cc-dashboard.md` exists with all required sections including repo-local Language Policy
- [ ] `longterm.md` `## Hooks` table contains the new row
- [ ] `CLAUDE.md` / `AGENTS.md` "Where to Look" references the dashboard path
- [ ] Skill discoverable via `Skill cc-dashboard` in a fresh CC session

## 4. Co-evolution with sendbox-protocol

cc-dashboard and sendbox-protocol must move together in the target repo:

- If `sendbox-protocol` is upgraded (new letter types, new lifecycle states), check whether new Action Types are needed in cc-dashboard — if so, register them in the target repo's hook config (do not extend the portable skill without a recurring justification).
- If `sendbox-protocol` is retired from the target repo, retire cc-dashboard too — they share a soft dependency.
- If a target repo replaces sendbox-protocol with a different inter-session-comm convention, re-evaluate cc-dashboard's fit; it may still apply if the substitute produces analogous letter-like artifacts.

## 5. Anti-patterns to surface in your post-run report

If you observe any of the following during your factory pass on a target repo, surface them in your report:

- Dashboard rows duplicating L2 tracker issues at L2 granularity (should be user-action granularity only)
- Dashboard rows accumulating in `## Active` without being marked done for >14 days (mark-done discipline broken)
- `## Archive` section growing unboundedly (housekeeping skipped)
- Letters being burned while their derived rows remain open without an explanation in commit message (lifecycle decoupling broken / forgotten)
- Multiple dashboard files appearing under `docs/Dashboard/` without a clear split rationale (premature v2 split)

## 6. Versioning

This playbook tracks the cc-dashboard skill version. Current: **v0.1.0 (2026-05-26)**.

When the skill bumps to v0.2.x (file-split or schema extension), update §3.2 / §3.3 to reflect new shape. When the skill bumps to v0.5.x (technology-stack change to web UI / structured data), this playbook needs a major revision — flag the gap before proceeding with a factory run against the new version.
