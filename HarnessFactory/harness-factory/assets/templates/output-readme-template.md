# HarnessStack — {Repository} at {Scale}/{Horizon}

> One-time distillation source for an AI agent operating in the target
> repository. Read once, condense sections 1–4 into `CLAUDE.md`, then
> consult `longterm.md` for full detail. Re-read this file only on recipe
> upgrade.

## 1. Identity

This repository runs HarnessStack at `{scale}` scale, horizon `{horizon}`.

- **Active recipe:** `{recipe-slug}`
- **Source template:** `{source-template-path}`
- **Effective from:** {effective-from-date}

## 2. Active Methods

{render one bullet per active method from the recipe's layer set, with a one-line responsibility, e.g.:}

- `Superpowers` — execution discipline (TDD, brainstorming, writing-plans, verification, finishing-a-development-branch).
- `OpenSpec` — spec layer; one task uses one `change-id`.
- `RepoMem` — long-term repository memory (persist + temp split).
- `ECC(medium)` — harness enhancement (pre-commit hooks, session-state, security scan).

## 3. Per-Task Pipeline (Compressed)

> This is the compressed view. **It is not authoritative.** For the full
> step list, conflict rules, and exception handling, see
> `longterm.md § Pipeline`.

{render 7–10 condensed steps from the active recipe's Pipeline, e.g.:}

1. `RepoMem.read` — load relevant persist memory.
2. `brainstorming` — establish design and approval gate.
3. `OpenSpec.explore` + `OpenSpec.propose` — produce change set.
4. `writing-plans` — produce implementation plan.
5. Execute (TDD; `ECC.session-state.persist` continuous; `RepoMem.capture` continuous).
6. `pre-commit-eval` and `security-scan` (if dependencies changed).
7. Dual verification: `OpenSpec.verify` + `Superpowers.verification-before-completion`.
8. `requesting-code-review`.
9. `finishing-a-development-branch`.
10. `OpenSpec.archive` + `RepoMem.merge` (HITL).

## 4. Hard Invariants

- `<task>` = `change-id` = `<slug>` — one identifier across OpenSpec, RepoMem, and HarnessStack docs.
- **Add-only**: a method that has been activated never deactivates; upgrades are extensions, never replacements.
- **Dual-verification gate**: both `OpenSpec.verify` and `Superpowers.verification-before-completion` MUST pass before `finishing-a-development-branch`.
- Task-level documents do not duplicate content (see `longterm.md § Cross-Method Invariants`).

## 5. Where To Read More

- Full long-term contract: `./longterm.md`
- Full usage manual (Day-One Init, per-task iteration, long-term iteration): `./_toUser/README.md`
- Task-level patch (if a task is in progress): `./temporary-<task>.md`

## 6. For AI Consumers

Distill sections 1–4 into `CLAUDE.md` (or the equivalent always-loaded
instruction file in your harness). Do not duplicate `longterm.md` verbatim;
the contract remains the authoritative source for details. Re-read this
README only on recipe upgrade or full rewrite events.
