import calendar

def is_leap_year(year):
  """Checks if a given year is a leap year using the 'calendar' module.

  Args:
    year: The year to check.

  Returns:
    True if the year is a leap year, False otherwise.
  """
  return calendar.isleap(year)

# Example usage
year = int(input("Enter a year: "))

if is_leap_year(year):
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")