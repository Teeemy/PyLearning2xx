# filter is also another function.
# it filters items frm list based on logic and
# return less num of items

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
 # to get even numbers
even_numbers = filter(lambda i: i % 2 == 0, number)

print(list(even_numbers))


