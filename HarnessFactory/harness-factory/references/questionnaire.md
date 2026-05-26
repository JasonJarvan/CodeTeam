# HarnessStack Questionnaire

## Purpose

Use this questionnaire to collect only the information needed to generate or update:

- `docs/HarnessStack/longterm.md`
- `docs/HarnessStack/temporary-<task>.md`

Ask the minimum number of questions needed to determine the correct output.

## Q0. Entry Mode

- Has the user already pre-fixed one or more layer choices (Primary, Spec,
  Execution, Memory, Harness)?

If yes, switch to Layer-First flow per
`references/question-flow.md`. List the fixed layers and try to match an
existing recipe under `assets/templates/recipes/` before asking further
questions.

If no, continue with Scenario-First flow below.

## Long-Term Questions

Ask these only when:

- `docs/HarnessStack/longterm.md` does not exist, or
- there is reason to believe the long-term baseline may need a full rewrite

### Q1. Collaboration Scale

- How many active contributors does this repository have?

Normalize to:

- `solo`
- `small-team`
- `large-team`

### Q2. Repository Type

- Is this repository mainly a product, research, or platform repository?

Normalize to:

- `product`
- `research`
- `platform`
- `other`

### Q3. Project Horizon

- Is this repository expected to be short-lived or long-lived?

Normalize to:

- `short-lived`
- `long-lived`

### Q4. Long-Term Knowledge Governance

- Does this repository need persistent architecture, memory, and version-plan governance?

Normalize to:

- `enabled`
- `disabled`

## Temporary Task Questions

Ask these for the current task.

### Q1. Task Name

- What is the shortest stable name for this task?

Use this to name `temporary-<task>.md`.

### Q2. Requirement Clarity

- Is the requirement already clear, partially clear, or still vague?

Normalize to:

- `clear`
- `partially-clear`
- `vague`

### Q3. Delivery Target

- What is the expected delivery target?

Normalize to:

- `<3h test`
- `PoC`
- `Demo`
- `MVP`
- `Alpha`
- `Beta`
- `MMP`
- `RC`
- `GA`

### Q4. Risk Level

- Is the task low, medium, or high risk?

Normalize to:

- `low`
- `medium`
- `high`

### Q5. Long-Term Knowledge Impact

- Will this task likely produce knowledge that should persist beyond the task?

Normalize to:

- `none`
- `low`
- `medium`
- `high`

## Question Minimization Rules

- If the repository already has a stable `longterm.md`, skip long-term questions unless rewrite conditions are triggered.
- If the task is obviously tiny and low risk, do not over-ask.
- If repository context already answers a question, do not ask it again.
- Prefer normalization into the predefined values above.
