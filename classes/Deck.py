from classes.Role import *
from classes.Building import *
from BUILDINGS import *

import random


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
        self.deck = [
            PALAIS, PALAIS, PALAIS,
            MANOIR, MANOIR, MANOIR, MANOIR, MANOIR,
            CHATEAU, CHATEAU, CHATEAU, CHATEAU,
            TOUR_DE_GUET, TOUR_DE_GUET, TOUR_DE_GUET,
            FORTERESSE, FORTERESSE,
            PRISON, PRISON, PRISON,
            CASERNE, CASERNE, CASERNE,
            CATHEDRALE, CATHEDRALE,
            TEMPLE, TEMPLE, TEMPLE,
            MONASTERE, MONASTERE, MONASTERE,
            EGLISE, EGLISE, EGLISE,
            COMPTOIR, COMPTOIR, COMPTOIR,
            TAVERNE, TAVERNE, TAVERNE, TAVERNE,
            MARCHE, MARCHE, MARCHE, MARCHE,
            PORT, PORT, PORT,
            HOTEL_DE_VILLE, HOTEL_DE_VILLE,
            ECHOPPE, ECHOPPE, ECHOPPE
        ]


class RoleDeck(Deck):
    def __init__(self):
        super().__init__()
        assassin = Assassin()
        voleur = Voleur()
        magicien = Magicien()
        roi = Roi()
        eveque = Eveque()
        marchand = Marchand()
        architecte = Architecte()
        condotiere = Condotiere()
        self.deck = [assassin, voleur, magicien, roi, eveque, marchand, architecte, condotiere]
        self.middle = []   # Roles in the middle of the table

    def __str__(self):
        string = ""
        for i, role in enumerate(self.deck):
            string += str(i + 1) + " - " + str(role) + "\n"

        return string

    def __getitem__(self, index):
        return self.deck[index]

    def getTurnOrder(self, role):
        return role.turnOrder()

    def sort(self):
        self.deck.sort(key=self.getTurnOrder)

    def showAssassin(self):
        """Shows every roles minus the one face up in the middle and the assassin."""
        string = ""
        for i, role in enumerate(self.deck):
            if role.role != "Assassin" and role not in self.middle:
                string += str(i + 1) + " - " + str(role) + "\n"
        print(string)

    def showVoleur(self):
        """Shows every roles minus the one face up in the middle and the assassin and the voleur."""
        string = ""
        for i, role in enumerate(self.deck):
            if role.role != "Assassin" and role.role != "Voleur" and role not in self.middle:
                string += str(i + 1) + " - " + str(role) + "\n"
        print(string)

    def reset(self):
        assassin = Assassin()
        voleur = Voleur()
        magicien = Magicien()
        roi = Roi()
        eveque = Eveque()
        marchand = Marchand()
        architecte = Architecte()
        condotiere = Condotiere()
        self.deck = [assassin, voleur, magicien, roi, eveque, marchand, architecte, condotiere]

    def startGame(self):
        self.shuffle()
        middle = self.draw()
        if middle == Roi:
            self.reset()
            self.startGame()
        else:
            print("There is no " + middle.role)