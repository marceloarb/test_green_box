import unittest
from deckOfCards import deckOfCards

class TestDeckCards(unittest.TestCase):
    def test_Deck_Of_Cards_Count(self):
        expected = 52
        length = len(deckOfCards().create_deck())
        actual = length
        self.assertEqual(actual,expected)