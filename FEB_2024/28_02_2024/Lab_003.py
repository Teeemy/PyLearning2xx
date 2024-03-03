# Hybrid inheritance consists of all the types of inheritance

# from line 6 to 18, its hierarchical inheritance
# FROM LINE 18 TO 20, ITS MULTIPLE INHERITANCE
class A:
    def methodA(self):
        return "METHOD A"


class B(A):
    def methodB(self):
        return "METHOD B"


class C(A):
    def methodC(self):
        return "METHOD C"


class D(B, C):
    def methodD(self):
        return "METHOD D"


d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())
