# OpenTeam sendbox — consolidated archive

This directory consolidates inter-component letters that were originally
authored inside each component's own `docs/sendbox/` while the four
components evolved independently.

When OpenTeam was assembled as the umbrella **System** for these four
components, the letters were copied here verbatim (no rewrites) so that
the cross-component design rationale stays discoverable from a single
location.

## Provenance

| Letter | Original location | Author component |
|---|---|---|
| `toAllAgents/from-sendbox-language-policy.md`           | `cc-sendbox/docs/sendbox/toAllAgents/`        | cc-sendbox |
| `toAllAgents/from-sendbox-self-desc.md`                 | `cc-sendbox/docs/sendbox/toAllAgents/`        | cc-sendbox |
| `toHarnessFactory/from-sendbox-embedding-playbook.md`   | `cc-sendbox/docs/sendbox/toHarnessFactory/`   | cc-sendbox |
| `toHarnessFactory/from-dashboard-embedding-playbook.md` | `cc-dashboard/docs/sendbox/toHarnessFactory/` | cc-dashboard |
| `toRepomem/from-sendbox-language-policy-suggestion.md`  | `cc-sendbox/docs/sendbox/toRepomem/`          | cc-sendbox |
| `toUser/from-v02-handoff.zh.md`                         | `cc-sendbox/docs/sendbox/toUser/`             | cc-sendbox |
| `toUser/glossary.md`                                    | `cc-sendbox/docs/sendbox/toUser/`             | cc-sendbox |

## Status of these letters under OpenTeam

These letters predate OpenTeam. Now that the four components live under
one umbrella, the "embedding playbooks" addressed to HarnessFactory and
the "language policy" suggestions addressed to RepoMem describe internal
component contracts rather than cross-repo correspondence. They remain
authoritative for that internal contract; see the OpenTeam top-level
`README.md` for how the components interact at the system level.

The components' own `docs/sendbox/` directories under each subtree
(`cc-sendbox/docs/sendbox/`, `cc-dashboard/docs/sendbox/`) still hold the
originals — kept in place because each component remains an independent
upstream repository.
