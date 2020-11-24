
class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    def add_cards(self, cards):
        print(self.deck_of_cards)
        hand = []
        hand.append(self.deck_of_cards.pop(len(self.deck_of_cards)-1))
        hand.append(self.deck_of_cards.pop(len(self.deck_of_cards)-1))
        return hand