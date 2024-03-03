# dict are not orederd, but we can create ordered list by importing orderDict

from collections import OrderedDict
od = OrderedDict()
od['a'] = 14
od['b'] = 24
od['c'] = 76
od['d'] = 12
od['e'] = 16
print(od)


# to iteratesa and find a key or value in dict

my_dict = {'b': 4, 'a': 2, 'c': 8}
for k,v in my_dict.items():
    if k == 'c':
        print("'c is found !")

        #or use
    op1 = 'f' in my_dict
    op2 = 'a' in my_dict
    print(op1)
    print(op2)

