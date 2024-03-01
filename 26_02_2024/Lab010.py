# INHERITANCE
# 1 SINGLE Inheritance

class Father:
    gold = 5 #property
    def drive_car(self): #function both can be access y son
        print("Camry")

    def threeBHKFlat(self):
        print("JBNK Flat")


class Son(Father):
    pass

Segun = Son()
Segun.drive_car()# inheritace from father class
Segun.threeBHKFlat()
print(Segun.gold)

print("--------")

baami = Father()
baami.drive_car()
print(baami.gold)