class Horse:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner


class Rider:
    def __init__(self, name, age):
        self.name = name
        self.age = age


john = Rider("John Deere", 25)
horse = Horse("penis", 4, john)

print(horse.owner.name)
