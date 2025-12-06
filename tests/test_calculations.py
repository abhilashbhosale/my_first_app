# E:\My_Projects\Python\my_first_app\tests\test_calculations.py
import pytest
from application.calculations import calculate_area, calculate_perimeter

# --- Fixture Definition ---

@pytest.fixture
def standard_dims():
    """Fixture to provide standard, valid dimensions (10x20)."""
    return 10, 20  # Returns a tuple: (length, width)

# --- Area Test Functions (4 Tests) ---

def test_area_with_positive_numbers():
    """Test Case 1: The happy path with expected positive inputs."""
    result = calculate_area(7, 8)
    assert result == 56

def test_area_with_fixture(standard_dims):
    """Test Case 2: Uses the fixture to grab the test data."""
    length, width = standard_dims
    result = calculate_area(length, width)
    assert result == 200

def test_area_with_zero():
    """Test Case 3: Expects a ValueError when one input is zero."""
    with pytest.raises(ValueError):
        calculate_area(0, 10)

def test_area_with_negative_input():
    """Test Case 4: Expects a ValueError when an input is negative."""
    with pytest.raises(ValueError):
        calculate_area(5, -1)

# --- Perimeter Test Function (1 New Test) ---

def test_perimeter_calculation():
    """Test Case 5: Tests calculation of the perimeter."""
    result = calculate_perimeter(5, 10)
    assert result == 30