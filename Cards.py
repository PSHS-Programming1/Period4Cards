from Cards import *
import random

class Deck(object):
    """Creates the deck"""


    def __init__(self, cardCounter):
        """this is like a counter almost"""
        self.cardCounter = cardCounter


    def __str__(self):
        """this is the info"""
        info = "Number of cards in the deck" + str(self.cardCounter)


    def get_cardCounter(self):
        """Counts the number of cards in a deck"""


    def createDeck(self):
        """Creates a deck of cards"""
        cardz = []
        cardCounter = 0
        for i in Card.SUITS:
            for j in Card.RANKS:
                card = Card(j, i)
                cardz += card
                cardCounter += 1
        return cardz


hand1 = Hand()
deck1 = Deck(52)
deck1.createDeck()
hand1.addCard(deck1)
print(hand1)
print(deck1)
#self.createDeck(deck1 = Deck(52))
#print(deck1)
#Deck.createDeck()
#print(Deck)




