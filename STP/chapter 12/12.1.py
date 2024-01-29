class Apple:
    def __init__(self, name, color, taste, price):
        self.name = name
        self.color = color
        self.taste = taste
        self.price = price


apple = Apple("Pink Lady", "Pink", "Sweet", "0.60")
print(apple.name, apple.color, apple.taste, apple.price)