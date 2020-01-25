from classes.Card import *
from classes.Deck import *


class Role(Card):
    def __init__(self, color, role):
        super().__init__(color)


class Assassin(Role):
    def __init__(self, player):
        super().__init__("none")
        self.player = player
        self.role = "Assassin"
        self.turnOrder = 1

    def __str__(self):
        return self.role

    def toString():
        return "Assassin"

    def getTurnOrder():
        return 1

    def action(self, deck):
        deck.showAssassin()
        choice = input("Who do you want to kill ? ")
        kill = deck[choice - 1]
        print("You killed the " + kill)
        for player in Player.players:
            if player.role == kill:
                player.killed()


class Voleur(Role):
    def __init__(self, player):
        super().__init__("none")
        self.player = player
        self.role = "Voleur"
        self.turnOrder = 2

    def __str__(self):
        return self.role

    def toString():
        return "Voleur"

    def getTurnOrder():
        return 2

    def action(self, deck):
        deck.showVoleur()
        choice = input("Who do you want to steal from ? ")
        steal = deck[choice - 1]
        print("You stole the " + steal)
        for player in Player.players:
            if player.role == steal:
                player.stolen()


class Magicien(Role):
    def __init__(self, player):
        super().__init__("none")
        self.player = player
        self.role = "Magicien"
        self.turnOrder = 3

    def __str__(self):
        return self.role

    def toString():
        return "Magicien"

    def getTurnOrder():
        return 3

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

            if choice <= len(Player.players) and choice > 0:
                choosing = False
                otherPlayer = Player.players[choice - 1]
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

            if choice <= len(self.player.hand) and choice > 0:
                choosing = False
                card = self.player.hand[choice - 1]
                self.player.discard(card)
                self.player.drawBuilding()

            else:
                print("Not a valid answer.")


class Roi(Role):
    def __init__(self, player):
        super().__init__("Yellow")
        self.player = player
        self.role = "Roi"
        self.turnOrder = 4

    def __str__(self):
        return self.role

    def toString():
        return "Roi"

    def getTurnOrder():
        return 4

    def action(self):
        self.player.king()


class Eveque(Role):
    def __init__(self, player):
        super().__init__("Blue")
        self.player = player
        self.role = "Eveque"
        self.turnOrder = 5

    def __str__(self):
        return self.role

    def toString():
        return "Eveque"

    def getTurnOrder():
        return 5

    def action(self):
        pass


class Marchand(Role):
    def __init__(self, player):
        super().__init__("Green")
        self.player = player
        self.role = "Marchand"
        self.turnOrder = 6

    def __str__(self):
        return self.role

    def toString():
        return "Marchand"

    def getTurnOrder():
        return 6

    def action(self):
        self.player.getMoney(1)


class Architecte(Role):
    def __init__(self, player):
        super().__init__("None")
        self.player = player
        self.role = "Architecte"
        self.turnOrder = 7

    def __str__(self):
        return self.role

    def toString():
        return "Architecte"

    def getTurnOrder():
        return 7

    def action(self):
        self.player.drawBuilding()
        self.player.drawBuilding()


class Condotiere(Role):
    def __init__(self, player):
        super().__init__("Red")
        self.player = player
        self.role = "Condotiere"
        self.turnOrder = 8

    def __str__(self):
        return self.role

    def toString():
        return "Condotiere"

    def getTurnOrder():
        return 8

    def action(self):
        pass


class RoleDeck(Deck):
    def __init__(self):
        super().__init__()
        self.deck = [Assassin, Voleur, Magicien, Roi, Eveque, Marchand, Architecte]
        self.middle = []

    def __str__(self):
        string = ""
        for i, role in enumerate(self.deck):
            string += str(i + 1) + " - " + role.toString() + "\n"

        return string

    def __getitem__(self, index):
        return self.deck[index]

    def getTurnOrder(self, role):
        return role.getTurnOrder()

    def sort(self):
        self.deck.sort(key=self.getTurnOrder)

    def showAssassin(self):
        """Shows every roles minus the one face up in the middle and the assassin."""
        string = ""
        for i, role in enumerate(self.deck):
            if role.toString() != "Assassin" and role not in self.middle:
                string += str(i + 1) + " - " + role.toString() + "\n"
        print(string)

    def showVoleur(self):
        """Shows every roles minus the one face up in the middle and the assassin and the voleur."""
        string = ""
        for i, role in enumerate(self.deck):
            if role.toString() != "Assassin" and role.toString() != "Voleur" and role not in self.middle:
                string += str(i + 1) + " - " + role.toString() + "\n"
        print(string)

    def reset(self):
        self.deck = [Assassin, Voleur, Magicien, Roi, Eveque, Marchand, Architecte]

    def startGame(self):
        self.shuffle()
        middle = self.draw()
        if middle == Roi:
            self.reset()
            self.startGame()
        else:
            print("There is no " + middle.toString())