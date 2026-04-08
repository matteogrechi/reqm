"""Tests for reqm.validate — each rule + end-to-end."""
from reqm.validate import (
    ValidationError,
    _check_required_fields,
    _check_duplicate_ids,
    _check_broken_links,
    _check_enum_values,
    validate,
)
from reqm.models import Requirement
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
    reqs = [_req(id="A", derived_from="NONEXISTENT")]
    errors = _check_broken_links(reqs)
    assert any("derived_from" in e.message for e in errors)


def test_broken_links_related_to():
    reqs = [_req(id="A", related_to=["NONEXISTENT"])]
    errors = _check_broken_links(reqs)
    assert any("related_to" in e.message for e in errors)


def test_broken_links_valid():
    reqs = [
        _req(id="A"),
        _req(id="B", derived_from="A", related_to=["A"]),
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
        _req(id="B", derived_from="A"),
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
