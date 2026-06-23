# Changelog

All notable changes to `sendbox-protocol` (the skill in `skills/sendbox-protocol/SKILL.md`) are recorded here. Format follows [Keep a Changelog](https://keepachangelog.com/); versioning is [SemVer](https://semver.org/) (MAJOR.MINOR.PATCH) applied to the skill body.

**Versioning scope**: this changelog tracks the skill body only. Repository-level changes (docs reshuffles, RepoMem captures, sendbox dogfood, CI bits) are visible via `git log` and not duplicated here.

## [0.4.0] — 2026-06-22

### Added — optional two-layer directory grouping

`§ Directory layout` now documents an OPTIONAL audience grouping for sendboxes that outgrow a flat recipient set: `toHuman/to<role>/` (user + human teams) and `toAgent/to<role>/` (agent sessions, orchestrators, skills, frameworks, programs). Flat `to<Role>/` stays the default and remains valid; the grouping changes no other rule (naming, frontmatter, lifecycle identical). Codifies a host convention (EverClaw's) as a portable, opt-in scaling pattern.

### Why minor bump

Additive, backwards-compatible — flat layouts remain conformant; two-layer is opt-in. Per SemVer, additive = MINOR.

## [0.3.0] — 2026-06-18

### Added — active verbs (handoff / inherit)

The handoff/inherit practice gains two callable, framework-agnostic verbs, documented in a new `verbs.md` referenced from `SKILL.md`:

- **handoff (write)**: scaffolds a compliant handoff letter from the current session — detects Mode A/B, fills frontmatter, injects the host-configured `read_first` set, lays the mode skeleton, drafts substantive sections from session context (non-derivable parts left as `<FILL>`), adds a suggested-skills block (skills to invoke), and fills the env block from git.
- **inherit (read)**: actively loads a handoff letter's `read_first` + must-read set into context, applies a hard/soft dependency split (missing hard fails loudly; soft degrades), renders Day-1 as a checklist, and stays read-only (mutating steps proposed, never auto-run).

Verbs are framework-agnostic: all host-specific data (mandatory `read_first` paths, suggested skills, Mode-B Day-1 template) is read from a host config (`docs/sendbox/_handoff-config.yaml`), never hardcoded in the skill.

Also reconciled the `read_first` documentation into the SKILL.md frontmatter spec (previously absent from this repo copy) and widened the skill description to fire on handoff/inherit natural-language intents.

### Why minor bump

Additive new capability (the verbs) layered over the existing handoff letter type; backwards-compatible — existing letters and the spec remain valid. Per SemVer, additive semantic = MINOR.

## [0.2.1] — 2026-05-16

### Added — cleanup checkpoints

Two explicit checkpoint moments codified for actively executing lifecycle dispositions (was implicit in anti-pattern #5; now prescriptive):

- **Checkpoint 1 — at session end**: scan sendbox for letters you authored or addressed; execute disposition (burn / archive / persist) for any letter whose lifecycle has triggered
- **Checkpoint 2 — at task convergence**: sweep matched letter pairs (handoff + milestone-done; blocker + decisions; plan-ready + greenlight; superseded broadcast). Prevents half-completed conversation clutter.

Plus exemption clarification: `persist` letters skip the checkpoint sweep — they are reference docs that live in sendbox dir but do not rot.

### Why patch bump

Makes implicit intent (anti-pattern #5 reactive audit) explicit and prescriptive (proactive sweep). Existing letter / lifecycle semantics unchanged; this is operational discipline, not new mechanics.

## [0.2.0] — 2026-05-16

### Added — handoff modes (child vs inheritance)

The `handoff.md` letter type now formally has two semantic modes, dictated by the lifecycle relationship between the spawning session (parent) and the spawned session.

- **Mode A (child-handoff)**: parent persists; new session is a bounded subordinate that converges back. Required content: subtask scope, minimum inputs, convergence path, parent cwd (if cross-cwd), out-of-scope statement. Forbidden: full project context dumps.
- **Mode B (inheritance-handoff)**: parent terminates; new session takes ownership. Required: identity statement, full status snapshot, must-read list, pending decisions, active relationships, env state. Forbidden: convergence path back to (now-defunct) parent.
- **Mode C (peer dialogue)**: not a handoff — use normal letter types between coexisting sessions.

Declared in letter body via `> mode: child` or `> mode: inheritance` quote block; filename stays `handoff.md`.

Mode detection rule added (two-question check; both must agree).

### Why minor bump

This is the first SKILL.md body change that introduces a semantic distinction agents must observe. Backwards-compatible (existing handoff letters remain valid; the modes are an explicit categorization of what was already implicit). Per SemVer: additive semantic = MINOR.

### Test coverage

- `tests/outsider-scenarios/06-handoff-modes.md` (4 scenarios, child / inheritance / peer-rejection / minimum-scope-child)
- Cumulative fixture scenarios: 27

### RepoMem capture

- `docs/RepoMem/persist/memory/handoff-modes.md` — durable lesson on the two-mode split, why it matters, failure modes observed in cc-sendbox / EverClaw practice

## [0.1.0] — 2026-05-16

Initial release. The skill distills 4 days of multi-agent EverClaw practice (11+ agents, 22+ letter types, 8 sendbox directories) into a portable, framework-agnostic convention.

### Added — core protocol

- Directory layout: `docs/sendbox/to<Role>/` with role-not-session naming
- Letter naming: `handoff.md` for entries, `from-<sender>-<topic>.md` for replies, ASCII lowercase-kebab
- YAML frontmatter spec for multi-recipient letters (`recipients[]`, `on_lifecycle_end`, `created`, `created_in`)
- 10 canonical letter types catalog (handoff, plan-ready, greenlight, blocker, decisions, milestone-done, archived, promote-to-durable, broadcast, toUser)
- 5 communication patterns including A-12 stop-and-ask
- 7 anti-patterns from real-world misuse
- Lifecycle dispositions: burn / archive / persist
- 6-step Quick Start

### Added — main-agent + canonical sendbox semantics (RED→GREEN patch 1)

User-identified gaps after baseline self-test:
- "main agent" was never defined — sessions had no clear holder of the canonical sendbox
- Cross-cwd write rules only covered same-repo `.worktrees/` and said nothing about subagents dispatched to a different repo or `/tmp`

Closed by:
- **Core Principle #0** — one canonical `docs/sendbox/` per project, held by the main agent (cwd = project root). Sendboxes do not fan out.
- **Cross-cwd write** section (renamed from Cross-worktree write) with 3-case table: same-repo worktree / different repo or `/tmp` / same-cwd peer
- Hard rules: never create parallel `docs/sendbox/` under a side cwd; never dual-write; if unreachable, surface to user rather than write a shadow
- Quick start step 1: explicit "pick the main agent's project root first"
- Red flags: detect `docs/sendbox/` under a subagent's cwd as misuse symptom

Verified: fresh outsider subagent answered 3 cross-cwd scenarios + bonus definition correctly with explicit rule citations.

### Added — minimal-sendbox reachability rule (RED→GREEN patch 2 sub-A)

User-identified gap in baseline:
- Minimal-sendbox rule did not distinguish "worktree session replying upstream" from "orchestrator relaying a substantive directive to a detached implementer". Outsider gave inconsistent answers (one wrote a letter, one did not, both with similar reasoning).

Closed by:
- **Reachability test** in "When to use" — detached recipient → sendbox is delivery, not redundancy
- **Anti-pattern #1 scope clause** — rule targets worktree session replying upstream; does NOT exempt orchestrator relaying to a detached implementer

Verified: re-test outsider got 4/4 on rule-clarification questions with explicit rule citations.

### Added — framework-agnostic Interop section (RED→GREEN patch 2 sub-B)

User principle: SKILL.md is for skill callers (any framework). HarnessStack-specific embedding mechanics belong outside the skill.

Closed by:
- §Interop rewritten with framework-agnostic terms: "pipeline-style workflows with verification gates / HITL approvals" (was "17-step pipeline"), "spec systems" (was "OpenSpec"), "long-term knowledge stores" (was "auto-memory")
- Letter type `from-<x>-repomem-merge-promotes.md` renamed to `from-<x>-promote-to-durable.md` (RepoMem was a framework leak)
- §Interop ends with pointer convention: framework-specific playbooks live at `docs/sendbox/to<Framework>Factory/`, not in the skill body

Verified: `grep -E 'HarnessStack|OpenSpec|ECC|RepoMem|repomem|17-step|auto-memory'` on SKILL.md returns zero matches.

### Added — secondary surface (framework-targeted, ships alongside skill)

These are not part of the skill body but ship with cc-sendbox:
- `docs/sendbox/toAgent/toAllAgents/from-sendbox-self-desc.md` — generic self-description for agent readers
- `docs/sendbox/toAgent/toHarnessFactory/from-sendbox-embedding-playbook.md` — HS-specific embedding playbook with decision tree, embed checklist, pipeline↔letter trigger map, copy-paste invariant template
- `docs/RepoMem/persist/architecture/sendbox-in-harnessstack.md` — durable architectural decision (positioning as cross-method invariant + customer-routing principle)
- `docs/HarnessStack/longterm.md § Cross-Method Invariants` — one-line invariant in cc-sendbox's own HS contract

### Repository

- `superpowers-repomem` recipe, solo / platform / long-lived
- LICENSE: MIT
- GitHub: https://github.com/JasonJarvan/cc-sendbox

[0.1.0]: https://github.com/JasonJarvan/cc-sendbox/releases/tag/v0.1.0
