<div align="center">

# CodeTeam

### A multi-agent collaboration **System** for long-horizon coding tasks.

**Communication · Coordination · Memory · Activation — four composable layers, one umbrella.**

![Type](https://img.shields.io/badge/Type-System-111111?style=flat-square)
![Scope](https://img.shields.io/badge/Scope-Long--horizon%20Coding-0A7B83?style=flat-square)
![Composition](https://img.shields.io/badge/Composition-4%20Subtrees-8A5CF6?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-black?style=flat-square)

</div>

CodeTeam is the umbrella **System** for four independently maintained
components that, when used together, give a multi-agent setup what it
needs to survive long-horizon coding work:

- a way for sessions to **talk** asynchronously across worktrees and
  branches without trampling each other
- a single surface where a human can **see** what they owe right now,
  projected from that chatter
- a place where lessons, architecture, and plans **persist** beyond any
  one chat
- a **factory** that decides which of the above belong in a target
  repository and embeds them correctly

Each layer is independently useful. Each can be adopted alone. CodeTeam
exists to document how they compose and to keep their boundaries honest.

---

## Why a "System" and not a single skill

A single coding agent in a single session can be handled by a single
skill. Long-horizon work cannot:

- One orchestrator may spawn two or three implementer sessions across
  separate worktrees. Chat does not reach all of them.
- A user steering that fleet accumulates pending decisions faster than
  any one letter can capture. They need an inbox, not a thread.
- Architecture rationale and hard-won lessons must outlive every
  session that produced them, or they decay into folklore.
- Whether any of this discipline is even appropriate depends on the
  target repository — solo platform repos and small-team product repos
  have different needs.

No single skill addresses all four. CodeTeam frames them as four
**layers** of a system: each layer answers a different question, each
layer has its own canonical artifact, and each layer can be adopted
without the others.

---

## The four layers

```
┌─────────────────────────────────────────────────────────────────┐
│  HarnessFactory  ── activation / embedding factory              │
│  ─ decides which layers belong in a target repo and embeds them │
├─────────────────────────────────────────────────────────────────┤
│  RepoMem         ── persistent memory layer                     │
│  ─ architecture · memory · version-plan · task-scoped temp      │
├─────────────────────────────────────────────────────────────────┤
│  cc-dashboard    ── projection / pending-action board           │
│  ─ one markdown file = the human's inbox                        │
├─────────────────────────────────────────────────────────────────┤
│  cc-sendbox      ── asynchronous file-based communication       │
│  ─ letters between sessions: handoff, decision, blocker, …      │
└─────────────────────────────────────────────────────────────────┘
                            ▲
                            │
                  target development repository
```

| Layer | Component | Canonical artifact | Independent repo |
|---|---|---|---|
| Activation | **HarnessFactory** | contractor templates + embedding playbooks | [JasonJarvan/HarnessFactory](https://github.com/JasonJarvan/HarnessFactory) |
| Memory | **RepoMem** | `docs/RepoMem/{persist,temp}/…` + `repo-mem` skill | [JasonJarvan/RepoMem](https://github.com/JasonJarvan/RepoMem) |
| Coordination | **cc-dashboard** | `docs/Dashboard/index.md` + `cc-dashboard` skill | [JasonJarvan/cc-dashboard](https://github.com/JasonJarvan/cc-dashboard) |
| Communication | **cc-sendbox** | `docs/sendbox/to<Role>/*.md` + `sendbox-protocol` skill | [JasonJarvan/cc-sendbox](https://github.com/JasonJarvan/cc-sendbox) |

---

## How the layers collaborate

A typical long-horizon flow inside a repo that has adopted all four:

1. **HarnessFactory** decides, at repo bootstrap or upgrade time, which
   layers the target repo actually needs (a solo platform repo may skip
   `cc-dashboard`; a small-team product repo gets all four).
2. **Orchestrator agent** opens a task. It records architecture context
   and the plan into **RepoMem** (`temp/<task>/…`).
3. Orchestrator spawns implementer sessions in separate worktrees and
   writes a **cc-sendbox** `handoff.md` to each.
4. Whenever a letter contains an action the *human* owes (review a PR,
   approve a plan, run a destructive command), the writing agent also
   appends a row to **cc-dashboard**'s single markdown file.
5. Implementers write back via sendbox letters: `plan-ready`,
   `blocker`, `decisions`, `milestone-done`.
6. When the task ends, RepoMem's **merge** flow promotes the
   task-scoped temp memory into long-term `persist/architecture/` and
   `persist/memory/`, with HITL review.

The same flow degrades gracefully:

- Drop `cc-dashboard` if there is no human steering the fleet.
- Drop `cc-sendbox` if there is only one session.
- Drop `RepoMem` if the repo will not outlive the current task.
- Drop `HarnessFactory` if there is no fleet of target repos to
  manage and you are hand-rolling adoption.

Each component's README explains its own use cases and its own "do not
use" cases in detail.

---

## Repository layout

```
CodeTeam/
├── README.md                       # this file
├── LICENSE                         # MIT
├── docs/
│   └── sendbox/                    # consolidated inter-component letters
│       ├── README.md               # provenance + status under CodeTeam
│       ├── toAllAgents/
│       ├── toHarnessFactory/
│       ├── toRepomem/
│       └── toUser/
├── cc-sendbox/                     # subtree of JasonJarvan/cc-sendbox  (main)
├── cc-dashboard/                   # subtree of JasonJarvan/cc-dashboard (main)
├── RepoMem/                        # subtree of JasonJarvan/RepoMem      (main)
└── HarnessFactory/                 # subtree of JasonJarvan/HarnessFactory (master)
```

The four component directories are integrated via **`git subtree`** with
`--squash` — their contents are full file copies inside this repo, not
submodule pointers. `git clone https://github.com/JasonJarvan/CodeTeam`
yields everything in one shot; no `--recursive` needed.

### Upstream policy

The four component repositories are the **upstream of record**.
CodeTeam is an **integration view**: it pulls updates from upstream, it
does not normally originate component changes.

Iterate inside each component's own repository as before; then update
CodeTeam to pick up the change:

```bash
git subtree pull --prefix=cc-sendbox      https://github.com/JasonJarvan/cc-sendbox.git      main   --squash
git subtree pull --prefix=cc-dashboard    https://github.com/JasonJarvan/cc-dashboard.git    main   --squash
git subtree pull --prefix=RepoMem         https://github.com/JasonJarvan/RepoMem.git         main   --squash
git subtree pull --prefix=HarnessFactory  https://github.com/JasonJarvan/HarnessFactory.git  master --squash
```

If, for any reason, a change is made inside CodeTeam to a component
subtree first, push it back upstream so the two views stay in sync:

```bash
git subtree push --prefix=cc-sendbox https://github.com/JasonJarvan/cc-sendbox.git <branch>
```

---

## Adopting CodeTeam in a target repo

CodeTeam itself is a *reference assembly* of four independently
adoptable components. You do not adopt CodeTeam as a whole — you adopt
the components your target repo needs, in the order their layers imply:

1. Read `HarnessFactory/README.md` and let it tell you which recipe
   your target repo wants.
2. Embed **cc-sendbox** if multiple sessions or subagents will
   coordinate in the target.
3. Embed **cc-dashboard** if (and only if) cc-sendbox is embedded *and*
   `toUser/` letters are actively used.
4. Embed **RepoMem** if durable architecture/memory/plan separation is
   worth maintaining.

The embedding playbooks under
[`docs/sendbox/toHarnessFactory/`](docs/sendbox/toHarnessFactory/)
are the authoritative decision trees for the first three steps.

---

## License

MIT — see [`LICENSE`](LICENSE).

Each component subtree carries its own LICENSE inside its directory;
those licenses govern the component code and remain authoritative for
that component.
