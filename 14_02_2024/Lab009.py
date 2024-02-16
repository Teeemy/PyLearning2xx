# list is collection of items.. duplicate is allowed in list
# there are many functions used in list below

my_list = [1, 2, 3]
my_list2= [1, True, "Temitope", 2.0] # it can have multiple types of data types

print(my_list)

print("Element at index 0:", my_list[0]) # index 0 is 1 bcus index start from 0

my_list [1] = 20 # changing index 1
print("LIst after changing element at index 1:", my_list)

my_list.append(4) # append means to add num at the back
print("List after appending:", my_list)

my_list.extend([8,6]) # extend means to add more list to the already existing list
print("List after extending:", my_list)

my_list.insert( 1 , 'a') # insert means to add a num or anything in the list
print("List after inserting 'a' at index 1:", my_list)

my_list.remove('a') # remove means to delete num from list
print("List after removing 'a':", my_list)

my_copy_list = my_list.copy() # append means to add num at the back
print(my_copy_list)

print("Index of 3 in the list: ", my_list.index(3)) # to print index  in a list

my_copy_list.sort()

print("sort my copy list: ", my_copy_list) # to sort a list in an ordered form

my_copy_list.reverse()

print("reversed of copy list: ",my_copy_list) # to reverse a list

#my_list.clear(4) # to clear a  list
#print("initial:", my_list)
#print(my_copy_list)