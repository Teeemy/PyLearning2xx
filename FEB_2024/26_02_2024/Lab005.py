# 3 diff types of data members were introduce for encapsulation process

# 1 PUBLIC
# 2 PRIVATE
# 3 PROTECTED

class Car:
    name = None

    # password = "123"

    def __init__(self):
        self.public_var = "public"  # this is a public encapsulation
        self._protected_var = "protected123"  # this is a protected variable with single underscore
        self.__private_var = "password@123"  # this ia a private variable with double underscore
        self.__password = "Pass234"  # this can only be access within the class not outside

    # it can be any name but when it starts with single underscore(protected) double underscore(double)

    # to access protected or private variable, u must use method

    def _protectedmethod(self):
        print("protected!")

    def __privatemethod(self):
        print("private!")
        print()

    def printName(self):
        print("I am allowed to use the private variable because i am in the class " + self.__password)


Honda = Car()
Honda.printName()

print(Honda.public_var)  # it is only public var you can access but to access private and protected. we use method with it.
# print(Honda.__password) # this is wrong.. password should be protected from public
print(Honda.printName())
