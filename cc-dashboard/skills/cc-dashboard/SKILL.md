---
name: cc-dashboard
version: 0.1.0
description: Use when multiple agent sessions accumulate pending user actions across sendbox letters / handoffs / external trackers and the user (or product owner) loses sight of "what do I owe right now?". Defines a single markdown file — `docs/Dashboard/index.md` — as the projection layer over scattered sendbox/handoff/tracker artifacts, with row schema, six action types (decision/start/review/triage/destructive/ops), write triggers tied to sendbox events, mark-done ownership options, and a 14-day rolling archive. Companion to the sendbox-protocol skill — projection layer, not replacement.
---

# CC Dashboard — Pending User Actions

A single source of truth (SSOT) for "what does the user need to do next?" across multi-agent / multi-session workflows. Built as a **projection** over scattered sendbox letters, handoff briefs, and external tracker tickets — not a replacement for any of them.

## When to use

**Use when:**

- One repository hosts ≥3 active agent sessions (orchestrator + implementers + subagents) and each generates pending user asks
- User-facing letters accumulate in `docs/sendbox/toUser/` and the user must read 5+ files to reconstruct "what's pending"
- A single letter contains multiple independent user decisions / actions with different completion timelines
- The user wears multiple roles (driver / courier / session-starter / reviewer) and switches modes frequently
- External trackers (Linear / Multica / Jira) exist but they hold L2 work units, not atomic user actions

**Do NOT use when:**

- Single agent session, single user, single decision flow — chat is sufficient
- Tasks are immediately actionable and resolved within one turn — no projection layer adds value
- An external tracker already provides personal-action granularity AND the team consistently uses it

**Reachability test:** if the user can answer "what do I owe right now?" in under 30 seconds by opening ONE file or screen, you don't need this skill. If they need ≥4 surfaces, you do.

## Core principles

1. **Atomic-action granularity, not letter granularity.** A letter with three independent user decisions emits three dashboard rows, not one. Atomic granularity matches the user's mental model ("am I done with this decision yet?") and lets row lifecycle decouple from letter lifecycle.
2. **Projection, not replacement.** Sendbox letters, handoffs, and tracker tickets remain authoritative for their domain. The dashboard projects pending user actions out of them; it never owns the underlying state.
3. **Any session writes, user reads, anyone marks done.** Writes happen at the trigger (letter creation, handoff creation, new external blocker observed). Reads are user-initiated. Mark-done can be any session that observes completion (low maintenance burden; rare stale rows self-correct).
4. **Markdown table for v1.** No SaaS, no SQL, no custom UI. A plain markdown table in a single file under version control. Resist premature complexity — the cost of switching later is one tool-driven migration script, not a redesign.
5. **One file per repo at the canonical path.** `docs/Dashboard/index.md`. Multi-repo orchestration reads each repo's file independently; do not centralize across repos.

## Data location

- **Canonical path**: `docs/Dashboard/index.md`
- **Two sections**: `## Active` (open rows) and `## Archive` (recently-done rows, rolling 14 days)
- **Versioning policy** (recommended):
  - v1 = single markdown table — start here
  - v2 = optional split into multiple files when row count or type-mix exceeds practical limits (not a commitment)
  - v5 = revisit technology stack (web UI, structured data, richer renderer) — not on day-1 roadmap

## Row schema

| Column | Required | Notes |
|---|---|---|
| `ID` | yes | `UN-NNN` monotonic; new row = `max(Active ∪ Archive) + 1` |
| `Type` | yes | One of `A`/`B`/`C`/`D`/`E`/`F` — see Action types |
| `Action` | yes | Imperative one-line description (language policy is repo-scoped — see below) |
| `Where (detail)` | yes | Path to sendbox letter / URL to MR / tracker issue link with anchor |
| `Blocker for` | yes | What this action unblocks (downstream L2 ship, decision, release, etc.) |
| `Since` | yes | `YYYY-MM-DD` of row creation |
| `Status` | yes | `open` or `done` |

### Action types

