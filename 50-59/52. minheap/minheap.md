# MinHeap

This week I'd like you to create a `MinHeap` class, which implements a heap data structure. Don't worry if you've 
never implemented a heap before: we're going to take this in steps. Efficiency will be important for our heap, 
but we're going to focus on the functionality we need to support first. Your `MinHeap` should accept an iterable 
of items and should allow the smallest item in the heap to be viewed (with `peek`) or removed (with `pop`).

    >>> heap = MinHeap([4, 7, 2, 3, 1, 11])
    >>> heap.pop()
    1
    >>> heap.peek()
    2
    >>> heap.pop()
    2
    >>> heap.pop()
    3

Your heap should also allow more items to be added to it with `push` and it should have a length that can be 
found with the built-in `len` function:

    >>> heap = MinHeap([4, 7, 2, 11])
    >>> heap.pop()
    2
    >>> heap.push(5)
    >>> heap.pop()
    4
    >>> heap.peek()
    5
    >>> len(heap)
    3

For the base problem, just worry about implementing a class that works like this: implement it in the most direct 
way you can, regardless of performance.

#### Bonus 1

For the first bonus, you should make sure that your heap is efficient (see heap on Wikipedia). Specifically, 
given a heap with 10,000 numbers you should be able to push 10 more numbers, and then pop 10 numbers in less 
time than it takes to sort the entire list of 10,000 numbers.

So if you have this:

    >>> from random import randint
    >>> MANY_BIG_NUMBERS = [randint(100, 1000) for n in range(10000)]
    >>> heap = MinHeap(MANY_BIG_NUMBERS)

All of these operations:

    >>> heap.push(150)
    >>> heap.push(950)
    >>> heap.push(400)
    >>> heap.push(760)
    >>> heap.push(280)
    >>> heap.push(870)
    >>> heap.push(330)
    >>> heap.push(1000)
    >>> heap.push(50)
    >>> heap.push(500)
    >>> items = [heap.pop() for _ in range(10)]

Should be faster than this operation:

    >>> MANY_BIG_NUMBERS.sort()

If you find yourself implementing very algorithmic code for this one, please check the hints. All the algorithms 
you need for this one are in the Python standard library.

#### Bonus 2

For the second bonus I'd like your heap to accept a `key` function which should work similarly to the `key` 
function accepted by Python's `sorted`, `min`, and `max` functions.

    >>> fruits = ['Watermelon', 'blueberry', 'pear', 'Lemon']
    >>> fruits_heap = MinHeap(fruits, key=str.lower)
    >>> fruits_heap.push('Apple')
    >>> fruits_heap.pop()
    >>> 'Apple'
    >>> fruits_heap.pop()
    'blueberry'

#### Bonus 3

For the third bonus I'd like you to also implement a `MaxHeap`.

This should work the same way as `MinHeap`, except the largest items should be removed instead of the smallest.

    >>> fruits = ['Watermelon', 'blueberry', 'pear', 'Lemon']
    >>> fruits_heap = MaxHeap(fruits, key=str.lower)
    >>> fruits_heap.push('lime')
    >>> fruits_heap.pop()
    'pear'
    >>> fruits_heap.pop()
    'lime'
    >>> fruits_heap.pop()
    'Lemon'
