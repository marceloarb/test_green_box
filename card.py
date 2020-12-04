class Card:
    """A class modeled for a Card"""

    def __init__(self, rank, suit):
        """Initialize rank and suit attributes"""

        self.rank = rank
        self.suit = suit

    def return_card(self):
        return f"{self.rank} of {self.suit}"