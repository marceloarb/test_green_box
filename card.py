from deckOfCards import deckOfCards

class card:
    def __init__(self):
        pass
    def user_hand_texas_holden(self):
        hand = []
        deckOfCards().create_deck()
        deck_of_cards = deckOfCards().getDeck()
        hand.append(deck_of_cards.pop(len(deck_of_cards)-1))
        hand.append(deck_of_cards.pop(len(deck_of_cards)-1))
        return hand


    
    