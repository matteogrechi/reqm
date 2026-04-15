"""Validation logic for requirements collections."""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
from reqm.models import Requirement, ValidationItem

ALLOWED_TYPES = {"Functional", "Performance", "Interface", "Constraint"}
ALLOWED_VERIFICATION = {"Test", "Analysis", "Inspection", "Demonstration"}


@dataclass
class ValidationError:
    req_id: str
    message: str


def _check_required_fields(requirements: list[Requirement]) -> list[ValidationError]:
    """Ensure id, title, type, and verification are non-empty."""
    errors: list[ValidationError] = []
    for req in requirements:
        if not req.id:
            errors.append(ValidationError(req_id=req.id or "<missing>", message="Missing required field: id"))
        if not req.title:
            errors.append(ValidationError(req_id=req.id or "<missing>", message="Missing required field: title"))
        if not req.type:
            errors.append(ValidationError(req_id=req.id, message="Missing required field: type"))
        if not req.verification:
            errors.append(ValidationError(req_id=req.id, message="Missing required field: verification"))
    return errors


def _check_duplicate_ids(requirements: list[Requirement]) -> list[ValidationError]:
    """Emit one error per occurrence of each duplicated id."""
    errors: list[ValidationError] = []
    counts = Counter(r.id for r in requirements)
    seen: set[str] = set()
    for req in requirements:
        if counts[req.id] > 1 and req.id not in seen:
            seen.add(req.id)
            errors.append(
                ValidationError(req_id=req.id, message=f"Duplicate requirement id: {req.id}")
            )
    return errors


def _check_broken_links(requirements: list[Requirement]) -> list[ValidationError]:
    """Ensure derived_from and related_to entries resolve to known ids."""
    errors: list[ValidationError] = []
    known_ids = {r.id for r in requirements}
    for req in requirements:
        for parent_id in req.derived_from:
            if parent_id not in known_ids:
                errors.append(
                    ValidationError(req_id=req.id, message=f"Broken link: derived_from '{parent_id}' does not exist")
                )
        for ref in req.related_to:
            if ref not in known_ids:
                errors.append(
                    ValidationError(req_id=req.id, message=f"Broken link: related_to '{ref}' does not exist")
                )
    return errors


def _check_broken_validated_by_links(
    requirements: list[Requirement],
    items: list[ValidationItem],
) -> list[ValidationError]:
    """Ensure validated_by entries resolve to known validation item ids."""
    errors: list[ValidationError] = []
    known_ids = {item.id for item in items}
    for req in requirements:
        for item_id in req.validated_by:
            if item_id not in known_ids:
                errors.append(
                    ValidationError(
                        req_id=req.id,
                        message=f"Broken link: validated_by '{item_id}' does not exist",
                    )
                )
    return errors


def _check_unknown_keys(requirements: list[Requirement]) -> list[ValidationError]:
    """Emit an error for each unrecognised frontmatter key."""
    errors: list[ValidationError] = []
    for req in requirements:
        for key in req.extra:
            errors.append(ValidationError(req_id=req.id, message=f"Unknown frontmatter key: '{key}'"))
    return errors


def _check_enum_values(requirements: list[Requirement]) -> list[ValidationError]:
    """Validate that type and verification values are within allowed enumerations."""
    errors: list[ValidationError] = []
    for req in requirements:
        if req.type not in ALLOWED_TYPES:
            errors.append(
                ValidationError(req_id=req.id, message=f"Invalid type '{req.type}'; must be one of {sorted(ALLOWED_TYPES)}")
            )
        for v in req.verification:
            if v not in ALLOWED_VERIFICATION:
                errors.append(
                    ValidationError(req_id=req.id, message=f"Invalid verification '{v}'; must be one of {sorted(ALLOWED_VERIFICATION)}")
                )
    return errors


def validate(
    requirements: list[Requirement],
    items: list[ValidationItem] | None = None,
) -> list[ValidationError]:
    """Run all validation rules against the requirements collection.

    Rules applied:
    - Required fields present (id, title, type, verification)
    - No duplicate IDs
    - All derived_from and related_to references resolve to existing IDs
    - Type and verification values are within allowed enumerations
    - No unrecognised frontmatter keys
    - All validated_by IDs resolve to known validation items (only when items provided)

    Args:
        requirements: Full collection of parsed requirements.
        items: Loaded validation items; when None the validated_by check is skipped.

    Returns:
        List of validation errors; empty list means the collection is valid.
    """
    errors: list[ValidationError] = []
    errors.extend(_check_required_fields(requirements))
    errors.extend(_check_duplicate_ids(requirements))
    errors.extend(_check_broken_links(requirements))
    errors.extend(_check_enum_values(requirements))
    errors.extend(_check_unknown_keys(requirements))
    if items is not None:
        errors.extend(_check_broken_validated_by_links(requirements, items))
    return errors