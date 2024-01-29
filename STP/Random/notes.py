class House:
    def __init__(self, people, location):
        self.people = people
        self.location = location
        self.value = 300000

    ## increase is in %
    def new_value(self, increase):
        change_value = self.value * (increase / 100)
        change_value = int(change_value)
        self.value = self.value + change_value


house = House(3, "Heerhugowaard")
house.new_value(5)
print(house.value)
