# Validation

reqm validates requirements against four rules. All rules run on every invocation
of `reqm validate`.

## Rules

### 1. Required Fields (`_check_required_fields`)

Every requirement must have non-empty values for:

- `id`
- `title`
- `type`
- `verification` (list must contain at least one item)

### 2. Duplicate IDs (`_check_duplicate_ids`)

No two requirements may share the same `id`. One error is emitted per duplicated
id.

### 3. Broken Links (`_check_broken_links`)

All `derived_from` and `related_to` references must resolve to existing
requirement ids. Each unresolved reference generates a separate error.

### 4. Enum Values (`_check_enum_values`)

Field values must be from the allowed set:

- `type`: `Functional`, `Performance`, `Interface`, `Constraint`
- `verification` items: `Test`, `Analysis`, `Inspection`, `Demonstration`

## Usage

```sh
reqm validate                        # validates FUN-reqm-product-requirements/ (default)
reqm validate --root docs/           # validates a different directory
```

On success: prints `All requirements valid.` and exits 0.
On failure: prints each `[ID] message` error line and exits 1.
