from classes.Card import *


class Building(Card):
    def __init__(self, color, name, price, value):
        super().__init__(color)
        self.name = name  # Name of the building
        self.value = value  # Value in points
        self.price = price  # Price to build it

    def __repr__(self):
        string = self.name + "\nCost : " + str(self.price) + "\nColor : " + self.color
        return string

    def __str__(self):
        string = self.name + " (" + str(self.value) + ")"
        return string
