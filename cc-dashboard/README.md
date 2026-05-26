# cc-dashboard

> One markdown file is your team's pending-actions board. No SaaS, no SQL, no UI. Any agent session appends rows; the user reads at a glance; anyone observing completion marks done.

A portable convention for a **single source of truth** dashboard of pending user actions in multi-agent / multi-session repositories. Built as a *projection* over sendbox letters, handoff briefs, and external tracker tickets — never as a replacement.

## The problem

You're running an orchestrator plus N implementer sessions across worktrees. Pending user asks accumulate across seven `sendbox/toUser/` letters, two tracker systems (Linear / Multica / Jira), and three markdown state files. The user opens four surfaces and still can't answer "what do I owe right now?".

## The fix

One file at `docs/Dashboard/index.md` containing a markdown table. Each row is one **atomic user action** — a letter with three independent decisions emits three rows, not one. Any agent session appends rows when writing letters or handoffs. The user reads. Anyone observing completion marks done.

```
| ID     | Type | Action                                  | Where (detail)              | Blocker for         | Since      | Status |
|--------|------|-----------------------------------------|-----------------------------|---------------------|------------|--------|
| UN-001 | C    | Review + merge MR !49                   | gitlab MR !49               | follow-up L2 ship   | 2026-05-20 | open   |
| UN-005 | A    | Decide: adopt mypy?                     | toUser/lint-policy.md §4.9  | lint-policy-v2 L2   | 2026-05-19 | open   |
| UN-014 | E    | Force-burn `.worktrees/bisect-*`        | manual rm -rf               | disk hygiene        | 2026-05-25 | open   |
```

## Why a markdown file (and not Linear / Notion / Jira / Multica)

- **Same surface as the code.** Lives in git alongside the work; diffs in PRs; survives session reset; rebases cleanly.
- **AI sessions append in one line.** No API token, no schema migration, no rate limit.
- **Atomic-action granularity.** Tracker tools hold L2 work units. cc-dashboard holds the *user actions on those L2s* — different granularity, different lifecycle.
- **One file beats N files.** Sendbox letters fan out (one per recipient role); the dashboard collapses (one per repo). The user scans one table.

## What you get

- Canonical path: `docs/Dashboard/index.md` (single markdown file, two sections: Active + Archive)
- Row schema: `ID | Type | Action | Where (detail) | Blocker for | Since | Status`
- **Six action types** with distinct completion signals:
  - **A** Decision / Approve  ·  **B** Start session  ·  **C** Review / Merge
  - **D** Read + Triage       ·  **E** Destructive ops ·  **F** Ops / Admin
- Write triggers tied to sendbox letter creation, handoff creation, and external-blocker observation
- Four mark-done ownership options with default (*any session + user*)
- Fourteen-day rolling archive
- Clean coupling rules with [`cc-sendbox`](https://github.com/JasonJarvan/cc-sendbox)'s `sendbox-protocol` skill

Full spec: [`skills/cc-dashboard/SKILL.md`](skills/cc-dashboard/SKILL.md).

## Install (30 seconds)

```sh
git clone https://github.com/JasonJarvan/cc-dashboard.git
mkdir -p ~/.claude/skills
ln -s "$(pwd)/cc-dashboard/skills/cc-dashboard" ~/.claude/skills/cc-dashboard
```

Claude Code discovers it at next session start. Invoke via the `Skill` tool with name `cc-dashboard`.

## Adopt in a target repo

```sh
cd <target-repo>
mkdir -p docs/Dashboard
# Copy the template from SKILL.md §"File template" into docs/Dashboard/index.md
# Add a thin hook config under your harness conventions (path varies by recipe)
# Cross-link from CLAUDE.md / AGENTS.md "Where to look"
```

For HarnessStack-managed repos there is an embedding playbook tailored for factory agents: [`docs/sendbox/toHarnessFactory/from-dashboard-embedding-playbook.md`](docs/sendbox/toHarnessFactory/from-dashboard-embedding-playbook.md).

## When to use

Use when:

- Three or more active agent sessions accumulate user-blocking asks
- A single letter typically holds two or more atomic user decisions
- The user wears multiple roles (driver / courier / session-starter / reviewer) and switches frequently
- External trackers exist but they hold L2 work units, not user-action granularity
- Reachability test fails: the user needs four or more surfaces to answer "what do I owe right now?"

Don't use when:

- Single session, single user, chat-resolved tasks
- An external tracker provides personal-action granularity *and* the team uses it consistently

## Companion skill

[`cc-sendbox`](https://github.com/JasonJarvan/cc-sendbox) — defines the underlying letter protocol cc-dashboard projects from. Adopting cc-dashboard without sendbox-protocol works but loses the natural coupling at letter-creation triggers.

## Repository structure

```
cc-dashboard/
├── README.md                                   # you are here
├── LICENSE                                     # MIT
├── skills/
│   └── cc-dashboard/
│       └── SKILL.md                            # main artifact (~250 lines)
└── docs/
    └── sendbox/
        └── toHarnessFactory/
            └── from-dashboard-embedding-playbook.md
```

## Status

- **v0.1** — protocol distilled from the `everclaw` repository's HarnessStack hook into a portable skill.
- Per-repo adoption requires a thin hook config declaring language policy and mark-done owner — see SKILL.md §"Adopting in a new repo".

## Provenance

Distilled from a research-subagent proposal evaluating Linear / Multica / file-based options for managing multi-agent pending-user-action sprawl. Business-specific identifiers from the source project (EVE-NN issue keys, MR numbers, project-specific letter paths) intentionally absent — only the reusable pattern survives.

## License

MIT — see [`LICENSE`](LICENSE).
