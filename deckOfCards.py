import card

class deckOfCards():
    def __init__(self):
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        values = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    def create_deck(self):
        print(suits)
        for suit in suits:
            for value in values:
                self.append( card(suit,value))

