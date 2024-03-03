# try,except and finally
try:
    num1 = int(input("Enter a number 1 \n"))
    num2 = int(input("Enter a number 2 \n"))
    result = num1 / num2
except ValueError as v:  # it will throw a value exception.i/e if there is wrong data types
    print(v)
except ZeroDivisionError as z:
    print(z)
else:
    print(f"Result{result}")
finally:
    print("I will always be executed anyhow!")

