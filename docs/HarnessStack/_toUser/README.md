# Using HarnessStack — Human Operator Guide

> Human-facing manual for operating the HarnessStack activated at
> `docs/HarnessStack/` in this repository (HarnessFactory dogfood
> instance). For the authoritative contract, see `../longterm.md`. For
> the one-time AI distillation source, see `../README.md`.

## 1. What This Stack Activates

This repository activates the following workflow layers (see
`../longterm.md § Current Active Long-Term Baseline` for full detail):

- `Superpowers` — execution-discipline skills: brainstorming,
  writing-plans, using-git-worktrees, executing-plans, TDD,
  verification-before-completion, requesting-code-review,
  finishing-a-development-branch.
- `RepoMem` — long-term repository memory; persists architecture,
  decisions, and tacit knowledge across tasks (HITL merge from
  temporary to long-term).

Inactive layers: Primary Workflow, Spec, Harness Enhancement (see
`../longterm.md` for the upgrade triggers that would activate them).

## 2. Day-One Init

Run these once when activating this stack:

1. Ensure `superpowers` and `repo-mem` skills are installed in your
   agent harness (Claude Code, Codex, or equivalent). Each ships as a
   discoverable skill — install per its own README.
2. Distill `../README.md` sections 1–4 into your `CLAUDE.md` (or the
   equivalent always-loaded instruction file). Do not copy `longterm.md`
   verbatim — keep the contract as the source of truth and the
   always-loaded file as the condensed pointer.
3. Ensure `docs/RepoMem/persist/` exists with at least a `MEMORY.md`
   index and a `version-plan.md`. The `repo-mem` skill manages these.
4. Read this manual end-to-end before starting your first task.

## 3. Per-Task Iteration Loop

For each task:

1. **Read context.** Run `RepoMem.read` to load long-term memory
   relevant to the task.
2. **Clarify intent.** Run `Superpowers.brainstorming` unless the intent
   is already crystal clear and the task is trivial.
3. **Open task docs.** Run `RepoMem.capture` to open
   `docs/RepoMem/temp/<task>/` for requirement notes and architecture
   sketches.
4. **Plan.** Run `Superpowers.writing-plans` to produce an executable
   plan. Skip for single-step tasks or `<3h test` delivery targets.
5. **Implement.** Use `Superpowers.using-git-worktrees` for isolation
   when needed, plus `executing-plans` and TDD per the plan.
6. **Capture continuously.** Record tacit knowledge — WHY, ruled-out
   approaches, conversation context — into temporary memory as you go.
   The plan records HOW; memory records WHY. Never duplicate.
7. **Verify.** Run `Superpowers.verification-before-completion`. This
   is non-negotiable — behavior must be verified before review.
8. **Review.** Run `Superpowers.requesting-code-review` (ask-first —
   confirm before triggering external visibility).
9. **Finish branch.** Run `Superpowers.finishing-a-development-branch`
   (ask-first — confirm scope before executing).
10. **Promote memory.** Run `RepoMem.merge` (HITL — a human reviews
    promotion candidates before they enter long-term memory). Runs
    AFTER step 9, never before.

If a task introduces constraints the long-term contract does not cover,
create a `temporary-<task>.md` patch per
`../longterm.md § Temporary Contractor Boundary Rules`.

## 4. Long-Term Iteration

`../longterm.md` is authoritative. Update it only when:

- a Full Rewrite Condition triggers (see
  `../longterm.md § Full Rewrite Conditions`), OR
- you switch to a superset recipe via the add-only principle — a
  single-line `Recipe Reference` edit plus a `Last Updated Because`
  entry, NOT a rewrite.

Routine task work does NOT modify `longterm.md` directly — use
`temporary-<task>.md` for task-scoped adjustments.

For HarnessFactory's own stack evolution (this dogfood instance), the
version trail lives in `docs/RepoMem/persist/version-plan.md`. The
factory iterates on itself by adding entries there as it ships new
versions.

## 5. Tracking HarnessStack Evolution

This repository uses `RepoMem`, so version-plan tracking lives at
`docs/RepoMem/persist/version-plan.md` (managed by the `repo-mem`
skill). New stack-level decisions (recipe upgrades, scenario changes,
layer additions) are recorded there.

HarnessFactory does not ship a version-plan skeleton inside the bundle.
Stack-evolution tracking is target-repo state, not factory output. For
target repos that do NOT use RepoMem, any single file (e.g.,
`docs/HarnessStack/version-plan.md`) works.

## 6. Pointers

- Authoritative contract: `../longterm.md`
- AI distillation source: `../README.md`
- Task-level patch (if active): `../temporary-<task>.md`
- Recipe binding: `../longterm.md § Document Meta § Recipe Reference`
- Factory-internal version trail: `../../RepoMem/persist/version-plan.md`

## 7. Common Questions

**Q: I just want to run a quick experiment — do I still need the full loop?**

See `../longterm.md § Temporary Contractor Boundary Rules`. For
`<3h test` delivery targets, the temporary contract may skip
`RepoMem.capture`, brainstorming, and writing-plans. Verification stays
non-negotiable.

**Q: I want to add a new method (e.g., OpenSpec) — how?**

This is a recipe upgrade. Per the add-only principle, switch to a
superset recipe (e.g., `superpowers-repomem` →
`openspec-superpowers-repomem`). Single-line edit in
`longterm.md § Document Meta § Recipe Reference` plus a
`Last Updated Because` entry. The previous file is preserved; the
upgrade is an extension, not a replacement.

**Q: A task seems to violate the contract — what do I do?**

First check whether it's a temporary-contract case (see § 3 above). If
the contract itself is wrong, see
`../longterm.md § Full Rewrite Conditions` to decide whether a rewrite
is justified. Do NOT silently rewrite the contract.

**Q: I'm operating HarnessFactory itself — does anything special apply?**

This is the dogfood instance. The factory iterates by modifying files
under `harness-factory/` (templates, references, SKILL.md), not by
modifying this `docs/HarnessStack/` directory. The flow is:
factory change → version-plan entry → re-render the dogfood bundle
when relevant. Treat `docs/HarnessStack/` as the activated contract,
not the source of factory logic.
