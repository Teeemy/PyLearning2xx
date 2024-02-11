import math

def calculate_area(radius):
    """Calculates the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.

    Raises:
        ValueError: If the radius is negative or zero.
    """

    if radius <= 0:
        raise ValueError("Radius must be positive.")

    area = math.pi * radius * radius
    return area

# Get user input for radius
radius = float(input("Enter the radius of the circle: "))

# Calculate and print the area
try:
    area = calculate_area(radius)
    print(f"The area of the circle with radius {radius} is: {area:.2f}")  # Format area to 2 decimal places
except ValueError as e:
    print(e)  # Print the error message