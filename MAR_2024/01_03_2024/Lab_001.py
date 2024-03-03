# Exception: is a event that occurs during the execution
# of a program that disrupt normal flow of the progrm
# in python execption are simple..
# try and except is used in python to handle exception
# try means to try code,if there is an error then excute except code
# except means execute except code if there is try problem'
# try and excep work hand in hand

a = int(input("Enter num 1 \n"))
b = int(input("Enter num 1 \n"))

try:
    c = a / b
    print("Div is", c)
except Exception as e:
    print(e)
print("Zero Division, please don't use B as zero!")
print("This is an important message that users need to see")
