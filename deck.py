import random

class Card:
    """
    A class to represent a playing card with a rank and suit.
    """

    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]
    # SUITS = ["clubs", "diamonds", "hearts", "spades"]

    def __init__(self, rank, suit):
        """
        Initializes a Card object with a given rank and suit.
        Raises ValueError if either rank or suit is invalid.
        """
        if rank not in self.RANKS:
            raise ValueError("invalid rank")
        if suit not in self.SUITS:
            raise ValueError("invalid suit")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """
        Returns the rank of the card.
        """
        return self._rank

    @property
    def suit(self):
        """
        Returns the suit of the card.
        """
        return self._suit

    def __str__(self):
        """
        Returns the string representation of the card (e.g., 'A♣').
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Returns the official string representation of the card.
        Same as __str__ in this implementation.
        """
        return self.__str__()  # repr is the same as str

class Deck:
    """
    A class to represent a standard deck of 52 playing cards.
    """

    def __init__(self):
        """
        Initializes the deck by creating 52 Card objects, one for each rank-suit combination.
        """
        _cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                _cards.append(Card(rank, suit))
        self._cards = _cards

    @property
    def cards(self):
        """
        Returns the list of Card objects in the deck.
        """
        return self._cards

    def __str__(self):
        """
        Returns the string representation of the entire deck.
        """
        return str(self._cards)

    def shuffle(self):
        """
        Shuffles the deck using the random.shuffle function.
        """
        random.shuffle(self.cards)

    def deal(self):
        """
        Removes and returns the top card from the deck.
        """
        return self.cards.pop(0)

if __name__ == "__main__":
    # Demonstrates usage of Card and Deck classes
    c1 = Card("A", "♣")
    print(c1.suit, c1.rank)  # Prints the suit and rank of a single card

    deck = Deck()            # Creates a new deck of cards
    print(deck)              # Prints the ordered deck
    deck.shuffle()           # Shuffles the deck
    print(deck)              # Prints the shuffled deck
    print(deck.deal())       # Deals the top card from the deck
    print(deck)              # Prints the deck after dealing one card