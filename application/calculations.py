# E:\My_Projects\Python\my_first_app\application\calculations.py

def calculate_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle. Raises ValueError if inputs are non-positive."""
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive.")
    return length * width

def calculate_perimeter(length: float, width: float) -> float:
    """Calculates the perimeter of a rectangle."""
    # Note: Perimeter is usually calculated even if dimensions are zero, but for consistency 
    # with the area function, we might add checks here too in a real-world scenario.
    # For this example, we keep it simple.
    return 2 * (length + width)