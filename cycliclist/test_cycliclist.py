import unittest


from cycliclist import CyclicList


class CyclicListTests(unittest.TestCase):

    """Tests for CyclicList."""

    def test_constructor(self):
        CyclicList([1, 2, 3, 4])

    def test_accepts_non_lists(self):
        numbers = CyclicList({1, 2, 3})
        self.assertEqual(next(iter(numbers)), 1)
        letters = CyclicList('hello')
        self.assertEqual(next(iter(letters)), 'h')

    def test_iterate_to_length(self):
        numbers = CyclicList([1, 2, 3])
        i = iter(numbers)
        self.assertEqual([next(i), next(i), next(i)], [1, 2, 3])

    def test_iterate_past_length(self):
        numbers = CyclicList([1, 2, 3])
        new_list = [x for x, _ in zip(numbers, range(10))]
        self.assertEqual(new_list, [1, 2, 3, 1, 2, 3, 1, 2, 3, 1])

    def test_iterators_are_independent(self):
        numbers = CyclicList([1, 2, 3, 4])
        i1 = iter(numbers)
        i2 = iter(numbers)
        self.assertEqual(next(i1), 1)
        self.assertEqual(next(i1), 2)
        self.assertEqual(next(i2), 1)
        self.assertEqual(next(i2), 2)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_length_append_and_pop(self):
        numbers = CyclicList([1, 2, 3])
        self.assertEqual(len(numbers), 3)
        numbers.append(4)
        self.assertEqual(numbers.pop(), 4)
        self.assertEqual(numbers.pop(0), 1)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_supports_indexing(self):
        numbers = CyclicList([1, 2, 3, 4])
        self.assertEqual(numbers[2], 3)
        numbers = CyclicList([1, 2, 3, 4])
        self.assertEqual(numbers[4], 1)
        self.assertEqual(numbers[-1], 4)
        numbers[5] = 0
        self.assertEqual(numbers[1], 0)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_slice(self):
        numbers = CyclicList([1, 2, 3, 4, 5])
        self.assertEqual(numbers[:7], [1, 2, 3, 4, 5, 1, 2])
        self.assertEqual(numbers[-3:], [3, 4, 5])
        self.assertEqual(numbers[-10:0], [1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
        self.assertEqual(numbers[-1:9], [5, 1, 2, 3, 4, 5, 1, 2, 3, 4])
        self.assertEqual(numbers[:], [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main(verbosity=2)
