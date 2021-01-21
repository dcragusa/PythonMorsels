import unittest
from random import randint
from timeit import default_timer

from minheap import MinHeap

BIG_NUMBERS = [
    3748, 7250, 140, 7669, 5711, 2284, 3322, 6435, 8138, 6920, 9634, 7511,
    5295, 5456, 7458, 5618, 102, 7747, 4638, 46, 4532, 1483, 944, 3542, 6641,
    9091, 693, 836, 3099, 3385, 7798, 758, 8407, 4756, 8801, 3936, 5301, 5744,
    6454, 1156, 7686, 5664, 2568, 6414, 3469, 2867, 8875, 6097, 2546, 4658,
    7027, 9437, 755, 8536, 8186, 9539, 661, 6706, 265, 2254, 2402, 3355, 9141,
    5091, 1727, 6739, 4599, 5599, 9007, 2925, 2894, 5333, 9586, 7409, 916,
    6420, 8493, 9531, 5083, 5350, 3346, 1378, 6260, 3143, 7216, 684, 170, 6721,
    418, 7013, 7729, 7484, 5355, 4850, 8073, 1389, 2084, 1856, 9740, 2747,
]
MANY_BIG_NUMBERS = [randint(100, 1000) for n in range(10000)]


class MinHeapTests(unittest.TestCase):

    """Tests for MinHeap."""

    def test_create_heap(self):
        MinHeap([322, 76, 4, 7, 2, 123, 47, 1, 18, 3, 29, 199, 11])
        MinHeap(BIG_NUMBERS)

    def test_length(self):
        numbers = [322, 76, 4, 7, 2, 123, 47, 1, 18, 3, 29, 199, 11]
        self.assertEqual(len(MinHeap(numbers)), len(numbers))
        self.assertEqual(len(MinHeap(BIG_NUMBERS)), len(BIG_NUMBERS))

    def test_peek_at_smallest(self):
        numbers = [11, 322, 3, 199, 29, 7, 1, 18, 76, 4, 2, 47, 123]
        h = MinHeap(numbers)
        self.assertEqual(h.peek(), 1)
        self.assertEqual(len(h), len(numbers))
        self.assertEqual(len(numbers), 13)
        i = MinHeap(BIG_NUMBERS)
        self.assertEqual(i.peek(), 46)
        self.assertEqual(len(i), len(BIG_NUMBERS))

    def test_pop_from_heap(self):
        numbers = [11, 322, 3, 199, 29, 7, 1, 18, 76, 4, 2, 47, 123]
        h = MinHeap(numbers)
        self.assertEqual(h.pop(), 1)
        self.assertEqual(len(h), len(numbers)-1)
        self.assertEqual(h.pop(), 2)
        self.assertEqual(h.pop(), 3)
        self.assertEqual(h.pop(), 4)
        self.assertEqual(len(h), len(numbers)-4)
        self.assertEqual(h.pop(), 7)
        self.assertEqual(h.pop(), 11)
        self.assertEqual(len(h), len(numbers)-6)
        i = MinHeap(BIG_NUMBERS)
        self.assertEqual(i.pop(), 46)

    def test_push_onto_heap(self):
        numbers = [11, 322, 3, 199, 29, 7, 1, 18, 76, 4, 2, 47, 123]
        i = MinHeap(BIG_NUMBERS)
        i.push(17)
        self.assertEqual(i.peek(), 17)
        i.push(24)
        self.assertEqual(i.pop(), 17)
        self.assertEqual(i.pop(), 24)
        self.assertEqual(i.pop(), 46)
        h = MinHeap(numbers)
        h.push(6)
        self.assertEqual(len(h), len(numbers)+1)
        self.assertEqual(h.pop(), 1)
        self.assertEqual(h.pop(), 2)
        self.assertEqual(h.pop(), 3)
        self.assertEqual(h.pop(), 4)
        self.assertEqual(h.pop(), 6)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_faster_than_sorting(self):
        with Timer() as sort_timer:
            sorted(MANY_BIG_NUMBERS)
        heap = MinHeap(MANY_BIG_NUMBERS)
        with Timer() as min_heap_timer:
            heap.push(150)
            heap.push(950)
            heap.push(400)
            heap.push(760)
            heap.push(280)
            heap.push(870)
            heap.push(330)
            heap.push(1000)
            heap.push(50)
            heap.push(500)
            items = [heap.pop() for _ in range(10)]
        self.assertEqual(len(items), 10)
        self.assertLess(min_heap_timer.elapsed, sort_timer.elapsed)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_key_function(self):
        fruits = ['Watermelon', 'blueberry', 'lime', 'Lemon', 'pear', 'loquat']
        fruits_heap = MinHeap(fruits, key=str.lower)
        self.assertEqual(fruits_heap.peek(), 'blueberry')
        fruits_heap.push('Apple')
        fruits_heap.push('jujube')
        self.assertEqual(fruits_heap.pop(), 'Apple')
        self.assertEqual(fruits_heap.pop(), 'blueberry')
        self.assertEqual(fruits_heap.pop(), 'jujube')
        self.assertEqual(fruits_heap.pop(), 'Lemon')