| Code | Type | Examples |
|---|---|---|
| **A** | Decision / Approve | Answer a mini-decision; approve a plan; pick between options |
| **B** | Start session | Kick off an implementer session in a worktree; start a dogfood / research session |
| **C** | Review / Merge | Review MR; walk verify; merge a branch |
| **D** | Read + Triage | Read a report and decide scope / timing / follow-up L2 |
| **E** | Destructive ops | Manual force-push, hard-reset, worktree burn — user executes, not the agent |
| **F** | Ops / Admin | Env config; token rotation; external credentials |

If a candidate row doesn't fit any type, the action probably doesn't belong in the dashboard — challenge whether it is truly user-blocking.

## Write triggers

A session MUST append rows to `docs/Dashboard/index.md § Active` when:

| Trigger | Row count | Typical type |
|---|---|---|
| Writing `docs/sendbox/toUser/*.md` letter | 1..N — one per atomic ask | A / C / D |
| Writing `docs/sendbox/to<Implementer>/*.md` handoff | ≥1 — at minimum "Start <Implementer> session" | B |
| Identifying a user-blocking action with no sendbox doc (upstream MR awaiting merge; external CVE alert needing triage) | 1 | C / D / F |

**Rule of thumb**: 1 letter → N rows. Resist 1 letter → 1 row — it collapses atomic actions and recreates the original "user has to read the whole letter to find pending sub-asks" pain.

## Mark-done protocol

Four ownership options. Pick one per repo and codify it in your repo's hook config:

| Option | Pros | Cons |
|---|---|---|
| **(a) Any session + user** | Lowest maintenance; rare stale rows self-correct when user notices | Occasional double-mark (harmless) |
| **(b) Orchestrator only** | Centralized; reviewer-visible | Orchestrator can miss; implementer can't help |
| **(c) User only** | Authoritative | Adds friction for user |
| **(d) Row author only** | Pairs creation and closure | Author session may be dead by completion time |

**Default recommendation: (a)**. Lowest friction; the failure mode (stale row) is benign and self-corrects when the user observes it ("UN-005 is done" → any session marks it).

After mark-done, **move** the row from `## Active` to `## Archive` in the same commit. Do not leave `done` rows in Active.

## Archive protocol

`## Archive` retains rows for **14 days rolling**. Older rows can be `git rm`'d — git log preserves the full history. No automation required v1; opportunistic housekeeping on dashboard touches is sufficient.

## Sendbox-protocol coupling

When `cc-sendbox`'s `sendbox-protocol` skill is also active in the repo, the two protocols are **independent with overlapping triggers**:

- Sendbox letter lifecycle = `burn` / `archive` / `persist`, ends when the recipient's lifecycle ends.
- Dashboard row lifecycle = `open` → `done` → archived → garbage-collected.
- The two lifecycles do not bind. A letter MAY burn while a derived row remains open (rare — usually means the letter recipient finished before the user acted). A row MAY be `done` while its source letter is still active (common — the letter has other asks still pending).

**Authoring rule**: every sendbox letter to user, and every handoff to implementer, triggers dashboard row append. **Cleanup rule**: burning a letter must NOT cascade-delete dashboard rows.

## Anti-patterns

**1 letter → 1 row "to keep it simple".** Defeats the purpose. The whole point is atomic actions; a letter aggregating three decisions emits three rows.

**Putting L2 work units in the dashboard.** L2s belong in your task tracker (Multica / Linear / Jira). Dashboard rows are *user actions on L2s*: "review this L2's MR", "approve this L2's scope". The L2 itself is not a user action.

**Letting the Archive grow forever.** After 14 days, `git rm` archived rows. History is in git log. Dashboards showing 6 months of done items are noise.

**Mixing dashboard rows into letter frontmatter.** Tempting because triggers overlap — but row fields, lifecycle, and cardinality differ. Keep files separate.

**Creating per-action files instead of one table.** Regresses to the original "many files = scattered" pain. The whole table being scannable in one screen is the point.

