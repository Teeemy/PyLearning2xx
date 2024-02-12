# problem statement
# find the leap year
year = int(input("Enter the Year: ") )

#Print whether the given year is a leap year or not

if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        print(f"{year} is a leap year")
else:
        print(f"{year} is not a leap year")