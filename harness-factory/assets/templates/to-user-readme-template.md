# Using HarnessStack — Human Operator Guide

> Human-facing manual for operating the HarnessStack activated at
> `docs/HarnessStack/` in this repository. For the authoritative contract,
> see `../longterm.md`. For the one-time AI distillation source, see
> `../README.md`.

## 1. What This Stack Activates

This repository activates the following workflow layers (see
`../longterm.md § Current Active Long-Term Baseline` for full detail):

{render one bullet per active method from the chosen recipe's layer set,
with a one-line operator-facing summary, e.g.:}

- `Superpowers` — execution-discipline skills: brainstorming, writing-plans, TDD, verification, finishing-a-development-branch.
- `RepoMem` — long-term repository memory; persists architecture, decisions, and tacit knowledge across tasks.

## 2. Day-One Init

Run these once when this stack is first activated in your repository:

1. Ensure the active methods are installed in your agent harness (Claude
   Code, Codex, or equivalent). Each method ships as a discoverable skill —
   install per its own README.
2. Distill `../README.md` sections 1–4 into your `CLAUDE.md` (or the
   equivalent always-loaded instruction file). Do not copy `longterm.md`
   verbatim — keep the contract as the source of truth, the always-loaded
   file as the condensed pointer.
3. {scenario-specific init steps from the recipe, e.g., create
   `docs/RepoMem/persist/` for RepoMem-enabled stacks, or `.openspec/changes/`
   for OpenSpec-enabled stacks.}
4. Read this manual end-to-end before starting your first task.

## 3. Per-Task Iteration Loop

For each task:

{render the condensed loop from the recipe's Pipeline + Execution Policy.
Below is the rendered form for `superpowers-repomem` as an example:}

1. **Read context.** Run `RepoMem.read` to load long-term memory.
2. **Clarify intent.** Run `Superpowers.brainstorming` unless the intent is
   already crystal clear.
3. **Open task docs.** Run `RepoMem.capture` to open
   `docs/RepoMem/temp/<task>/`.
4. **Plan.** Run `Superpowers.writing-plans` to produce an executable plan.
5. **Implement.** Use `git-worktrees` + TDD per the plan.
6. **Capture continuously.** Record tacit knowledge into temporary memory
   as you go.
7. **Verify.** Run `Superpowers.verification-before-completion`.
8. **Review.** Run `Superpowers.requesting-code-review`.
9. **Finish branch.** Run `Superpowers.finishing-a-development-branch`.
10. **Promote memory.** Run `RepoMem.merge` (HITL — a human reviews
    promotion candidates before they enter long-term memory).

If a task introduces constraints the long-term contract does not cover,
create a `temporary-<task>.md` patch per
`../longterm.md § Temporary Contractor Boundary Rules`.

## 4. Long-Term Iteration

`../longterm.md` is authoritative. Update it only when:

- a Full Rewrite Condition triggers (see
  `../longterm.md § Full Rewrite Conditions`), OR
- you switch to a superset recipe via the add-only principle — a single-line
  `Recipe Reference` change plus a `Last Updated Because` entry, NOT a
  rewrite.

Routine task work does NOT modify `longterm.md` directly — use
`temporary-<task>.md` for task-scoped adjustments.

## 5. Tracking HarnessStack Evolution (Optional)

If you want a version trail of how this stack evolves (recipe upgrades,
scenario changes, layer additions), maintain a version-plan document.
Recommended placements:

- **If your repository uses `RepoMem` (active in this stack):** place it at
  `docs/RepoMem/persist/version-plan.md`. The `repo-mem` skill maintains
  this naturally.
- **Otherwise:** any single file works — e.g.,
  `docs/HarnessStack/version-plan.md`.

HarnessFactory does not ship a version-plan skeleton inside the bundle.
Stack-evolution tracking is target-repo state, not factory output.

## 6. Pointers

- Authoritative contract: `../longterm.md`
- AI distillation source: `../README.md`
- Task-level patch (if active): `../temporary-<task>.md`
- Recipe binding: `../longterm.md § Document Meta § Recipe Reference`

## 7. Common Questions

**Q: I just want to run a quick experiment — do I still need the full loop?**

See `../longterm.md § Temporary Contractor Boundary Rules`. For `<3h test`
delivery targets, the temporary contract may skip heavier steps.

**Q: I want to add a new method (e.g., OpenSpec) — how?**

This is a recipe upgrade. Per the add-only principle, switch to a superset
recipe (e.g., `superpowers-repomem` → `openspec-superpowers-repomem`).
Single-line edit in `longterm.md § Document Meta § Recipe Reference`. The
previous file is preserved; the upgrade is an extension, not a replacement.

**Q: A task seems to violate the contract — what do I do?**

First check whether it's a temporary-contract case (see § 3 above). If the
contract itself is wrong, see `../longterm.md § Full Rewrite Conditions` to
decide whether a rewrite is justified. Do not silently rewrite the
contract.
