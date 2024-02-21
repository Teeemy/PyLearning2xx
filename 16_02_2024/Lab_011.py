# SET is collection of unique item
# it does not return duplicate values
set3 = {1, 2, 3, 4, 5, 5, 4, 3}  # set is an ordered unique item
print(set3)

# converting list to set
list1 = [42.2, 33, 33, 45, 21]
set1 = set(list1)
print(len(set1))
print(set1)

# converting set to list
set2 = {3, 5, 7, 28, 9, 1, 1}
list2 = list(set2)
print(list2)

# converting tuple to set
t = ("TheTestingAcademy", "for", "a", "TheTestingAcademy")
print(set(t))

# union of set means concatenation of set
set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)

# intersection of set means finding common elements
set1 = {1, 2, 3, 4, 5, 6, }
set2 = {4, 5, 6, 7, 8, 9, }
my_set = set1.intersection(set2)
print(my_set)

# diff of set means to find uncommon elements
set1 = {1, 2, 3, 4, 5, 6, }
set2 = {4, 5, 6, 7, 8, 9, }
my_set = set1.difference(set2)  # i.e what is in set1 but not in set 2
my_set2 = set2.difference(set1)  # i.e what is in set2 but not in set 1
print(my_set)
print(my_set2)
