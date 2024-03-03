# *args and *kargs
# args means any number of argument

#def sum(a, b, c):
    #return a + b + c

#r = sum(1, 2, 3)
#print(r)

def print_argument(*args): # it means it can print any number of argument given
    for i in args:
        print(i,end=" ")


print_argument(1)
print_argument(1, 2)
print_argument(1, 2, 3)
print_argument(1, 2, 3, 4)


