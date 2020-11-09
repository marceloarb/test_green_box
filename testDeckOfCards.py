import unittest
from deckOfCards import deckOfCards

class TestDeckCards(unittest.TestCase):
    def test_Deck_Of_Cards_Count(self):
        expected = 52
        length = len(deckOfCards().create_deck())
        actual = length
        self.assertEqual(actual,expected)
    #Ask Josh if you can check if the deck of cards empty can be checked like that or if we need to check the same function like the one above.
    def test_Deck_Of_Cards_Empty(self):
        expected = 0
        length = len(deckOfCards().deck)
        actual = length
        self.assertEqual(actual,expected)
    def test_Shuffle_Deck_Of_Cards(self):
        expected = deckOfCards().create_deck()
        actual = deckOfCards().shuffle_deck()
        self.assertNotEqual(actual,expected)
    
    
    