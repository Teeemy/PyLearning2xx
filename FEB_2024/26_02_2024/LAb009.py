# create a class name Password
class Password:
    def __init__(self, Password):
        self.__password = Password
        self.public_var = 15

    # use fn to get and set the private and protected variable
    def get_password(self, is_authenticated):
        if is_authenticated:
            print(self.__password)
        else:
            print("Invalid Password")

    def set_password(self, password):
        if len(password) > 10:
            self.__password = password
        else:
            print("Not Allowed, weak password")


pwd = Password("Hacker123")
# print(pwd.public_var)
pwd.get_password(False)
pwd.set_password("Armitrnd34")

