# MULTI LEVEL Inheritance

class Grand_father:
    def home(self):
        print("Granny")


class Father(Grand_father):
   def home2(self):
       print("Maitama")

class Son(Father):
    def home3(self):
        print("Asokoro")

Yusuf = Son()
Yusuf.home()
Yusuf.home2()
Yusuf.home3()

Yekin = Father()
Yekin.home()
Yekin.home2()


Yunus = Grand_father()
Yunus.home()

