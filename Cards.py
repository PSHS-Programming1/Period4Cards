import random

class Card(object):
    """Create a card base on rank and suit"""
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["S","C","H","D"]

    def __init__(self, rank:str, suit:str, isFaceUp = True):
        self.rank = rank
        self.suit = suit
        self.card = (rank, suit)
        self.isFaceUp = isFaceUp

    def __str__(self):
        if self.isFaceUp:
            output = self.rank + "-" + self.suit
            return output
        else:
            return "XX"

    def flipCard(self):
        if self.isFaceUp:
            self.isFaceUp = False
        else:
            self.isFaceUp = True


class Hand(object):
    """This creates a hand of cards"""

    def __init__(self):
        """creates an empty hand"""
        self.cards = []

    def __str__(self):
        if len(self.cards) == 0:
            return "<Empty Hand>"
        output = ""
        for card in self.cards:
            output += "[" +card.__str__() + "] "
        return output

    def addCard(self,card:Card):
        """This will add a card to the hand"""
        self.cards.append(card)

    def giveCard(self, card:Card, otherHand):
        """removes card from current hand
        to add to other hand"""
        if card in self.cards:
            otherHand.addCard(card)
            self.cards.remove(card)
        else:
            print("can't give that card")

    def getCard(self, rank, suit):
        """return a card from the hand of a given
        rank and suit: None otherwise"""
        for card in self.cards:
            if card.rank == rank and card.suit == suit:
                return card
        return None

    def clearCards(self):
        """remove all cards from hand"""
        self.cards = []

class Deck(Hand):
    """Creates a deck that is a hand"""
    def __init__(self):
        super().__init__()

    def __str__(self):     #changed the __str__ function so it tells you how many cards the deck has left
        if len(self.cards) == 0:
            return "<Empty Deck>"
        elif len(self.cards) == 1:
            return "There is 1 card left in the deck"
        else:
            return "There are " + str(len(self.cards)) + " cards left in the deck"

    def createDeck(self):
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                deck.addCard(Card(rank, suit))

    def shuffle(self):
        for i in range(300):
            shuffledCard = random.choice(self.cards)
            self.cards.remove(shuffledCard)
            self.addCard(shuffledCard)

#I changed the testing to test how the deck interacts with the hands
hand = Hand()
otherHand = Hand()
thirdHand = Hand()
print("hand:", hand)      #hand is temporary and a name should be passed by parameters to hand later
print("otherHand:", otherHand)
print("thirdHand:", thirdHand)
deck = Deck()
deck.createDeck()
deck.shuffle()
print(deck)
for i in range(7):
    deck.giveCard(deck.getCard(deck.cards[0].rank, deck.cards[0].suit), hand)          #deals 7 cards to each hand
    deck.giveCard(deck.getCard(deck.cards[0].rank, deck.cards[0].suit), otherHand)
    deck.giveCard(deck.getCard(deck.cards[0].rank, deck.cards[0].suit), thirdHand)
print("hand:", hand)
print("otherHand:", otherHand)
print("thirdHand:",thirdHand)
print(deck)
