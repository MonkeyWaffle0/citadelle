from classes.Role import *
from classes.Building import *

class Deck:
    """Abstract class of a deck of card"""
    def __init__(self):
        self.deck = []

    def add(self, card):
        self.deck.append(card)

    def shuffle(self):
        """Shuffles the deck"""
        for i in range(len(self.deck)):
            otherCard = random.randrange(len(self.deck))
            temp = self.deck[i]
            self.deck[i] = self.deck[otherCard]
            self.deck[otherCard] = temp

    def draw(self):
        """Draw the next card in the deck, increment the currentCard variable."""
        card = self.deck[0]
        self.remove(card)
        return card

    def remove(self, card):
        """Remove the card from the deck."""
        if card in self.deck:
            self.deck.remove(card)
        else:
            print("The card is not in the deck.")


class BuildingDeck(Deck):
    def __init__(self):
        super().__init__()
        card1 = Building("Red", "Prison", 2, 2)
        card2 = Building("Green", "Echoppe", 2, 2)
        card3 = Building("Yellow", "Chateau", 5, 5)

        self.add(card1)
        self.add(card2)
        self.add(card3)


class RoleDeck(Deck):
    def __init__(self):
        super().__init__()
        self.deck = [Assassin, Voleur, Magicien, Roi, Eveque, Marchand, Architecte, Condotiere]
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