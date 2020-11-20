
class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    def add_cards(self, cards):
        self.hand.add_cards(cards)