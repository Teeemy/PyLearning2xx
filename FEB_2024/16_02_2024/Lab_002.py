# map function  is used to will give square of a number. it is used for many numbers

def sq_of_number(num):
    return num ** 2


result = sq_of_number(5)
print(result)

# another way of using map
# map takes each item frm d list and execute the function on it
numbers = [1,2,3,4,5]

sq_of_number = list(map(sq_of_number, numbers))

print(sq_of_number)
