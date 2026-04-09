from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def volume(self):
        return 0


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def volume(self):
        return 0


class Cube(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 6 * self.side * self.side

    def volume(self):
        return self.side ** 3

c = Circle(5)
s = Square(4)
cu = Cube(3)

print("Circle Area:", c.area())
print("Circle Volume:", c.volume())

print("Square Area:", s.area())
print("Square Volume:", s.volume())

print("Cube Area:", cu.area())
print("Cube Volume:", cu.volume())
