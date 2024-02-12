# create a program that takes 2 numbers as input and print whether the first number is
# greater than, less than or equal to the second number
b = 10
c = 20
if b > c:
    print("hello")
elif b < c:
    print("good")
else:
    print("ciao")

# print(b < c)
# print(b == c)
# print(b > c)

def compare_numbers(num1, num2):
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 < num2:
        print(f"{num1} is less than {num2}")
    else:
        print(f"{num1} is equal to {num2}")

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        compare_numbers(num1, num2)
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()