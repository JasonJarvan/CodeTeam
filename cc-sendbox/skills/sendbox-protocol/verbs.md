# Sendbox Verb Procedures

Callable procedures for the two implicit sendbox actions: **handoff** (write) and **inherit** (read). Both are invoked by natural-language intent matched against the `sendbox-protocol` skill description. Both procedures execute the spec defined in `SKILL.md` — they do not re-implement it. References below (e.g. "see SKILL.md 'YAML frontmatter'") point at the canonical spec sections.

## Host config

Both verbs read an optional host config file to supply framework-specific values. Default path: `docs/sendbox/_handoff-config.yaml` (relative to the project root). If absent, the verbs proceed with protocol-generic output and emit a warning on each host-specific field.

### Schema (embed verbatim in your host config)

```yaml
# docs/sendbox/_handoff-config.yaml
#
# Host config for sendbox-protocol handoff/inherit verbs.
# All fields are optional; absent fields fall back to protocol-generic behavior.

read_first:
  hard:                        # missing → inherit fails loudly
    - <absolute path>          # e.g. /home/you/project/docs/longterm.md
  soft:                        # missing → inherit degrades with warning
    - <absolute path>          # e.g. /home/you/project/docs/CONTEXT-MAP.md

suggested_skills:              # skills the recipient should invoke (not just read)
  - <skill-name>               # e.g. repo-mem, cc-dashboard

must_read_extra:               # additional paths beyond read_first that inherit loads
  - <absolute path>

day1_template_mode_b: |        # freeform Day-1 checklist template for Mode B inheritors
  - [ ] Step one
  - [ ] Step two
```

The config file itself is located by a relative path (`docs/sendbox/_handoff-config.yaml` relative to the project root); the values within it (`read_first.hard`, `read_first.soft`, `must_read_extra`) are absolute paths to the files the verb reads.

Fields:
- `read_first.hard` — absolute paths that are mandatory prerequisites; inherit fails loudly if any are missing or unreadable.
- `read_first.soft` — absolute paths that are recommended; inherit degrades gracefully (warning, not failure) if missing.
- `suggested_skills` — skill names the recipient should actively invoke as part of onboarding (addresses the "read the recipe but don't run the discipline" gap).
- `must_read_extra` — additional absolute paths to load into context beyond `read_first`; host-defined extended reading set.
- `day1_template_mode_b` — freeform multiline template rendered as the Day-1 checklist for Mode B inheritance handoffs.

---

## handoff — write a compliant handoff letter

**Purpose:** scaffold a filled handoff letter from the current session's state, writing it directly to `docs/sendbox/to<Role>/handoff.md`. The deliverable is the file; the author edits it in place.

### Inputs

- **Role** — the recipient role (e.g. `Impler`, `Orchestrator`, `CliTeam`). Prompt if not supplied.
- **Purpose / next-session goal** — infer from session context; ask one clarifying line only when genuinely ambiguous.
- **Host config** — loaded from `docs/sendbox/_handoff-config.yaml`; absent → warn and proceed.

### Procedure

**Step 1 — Mode detection**

Determine Mode A or Mode B (see SKILL.md "Handoff modes — child vs inheritance"):
- Ask: does the spawning session continue to live after this handoff?
  - Yes → **Mode A** (child; parent persists, child converges back)
  - No → **Mode B** (inheritance; parent ends, full ownership transfer)
- Ask: does the new session need to report back?
  - Yes → Mode A; No → Mode B
- When ambiguous, ask one clarifying question before proceeding.

**Step 2 — Write the file**

Write directly to `docs/sendbox/to<Role>/handoff.md`. Output a one-line confirmation (e.g. "Written to docs/sendbox/to<Role>/handoff.md") and stop — do not reproduce the file content in chat. The author edits the file in place.

**Step 3 — Scaffold frontmatter**

Use YAML frontmatter (see SKILL.md "YAML frontmatter"):

