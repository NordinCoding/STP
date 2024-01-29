import math


class Circle:
    def __init__(self):
        self.area = 0

    def calculate_area(self, radius):
        pi = math.pi
        area = pi * (radius ** 2)
        return area


circle = Circle()
circle.area = circle.calculate_area(7)
print(circle.area)
