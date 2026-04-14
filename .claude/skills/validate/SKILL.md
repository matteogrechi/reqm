---
name: validate
description: Guidelines and constraints for modifying reqm validation logic. Use when touching reqm/validate.py or adding, removing, or changing a validation rule.
---

# Validate Skill

Load this skill before touching `reqm/validate.py`.

## Guardrails

- **`validate()` is a pure function** — no I/O, no side effects, no exceptions for expected error conditions.
- **Each rule is an independent private function** — `validate()` only composes them.
- **`reqm validate` must exit non-zero** when any `ValidationError` is returned.
- Never combine multiple concerns into a single `_check_*` function.

## Workflow

### 1. Read the current state

Read `reqm/validate.py` and `reqm/models.py` to understand the existing contract and data shapes before making any changes.

### 2. Add the rule function

```python
def _check_<rule_name>(requirements: list[Requirement]) -> list[ValidationError]:
    errors = []
    # one concern only
    return errors
```

### 3. Compose into `validate()`

```python
def validate(requirements: list[Requirement]) -> list[ValidationError]:
    errors = []
    errors += _check_required_fields(requirements)
    errors += _check_duplicate_ids(requirements)
    errors += _check_broken_links(requirements)
    errors += _check_enum_values(requirements)
    errors += _check_<rule_name>(requirements)   # add here
    return errors
```

### 4. Test

Add cases in `tests/test_validate.py`:
- A requirement that triggers the error
- A valid requirement that does not trigger it

Run: `pytest tests/test_validate.py`

### 5. Document

Add the rule to `docs/validation.md`.

## Required rules (must all be present)

| Function | What it checks |
|---|---|
| `_check_required_fields` | `id`, `title`, `type`, `verification` present and non-empty |
| `_check_duplicate_ids` | No two requirements share the same `id` |
| `_check_broken_links` | All `derived_from` and `related_to` values resolve to existing ids |
| `_check_enum_values` | `type` and each `verification` value within their allowed sets |

## Done checklist

- [ ] New rule is a private `_check_<rule>()` function with one concern
- [ ] Called inside `validate()` with `errors +=`
- [ ] Tests added — both the failing and the passing case
- [ ] `pytest tests/test_validate.py` passes
- [ ] `reqm validate` exits non-zero on any error
- [ ] Rule documented in `docs/validation.md`
