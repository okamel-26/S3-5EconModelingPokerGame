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

@property
def is_pair(self):
    """
    Checks if the hand contains exactly one pair (two cards of the same rank).
    The method counts how many times ranks match in different positions.
    A valid single pair results in exactly two matches.
    Returns True if the hand has a single pair, otherwise False.
    """
    matches = 0
    for c1 in self.cards:
        for c2 in self.cards:
            if c1 == c2:
                continue
    for i in range(5):
        for j in range(5):
            if i == j:
                continue
            if self.cards[i].rank == self.cards[j].rank:
                matches += 1
    if matches == 2:
        return True
    return False

matches = 0
count = 0

# Continuously generate and check hands until 100 flushes are found
while matches < 1000:
    deck = Deck()        # Create a new shuffled deck
    deck.shuffle()
    hand = Hand(deck)    # Deal a new hand
    count += 1           # Increment total number of hands checked
    if hand.is_flush:    # Check if the hand is a flush
        matches += 1     # Count the flush

# Calculate and print probability
print(f"The probability of a flush is {100 * matches / count}%")