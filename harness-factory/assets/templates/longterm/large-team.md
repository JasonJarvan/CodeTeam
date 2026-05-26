# longterm-large-team.md Template

## Document Meta

- Repository:
- Effective From:
- Source Template:
  - `harness-factory/assets/templates/longterm/large-team.md`
- Recipe Reference:
  - pick a large-team recipe under `harness-factory/assets/templates/recipes/`;
    a Primary Workflow framework (BMAD or GSD) MUST be active
- Last Updated Because:

## Current Long-Term Assessment

- Collaboration Scale:
  - `large-team`
- Repository Type:
  - `product | research | platform | other`
- Project Horizon:
  - `short-lived | long-lived`
- Long-Term Knowledge Governance:
  - `enabled`

## Current Active Long-Term Baseline

### 1. Primary Workflow Layer

- Default enabled:
  - `GSD` or `BMAD`
- Emergent Ownership:
  - Not applicable — a Primary framework is mandatory at this scale.
- Default inactive:
  - none by default
- Upgrade trigger:
  - coordination overhead requires stronger roadmap and planning structure

### 2. Spec Layer

- Default enabled:
  - `OpenSpec`
- Default inactive:
  - none by default
- Upgrade trigger:
  - require stricter enforcement when multiple concurrent changes interact

### 3. Execution Discipline Layer

- Default enabled:
  - `Superpowers`
- Default inactive:
  - none by default
- Upgrade trigger:
  - enforce stronger plan execution, review, and verification across contributors

### 4. Repository Memory Layer

- Default enabled:
  - `RepoMem`
- Default inactive:
  - none by default
- Upgrade trigger:
  - expand architecture and memory decomposition as repository domains multiply

### 5. Harness Enhancement Layer

- Default enabled:
  - `ECC(strong)`
- Default inactive:
  - none by default
- Upgrade trigger:
  - increase safety, eval, and orchestration rigor for high-stakes delivery

## Pipeline

- Pull from the chosen large-team recipe. The Primary framework drives the
  outer loop; OpenSpec/Superpowers/RepoMem run within each change.

## Cross-Layer Conflicts

- Pull from the chosen recipe. Notable additions at this scale: Primary
  framework planning vs OpenSpec proposal; Primary review gates vs Superpowers
  requesting-code-review.

## Verification Topology

- Primary framework's release-gate verification runs at the top.
- OpenSpec.verify and Superpowers.verification-before-completion run per
  change.

## Merge Gates

- RepoMem.merge runs after OpenSpec.archive. RepoMem.merge is HITL.
- Primary framework's release gates may add additional HITL points.

## Suitability Envelope

### Fits

- 6+ contributors
- multi-quarter roadmap
- strong governance and audit needs

### Does Not Fit

- short-lived prototypes
- single-contributor work

## Temporary Contractor Boundary Rules

### Temporary Contractor May Adjust

- raise or lower task-level intensity within the already active stack
- choose different temporary flow by clarity and delivery target
- narrow or widen verification intensity for the current task

### Temporary Contractor May Not Override

- the existence of `OpenSpec`, `RepoMem`, `Superpowers`, or `ECC` as the baseline
- long-term governance, audit, and safety expectations
- this document's collaboration-scale assumption without full rewrite

## Full Rewrite Conditions

- collaboration scale materially drops
- primary workflow needs to switch permanently between heavier planning systems
- governance intensity materially changes across the repository

## Related Documents

- `docs/HarnessStack/temporary-<task>.md`
- `docs/RepoMem/persist/version-plan.md`
