# Embedding playbook — sendbox-protocol into a HarnessStack repo

> Promoted from `cc-sendbox/docs/sendbox/toHarnessFactory/from-sendbox-embedding-playbook.md` on 2026-05-26. The original letter is on the sendbox-protocol `persist → promoted-then-burned` lifecycle; this is the durable form.

This playbook tells a HarnessFactory agent (1) whether the target repo needs sendbox, and (2) exactly what to do to embed it. It is HS-specific.

## 1. Prerequisite

Required pre-read (≤3 min): upstream `sendbox-protocol` self-description (`~/.claude/skills/sendbox-protocol/SKILL.md`). Everything below assumes you know what sendbox is.

Authoritative skill source: `~/.claude/skills/sendbox-protocol/SKILL.md`.

## 2. Decision tree — embed or skip?

Embed sendbox into the target HS repo when **both** dimensions hold:

### 2.1 Recipe / scale dimension

| Target recipe | Embed sendbox? |
|---|---|
| `superpowers` (no RepoMem) | Skip by default — single-session execution discipline; sendbox adds ceremony |
| `superpowers-repomem` (solo, platform/library) | Embed iff §2.2 also says yes (most solo platform repos do NOT need it) |
| `openspec-superpowers-repomem` (small-team product) | Embed by default — multi-task work commonly spawns subagents |
| `openspec-superpowers-repomem-ecc` (small-team product, hardened) | Embed by default |
| Any recipe extending a primary-workflow layer (BMAD / gstack / GSD) | Embed by default |

### 2.2 Work-mode dimension

Embed if **any** of these is plausible in the target repo's near-term work:

- A task may be dispatched to a **subagent in a different cwd / worktree / repo**
- The repo will run **multi-worktree parallel work** (orchestrator + ≥1 implementer)
- The repo will produce **A-12 stop-and-ask boundaries** that need durable record
- The repo communicates with another HS repo via a **cross-repo handoff** mechanism

If none, skip the embed even if §2.1 says embed-by-default. Re-evaluate when work mode changes.

### 2.3 Skip outcome

If skipping: do NOT create `docs/sendbox/`, do NOT touch `longterm.md`. Record the decision in the target repo's `version-plan[.{lang}].md` "future considerations" / "未来考虑" so a future factory pass can reconsider.

## 3. Embedding checklist (when §2 says embed)

### 3.1 Install the skill

```sh
ln -s /home/<user>/Codes/cc-sendbox/skills/sendbox-protocol ~/.claude/skills/sendbox-protocol
```

Verify: Claude Code recognizes `sendbox-protocol` in the skill list at next session start.

### 3.2 Add one cross-method invariant to target `longterm.md`

Paste the §5 template **verbatim** into the target's `docs/HarnessStack/longterm.md § Cross-Method Invariants`. Do NOT inline the skill body. Do NOT paraphrase the wording — the wording is part of the contract.

### 3.3 Pipeline ↔ sendbox trigger reference

Do not insert new pipeline steps. Sendbox is triggered by *conditions* that overlay existing steps:

| HS pipeline step | Condition that triggers a letter | Canonical letter type |
|---|---|---|
| Step 2 brainstorming (multi-session work) | Spawning a fresh recipient session | `handoff.md` to `to<Role>/` |
| Step 5 worktree + executing-plans | Implementer awaits orchestrator greenlight | `from-<sender>-plan-ready.md` |
| Step 5 (during implementation) | A-12 stop-and-ask hit | `from-<sender>-blocker-<topic>.md` |
| Step 7 verification | Vertical-slice acceptance gate hit | `from-<sender>-<milestone>-done.md` |
| Step 8 requesting-code-review | Orchestrator owes N decisions to one recipient | `from-<orche>-<recipient>-decisions.md` (bundled) |
| Step 9 finishing-a-development-branch | Branch close-out summary | `from-<sender>-archived.md` |
| Step 10 RepoMem.merge HITL | Promotion candidates from temp → persist | `from-<sender>-repomem-merge-promotes.md` |
| Any time | New constraint applies to all active sessions | `toAllActiveSessions/from-<orche>.md` (broadcast) |

This map is *reference*, not enforcement. Only write a letter when the Minimal Sendbox rule says you should.

### 3.4 Verification (factory side, before declaring embed done)

- Target's `CLAUDE.md` (if it has one) does NOT override or weaken the sendbox hard rules.
- Target's `docs/sendbox/` is NOT scaffolded yet — it appears the first time a letter is actually written.
- `~/.claude/skills/sendbox-protocol` is reachable from the target user's Claude Code env.
- The invariant text in §3.2 is verbatim, not paraphrased.

## 4. Anti-patterns

1. **Do not inline the skill body** into the target's `longterm.md`. Reference; do not duplicate.
2. **Do not scaffold `docs/sendbox/`** with empty subdirectories. Let it grow as letters are written.
3. **Do not embed into a `superpowers`-only recipe** unless §2.2 explicitly says so.
4. **Do not modify the skill** in the target repo. File an upstream issue against `cc-sendbox` instead.
5. **Do not write the invariant in your own words.** §5 wording is contract wording.

## 5. Copy-paste invariant template

Paste this **verbatim** into the target's `docs/HarnessStack/longterm.md § Cross-Method Invariants`:

```markdown
- **Multi-session work uses sendbox-protocol.** When a task involves multiple
  sessions, dispatched subagents, or cross-worktree coordination, the
  `sendbox-protocol` skill (see `~/.claude/skills/sendbox-protocol/SKILL.md`)
  is the canonical asynchronous channel. The main agent's `docs/sendbox/` is
  the single source of truth, and subagents in side cwds write to it by
  relative or absolute path — never fan out under their own cwd. See
  `methods/sendbox/embedding-playbook.md` for the embedding playbook.
```

If the target repo bundles a vendored copy of cc-sendbox, adjust only the path in the parenthetical reference; leave the rest unchanged.

## 6. Pointers

- Generic self-desc: upstream `sendbox-protocol` SKILL.md
- Profile: `profile.md` (this directory)
- GitHub: https://github.com/JasonJarvan/cc-sendbox
