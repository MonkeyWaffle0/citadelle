from classes.Role import *


class Player:
    players = []  # List of players
    buildingDeck = BuildingDeck()
    roleDeck = RoleDeck()

    def __init__(self, name):
        self.crown = False  # If the player has the crown
        self.killed = False  # If the player is killed
        self.stolen = False  # If the player got stolen by the voleur.
        self.order = 0  # Turn order
        self.role = ""  # His current role
        self.hand = []  # Buildings in his hand
        self.money = 2  # Amount of money he has
        self.city = []  # Buildings he built
        self.name = name

        self.players.append(self)

    def chooseRole(self):
        """Show the available roles, the player chose one."""
        print("Available roles :")
        print(self.roleDeck)
        choice = int(input("Which one do you chose ? "))
        self.role = self.roleDeck[choice - 1]
        self.roleDeck.remove(self.role)

    def pay(self, amount):
        if amount > self.money:
            print("You dont have enough gold coins for this.")
            return False
        else:
            self.money -= amount
            return True

    def showMoney(self):
        print("You have", self.money, "gold coins.")

    def getMoney(self, amount):
        self.money += amount

    def drawBuilding(self):
        """Draws a building from the building deck"""
        card = self.buildingDeck.draw()
        print("You drew", card.fg, str(card), Style.RESET_ALL)
        self.hand.append(card)

    def discard(self, card):
        """Discard a card from his hand"""
        self.hand.remove(card)

    def build(self, card):
        if card in self.city:
            print("You already have one of this building in your city.")
            return False
        elif self.pay(card.value):
            self.city.append(card)
            self.discard(card)
            print("You built a " + card)
            self.showMoney()
            return True
        else:
            return False

    def killed(self):
        self.killed = True

    def stolen(self):
        self.stolen = True

    def king(self):
        for player in self.players:
            player.crown = False
        self.crown = True

    def show(self):
        """Show every players"""
        string = ""
        for i, player in enumerate(self.players):
            string += str(i + 1) + " - " + player.name

    def showHand(self):
        print("You have :")
        for card in self.hand:
            print(card.fg, card, Style.RESET_ALL)