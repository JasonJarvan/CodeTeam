# Embedding playbook — cc-dashboard into a HarnessStack repo

> Promoted from `cc-dashboard/docs/sendbox/toHarnessFactory/from-dashboard-embedding-playbook.md` on 2026-05-26. The original letter is on the sendbox-protocol `persist → promoted-then-burned` lifecycle; this is the durable form.

This playbook tells a HarnessFactory agent (1) whether the target repo needs cc-dashboard, and (2) exactly what to do to embed it when needed.

## 1. Prerequisite

Authoritative skill source: `~/.claude/skills/cc-dashboard/SKILL.md`.

**One-paragraph overview**: cc-dashboard maintains a single markdown file (`docs/Dashboard/index.md`) listing every pending action the user owes — projected out of sendbox letters, handoff briefs, and external tracker tickets. Atomic granularity. Independent lifecycle from letters (`open → done → archived`). Written by any agent session at letter/handoff creation; read by the user; mark-done by anyone observing completion.

**Required companion**: `sendbox-protocol` skill must be embedded in the target repo first. Without sendbox letters, dashboard has nothing to project.

## 2. Decision tree — embed or skip?

Embed when **all three** dimensions hold:

### 2.1 sendbox-protocol prerequisite

| Target repo state | Embed cc-dashboard? |
|---|---|
| `sendbox-protocol` not embedded | Skip — defer until sendbox is embedded |
| `sendbox-protocol` embedded but `toUser/` rarely or never used | Skip — no user-action surface to project |
| `sendbox-protocol` embedded with active `toUser/` + multi-implementer flow | Continue to §2.2 |

### 2.2 Recipe / scale dimension

| Target recipe | Embed cc-dashboard? |
|---|---|
| `superpowers` (no RepoMem) | Skip |
| `superpowers-repomem` (solo, library) | Skip by default — re-evaluate if multi-implementer work emerges |
| `openspec-superpowers-repomem` (small-team product) | Embed iff §2.3 also says yes |
| `openspec-superpowers-repomem-ecc` (small-team product, hardened) | Embed by default if §2.3 says yes |
| Any recipe extending a primary-workflow layer (BMAD / gstack / GSD) | Embed by default |

### 2.3 User-action surface dimension

Embed if **any** of these is plausible:

- ≥3 active agent sessions accumulating user-blocking asks
- A single letter typically contains ≥2 atomic user decisions/actions with distinct completion timelines
- The user wears multiple roles (driver / courier / session-starter / reviewer) and switches frequently
- External trackers exist but hold L2 work units, not user-action granularity
- Reachability test fails: the user needs to open ≥4 surfaces to answer "what do I owe right now?"

If none, skip even if §2.1 + §2.2 say embed.

### 2.4 Skip outcome

If skipping: do NOT create `docs/Dashboard/`, do NOT add a hook config. Record the decision in the target repo's `version-plan[.{lang}].md` "future considerations" / "未来考虑".

## 3. Embedding checklist (when §2 says embed)

### 3.1 Skill registration

```sh
ln -s "$(realpath ${CC_DASHBOARD_REPO})/skills/cc-dashboard" ~/.claude/skills/cc-dashboard
```

### 3.2 Hook config

Create `<target>/docs/HarnessStack/hooks/cc-dashboard.md` with these required sections:

- Status / Scope / Skip-protocol / Authority frontmatter
- Purpose paragraph
- Data Location (path + versioning policy)
- **Language Policy** — declare the `Action`-column language for THIS repo
- Row Schema (copy from upstream SKILL.md)
- Action Types (A–F)
- Write Triggers (sendbox letter / handoff / external blocker)
- Mark-Done Protocol — pick one of (a)/(b)/(c)/(d) from upstream SKILL.md
- Archive Protocol (default 14-day rolling)
- Sendbox-protocol Coupling note (independent lifecycle, overlapping triggers)
- Hook Boundary (MUST NOT modify pipeline ordering / merge gates / verification topology)

### 3.3 Data file seed

Create `<target>/docs/Dashboard/index.md` from the template in upstream SKILL.md. Backfill by scanning:

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
- [ ] `longterm.md § Hooks` table contains the new row
- [ ] `CLAUDE.md` / `AGENTS.md` "Where to Look" references the dashboard path
- [ ] Skill discoverable via `Skill cc-dashboard` in a fresh CC session

## 4. Co-evolution with sendbox-protocol

cc-dashboard and sendbox-protocol move together:

- If `sendbox-protocol` is upgraded (new letter types, new lifecycle states), check whether new Action Types are needed — register them in the target repo's hook config (do not extend the portable skill without recurring justification).
- If `sendbox-protocol` is retired from the target repo, retire cc-dashboard too.
- If a target repo replaces sendbox-protocol with a different inter-session-comm convention, re-evaluate cc-dashboard's fit.

## 5. Anti-patterns

Surface in your post-run report if observed:

- Dashboard rows duplicating L2 tracker issues at L2 granularity
- Dashboard rows accumulating in `## Active` without being marked done for >14 days
- `## Archive` section growing unboundedly
- Letters being burned while their derived rows remain open without explanation
- Multiple dashboard files appearing under `docs/Dashboard/` without a clear split rationale

## 6. Versioning

This playbook tracks the cc-dashboard skill version. Current: **v0.1.0 (2026-05-26)**. v0.2.x (file-split / schema extension) updates §3.2 / §3.3 shape. v0.5.x (technology-stack change to web UI / structured data) requires a major revision of this playbook.
