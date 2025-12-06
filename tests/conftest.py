# tests/conftest.py
import pytest

# Define a fixture that returns a common pair of test data
@pytest.fixture
def standard_dims():
    """Fixture to provide standard length and width (10x20)."""
    print("\n--- Running Fixture Setup ---") # Often used for setup logs
    return 10, 20  # Returns a tuple: (length, width)