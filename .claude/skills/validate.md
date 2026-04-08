# Skill: Validation Rules

Load this file before touching `reqm/validate.py`.

## Principles

- `validate()` is a pure function: `list[Requirement] → list[ValidationError]`
- No I/O, no side effects, no exceptions for expected error conditions
- Each rule is an independent function; `validate()` composes them

## Rule structure

```python
def _check_<rule_name>(requirements: list[Requirement]) -> list[ValidationError]:
    errors = []
    # ... check logic ...
    return errors

def validate(requirements: list[Requirement]) -> list[ValidationError]:
    errors = []
    errors += _check_required_fields(requirements)
    errors += _check_duplicate_ids(requirements)
    errors += _check_broken_links(requirements)
    errors += _check_enum_values(requirements)
    return errors
```

## Required rules (must all be implemented)

| Rule | Description |
| --- | --- |
| `required_fields` | id, title, type, verification must be present and non-empty |
| `duplicate_ids` | No two requirements share the same id |
| `broken_links` | All derived_from and related_to values resolve to existing ids |
| `enum_values` | type within allowed set; each verification value within allowed set |

## Adding a new rule

1. Add a `_check_<rule>()` function
2. Call it inside `validate()`
3. Add a test in `tests/test_validate.py`
4. Document it in `docs/validation.md`
