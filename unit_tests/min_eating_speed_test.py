import unittest

from algo_functions.lab2.min_eating_speed import min_eating_speed


class TestMinEatingSpeed(unittest.TestCase):
    def test_example_1(self):
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(min_eating_speed(piles, h), 4)

    def test_example_2(self):
        piles = [30, 11, 23, 4, 20]
        h = 5
        self.assertEqual(min_eating_speed(piles, h), 30)

    def test_example_3(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(min_eating_speed(piles, h), 23)

    def test_small_piles(self):
        piles = [1, 2, 3]
        h = 6
        self.assertEqual(min_eating_speed(piles, h), 1)


if __name__ == '__main__':
    unittest.main()
