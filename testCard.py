import unittest
from card import card

class TestCard(unittest.TestCase):
    def test_card_hand_length(self):
        expected = 2
        actual = card().user_hand_texas_holden()
        actual = len(actual)
        self.assertEqual(actual,expected)
    def test_card_hand_is_random(self):
        expected = card().user_hand_texas_holden()
        actual = card().user_hand_texas_holden()
        self.assertNotEqual(actual,expected)
