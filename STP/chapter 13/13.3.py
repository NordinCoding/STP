class Shape:
    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):
    def __init__(self, long_side, short_side):
        super().__init__()
        self.long_side = long_side
        self.short_side = short_side

    def calculate_perimeter(self):
        return (self.long_side * 2) + (self.short_side * 2)


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, change):
        self.side = self.side - change


square = Square(4)
rectangle = Rectangle(4, 2)

square.what_am_i()
rectangle.what_am_i()