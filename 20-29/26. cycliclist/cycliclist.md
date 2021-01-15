# CyclicList

This week I'd like you to write a class called `CyclicList` which acts sort of like a list except that looping 
over it will result in an infinite loop, repeating the list items forever.

    >>> my_list = CyclicList([1, 2, 3])
    >>> for i, n in enumerate(my_list):
    ...     print(n)
    ...     if i > 8:
    ...         break
    ...
    1
    2
    3
    1
    2
    3
    1
    2
    3
    1
    >>> from itertools import islice
    >>> list(islice(my_list, 5))
    [1, 2, 3, 1, 2]

Your `CyclicList` class should accept any iterable and when looping over a `CyclicList` object the results should 
always start at the beginning of the list.

#### Bonus 1

For the first bonus, I'd like your `CyclicList` objects to support the `len` function and to have `append` and 
`pop` methods that work like the ones on Python's lists.

    >>> my_list = CyclicList([1, 2, 3])
    >>> my_list.append(4)
    >>> my_list.pop()
    4
    >>> len(my_list)
    3
    >>> my_list.pop(0)
    1
    >>> len(my_list)
    2

#### Bonus 2

For the second bonus, I'd like you to make sure that `CyclicList` objects support `index`, which should also 
work in a cyclic manner.

    >>> my_list = CyclicList([1, 2, 3])
    >>> my_list[1]
    2
    >>> my_list[-1]
    3
    >>> my_list[5]
    3
    >>> my_list[-4]
    3

#### Bonus 3

For the third bonus, I'd like you to allow `CyclicList` objects to support cyclic slicing. I don't expect your 
slicing to support steps at all: you only need to support slices with a start and stop.

    >>> my_list = CyclicList([1, 2, 3])
    >>> my_list[-2:]
    [2, 3]
    >>> my_list[:8]
    [1, 2, 3, 1, 2, 3, 1, 2]
    >>> my_list[-2:2]
    [2, 3, 1, 2]
    >>> my_list[:-1]
    []

When slicing, you can assume that the start defaults to 0 and the stop defaults to the length of the sequence 
when the start is non-negative and 0 when the start is negative. The examples above and the tests demonstrate this.
