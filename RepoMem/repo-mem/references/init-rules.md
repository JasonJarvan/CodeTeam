# Init Rules

## New Repository Init

For a new repository or a repository that accepts standard RepoMem layout directly:

- generate the standard persistent skeleton
- create config, version-plan, architecture index, and memory index
- provide temp templates for later task work

## Existing Repository Init

For an existing repository, use a proposal-first flow:

1. Analyze the existing repository.
2. Generate `temp/<slug>/init-proposal.md`.
3. Let the user review and edit the proposal.
4. Apply the confirmed proposal.
5. Create missing persistent docs.
6. Only fill missing content in existing persistent docs.
7. If conflicts appear, generate `temp/<slug>/init-conflicts.md`.
8. Discuss each conflict by `conflict_id`.
9. Apply the confirmed conflict resolutions.
10. Show `git diff`.

## Init Proposal Structure

`init-proposal.md` must include:

- `Repository Summary`
- `Detected Documentation Sources`
- `Candidate Domains`
- `Suggested Persistent Layout`
- `Migration Suggestions`
- `Open Questions`
- `Recommended Next Step`

For any section that expects user answers, especially `Open Questions`, number each item as `1.`, `2.`, `3.` so the user can answer by id in conversation.

## Init Conflicts Structure

`init-conflicts.md` must include:

- `Summary`
- `Conflict Items`
- `Suggested Resolution Options`
- `Human Decisions`
- `Execution Notes`

Each conflict item must include a stable `conflict_id`.
When asking the user to resolve conflicts or open questions, prefer numbered items or stable ids for direct reply mapping.

Supported conflict-resolution paths currently include:

- `keep existing`
- `replace with proposed`
- `merge both`
- `rewrite manually`

## Safety Rules

- Do not overwrite existing persistent content blindly.
- Do not skip user review of `init-proposal.md`.
- Do not resolve conflicts automatically without confirmed guidance.
- Treat `rewrite manually` as a human-led path unless a later version adds a safe structured rewrite flow.
