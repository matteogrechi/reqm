"""Tests for reqm.validate — each rule + end-to-end."""
from reqm.validate import (
    ValidationError,
    _check_required_fields,
    _check_duplicate_ids,
    _check_broken_links,
    _check_broken_validated_by_links,
    _check_enum_values,
    _check_id_format,
    validate,
)
from reqm.models import Requirement, FolderMeta, ValidationItem
from pathlib import Path


def _req(**kwargs):
    """Helper to create a minimal Requirement."""
    data = {
        "path": Path("/tmp/x.md"),
        "id": "X",
        "title": "Test",
        "type": "Functional",
        "verification": ["Test"],
    }
    data.update(kwargs)
    return Requirement(**data)


def _item(**kwargs):
    """Helper to create a minimal ValidationItem."""
    data = {
        "path": Path("/tmp/tc.md"),
        "id": "TC-001",
        "title": "Test item",
    }
    data.update(kwargs)
    return ValidationItem(**data)


def test_required_fields_all_present():
    req = _req()
    errors = _check_required_fields([req])
    assert errors == []


def test_required_fields_missing_id():
    req = _req(id="", title="Test", type="Functional", verification=["Test"])
    errors = _check_required_fields([req])
    assert any("id" in e.message for e in errors)


def test_required_fields_missing_title():
    req = _req(title="")
    errors = _check_required_fields([req])
    assert any("title" in e.message for e in errors)


def test_required_fields_missing_type():
    req = _req(type="")
    errors = _check_required_fields([req])
    assert any("type" in e.message for e in errors)


def test_required_fields_missing_verification():
    req = _req(verification=[])
    errors = _check_required_fields([req])
    assert any("verification" in e.message for e in errors)


def test_duplicate_ids():
    reqs = [_req(id="DUP"), _req(id="DUP"), _req(id="OK")]
    errors = _check_duplicate_ids(reqs)
    assert len(errors) == 1
    assert "DUP" in errors[0].message


def test_no_duplicate_ids():
    reqs = [_req(id="A"), _req(id="B"), _req(id="C")]
    errors = _check_duplicate_ids(reqs)
    assert errors == []


def test_broken_links_derived_from():
    reqs = [_req(id="A", derived_from=["NONEXISTENT"])]
    errors = _check_broken_links(reqs)
    assert any("derived_from" in e.message for e in errors)


def test_broken_links_related_to():
    reqs = [_req(id="A", related_to=["NONEXISTENT"])]
    errors = _check_broken_links(reqs)
    assert any("related_to" in e.message for e in errors)


def test_broken_links_valid():
    reqs = [
        _req(id="A"),
        _req(id="B", derived_from=["A"], related_to=["A"]),
    ]
    errors = _check_broken_links(reqs)
    assert errors == []


def test_enum_values_invalid_type():
    reqs = [_req(type="InvalidType")]
    errors = _check_enum_values(reqs)
    assert any("Invalid type" in e.message for e in errors)


def test_enum_values_invalid_verification():
    reqs = [_req(verification=["Magic"])]
    errors = _check_enum_values(reqs)
    assert any("Invalid verification" in e.message for e in errors)


def test_enum_values_all_valid():
    reqs = [
        _req(id="A", type="Functional", verification=["Test"]),
        _req(id="B", type="Performance", verification=["Analysis"]),
        _req(id="C", type="Interface", verification=["Inspection"]),
        _req(id="D", type="Constraint", verification=["Demonstration"]),
    ]
    errors = _check_enum_values(reqs)
    assert errors == []



def test_validate_end_to_end_valid():
    reqs = [
        _req(id="A"),
        _req(id="B", derived_from=["A"]),
    ]
    errors = validate(reqs)
    assert errors == []


def test_validate_end_to_end_with_errors():
    reqs = [
        _req(id="", title=""),
        _req(id="X", type="BadType", verification=[]),
    ]
    errors = validate(reqs)
    assert len(errors) > 0


def test_broken_validated_by_links_detected():
    reqs = [_req(id="A", validated_by=["TC-999"])]
    items: list[ValidationItem] = []
    errors = _check_broken_validated_by_links(reqs, items)
    assert any("validated_by" in e.message for e in errors)
    assert any("TC-999" in e.message for e in errors)


def test_broken_validated_by_links_valid():
    reqs = [_req(id="A", validated_by=["TC-001"])]
    items = [_item(id="TC-001")]
    errors = _check_broken_validated_by_links(reqs, items)
    assert errors == []


def test_validate_skips_validated_by_when_items_none():
    """validated_by check is skipped when items=None (no validation root configured)."""
    reqs = [_req(id="A", validated_by=["NONEXISTENT"])]
    errors = validate(reqs)  # items defaults to None
    assert errors == []


def test_validate_checks_validated_by_when_items_provided():
    reqs = [_req(id="A", validated_by=["NONEXISTENT"])]
    errors = validate(reqs, items=[])
    assert any("validated_by" in e.message for e in errors)


# ---------------------------------------------------------------------------
# _check_id_format
# ---------------------------------------------------------------------------

def _folder(folder_id: str, path: str) -> FolderMeta:
    """Helper to create a minimal FolderMeta."""
    return FolderMeta(path=Path(path), id=folder_id, title="")


def test_id_format_valid():
    folder = _folder("REQM-FUN", "/spec/REQM-FUN-folder")
    req = _req(id="REQM-FUN-001", path=Path("/spec/REQM-FUN-folder/req.md"))
    errors = _check_id_format([req], [folder])
    assert errors == []


def test_id_format_missing_spec_key():
    folder = _folder("REQM-FUN", "/spec/REQM-FUN-folder")
    req = _req(id="FUN-001", path=Path("/spec/REQM-FUN-folder/req.md"))
    errors = _check_id_format([req], [folder])
    assert len(errors) == 1
    assert "FUN-001" in errors[0].message


def test_id_format_wrong_folder_key():
    folder = _folder("REQM-FUN", "/spec/REQM-FUN-folder")
    req = _req(id="REQM-CLI-001", path=Path("/spec/REQM-FUN-folder/req.md"))
    errors = _check_id_format([req], [folder])
    assert len(errors) == 1


def test_id_format_non_three_digit_number():
    folder = _folder("REQM-FUN", "/spec/REQM-FUN-folder")
    req = _req(id="REQM-FUN-1", path=Path("/spec/REQM-FUN-folder/req.md"))
    errors = _check_id_format([req], [folder])
    assert len(errors) == 1


def test_id_format_skipped_when_no_folders():
    req = _req(id="anything", path=Path("/spec/REQM-FUN-folder/req.md"))
    errors = validate([req], folders=None)
    id_errors = [e for e in errors if "format" in e.message.lower()]
    assert id_errors == []


def test_id_format_integrated_via_validate():
    folder = _folder("REQM-FUN", "/spec/REQM-FUN-folder")
    req = _req(id="REQM-FUN-001", path=Path("/spec/REQM-FUN-folder/req.md"))
    errors = validate([req], folders=[folder])
    assert errors == []
