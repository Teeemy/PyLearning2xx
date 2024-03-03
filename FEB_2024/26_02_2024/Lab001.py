# how to create a class
class Person:  # the first letter of the class should be capital
    name = None  # this a class/instance variables
    age = None

    def walk(self):
        print("Ciao my name is", self.name)
        print("Ciao my age is", self.age)


Ziyad = Person()  # obj crreation
Ziyad.walk()
