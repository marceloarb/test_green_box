import unittest
from card import card

class TestCard(unittest.TestCase):
    def test_card_hand(self):
        expected = 2
        actual = card().user_hand_texas_holden()
        actual = len(actual)
        self.assertEqual(actual,expected)
