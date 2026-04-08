# Skill: INCOSE Requirements Rewriting

Load this file before rewriting or auditing any requirement file.

## Purpose

This skill provides a checklist and process for rewriting requirements to conform
with INCOSE Systems Engineering Handbook (SE HBK) quality criteria. Apply it
whenever creating a new requirement or reviewing an existing one.

## INCOSE quality criteria (SMART-V)

Every requirement must satisfy **all** of the following:

| Criterion    | Check |
|---|---|
| **Atomic**      | Contains exactly one "shall" statement expressing one discrete behaviour or constraint |
| **Unambiguous** | Has exactly one valid interpretation; uses no vague terms ("user-friendly", "appropriate", "as needed", "if possible", "etc.") |
| **Verifiable**  | Can be proven satisfied via Inspection, Analysis, Test, or Demonstration |
| **Traceable**   | Has a `derived_from` or `related_to` link, or explicitly documents why it has none |
| **Consistent**  | Does not conflict with any other requirement |
| **Complete**    | No TBD/TBC content; all conditions and quality attributes fully specified |
| **Feasible**    | Can be implemented within known technical and project constraints |
| **Necessary**   | Removing it would create a deficiency in the delivered system |

## Canonical frontmatter schema (INCOSE-extended)

```yaml
---
id: SYS-001                      # required — unique across the repo
title: "Short imperative title"  # required — max ~60 chars, imperative mood
type: Functional                 # required — see allowed values below
priority: High                   # required — Critical | High | Medium | Low
status: Draft                    # required — Draft | Approved | Deprecated
stability: Stable                # required — Volatile | Stable | Locked
verification: [Test]             # required — one or more of: Test | Analysis | Inspection | Demonstration
tags: [tag1, tag2]               # optional
relationships:
  derived_from: null             # ID of the single parent requirement, or null
  related_to: [SYS-002, SYS-003] # IDs of horizontally related requirements
---
```

### Type — allowed values

| Value       | When to use |
|---|---|
| Functional  | Describes what the system shall do |
| Performance | Quantifies how fast, accurate, or efficient the system must be |
| Interface   | Defines a boundary or protocol with an external system or actor |
| Constraint  | Restricts the solution space (safety, security, regulatory, architectural) |

### Priority — semantics

| Value    | Meaning |
|---|---|
| Critical | Cannot ship without this; non-negotiable |
| High     | Core feature; omit only in exceptional circumstances |
| Medium   | Important but deferrable without blocking the primary use case |
| Low      | Nice to have; can be deferred to a later release |

### Status — semantics

| Value      | Meaning |
|---|---|
| Draft      | Under development; may change |
| Approved   | Baselined; changes require a formal change request |
| Deprecated | Superseded or removed; kept for traceability only |

### Stability — semantics

| Value    | Meaning |
|---|---|
| Volatile | Expected to change as the design matures |
| Stable   | Unlikely to change without a stakeholder-driven reason |
| Locked   | Must not change without a formal review-board decision |

### Verification — selection guide

| Method        | Use when |
|---|---|
| Test          | Behaviour can be exercised by running the software with defined inputs and checking outputs |
| Inspection    | Compliance is determined by reading code, configuration, or output files |
| Analysis      | Compliance is established by calculation or modelling (e.g. performance bounds) |
| Demonstration | Compliance is shown by operating the system in a specified real-world mode |

## Rewrite process (step by step)

### Step 1 — Audit

Read the requirement file and count "shall" statements. If N > 1, the requirement
is compound and must be split.

### Step 2 — Split compound requirements

Create one file per "shall" statement. Assign new sequential IDs to the additional
statements within the same folder. Keep the existing ID for the first/primary statement.

### Step 3 — Write the shall statement

Use the canonical template:

```
The <subject> shall <verb> <object> [<qualifier>].
```

- **Subject**: the specific system component responsible (not "the system" in general)
- **Verb**: active voice, observable action (do, produce, display, accept, exit, write)
- **Object**: the thing acted upon
- **Qualifier**: conditions, quantitative limits, or constraints — only if they tighten the requirement

### Step 4 — Assign metadata

Set `priority`, `status`, `stability`, and `verification` using the tables above.
Set `status: Draft` for any new or rewritten requirement.

### Step 5 — Update relationships

Ensure `derived_from` and `related_to` reference the **new** IDs after any renumbering.
Group tightly related atomic requirements using `related_to`.

### Step 6 — Write acceptance criteria

Each criterion in `## Acceptance Criteria` must:

- Correspond directly to the chosen `verification` method
- Be independently verifiable (no compound criteria joined by "and")
- For **Test** requirements: be directly executable as a test case with explicit inputs and expected outputs
- For **Inspection** requirements: name the artefact to inspect and what to look for

## Anti-patterns to eliminate

| Anti-pattern | Example | Fix |
|---|---|---|
| Compound requirement | "The system shall do X and Y" | Split into two atomic requirements |
| Vague qualifier | "The system shall respond quickly" | Quantify: "shall respond within 200 ms" |
| Design prescription | "The system shall use a hash map to store X" | Remove the how; specify only the what |
| Escape clause | "The system shall, where possible, support X" | Either require it unconditionally or remove it |
| TBD content | "Format to be defined in a future requirement" | Define it, or keep the requirement as `status: Draft` with a cross-reference note |
| Passive voice | "Requirements shall be validated by the tool" | "The tool shall validate all requirements" |
| Implicit subject | "Shall discover all exporters at runtime" | "The CLI shall discover all exporters at runtime" |
| Bundled acceptance criteria | "Header is bold, blue, and frozen" (one criterion) | Keep as one criterion only if verified together; split if they can fail independently |

## File naming convention

```
<FOLDER>/<ID>-<slug>.md
```

- `<ID>`: uppercase folder key + zero-padded number, e.g. `ARCH-004`
- `<slug>`: 2–5 word kebab-case summary of the shall statement, e.g. `entry-point-registration`

**Example**: `ARCH-architecture/ARCH-004-immutable-requirements-directory.md`

## Body sections — required structure

Every requirement file must contain exactly these three Markdown sections, in order:

```markdown
## Description

The <subject> shall <verb> <object> [<qualifier>].

## Rationale

<Why this requirement exists. Reference any standards, stakeholder needs, or
failure modes that motivate it.>

## Acceptance Criteria

- <Criterion 1 — independently verifiable>
- <Criterion 2 — independently verifiable>
```