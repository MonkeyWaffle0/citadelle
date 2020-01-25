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