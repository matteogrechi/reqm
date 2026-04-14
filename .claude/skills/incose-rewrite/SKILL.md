---
name: incose-rewrite
description: Process and criteria for writing or rewriting requirements to INCOSE SE HBK standards. Use when creating a new requirement file, rewriting an existing one, or auditing a requirement for quality.
---

# INCOSE Rewrite Skill

Load this skill before creating, rewriting, or auditing any requirement file.

## Guardrails

- **Never touch files inside `FUN-reqm-product-requirements/`** — that directory is read-only.
- **One "shall" statement per file** — compound requirements must be split.
- **No TBD or TBC content** in an `Approved` requirement — mark it `Draft` instead.
- **Every new or rewritten requirement must include** `priority`, `status`, and `stability`.

## Workflow

### Step 1 — Audit

Read the requirement file. Count "shall" statements. If N > 1 → go to Step 2.

### Step 2 — Split compound requirements

Create one file per "shall" statement. Keep the existing ID for the primary statement;
assign new sequential IDs for the additional ones within the same folder.

### Step 3 — Write the shall statement

```
The <subject> shall <verb> <object> [<qualifier>].
```

- **Subject** — the specific component responsible, not "the system" in general
- **Verb** — active voice, observable action: do, produce, display, accept, exit, write
- **Object** — the thing acted upon
- **Qualifier** — only add if it meaningfully tightens the requirement

### Step 4 — Assign metadata

Set `priority`, `status`, `stability`, and `verification` using the tables below.
Always set `status: Draft` for any new or rewritten requirement.

### Step 5 — Update relationships

Update `derived_from` and `related_to` to reference the correct IDs after any renumbering.

### Step 6 — Write acceptance criteria

Each criterion in `## Acceptance Criteria` must:
- Correspond directly to the chosen `verification` method
- Be independently verifiable (no compound criteria joined by "and")
- For **Test**: explicit inputs and expected outputs
- For **Inspection**: name the artefact to inspect and what to look for

## Canonical frontmatter schema

```yaml
---
id: SYS-001                      # required — unique across the repo
title: "Short imperative title"  # required — max ~60 chars, imperative mood
type: Functional                 # required — see Type table below
priority: High                   # required — Critical | High | Medium | Low
status: Draft                    # required — Draft | Approved | Deprecated
stability: Stable                # required — Volatile | Stable | Locked
verification: [Test]             # required — one or more: Test | Analysis | Inspection | Demonstration
tags: [tag1, tag2]               # optional
relationships:
  derived_from: [SYS-000]        # one or more parent requirement IDs
  related_to: [SYS-002, SYS-003] # IDs of horizontally related requirements
  validated_by: [TEST-001]       # linked test case IDs
---
```

## Reference tables

### Type

| Value | When to use |
|---|---|
| Functional | Describes what the system shall do |
| Performance | Quantifies speed, accuracy, or efficiency |
| Interface | Defines a boundary or protocol with an external actor |
| Constraint | Restricts the solution space (safety, security, regulatory, architectural) |

### Priority

| Value | Meaning |
|---|---|
| Critical | Cannot ship without this; non-negotiable |
| High | Core feature; omit only in exceptional circumstances |
| Medium | Important but deferrable without blocking the primary use case |
| Low | Nice to have; can be deferred to a later release |

### Status

| Value | Meaning |
|---|---|
| Draft | Under development; may change |
| Approved | Baselined; changes require a formal change request |
| Deprecated | Superseded or removed; kept for traceability only |

### Stability

| Value | Meaning |
|---|---|
| Volatile | Expected to change as the design matures |
| Stable | Unlikely to change without a stakeholder-driven reason |
| Locked | Must not change without a formal review-board decision |

### Verification method selection

| Method | Use when |
|---|---|
| Test | Behaviour can be exercised with defined inputs and checked outputs |
| Inspection | Compliance is determined by reading code, config, or output files |
| Analysis | Compliance is established by calculation or modelling |
| Demonstration | Compliance is shown by operating the system in a real-world mode |

## Required file structure

Every requirement file must contain exactly these three sections, in order:

```markdown
## Description

The <subject> shall <verb> <object> [<qualifier>].

## Rationale

<Why this requirement exists. Reference standards, stakeholder needs, or failure modes.>

## Acceptance Criteria

- <Criterion 1 — independently verifiable>
- <Criterion 2 — independently verifiable>
```

## File naming convention

```
<FOLDER>/<ID>-<slug>.md
```

- `<ID>`: uppercase folder key + zero-padded number, e.g. `ARCH-004`
- `<slug>`: 2–5 word kebab-case summary, e.g. `entry-point-registration`

Example: `ARCH-architecture/ARCH-004-immutable-requirements-directory.md`

## INCOSE quality criteria (SMART-V)

| Criterion | Check |
|---|---|
| **Atomic** | Exactly one "shall" statement expressing one discrete behaviour |
| **Unambiguous** | Exactly one valid interpretation; no vague terms ("user-friendly", "as needed", "if possible") |
| **Verifiable** | Can be proven satisfied via Inspection, Analysis, Test, or Demonstration |
| **Traceable** | Has a `derived_from` or `related_to` link, or documents why it has none |
| **Consistent** | Does not conflict with any other requirement |
| **Complete** | No TBD/TBC; all conditions and quality attributes fully specified |
| **Feasible** | Implementable within known constraints |
| **Necessary** | Removing it would create a deficiency in the delivered system |

## Anti-patterns to eliminate

| Anti-pattern | Example | Fix |
|---|---|---|
| Compound requirement | "The system shall do X and Y" | Split into two atomic requirements |
| Vague qualifier | "shall respond quickly" | Quantify: "shall respond within 200 ms" |
| Design prescription | "shall use a hash map to store X" | Specify only the what, not the how |
| Escape clause | "shall, where possible, support X" | Require unconditionally or remove |
| TBD content | "Format TBD" | Define it, or keep `status: Draft` with a cross-reference note |
| Passive voice | "Requirements shall be validated by the tool" | "The tool shall validate all requirements" |
| Implicit subject | "Shall discover all exporters at runtime" | "The CLI shall discover all exporters at runtime" |

## Done checklist

- [ ] Exactly one "shall" statement per file
- [ ] All eight SMART-V criteria satisfied
- [ ] All required frontmatter fields set (`id`, `title`, `type`, `priority`, `status`, `stability`, `verification`)
- [ ] `status: Draft` on any new or rewritten requirement
- [ ] `derived_from` / `related_to` IDs are valid and up to date
- [ ] Exactly three body sections present: Description, Rationale, Acceptance Criteria
- [ ] Each acceptance criterion is independently verifiable
- [ ] File named `<ID>-<slug>.md` in the correct folder
