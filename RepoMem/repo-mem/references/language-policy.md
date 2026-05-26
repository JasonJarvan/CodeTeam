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

## Audience-Based Language Choice (optional refinement)

The Primary/Secondary model above keeps a single source-of-truth language. Some projects want a finer split: model-facing docs in English (more compact, cross-team neutral), user-facing docs in the user's preferred language.

This optional refinement adds two configs:

- `userLanguage` (default: project primary language)
- `modelLanguage` (default: English)

When enabled:

- **HITL / user-facing docs** (the user reads in workflow): use `userLanguage`
- **Non-HITL / model-facing docs** (agents read; user does not touch in workflow): use `modelLanguage`

### Filename Suffix Convention

- `<name>.md` (no suffix) = English (default; matches modelLanguage)
- `<name>.{lang}.md` = non-English content (ISO 639-1: `.zh`, `.ja`, `.de`, …)

If `userLanguage ≠ English`, user-facing docs MUST carry the suffix.

### When to Enable

Enable when:

- the repo's human user reads in a non-English language
- the repo's docs split cleanly into agent-internal vs user-facing
- token efficiency / model-performance favors English for internal docs

Skip when:

- the team is fully native-speaker uniform (single-language is simpler)
- the repo is monolingual by policy

### Relationship to Primary/Secondary Model

These two models can coexist. A repo may:

- use Primary-only (current default)
- use Audience-based (this refinement)
- use both: primary as authoritative; `.{lang}.md` translations on user-facing docs

Configure in `persist/config.md`:

- `audience_split: enabled | disabled` (default `disabled` for backwards compat)
- `user_language: <lang code>`
- `model_language: <lang code>` (default `en`)

### Provenance

This refinement was proposed by the cc-sendbox project's language policy (see https://github.com/JasonJarvan/cc-sendbox `docs/sendbox/toAllAgents/from-sendbox-language-policy.md`) and accepted upstream into repo-mem's reference set on 2026-05-26 via HITL diff review.
