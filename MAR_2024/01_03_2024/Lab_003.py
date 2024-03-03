# using try and except to create a function

class ABC:
    def f2(self):
        try:
            x = int(input("Enter a valid number \n"))
        except Exception as e:
            print("Enter only int value as x")
        else:
            print(x)
        finally:
            print("I get printed anyhow")


a = ABC()
a.f2()
