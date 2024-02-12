# write a program to calculate the area of a circle
# given its radius using the formula area= πxr^2 (Take pie as 3.14)

import math

radius = float(input("Enter the radius"))  # take input from user
print(3.14 * radius ** 2)
# print(math.pi)
area = math.pi * pow(radius, 2)
# print(area)


