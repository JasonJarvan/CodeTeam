# Frontmatter

## Config

`persist/config.md` uses frontmatter for repository-memory configuration.

Required fields:

- `default_language`
- `secondary_languages`
- `translation_sync_policy`

## Temp Documents

All task-scoped temp docs use frontmatter.

Required in all temp docs:

- `slug`
- `status`
- `domains`
- `updated_at`

Required only in `requirements.md`:

- `task_type`

## Init Proposal Documents

`init-proposal.md` uses:

- `slug`
- `status`
- `updated_at`
- `task_type: init`

`init-conflicts.md` may use the same minimum fields when stored as a temp workflow artifact.

## Status Values

V1 uses:

- `active`
- `merged`

## Domains

- Select `domains` from the current domain map in `persist/architecture/index.md`.
- Allow multiple domains.
- Let the agent update `domains` silently as task scope evolves.

## Example

```yaml
---
slug: fix-login-timeout
status: active
domains:
  - auth
  - session-management
updated_at: 2026-04-03
task_type: bugfix
---
```
