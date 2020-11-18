from deckOfCards import deckOfCards

class card:
    def __init__(self):
        self.deck_of_cards = deckOfCards().create_deck()
    def user_hand_texas_holden(self):
        hand = []
        hand.append(self.deck_of_cards.pop(len(self.deck_of_cards)-1))
        hand.append(self.deck_of_cards.pop(len(self.deck_of_cards)-1))
        return hand


    
    