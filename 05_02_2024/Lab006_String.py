# Strings is a bunch of char.it can be "" or ''

firstname = "Temitope"
lastname = 'Oyinkansola'
print(firstname)
print(lastname)
print(type(firstname))
print(type(lastname))

# format string -> f
# f is used to replace the value

T = "Tope"
M = 'Mariam'
O = 'Onibonoje'

firstname = "Kojo"
lastname = 'ojor'
age = 39
isMarried = True
print(f"your name is {T} {M}")
print(f'your surname is {O}')
print(f"your name is {firstname} {lastname}.your age is {age} and you are {isMarried}")

# String format for table of
# 2 x 1 =2
num = 2 # you can change the value of 2 to another number
print(f"{num}x1={num}")
print(f"{num}x2={num*2}")
print(f"{num}x3={num*3}")
print(f"{num}x4={num*4}")
print(f"{num}x5={num*5}")

name = 'batman'
name2 =" superman"
print(len(name)) #len start from -> 1 # index start from -> 0
print(name[4]) # print the value at 4 (index)
print(name[5])
print(name[3])
print(len(name)-1)
print(name[len(name)-1])