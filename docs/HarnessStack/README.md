# HarnessStack — HarnessFactory at solo/long-lived

> One-time distillation source for an AI agent operating in this
> repository. Read once, condense sections 1–4 into `CLAUDE.md`, then
> consult `longterm.md` for full detail. Re-read this file only on recipe
> upgrade.

## 1. Identity

This repository runs HarnessStack at `solo` scale, horizon `long-lived`.

- **Active recipe:** `superpowers-repomem`
- **Source template:** `harness-factory/assets/templates/longterm/solo.md`
- **Effective from:** 2026-05-15

This is the **dogfood** instance: HarnessFactory runs the contract on
itself. Repository Type is `platform` (specifically: a HarnessFactory
skill / methodology repository — see `longterm.md § Current Long-Term
Assessment` for the note).

## 2. Active Methods

- `Superpowers` — execution discipline: brainstorming, writing-plans,
  using-git-worktrees, executing-plans, TDD, verification-before-completion,
  requesting-code-review, finishing-a-development-branch.
- `RepoMem` — long-term repository memory: persist + temp split, HITL
  merge from temporary to long-term.

Inactive layers (per the `superpowers-repomem` recipe; see `longterm.md`
for upgrade triggers): Primary Workflow, Spec, Harness Enhancement.

## 3. Per-Task Pipeline (Compressed)

> This is the compressed view. **It is not authoritative.** For the full
> step list, conflict rules, and exception handling, see
> `longterm.md § Pipeline`.

1. `RepoMem.read` — load long-term architecture and memory as task context.
2. `Superpowers.brainstorming` — clarify vague intent.
3. `RepoMem.capture` — open task-level temporary docs (requirement, architecture).
4. `Superpowers.writing-plans` — produce executable plan.
5. `Superpowers.using-git-worktrees` + `executing-plans` + TDD — implement.
6. `RepoMem.capture` (continuous) — record tacit knowledge into temporary memory.
7. `Superpowers.verification-before-completion` — verify behavior.
8. `Superpowers.requesting-code-review`.
9. `Superpowers.finishing-a-development-branch`.
10. `RepoMem.merge` (HITL) — promote stable knowledge from temporary to long-term.

## 4. Hard Invariants

- **Add-only**: methods never deactivate; recipe upgrades are extensions,
  not replacements (single-line `Recipe Reference` edit).
- **Verification gate**: `Superpowers.verification-before-completion`
  MUST pass before `requesting-code-review`.
- **Merge order**: `RepoMem.merge` runs after
  `Superpowers.finishing-a-development-branch`, never before, and is
  HITL — a human reviews promotion candidates.
- **Doc sedimentation**: temporary memory is authoritative during the
  task; long-term memory only accepts content via the HITL merge step.
  Plan vs memory: `writing-plans` defines HOW; RepoMem temporary docs
  record WHY/context — never duplicate plan steps into memory.

## 5. Where To Read More

- Full long-term contract: `./longterm.md`
- Full usage manual (Day-One Init, per-task iteration, long-term iteration): `./_toUser/README.md`
- Task-level patch (if a task is in progress): `./temporary-<task>.md`

## 6. For AI Consumers

Distill sections 1–4 into `CLAUDE.md` (or the equivalent always-loaded
instruction file in your harness). Do not duplicate `longterm.md`
verbatim; the contract remains the authoritative source for details.
Re-read this README only on recipe upgrade or full rewrite events.
