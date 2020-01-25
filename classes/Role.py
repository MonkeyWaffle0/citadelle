from classes.Card import *
from classes.Deck import *
from classes.Player import *


class Role(Card):
    def __init__(self, color, role):
        super().__init__(color)


class Assassin(Role):
    def __init__(self):
        super().__init__("none")
        self.player = None
        self.role = "Assassin"
        self.turnOrder = 1

    def __str__(self):
        return self.role

    def action(self, deck):
        deck.showAssassin()
        choice = input("Who do you want to kill ? ")
        kill = deck[choice - 1]
        print("You killed the " + kill)
        for player in Player.players:
            if player.role == kill:
                player.killed()


class Voleur(Role):
    def __init__(self):
        super().__init__("none")
        self.player = None
        self.role = "Voleur"
        self.turnOrder = 2

    def __str__(self):
        return self.role

    def action(self, deck):
        deck.showVoleur()
        choice = input("Who do you want to steal from ? ")
        steal = deck[int(choice) - 1]
        print("You stole the " + steal)
        for player in Player.players:
            if player.role == steal:
                player.stolen()


class Magicien(Role):
    def __init__(self):
        super().__init__("none")
        self.player = None
        self.role = "Magicien"
        self.turnOrder = 3

    def __str__(self):
        return self.role

    def action(self, deck):
        print("Do you want to :")
        print("1 - Swap your hand with another player")
        print("2 - Change some of your cards")
        print("3 - Nothing")

        choosing = True
        while choosing:
            choice = input()

            if choice == "1":
                choosing = False
                self.swap()
            elif choice == "2":
                choosing = False
                self.change()
            elif choice == "3":
                choosing = False
            else:
                print("Not a valid answer.")

    def swap(self):
        print("Players :")
        Player.show(Player)
        choice = input("Who do you want to swap cards with ? ")

        choosing = True
        while choosing:
            choice = input()

            if len(Player.players) >= int(choice) > 0:
                choosing = False
                otherPlayer = Player.players[int(choice) - 1]
                temp = self.player.hand
                self.player.hand = otherPlayer.hand
                otherPlayer.hand = temp

            else:
                print("Not a valid answer.")

    def change(self):
        string = ""
        for i, card in enumerate(self.player.hand):
            string += str(i + 1) + " - " + card + "\n"

        print(string)
        print("What card do you want to change ?")

        choosing = True
        while choosing:
            choice = input()

            if len(self.player.hand) >= int(choice) > 0:
                choosing = False
                card = self.player.hand[int(choice) - 1]
                self.player.discard(card)
                self.player.drawBuilding()

            else:
                print("Not a valid answer.")


class Roi(Role):
    def __init__(self):
        super().__init__("Yellow")
        self.player = None
        self.role = "Roi"
        self.turnOrder = 4

    def __str__(self):
        return self.role

    def action(self):
        self.player.king()


class Eveque(Role):
    def __init__(self):
        super().__init__("Blue")
        self.player = None
        self.role = "Eveque"
        self.turnOrder = 5

    def __str__(self):
        return self.role

    def action(self):
        pass


class Marchand(Role):
    def __init__(self):
        super().__init__("Green")
        self.player = None
        self.role = "Marchand"
        self.turnOrder = 6

    def __str__(self):
        return self.role

    def action(self):
        self.player.getMoney(1)


class Architecte(Role):
    def __init__(self):
        super().__init__("None")
        self.player = None
        self.role = "Architecte"
        self.turnOrder = 7

    def __str__(self):
        return self.role

    def action(self):
        self.player.drawBuilding()
        self.player.drawBuilding()


class Condotiere(Role):
    def __init__(self):
        super().__init__("Red")
        self.player = None
        self.role = "Condotiere"
        self.turnOrder = 8

    def __str__(self):
        return self.role

    def action(self):
        pass
