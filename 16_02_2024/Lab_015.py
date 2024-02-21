# Dictionary is a key value data type
# it is an ordered collection of data
my_dict = {}  # creating an empty dic
my_dict2 = dict()
my_tuple = ()
my_set = {1}
my_list = []
print(type(my_dict))
print(type(my_dict2))
print(type(my_tuple))
print(type(my_list))
print(type(my_set))

# example of dict
phone_book = {"Batman": 987654321, "Wonderwoman": 123456789, "Spiderman": 978653420}
print(phone_book)
print(len(phone_book))
print(phone_book["Wonderwoman"])

phone_book2 = dict(Batman=234, Vikings=132, Flash =541,VanHelsing=437)  # without doublequotes ""
print(phone_book2)
print(len(phone_book2))
print(phone_book2['Flash'])
print(phone_book2["Flash"])
print(phone_book2.get('Flash'))
