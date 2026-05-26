# Language Policy

## Primary Language

- Keep one repository primary language in `persist/config.md`.
- Use the primary language for:
  - persistent docs
  - temp docs
  - merge suggestions
  - maintenance proposals
  - HITL review items

## Secondary Languages

- Secondary languages are mirrors only.
- Store them under `multi-lang/<language>/`.
- Do not treat them as the primary fact source.
- Do not use them for normal temp-doc collaboration.

## Sync Policy

Use `translation_sync_policy` from `persist/config.md`.

V1 recommended value:

- `ask-after-persist-change`

That means:

- after important persistent-doc updates, ask whether to sync translations
- do not auto-translate by default
