# get even num

number = [1, 4, 7, 9, 2, 6]


def even(num):  # converting using function
    return num % 2 == 0


even_numbers = filter(even, number)
print(list(even_numbers))

even_lambda = lambda num: num % 2 == 0  # converting using lambda
