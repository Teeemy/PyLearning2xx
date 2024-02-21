# if you don't use dict, then u must use double quotes ""
Mariam_details = dict (name="Mariam",age=32,isMale=False,Address="Via Bandello Italy")
Mariam_details2 = {"name":"Mariam","90": 32,",isMale":False,"Address":"Via Bandello Italy"}

print(Mariam_details2.get("90"))
print(Mariam_details["age"])
print(Mariam_details["name"])

my_dict = {'a': 1, 'b': 2,' c': 3,'a' : 54}# keys cannot be duplicated in dict..
# it will print the last duplicates and # store the first one
# keys must be unique in dict'

print(my_dict)
print(len(my_dict))

keys = my_dict.keys() # to get the keys of the value
values = my_dict.values()

keys_list = list(keys)
print(values)
