import unittest
import deckOfCards

class TestDeckCards(unittest.TestCase):
    def test_Deck_Of_Cards_Count(self):
        expected = 52
        actual = deckOfCards.deckOfCards.create_deck()
        self.assertEqual(actual,expected)