# File Layout

## Target Repository Standard Layout

When `repo-mem init` initializes a target repository, use:

```text
docs/RepoMem/
├── persist/
│   ├── config.md
│   ├── version-plan.md
│   ├── architecture/
│   │   ├── index.md
│   │   └── <domain>.md
│   └── memory/
│       ├── index.md
│       └── <domain>.md
├── temp/
│   ├── <slug>/
│   │   ├── requirements.md
│   │   ├── architecture.md
│   │   └── memory.md
│   │   ├── init-proposal.md
│   │   └── init-conflicts.md
│   └── <maintenance-slug>/
│       └── proposal.md
└── multi-lang/
    └── <language>/
```

Use `init-proposal.md` and `init-conflicts.md` only for existing-repository initialization flows.
Do not treat them as the normal task-memory trio.

## This Repository's Self-Hosted Layout

This repository uses RepoMem to manage RepoMem itself.
Keep self-hosted docs separate from the skill package:

```text
RepoMem/
├── repo-mem/
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   └── assets/templates/
└── docs/RepoMem/
    ├── persist/
    ├── temp/
    └── multi-lang/
```

## Separation Rules

- Treat `repo-mem/` as the reusable skill package.
- Treat `repo-mem/assets/templates/` as initialization sources for other repositories.
- Treat `docs/RepoMem/` as the self-hosted fact source for this repository.
- Do not treat `docs/RepoMem/` as the skill package itself.
- Runtime experience may inform the skill later, but only through explicit review and promotion.
