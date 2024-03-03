# Abstration: hiding the details and showing what is required
# abstract base class or abstract base methods

# abstract methd
from abc import ABC, abstractmethod


class Animal(ABC):  # this inheritance is  from ABC class in the python compiler
    pass

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):  # incomplete function/method
        pass


class Dog(Animal):  # inheritance from animal class
    pass

    def sound(self):  # sound func must be called to access the abstract method
        return "BOW BOW"


class Cat(Animal):
    pass

    def sound(self):
        return "MEOW"

dog = Dog("Sharon")
print(dog.sound())

cat = Cat("Jully")
print(cat.sound())
