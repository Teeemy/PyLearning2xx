# pop means removing the variable and printing the value

my_dict = {'a': 1, 'b': 4, 'c': 2}
val = my_dict.pop('b')
val2 = my_dict.pop('a')
print(val)
print(val2)

Knights = {'gallahad': 'the pure', 'robin': 'the brave'}
print(len(Knights)) # to print the value and key item

for k,v in Knights.items(): # to iterates over the items and value
    print(k ,"...." ,v)
