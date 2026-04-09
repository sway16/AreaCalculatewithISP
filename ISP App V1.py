class AreaCalculator:
    def calculate_area(self, shape, value):
        if shape == "circle":
            return 3.14 * value * value
        elif shape == "square":
            return value * value
        elif shape == "rectangle":
            return value[0] * value[1]
        else:
            return 0


calc = AreaCalculator()

print(calc.calculate_area("circle", 5))
print(calc.calculate_area("square", 4))
print(calc.calculate_area("rectangle", (4, 6)))