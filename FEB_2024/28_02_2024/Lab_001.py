# single inheriance is mostly use in Automation
# Hierarchical Inheritance

class Vehicle:
    def details(self):
        return "THIS IS A VEHICLE"


class Car(Vehicle):
    pass
   ## def details(self):
       ## return "THIS IS A CAR"


class Bicycle(Vehicle):
    def details(self):
        return "THIS IS A BICYCLE"


car = Car()
bicycle = Bicycle()

print(car.details())
print(bicycle.details())