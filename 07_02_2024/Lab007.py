# String concat
str1 = "hello"
str2 = "world"
str3 = str1 + str2  ## + is an operator.it means to concat
print(str3)

name = "Ashabi"
age = 31
# r = name+age will give typeerro bcs str and int cannot concat
# it is possible when u convert int to string
r = name + str(age)  # conversion of int to str
print(r)

g = "Hello"
g += "World"  # another way of concatenating
print(g)

# increment and decrement
x = 5
x -= 1
print(x)

x = 10
# y = ++x not allowed in python but java
y = x+1
print(y)