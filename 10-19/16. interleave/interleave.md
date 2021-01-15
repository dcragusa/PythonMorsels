# interleave

For this week's problem, I want you to write a function called `interleave` which accepts two iterables of any 
type and return a new iterable with each of the given items "interleaved" (item 0 from iterable 1, then item 0 
from iterable 2, then item 1 from iterable 1, and so on).

We are making an assumption here that both iterables contain the same number of elements.

Here's an example:

    >>> numbers = [1, 2, 3, 4]
    >>> interleave(numbers, range(5, 9))
    [1, 5, 2, 6, 3, 7, 4, 8]
    >>> interleave(numbers, (n**2 for n in numbers))
    [1, 1, 2, 4, 3, 9, 4, 16]

#### Bonus 1

For the first bonus, your `interleave` function should return an iterator:

    >>> i = interleave([1, 2, 3, 4], [5, 6, 7, 8])
    >>> next(i)
    1
    >>> list(i)
    [5, 2, 6, 3, 7, 4, 8]

#### Bonus 2

For second bonus your `interleave` function should accept any number of arguments:

    >>> interleave([1, 2, 3], [4, 5, 6], [7, 8, 9])
    [1, 4, 7, 2, 5, 8, 3, 6, 9]

#### Bonus 3

For the third bonus, your `interleave` function should work with iterables of different lengths. Short iterables 
should be skipped over once exhausted:

    >>> interleave([1, 2, 3], [4, 5, 6, 7, 8])
    [1, 4, 2, 5, 3, 6, 7, 8]
    >>> interleave([1, 2, 3], [4, 5], [6, 7, 8, 9])
    [1, 4, 6, 2, 5, 7, 3, 8, 9]
