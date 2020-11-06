from card import card

class deckOfCards:
    def __init__(self):
        self.suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self.values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    def create_deck(self):
        deck = []
        for suit in self.suits:
            for value in self.values:
                deck.append(value +" "+ suit)
        return deck
    
p1 = deckOfCards()

print(p1.create_deck())
