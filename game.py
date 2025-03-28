from deck import Deck, Card

class Hand:
    """
    A class to represent a poker hand consisting of 5 cards.
    """

    def __init__(self, deck):
        """
        Initializes the Hand object by dealing 5 cards from the given deck.
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        Returns the list of 5 Card objects in the hand.
        """
        return self._cards

    def __str__(self):
        """
        Returns the string representation of the hand.
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Checks if all cards in the hand have the same suit (i.e., the hand is a flush).
        Returns True if all suits match, False otherwise.
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

# Continuously generate and check hands until a flush is found
while True:
    deck = Deck()        # Create a new shuffled deck
    deck.shuffle()
    hand = Hand(deck)    # Deal a new hand
    if hand.is_flush:    # Check if the hand is a flush
        print(hand)      # If flush, print the hand
        break            # Stop the loop once a flush is found