"""Unit tests for __version__.py."""

import montypy.grail


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(montypy.grail, "__version__")
    assert montypy.grail.__version__ != "0.0.0"
