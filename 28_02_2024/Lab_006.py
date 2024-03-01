# Method OVerriding:same name in parent and child class
# child always override parent functions
#super means call my parent function
class Animal:
    def __init__(self):
        pass

    def sound(self):
        print("Animals makes sound")


class Dog(Animal):
    def __init__(self):
        pass

    def sound(self):
       # super().sound() it can be used to call animal method
        print("Dogs bark")


animal = Animal()
animal.sound()

dog = Dog()
dog.sound()
