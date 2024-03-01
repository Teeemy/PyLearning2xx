# Multiple Inheritance is MRO  i.e method resolution order
class Father:
    def father_money(self):
        return "3000"

    def home(self):
        # print("This is from the Father")
        return "This is from the Father"


class Mother:
    def mother_money(self):
        return "2000"

    def home(self):
        # print("This is from the Mother")
        return "This is from the Mother"


# class Son(Father, Mother):
# pass

class Son(Mother, Father):
    pass


son = Son()
print(son.father_money())
print(son.mother_money())
print(son.home())  # the program is confuse on what to print here bcus both father and mother money are from hone
# it will authomatically print in order
