"""Tests for reqm.fs — parse and load functions."""
from pathlib import Path

import pytest
from reqm.fs import (
    _split_frontmatter,
    _extract_sections,
    parse_folder_meta,
    parse_requirement,
    parse_validation_item,
    load_folder_meta,
    load_requirements,
    find_spec_root,
    load_spec_meta,
    load_validation_items,
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
    assert req.derived_from == []
    assert req.related_to == []
    assert req.tags == ["test"]


def test_parse_requirement_with_derived_from(fixtures_dir: Path):
    req = parse_requirement(fixtures_dir / "B-child-requirement.md")
    assert req.id == "B"
    assert req.derived_from == ["A"]
    assert req.related_to == ["C"]


def test_parse_requirement_with_tests(fixtures_dir: Path):
    req = parse_requirement(fixtures_dir / "E-requirement-with-tests.md")
    assert req.id == "E"
    assert req.validated_by == ["TC-001", "TC-002"]



def test_parse_folder_meta(fixtures_dir: Path):
    meta = parse_folder_meta(fixtures_dir / ".folder-metadata.md")
    assert meta.id == "FIX"
    assert meta.title == "Test Fixtures Folder"
    assert meta.path == fixtures_dir
    assert "unit tests" in meta.description


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
    assert "GA-group-a-folder" in str(nested[0].path)


def test_parse_validation_item(validation_items_dir: Path):
    item = parse_validation_item(validation_items_dir / "TC-001.md")
    assert item.id == "TC-001"
    assert item.title == "Verify requirement E links to validation items"
    assert item.method == "Test"
    assert item.level == "System"
    assert item.status == "Draft"
    assert "Objective" in item.objective or item.objective != ""


def test_load_validation_items(validation_items_dir: Path):
    items = load_validation_items(validation_items_dir)
    ids = {i.id for i in items}
    assert ids == {"TC-001", "TC-002"}
    assert len(items) == 2


def test_load_validation_items_empty_dir(tmp_path: Path):
    items = load_validation_items(tmp_path)
    assert items == []


def test_load_spec_meta_missing(tmp_path: Path):
    """Returns a default SpecMeta when file is absent."""
    result = load_spec_meta(tmp_path)
    assert result.path == tmp_path
    assert result.id == ""
    assert result.title == ""
    assert result.type == "requirements"
    assert result.related_specifications == []


def test_load_spec_meta_present(tmp_path: Path):
    """Parses a valid .specification-metadata.md file."""
    meta_file = tmp_path / ".specification-metadata.md"
    meta_file.write_text(
        """---
id: REQM
title: reqm Requirements
type: validation_items
related_specifications:
  - id: SYS
    local_path: ../sys-arch
---

## Description

Test specification.
"""
    )
    result = load_spec_meta(tmp_path)
    assert result.path == tmp_path
    assert result.id == "REQM"
    assert result.title == "reqm Requirements"
    assert result.type == "validation_items"
    assert result.description == "Test specification."
    assert len(result.related_specifications) == 1
    rs = result.related_specifications[0]
    assert rs.id == "SYS"
    assert rs.local_path == "../sys-arch"


def test_load_spec_meta_empty_related(tmp_path: Path):
    """Handles missing or null related_specifications gracefully."""
    meta_file = tmp_path / ".specification-metadata.md"
    meta_file.write_text(
        """---
id: STANDALONE
related_specifications:
---

## Notes

No related specifications.
"""
    )
    result = load_spec_meta(tmp_path)
    assert result.id == "STANDALONE"
    assert result.related_specifications == []


def test_load_spec_meta_multiple_related(tmp_path: Path):
    """Parses multiple related_specifications entries."""
    meta_file = tmp_path / ".specification-metadata.md"
    meta_file.write_text(
        """---
id: CORE
related_specifications:
  - id: SYS
    local_path: ../sys-arch
  - id: TEST
    local_path: /abs/path/to/tests
---

## Description

Core specification with multiple relations.
"""
    )
    result = load_spec_meta(tmp_path)
    assert len(result.related_specifications) == 2
    assert result.related_specifications[0].id == "SYS"
    assert result.related_specifications[1].local_path == "/abs/path/to/tests"


def test_find_spec_root_finds_in_current_dir(tmp_path: Path):
    """Returns start when .specification-metadata.md is in start itself."""
    (tmp_path / ".specification-metadata.md").write_text("---\nid: X\n---\n")
    assert find_spec_root(tmp_path) == tmp_path


def test_find_spec_root_walks_upward(tmp_path: Path):
    """Finds .specification-metadata.md in a parent directory."""
    (tmp_path / ".specification-metadata.md").write_text("---\nid: X\n---\n")
    subdir = tmp_path / "sub" / "deep"
    subdir.mkdir(parents=True)
    assert find_spec_root(subdir) == tmp_path


def test_find_spec_root_not_found(tmp_path: Path):
    """Raises FileNotFoundError when no metadata file exists anywhere."""
    with pytest.raises(FileNotFoundError):
        find_spec_root(tmp_path)


def test_find_spec_root_coexistence_error(tmp_path: Path):
    """Raises RuntimeError when both metadata file variants exist."""
    (tmp_path / ".specification-metadata.md").write_text("---\nid: X\n---\n")
    (tmp_path / ".project-metadata.md").write_text("---\nproject_key: X\n---\n")
    with pytest.raises(RuntimeError):
        find_spec_root(tmp_path)


def test_find_spec_root_coexistence_with_folder_metadata(tmp_path: Path):
    """Raises RuntimeError when .specification-metadata.md and .folder-metadata.md coexist."""
    (tmp_path / ".specification-metadata.md").write_text("---\nid: X\n---\n")
    (tmp_path / ".folder-metadata.md").write_text("---\nid: X-FOLD\ntitle: Folder\n---\n")
    with pytest.raises(RuntimeError):
        find_spec_root(tmp_path)