# To test the Bonus part of this exercise, comment out the following line
# @unittest.expectedFailure
class MaxHeapTests(unittest.TestCase):

    """Tests for MaxHeap."""

    def test_create_heap(self):
        from minheap import MaxHeap
        MaxHeap([322, 76, 4, 7, 2, 123, 47, 1, 18, 3, 29, 199, 11])
        MaxHeap(BIG_NUMBERS)

    def test_length(self):
        from minheap import MaxHeap
        numbers = [322, 76, 4, 7, 2, 123, 47, 1, 18, 3, 29, 199, 11]
        self.assertEqual(len(MaxHeap(numbers)), len(numbers))
        self.assertEqual(len(MaxHeap(BIG_NUMBERS)), len(BIG_NUMBERS))

    def test_peek_at_largest(self):
        from minheap import MaxHeap
        numbers = [11, 322, 3, 199, 29, 7, 1, 18, 76, 4, 2, 47, 123]
        h = MaxHeap(numbers)
        self.assertEqual(h.peek(), 322)
        self.assertEqual(len(h), len(numbers))
        self.assertEqual(len(numbers), 13)
        i = MaxHeap(BIG_NUMBERS)
        self.assertEqual(i.peek(), 9740)
        self.assertEqual(len(i), len(BIG_NUMBERS))

    def test_pop_from_heap(self):
        from minheap import MaxHeap
        numbers = [11, 322, 3, 199, 29, 7, 1, 18, 76, 4, 2, 47, 123]
        h = MaxHeap(numbers)
        self.assertEqual(h.pop(), 322)
        self.assertEqual(len(h), len(numbers)-1)
        self.assertEqual(h.pop(), 199)
        self.assertEqual(h.pop(), 123)
        self.assertEqual(h.pop(), 76)
        self.assertEqual(len(h), len(numbers)-4)
        self.assertEqual(h.pop(), 47)
        self.assertEqual(h.pop(), 29)
        self.assertEqual(len(h), len(numbers)-6)
        i = MaxHeap(BIG_NUMBERS)
        self.assertEqual(i.pop(), 9740)

    def test_push_onto_heap(self):
        from minheap import MaxHeap
        numbers = [11, 322, 3, 199, 29, 7, 1, 18, 76, 4, 2, 47, 123]
        i = MaxHeap(BIG_NUMBERS)
        i.push(9999)
        self.assertEqual(i.peek(), 9999)
        i.push(9988)
        self.assertEqual(i.pop(), 9999)
        self.assertEqual(i.pop(), 9988)
        self.assertEqual(i.pop(), 9740)
        h = MaxHeap(numbers)
        h.push(144)
        self.assertEqual(len(h), len(numbers)+1)
        self.assertEqual(h.pop(), 322)
        self.assertEqual(h.pop(), 199)
        self.assertEqual(h.pop(), 144)
        self.assertEqual(h.pop(), 123)

    def test_key_function(self):
        from minheap import MaxHeap
        fruits = ['Watermelon', 'blueberry', 'lime', 'Lemon', 'pear', 'loquat']
        fruits_heap = MaxHeap(fruits, key=str.lower)
        self.assertEqual(fruits_heap.peek(), 'Watermelon')
        self.assertEqual(fruits_heap.pop(), 'Watermelon')
        self.assertEqual(fruits_heap.pop(), 'pear')
        fruits_heap.push('jujube')
        self.assertEqual(fruits_heap.pop(), 'loquat')
        self.assertEqual(fruits_heap.pop(), 'lime')
        self.assertEqual(fruits_heap.pop(), 'Lemon')
        self.assertEqual(fruits_heap.pop(), 'jujube')


class Timer:

    """Context manager to time a code block."""

    def __enter__(self):
        self.start = default_timer()
        return self

    def __exit__(self, *args):
        self.end = default_timer()
        self.elapsed = self.end - self.start


if __name__ == "__main__":
    unittest.main(verbosity=2)
