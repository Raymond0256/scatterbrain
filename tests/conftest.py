"""Configurations for test files."""
from _pytest.config import Config


def pytest_configure(config: Config) -> None:
    """Configure markers for pytest."""
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")
