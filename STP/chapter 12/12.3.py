class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.area = 0

    def calculate_area(self):
        area = (self.base * 0.5) * self.height
        return area


triangle = Triangle(10, 7)
triangle.area = triangle.calculate_area()
print(triangle.area)
