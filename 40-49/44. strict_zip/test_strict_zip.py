import unittest
from itertools import count, repeat

from strict_zip import strict_zip


class StrictZipTests(unittest.TestCase):

    """Tests for strict_zip."""

    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_empty_sequences(self):
        self.assertIterableEqual(strict_zip([]), [])
        self.assertIterableEqual(strict_zip([], [], [], []), [])
        self.assertIterableEqual(strict_zip(), [])

    def test_with_two_sequences(self):
        self.assertIterableEqual(
            strict_zip([1], ['a']),
            [(1, 'a')],
        )
        self.assertIterableEqual(
            strict_zip((1, 2, 3), 'abc'),
            [(1, 'a'), (2, 'b'), (3, 'c')]
        )

    def test_with_three_sequences(self):
        self.assertIterableEqual(
            strict_zip([1.1, 2.2, 3.3], ['i', 'ii', 'iii']),
            [(1.1, 'i'), (2.2, 'ii'), (3.3, 'iii')],
        )
        self.assertIterableEqual(
            strict_zip(range(5), ('abcde'), list(range(10, 15))),
            [(0, 'a', 10), (1, 'b', 11), (2, 'c', 12), (3, 'd', 13), (4, 'e', 14)],
        )

    def test_with_many_sequences(self):
        self.assertIterableEqual(
            strict_zip([1, 2], [3, 4], [5, 6], [7, 8]),
            [(1, 3, 5, 7), (2, 4, 6, 8)]
        )

    def test_with_none_values(self):
        self.assertIterableEqual(
            strict_zip([None, None], [None, None]),
            [(None, None), (None, None)],
        )

    def test_unequal_length(self):
        with self.assertRaises(ValueError):
            list(strict_zip(['a', 'b', 'c'], [10, 22, 56, 78]))
        with self.assertRaises(ValueError):
            list(strict_zip('here', 'are', 'four', 'sequences'))
        with self.assertRaises(ValueError):
            list(strict_zip([1, 2, 3, 4], [5, 6, 7]))
        with self.assertRaises(ValueError):
            list(strict_zip([None, None], [None, None, None]))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_non_indexable_iterables(self):
        numbers = range(5)
        squares = (n**2 for n in numbers)
        cubes = (n**3 for n in numbers)
        self.assertIterableEqual(
            strict_zip(numbers, squares, cubes),
            [(0, 0, 0), (1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64)],
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_iterator(self):
        z1 = strict_zip(range(10, 15))
        self.assertEqual(next(z1), (10,))
        self.assertEqual(next(z1), (11,))
        self.assertIterableEqual(z1, [(12,), (13,), (14,)])

        z2 = strict_zip(range(10, 15), [n**2 for n in range(10, 15)])
        self.assertEqual(next(z2), (10, 100))
        self.assertEqual(next(z2), (11, 121))
        self.assertIterableEqual(z2, [(12, 144), (13, 169), (14, 196)])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_with_lazy_iterators(self):
        # Ensure looping happens lazily
        numbers = [1, 2, 'a']
        squares = (n**2 for n in numbers)
        zipped = strict_zip(numbers, squares)
        self.assertEqual(next(zipped), (1, 1))
        self.assertEqual(next(zipped), (2, 4))
        with self.assertRaises(TypeError):
            next(zipped)  # 'a' not squared until this point

        # Test an infinite iterable and a finite one
        one_infinite = strict_zip([1, 2, 3], count(10))
        self.assertIterableEqual(next(one_infinite), (1, 10))
        self.assertIterableEqual(next(one_infinite), (2, 11))
        self.assertIterableEqual(next(one_infinite), (3, 12))
        with self.assertRaises(ValueError):
            next(one_infinite)

        # Test all infinite iterables
        both_infinite = strict_zip(repeat(2), count())
        self.assertIterableEqual(next(both_infinite), (2, 0))
        self.assertIterableEqual(next(both_infinite), (2, 1))
        self.assertIterableEqual(next(both_infinite), (2, 2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
