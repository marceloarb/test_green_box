from class1 import math
import unittest

class TestArray(unittest.TestCase):
    def test_iterate(self):
        self.assertEqual(math.iterate([3,4,5,6]),[3,4,5,6]) 


if __name__ == '__main__':
    unittest.main()