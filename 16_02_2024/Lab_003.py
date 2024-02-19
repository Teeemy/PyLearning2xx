# another example of map function

my_list1 = [21, 34, 54]
import math


def sq_rt(num):
    return math.sqrt(num)
    # return math.cbrt() fr cube root


sq_list = list(map(sq_rt, my_list1))
print(sq_list)
