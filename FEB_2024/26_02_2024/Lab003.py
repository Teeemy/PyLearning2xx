# create a page class for vwo

class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):# paramiterized constructor helps to set the value of None in the obj
        self.email = email
        self.password = password

    def loginconfirm(self):
        if self.password == "Mar1234":
            print("Login successfully")
        else:
            print("Invalid User")


zain = VWOLoginPage("zain@zain.com", "3456") # obj
zain.loginconfirm()

print("-------------")

mary = VWOLoginPage("ayun@yahoo.com","Mar1234")
mary.loginconfirm()

print(id(zain)) # to see tht they RE STORED IN DIFF MEMOERY
print(id(mary))
