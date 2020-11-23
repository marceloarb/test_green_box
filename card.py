from deckOfCards import deckOfCards

class card():
    SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")
    RANKS = (
                "2", "3", "4", "5", "6", "7", "8", "9", "10", 
                "Jack", "Queen", "King", "Ace"
            )
    def user_hand_texas_holden(self):
        print(self.deck_of_cards)
        hand = []
        hand.append(self.deck_of_cards.pop(len(self.deck_of_cards)-1))
        hand.append(self.deck_of_cards.pop(len(self.deck_of_cards)-1))
        return hand


    
    