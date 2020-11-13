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
        return self.deck
    def shuffle_deck(self):
        self.create_deck()
        if len(self.deck) < 52:
            print("Cannot shuffle the cards")
        else:
            shuffle(self.deck)
            return self.deck
    def getDeck(self):
        self.create_deck()
        deck = self.shuffle_deck()
        return deck
