import unittest

from comparator import Comparator


class ComparatorTests(unittest.TestCase):

    """Tests for Comparator."""

    def test_equality_with_delta(self):
        self.assertEqual(5.5, Comparator(6, delta=0.5))
        self.assertEqual(6.5, Comparator(6, delta=0.5))
        self.assertNotEqual(6.51, Comparator(6, delta=0.5))
        self.assertNotEqual(5.49, Comparator(6, delta=0.5))

    def test_equality_with_default_delta(self):
        self.assertEqual(Comparator(5), 4.99999999)
        self.assertEqual(Comparator(5), 5.00000001)
        self.assertEqual(5, Comparator(4.99999999))
        self.assertEqual(5, Comparator(5.00000001))
        self.assertNotEqual(Comparator(5), 4.99999)
        self.assertNotEqual(Comparator(5), 5.00001)

    def test_negative_numbers(self):
        self.assertNotEqual(-5.5, Comparator(-6, delta=0.25))
        self.assertEqual(-5.75, Comparator(-6, delta=0.25))
        self.assertEqual(-6.25, Comparator(-6, delta=0.25))
        self.assertNotEqual(-6.3, Comparator(-6, delta=0.25))

    def test_very_small_delta(self):
        self.assertEqual(-6.000000000000001, Comparator(-6, delta=1e-15))
        self.assertNotEqual(-6.000000000000002, Comparator(-6, delta=1e-15))

    def test_string_representation(self):
        self.assertEqual(
            repr(Comparator(5, delta=0.1)),
            "Comparator(5, delta=0.1)",
        )
        self.assertEqual(repr(Comparator(5)), "Comparator(5, delta=1e-07)")
        self.assertEqual(str(Comparator(5)), "Comparator(5, delta=1e-07)")

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_addition_and_subtraction(self):
        self.assertEqual(Comparator(5, delta=0.1) + 6, 11.1)
        self.assertEqual(6 + Comparator(5, delta=0.1), 10.9)
        self.assertNotEqual(Comparator(5, delta=0.1) + 6, 11.2)
        self.assertNotEqual(6 + Comparator(5, delta=0.1) + 6, 10.8)
        self.assertEqual(Comparator(7, delta=0.1) - 6, 1.05)
        self.assertNotEqual(Comparator(7, delta=0.1) - 6, 1.2)
        self.assertEqual(7 - Comparator(7, delta=0.1), 0.05)
        self.assertNotEqual(7 - Comparator(7, delta=0.1), 0.11)
        self.assertEqual(6 - Comparator(7, delta=0.1), -1.05)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_arithmetic_and_comparisons_with_comparators(self):
        five = Comparator(5, delta=0.1)
        six = Comparator(6, delta=0.1)
        seven = Comparator(7, delta=0.5)
        self.assertEqual(five + six, 11.1)
        self.assertNotEqual(five + six, 11.2)
        self.assertEqual(five + seven, 12.1)
        self.assertEqual(five + seven, 12.5)
        self.assertEqual(seven + five, 12.5)
        self.assertNotEqual(five + seven, 12.6)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_default_delta_context_manager(self):
        with Comparator.default_delta(0.5):
            self.assertEqual(Comparator(5), 5.5)
            self.assertNotEqual(Comparator(5), 5.6)
            self.assertNotEqual(Comparator(5, delta=0.1), 5.5)
        self.assertNotEqual(Comparator(5), 5.5)
        try:
            with Comparator.default_delta(0.5):
                raise ValueError
        except ValueError:
            pass
        self.assertNotEqual(Comparator(5), 5.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
