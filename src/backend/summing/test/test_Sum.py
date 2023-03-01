import unittest

from backend.summing.Sum import Sum

class testSum(unittest.TestCase):
    
    def setUp(self):
        self.Sum = Sum()
    
    def test_1_plus_1(self):
        expected = 2
        actual = self.Sum.sum(1, 1)
        self.assertEqual(expected, actual)

    def test_2_plus_2(self):
        expected = 4
        actual = self.Sum.sum(2, 2)
        self.assertEqual(expected, actual)

    def test_0_plus_0(self):
        expected = 0
        actual = self.Sum.sum(0, 0)
        self.assertEqual(expected, actual)
    
    def test_minus_1_plus_1(self):
        expected = 0
        actual = self.Sum.sum(-1, 1)
        self.assertEqual(expected, actual)

    def test_minus_1_plus_minus_1(self):
        expected = -2
        actual = self.Sum.sum(-1, -1)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()