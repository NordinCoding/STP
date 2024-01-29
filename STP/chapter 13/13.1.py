class Rectangle:
    def __init__(self, long_side, short_side):
        self.long_side = long_side
        self.short_side = short_side

    def calculate_perimeter(self):
        return (self.long_side * 2) + (self.short_side * 2)


class Square:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4


rectangle = Rectangle(5, 4)
print(rectangle.calculate_perimeter())

square = Square(4)
print(square.calculate_perimeter())
