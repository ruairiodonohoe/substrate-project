"""Test Substrate Project."""

import substrate_project


def test_import() -> None:
    """Test that the app can be imported."""
    assert isinstance(substrate_project.__name__, str)
