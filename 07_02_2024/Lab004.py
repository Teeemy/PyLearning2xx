# Assignment operator: will store the values of
# variable literal to the identifier
name = "Yemisi"

# unary operator- applied to single literal
age = 95
print(age)
my_bank_bal = -205
print(my_bank_bal)

#not operator is also a unary operator.it will do reverse of the
#correct value. it only works with boolean

is_married = True
print(not is_married)

#is operator: is identity operator

a = 5
b = 5
c = False
d = 6
print(a is b) # it means both a and b belong to the same datatypes,
# so we print true
print(b is c)
print(a is d) # false

my_list = [1, 2, 3]
my_list2 = [1, 2, 3]
print(my_list is my_list2)