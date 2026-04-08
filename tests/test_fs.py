"""Tests for reqm.fs — parse and load functions."""
from pathlib import Path

import pytest
from reqm.fs import (
    _split_frontmatter,
    _extract_sections,
    parse_folder_meta,
    parse_requirement,
    load_folder_meta,
    load_requirements,
)


def test_split_frontmatter():
    text = """---
id: A
title: Test
---

## Description

Body text here.
"""
    yaml_text, body = _split_frontmatter(text)
    assert "id: A" in yaml_text
    assert "title: Test" in yaml_text
    assert "## Description" in body
    assert "Body text here." in body


def test_split_frontmatter_no_delimiter():
    text = "Just plain markdown"
    yaml_text, body = _split_frontmatter(text)
    assert yaml_text == ""
    assert body == text


def test_extract_sections():
    body = """## Description

This is the description.

## Rationale

This is the rationale.
"""
    sections = _extract_sections(body)
    assert "Description" in sections
    assert "This is the description." in sections["Description"]
    assert "Rationale" in sections
    assert "This is the rationale." in sections["Rationale"]


def test_parse_requirement(fixtures_dir: Path):
    req = parse_requirement(fixtures_dir / "A-parent-requirement.md")
    assert req.id == "A"
    assert req.title == "Parent requirement"
    assert req.type == "Functional"
    assert req.verification == ["Test"]
    assert "parent requirement" in req.description
    assert "Used for testing" in req.rationale
    assert "Must work correctly" in req.acceptance_criteria
    assert req.derived_from is None
    assert req.related_to == []
    assert req.tags == ["test"]


def test_parse_requirement_with_derived_from(fixtures_dir: Path):
    req = parse_requirement(fixtures_dir / "B-child-requirement.md")
    assert req.id == "B"
    assert req.derived_from == "A"
    assert req.related_to == ["C"]


def test_parse_requirement_with_tests(fixtures_dir: Path):
    req = parse_requirement(fixtures_dir / "E-requirement-with-tests.md")
    assert req.id == "E"
    assert req.tests == ["TEST-001", "TEST-002"]


def test_parse_requirement_extra_keys(fixtures_dir: Path):
    req = parse_requirement(fixtures_dir / "A-parent-requirement.md")
    # No extra keys expected in this fixture
    assert isinstance(req.extra, dict)


def test_parse_folder_meta(fixtures_dir: Path):
    meta = parse_folder_meta(fixtures_dir / ".folder-metadata.md")
    assert meta.id == "FIX"
    assert meta.title == "Test Fixtures Folder"
    assert meta.path == fixtures_dir


def test_load_folder_meta_exists(fixtures_dir: Path):
    meta = load_folder_meta(fixtures_dir)
    assert meta is not None
    assert meta.id == "FIX"


def test_load_folder_meta_missing(tmp_path: Path):
    result = load_folder_meta(tmp_path)
    assert result is None


def test_load_requirements(fixtures_dir: Path):
    reqs = load_requirements(fixtures_dir)
    ids = {r.id for r in reqs}
    assert ids == {"A", "B", "C", "D", "E", "F"}
    assert len(reqs) == 6


def test_load_requirements_nested(fixtures_dir: Path):
    """Recursive discovery finds nested requirements."""
    reqs = load_requirements(fixtures_dir)
    nested = [r for r in reqs if r.id == "F"]
    assert len(nested) == 1
    assert "group-a" in str(nested[0].path)
