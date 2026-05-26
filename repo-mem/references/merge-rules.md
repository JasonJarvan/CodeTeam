# Merge Rules

## Merge

- Run `merge` only when a requirement or bugfix task has reached closure.
- Before writing, produce a structured suggestion list:
  - `to architecture`
  - `to memory`
  - `do not merge`
- Each suggestion should identify:
  - target persistent file
  - content category
  - short reason
  - source temp file when useful
- Require HITL confirmation before writing.
- After writing:
  - update temp-doc status to `merged` only for files that actually merged
  - update merge-target metadata in those temp docs
  - show post-write `git diff`
  - remind the user they can edit docs directly

## Prune

- Keep `prune` HITL-first.
- Produce a maintenance proposal instead of directly deleting large sections.
- Let the proposal classify changes such as:
  - remove
  - rewrite
  - already encoded in code
- Let the user either:
  - edit persistent docs directly
  - revise the proposal and ask the agent to apply it

## Split

- Keep `split` HITL-first.
- Produce a maintenance proposal instead of automatically restructuring large sections.
- Do not automatically invent new domains.
- Reuse existing domains when possible.
- If a new domain seems necessary, suggest it explicitly for human review.

## Proposal Structure

Maintenance `proposal.md` files must include:

- `Summary`
- `Why This Maintenance Is Needed`
- `Scope`
- `Suggested Changes`
- `Human Review Paths`
- `Execution Notes`
