#Factorial
#n = 5 mean 5,4,3,2,1,=120 i.e 5*4*3*2*1 = 120
# n = 3 mean 3,2,1 = 3*2*1 = 6

number = int(input("Enter the fac number\n"))
if number < 0:
    print("Factorial")
elif number == 0:
    print("factorial - ", 1)
else:
    fact = 1
    for i in range(1, number +1):
        fact = fact * i
    print("factorial",fact)

