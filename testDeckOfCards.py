import unittest
from deckOfCards import deckOfCards
from card import card


class TestDeckCards(unittest.TestCase):
    def test_Deck_Of_Cards_Count(self):
        expected = 52
        length = len(deckOfCards().deck)
        actual = length
        self.assertEqual(actual,expected)
    #Ask Josh if you can check if the deck of cards empty can be checked like that or if we need to check the same function like the one above.
    

if __name__ == '__main__':
    unittest.main()
        
    
    
    