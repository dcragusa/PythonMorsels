import sys
import unittest
from collections.abc import Generator

from sliceview import SliceView


class SliceViewTests(unittest.TestCase):

    """Tests for SliceView."""

    def test_no_start_or_stop(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = SliceView(numbers)
        self.assertEqual(list(view), numbers)
        self.assertIsNot(view, numbers)
        self.assertNotEqual(type(view), list)
        self.assertNotEqual(type(view), tuple)

    def test_stop_but_no_start(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = SliceView(numbers, stop=4)
        self.assertEqual(list(view), [2, 1, 3, 4])

    def test_start_but_no_stop(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = SliceView(numbers, start=2)
        self.assertEqual(list(view), [3, 4, 7, 11, 18])

    def test_start_and_stop(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = SliceView(numbers, start=1, stop=5)
        self.assertEqual(list(view), [1, 3, 4, 7])

    def test_no_memory_used(self):
        numbers = range(1000000)
        view = SliceView(numbers, start=1, stop=5)
        if isinstance(view, Generator):
            next(view)
            size = sum(
                sys.getsizeof(obj)
                for obj in view.gi_frame.f_locals.values()
            )
        else:
            size = sys.getsizeof(view)
        self.assertLess(size, 8000, 'Too much memory used')
        self.assertNotEqual(type(view), list)
        self.assertNotEqual(type(view), tuple)

    def test_does_not_slice_sequence(self):
        class UnsliceableList(list):
            def __getitem__(self, index):
                if not isinstance(index, int):
                    return NotImplemented
                return super().__getitem__(index)
        numbers = UnsliceableList([2, 1, 3, 4, 7, 11, 18])
        view = SliceView(numbers, stop=5)
        self.assertEqual(list(view), [2, 1, 3, 4, 7])

    def test_negative_start(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = SliceView(numbers, start=-3)
        self.assertEqual(list(view), [7, 11, 18])

    def test_negative_stop(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = SliceView(numbers, stop=-2)
        self.assertEqual(list(view), [2, 1, 3, 4, 7])

    def test_out_of_range(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = SliceView(numbers, start=-100)
        self.assertEqual(list(view), [2, 1, 3, 4, 7, 11, 18])
        view = SliceView(numbers, stop=100)
        self.assertEqual(list(view), [2, 1, 3, 4, 7, 11, 18])

    def test_negative_step(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = SliceView(numbers, step=-1)
        self.assertEqual(list(view), [18, 11, 7, 4, 3, 1, 2])
        view = SliceView(numbers, stop=1, step=-2)
        self.assertEqual(list(view), [18, 7, 3])

    # @unittest.expectedFailure
    def test_looping_multiple_times(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = SliceView(numbers, start=2)
        self.assertEqual(list(view), [3, 4, 7, 11, 18])
        self.assertEqual(list(view), [3, 4, 7, 11, 18])

    # @unittest.expectedFailure
    def test_has_length(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        self.assertEqual(len(SliceView(numbers, stop=4)), 4)
        self.assertEqual(len(SliceView(numbers, start=2)), 5)
        self.assertEqual(len(SliceView(numbers, start=1, stop=5)), 4)
        self.assertEqual(len(SliceView(numbers, start=-3)), 3)
        self.assertEqual(len(SliceView(numbers, stop=-2)), 5)
        self.assertEqual(len(SliceView(numbers, start=-100)), 7)
        self.assertEqual(len(SliceView(numbers, stop=100)), 7)
        self.assertEqual(len(SliceView(numbers, step=-1)), 7)
        self.assertEqual(len(SliceView(numbers, stop=1, step=-2)), 3)

    # @unittest.expectedFailure
    def test_slicing_and_indexing(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = SliceView(numbers)
        self.assertEqual(list(view[2:]), [3, 4, 7, 11, 18])
        self.assertEqual(list(view[:-1]), [2, 1, 3, 4, 7, 11])
        self.assertEqual(list(view[::-1]), [18, 11, 7, 4, 3, 1, 2])
        self.assertEqual(type(view[::-1]), SliceView)
        self.assertEqual(view[::-1][1], 11)
        self.assertEqual(view[::-1][-2], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
