from deckOfCards import deckOfCards

class card:
    def __init__(self):
        pass
    def user_hand_texas_holden(self):
        hand = []
        create_deck = deckOfCards().create_deck()
        deck_of_cards = deckOfCards().shuffle_deck()
        hand.append(deck_of_cards.pop(len(deck_of_cards)-1))
        hand.append(deck_of_cards.pop(len(deck_of_cards)-1))
        return hand


    
    