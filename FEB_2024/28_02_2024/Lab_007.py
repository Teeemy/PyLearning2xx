# Method Overloading
# python does not support method overloading in traditional sense
# overloading means same name function with diff parameters

class MathUtil:
    def add(self, a, b=0, c=0):
        return a + b + c


math = MathUtil()
op0 = math.add(1)
op1 = math.add(1, 2)
op2 = math.add(1, 2, 3)  # method overloading
