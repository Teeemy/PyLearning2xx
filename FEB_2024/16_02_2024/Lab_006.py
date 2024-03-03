# Tuple is a collection of items like list
# values cannot be  changed like in list
# tuple does not have square bracket like list

# my_list[1,2,3,4,5,] and my_tuple(1,2,3,4,5)
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))

my_list = [1, 2, 3, 4]
my_list[0] = 21  # changing value
print(my_list)
print(type(my_list))

new_tuple = tuple(my_list)  # converting tuple to list
print(new_tuple)
