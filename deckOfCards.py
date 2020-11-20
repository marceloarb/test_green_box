from random import shuffle 

class deckOfCards:
    def __init__(self):
        self.deck = []
        self.suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self.values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    def create_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append(value +" "+ suit)
    def shuffle_deck(self):
        if len(self.deck) < 52:
            print("Cannot shuffle the cards")
        else:
            shuffle(self.deck)
    def get_deck(self):
        self.create_deck()
        self.shuffle_deck()            
