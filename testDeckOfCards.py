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
    def test_Only_Have_One_Deck(self):
        expected = 48
        user1 = card().user_hand_texas_holden()
        user2 = card().user_hand_texas_holden()
        actual = len(card().deck_of_cards)
        self.assertEqual(actual,expected)
    def test_Shuffle_Deck_Of_Cards(self):
        expected = deckOfCards().deck
        actual = deckOfCards().shuffle_deck()
        self.assertNotEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()
        
    
    
    