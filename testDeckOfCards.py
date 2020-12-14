import unittest
from deckOfCards import Deck


class TestDeckCards(unittest.TestCase):
    def test_Deck_Of_Cards_Count(self):
        expected = 52
        length = len(Deck().cards)
        actual = length
        self.assertEqual(actual,expected)
    #Ask Josh if you can check if the deck of cards empty can be checked like that or if we need to check the same function like the one above.
    
    def test_Deck_Is_Shuffled(self):
        expected = Deck().cards
        actual = Deck().shuffle()
        actual = Deck().cards
        self.assertNotEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()
        
    
    
    