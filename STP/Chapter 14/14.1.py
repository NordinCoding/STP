class Square:
    square_list = []

    def __init__(self, w, l):
        self.width = w
        self.length = l
        self.square_list.append((self.width, self.length))

    def print_square(self):
        string = int(self.length)
        for i in range(3):
            print(string, "by ", end="")
        print(string)


s1 = Square(4, 4)
s1.print_square()

s2 = Square(3, 3)
s2.print_square()

s3 = Square(2, 2)
s3.print_square()
