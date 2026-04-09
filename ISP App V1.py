from abc import ABC, abstractmethod


class AreaShape(ABC):
    @abstractmethod
    def area(self):
        pass


class VolumeShape(ABC):
    @abstractmethod
    def volume(self):
        pass


class Circle(AreaShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(AreaShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Cube(AreaShape, VolumeShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 6 * self.side * self.side

    def volume(self):
        return self.side ** 3


class AreaCalculator:
    def calculate(self, shape: AreaShape):
        return shape.area()

calc = AreaCalculator()

print("Circle Area:", calc.calculate(Circle(5)))
print("Square Area:", calc.calculate(Square(4)))
print("Cube Area:", calc.calculate(Cube(3)))


cube = Cube(3)
print("Cube Volume:", cube.volume())








'''class Cylinder(AreaShape, VolumeShape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        return 2 * 3.14 * self.radius * (self.height + self.radius)

    def volume(self):
        return 3.14 * self.radius**2 * self.height'''

'''print("Cylinder Area:", Cylinder(3,5).area())
print("Cylinder Volume:", Cylinder(3,5).volume())'''
