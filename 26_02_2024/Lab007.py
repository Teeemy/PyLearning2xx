class Browser:
    def submit(self):
        self.__password = "1234"
        self._username = "Mariam@13"
        self.heading = "VWO Login"

    def details(self):
        print("your username is protected " + self._username)
        print("your password is private "+ self.__password)


firefox = Browser()
# firefox.__password in this case you can't access the password bcus it is private
# in order to access it, you must create a method which is under the same class

firefox = Browser()
firefox.submit()

print(firefox.heading)
print(firefox.details())
