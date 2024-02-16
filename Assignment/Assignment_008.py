# Implement a Function to Calculate the Factorial of a Number
import math

def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for c in range(2, n + 1):
            result *= i
        return result
    result = factorial(number)
    print(f"The factorial of {number} is {result}")

num = int(input("Enter the number: \n"))
factorial = math.factorial(num)
print("The factorial of", num, "is", factorial)




