def is_leap_year(year):
    """
    Checks if a given year is a leap year.

    Args:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """

    if year % 4 != 0:
        return False  # Not divisible by 4, not a leap year
    elif year % 100 == 0:
        return year % 400 == 0  # Divisible by 100, must also be divisible by 400
    else:
        return True  # Divisible by 4 but not by 100, a leap year

# Get the year from the user (optional)
year = int(input("Enter a year: "))
if year <= 0:
    raise ValueError(" Year must be positive.")
# Check if the year is a leap year and print the result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")