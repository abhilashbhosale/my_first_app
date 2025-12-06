# E:\My_Projects\Python\my_first_app\application\calculations.py

def calculate_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle."""
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive.")
    return length * width