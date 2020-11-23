from random import shuffle 

class deckOfCards:
    def __init__(self):
        pass
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
