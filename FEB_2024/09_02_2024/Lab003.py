# problem statement
# find the maximum btw 3 numbers
num1 = int(input("ENTER NUM1"))
num2 = int(input("ENTER NUM2"))
num3 = int(input("ENTER NUM3"))

# call the max function
# max_num = max(num1,num2,num3) max function
#print(max_num) else use if loops operation (and) not or

if num1 > num2 and num1 > num3:
    print("Max is ", num1)
elif num2 > num1 and num2 > num3:
    print("Max is ", num2)
else:
    print("Max is ", num3)