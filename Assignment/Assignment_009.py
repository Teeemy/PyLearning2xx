# complete the factorial program with the function
# default value is 1

def factorial(n):

  if n < 0:
    raise ValueError("n must be non-negative")

  if n == 0:
    return 1

  else:
    return n * factorial(n - 1)

# Example usage
number = 1
result = factorial(number)
print(f"The factorial of {number} is {result}")