**Skipping the dashboard for "trivial" letters.** If you wrote a letter, the letter is non-trivial enough to warrant ≥1 row. If a letter is truly trivial, don't write the letter — chat is fine.

**Backfilling without scanning for completions.** When initializing the dashboard, scan existing sendbox letters and tracker tickets and mark already-completed actions directly into Archive — do NOT dump them into Active.

## File template

When initializing the dashboard in a new repo, create `docs/Dashboard/index.md`:

```markdown
# User Now — Pending Actions

> Single source of truth for "what the user needs to do next".
> Authors: any agent session may append. Reader: user.
> Protocol: see your repo's cc-dashboard hook config (or the portable skill).

## Active

| ID | Type | Action | Where (detail) | Blocker for | Since | Status |
|---|---|---|---|---|---|---|

## Archive

| ID | Action | Done | By |
|---|---|---|---|
```

## Adopting in a new repo

1. Run the reachability test. If users can answer "what do I owe?" by opening ≤1 surface, skip this skill.
2. Pick a mark-done ownership option (default: any session + user).
3. Decide your **language policy** for the `Action` column. The skill is language-neutral; declare in your repo:
   - English-only (default for international repos)
   - Local language (e.g., 中文 for a 中文-primary repo) — declare in your hook config
   - Schema enums (`Type`, `Status`) and structural fields (`ID`, `Since`, file paths) always stay ASCII
4. Decide your **action-type set**. The six types A/B/C/D/E/F cover most workflows; only extend if you have a recurring 7th category and can name it.
5. Create `docs/Dashboard/index.md` from the template above.
6. Backfill by scanning `docs/sendbox/toUser/`, active handoffs, and external tracker tickets assigned to the user. Mark already-done actions directly into Archive.
7. Add a hook config file in your repo's harness/process docs that codifies: data path, action types, write triggers, mark-done owner, language policy. Reference this skill for the protocol contract.
8. Cross-link from your repo's `CLAUDE.md` / `AGENTS.md` "Where to look" table so future sessions discover the dashboard at session start.

## Quick start commands

```bash
# 1. Create directory and seed file
mkdir -p docs/Dashboard
cat > docs/Dashboard/index.md <<'EOF'
# User Now — Pending Actions

> Single source of truth for "what the user needs to do next".

## Active

| ID | Type | Action | Where (detail) | Blocker for | Since | Status |
|---|---|---|---|---|---|---|

## Archive

| ID | Action | Done | By |
|---|---|---|---|
EOF

# 2. (Optional) Add to your CLAUDE.md "Where to look" table
#    Manual edit — append: "| Know what the user owes now | docs/Dashboard/index.md |"

# 3. Author your repo-local hook config (path varies by recipe; example for OSR+ECC):
#    docs/HarnessStack/hooks/cc-dashboard.md  — codifies repo-specific choices
```

## Boundary (what this skill MUST NOT do)

- Modify any pipeline step ordering, merge gates, or verification topology of an adopting recipe (OpenSpec / Superpowers / OSR+ECC / etc.).
- Become source of truth for L2 work units, OpenSpec change records, or RepoMem persist content.
- Replace tracker-tool dashboards (Linear, Multica) — the cc-dashboard is *user-action* granularity; trackers are *work-unit* granularity.
- Cascade delete or modify upstream sendbox letters when rows are marked done.

Violations invalidate the hook in the adopting repo; correct before re-enabling.

## Provenance

Distilled from the `everclaw` repository's HarnessStack hook (`docs/HarnessStack/hooks/cc-dashboard.md`), itself born from a research-subagent proposal that evaluated Linear / Multica / file-based options for managing multi-agent pending-user-action sprawl. Business-specific identifiers (EVE-NN issue keys, MR numbers, project-specific letter paths) intentionally absent from this portable skill.

## See also

- `sendbox-protocol` (skill in the `cc-sendbox` repo) — companion protocol for the underlying letters this skill projects from. Adopting cc-dashboard without sendbox-protocol is supported but less coherent.
