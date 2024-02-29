class Car:
    name = None

    def __init__(self):
        self.name = "public variable"

    def public_function(self):
        print("This is a public func()")

    def __private_fuction(self):
        print("This is a private func()")

    def public_fn_private(self):  # public fn can access private fn only when it is within the same class
        self.__private_fuction()  # this is only allowed bcus it is within the class

# so the concepts of encapsulation says that you are only allowed to access the private and protected
# variables when you are within the same class
# private and protected are mostly use for security, so nobody can have access