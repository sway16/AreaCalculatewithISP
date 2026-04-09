from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Calculator works with any shape
class AreaCalculator:
    def calculate(self, shape: Shape):
        return shape.area()


# Usage
calc = AreaCalculator()

print(calc.calculate(Circle(5)))
print(calc.calculate(Square(4)))
print(calc.calculate(Rectangle(4, 6)))