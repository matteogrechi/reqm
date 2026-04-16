# Validation

reqm validates requirements against six rules on every invocation of
`reqm validate`. Two of these rules are conditional: ID format requires folder
metadata; the `validated_by` check requires linked validation items.

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

### 5. ID Format (`_check_id_format`)

When an `id` is declared in `.specification-metadata.md`, every requirement `id`
must match the pattern `<folder_id>-NNN` where `folder_id` is the `id` field of
the enclosing folder's `.folder-metadata.md` and `NNN` is exactly three digits.
Because folder IDs already embed the specification key (e.g. `REQM-ARCH`), the
full requirement ID is self-describing without repetition — for example
`REQM-ARCH-001`.

This rule is skipped when the specification `id` is empty.

### 6. Broken `validated_by` Links (`_check_broken_validated_by_links`)

All `validated_by` references must resolve to known validation item IDs. Each
unresolved reference generates a separate error.

This rule runs only when validation items are loaded (i.e. when the specification
has a `related_specifications` entry pointing to a `type: validation_items`
specification).

## Usage

```sh
reqm validate   # discovers the specification root by walking up from the current directory
```

The tool finds the specification root by walking upward from the current directory
until it finds a `.specification-metadata.md` file.

On success: prints `All requirements valid.` and exits 0.
On failure: prints each `[ID] message` error line and exits 1.
