---
name: feature
description: Workflow for handling feature requests and feature changes. Use whenever the user asks for a new feature or a change to an existing feature.
---

# Feature Skill

Load this skill before acting on any feature request or feature change.

## Guardrails

- **Never touch `FUN-reqm-product-requirements/` without explicit user confirmation** — requirements are the contract, not a scratch pad.
- **Never start implementing before the user confirms the plan** — show the requirement delta and implementation plan first.
- **No speculative scope** — only add requirements and code that directly address what the user asked for.
- **Requirements drive implementation** — if a feature has no requirement backing it, do not implement it.

## Workflow

### 1. Read the existing requirements

Glob every `.md` file under `FUN-reqm-product-requirements/` and read each one. Build a mental map of:

- Which requirement IDs already exist
- Which areas (CLI, ARCH, EXP, …) are relevant to the requested change
- Any requirement whose acceptance criteria overlaps with the requested feature

### 2. Check for collisions

For each requirement that could conflict with or be superseded by the request, note:

- The requirement ID and title
- The specific clause that collides
- Whether the requirement should be **updated**, **superseded**, or **left unchanged**

### 3. Draft the requirement delta

Produce the minimal set of changes to `FUN-reqm-product-requirements/`:

**New requirements** — create a new `.md` file following the project convention:

```
<AREA>-<NNN>-<slug>.md
```

Use the next available number in the relevant area folder. Fill every frontmatter field:

```yaml
---
id: <AREA>-<NNN>
title: <imperative-mood sentence>
type: Functional | NonFunctional | Interface | Process
priority: High | Medium | Low
status: Draft
stability: Volatile | Evolving | Stable
verification: [Test | Review | Inspection | Analysis | Demonstration]
tags: [...]
relationships:
  derived_from: null | [<IDs>]
  related_to: [<IDs>]
---
```

Include `## Description`, `## Rationale`, and `## Acceptance Criteria` sections.
Write to INCOSE standards (the `/incose-rewrite` skill has the full criteria).

**Updated requirements** — show the exact lines to change (old → new) for each affected file.

Do **not** write or edit any file yet.

### 4. Draft the implementation plan

Outline the code changes required, grouped by module, referencing file paths and
function names where known. Keep it brief — bullet points, no prose. Cover:

- Which modules change and why
- New functions or classes to add
- Tests to write
- Docs to update

### 5. Present to the user and wait

Show the user:

1. **Requirement delta** — list of new requirements (with IDs and one-line summaries)
   and updated requirements (ID + what changes).
2. **Implementation plan** — the outline from step 4.
3. A clear prompt: **"Confirm to proceed, or let me know what to adjust."**

Do **not** write any file until the user explicitly confirms.

### 6. Execute (only after confirmation)

Apply changes in this order:

1. Write or update requirement files in `FUN-reqm-product-requirements/`.
2. Implement code changes following the relevant module skill
   (`/exporter`, `/validate`, `/models`, etc.) if applicable.
3. Run `uv run pytest` — fix until green.
4. Run `uv run reqm validate FUN-reqm-product-requirements/` — fix until clean.
5. Update `docs/` to reflect the new state.

## Done checklist

- [ ] All existing requirements read before writing a single line
- [ ] Colliding requirements identified and disposition noted
- [ ] New/updated requirements written with complete frontmatter and all three body sections
- [ ] User confirmed the plan before any file was created or edited
- [ ] `uv run pytest` passes
- [ ] `uv run reqm validate FUN-reqm-product-requirements/` passes
- [ ] `docs/` updated if behaviour changed
