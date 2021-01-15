import unittest
from decimal import Decimal

from is_perfect_square import is_perfect_square


class IsPerfectSquareTests(unittest.TestCase):

    """Tests for is_perfect_square."""

    def test_small_number(self):
        self.assertTrue(is_perfect_square(1))
        self.assertTrue(is_perfect_square(4))
        self.assertFalse(is_perfect_square(8))
        self.assertFalse(is_perfect_square(35))

    def test_4_digit_number(self):
        self.assertTrue(is_perfect_square(5776))
        self.assertFalse(is_perfect_square(9306))

    def test_big_number(self):
        self.assertTrue(is_perfect_square(1586375448590241))
        self.assertFalse(is_perfect_square(1420958445736851))

    def test_non_real_numbers(self):
        self.assertFalse(is_perfect_square(4.5))
        with self.assertRaises(TypeError):
            is_perfect_square(1j)
        with self.assertRaises(TypeError):
            is_perfect_square('hello')

    def test_decimal_number(self):
        square_number = Decimal('100')
        self.assertTrue(is_perfect_square(square_number))
        self.assertFalse(is_perfect_square(square_number-1))
        self.assertFalse(is_perfect_square(square_number+1))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_negative_numbers(self):
        square_number = -4
        self.assertFalse(is_perfect_square(square_number))
        self.assertFalse(is_perfect_square(square_number-1))
        self.assertFalse(is_perfect_square(square_number+1))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_really_big_numbers(self):
        n = 838382848348234**2
        m = n**2
        m = 8383828483252752341748234**2
        self.assertTrue(is_perfect_square(n))
        self.assertFalse(is_perfect_square(n-1))
        self.assertFalse(is_perfect_square(n+1))
        self.assertTrue(is_perfect_square(m))
        self.assertFalse(is_perfect_square(m-1))
        self.assertFalse(is_perfect_square(m+1))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_complex_numbers(self):
        self.assertTrue(is_perfect_square(-4, complex=True))
        self.assertTrue(is_perfect_square(-100, complex=True))
        self.assertFalse(is_perfect_square(-1000, complex=True))
        self.assertTrue(is_perfect_square(512j, complex=True))
        self.assertFalse(is_perfect_square(100j, complex=True))
        self.assertTrue(is_perfect_square(-5+12j, complex=True))
        with self.assertRaises(TypeError):
            is_perfect_square(-4, True)  # complex must be a keyword argument


if __name__ == "__main__":
    unittest.main()
