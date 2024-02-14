# global in python

# Fibonacci series is incrementation e.g 0,1,1,2,3,5,8,13=0+1+1+2+3+5+8+13=21

#a = 10
#b = 12
#a, b = a, a + b
#print(a, b)

a, b = 0,1
while a < 10:
    print(a, end=" ") # end =" " means to be on the same line
    a, b = b, a+b
