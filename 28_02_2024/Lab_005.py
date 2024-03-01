# polymorphism: it means many forms of obj creation
# poly consists of method overloading and method overriding

class Shape:
    def area(self):
        print("Area of Shape")


class Rectangle(Shape):
    def __init__(self, length, width):  # constructor
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # calcuating rectangle area


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius  # calculate circle area


shape1 = Rectangle(3, 4)
print(shape1.area())

shape2 = Circle(10)
print(shape2.area())
# polymorphism name remain same but purpose is diff in above example

shape3 = Shape()
print(shape3.area())