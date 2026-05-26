# HarnessStack — HarnessFactory at solo/long-lived

> One-time distillation source for an AI agent operating in the target
> repository. Read once, condense sections 1–4 into `CLAUDE.md`, then
> consult `longterm.md` for full detail. Re-read this file only on recipe
> upgrade.

## 1. Identity

This repository runs HarnessStack at `solo` scale, horizon `long-lived`.

- **Active recipe:** `superpowers-repomem`
- **Source template:** `harness-factory/assets/templates/longterm/solo.md`
- **Effective from:** 2026-05-13

## 2. Active Methods

- `Superpowers` — execution discipline; brainstorming and writing-plans also carry the emergent primary-workflow responsibility (no separate Primary layer active).
- `RepoMem` — long-term repository memory (persist + temporary split, HITL merge into long-term).
- Inactive by default: `OpenSpec` (spec layer), `ECC` / `ECC(light)` (harness enhancement), `BMAD` / `gstack` / `GSD` (primary workflow frameworks).

## 3. Per-Task Pipeline (Compressed)

> This is the compressed view. **It is not authoritative.** For the full
> step list, conflict rules, and exception handling, see
> `longterm.md § Pipeline`.

1. `RepoMem.read` — load long-term architecture and memory as task context.
2. `Superpowers.brainstorming` — clarify vague intent.
3. `RepoMem.capture` — open task-level temporary docs (requirement, architecture).
4. `Superpowers.writing-plans` — produce executable plan.
5. Execute — `using-git-worktrees` + `executing-plans` + TDD; `RepoMem.capture` continuous.
6. `Superpowers.verification-before-completion` — single verification entry.
7. `Superpowers.requesting-code-review`.
8. `Superpowers.finishing-a-development-branch`.
9. `RepoMem.merge` (HITL) — promote stable knowledge from temporary to long-term.
10. `RepoMem.prune / split` — periodic hygiene, not per-task.

## 4. Hard Invariants

- **Add-only**: a method that has been activated never deactivates; upgrades are extensions, never replacements (e.g., `superpowers-repomem` → `openspec-superpowers-repomem` is a single-line `Recipe Reference` update, not a rewrite).
- **Single verification gate**: `Superpowers.verification-before-completion` MUST pass before `finishing-a-development-branch`. RepoMem has no verification role and never gates completion.
- **Merge ordering**: `RepoMem.merge` runs strictly AFTER `finishing-a-development-branch`, never before, and is always HITL.
- **`<task>` = `<slug>`**: one identifier across RepoMem temporary docs and any HarnessStack temporary contract for the same task.
- **No content duplication across task-level documents**: writing-plans owns HOW; RepoMem temporary memory owns WHY/context. See `longterm.md § Cross-Layer Conflicts`.

## 5. Where To Read More

- Full long-term contract: `./longterm.md`
- Task-level patch (if a task is in progress): `./temporary-<task>.md`

## 6. For AI Consumers

Distill sections 1–4 into `CLAUDE.md` (or the equivalent always-loaded
instruction file in your harness). Do not duplicate `longterm.md` verbatim;
the contract remains the authoritative source for details. Re-read this
README only on recipe upgrade or full rewrite events.
