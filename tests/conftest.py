"""Shared pytest fixtures and configuration."""
from __future__ import annotations
from pathlib import Path

import pytest


@pytest.fixture
def fixtures_dir() -> Path:
    """Path to the test fixtures directory (inside the spec root wrapper)."""
    return Path(__file__).parent / "FIX-spec-root" / "FIX-test-fixtures-folder"


@pytest.fixture
def validation_items_dir() -> Path:
    """Path to the test validation items directory."""
    return Path(__file__).parent / "FIX-validation-items"