# E:\My_Projects\Python\my_first_app\tests\test_calculations.py
import pytest
from application.calculations import calculate_area

# --- Fixture Definition (Often placed in conftest.py) ---

@pytest.fixture
def standard_dims():
    """Fixture to provide standard, valid dimensions (10x20)."""
    # This setup code runs once before any test that uses it
    return 10, 20  # Returns a tuple: (length, width)

# --- Test Functions ---

def test_area_with_positive_numbers():
    """Test Case 1: The happy path with expected positive inputs."""
    # Arrange & Act
    result = calculate_area(7, 8)
    
    # Assert
    assert result == 56

def test_area_with_fixture(standard_dims):
    """Test Case 2: Uses the fixture to grab the test data."""
    # Arrange: Unpack values provided by the fixture
    length, width = standard_dims
    
    # Act
    result = calculate_area(length, width)
    
    # Assert
    assert result == 200

def test_area_with_zero():
    """Test Case 3: Expects a ValueError when one input is zero."""
    # Assert: Use pytest.raises to check if the ValueError is triggered
    with pytest.raises(ValueError):
        calculate_area(0, 10)

def test_area_with_negative_input():
    """Test Case 4: Expects a ValueError when an input is negative."""
    # Assert: Checks for the ValueError
    with pytest.raises(ValueError):
        calculate_area(5, -1)

# To run these tests successfully:
# 1. Ensure your (venv) is active.
# 2. Run: pytest