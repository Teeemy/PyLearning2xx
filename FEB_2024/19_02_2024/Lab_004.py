# create a program of calculator

class Cal:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

object_ref = Cal()
result = object_ref.sum(6,4)
print(result)

result1 = object_ref.sub(6,4)
print(result1)

result2 = object_ref.mul(6,4)
print(result2)

result3 = object_ref.div(6,4)
print(result3)