```yaml
---
recipients:
  - role: <Role>
    purpose: <why this session reads this letter>
    lifecycle: <concrete condition — a milestone, "until superseded by <filename>", etc.>
on_lifecycle_end: burn | archive | persist
created: <YYYY-MM-DD>
created_in: <human-readable origin tag, e.g. "orche-session-2026-06-18">
read_first:
  hard:
    - <absolute path>     # from host config read_first.hard; <FILL> if config absent
  soft:
    - <absolute path>     # from host config read_first.soft; <FILL> if config absent
---
```

- Inject `read_first` from host config. If host config is absent, write `<FILL: hard read_first paths>` and `<FILL: soft read_first paths>` with a warning comment.
- `on_lifecycle_end`: Mode A → `burn`; Mode B → `persist` (until inheritor's first milestone-done, then burn).

**Step 4 — Lay the mode skeleton and draft substantive sections**

Use the skeleton for the detected mode (see SKILL.md "Skeletons"). Draft every section from session context where derivable. Leave non-derivable parts as explicit `<FILL>` — do not hallucinate or guess.

Mode A skeleton:
> Opening frontmatter/quote-block → START GATE or TL;DR → problem/context → scope + out-of-scope → design/approach (if planning-heavy) → coordination / shared files → conventions / pipeline → sendbox cadence (if multi-phase) → lifecycle (burn condition) → convergence path → signature

Mode B skeleton:
> YAML frontmatter → mode + session identity table → what prior shipped / state → pending USER decisions → Must-read → active relationships → hard rules → env / cleanup state → Day-1 checklist → transition note + signature

**Step 5 — Suggested-skills block**

After `read_first`, add a `suggested_skills:` block listing the skills the recipient should *invoke* (not merely read about). Source from host config `suggested_skills`; if absent, omit the block and warn.

```
> suggested_skills: repo-mem, cc-dashboard   # invoke these, don't just read about them
```

**Step 6 — Fill the env block from git**

Query and populate:
- trunk HEAD commit hash and message
- current branch
- worktree status (clean / dirty; uncommitted files if any)

**Step 7 — Reference artifacts by absolute path**

When citing existing docs, specs, or letters, use absolute paths. Do not restate content that already exists at a known path — link it. Absolute paths are load-bearing for worktree-isolated recipients (see SKILL.md "YAML frontmatter" for the rationale).

**Step 8 — Redaction reminder**

Add one line at the end of the letter body: `<!-- These letters are committed to git; redact credentials, tokens, and PII before saving. -->`

**Step 9 — Remind author to confirm lifecycle and burn condition**

After writing, output one line to the author: "Review the lifecycle / burn condition in the frontmatter; confirm it is a concrete evaluable condition before finalizing."

### Completion criteria (checkable)

- [ ] File exists at `docs/sendbox/to<Role>/handoff.md` with valid YAML frontmatter.
- [ ] `read_first.hard` and `read_first.soft` are populated from host config (or contain `<FILL>` placeholders with warning if config absent).
- [ ] Mode is explicitly declared in the letter (quote block `> mode: child` or `> mode: inheritance`).
- [ ] Mode skeleton is present and all derivable sections are drafted from session context.
- [ ] Every non-derivable field is `<FILL>`, not guessed or hallucinated.
- [ ] `on_lifecycle_end` matches the mode: `burn` (Mode A) or `persist` (Mode B).
- [ ] Env block (branch, HEAD, worktree status) is filled from git.
- [ ] All artifact references use absolute paths.
- [ ] Redaction reminder line is present.
- [ ] Author received the lifecycle-confirmation reminder.

---

## inherit — actively load a handoff letter

**Purpose:** consume a handoff letter: load its required reading set into context and render an executable Day-1 checklist. Read-only — mutating steps are proposals, never auto-executed.

### Inputs

- **Letter path or role** — a given path; or locate the newest `handoff.md` under `docs/sendbox/to<Role>/`. Role identity is supplied by the invoker or read from the letter's identity section.
- **Host config** — loaded from `docs/sendbox/_handoff-config.yaml`; absent → warn and proceed.

### Procedure

**Step 1 — Locate the letter**

If a path is given, use it. Otherwise find the most recently modified `handoff.md` under `docs/sendbox/to<Role>/`. If no letter is found, fail with: "No handoff.md found for role <Role>; supply a path or confirm the letter exists."

**Step 2 — Parse frontmatter**

Read and parse the YAML frontmatter (see SKILL.md "YAML frontmatter"). Extract `recipients`, `read_first`, `on_lifecycle_end`, `created_in`. Identify the mode from the letter body (`> mode: child` or `> mode: inheritance`). Surface `created_in` in the inherited-identity statement (Step 5) so the inheritor sees letter provenance.

**Step 3 — Load read_first into context (hard/soft split)**

Apply the hard/soft split using host config `read_first` (or the letter's own frontmatter `read_first` if config is absent):

- **Hard dependencies**: for each path in `read_first.hard`, read the file into context. If a file is missing or unreadable: **fail loudly** — "Hard read_first dependency missing: `<path>`. Cannot proceed until this file is accessible. Check the path and retry."
- **Soft dependencies**: for each path in `read_first.soft`, attempt to read into context. If missing: **degrade gracefully** — "Soft read_first dependency missing: `<path>`. Proceeding without it; onboarding may be incomplete."
- Also load every path in host config `must_read_extra` (soft; degrade on missing).

Active loading is the core value: reading the file list into context closes the "read the recipe" gap; silent skips re-open it.

**Step 4 — Read remaining letter content**

Read the full letter body: identity statement, status snapshot, must-read list, pending decisions, active relationships, env/tool state.

**Step 5 — Render Day-1 checklist**

For Mode B (inheritance):
- Use host config `day1_template_mode_b` if present; otherwise derive a generic checklist from the letter's Day-1 section.
- State the inherited identity explicitly, including provenance from `created_in`: "You are <Role>, inheriting <parent>'s responsibility for <scope> (handoff written in <created_in>)."
- State the persist-until-first-milestone rule: "This handoff letter persists until you log your first milestone-done letter; that milestone implicitly ratifies the transfer. Burn this letter at that point."

For Mode A (child):
- Render the task scope, success criteria, convergence path, and out-of-scope statement as an actionable checklist.

**Step 6 — Present updated picture without re-asking resolved questions**

Read the status snapshot and pending-decisions sections. Do not re-ask questions the letter marks as resolved or decided. Present the current state as given; flag only genuinely open questions.

**Step 7 — List mutating Day-1 steps as proposals**

Any Day-1 step that mutates shared state (`git pull`, burn a superseded letter, `git rm`) is listed as a proposal, not auto-executed. For destructive shared-branch actions (burning a letter, force operations), require explicit user confirmation before executing.

### Completion criteria (checkable)

- [ ] Letter located and confirmed to exist at the stated path.
- [ ] Frontmatter parsed; mode identified (A or B) from letter body.
- [ ] Every hard `read_first` dependency is loaded into context; any missing hard dep caused a loud failure (not a silent skip).
- [ ] Every soft `read_first` dependency was attempted; missing ones produced a warning (not a silent skip).
- [ ] `must_read_extra` paths (from host config) were attempted; missing ones produced a warning.
- [ ] Day-1 checklist rendered from host template (Mode B) or letter content (Mode A).
- [ ] Mode B: inherited identity stated (includes `created_in` provenance); persist-until-first-milestone rule stated.
- [ ] Mode A: rendered checklist includes the convergence path (where to write back when done / when blocked) and the out-of-scope statement (what the child must NOT do).
- [ ] No resolved questions re-asked; open questions flagged clearly.
- [ ] Mutating Day-1 steps listed as proposals only; destructive shared-branch actions not auto-executed.
