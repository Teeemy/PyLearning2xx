# oops : object-oriented programming is concept that says everything can
# be converted to obj and classes
# every class can have attribute and behaviour in oops
# Class is a blueprint to create an object i.e design

# create a person class
# mariam,temi,oyin they are all obj

# class person: # is an empty class ' obj is created with class name and()
# pass

class Person:
    # Attributes are called data members
    name = None
    age = None
    id = None
    phone_no = None

    # Behaviour is methods..whenever a function is mention in class it is called method

    def talk(self):  # self means it is owned instance i.e it is d first args of every
        print("I can talk")  # func within the class
        # self is a special variable that is used within
        # the context of oop.it is a ref to instnace of a class

    def sleep(self):  # this is a method and mthods are part of class
        print("I am a Method")
        print("I can sleep")

    def eat(self):
        print("I can eat")

    # def another():  # this is a function. it is an independent function
    # print("I am a function")

    def person_information(self):
        print("Your information entails", self.name, self.age, self.id, self.phone_no)


person_name = input("Enter your name\n")
person_age = input("Enter your age\n")
person_id = input("Enter your id\n")
person_phone_no = input("Enter your phone no\n")

# objects creation.. to create an obj there must be ClassName()
person_obj_ref = Person()

person_obj_ref.name
person_obj_ref.age
person_obj_ref.id
person_obj_ref.phone_no

person_obj_ref.person_information()

# mariam = Person()
# mariam.name = "Mariam"
# print(mariam.name)
